# G5 TV Launcher – Themes

[English](README.md) · [Deutsch](README.de.md)

Downloads: [Frühling](fruehling.json) · [Sommer](sommer.json) · [Herbst](herbst.json) · [Theme-Vorlage](template.json)

Der Dateiimport ist in lokalen Testversionen ab **0.2.67** enthalten; die unten beschriebene Kategorieauswahl benötigt **0.2.68 oder neuer**; die öffentlich verlinkte Version 0.2.60 bietet ihn noch nicht. Der Import wurde vom Nutzer am Fernseher getestet; die Darstellung hängt vom Gerät ab. Das Format ist experimentell und kann sich vor einer Veröffentlichung ändern.

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
| `image` | Optionales Hintergrundbild als Datenadresse `data:image/png;base64,...`, `data:image/jpeg;base64,...` oder `data:image/webp;base64,...`; höchstens 70.000 Zeichen einschließlich Präfix. Ohne dieses Feld wird ein einfarbiger Hintergrund verwendet. |

Die gesamte Datei darf höchstens 80.000 Bytes groß sein. Theme-Dateien enthalten Daten und keinen Code: Skripte, externe URLs und SVG-Bilddaten werden nicht akzeptiert. Das aktuelle Format verändert Farben und Hintergrundbild, nicht das gesamte Launcher-Layout oder Animationen. Eigene oder zur Weitergabe freigegebene Bilder verwenden und bei einer Veröffentlichung Urheber und Lizenz angeben.

Beispiel:

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
