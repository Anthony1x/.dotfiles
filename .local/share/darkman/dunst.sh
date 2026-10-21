#!/bin/sh

# dunst reads drop-ins from dunstrc.d/ on top of dunstrc; `dunstctl reload` applies them.
case "$1" in
    dark) flavor=mocha ;;
    light) flavor=latte ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

mkdir -p ~/.config/dunst/dunstrc.d
cp ~/.config/dunst/colors-"$flavor".conf ~/.config/dunst/dunstrc.d/99-colors.conf
dunstctl reload || true
