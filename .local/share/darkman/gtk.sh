#!/bin/sh

# GTK 3/4 theme, icons and the color-scheme preference. xdg-desktop-portal-gnome
# relays color-scheme to kitty, Firefox, Chromium, VS Code and libadwaita apps.
case "$1" in
    dark) flavor=mocha icons=Tela-pink-dark scheme=prefer-dark prefer_dark=1 ;;
    light) flavor=latte icons=Tela-pink-light scheme=prefer-light prefer_dark=0 ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac
theme="catppuccin-$flavor-pink-standard+default"

# Theme and icons first, so apps reacting to color-scheme already see them.
gsettings set org.gnome.desktop.interface gtk-theme "$theme"
gsettings set org.gnome.desktop.interface icon-theme "$icons"
gsettings set org.gnome.desktop.interface color-scheme "$scheme"

# Same values in the files nwg-look maintains (read by apps without gsettings).
for ini in ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini; do
    sed -i -e "s/^gtk-theme-name=.*/gtk-theme-name=$theme/" \
        -e "s/^gtk-icon-theme-name=.*/gtk-icon-theme-name=$icons/" \
        -e "s/^gtk-application-prefer-dark-theme=.*/gtk-application-prefer-dark-theme=$prefer_dark/" \
        "$ini"
done
sed -i -e "s|^Net/ThemeName .*|Net/ThemeName \"$theme\"|" \
    -e "s|^Net/IconThemeName .*|Net/IconThemeName \"$icons\"|" \
    ~/.config/xsettingsd/xsettingsd.conf

# libadwaita apps pick up the Catppuccin stylesheet on their next start.
for f in assets gtk.css gtk-dark.css; do
    ln -sfn "/usr/share/themes/$theme/gtk-4.0/$f" ~/.config/gtk-4.0/"$f"
done
