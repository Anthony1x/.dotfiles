from libqtile.config import Screen
from libqtile import bar, qtile
from colors import colors, Gruvbox
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from keys import terminal

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
            distro="Arch_yay",
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
            format = "⏱  %a, %b %d - %I:%M:%S %p",
        ),
        widget.Spacer(
            **decor_right,
            foreground="#08080c99",
        ),
        widget.Net(
            **decor_right,
            #background='#303F9F'+'.8',
            background=Gruvbox['shade1'],
            #foreground = colors[1],
            format='{down:.0f}{down_suffix} ↓↑',
            padding=10
        ),
        widget.CPU(
            **decor_right,
            format = ' {load_percent}%',
            #foreground = colors[4],
            background=Gruvbox['shade2'],
            padding=10,
        ),
         widget.Memory(
            **decor_right,
            padding=10,
            background=Gruvbox['shade3'],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
            measure_mem='M',
            format = '{MemUsed: .0f}{mm}',
            fmt = ' {} used',
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade5'],
            fmt = ' {}',
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade6'],
            channel='Capture',
            #foreground = colors[7],
            fmt = ' {}',
        ),
        widget.CurrentLayoutIcon(
            **decor_left,
            #background="#ffffff.7",
            #background=Gruvbox['red']+".7",
            background='#FF5E5E'+'.7',
            padding = 2,
            scale = 0.6,
            foreground = colors[1],
        ),
        widget.CurrentLayout(
            **decor_left,
            background='#FF5E5E'+'.7',
            #foreground = colors[1],
            padding = 5
        ),
        widget.Systray(
            **decor_right,
            background=Gruvbox['shade8'],
            padding = 3
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


fake_screen_layouts = [
    # 16:9 middle
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(),background=tsBgColor, size=26),x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=1280,height=1440),
        Screen(x=1280,y=1440,width=2560,height=1440),
        Screen(x=3840,y=1440,width=1280,height=1440),
    ],
    # 21:9 middle
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(),background=tsBgColor, size=26),x=0,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=840,height=1440),
        Screen(x=840,y=1440,width=3440,height=1440),
        Screen(x=4280,y=1440,width=840,height=1440),
    ],
    # 32:9, no fake screens
    [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(),background=tsBgColor, size=26),x=0,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=5120,height=1440),
    ],
]

fake_screen_index = 0;
fake_screens = fake_screen_layouts[fake_screen_index]
