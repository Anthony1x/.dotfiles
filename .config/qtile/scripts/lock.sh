#!/bin/sh
# Lock the screen on whichever backend is running.
# Used by the lock keybinding and by swayidle (see autostart.sh).

if [ -n "$WAYLAND_DISPLAY" ]; then
    # swaylock refuses to start twice, but pgrep avoids pointless error noise
    pgrep -x swaylock >/dev/null || exec swaylock -f
else
    exec betterlockscreen -l
fi
