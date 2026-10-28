# Changelog

Changes to G5 TV Launcher. Versions refer to the app package; older entries describe development builds and are not a promise of compatibility with every TV.

## 0.2.28
- Add English and German throughout the launcher, including navigation, settings, buttons and messages. English is the default.
- Add a language selector; save the selection on the TV and include it in settings backups. App names and custom input labels remain as supplied by the TV or user.

## 0.2.27
- Place the Favorites and Inputs headings and descriptions inside the illustrated banner, matching the Overview layout.
- Keep the favorites dock, input shortcuts and their management controls below the banner.

## 0.2.26
- Show the chosen scene in a banner on Favorites and Inputs with the same framing as Overview.
- Correct the oversized and cropped full-screen rendering introduced in the earlier intermediate build.

## 0.2.25
- Add a setting for the start page: Overview, Favorites or Inputs; Overview is the default.
- Apply the selection when starting or reopening the launcher, and include it in settings backups.

## 0.2.24
- Return to Overview when webOS relaunches the app, including when opened through a Home-button shortcut, and close any open dialogs.
- Add the selected landscape imagery to Favorites and Inputs; subsequent builds refine its framing and page titles.

## 0.2.23
- Add optional Home-button mapping through an installed, active Magic Mapper 1.1.2 configured to start on the TV.
- Save the previous Home mapping and provide a way to restore it; preserve mappings for other buttons and detect conflicting changes.
- Leave installation and startup configuration of Magic Mapper to the user.

## 0.2.22
- Replace the browser download and file picker with settings backup and restore through the Homebrew service.
- Save JSON to `/media/developer/g5-tv-launcher/backup.json` on the TV, validate data when restoring, and allow the file to be copied via SFTP. Saving again replaces the existing backup.
- Include launcher preferences, favorites and custom input labels in the backup.

## 0.2.21
- Place HDMI 1–4 and Live TV in one centered row, farther below the Inputs heading.

## 0.2.20
- Add padding around the top navigation to prevent focus and pointer outlines from being clipped.

## 0.2.19
- Add the TV-and-dock launcher icon in webOS-compatible PNG sizes.

## 0.2.18
- Move the Live TV shortcut from the app collection to Inputs.

## 0.2.17
- Filter HDMI launch points from the app collection and favorites selection while retaining them for input names.

## 0.2.16
- Add five illustrated overview scenes that change with the selected background.

## 0.2.15
- Add three selectable icon sizes for favorites without labels and increase spacing at larger sizes.

## 0.2.14
- Display optional favorite app names below their icons.

## 0.2.13
- Read supported local app icon files through the existing Homebrew service; keep the initial-letter fallback when an icon cannot be loaded.

## 0.2.12
- Derive HDMI labels from matching TV launch-point IDs; locally customized labels take precedence.

## 0.2.11
- Separate selected favorites from other apps in the management list and widen the favorites bar.

## 0.2.10
- Align favorites-management controls and improve focus and scrolling when reordering long lists.

## 0.2.9
- Add favorite ordering, app-icon loading attempts, optional labels, and JSON settings backup and restore.

## 0.2.8
- Arrange the four HDMI shortcuts in a centered row on wide screens.

## 0.2.7
- Remove the duplicate bottom favorites dock and present favorites in a compact central glass bar.
- Add favorite management from the overview and Favorites tab, plus locally editable HDMI labels.

## 0.2.6
- Rename the navigation tabs to Overview, Favorites and Inputs.

## 0.2.5
- Remove the Library tab and display selected favorites in a larger centered view.

## 0.2.4
- Add favorite selection and HDMI shortcuts; update the TV settings shortcut.

## 0.2.3
- Add pointer-edge navigation and left/right controls for the app rail; use the webOS Application Manager for app launches.

## 0.2.2
- Simplify visual effects and scrolling for TV performance, load app tiles in batches, and make navigation tabs switch views.

## 0.2.1
- Repackage the IPK for Glasshouse and assign a distinct version.

## 0.2.0
- Redesign the home screen with five selectable backgrounds, optional clock and weather, location selection, a glass dock and wheel navigation.

## 0.1.0
- Initial standalone launcher with a TV-oriented interface, Homebrew app discovery, app launching and system shortcuts.
