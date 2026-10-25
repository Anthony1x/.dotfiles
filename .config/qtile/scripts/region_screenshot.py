#!/usr/bin/env python3
"""
Region screenshot: capture full screen, wait for arrow/wasd key,
crop the selected region based on the active fake_screen layout,
open in satty. Uses ctypes + libX11 for keyboard grabbing.
"""

import ctypes
import os
import subprocess
import re
import sys
import tempfile
from pathlib import Path

# ── X11 key constants ──
XK_Up     = 0xFF52
XK_Down   = 0xFF54
XK_Left   = 0xFF51
XK_Right  = 0xFF53
XK_w      = 0x77
XK_W      = 0x57
XK_a      = 0x61
XK_A      = 0x41
XK_s      = 0x73
XK_S      = 0x53
XK_d      = 0x64
XK_D      = 0x44
XK_Escape = 0xFF1B

# ── Fake screen layout config (mirrors fake_screens.py) ──
LAYOUT_CONFIG = [
    {"name": "16:9 middle",          "width": 2560, "screens": 3},
    {"name": "YouTube optimized",    "width": 2250, "screens": 3},
    {"name": "18:9 middle",          "width": 2880, "screens": 3},
    {"name": "4:3 middle",           "width": 1920, "screens": 3},
    {"name": "1/3 each",             "width": 1706, "screens": 3},
    {"name": "21:9 + 11:9",          "width": 3440, "screens": 2},
    {"name": "11:9 + 21:9",          "width": 1680, "screens": 2},
    {"name": "21:9 middle",          "width": 3440, "screens": 3},
    {"name": "2x 16:9 side by side", "width": 2560, "screens": 2},
    {"name": "32:9, no fake screens", "width": 5120, "screens": 1},
]

BOTTOM_W = 5120
BOTTOM_H = 1440
BOTTOM_Y = 1440  # y offset of the bottom monitor


class XKeyEvent(ctypes.Structure):
    _fields_ = [
        ("type",        ctypes.c_int),
        ("serial",      ctypes.c_ulong),
        ("send_event",  ctypes.c_int),
        ("display",     ctypes.c_void_p),
        ("window",      ctypes.c_ulong),
        ("root",        ctypes.c_ulong),
        ("subwindow",   ctypes.c_ulong),
        ("time",        ctypes.c_ulong),
        ("x",           ctypes.c_int),
        ("y",           ctypes.c_int),
        ("x_root",      ctypes.c_int),
        ("y_root",      ctypes.c_int),
        ("state",       ctypes.c_uint),
        ("keycode",     ctypes.c_uint),
        ("same_screen", ctypes.c_int),
    ]


def read_fake_screen_index():
    env_path = Path.home() / ".config/qtile/.env"
    try:
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("FAKE_SCREEN_INDEX"):
                    val = line.split("=", 1)[1].strip().strip("'\"")
                    return int(val)
    except (OSError, ValueError):
        pass
    return 0


def find_top_monitor():
    """Find the top monitor via xrandr. Returns (x, y, w, h) or None."""
    out = subprocess.check_output(["xrandr"], text=True)
    monitors = []
    for line in out.splitlines():
        if " connected" not in line:
            continue
        m = re.search(r"(\d+)x(\d+)\+(\d+)\+(\d+)", line)
        if m:
            w, h, x, y = map(int, m.groups())
            monitors.append((x, y, w, h))

    if not monitors:
        return None

    # The top monitor is the one with the smallest y (and smaller width)
    sorted_by_y = sorted(monitors, key=lambda m: m[1])
    top = sorted_by_y[0]

    # If the first by y is actually the wider/bottom one, swap
    if top[2] >= 2560 and len(monitors) > 1:
        for m in monitors:
            if m[2] < top[2]:
                top = m
                break

    return top


