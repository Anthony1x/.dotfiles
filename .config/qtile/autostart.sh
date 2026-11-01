#!/bin/bash

scripts=~/.config/qtile/scripts

export QT_QPA_PLATFORMTHEME=qt6ct

# WAYLAND_DISPLAY is set by qtile's wayland backend (also when nested in X11).
# Don't use XDG_SESSION_TYPE here, it's "tty" when started from a TTY.
if [ -n "$WAYLAND_DISPLAY" ]; then
    # Export the session environment to D-Bus activated and systemd --user services.
    # Without this xdg-desktop-portal(-wlr) can't find the compositor, which breaks
    # screen sharing and file pickers.
    dbus-update-activation-environment --systemd \
        WAYLAND_DISPLAY DISPLAY XDG_CURRENT_DESKTOP XDG_SESSION_TYPE XDG_SESSION_DESKTOP \
        XCURSOR_THEME XCURSOR_SIZE QT_QPA_PLATFORMTHEME \
        GTK_IM_MODULE QT_IM_MODULE XMODIFIERS

    # Monitors + wallpapers (xrandr / feh equivalents). Outputs are matched by
    # resolution, see wayland_setup.py.
    python3 "$scripts/wayland_setup.py" outputs
    python3 "$scripts/wayland_setup.py" wallpaper

    # Night light (redshift equivalent)
    gammastep-indicator -c ~/.config/gammastep/gammastep.conf &

    # DISABLED until the lock screen is debugged: with swaylock on qtile, keystrokes
    # typed at the lock screen went to the focused app instead (password leaked into a
    # terminal). Idle lock after 10 min + monitors off (X11's DPMS equivalent):
    # swayidle -w \
    #     timeout 600 "$scripts/lock.sh" \
    #     timeout 601 'wlopm --off "*"' \
    #     resume 'wlopm --on "*"' \
    #     before-sleep "$scripts/lock.sh" \
    #     lock "$scripts/lock.sh" &

    # Input synthesis for ~/Documents/Dev/vn-cards (xdotool equivalent)
    ydotoold &
else
    sleep 1

    export XCURSOR_PATH="catppuccin-mocha-dark-cursors"

    # X11 commands
    xrandr --output DP-0 --mode 2560x1440 --pos 1280x0
    xrandr --output DP-4 --primary --mode 5120x1440 --pos 0x1440

    # ~/.config/qtile/scripts/picom_toggle.sh &
    # TODO: Redshift doesn't work?
    redshift &

    # Set wallpapers
    feh --bg-fill --randomize ~/Pictures/Wallpaper/Desktop/Minecraft/
fi

# Programs to autostart
~/Documents/Dev/vn-cards/scripts/audio-replay-recorder.sh &
fcitx5 -d &
dunst &
/usr/libexec/xdg-desktop-portal &
# npx arrpc &
sleep 1
