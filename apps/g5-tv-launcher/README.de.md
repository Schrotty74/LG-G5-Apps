# G5 TV Launcher 0.2.28

[English](README.md) · [Deutsch](README.de.md)

Ein eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Die Oberfläche bietet eine anpassbare Favoritenleiste und Schnellzugriffe auf TV-Eingänge.

## Einblicke

Zum Vergrößern auf ein Bild klicken.

<a href="screenshots/overview.jpg"><img src="screenshots/overview-thumb.jpg" alt="Übersicht" width="240"></a>
<a href="screenshots/favorites.jpg"><img src="screenshots/favorites-thumb.jpg" alt="Favoriten" width="240"></a>
<a href="screenshots/inputs.jpg"><img src="screenshots/inputs-thumb.jpg" alt="Eingänge" width="240"></a>

## Funktionen

- Installierte Apps in der Übersicht durchsehen und starten; HDMI-Eingänge und Live TV haben eine eigene Seite „Eingänge“.
- Favoriten in der Glas-Dockleiste hinzufügen, entfernen und sortieren. App-Symbole mit oder ohne Namen anzeigen und für die Ansicht ohne Namen zwischen drei Größen wählen.
- Bedienung mit Steuerkreuz, Zeiger und Mausrad der Magic Remote.
- HDMI 1–4 und Live TV öffnen. HDMI-Namen aus den Startpunkten des Fernsehers übernehmen oder selbst vergeben.
- Zwischen fünf illustrierten Szenen wählen, die im Banner auf Übersicht, Favoriten und Eingängen angezeigt werden.
- Uhr und Wetter getrennt ein- oder ausblenden und einen Wetterstandort wählen.
- Übersicht, Favoriten oder Eingänge als Startseite wählen; die Auswahl gilt auch beim erneuten Öffnen.
- Die Oberfläche zwischen Englisch und Deutsch umschalten; Englisch ist voreingestellt.
- Die Home-Taste optional über Magic Mapper 1.1.2 diesem Launcher zuweisen und die vorherige Belegung wiederherstellen. [Voraussetzungen und Details](#optionale-home-tastenbelegung).
- Launcher-Einstellungen, Favoriten und eigene Eingangsbezeichnungen als JSON-Backup auf dem Fernseher speichern und wiederherstellen.

## Downloads und Quellcode

- [IPK 0.2.28 herunterladen](g5-tv-launcher_0.2.28_all.ipk)
- [Quellcode-ZIP herunterladen](g5-tv-launcher-source_0.2.28.zip)
- [Vollständiger App-Quellcode](app/)
- [Entwicklungsnotizen (English)](DEVELOPMENT.md)
- [Changelog (English)](CHANGELOG.md)

## Installation

Voraussetzungen sind ein gerooteter Fernseher und ein funktionierender Homebrew-Channel-Dienst. Die IPK per SFTP nach `/tmp` übertragen und dann per SSH installieren:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-tv-launcher_0.2.28_all.ipk","subscribe":true}'
```

Alternativ kann die IPK über Glasshouse hochgeladen werden. Die App-ID lautet `org.schrotty74.g5launcher`.

## Hinweise

Der Launcher ist eine normale App. Durch die Installation werden LG Home, die Home-Taste und der Autostart nicht automatisch umgestellt. Er nutzt den Homebrew-Dienst zum Lesen der App-Liste und lokaler App-Symbole; nicht verfügbare Symbole werden durch einen Buchstaben ersetzt. Das Wetter nutzt Open-Meteo und benötigt Internet. Das Backup liegt auf dem Fernseher unter `/media/developer/g5-tv-launcher/backup.json` und kann per SFTP kopiert werden. Eine neue Sicherung ersetzt die vorige. Der Live-TV-Schnellzugriff und die Darstellung sollten auf dem jeweiligen Fernseher geprüft werden.

## Auf dem Mac aus dem Quellcode bauen

Python 3 installieren, das Terminal in diesem App-Ordner öffnen und ausführen:

```sh
python3 build.py
```

Das Paket liegt danach unter `dist/g5-tv-launcher_0.2.28_all.ipk`. Mit `python3 build.py --output /pfad/zum/ausgabeordner` lässt sich ein anderer Ausgabeordner wählen. Das Skript nutzt nur die Python-Standardbibliothek und benötigt keinen festen Pfad auf dem Computer.

## Optionale Home-Tastenbelegung

Für die optionale Home-Tastenbelegung muss [Magic Mapper für webOS 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2) installiert und aktiv sowie für den Start auf dem Fernseher eingerichtet sein. Diese Launcher-Integration prüft auf Version 1.1.2. Weitere Informationen und die Installation über den Homebrew Channel stehen im [Magic-Mapper-Projekt](https://github.com/afonsojramos/magic-mapper-webos#installing-from-homebrew-channel).

In den Einstellungen lässt sich die Home-Taste ausdrücklich diesem Launcher zuweisen. Die bisherige Home-Belegung wird lokal gesichert und kann dort wiederhergestellt werden; andere Tastenbelegungen bleiben erhalten. Vor dem Deinstallieren des Launchers die vorherige Belegung wiederherstellen. Glasshouse Home oder andere Home-Zuordnungen können sich gegenseitig beeinflussen. Die Option installiert Magic Mapper nicht und ändert dessen Autostart-Hook nicht.

Die Startseite kann auf Übersicht, Favoriten oder Eingänge eingestellt werden und gilt auch beim erneuten Öffnen. Die gewählte illustrierte Szene erscheint auf allen drei Seiten im Banner.

## Sprache

Englisch ist die Voreinstellung. Unter Einstellungen → Sprache lässt sich zwischen Englisch und Deutsch wechseln. Die Auswahl wird auf dem Fernseher gespeichert und im Einstellungen-Backup mitgesichert.
