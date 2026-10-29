#!/bin/sh
# Managed by org.schrotty74.g5launcher direct Home; activated only by settings.
APP_DIR=/media/developer/apps/usr/palm/applications/org.schrotty74.g5launcher
[ -f "$APP_DIR/home_mode_helper.py" ] || exit 0
STATE_DIR=/var/lib/webosbrew/g5-tv-launcher/home-mode
mkdir -p "$STATE_DIR" || exit 1
nohup sh -c 'sleep 10; exec python3 "$1/home_mode_helper.py" boot' sh "$APP_DIR" </dev/null >>"$STATE_DIR/boot.log" 2>&1 &
exit 0
