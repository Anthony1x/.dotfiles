import os
import subprocess
from libqtile import hook, qtile
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

# Import configuration modules
from settings import (
    mod, super_disabled, is_wayland, cursor_theme, cursor_size,
    kb_layout, kb_repeat_delay, kb_repeat_rate, current_fake_screen_index,
)
from keys import keys
from groups import groups, group_keys
from layouts import layouts, floating_layout
from screens import fake_screens, widget_defaults, extension_defaults, screen_keys
from fake_screens import layout_config

if is_wayland:
    from libqtile.backend.wayland import InputConfig

    # Session environment, the Wayland counterpart of ~/.xinitrc. Everything qtile
    # spawns (autostart, keybindings) inherits this.
    os.environ.update({
        # picks portals/qtile-portals.conf (screen sharing via xdg-desktop-portal-wlr)
        "XDG_CURRENT_DESKTOP": "qtile",
        "TERMINAL": "/sbin/kitty",
        "EDITOR": "/sbin/neovide",
        "XCURSOR_THEME": cursor_theme,
        "XCURSOR_SIZE": str(cursor_size),
        # Toolkits: prefer Wayland, fall back to X11 (XWayland)
        "QT_QPA_PLATFORM": "wayland;xcb",
        "MOZ_ENABLE_WAYLAND": "1",
        "_JAVA_AWT_WM_NONREPARENTING": "1",
        # fcitx5. qtile has no text-input/input-method protocol, so Wayland-native
        # GTK/Qt apps talk to fcitx5 over D-Bus, XWayland apps via XMODIFIERS.
        "GTK_IM_MODULE": "fcitx",
        "QT_IM_MODULE": "fcitx",
        "SDL_IM_MODULE": "fcitx",
        "XMODIFIERS": "@im=fcitx",
    })
    # scripts/wayland-bin/rofi pins rofi to the primary monitor (see the script)
    wayland_bin = os.path.expanduser("~/.config/qtile/scripts/wayland-bin")
    if wayland_bin not in os.environ["PATH"].split(":"):  # config.py runs again on reload
        os.environ["PATH"] = f"{wayland_bin}:{os.environ['PATH']}"

    if os.path.isdir("/proc/driver/nvidia"):  # same as hyprland.lua
        os.environ.update({
            "LIBVA_DRIVER_NAME": "nvidia",
            "__GLX_VENDOR_LIBRARY_NAME": "nvidia",
            "NVD_BACKEND": "direct",
        })

# Aggregate keybindings
keys.extend(group_keys)
keys.extend(screen_keys)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Wayland specific config
if is_wayland:
    wl_input_rules = {
        "type:pointer": InputConfig(accel_profile='flat'),
        # kb_repeat_*: same as `xset r rate 300 40` in .xinitrc
        "type:keyboard": InputConfig(
            kb_layout=kb_layout,
            kb_repeat_delay=kb_repeat_delay,
            kb_repeat_rate=kb_repeat_rate,
        ),
    }
    # Same as Xcursor.theme / Xcursor.size in .Xresources
    wl_xcursor_theme = cursor_theme
    wl_xcursor_size = cursor_size

    @hook.subscribe.enter_chord
    def region_screenshot_hint(chord_name):
        """Wayland replacement for the notification region_screenshot.py shows on X11."""
        if chord_name == "screenshot":
            name = layout_config[min(current_fake_screen_index, len(layout_config) - 1)]["name"]
            subprocess.Popen([
                "dunstify", "--timeout=5000", "Screenshot Region",
                f"{name} layout — ↑/W top · ←/A left · ↓/S middle · →/D right · Esc cancel",
            ])


@hook.subscribe.startup_once
def autostart():
    # QTILE_NO_AUTOSTART=1 is handy for testing (e.g. a nested session) without
    # launching a second copy of every daemon.
    if os.environ.get("QTILE_NO_AUTOSTART"):
        return
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

wmname = "qtile"