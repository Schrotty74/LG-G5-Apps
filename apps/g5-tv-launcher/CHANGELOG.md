# Changelog

Each entry summarizes the changes present in the uploaded build and source since the previous documented version. Intermediate builds are not listed separately.

## 0.2.80

- Prevent the Direct Home monitor from automatically restoring LG Home solely because a heartbeat is missing. This addresses the unwanted recovery observed after opening the browser; the exact reason the monitor considered Home unresponsive remains unconfirmed. Automatic recovery for a genuinely unresponsive page is also no longer performed; manual LG Home restoration remains available.
- Independently correct the version used by the manual update check. The published 0.2.70 code compared against 0.2.60; this was a separate issue from the Direct Home recovery.
- Add an animated Cyberpunk special theme with brighter neon colors, illuminated windows and moving foreground lines; these effects follow the existing animation setting.
- Extend imported themes with predefined neon, rain, snow and particle effects, configurable color, duration, opacity and playback direction. Existing static themes remain supported.
- Allow imported themes to define scenes using rectangles, ellipses and polygons, with individual movement, blinking or swaying animations. Add a scene template, guides and a drawn animated beach theme.
- Keep the existing limit of three imported themes; a higher limit remains a future consideration.

The user confirmed the Cyberpunk appearance and animations, imported-theme animation and basic beach scene rendering on their TV. The separately rebuilt 0.2.80 release IPK has not been tested on the TV; not every imported-effect option or scene combination has been verified on-device.

## 0.2.70

- Keep Direct Home startup independent of the installed Magic Mapper status check and log the boot stage and traceback when recovery is needed. Preserve the legacy method and its cleanup when switching from it.
- Refresh weather once more five seconds after startup, relaunch or returning to the foreground, while retaining the chosen regular update interval.
- Add a choice between digital and analog clock displays, with the existing clock size setting and settings backup.
- Add Overview app management to hide, restore and reorder apps. Existing favorite selection and ordering remain available.
- Add experimental custom background themes, with separate Standard, Special and Imported categories. Install supported JSON files from `/tmp` or the JSON entry field; validate theme content, ignore unrelated JSON files, and clear the entry field after successful import. Retain up to three custom themes.
- Add Spring, Summer and Autumn theme downloads, a reusable JSON template, and English and German guides explaining import, format and authoring.
- Add an experimental triple-Home recovery gesture for Direct Home. It depends on Home relaunch events reaching the running launcher and is not an independently verified recovery path if the interface is unresponsive. The existing LG Home restore option remains available.
- Add tests for local theme file access and validation, including unrelated files and unsafe paths.

The previous Direct Home version started after an overnight standby on the user's LG G5. The user confirmed clock switching, Overview app management, theme import, category selection, filtering, removal and clearing the entry field in the preceding local tests. The 0.2.70 package is rebuilt from that test source and has not itself been tested on the TV. The delayed weather retry and emergency gesture still require device verification.

## 0.2.60 (test version)

- Add an opt-in TV Home screen selector with LG Home, the legacy Magic Mapper/autostart method and Direct Home takeover. Applying the selection requires confirmation; the legacy method remains available as a fallback.
- Stage the launcher as the TV Home screen without overwriting LG Home files. Check for Glasshouse and other takeover conflicts, preserve unrelated key mappings and provide LG Home restoration and an SSH recovery command.
- Add a local bridge for Direct Home access to app lists, icons, settings and backup operations, plus a heartbeat and recovery monitor. Share launcher preferences between the normal app and Direct Home.
- Add Home method status, confirmation and guidance to the settings menu, including instructions to restore LG Home before updating or uninstalling. Switching to Direct Home disables the launcher-owned legacy autostart and mapping as needed.
- Add a weather provider selection between Open-Meteo and GeoSphere Austria's AROME model via Open-Meteo. Keep the existing location search and day/night handling.
- Add Meteocons and Makin’ Things SVG weather icon sets, with independent animation settings for each set. Include their licenses and copy the icons into the Direct Home stage.
- Preserve the new weather settings in launcher backups and restore them with existing settings.
- Add host-side tests for Home method transitions, recovery, bridge operations and staging of weather icons.

Direct Home and weather icon switching were tested on the TV; the launcher returned after a short standby. Testing after several hours of standby remains open. A previous crash is no longer occurring, but its cause was not identified. Version 0.2.60 is a test version and is separate from the published 0.2.50 IPK.

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
