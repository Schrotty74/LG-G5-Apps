# G5 TV Launcher – Themes

[English](README.md) · [Deutsch](README.de.md)

Downloads: [Frühling](fruehling.json) · [Sommer](sommer.json) · [Herbst](herbst.json) · [Winter](winter.json) · [Cyberpunk Neon](cyberpunk-neon.json) · [Theme-Vorlage](template.json)

Dateiimport und Kategorieauswahl sind in **0.2.70** enthalten. Der Import wurde vom Nutzer am Fernseher getestet; die Darstellung hängt vom Gerät ab. Das Format ist experimentell und kann sich in einer zukünftigen Version ändern.

**Animationen:** Die Effekte für importierte Themes und die Einstellungen unter `animationOptions` sind nur im neueren Teststand enthalten, nicht in der veröffentlichten IPK 0.2.70. Die neuen Einstellmöglichkeiten wurden noch nicht am Fernseher getestet. Der Import und der Neon-Effekt wurden im Teststand am Fernseher ausprobiert. Andere Effekte sind am Fernseher noch nicht bestätigt. Ältere Themes ohne Animationsfeld funktionieren weiterhin.

## Auf einem gerooteten Fernseher importieren

1. Die gewünschte Theme-JSON-Datei herunterladen und per SFTP, zum Beispiel mit Termius, direkt nach `/tmp` auf den Fernseher übertragen. Dateien in `/tmp` sind vorübergehend; eine eigene Kopie behalten.
2. Im Launcher **Einstellungen → Darstellung → Eigene Themes** öffnen. **Dateien suchen** wählen, die Datei auswählen und **Datei importieren** drücken.
3. Unter **Theme-Kategorie** „Importierte Themes“ und darunter bei **Hintergrund** das gewünschte Theme wählen. Es lassen sich höchstens drei eigene Themes speichern. Um Platz zu machen, ein Theme unter „Eigene Themes“ entfernen. Die Quelldatei in `/tmp` ist von der importierten Kopie getrennt.

Die Dateiauswahl zeigt passende Theme-JSON-Dateien direkt in `/tmp` und ignoriert andere JSON-Dateien; Unterordner werden nicht durchsucht. In Versionen mit JSON-Eingabefeld kann auch der vollständige Theme-Inhalt eingefügt und installiert werden. Eine URL-Importfunktion ist das nicht.

## Eigenes Theme erstellen

[template.json](template.json) kopieren, als UTF-8 bearbeiten und mit einem ASCII-Dateinamen speichern, der auf `.json` endet, zum Beispiel `mein-theme.json`:

| Feld | Bedeutung |
| --- | --- |
| `format` | Muss `g5-theme` sein. |
| `version` | Zahl `1`. |
| `id` | Eindeutige Kennung, 1–32 kleine ASCII-Buchstaben, Ziffern oder Bindestriche. Eine bereits verwendete ID ersetzt das entsprechende importierte Theme. |
| `name` | Angezeigter Name, 1–60 Zeichen. |
| `background` | Hintergrundfarbe als `#RRGGBB`. |
| `accent` | Akzentfarbe als `#RRGGBB`. |
| `glow` | Leuchtfarbe als `#RRGGBB`. |
| `animation` | Optional: `none`, `neon`, `rain`, `snow` oder `particles`; ohne Feld gilt `none`. Das sind vorgegebene Launcher-Effekte. Animationen müssen in den Launcher-Einstellungen eingeschaltet sein. Sie erscheinen im Hintergrundbanner. |
| `animationOptions` | Optionales Objekt zum Anpassen des gewählten Effekts; die erlaubten Felder stehen unten. Nur im unterstützenden Teststand verfügbar. |
| `image` | Optionales Hintergrundbild als Datenadresse `data:image/png;base64,...`, `data:image/jpeg;base64,...` oder `data:image/webp;base64,...`; höchstens 70.000 Zeichen einschließlich Präfix. Ohne dieses Feld wird ein einfarbiger Hintergrund verwendet. |

Die gesamte Datei darf höchstens 80.000 Bytes groß sein. Theme-Dateien enthalten Daten und keinen Code: Skripte, externe URLs und SVG-Bilddaten werden nicht akzeptiert. Das Format verändert Farben und Hintergrundbild; im unterstützenden Teststand ergänzt es einen wählbaren vorgegebenen Animationseffekt. Freie Animationsskripte und Änderungen am Launcher-Layout werden nicht unterstützt. Eigene oder zur Weitergabe freigegebene Bilder verwenden und bei einer Veröffentlichung Urheber und Lizenz angeben.

### Animation anpassen

Das optionale Objekt `animationOptions` kann diese Felder enthalten. Nicht angegebene Felder behalten die Voreinstellung des Effekts. Für Dezimalzahlen in JSON einen Punkt verwenden.

| Feld | Erlaubter Wert | Wirkung |
| --- | --- | --- |
| `color` | Farbe als `#RRGGBB` | Farbe des Effekts. |
| `duration` | Zahl von 0.5 bis 30 | Dauer eines Durchlaufs in Sekunden; kleinere Werte sind schneller. |
| `opacity` | Zahl von 0 bis 1 | Deckkraft des Effekts; 0 ist unsichtbar. |
| `direction` | `normal`, `reverse` oder `alternate` | Richtung des Animationsablaufs. |

Die Parameter ändern einen der vorgegebenen Effekte im Banner; sie erzeugen keine frei programmierbaren Animationen. Animationen müssen im Launcher eingeschaltet sein. Das Beispiel und die [Vorlage](template.json) können angepasst werden:

```json
{
  "format": "g5-theme",
  "version": 1,
  "id": "mein-erstes-theme",
  "name": "Mein erstes Theme",
  "background": "#102030",
  "accent": "#80d0ff",
  "glow": "#4466aa"
}
```
