from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import qtile

mod = "mod4"
alt = "mod1"
shift = "shift"

terminal = "kitty"
mymenu = "rofi -show drun"
browser = "brave"
files = "thunar"
screenie = "flameshot gui"

screen_lock = "betterlockscreen -l"
scripts_dir = "/home/anthony/.config/qtile/scripts"
shutdown_command = "rofi -show power-menu -modi power-menu:/home/anthony/.local/bin/rofi-power-menu"

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, alt], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod, shift], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, shift], "x", lazy.spawn(shutdown_command), desc="Open power menu"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn(mymenu)),
    Key([mod], "q", lazy.spawn(browser)),
    Key([mod, shift], "Return", lazy.spawn(files)),
    Key([mod, alt], "s", lazy.spawn(screenie)),
    Key([mod, alt], "o", lazy.spawn(f"{scripts_dir}/picom_toggle.sh")),
    Key([mod, alt], "l", lazy.spawn(screen_lock)),

    # Movement Keys
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, shift], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, shift], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, shift], "up", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "down", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),

    # Layouts
    Key([alt], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt, shift], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%')),
    Key([], "XF86AudioMute", lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause')),
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous')),
    Key([], "XF86AudioNext", lazy.spawn('playerctl next')),
]

# Scratchpad keybindings
keys.extend([
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod, shift], "n", lazy.group['scratchpad'].dropdown_toggle('top')),
])

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", alt],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
