#!/bin/bash

sleep 1

# Set monitors (exported by arandr)
xrandr --output DP-0 --mode 2560x1440 --pos 1280x0
xrandr --output DP-4 --primary --mode 5120x1440 --pos 0x1440
# xrandr --output DP-1 --mode 2560x1440 --pos 1280x0 --rotate normal --output HDMI-1 --off --output DP-2 --off --output DP-3 --primary --mode 5120x1440 --pos 0x1440 --rotate normal --output None-1 --off

# Set wallpapers
feh --bg-fill /home/anthony/Pictures/Wallpaper/Desktop/Firewatch.jpg

# Programs to autostart
fcitx5 -d &
dunst &
redshift &
picom -b --config $HOME/.config/qtile/scripts/picom.conf &
sleep 1
