from libqtile.config import Key
from libqtile.lazy import lazy
from dotenv import set_key
from settings import (
    mod, alt, shift, control,
    terminal, menu, browser, files, screenie, screen_lock,
    powermenu, layout_select, scripts_dir,
    anki_screenie, anki_record, anki_replay,
    env, should_have_borders
)

# Function to toggle borders
def switch(qtile):
    new_state = not should_have_borders
    set_key(dotenv_path=env, key_to_set='BORDERS', value_to_set=str(new_state))
    qtile.reload_config()

keys = [
    # Essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, alt], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window"),
    Key([mod, shift], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, shift], "x", lazy.spawn(powermenu), desc="Open power menu"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn(menu)),
    Key([mod], "q", lazy.spawn(browser)),
    Key([mod, shift], "Return", lazy.spawn(files)),
    Key([mod, alt], "s", lazy.spawn(screenie)),
    Key([mod, control], "p", lazy.spawn(f"{scripts_dir}/picom_toggle.sh")),
    Key([mod, alt], "l", lazy.spawn(screen_lock)),
    Key([mod, shift], "q", lazy.spawn(layout_select)),
    
    # Border toggle
    Key([mod, shift], "p", lazy.function(switch), desc="Switch between border and no border"),

    # Movement Keys
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

    Key([mod, control], "i", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, control], "o", lazy.layout.grow(), desc="Grow window"),

    Key([mod, control], "left", lazy.previous_screen(), desc="Previous screen"),
    Key([mod, control], "right", lazy.next_screen(), desc="Next screen"),

    # Layouts
    Key([alt], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt, shift], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f'{scripts_dir}/volume.sh up')),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        f'{scripts_dir}/volume.sh down')),
    Key([], "XF86AudioMute", lazy.spawn(f'{scripts_dir}/volume.sh mute')),
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause')),
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous')),
    Key([], "XF86AudioNext", lazy.spawn('playerctl next')),

    # Anki recording scripts
    Key([mod], "m", lazy.spawn(anki_screenie)),
    Key([mod, shift], "m", lazy.spawn(anki_record)),
    Key([mod, control], "m", lazy.spawn(anki_replay)),
]