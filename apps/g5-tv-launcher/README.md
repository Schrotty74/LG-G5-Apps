# G5 TV Launcher 0.2.70

**Version 0.2.70:** Includes the tested launcher features and experimental custom themes. The rebuilt release package itself has not yet been tested on the TV; see [project status](PROJECT_STATUS.md).

[English](README.md) · [Deutsch](README.de.md)

A standalone homebrew launcher for a rooted LG G5 with webOS 25. It provides a TV-oriented interface with a customizable favorites dock and input shortcuts.

## Screenshots

Click an image to view it full size.

<a href="screenshots/overview.jpg"><img src="screenshots/overview-thumb.jpg" alt="Overview" width="240"></a>
<a href="screenshots/favorites.jpg"><img src="screenshots/favorites-thumb.jpg" alt="Favorites" width="240"></a>
<a href="screenshots/inputs.jpg"><img src="screenshots/inputs-thumb.jpg" alt="Inputs" width="240"></a>

## Features

- Browse and launch installed apps from Overview; HDMI inputs and Live TV have their own Inputs page.
- Add, remove and reorder favorites in the glass-style dock. Show app icons with or without names and choose from three icon sizes when names are hidden.
- Open HDMI 1–4 and Live TV. HDMI names can be read from the TV's launch points or customized.
- Choose from seven illustrated scenes, shown in the banner on Overview, Favorites and Inputs. Halloween and Christmas are grouped under Special themes.
- Choose LG Home, the legacy method or Direct Home takeover in the TV Home screen settings. Direct Home does not require Magic Mapper; the legacy method remains available as a fallback.
- Show or hide the clock and weather independently; choose a location and either Open-Meteo or GeoSphere Austria data via Open-Meteo.
- Select Overview, Favorites or Inputs as the start page, including when reopening the launcher.
- Search installed apps by name.
- Adjust clock and weather sizes independently; set the weather refresh interval to 15 minutes, hourly, twice daily or daily.
- Choose Meteocons or Makin’ Things weather icons and independently enable or disable animation for each set. Day/night switching uses local sunrise and sunset times.

See the complete [feature overview with full feature list](FEATURES.md) for further details.

## Downloads and source

- [Download current IPK](g5-tv-launcher_0.2.70_all.ipk)
- [Download current source ZIP](g5-tv-launcher-source_0.2.70.zip)
- [Complete app source](app/)
- [Development notes](DEVELOPMENT.md)
- [Project status and continuation notes (German)](PROJECT_STATUS.md)
- [Changelog](CHANGELOG.md)


- [QR code for version 0.2.70](g5-tv-launcher-qr_0.2.70.png)

## Installation

A rooted TV and a working Homebrew Channel service are required. Transfer the IPK to `/tmp` using SFTP, then install it via SSH:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-tv-launcher_0.2.70_all.ipk","subscribe":true}'
```

Glasshouse's IPK upload can also be used. The app ID is `org.schrotty74.g5launcher`. If Direct Home takeover is active, restore LG Home before updating or uninstalling; re-enable takeover after installation. See [Direct Home test and recovery](HOME_TAKEOVER_TEST.md).

## TV Home screen

Under Settings → Start & Home → TV Home screen, choose **LG Home**, **Legacy method**, or **Direct Home takeover**, then select **Apply method**. Direct Home uses the launcher as the TV Home screen without Magic Mapper. The legacy method uses the existing Home mapping and autostart as a fallback. Disable Glasshouse Home before switching methods. Restore LG Home before updating or uninstalling.

Direct Home started after overnight standby in the preceding 0.2.63 device test. See [test and recovery instructions](HOME_TAKEOVER_TEST.md).

## Optional autostart

For LG Home and the legacy method, enable or disable the optional launcher autostart under Start & Home. Direct Home uses its own startup mechanism and disables the legacy autostart when switching. Restore LG Home and disable the optional autostart before uninstalling.

## Notes

Installing the launcher does not automatically replace LG Home or configure the Home button or autostart; these options require explicit activation. It uses the Homebrew service to read launch points and local app icons; unavailable icons fall back to a letter. Weather and location lookup use Open-Meteo and require an internet connection; the GeoSphere option selects GeoSphere Austria’s AROME model via Open-Meteo. Backups are stored at `/media/developer/g5-tv-launcher/backup.json` on the TV and can be copied via SFTP. Saving again replaces the previous backup. The Live TV shortcut and exact appearance should be checked on the target TV.

## Build from source on macOS

Install Python 3, open Terminal in this app directory, and run:

```sh
python3 build.py
```

The script writes `dist/g5-tv-launcher_0.2.70_all.ipk`. Use `python3 build.py --output /path/to/output` to choose another output directory. It uses only Python's standard library; no absolute path to the developer's computer is needed.

## Optional Home button mapping

The optional Home button mapping requires [Magic Mapper for webOS 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2) to be installed, active and configured to start on the TV. This launcher integration checks for version 1.1.2. See the [Magic Mapper project and Homebrew installation instructions](https://github.com/afonsojramos/magic-mapper-webos#installing-from-homebrew-channel).

In the launcher's Settings, explicitly assign Home to this launcher. You do not need to configure the Home button manually in Magic Mapper first; the launcher applies the mapping through Magic Mapper. The previous Home mapping is saved locally and can be restored from the same screen; other button mappings are retained. Restore the previous mapping before uninstalling the launcher. Glasshouse Home or other Home remappers may interfere. This option does not install Magic Mapper or change its startup hook.

The launch view can be set to Overview, Favorites or Inputs and also applies when the launcher is reopened. The selected illustrated scene is shown in the banner on all three pages.

## Language

English is the default. Change the language to English or German under Settings → Language. The selection is stored on the TV and included in settings backups.

## Custom themes

[Download Spring, Summer, Autumn and Winter themes, import instructions and the theme template](themes/README.md). Theme import is included in version 0.2.70.
