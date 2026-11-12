#!/bin/zsh
# Toggle kitty's quick access terminal like a quake terminal:
#   hidden              -> show it
#   visible, not focused -> focus it
#   visible and focused  -> hide it and hand focus back to the previous app
# Needed because hiding it leaves kitty-quick-access as the active app with no window.

kitten=/Applications/kitty.app/Contents/MacOS/kitten
qa_bundle=net.kovidgoyal.kitty-quick-access

bundle_of() { lsappinfo info -only bundleid "$1" | sed -n 's/.*bundleID="\([^"]*\)".*/\1/p' }

# The panel never shows up in lsappinfo's visibleProcessList, so ask the window server instead
qa_visible() {
    pgrep -qf 'MacOS/kitty-quick-access' || return 1
    (( $(osascript -l JavaScript -e 'ObjC.import("CoreGraphics"); ObjC.deepUnwrap(ObjC.castRefToObject($.CGWindowListCopyWindowInfo(1, 0))).filter(w => w.kCGWindowOwnerName === "kitty-quick-access").length') > 0 ))
}

cd ~ || exit 1

if ! qa_visible; then
    exec $kitten quick-access-terminal
elif [[ $(bundle_of "$(lsappinfo front)") != $qa_bundle ]]; then
    open -b $qa_bundle
else
    $kitten quick-access-terminal
    prev=$(lsappinfo visibleProcessList | tr ' ' '\n' | grep '^ASN:' | grep -v '"kitty-quick-access":' | head -1)
    [[ -n $prev ]] && open -b "$(bundle_of "${prev%%-\"*}")"
fi
