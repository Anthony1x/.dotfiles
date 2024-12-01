from libqtile.config import Screen
from libqtile import bar, qtile
from colors import colors, Gruvbox
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from keys import terminal
from dotenv import set_key
from keys import keys, mod, shift
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import qtile
from dotenv import get_key
from pathlib import Path

font = "JetbrainsMono Nerd Font"


decor_left = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash"
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash"
        )
    ],
}

tsBgColor = '#08080c99' #'#0d0d1399'

c = "#282c34"
def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            **decor_left,
            fontsize = 11,
            font = font,
            margin_y = 5,
            margin_x = 5,
            padding_y = 0,
            padding_x = 1,
            borderwidth = 3,
            active = colors[8],
            inactive = colors[1],
            rounded = False,
            hide_unused = True,
            highlight_color = colors[2],
            highlight_method = "line",
            this_current_screen_border = colors[7],
            this_screen_border = colors [4],
            other_current_screen_border = colors[7],
            other_screen_border = colors[4],
        ),
        widget.CheckUpdates(
            **decor_left,
            fmt=" {}",
            foreground="000000.8",
            font = font,
            distro="Arch_paru",
            update_interval=900,
            colour_have_updates=colors[4],
            colour_no_updates=colors[4],
        ),
        widget.WindowName(
            **decor_left,
            max_chars=40,
            #background=Gruvbox['blue']+'.2',
            #background=Color2+".4",
            foreground = colors[6],
            width=555,
            padding=5,
            font = font,
            background="#08080c99",
        ),
        widget.Spacer(
            **decor_right,
            foreground="#08080c99",
        ),
        widget.Clock(
            **decor_left,
            padding=10,
            background=Gruvbox['shade5'],
            #foreground = colors[4],
            format = "%a, %b %d - %H:%M 󰥔",
            font = font,
        ),
        widget.Spacer(
            **decor_right,
            foreground="#08080c99",
            font = font,
        ),
        widget.Net(
            **decor_right,
            #background='#303F9F'+'.8',
            background=Gruvbox['shade1'],
            #foreground = colors[1],
            format='{down:.0f}{down_suffix} ↓ {up:.0f}{up_suffix}↑',
            padding=10,
            font = font,
        ),
        widget.CPU(
            **decor_right,
            format = '{load_percent}% ',
            #foreground = colors[4],
            background=Gruvbox['shade2'],
            padding=10,
            font = font,
        ),
         widget.Memory(
            **decor_right,
            padding=10,
            background=Gruvbox['shade3'],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
            measure_mem='M',
            format = '{MemUsed: .0f}{mm}',
            fmt = '{} used  ',
            font = font,
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade5'],
            fmt = '{}  ',
            font = font,
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade6'],
            channel='Capture',
            #foreground = colors[7],
            font = font,
            fmt = '{} ',
        ),
        widget.CurrentLayout(
            **decor_left,
            background='#FF5E5E'+'.7',
            font = font,
            #foreground = colors[1],
            # padding = 2
        ),
        widget.Systray(
            **decor_right,
            font = font,
            #background=Gruvbox['shade8'],
            padding = 5
        ),
    ]

    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2

# --- SCREEN INDEX SHIFT START --- #

file = Path('/home/anthony/.config/qtile/.env')
current_index = int(get_key(dotenv_path=file, key_to_get="FAKE_SCREEN_INDEX"))

def next_layout(qtile):
    global file, current_index

    current_index += 1
    if current_index >= len(fake_screen_layouts):
        current_index = 0

    set_key(dotenv_path=file, key_to_set="FAKE_SCREEN_INDEX", value_to_set=str(current_index))

    qtile.reload_config()

def prev_layout(qtile):
    global file, current_index

    current_index -= 1
    if current_index < 0:
        current_index = len(fake_screen_layouts) - 1  # Loop back to the last layout if going below 0
    set_key(dotenv_path=file, key_to_set="FAKE_SCREEN_INDEX", value_to_set=str(current_index))

    qtile.reload_config()

keys.extend([
    #  Switch super-ultrawide monitor layout
    Key([mod, shift], "o", lazy.function(next_layout)),
    Key([mod, shift], "i", lazy.function(prev_layout)),
])

# --- SCREEN INDEX SHIFT END --- #

fake_screen_layouts = [
    # 16:9 middle
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), background=tsBgColor, size=26),x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=1280,height=1440),
        Screen(x=1280,y=1440,width=2560,height=1440),
        Screen(x=3840,y=1440,width=1280,height=1440),
    ],
    # 21:9 + 11:9
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), background=tsBgColor, size=26),x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=3440,height=1440),
        Screen(x=3440,y=1440,width=1680,height=1440),
    ],
    # 2x 16:9 side by side
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), background=tsBgColor, size=26),x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=2560,height=1440),
        Screen(x=2560,y=1440,width=2560,height=1440),
    ],
    # 32:9, no fake screens
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), background=tsBgColor, size=26),x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=5120,height=1440),
    ],
]

fake_screens = fake_screen_layouts[current_index]
