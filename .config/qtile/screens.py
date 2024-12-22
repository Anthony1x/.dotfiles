from keys import terminal
from libqtile.config import Screen
from libqtile import bar, qtile
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from dotenv import set_key
from keys import keys, mod, shift
from libqtile.config import Key
from libqtile.lazy import lazy
from dotenv import get_key
from pathlib import Path
from colors import CATPPUCCIN_MOCHA as theme
from variables import bar_font, group_names, group_labels, widget_decoration_rect_border_color, \
    widget_decoration_rect_color, widget_decoration_rect_opacity, widget_decoration_rect_border_width, \
    widget_decoration_rect_filled, widget_decoration_rect_padding_x, widget_decoration_rect_padding_y, \
    widget_decoration_rect_radius, widget_gap, widget_left_offset, widget_padding, widget_right_offset, \
    bar_background_color, bar_background_opacity, bar_bottom_margin, bar_fontsize, bar_foreground_color, \
    bar_global_opacity, bar_left_margin, bar_right_margin, bar_size, bar_top_margin, layouts_margin


class WidgetTweaker:
    def __init__(self, func):
        self.format = func


@WidgetTweaker
def groupBox(output):
    index = group_names.index(output)
    label = group_labels[index]

    return label


@WidgetTweaker
def volume(output):
    if output.endswith('%'):
        volume = int(output[:-1])

        icons = {
            range(0, 33): '󰕿 ',
            range(33, 66): '󰖀 ',
            range(66, 101): '󰕾 '
        }

        icon = icons[next(filter(lambda r: volume in r, icons.keys()))]

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
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
            terminal + ' -e btop')},
        measure_mem='M',
        format='{MemUsed: .0f}{mm}',
        fmt=' {} ',
    ),
    widget.Memory(
        padding=5,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
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

# --- SCREEN INDEX SHIFT START --- #

env = Path('/home/anthony/.config/qtile/.env')
current_index = int(get_key(dotenv_path=env, key_to_get="FAKE_SCREEN_INDEX"))


def next_layout(qtile):
    global env, current_index

    current_index += 1
    if current_index >= len(fake_screen_layouts):
        current_index = 0

    set_key(dotenv_path=env, key_to_set="FAKE_SCREEN_INDEX",
            value_to_set=str(current_index))

    qtile.reload_config()


def prev_layout(qtile):
    global env, current_index

    current_index -= 1
    if current_index < 0:
        # Loop back to the last layout if going below 0
        current_index = len(fake_screen_layouts) - 1
    set_key(dotenv_path=env, key_to_set="FAKE_SCREEN_INDEX",
            value_to_set=str(current_index))

    qtile.reload_config()


keys.extend([
    #  Switch super-ultrawide monitor layout
    Key([mod, shift], "o", lazy.function(next_layout)),
    Key([mod, shift], "i", lazy.function(prev_layout)),
])

# --- SCREEN INDEX SHIFT END --- #

bar = bar.Bar(
    widgets=left_offset + left + sep + middle + sep + right + right_offset,
    size=bar_size,
    background=bar_background_color +
    format(int(bar_background_opacity * 255), "02x"),
    margin=[bar_top_margin, bar_right_margin,
            bar_bottom_margin-layouts_margin, bar_left_margin],
    opacity=bar_global_opacity
)

workstation = get_key(dotenv_path=env, key_to_get="WORKSTATION")

if (workstation == "PC"):
    fake_screen_layouts = [
        # 16:9 middle
        [
            Screen(bottom=bar, x=1280, y=0, width=2560, height=1440),
            Screen(x=0, y=1440, width=1280, height=1440),
            Screen(x=1280, y=1440, width=2560, height=1440),
            Screen(x=3840, y=1440, width=1280, height=1440),
        ],
        # 21:9 + 11:9
        [
            Screen(bottom=bar, x=1280, y=0, width=2560, height=1440),
            Screen(x=0, y=1440, width=3440, height=1440),
            Screen(x=3440, y=1440, width=1680, height=1440),
        ],
        # 2x 16:9 side by side
        [
            Screen(bottom=bar, x=1280, y=0, width=2560, height=1440),
            Screen(x=0, y=1440, width=2560, height=1440),
            Screen(x=2560, y=1440, width=2560, height=1440),
        ],
        # 32:9, no fake screens
        [
            Screen(bottom=bar, x=1280, y=0, width=2560, height=1440),
            Screen(x=0, y=1440, width=5120, height=1440),
        ],
    ]
else:
    fake_screen_layouts = [
        Screen(top=bar, x=0, y=0, width=2560, height=1440)
    ]

fake_screens = fake_screen_layouts[current_index]
