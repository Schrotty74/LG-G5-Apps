![LG G5 Apps](assets/lg-g5-apps-logo.jpg)

# LG-G5-Apps

Small homebrew apps and tools for LG G-series TVs. Each app has its own directory under `apps/`, including source code and downloads.

[English](README.md) | [Deutsch](README.de.md)

## Apps

### G5 System Monitor

A local, read-only dashboard for a rooted LG G5 running webOS 25. It displays CPU and RAM usage, system uptime, firmware and model details, storage, network status, and a snapshot of running processes. It also includes CPU and RAM history charts, a configurable refresh interval, and scrolling with the remote or mouse wheel.

- **Current version:** 0.9.2
- **Download IPK:** [G5 System Monitor 0.9.2](https://github.com/Schrotty74/LG-G5-Apps/raw/refs/heads/main/apps/system-monitor/g5-system-monitor_0.9.2_all.ipk)
- **Source code and installation notes:** [apps/system-monitor](apps/system-monitor/)
- **Changelog:** [All versions and changes](apps/system-monitor/CHANGELOG.md)

The app requires the Homebrew Channel and its Luna exec service. It does not run background services or change system files or autostart settings. Temperature is omitted because no readable sensor value was found on the tested TV.

## Installing an IPK on webOS

1. Download the `.ipk` file and transfer it to the TV with SFTP, for example to `/tmp`.
2. Connect to the TV over SSH as root.
3. Run the command below, replacing `FILENAME.ipk` with the actual file name:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/FILENAME.ipk","subscribe":true}'
```

The install service prints its status in the terminal. After a successful installation, the app appears in the launcher. This method requires root access and a working Homebrew environment. Files in this repository are webOS IPK packages, not Android APKs.

## Adding more apps

Place each additional app in its own directory under `apps/<app-name>/`, then add it to this overview.
