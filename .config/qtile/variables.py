from colors import CATPPUCCIN_MOCHA as theme
from libqtile.config import Group
from keys import keys, mod, shift, terminal
from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

# Layouts

layouts_margin = 6
layouts_border_width = 2
layouts_border_width_floating = 3
layouts_border_color = theme['disabled']
layouts_border_focus_color = theme['accent']
layouts_border_on_single = True
layouts_restore = False

layout_theme = {
    "border_width": layouts_border_width,
    "margin": layouts_margin,
    "border_focus": layouts_border_focus_color,
    "border_normal": layouts_border_color,
    "border_on_single": layouts_border_on_single
}

layout_theme_floating = {
    "border_width": layouts_border_width_floating,
    "margin": layouts_margin,
    "border_focus": layouts_border_focus_color,
    "border_normal": layouts_border_color,
    "border_on_single": layouts_border_on_single
}

# Top bar

bar_top_margin = 5
bar_bottom_margin = 5
bar_left_margin = 0
bar_right_margin = 0
bar_size = 32
bar_background_color = theme['background']
bar_foreground_color = theme['foreground']
bar_background_opacity = 0
bar_global_opacity = 1.0
bar_nerd_font = "JetbrainsMono Nerd Font"
bar_font = bar_nerd_font # "Opensans Medium"
bar_fontsize = 13.2

# Widgets

widget_gap = 6
widget_left_offset = 4
widget_right_offset = 4
widget_padding = 15

# Widgets Decorations

widget_decoration = "RectDecoration"

widget_decoration_border_width = 1
widget_decoration_border_color = theme['accent']
widget_decoration_border_opacity = 1.0
widget_decoration_border_padding_x = 0
widget_decoration_border_padding_y = 0

widget_decoration_powerline_path = "arrow_left"
widget_decoration_powerline_size = 10
widget_decoration_powerline_padding_x = 0
widget_decoration_powerline_padding_y = 0

widget_decoration_rect_filled = True
widget_decoration_rect_color = theme["alt_background"]
widget_decoration_rect_opacity = 1.0
widget_decoration_rect_border_width = 2.7
widget_decoration_rect_border_color = theme["accent"]
widget_decoration_rect_padding_x = 0
widget_decoration_rect_padding_y = 0
widget_decoration_rect_radius = 10

# Groups
groups = []

groups_count = 9
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = group_names

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout='monadtall',
            label=group_labels[i],
        ))

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Mod + number to move to that group."),
        Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group."),
        Key([mod, shift], "Tab", lazy.screen.prev_group(), desc="Move to previous group."),
        Key([mod, shift], i.name, lazy.window.togroup(i.name), desc="Move focused window to new group."),
    ])

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", f"{terminal} --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("top", f"{terminal} --class=scratch -e btop", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", f"{terminal} --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))
