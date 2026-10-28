# G5 TV Launcher 0.2.19

[English](README.md) · [Deutsch](README.de.md)

Ein eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Die Oberfläche bietet eine anpassbare Favoritenleiste und Schnellzugriffe auf TV-Eingänge.

## Funktionen

- Installierte Apps in der Übersicht durchsehen und starten
- Favoriten hinzufügen, entfernen und sortieren; App-Symbole mit oder ohne Namen anzeigen und für die Ansicht ohne Namen zwischen drei Größen wählen
- Bedienung mit Steuerkreuz, Zeiger und Mausrad der Magic Remote
- HDMI 1–4 und Live TV über den Reiter „Eingänge“ öffnen; HDMI-Namen aus den TV-Startpunkten übernehmen oder im Launcher selbst vergeben
- Fünf illustrierte Hintergrundszenen; Uhr und Wetter optional anzeigen
- Launcher-Einstellungen als JSON-Backup exportieren und importieren

## Downloads und Quellcode

- [IPK 0.2.19 herunterladen](g5-tv-launcher_0.2.19_all.ipk)
- [Quellcode-ZIP herunterladen](g5-tv-launcher-source_0.2.19.zip)
- [Vollständiger App-Quellcode](app/)
- [Entwicklungsnotizen (English)](DEVELOPMENT.md)

## Installation

Voraussetzungen sind ein gerooteter Fernseher und ein funktionierender Homebrew-Channel-Dienst. Die IPK per SFTP nach `/tmp` übertragen und dann per SSH installieren:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-tv-launcher_0.2.19_all.ipk","subscribe":true}'
```

Alternativ kann die IPK über Glasshouse hochgeladen werden. Die App-ID lautet `org.schrotty74.g5launcher`.

## Hinweise

Der Launcher ist eine normale App. Durch die Installation werden LG Home, die Home-Taste und der Autostart nicht automatisch umgestellt. Er nutzt den Homebrew-Dienst zum Lesen der App-Liste und lokaler App-Symbole; nicht verfügbare Symbole werden durch einen Buchstaben ersetzt. Das Wetter nutzt Open-Meteo und benötigt Internet. Download und Wiederherstellung der Backup-Datei hängen von der Web-Laufzeit des Fernsehers ab. Der Live-TV-Schnellzugriff und die Darstellung sollten auf dem jeweiligen Fernseher geprüft werden.

## Auf dem Mac aus dem Quellcode bauen

Python 3 installieren, das Terminal in diesem App-Ordner öffnen und ausführen:

```sh
python3 build.py
```

Das Paket liegt danach unter `dist/g5-tv-launcher_0.2.19_all.ipk`. Mit `python3 build.py --output /pfad/zum/ausgabeordner` lässt sich ein anderer Ausgabeordner wählen. Das Skript nutzt nur die Python-Standardbibliothek und benötigt keinen festen Pfad auf dem Computer.
