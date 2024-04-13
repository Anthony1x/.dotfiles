from typing import List  # noqa: F401
import os
import subprocess
from os import path

from libqtile import layout, hook
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match
from libqtile.lazy import lazy
from screens import fake_screens
from keys import mod
from groups import groups
from layouts import layouts, floating_layout

groups = groups
layouts = layouts
floating_layout = floating_layout
fake_screens = fake_screens

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"
