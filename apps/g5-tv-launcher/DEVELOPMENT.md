# Development notes

- App ID: `org.schrotty74.g5launcher`; package version: 0.2.18.
- `app/` contains the webOS app: HTML, JavaScript, CSS, app icon, and five local SVG scenes. The IPK is built from this directory.
- The app lists launch points using the existing Homebrew Channel Luna service and launches apps via the webOS Application Manager. HDMI launch points are filtered from the app collection but retained to resolve input labels. Live TV is exposed under Inputs.
- The Homebrew exec service reads local icon paths with an allowlist and size limit. Fallback initials are used when an icon cannot be read. Weather requests go to Open-Meteo.
- Settings, favorite order, icon size and input labels are stored under `g5home.prefs` in localStorage; the JSON backup contains these settings. Download/import support depends on the TV runtime.
- The package makes no Home-button, autostart, root-configuration, firmware, or system-partition changes. Verify launcher behavior on the target TV after changes.
- The source ZIP is a convenience snapshot; `app/` is the canonical source tree in this repository.
- Build with `python3 build.py` from this directory using Python 3's standard library; `--output` selects an alternate destination. The `/usr/palm` paths in the IPK and TV icon allowlist are webOS platform paths, not paths on the developer's computer.
