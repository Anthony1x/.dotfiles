#!/bin/sh

# awww runs two daemons (awww@wallpaper, awww@backdrop). niri's layer-rule puts
# "backdrop" behind the workspaces in the overview, so it gets the blurred image.
# swaylock reads the blurred one through a symlink, keeping its config static.
case "$1" in
    dark) image=Physcic-Mindwarp-2 ;;
    light) image=wallhaven-gwdvxq ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac
dir=~/Pictures/Wallpapers

mkdir -p ~/.local/state/wallpaper
ln -sfn "$dir/$image-blur.jpg" ~/.local/state/wallpaper/blur.jpg

awww img --namespace wallpaper "$dir/$image.jpg"
awww img --namespace backdrop "$dir/$image-blur.jpg"
