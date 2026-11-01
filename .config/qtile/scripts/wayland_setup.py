#!/usr/bin/env python3
"""
Wayland counterparts of the xrandr / feh lines in autostart.sh.

  wayland_setup.py outputs     position + set modes of the two physical monitors
  wayland_setup.py wallpaper   random wallpaper per output (like `feh --bg-fill --randomize`)

Outputs are identified by their resolution instead of their connector name, because
the names (DP-2/DP-4 on the DRM backend, X11-0 when nested, ...) are not stable.
"""

import json
import random
import shutil
import subprocess
import sys
from pathlib import Path

WALLPAPER_DIR = Path.home() / "Pictures/Wallpaper/Desktop/Minecraft"
FALLBACK_WALLPAPER = Path.home() / "Pictures/Wallpaper/Desktop/city.jpg"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

# Physical layout, must match the fake_screens geometry in screens.py:
# 32" 2560x1440 centred on top, 49" 5120x1440 below it.
TOP = {"width": 2560, "height": 1440, "pos": (1280, 0)}
BOTTOM = {"width": 5120, "height": 1440, "pos": (0, 1440)}


def get_outputs():
    try:
        out = subprocess.check_output(["wlr-randr", "--json"], text=True)
    except (OSError, subprocess.CalledProcessError) as e:
        print(f"wlr-randr failed: {e}", file=sys.stderr)
        return []
    return json.loads(out)


def best_mode(output, width, height):
    """Highest refresh rate mode with the given size, or None."""
    modes = [m for m in output.get("modes", [])
             if m["width"] == width and m["height"] == height]
    return max(modes, key=lambda m: m["refresh"], default=None)


def find_output(outputs, spec):
    for o in outputs:
        if best_mode(o, spec["width"], spec["height"]):
            return o
    return None


def setup_outputs():
    outputs = get_outputs()
    # Check the wide one first so a 5120x1440 panel is never mistaken for a 2560x1440 one
    bottom = find_output(outputs, BOTTOM)
    top = find_output([o for o in outputs if o is not bottom], TOP)
    if not (top and bottom):
        # Laptop / nested / unknown setup: leave the compositor's layout alone
        print("expected monitors not found, leaving outputs untouched")
        return

    cmd = ["wlr-randr"]
    for out, spec in ((bottom, BOTTOM), (top, TOP)):
        mode = best_mode(out, spec["width"], spec["height"])
        cmd += [
            "--output", out["name"],
            "--on",
            "--mode", f'{mode["width"]}x{mode["height"]}@{mode["refresh"]:.3f}Hz',
            "--pos", f'{spec["pos"][0]},{spec["pos"][1]}',
            "--scale", "1",
        ]
    subprocess.run(cmd, check=False)


def setup_wallpaper():
    if not shutil.which("swaybg"):
        print("swaybg not installed", file=sys.stderr)
        return

    images = sorted(p for p in WALLPAPER_DIR.iterdir()
                    if p.suffix.lower() in IMAGE_SUFFIXES) if WALLPAPER_DIR.is_dir() else []
    if not images:
        images = [FALLBACK_WALLPAPER]

    names = [o["name"] for o in get_outputs() if o.get("enabled", True)]
    if not names:
        return

    subprocess.run(["pkill", "-x", "swaybg"], check=False)

    cmd = ["swaybg"]
    for name in names:
        cmd += ["-o", name, "-i", str(random.choice(images)), "-m", "fill"]
    subprocess.Popen(cmd, start_new_session=True,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    actions = {"outputs": setup_outputs, "wallpaper": setup_wallpaper}
    if len(sys.argv) != 2 or sys.argv[1] not in actions:
        sys.exit(f"usage: {Path(sys.argv[0]).name} {{{'|'.join(actions)}}}")
    actions[sys.argv[1]]()


if __name__ == "__main__":
    main()
