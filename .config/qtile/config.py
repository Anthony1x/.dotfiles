import os
import subprocess
from libqtile import hook, qtile
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

# Import configuration modules
from settings import mod
from keys import keys
from groups import groups, group_keys
from layouts import layouts, floating_layout
from screens import fake_screens, widget_defaults, extension_defaults, screen_keys

if qtile.core.name == "wayland":
    from libqtile.backend.wayland import InputConfig

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
if qtile.core.name == "wayland":
    wl_input_rules = {
        "type:pointer": InputConfig(accel_profile='flat'),
        "type:keyboard": InputConfig(kb_layout="de"),
    }


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

wmname = "qtile"