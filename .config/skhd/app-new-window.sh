#!/usr/bin/env bash
# New window in the running instance of an app that opens one per launch (Firefox, Chromium).
# Usage: app-new-window.sh <bundle id> <args that make the running instance open a new window...>
# Always goes through open: started directly by skhd, macOS attributes the browser to skhd and denies it
# its own profile (Firefox: "Profile Missing").

bundle=$1; shift
asn=$(lsappinfo find bundleid="$bundle")

# Not running: launch it like the Dock
[ -z "$asn" ] && exec open -b "$bundle"

pid=$(lsappinfo info -only pid "${asn%%-\"*}" | sed -n 's/.*pid = \([0-9]*\).*/\1/p')

# newest  -> highest window number the app has so far
# wait N  -> block (max 3 s) until a real window newer than N is on screen
windows() {
    osascript -l JavaScript - "$pid" "$@" <<'EOF'
ObjC.import('CoreGraphics')
function run([pid, mode, before]) {
    const wins = opts => ObjC.deepUnwrap(ObjC.castRefToObject($.CGWindowListCopyWindowInfo(opts, 0)))
        .filter(w => w.kCGWindowOwnerPID === Number(pid) && w.kCGWindowLayer === 0)
    if (mode === 'newest') return Math.max(0, ...wins(0).map(w => w.kCGWindowNumber))
    for (let i = 0; i < 60; i++) {
        if (wins(1).some(w => w.kCGWindowNumber > Number(before) && w.kCGWindowBounds.Height > 100)) return 'ok'
        delay(0.05)
    }
    return 'timeout'
}
EOF
}

# Create first, activate afterwards: the app puts its new window in front of its others, and with no window
# left, activating first would make the app open one by itself (reopen) on top of the requested one.
before=$(windows newest)
open -nb "$bundle" --args "$@"
windows wait "$before" >/dev/null
exec open -b "$bundle"
