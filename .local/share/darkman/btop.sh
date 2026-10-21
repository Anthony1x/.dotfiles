#!/bin/sh

# btop hot-reloads its config on SIGUSR2 (same as Ctrl+R).
case "$1" in
    dark) flavor=mocha ;;
    light) flavor=latte ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

sed -i "s|^color_theme = .*|color_theme = \"$HOME/.config/btop/themes/catppuccin_$flavor.theme\"|" \
    ~/.config/btop/btop.conf
pkill -USR2 -x btop || true
