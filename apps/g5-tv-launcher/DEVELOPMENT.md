# Development notes

- App ID: `org.schrotty74.g5launcher`; package version: 0.2.28.
- `app/` contains the webOS app: HTML, JavaScript, CSS, app icon, and five local SVG scenes. The IPK is built from this directory.
- The app lists launch points using the existing Homebrew Channel Luna service and launches apps via the webOS Application Manager. HDMI launch points are filtered from the app collection but retained to resolve input labels. Live TV is exposed under Inputs.
- The Homebrew exec service reads local icon paths with an allowlist and size limit. Fallback initials are used when an icon cannot be read. Weather requests go to Open-Meteo.
- Settings, favorite order, icon size and input labels are stored under `g5home.prefs` in localStorage; the JSON backup contains these settings. Backups are written to `/media/developer/g5-tv-launcher/backup.json` through the Homebrew service; save replaces the previous file.
- The package makes no Home-button changes on installation. The optional Home mapping uses the existing Magic Mapper 1.1.2 configuration interface only after explicit activation; it does not change the startup hook, firmware, root configuration or system partitions. Verify launcher behavior on the target TV after changes.
- The source ZIP is a convenience snapshot; `app/` is the canonical source tree in this repository.
- Build with `python3 build.py` from this directory using Python 3's standard library; `--output` selects an alternate destination. The `/usr/palm` paths in the IPK and TV icon allowlist are webOS platform paths, not paths on the developer's computer.
- `home_key_helper.py` checks Magic Mapper 1.1.2 and running status, backs up the previous Home entry, preserves other mappings, checks for conflicts, and uses the mapper’s configure command. Restore only applies if Home still points to this launcher. Test on the target TV.

- The webOSRelaunch event returns to the configured start view and closes open dialogs. Background scenes also apply to Favorites and Inputs.

- `i18n.js` translates launcher text and accessibility labels. Language defaults to English, is stored in `g5home.prefs`, and is included in JSON backups. TV-provided app names and user labels are preserved.
