#!/bin/bash

xrandr --output DP1 --primary --mode 3440x1440 --pos 1920x240 --rotate normal
xrandr --output HDMI1 --mode 1920x1200 --pos 5360x0 --rotate left
xrandr --output eDP1 --mode 1920x1080 --pos 0x1080 --rotate normal

# Set wallpapers
feh --bg-fill /home/anthony/Pictures/Wallpapers/Poon.png

swww query || swww init &

