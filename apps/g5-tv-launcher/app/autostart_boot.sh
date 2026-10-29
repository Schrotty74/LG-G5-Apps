#!/bin/sh
# G5 TV Launcher: Homebrew Channel invokes this linked hook at cold boot.
APP_DIR=/media/developer/apps/usr/palm/applications/org.schrotty74.g5launcher
HELPER="$APP_DIR/autostart_helper.py"
STATE_DIR=/var/lib/webosbrew/g5-tv-launcher
[ -f "$HELPER" ] || exit 0
mkdir -p "$STATE_DIR" || exit 1
nohup python3 "$HELPER" watch boot </dev/null >>"$STATE_DIR/autostart.log" 2>&1 &
exit 0
