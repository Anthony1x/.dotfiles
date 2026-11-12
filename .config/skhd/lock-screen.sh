#!/usr/bin/env bash
# Lock the screen right away, then turn the displays off.
# pmset alone only locks once the screen-lock delay has passed; SACLockScreenImmediate (private login.framework)
# locks immediately and, unlike a forwarded ctrl+cmd+q, needs no permission to post key events.

osascript -l JavaScript <<'EOF'
ObjC.import('Foundation');
$.NSBundle.bundleWithPath('/System/Library/PrivateFrameworks/login.framework').load;
ObjC.bindFunction('SACLockScreenImmediate', ['int', []]);
$.SACLockScreenImmediate();
EOF
pmset displaysleepnow
