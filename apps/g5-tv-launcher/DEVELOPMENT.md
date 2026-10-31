# Development notes

- Version 0.2.80 is rebuilt from tested 0.2.72 source. The release IPK itself has not been tested on the TV. The user confirmed the Cyberpunk theme, imported neon animation and beach scene; not every animation option has been device-tested. The Direct Home monitor logs a missing heartbeat without automatically restoring LG Home; manual recovery remains available.
- GeoSphere AROME weather data is requested through Open-Meteo. Meteocons and Makin’ Things SVG icons include their MIT licenses in `app/weather-icons/`. Each set has an independent animation setting.
- Direct Home stages the icon assets with the app. Return to LG Home before updating the test installation, then re-enable Direct Home. Existing Magic Mapper and autostart options remain available.

- App ID: `org.schrotty74.g5launcher`; package version: 0.2.80.
- `app/` contains the webOS app: HTML, JavaScript, CSS, app icon, and eight illustrated themes with local SVG assets. The IPK is built from this directory.
- The app lists launch points using the existing Homebrew Channel Luna service and launches apps via the webOS Application Manager. HDMI launch points are filtered from the app collection but retained to resolve input labels. Live TV is exposed under Inputs.
- The Homebrew exec service reads local icon paths with an allowlist and size limit. Fallback initials are used when an icon cannot be read. Weather requests go to Open-Meteo.
- Settings, favorite order, icon size and input labels are stored under `g5home.prefs` in localStorage; the JSON backup contains these settings. Backups are written to `/media/developer/g5-tv-launcher/backup.json` through the Homebrew service; save replaces the previous file.
- The package makes no Home-button changes on installation. The optional Home mapping uses the existing Magic Mapper 1.1.2 configuration interface only after explicit activation; Home mapping itself does not change the startup hook. The separate, opt-in autostart integration installs a launcher-owned link in the Homebrew startup hook; disable it before uninstalling. Verify launcher behavior on the target TV after changes.
- The source ZIP is a convenience snapshot; `app/` is the canonical source tree in this repository.
- Build with `python3 build.py` from this directory using Python 3's standard library; `--output` selects an alternate destination. The `/usr/palm` paths in the IPK and TV icon allowlist are webOS platform paths, not paths on the developer's computer.
- `home_key_helper.py` checks Magic Mapper 1.1.2 and running status, backs up the previous Home entry, preserves other mappings, checks for conflicts, and uses the mapper’s configure command. Restore only applies if Home still points to this launcher. Test on the target TV.

- The webOSRelaunch event returns to the configured start view and closes open dialogs. Background scenes also apply to Favorites and Inputs.

- `i18n.js` translates launcher text and accessibility labels. Language defaults to English, is stored in `g5home.prefs`, and is included in JSON backups. TV-provided app names and user labels are preserved.

- Version 0.2.32 adds app search, customizable shortcuts, background rotation, optional transitions and dock magnification, dock layout options and manual version checks. The update check reads the public app metadata from GitHub and does not install packages. Test TV rendering and remote navigation after changes.

- Since 0.2.33, clock and weather have independent sizes, the settings menu is grouped, and weather refresh intervals are configurable. Weather lookup searches in both supported languages and allows choosing a matching location; the TV time zone is a preference, not a guarantee of the intended location. A selected location is stored in settings and backup. Sunrise and sunset determine day/night icon transitions. Do not hardcode a personal location.

- Version 0.2.46 includes Halloween and Christmas under Special themes. Seasonal effects run only when animations are enabled: the Halloween spider, flickering house and pumpkin lights, Christmas snowfall and Santa's alternating-direction sleigh (12 seconds flying, 5 seconds between flights). Seasonal timers stop when the active theme or animation setting changes and while the document is hidden. The spider uses a timer that stops when the theme or animation setting changes and while the document is hidden. Theme names are included in backup validation and random background rotation.

- Autostart uses `autostart_helper.py` and `autostart_boot.sh`; cold boot waits 10 seconds and retries, while wake-up uses a shorter delay. The owner tested startup after deep standby on their G5. See [IPK packaging guidance](../../IPK_PACKAGING.md).
