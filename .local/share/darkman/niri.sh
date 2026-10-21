#!/bin/sh

# niri watches included files and live-reloads, so swapping colors.kdl is enough.
case "$1" in
    dark) flavor=mocha ;;
    light) flavor=latte ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

# Write to a temp file and rename, so niri never reads a half-written file.
cp ~/.config/niri/colors-"$flavor".kdl ~/.config/niri/colors.kdl.tmp
mv ~/.config/niri/colors.kdl.tmp ~/.config/niri/colors.kdl
