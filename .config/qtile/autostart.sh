#!/bin/bash

sleep 1

# Set monitors
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    # Wayland equivalent commands using wlr-randr
    # For some reason, the outputs are different. I don't know why.
    wlr-randr --output DP-1 --mode 2560x1440 --pos 1280,0
    wlr-randr --output DP-3 --mode 5120x1440 --pos 0,1440

    # Set wallpapers
    swaybg --image ~/Pictures/Wallpaper/Desktop/city.jpg &
else
    # X11 commands
    xrandr --output DP-0 --mode 2560x1440 --pos 1280x0
    xrandr --output DP-4 --primary --mode 5120x1440 --pos 0x1440

    ~/.config/qtile/scripts/picom_toggle.sh &
    redshift &

    # Set wallpapers
    feh --bg-fill ~/Pictures/Wallpaper/Desktop/city.jpg &
fi

# Programs to autostart
fcitx5 -d &
dunst &
# npx arrpc &
sleep 1
