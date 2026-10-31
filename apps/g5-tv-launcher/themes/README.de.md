# G5 TV Launcher – Themes

[English](README.md) · [Deutsch](README.de.md)

## Statische Themes

[Frühling](static/fruehling.json) · [Sommer](static/sommer.json) · [Herbst](static/herbst.json) · [Winter](static/winter.json)

## Animierte Themes

[Cyberpunk Neon](animated/cyberpunk-neon.json) · [Strand](animated/strand-vektor.json)

[Theme-Vorlage](template.json)

Dateiimport und Kategorieauswahl sind in **0.2.70** enthalten. Der Import wurde vom Nutzer am Fernseher getestet; die Darstellung hängt vom Gerät ab. Das Format ist experimentell und kann sich in einer zukünftigen Version ändern.

**Kompatibilität:** Strand und Cyberpunk Neon benötigen Launcher-Version 0.2.80 oder neuer. Ältere Versionen unterstützen die gezeigten Animationen beziehungsweise Szenenelemente nicht vollständig.

**Animationen:** Effekte für importierte Themes und `animationOptions` sind ab 0.2.80 enthalten. Die neuen Einstellmöglichkeiten wurden noch nicht am Fernseher getestet. Der Import und der Neon-Effekt wurden im Teststand am Fernseher ausprobiert. Andere Effekte sind am Fernseher noch nicht bestätigt. Ältere Themes ohne Animationsfeld funktionieren weiterhin.

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
| `animationOptions` | Optionales Objekt zum Anpassen des gewählten Effekts; die erlaubten Felder stehen unten. Ab Version 0.2.80 verfügbar. |
| `scene` | Optional: Formen und Einzelanimationen, siehe Abschnitt unten. Ab Version 0.2.80. |
| `image` | Optionales Hintergrundbild als Datenadresse `data:image/png;base64,...`, `data:image/jpeg;base64,...` oder `data:image/webp;base64,...`; höchstens 70.000 Zeichen einschließlich Präfix. Ohne dieses Feld wird ein einfarbiger Hintergrund verwendet. |

Die gesamte Datei darf höchstens 80.000 Bytes groß sein. Theme-Dateien enthalten Daten und keinen Code: Skripte, externe URLs und SVG-Bilddaten werden nicht akzeptiert. Das Format verändert Farben und Hintergrundbild; ab Version 0.2.80 ergänzt es einen wählbaren vorgegebenen Animationseffekt. Freie Animationsskripte und Änderungen am Launcher-Layout werden nicht unterstützt. Eigene oder zur Weitergabe freigegebene Bilder verwenden und bei einer Veröffentlichung Urheber und Lizenz angeben.

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
  "id": "my-first-theme",
  "name": "My first theme",
  "background": "#102030",
  "accent": "#80d0ff",
  "glow": "#4466aa",
  "animation": "neon",
  "animationOptions": {
    "color": "#ff45d4",
    "duration": 4,
    "opacity": 0.75,
    "direction": "alternate"
  },
  "scene": [
    {
      "type": "rect",
      "x": 100,
      "y": 250,
      "width": 180,
      "height": 80,
      "color": "#5bbfd1",
      "animation": {
        "type": "move",
        "duration": 4,
        "dx": 30,
        "dy": 0
      }
    },
    {
      "type": "ellipse",
      "x": 720,
      "y": 45,
      "width": 90,
      "height": 90,
      "color": "#ffd778",
      "animation": {
        "type": "blink",
        "duration": 4
      }
    },
    {
      "type": "polygon",
      "points": [
        [
          600,
          400
        ],
        [
          650,
          300
        ],
        [
          700,
          400
        ]
      ],
      "color": "#4fa977",
      "animation": {
        "type": "sway",
        "duration": 5
      }
    }
  ]
}
```

## Eigene Szenen mit einzelnen Animationen

**Kompatibilität:** Das Feld `scene` wird ab Version **0.2.80** unterstützt. Die ältere veröffentlichte Version 0.2.70 zeichnet diese Szenenelemente nicht. Der Import und die grundsätzliche Darstellung einer Szene wurden vom Nutzer am Fernseher ausprobiert; nicht jede Kombination ist getestet.

`scene` ist eine Liste von höchstens 100 Formen. Die Formen werden in Listenreihenfolge gezeichnet; spätere liegen darüber. Die Koordinaten beziehen sich auf eine Fläche von **1000 × 500**. Das breite TV-Banner kann oben und unten etwas abschneiden.

| Feld | Bedeutung |
| --- | --- |
| `type` | `rect` für Rechteck, `ellipse` für Ellipse oder `polygon` für eine Form aus Eckpunkten. |
| `color` | Füllfarbe als `#RRGGBB`. |
| `x`, `y` | Position bei Rechteck und Ellipse: x von 0 bis 1000, y von 0 bis 500. |
| `width`, `height` | Breite von 1 bis 1000 und Höhe von 1 bis 500 bei Rechteck und Ellipse. |
| `points` | Bei Polygonen 3 bis 40 Punkte als `[[x,y], ...]` mit denselben Koordinatengrenzen. |
| `opacity` | Optional: Deckkraft von 0 bis 1. |
| `animation` | Optionales Objekt mit `type` und `duration`. `move` bewegt hin und zurück, `blink` lässt die Form aufleuchten, `sway` schwenkt sie mit festem Winkel. Dauer: 0.5 bis 60 Sekunden. Bei `move` legen die optionalen Werte `dx` und `dy` zwischen -300 und 300 die Verschiebung fest. |

Animationen müssen in den Launcher-Einstellungen eingeschaltet sein. Die Vorlage enthält für jede Form ein Beispiel. Bestehende Themes ohne `scene` bleiben verwendbar.

