from pathlib import Path
from dotenv import get_key
from colors import CATPPUCCIN_MOCHA as theme

# Paths
home: Path = Path.home()
env: Path = home / ".config/qtile/.env"
scripts_dir: Path = home / ".config/qtile/scripts"

# Mod Keys
mod: str = "mod4"
alt: str = "mod1"
shift: str = "shift"
control: str = "control"

# Applications
terminal: str = "kitty"
menu: str = "rofi -show drun"
browser: str = "floorp"
files: str = "thunar"
screenie: str = "flameshot gui"
screen_lock: str = "betterlockscreen -l"
powermenu: str = "rofi -show power-menu -modi power-menu://home/anthony/dotfiles/.config/rofi/scripts//rofi-power-menu"
layout_select: str = "/home/anthony/.config/rofi/scripts/select_layout.sh"

# Anki
anki_menu: str = "/home/anthony/.config/rofi/scripts/anki.sh"
anki_screenie: str = "/home/anthony/Documents/Dev/vn-cards/capture.sh"
anki_record: str = f"{anki_screenie} --record"
anki_replay: str = "/home/anthony/Documents/Dev/vn-cards/audio-replay-save.sh"

# State & Environment
should_have_borders: bool = (get_key(dotenv_path=env, key_to_get='BORDERS')) == "True"
workstation: str | None = get_key(dotenv_path=env, key_to_get="WORKSTATION")
current_fake_screen_index: int = int(get_key(dotenv_path=env, key_to_get="FAKE_SCREEN_INDEX") or 0)

# Layout Themes
layouts_margin: int = 6 if should_have_borders else 0
layouts_border_width: int = 2 if should_have_borders else 0
layouts_border_width_floating: int = 3
layouts_border_color: str = theme['disabled']
layouts_border_focus_color: str = theme['accent']
layouts_border_on_single: bool = True

layout_theme: dict = {
    "border_width": layouts_border_width,
    "margin": layouts_margin,
    "border_focus": layouts_border_focus_color,
    "border_normal": layouts_border_color,
    "border_on_single": layouts_border_on_single
}

layout_theme_floating: dict = {
    "border_width": layouts_border_width_floating,
    "margin": layouts_margin,
    "border_focus": layouts_border_focus_color,
    "border_normal": layouts_border_color,
    "border_on_single": layouts_border_on_single
}

# Bar Styling
bar_top_margin: int = 3
bar_bottom_margin: int = 8
bar_left_margin: int = layouts_margin
bar_right_margin: int = layouts_margin
bar_size: int = 32
bar_background_color: str = theme['background']
bar_foreground_color: str = theme['foreground']
bar_background_opacity: float = 0.0
bar_global_opacity: float = 1.0
bar_nerd_font: str = "JetbrainsMono Nerd Font"
bar_font: str = bar_nerd_font
bar_fontsize: float = 13.2

# Widget Styling
widget_gap: int = 6
widget_left_offset: int = 4
widget_right_offset: int = 4
widget_padding: int = 15

widget_decoration_rect_filled: bool = True
widget_decoration_rect_color: str = theme["alt_background"]
widget_decoration_rect_opacity: float = 1.0
widget_decoration_rect_border_width: int = 2
widget_decoration_rect_border_color: str = theme["accent"]
widget_decoration_rect_padding_x: int = 0
widget_decoration_rect_padding_y: int = 0
widget_decoration_rect_radius: int = 10