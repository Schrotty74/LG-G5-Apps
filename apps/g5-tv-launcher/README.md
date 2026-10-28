# G5 TV Launcher 0.2.18

[English](README.md) · [Deutsch](README.de.md)

A standalone homebrew launcher for a rooted LG G5 with webOS 25. It provides a TV-oriented interface with a customizable favorites dock and input shortcuts.

## Features

- Browse installed apps and launch them from the overview
- Add, remove and reorder favorites; show app icons with or without names and choose from three icon sizes when names are hidden
- Navigate using the Magic Remote directional controls, pointer and wheel
- Open HDMI 1–4 and Live TV from the Inputs tab; HDMI labels can be read from TV launch points or customized in the launcher
- Choose from five illustrated background scenes; optionally show the clock and weather
- Export and import launcher settings as a JSON backup

## Downloads and source

- [Download IPK 0.2.18](g5-tv-launcher_0.2.18_all.ipk)
- [Download source ZIP](g5-tv-launcher-source_0.2.18.zip)
- [Complete app source](app/)
- [Development notes](DEVELOPMENT.md)

## Installation

A rooted TV and a working Homebrew Channel service are required. Transfer the IPK to `/tmp` using SFTP, then install it via SSH:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-tv-launcher_0.2.18_all.ipk","subscribe":true}'
```

Glasshouse's IPK upload can also be used. The app ID is `org.schrotty74.g5launcher`.

## Notes

The launcher is an ordinary app. Installing it does not automatically replace LG Home or configure the Home button or autostart. It uses the Homebrew service to read launch points and local app icons; unavailable icons fall back to a letter. Weather uses Open-Meteo and requires an internet connection. Backup file download and restore depend on the TV's web runtime. The Live TV shortcut and exact appearance should be checked on the target TV.

## Build from source on macOS

Install Python 3, open Terminal in this app directory, and run:

```sh
python3 build.py
```

The script writes `dist/g5-tv-launcher_0.2.18_all.ipk`. Use `python3 build.py --output /path/to/output` to choose another output directory. It uses only Python's standard library; no absolute path to the developer's computer is needed.
