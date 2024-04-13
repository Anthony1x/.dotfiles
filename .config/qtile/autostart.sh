#!/bin/bash

# Set monitors (exported by arandr)
xrandr --output DP-0 --mode 2560x1440 --pos 1280x0
xrandr --output DP-4 --primary --mode 5120x1440 --pos 0x1440

# Set wallpapers
feh --bg-fill /home/anthony/Pictures/Wallpaper/Desktop/Catppuccin.png

swww query || swww init &

