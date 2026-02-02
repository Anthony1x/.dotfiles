from typing import Any
from libqtile.bar import Bar
from libqtile import bar, qtile
from libqtile.config import Screen, Key
from libqtile.lazy import lazy
from qtile_extras import widget
from dotenv import set_key

from settings import (
    theme, env, current_fake_screen_index, workstation, terminal,
    bar_font, bar_fontsize, bar_foreground_color, bar_background_color,
    bar_background_opacity, bar_global_opacity, bar_size,
    bar_top_margin, bar_bottom_margin, bar_left_margin, bar_right_margin,
    layouts_margin,
    widget_gap, widget_padding, widget_left_offset, widget_right_offset,
    widget_decoration_rect_filled, widget_decoration_rect_color,
    widget_decoration_rect_opacity, widget_decoration_rect_border_width,
    widget_decoration_rect_border_color, widget_decoration_rect_padding_x,
    widget_decoration_rect_padding_y, widget_decoration_rect_radius,
    mod, shift
)
from groups import group_names, group_labels
from fake_screens import layout_config


class WidgetTweaker:
    def __init__(self, func):
        self.format = func


group_map = dict(zip(group_names, group_labels))


@WidgetTweaker
def groupBox(output):
    return group_map.get(output, output)


@WidgetTweaker
def volume(output: str):
    if output.endswith('%'):
        volume = int(output[:-1])

        icons = {
            range(0, 33): '󰕿 ',
            range(33, 66): '󰖀 ',
            range(66, 101): '󰕾 '
        }

        try:
            icon = icons[next(filter(lambda r: volume in r, icons.keys()))]
        except StopIteration:
            icon = '󰕾 '

        return icon + output
    elif output == 'M':
        return '󰕿 Muted'
    else:
        return output


decorations = {
    "RectDecoration": {
        "group": True,
        "filled": widget_decoration_rect_filled,
        "colour": widget_decoration_rect_color + format(int(widget_decoration_rect_opacity * 255), "02x"),
        "line_width": widget_decoration_rect_border_width,
        "line_colour": widget_decoration_rect_border_color,
        "padding_x": widget_decoration_rect_padding_x,
        "padding_y": widget_decoration_rect_padding_y,
        "radius": widget_decoration_rect_radius,
    }
}

decoration = [getattr(widget.decorations, 'RectDecoration')
              (**decorations['RectDecoration'])]

widget_defaults = dict(
    font=bar_font,
    foreground=bar_foreground_color,
    fontsize=bar_fontsize,
    padding=widget_padding,
    decorations=decoration
)

extension_defaults = widget_defaults.copy()

sep = [widget.WindowName(foreground="#00000000", fmt="", decorations=[])]
left_offset = [widget.Spacer(length=widget_left_offset, decorations=[])]
right_offset = [widget.Spacer(length=widget_right_offset, decorations=[])]
space = widget.Spacer(length=widget_gap, decorations=[])

left = [
    widget.GroupBox(
        font=f"{bar_font} Bold",
        disable_drag=True,
        fontsize=15,
        inactive=theme['disabled'],
        active=bar_foreground_color,
        block_highlight_text_color=theme['accent'],
        padding=7,
        fmt=groupBox,
        highlight_color="#00000000",
        highlight_method="line",
        this_current_screen_border=theme['highlight'],
        this_screen_border='00000000',
        other_current_screen_border=theme['highlight'],
        other_screen_border='00000000',
    ),
]

middle = [
    widget.Clock(
        format="%a, %b %d - %H:%M",
    )
]

right = [
    widget.Net(
        format='↓{down:.0f}{down_suffix} ↑{up:.0f}{up_suffix}',
        padding=5,
    ),
    widget.CPU(
        format=' {load_percent}%',
        padding=5,
    ),
    widget.Memory(
        padding=5,
        mouse_callbacks={'Button1': lambda: qtile.spawn(
            terminal + ' -e btop')},
        measure_mem='M',
        format='{MemUsed: .0f}{mm}',
        fmt=' {} ',
    ),
    widget.Memory(
        padding=5,
        mouse_callbacks={'Button1': lambda: qtile.spawn(
            terminal + ' -e btop')},
        measure_mem='M',
        format='{SwapUsed: .0f}{mm}',
        fmt='󰾵{} ',
    ),
    space,
    widget.Volume(
        step=2,
        padding=10,
        fmt=volume,
        mouse_callbacks={'Button1': lazy.spawn(
            'pactl set-sink-mute @DEFAULT_SINK@ toggle')},
    ),
    widget.Volume(
        padding=10,
        fmt=' {}',
        channel='Capture',
    ),
    space,
    widget.StatusNotifier(),
]

bar_instance: Bar = bar.Bar(
    widgets=left_offset + left + sep + middle + sep + right + right_offset,
    size=bar_size,
    background=bar_background_color +
    format(int(bar_background_opacity * 255), "02x"),
    margin=[0, layouts_margin,
            layouts_margin, layouts_margin],
    opacity=bar_global_opacity
)

# Screens Logic

top_screen = Screen(bottom=bar_instance, x=1280, y=0, width=2560, height=1440)


def generate_layout(width, screens=3):
    if screens == 3:
        side_width = (5120 - width) // 2
        return [
            top_screen,
            Screen(x=0, y=1440, width=side_width, height=1440),
            Screen(x=side_width, y=1440, width=width, height=1440),
            Screen(x=side_width + width, y=1440, width=side_width, height=1440),
        ]
    elif screens == 2:
        return [
            top_screen,
            Screen(x=0, y=1440, width=width, height=1440),
            Screen(x=width, y=1440, width=5120 - width, height=1440),
        ]
    elif screens == 1:
        return [
            top_screen,
            Screen(x=0, y=1440, width=5120, height=1440),
        ]


fake_screen_layouts = [
    generate_layout(layout["width"], layout["screens"]) for layout in layout_config
] if (workstation == "PC") else [Screen(top=bar_instance, x=0, y=0, width=2560, height=1440)]

fake_screens = fake_screen_layouts[current_fake_screen_index if (workstation == "PC") else 0]

# Screen Index Shift Logic

def next_layout(qtile):
    new_index = current_fake_screen_index + 1
    if new_index >= len(fake_screen_layouts):
        new_index = 0

    set_key(dotenv_path=env, key_to_set="FAKE_SCREEN_INDEX",
            value_to_set=str(new_index))

    qtile.reload_config()


def prev_layout(qtile):
    new_index = current_fake_screen_index - 1
    if new_index < 0:
        new_index = len(fake_screen_layouts) - 1

    set_key(dotenv_path=env, key_to_set="FAKE_SCREEN_INDEX",
            value_to_set=str(new_index))

    qtile.reload_config()

screen_keys = [
    Key([mod, shift], "o", lazy.function(next_layout)),
    Key([mod, shift], "i", lazy.function(prev_layout)),
]
