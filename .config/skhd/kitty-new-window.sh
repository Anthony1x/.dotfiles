#!/usr/bin/env bash
# New kitty OS window in the same instance the Dock uses (default instance group).
# Needs --single-instance in ~/.config/kitty/macos-launch-services-cmdline, so a Dock-launched kitty listens.

kitty=/Applications/kitty.app/Contents/MacOS/kitty
server=$(lsof -t "$(getconf DARWIN_USER_CACHE_DIR)kitty-ipc-$UID.lock" 2>/dev/null)

# Not running: launch it like the Dock. Running without --single-instance: only activate it,
# since kitty --single-instance would start a second instance instead of adding a window.
[ -z "$server" ] && exec open -a kitty

# Count windows before activating: every window runs a child process besides kitty's own kitten helpers
windows=$(pgrep -P "$server" | while read -r pid; do ps -o command= -p "$pid"; done | grep -vc '/kitten __')

# Activate first so the new window becomes the key window; activating afterwards raises the previously
# focused one. With no window left, the reopen event sent by open already creates one.
open -a kitty
[ "$windows" -gt 0 ] && exec "$kitty" --single-instance --directory ~
exit 0
