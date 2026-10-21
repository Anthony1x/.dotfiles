#!/bin/sh

# Point colors.css at the flavor; waybar reloads the style by itself
# (reload_style_on_change). SIGUSR2 would reload too, but crashes waybar.
case "$1" in
    dark) flavor=mocha ;;
    light) flavor=latte ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

ln -sfn "$flavor.css" ~/.config/waybar/colors.css
# Refresh the custom/theme icon.
pkill -RTMIN+8 -x waybar || true
