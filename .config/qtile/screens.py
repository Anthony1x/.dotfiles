import os
from libqtile.config import Screen
from libqtile import bar, widget
from colors import colors
# from libqtile.log_utils import logger
from libqtile.lazy import lazy

window_name = widget.WindowName()
sep = widget.Sep(linewidth = 1, paddog = 10, foreground = colors[0], background = colors[0])
groupbox = widget.GroupBox(
                    font = "JetBrainsMono Nerd Font Mono",
                    fontsize = 20,
                    margin_y = 4,
                    margin_x = 4,
                    padding_y = 6,
                    padding_x = 6,
                    borderwidth = 2,
                    disable_drag = True,
                    active = colors[2],
                    inactive = colors[10], #unfocused
                    hide_unused = True,
                    rounded = True,
                    highlight_method = "block",
                    highlight_color = colors[13],  #box color
                    this_current_screen_border = colors[0],
                    this_screen_border = colors[0],
                    other_current_screen_border = colors[13],
                    other_screen_border = colors[13],
                    urgent_alert_method = "line",
                    urgent_border = colors[6],
                    urgent_text = colors[1],
                    foreground = colors[0],
                    background = colors[0],
                    use_mouse_wheel = False
            )
weather = widget.OpenWeather(
            app_key = "4cf3731a25d1d1f4e4a00207afd451a2",
            cityid = "4997193",
            format = '{icon} {main_temp}°',
            metric = False,
            font = "JetBrainsMono Nerd Font Mono",
            fontsize = 13,
            background = colors[0],
            foreground = colors[8],
        )
tasks = widget.TaskList(
            icon_size = 13,
            font = "JetBrainsMono Nerd Font Mono",
            fontsize= 13,
            foreground = colors[0],
            background = colors[10],
            borderwidth = 0,
            border = colors[3],
            margin_y = -3,
            margin = 0,
            padding = 8,
            highlight_method = "block",
            title_width_method = "uniform",
            urgent_alert_method = "border",
            urgent_border = colors[0],
            rounded = False,
            txt_floating = "🗗 ",
            txt_maximized = "🗖 ",
            txt_minimized = "🗕 ",
        )
volicon = widget.TextBox(text = "󰕾", fontsize = 25, font = "JetBrainsMono Nerd Font Mono", foreground = colors[6], background = colors[0])
volume = widget.Volume(foreground=colors[8], padding=10, background = colors[0])
cpuicon = widget.TextBox(text = "", fontsize = 20, font = "JetBrainsMono Nerd Font Mono",  background = colors[0], foreground = colors[5])
cpu = widget.CPU(font = "JetBrainsMono Nerd Font Mono", update_interval = 1.0, format = '{load_percent}%', foreground = colors[8], background = colors[0], padding = 5)
memicon = widget.TextBox(text = "", fontsize = 20, font = "JetBrainsMono Nerd Font Mono", background = colors[0], foreground = colors[7])
mem = widget.Memory(font = "JetBrainsMono Nerd Font Mono", foreground = colors[8], background = colors[0], format = '{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}', measure_mem='G', padding = 5,)
clockicon = widget.TextBox(text = "", fontsize = 20, font = "JetBrainsMono Nerd Font Mono", background = colors[0], foreground = colors[6])
clock = widget.Clock(format='%a, %d-%m.%Y, %H:%M', font = "JetBrainsMono Nerd Font Mono", padding = 10, background = colors[0], foreground = colors[8])
curlayout = widget.CurrentLayoutIcon(scale = 0.5, foreground = colors[0], background = colors[4], padding = 10,)
tray = widget.Systray(background = colors[0])

bottom_screen_bar = bar.Bar([
            groupbox,
            sep,
            weather,
            tasks,
            sep,
            volicon,
            volume,
            cpuicon,
            cpu,
            memicon,
            mem,
            clockicon,
            clock,
            curlayout,
        ],
        margin=3,
        size=30
    )


top_screen_bar = bar.Bar([
            groupbox,
            sep,
            weather,
            tasks,
            sep,
            volicon,
            volume,
            cpuicon,
            cpu,
            memicon,
            mem,
            tray,
            sep,
            clockicon,
            clock,
            curlayout,
        ],
        margin=3,
        size=30
    )

fake_screen_layouts = [
    # 16:9 middle
    [
        Screen(bottom=top_screen_bar,x=1280,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=1280,height=1440),
        Screen(x=1280,y=1440,width=2560,height=1440),
        Screen(x=3840,y=1440,width=1280,height=1440),
    ],
    # 21:9 middle
    [
        Screen(bottom=top_screen_bar,x=0,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=840,height=1440),
        Screen(x=840,y=1440,width=3440,height=1440),
        Screen(x=4280,y=1440,width=840,height=1440),
    ],
    # 32:9, no fake screens
    [
        Screen(bottom=top_screen_bar,x=0,y=0,width=2560,height=1440),
        Screen(x=0,y=1440,width=5120,height=1440),
    ],
]

fake_screen_index = 0;
fake_screens = fake_screen_layouts[fake_screen_index]