def compute_regions(config):
    """Compute capture regions from the active fake_screen layout config."""
    width = config["width"]
    screens = config["screens"]

    top = find_top_monitor()
    if top is None:
        top = (1280, 0, 2560, 1440)  # fallback

    regions = {
        "top": f"{top[2]}x{top[3]}+{top[0]}+{top[1]}",
    }

    if screens == 3:
        side = (BOTTOM_W - width) // 2
        regions["left"]   = f"{side}x{BOTTOM_H}+0+{BOTTOM_Y}"
        regions["middle"] = f"{width}x{BOTTOM_H}+{side}+{BOTTOM_Y}"
        regions["right"]  = f"{side}x{BOTTOM_H}+{side + width}+{BOTTOM_Y}"

    elif screens == 2:
        regions["left"]  = f"{width}x{BOTTOM_H}+0+{BOTTOM_Y}"
        regions["right"] = f"{BOTTOM_W - width}x{BOTTOM_H}+{width}+{BOTTOM_Y}"
        regions["middle"] = f"{BOTTOM_W}x{BOTTOM_H}+0+{BOTTOM_Y}"  # full bottom

    elif screens == 1:
        full = f"{BOTTOM_W}x{BOTTOM_H}+0+{BOTTOM_Y}"
        regions["left"] = full
        regions["middle"] = full
        regions["right"] = full

    return regions


# ── X11 keyboard grab ──

def grab_key_x11():
    lib = ctypes.CDLL("libX11.so.6")

    lib.XOpenDisplay.restype = ctypes.c_void_p
    lib.XOpenDisplay.argtypes = [ctypes.c_char_p]
    lib.XDefaultRootWindow.restype = ctypes.c_ulong
    lib.XDefaultRootWindow.argtypes = [ctypes.c_void_p]
    lib.XGrabKeyboard.restype = ctypes.c_int
    lib.XGrabKeyboard.argtypes = [
        ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int,
        ctypes.c_int, ctypes.c_int, ctypes.c_ulong,
    ]
    lib.XNextEvent.restype = ctypes.c_int
    lib.XNextEvent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    lib.XUngrabKeyboard.restype = ctypes.c_int
    lib.XUngrabKeyboard.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    lib.XCloseDisplay.restype = ctypes.c_int
    lib.XCloseDisplay.argtypes = [ctypes.c_void_p]
    lib.XLookupKeysym.restype = ctypes.c_ulong
    lib.XLookupKeysym.argtypes = [ctypes.c_void_p, ctypes.c_int]

    GrabModeAsync = 1
    CurrentTime = 0

    display = lib.XOpenDisplay(None)
    if not display:
        return XK_Escape

    root = lib.XDefaultRootWindow(display)
    status = lib.XGrabKeyboard(
        display, root, True, GrabModeAsync, GrabModeAsync, CurrentTime,
    )
    if status != 0:
        lib.XCloseDisplay(display)
        return XK_Escape

    event = XKeyEvent()
    while True:
        lib.XNextEvent(display, ctypes.byref(event))
        if event.type == 2:
            break

    keysym = lib.XLookupKeysym(ctypes.byref(event), 0)
    lib.XUngrabKeyboard(display, CurrentTime)
    lib.XCloseDisplay(display)
    return keysym


def notify(msg):
    subprocess.run(
        ["dunstify", "--timeout=5000", "Screenshot Region", msg],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


# ── Main ──

def main():
    index = read_fake_screen_index()
    if index >= len(LAYOUT_CONFIG):
        index = 0

    config = LAYOUT_CONFIG[index]
    regions = compute_regions(config)

    # 1. Take full screenshot
    tmp = os.path.join(tempfile.gettempdir(), "qtile_region_screenshot.png")
    subprocess.run(["maim", "--hidecursor", tmp], check=True)

    # 2. Notify
    name = config["name"]
    notify(f"{name} layout — ↑/W top · ←/A left · ↓/S middle · →/D right · Esc cancel")

    # 3. Wait for key
    KEY_TO_REGION = {
        XK_Up:    "top",
        XK_w:     "top",
        XK_W:     "top",
        XK_Down:  "middle",
        XK_s:     "middle",
        XK_S:     "middle",
        XK_Left:  "left",
        XK_a:     "left",
        XK_A:     "left",
        XK_Right: "right",
        XK_d:     "right",
        XK_D:     "right",
    }

    keysym = grab_key_x11()
    region_key = KEY_TO_REGION.get(keysym)

    # 4. Crop and open
    if region_key and region_key in regions:
        geometry = regions[region_key]
        subprocess.run(
            f"convert {tmp} -crop {geometry} png:- | satty --filename - --fullscreen",
            shell=True,
        )

    try:
        os.remove(tmp)
    except OSError:
        pass


if __name__ == "__main__":
    main()
