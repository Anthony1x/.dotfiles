#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# Custom stuff from yours truly
TERMINAL=/sbin/kitty
EDITOR=/sbin/neovide

xset r rate 300 40

GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
SDL_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx

GTK_THEME=Adwaita:dark
QT_QPA_PLATFORMTHEME=qt5ct:qt6ct
QT_STYLE_OVERIDE=GTK+

XCURSOR_PATH="catppuccin-mocha-dark-cursors"

# End

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ]; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
        [ -x "$f" ] && . "$f"
    done
    unset f
fi
