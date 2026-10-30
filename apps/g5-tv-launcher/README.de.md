# G5 TV Launcher 0.2.60

**Testversion 0.2.60:** Direct Home und die Wetteränderungen stehen zum Test bereit. Der Test nach längerem Standby ist noch offen; siehe [Projektstand](PROJECT_STATUS.md).

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
- HDMI 1–4 und Live TV öffnen. HDMI-Namen aus den Startpunkten des Fernsehers übernehmen oder selbst vergeben.
- Zwischen sieben illustrierten Szenen wählen, die im Banner auf Übersicht, Favoriten und Eingängen angezeigt werden. Halloween und Weihnachten sind als Spezial-Themes gruppiert.
- In den TV-Homescreen-Einstellungen zwischen LG Home, der bisherigen Methode und der direkten Home-Übernahme wählen. Direct Home benötigt keinen Magic Mapper; die bisherige Methode bleibt als Rückfalllösung verfügbar.
- Uhr und Wetter getrennt ein- oder ausblenden; einen Standort und Open-Meteo oder GeoSphere Austria über Open-Meteo wählen.
- Übersicht, Favoriten oder Eingänge als Startseite wählen; die Auswahl gilt auch beim erneuten Öffnen.
- Installierte Apps nach Namen suchen.
- Uhrzeit und Wetter unabhängig voneinander vergrößern; Wetterdaten alle 15 Minuten, stündlich, zweimal täglich oder täglich aktualisieren.
- Zwischen Meteocons und Makin’ Things wählen und die Animation für jedes Wettersymbol-Set getrennt ein- oder ausschalten. Der Tag-Nacht-Wechsel nutzt Sonnenauf- und -untergang am Standort.

Die vollständige [Funktionsübersicht](FEATURES.de.md) enthält weitere Details.

## Downloads und Quellcode

- [Aktuelle Test-IPK herunterladen](g5-tv-launcher_0.2.60_all.ipk)
- [Aktuelles Test-Quellcode-ZIP herunterladen](g5-tv-launcher-source_0.2.60.zip)
- [Vollständiger App-Quellcode](app/)
- [Entwicklungsnotizen (English)](DEVELOPMENT.md)
- [Projektstand und Hinweise für die Weiterentwicklung](PROJECT_STATUS.md)
- [Changelog (English)](CHANGELOG.md)

## Installation

Voraussetzungen sind ein gerooteter Fernseher und ein funktionierender Homebrew-Channel-Dienst. Die IPK per SFTP nach `/tmp` übertragen und dann per SSH installieren:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-tv-launcher_0.2.60_all.ipk","subscribe":true}'
```

Alternativ kann die IPK über Glasshouse hochgeladen werden. Die App-ID lautet `org.schrotty74.g5launcher`. Ist die direkte Home-Übernahme aktiv, vor einem Update oder der Deinstallation LG Home wiederherstellen; nach der Installation kann Direct Home erneut aktiviert werden. Siehe [Direct-Home-Test und Wiederherstellung](HOME_TAKEOVER_TEST.md).

## TV-Homescreen

Unter Einstellungen → Start & Home → TV-Homescreen **LG Home**, **Bisherige Methode** oder **Direkte Home-Übernahme** wählen und anschließend **Methode anwenden** drücken. Direct Home verwendet den Launcher als TV-Homescreen und benötigt keinen Magic Mapper. Die bisherige Methode mit Home-Tastenbelegung und Autostart bleibt als Rückfalllösung erhalten. Vor dem Wechsel Glasshouse Home ausschalten. Vor einem Update oder der Deinstallation LG Home wiederherstellen.

Direct Home wurde nach kurzem Standby getestet; der Test nach mehreren Stunden steht noch aus. Weitere Hinweise stehen unter [Test und Wiederherstellung](HOME_TAKEOVER_TEST.md).

## Optionaler Autostart

Für LG Home und die bisherige Methode lässt sich der optionale Launcher-Autostart unter Start & Home ein- und ausschalten. Direct Home nutzt einen eigenen Startmechanismus und schaltet den bisherigen Autostart beim Wechsel ab. Vor der Deinstallation LG Home wiederherstellen und den optionalen Autostart ausschalten.

## Hinweise

Durch die Installation werden LG Home, die Home-Taste und der Autostart nicht automatisch umgestellt; diese Optionen müssen ausdrücklich aktiviert werden. Er nutzt den Homebrew-Dienst zum Lesen der App-Liste und lokaler App-Symbole; nicht verfügbare Symbole werden durch einen Buchstaben ersetzt. Wetter und Standortsuche nutzen Open-Meteo und benötigen Internet; die GeoSphere-Auswahl verwendet das AROME-Modell von GeoSphere Austria über Open-Meteo. Das Backup liegt auf dem Fernseher unter `/media/developer/g5-tv-launcher/backup.json` und kann per SFTP kopiert werden. Eine neue Sicherung ersetzt die vorige. Der Live-TV-Schnellzugriff und die Darstellung sollten auf dem jeweiligen Fernseher geprüft werden.

## Auf dem Mac aus dem Quellcode bauen

Python 3 installieren, das Terminal in diesem App-Ordner öffnen und ausführen:

```sh
python3 build.py
```

Das Paket liegt danach unter `dist/g5-tv-launcher_0.2.60_all.ipk`. Mit `python3 build.py --output /pfad/zum/ausgabeordner` lässt sich ein anderer Ausgabeordner wählen. Das Skript nutzt nur die Python-Standardbibliothek und benötigt keinen festen Pfad auf dem Computer.

## Optionale Home-Tastenbelegung

Für die optionale Home-Tastenbelegung muss [Magic Mapper für webOS 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2) installiert und aktiv sowie für den Start auf dem Fernseher eingerichtet sein. Diese Launcher-Integration prüft auf Version 1.1.2. Weitere Informationen und die Installation über den Homebrew Channel stehen im [Magic-Mapper-Projekt](https://github.com/afonsojramos/magic-mapper-webos#installing-from-homebrew-channel).

In den Einstellungen des Launchers lässt sich die Home-Taste ausdrücklich diesem Launcher zuweisen. Die Home-Taste muss zuvor nicht manuell in Magic Mapper belegt werden; der Launcher richtet die Zuordnung über Magic Mapper ein. Die bisherige Home-Belegung wird lokal gesichert und kann dort wiederhergestellt werden; andere Tastenbelegungen bleiben erhalten. Vor dem Deinstallieren des Launchers die vorherige Belegung wiederherstellen. Glasshouse Home oder andere Home-Zuordnungen können sich gegenseitig beeinflussen. Die Option installiert Magic Mapper nicht und ändert dessen Autostart-Hook nicht.

Die Startseite kann auf Übersicht, Favoriten oder Eingänge eingestellt werden und gilt auch beim erneuten Öffnen. Die gewählte illustrierte Szene erscheint auf allen drei Seiten im Banner.

## Sprache

Englisch ist die Voreinstellung. Unter Einstellungen → Sprache lässt sich zwischen Englisch und Deutsch wechseln. Die Auswahl wird auf dem Fernseher gespeichert und im Einstellungen-Backup mitgesichert.

