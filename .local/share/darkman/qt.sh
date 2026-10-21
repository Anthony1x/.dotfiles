#!/bin/sh

# Qt 6 via qt6ct (palette + icons) and Kvantum (widget style).
case "$1" in
    dark) flavor=mocha icons=Tela-pink-dark ;;
    light) flavor=latte icons=Tela-pink-light ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

sed -i "s/^theme=.*/theme=catppuccin-$flavor-pink/" ~/.config/Kvantum/kvantum.kvconfig
sed -i -e "s|^color_scheme_path=.*|color_scheme_path=$HOME/.config/qt6ct/colors/catppuccin-$flavor-pink.conf|" \
    -e "s/^icon_theme=.*/icon_theme=$icons/" \
    ~/.config/qt6ct/qt6ct.conf
