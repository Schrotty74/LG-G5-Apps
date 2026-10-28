# LG-G5-Apps

[English](README.md) · [Deutsch](README.de.md)

Homebrew apps and tools for LG G-series TVs. Each app has its own directory with its complete source, build and installation notes, and downloadable webOS packages.

| Icon | App | Summary | Source, downloads & guide | Context |
|---|---|---|---|---|
| <img src="apps/system-monitor/app/icon.png" width="72" alt="G5 System Monitor"> | [G5 System Monitor](apps/system-monitor/README.md) | Read-only dashboard for CPU, RAM, uptime, system information, storage, network, and running processes | [English](apps/system-monitor/README.md) · [Deutsch](apps/system-monitor/README.de.md) · [IPK 0.9.2](https://github.com/Schrotty74/LG-G5-Apps/raw/refs/heads/main/apps/system-monitor/g5-system-monitor_0.9.2_all.ipk) · [Source ZIP](apps/system-monitor/g5-system-monitor-source-v0.9.2.zip) · [Source tree](apps/system-monitor/app/) | [Development notes](apps/system-monitor/DEVELOPMENT.md) · [Changelog](apps/system-monitor/CHANGELOG.md) · [UI preview](apps/system-monitor/preview.png) |
| <img src="apps/g5-tv-launcher/app/icon.png" width="72" alt="G5 TV Launcher"> | [G5 TV Launcher](apps/g5-tv-launcher/README.md) | Customizable homebrew launcher with favorites, illustrated backgrounds, weather, and input shortcuts | [English](apps/g5-tv-launcher/README.md) · [Deutsch](apps/g5-tv-launcher/README.de.md) · [IPK 0.2.32](apps/g5-tv-launcher/g5-tv-launcher_0.2.32_all.ipk) · [Source ZIP](apps/g5-tv-launcher/g5-tv-launcher-source_0.2.32.zip) · [Source tree](apps/g5-tv-launcher/app/) | [Development notes](apps/g5-tv-launcher/DEVELOPMENT.md) · [Changelog](apps/g5-tv-launcher/CHANGELOG.md) |

G5 System Monitor 0.9.2 is the current package. The UI preview is a mock-up based on the app source; every value shown in it is demo data, not a capture from the TV.

## Installing an IPK

1. Download the `.ipk` file and transfer it to the TV with SFTP, for example to `/tmp`.
2. Connect to the TV over SSH as root.
3. Run the command below, replacing `FILENAME.ipk` with the exact file name:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/FILENAME.ipk","subscribe":true}'
```

The install service reports its progress in the terminal. After a successful installation, the app appears in the launcher. This method requires root access and a working Homebrew environment.

## Adding more apps

Each additional app gets its own directory under `apps/<app-name>/`. Add it as a row in the table above, with links to its source, package, documentation, and continuation context.
