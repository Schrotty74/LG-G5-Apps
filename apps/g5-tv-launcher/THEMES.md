# Creating background themes / Hintergrund-Themes erstellen

[Deutsch](#deutsch)

This guide describes the existing source-based background scenes. It does **not** describe an installable theme format: there is currently no theme import, template package, or theme gallery. Adding a theme requires modifying and rebuilding the launcher. Full interface layouts are not interchangeable themes in the current implementation.

## Start from the right source

Use the [launcher source](app/) for the published repository version, or the matching source ZIP in [zwischenstaende](zwischenstaende/) for an explicitly named test version. Test builds are not public releases. Never distribute personal TV settings, backup files, credentials, or IP addresses. Use artwork you have permission to redistribute and supply attribution and license details.

## Add a background scene

1. Create an SVG in `app/scenes/`, for example `my-scene.svg`. Use an existing scene as a reference; check readability behind the clock, weather and cards at TV size.
2. In `app/style.css`, add selectors for `.scene.my-scene` and `.scene.my-scene .feature-art`, including `background-image: url('scenes/my-scene.svg')`. Existing scene rules show color variables and gradients.
3. In `app/index.html`, add an option with `value="my-scene"` to `background-select`. Add its German label and an English translation to `app/i18n.js`.
4. In `app/script.js`, add the ID to the valid list in `setBackground`, the random-selection list in `rotateBackground`, and the backup-restore `backgrounds` list. If the theme should appear in time-of-day mode, explicitly update its mapping too. Review any additional theme validation when working from a newer version.
5. Optional animation requires CSS/JS work. Respect the existing animation setting and pause behavior; compare the Halloween and Christmas implementations rather than assuming an SVG animation follows the global switch automatically.
6. Build from the source directory with `python3 build.py`. Keep app metadata, build version and output name consistent. Test language switching, fixed and random backgrounds, backup restore, animations on/off, remote control, and Direct Home on a real TV. Host-side tests are not a substitute for TV testing.

Do not replace the user's installed launcher or publish a modified IPK without their agreement. For Direct Home updates, restore LG Home before installing and reactivate the chosen mode afterwards.

## Deutsch

Diese Anleitung beschreibt die vorhandenen, fest eingebauten Hintergrund-Szenen. **Es gibt derzeit kein separat installierbares Theme-Format**, keinen Theme-Import und keine Theme-Galerie. Für ein eigenes Theme muss der Launcher-Quellcode angepasst und neu gebaut werden; vollständige Oberflächen-Layouts sind noch nicht als Themes austauschbar.

1. Den passenden [Launcher-Quellcode](app/) oder das gewünschte ZIP aus [zwischenstaende](zwischenstaende/) verwenden. Testversionen sind keine veröffentlichten Versionen. Nur eigene oder zur Weitergabe freigegebene Grafiken verwenden und Lizenz sowie Urheber angeben.
2. Eine SVG-Datei in `app/scenes/` erstellen, zum Beispiel `my-scene.svg`. Vorhandene Szenen dienen als Vorlage.
3. In `app/style.css` Regeln für `.scene.my-scene` und `.scene.my-scene .feature-art` ergänzen; das Bild über `background-image: url('scenes/my-scene.svg')` einbinden.
4. In `app/index.html` bei `background-select` eine Option mit `value="my-scene"` und deutschem Namen ergänzen. In `app/i18n.js` die englische Übersetzung hinzufügen.
5. In `app/script.js` die Kennung in die Liste `valid` von `setBackground`, die Zufallsliste `names` in `rotateBackground` und die Backup-Wiederherstellungsliste `backgrounds` aufnehmen. Für den Tageszeitmodus dessen Zuordnung ebenfalls gezielt anpassen. Bei neueren Versionen weitere Prüfungen kontrollieren.
6. Optionale Animationen in CSS/JS erstellen und den vorhandenen Animationsschalter sowie das Pausieren beachten. Halloween und Weihnachten dienen als Beispiele.
7. Mit `python3 build.py` bauen. Versionsangaben abstimmen und auf dem Fernseher unter anderem Deutsch/Englisch, feste und zufällige Hintergründe, Backup-Wiederherstellung, Animation ein/aus, Fernbedienung und Direct Home prüfen.

Persönliche Einstellungen, Backups, Zugangsdaten und IP-Adressen gehören nicht in eine Veröffentlichung. Vor einem Update bei aktiver direkter Home-Übernahme LG Home wiederherstellen und die gewünschte Methode danach erneut aktivieren.
