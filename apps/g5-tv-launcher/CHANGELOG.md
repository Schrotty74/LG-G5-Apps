# Changelog

Entries describe versions published in this repository. Each entry includes the relevant changes since the previous published version; intermediate test builds are grouped into the next published version.

## 0.2.50

- Add optional autostart after a cold boot and when waking from standby. The launcher waits 10 seconds at cold boot and retries if needed; wake-up uses a shorter delay.
- Use an app-owned boot script and a symbolic link for the Homebrew startup hook; migrate the earlier launcher-owned hook and preserve unrelated hooks.
- Add settings to enable, disable and check autostart. Home-button mapping remains separate; disable autostart before uninstalling.
- Correct IPK archive paths and add Installed-Size metadata for Homebrew catalog validation.

## 0.2.46

- Add Halloween and Christmas themes, grouped separately from the standard backgrounds.
- Add optional seasonal animations: a descending spider at changing positions, flickering Halloween house windows and pumpkin face, and falling snow for Christmas. A reindeer-drawn sleigh crosses the Christmas scene in alternating directions, with a 12-second flight and a 5-second pause. The effects follow the existing animation setting.
- Include the new themes in background selection, random rotation and settings backup/restore validation.

## 0.2.39

- Add independent clock and weather sizes and configurable weather refresh intervals of 15 minutes, one hour, 12 hours or 24 hours. Include these settings in backups.
- Add optional weather animations, a moon for clear nights, a moon behind clouds for cloudy nights, and a rain-cloud icon with animated drops.
- Switch day and night icons using the selected location's sunrise and sunset, independently of the weather refresh interval.
- Search locations in English and German, prefer results matching the TV's time zone and let users select a result by city, region and country. Save the chosen location and discard outdated weather responses.
- Organize the settings menu into categories with scrollable sections.

## 0.2.32

- Add app search and customizable Overview shortcuts for apps, HDMI inputs and TV settings.
- Allow backgrounds to stay fixed, change on launch or change with the time of day.
- Add optional page transitions and macOS-inspired magnification of the favorite icon selected with the pointer or directional controls.
- Add dock spacing, transparency and position settings; fix spacing selection across icon sizes and label modes.
- Provide more room for focus outlines around the Overview app rail.
- Add manual GitHub version checks without automatic installation, and include the new preferences in settings backups.

## 0.2.28

- Add an English and German interface and a language selector. English is the default; the selected language is saved and backed up. TV-provided app names and custom labels remain unchanged.
- Allow Overview, Favorites or Inputs as the start page, including when the app is reopened via the Home button.
- Show the same illustrated banner framing and page headings on all three pages.
- Add optional Home-button mapping using an installed and active Magic Mapper 1.1.2 configured to start on the TV. Preserve other mappings, detect conflicts and allow restoring the previous Home mapping.
- Replace browser download and file selection for settings backups with JSON save and restore through the Homebrew service. The backup is stored on the TV at `/media/developer/g5-tv-launcher/backup.json`, can be copied via SFTP, and is replaced by the next save.

## 0.2.21

- Place HDMI 1–4 and Live TV in one centered row below the Inputs heading.
- Add space around the top navigation to prevent focus and pointer outlines from being clipped.

## 0.2.19

- Add the TV-and-dock launcher icon in webOS-compatible PNG sizes.

## 0.2.18

First version published in this repository, incorporating earlier development builds:

- Add the standalone TV launcher with app discovery through the Homebrew service, app launching, system shortcuts and performance-oriented scrolling.
- Provide Overview, Favorites and Inputs views with five illustrated backgrounds, optional clock and weather, location selection and a glass-style favorites dock.
- Support Magic Remote directional controls, pointer-edge navigation and wheel navigation in app rails.
- Add favorite selection, ordering, management, optional names under icons and selectable icon sizes. Read local app icons where available and fall back to initials.
- Open four HDMI inputs and Live TV from Inputs; use TV launch points to derive HDMI names or allow locally customized labels. Exclude HDMI inputs and Live TV from the app collection.
- Add settings backup and restore, focus and scrolling improvements for longer favorites lists, and packaging compatible with Glasshouse.
