from libqtile import qtile
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from dotenv import set_key
from settings import (
    mod, alt, shift, control,
    terminal, menu, browser, files, screenie, region_screenie, screen_lock,
    powermenu, layout_select, scripts_dir,
    anki_screenie, anki_record, anki_replay,
    env, should_have_borders, super_disabled, is_wayland
)

# Function to toggle borders
def switch(qtile):
    new_state = not should_have_borders
    set_key(dotenv_path=env, key_to_set='BORDERS', value_to_set=str(new_state))
    qtile.reload_config()

# Function to toggle super keybindings
def switch_super(qtile):
    new_state = not super_disabled
    set_key(dotenv_path=env, key_to_set='SUPER_TOGGLE', value_to_set=str(new_state))
    qtile.reload_config()

# Toggle the bar. On Wayland the bar's redraws cost the compositor frames (qtile
    # composites and runs Python on one thread), which shows as hitches in games.
    # screens.py checks for this file when the config loads.
no_bar_flag = scripts_dir.parent / ".nobar"


def toggle_bar(qtile):
    if no_bar_flag.exists():
        no_bar_flag.unlink()
    else:
        no_bar_flag.touch()
    qtile.reload_config()


keys = [
    # Essentials (Always active)
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, shift], "Return", lazy.spawn(files)),
    Key([mod, shift], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod, shift], "left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, shift], "right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, shift], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, control], "left", lazy.prev_screen(), desc="Previous screen"),
    Key([mod, control], "right", lazy.next_screen(), desc="Next screen"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Layouts
    Key([alt], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt, shift], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

    # Super toggle (Always active)
    Key([], "XF86Tools", lazy.function(switch_super), desc="Toggle super keybindings"),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f'{scripts_dir}/volume.sh up')),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        f'{scripts_dir}/volume.sh down')),
    Key([], "XF86AudioMute", lazy.spawn(f'{scripts_dir}/volume.sh mute')),
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause')),
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous')),
    Key([], "XF86AudioNext", lazy.spawn('playerctl next')),
]

if is_wayland:
    # Ctrl+Alt+F1..F7 to switch VTs (on X11 the X server does this itself)
    for vt in range(1, 8):
        keys.append(Key(
            ["control", alt], f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}"))

# Region screenshot. X11: the script grabs the keyboard itself and waits for a
# key. Wayland has no global keyboard grab, so a key chord picks the region and
# passes it to the script instead (the hint notification is in config.py).
if is_wayland:
    region_screenie_key = KeyChord(
        [mod, alt], "s",
        [Key([], key, lazy.spawn(f"{region_screenie} --region {region}"))
         for key, region in (
            ("Up", "top"), ("w", "top"),
            ("Down", "middle"), ("s", "middle"),
            ("Left", "left"), ("a", "left"),
            ("Right", "right"), ("d", "right"),
        )],
        name="screenshot",
    )
else:
    region_screenie_key = Key([mod, alt], "s", lazy.spawn(region_screenie))

if not super_disabled:
    keys.extend([
        # Super + Letter keys (Toggleable)
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod], "f", lazy.window.toggle_floating(),
            desc="Toggle floating on the focused window"),
        Key([mod, alt], "f", lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window"),
        Key([mod, shift], "x", lazy.spawn(powermenu), desc="Open power menu"),
        Key([mod], "d", lazy.spawn(menu)),
        Key([mod], "q", lazy.spawn(browser)),
        region_screenie_key,
        Key([mod, control], "s", lazy.spawn(screenie)),
        Key([mod, alt], "l", lazy.spawn(screen_lock)),
        Key([mod, shift], "q", lazy.spawn(layout_select)),
        Key([mod, shift], "p", lazy.function(switch), desc="Switch between border and no border"),
        Key([mod], "b", lazy.function(toggle_bar), desc="Toggle the bar (off = smooth games on Wayland)"),

        Key([mod, control], "i", lazy.layout.shrink(), desc="Shrink window"),
        Key([mod, control], "o", lazy.layout.grow(), desc="Grow window"),

        # Anki recording scripts
        Key([mod], "m", lazy.spawn(anki_screenie)),
        Key([mod, shift], "m", lazy.spawn(anki_record)),
        Key([mod, control], "m", lazy.spawn(anki_replay)),
    ])

    # picom/fastcompmgr is X11-only; the Wayland compositor does its own compositing
    if not is_wayland:
        keys.append(Key([mod, control], "p", lazy.spawn(f"{scripts_dir}/picom_toggle.sh")))
