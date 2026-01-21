#!/bin/bash

sleep 1

export XCURSOR_PATH="catppuccin-mocha-dark-cursors"
export QT_QPA_PLATFORMTHEME="qt6ct"

# Set monitors
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then

    # Wayland equivalent commands using wlr-randr
    # For some reason, the outputs are different. I don't know why.
    wlr-randr --output DP-1 --mode 2560x1440 --pos 1280,0
    wlr-randr --output DP-3 --mode 5120x1440 --pos 0,1440

    # Set wallpapers
    swaybg --image ~/Pictures/Wallpaper/Desktop/city.jpg &

    gammastep-indicator -c ~/.config/gammastep/gammastep.conf &
else
    # X11 commands
    xrandr --output DP-0 --mode 2560x1440 --pos 1280x0
    xrandr --output DP-4 --primary --mode 5120x1440 --pos 0x1440

    ~/.config/qtile/scripts/picom_toggle.sh &
    redshift &

    # Set wallpapers
    feh --bg-fill --randomize \
        ~/Pictures/Wallpaper/Desktop/2026-01-15_13.21.56.png \
        ~/Pictures/Wallpaper/Desktop/2026-01-15_13.20.41.png \
        ~/Pictures/Wallpaper/Desktop/2026-01-15_13.23.29.png

fi

# Programs to autostart
~/Documents/Dev/vn-cards/audio-replay-recorder.sh &
fcitx5 -d &
dunst &
# npx arrpc &
sleep 1
