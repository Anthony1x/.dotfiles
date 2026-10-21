#!/bin/sh

# rofi reads its theme on every start, so pointing the symlink is enough.
case "$1" in
    dark) flavor=mocha ;;
    light) flavor=latte ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

ln -sfn "catppuccin-$flavor.rasi" ~/.local/share/rofi/themes/catppuccin.rasi
