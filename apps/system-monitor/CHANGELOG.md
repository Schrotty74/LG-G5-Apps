# Changelog

## 0.9.3

- Corrected IPK archive paths so the Homebrew catalog validation can read its package metadata.

## 0.9.2

- Softened hard, offset card shadows that looked like a second tile outline.
- Kept softer shadows to preserve the dashboard's depth.

## 0.9.1

- Stacked filesystem mount paths and capacity values vertically.
- Allowed long mount paths to wrap inside their card, preventing overlap with neighboring tiles and usage bars.

## 0.9.0

- Added more depth to dashboard cards with layered highlights and subtle perspective.
- Added a raised focus treatment for buttons and respected reduced-motion preferences.
- Preserved the dark dashboard design and existing monitoring features.

## 0.8.0

- Added a RAM history chart with up to 30 readings.
- Added usage bars for recognized filesystems.
- Added a selectable refresh interval of 3, 5, or 10 seconds.
- Kept the interval selection for the current session only.

## 0.7.0

- Added model, webOS TV SDK, firmware, and board information.
- Added storage capacity and network status.
- Read filesystem usage with `df -kP`; gathered interfaces, IPv4 addresses, and the default route for network details.

## 0.6.0

- Removed the temperature tile because the tested device exposed no usable sensor reading.
- Added an Exit button and Magic Remote Back handling through `webOS.platformBack()`.
- Added mouse-wheel scrolling.

## 0.5.0

- Added firmware and SDK details through `com.webos.service.tv.systemproperty/getSystemInfo`.
- Checked sensor paths under `/sys/class/thermal` and `/sys/class/hwmon`.

## 0.4.0

- Added scrolling with the remote's directional controls and Page Up/Page Down.
- Made the process section focusable so it can be reached on the TV screen.

## 0.3.0

- Established the dashboard's CPU usage, RAM usage, uptime, kernel, root status, CPU history, and process snapshot.
- Adjusted the Homebrew Luna endpoint and response handling.
- Improved parsing for different `top` output formats.
- Ignored delayed responses after a request timeout.
- Created the first installable IPK.
