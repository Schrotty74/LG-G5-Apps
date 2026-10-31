# LG-G5-Apps

[English](README.md) · [Deutsch](README.de.md)

Homebrew-Apps und Werkzeuge für LG-Fernseher der G-Serie. Jede App hat ein eigenes Verzeichnis mit vollständigem Quellcode, Bau- und Installationshinweisen sowie herunterladbaren webOS-Paketen.

| Icon | App | Kurzbeschreibung | Quellcode, Downloads und Anleitung | Kontext |
|---|---|---|---|---|
| <img src="apps/system-monitor/app/icon.png" width="72" alt="G5 System Monitor"> | [G5 System Monitor](apps/system-monitor/README.de.md) | Nur lesendes Dashboard für CPU, RAM, Laufzeit, Systeminformationen, Speicherplatz, Netzwerk und aktive Prozesse | [English](apps/system-monitor/README.md) · [Deutsch](apps/system-monitor/README.de.md) · [IPK 0.9.3](https://github.com/Schrotty74/LG-G5-Apps/raw/refs/heads/main/apps/system-monitor/g5-system-monitor_0.9.3_all.ipk) · [Quellcode-ZIP](apps/system-monitor/g5-system-monitor-source-v0.9.3.zip) · [Quellcode](apps/system-monitor/app/) | [Entwicklungsnotizen](apps/system-monitor/DEVELOPMENT.md) · [Changelog (English)](apps/system-monitor/CHANGELOG.md) · [Vorschau](apps/system-monitor/preview.png) |
| <img src="apps/g5-tv-launcher/app/icon.png" width="72" alt="G5 TV Launcher"> | [G5 TV Launcher](apps/g5-tv-launcher/README.de.md) | Anpassbarer Homebrew-Launcher mit Favoriten, illustrierten Hintergründen, Wetter und Eingängen | [English](apps/g5-tv-launcher/README.md) · [Deutsch](apps/g5-tv-launcher/README.de.md) · [IPK 0.2.70](apps/g5-tv-launcher/g5-tv-launcher_0.2.70_all.ipk) · [Quellcode-ZIP](apps/g5-tv-launcher/g5-tv-launcher-source_0.2.70.zip) · [Quellcode](apps/g5-tv-launcher/app/) | [Entwicklungsnotizen (English)](apps/g5-tv-launcher/DEVELOPMENT.md) · [Changelog (English)](apps/g5-tv-launcher/CHANGELOG.md) |

G5 System Monitor 0.9.3 ist das aktuelle Paket. Die UI-Vorschau ist eine Darstellung anhand des App-Quellcodes. Alle darin gezeigten Werte sind Demodaten und keine Aufnahme vom Fernseher.

## App-Katalog für Glasshouse und Homebrew Channel

Der [G5-Apps-Katalog](repo.json) enthält die veröffentlichten Versionen von G5 TV Launcher und G5 System Monitor.

Der Katalog wird beim Veröffentlichen eines GitHub-Releases automatisch aktualisiert, wenn die passende IPK als Release-Datei vorliegt. Vorabversionen und Testpakete bleiben unberücksichtigt. Änderungen an einer bereits veröffentlichten Release-Seite starten den Ablauf nicht erneut.

**Glasshouse**

1. Glasshouse öffnen und zu **Apps → Other app catalogs** wechseln.
2. Die Option zum Hinzufügen eines Katalogs wählen und diese Repository-Adresse eingeben:
   `https://github.com/Schrotty74/LG-G5-Apps`
3. Den Katalog hinzufügen. Die beiden Apps erscheinen anschließend zur Auswahl und Installation.

**Homebrew Channel**

1. Den Homebrew Channel auf dem Fernseher öffnen und **Settings → Add repository** wählen.
2. Die direkte Katalog-Adresse eingeben und hinzufügen:
   `https://raw.githubusercontent.com/Schrotty74/LG-G5-Apps/main/repo.json`
3. Die Apps im Katalog auswählen und installieren.

Das Hinzufügen in Glasshouse wurde auf einem Fernseher getestet. Die Einrichtung im Homebrew Channel ist noch nicht auf einem Fernseher getestet.

## Glasshouse-Bildschirmschoner

[Retro-Gaming und Jahreszeiten herunterladen](screensavers/g5-glasshouse-screensavers.zip). Die Bildschirmschoner benötigen Glasshouse auf einem gerooteten Fernseher. Retro-Gaming wurde auf einem LG G5 ausprobiert; die überarbeitete Jahreszeiten-Version ist noch nicht am Fernseher bestätigt.

1. Die ZIP-Datei per SFTP, etwa mit Termius, nach `/tmp` auf den Fernseher übertragen.
2. Per SSH verbinden und die beiden Ordner entpacken:

   ```sh
   mkdir -p /var/lib/tvweb/screensavers && unzip -n /tmp/g5-glasshouse-screensavers.zip -d /var/lib/tvweb/screensavers
   ```

3. In Glasshouse **Screensaver** öffnen und **Retro-Gaming** oder **Jahreszeiten** auswählen. Für einen sofortigen Test eine webOS-App am Fernseher öffnen und **Start screen saver** wählen. Eine Fernbedienungstaste beendet die Anzeige.

`unzip -n` überschreibt keine vorhandenen Dateien. Bei einer bestehenden älteren Testversion müssen die Dateien gezielt aktualisiert und das Motiv anschließend in Glasshouse erneut ausgewählt werden.

## IPK installieren

1. Die gewünschte `.ipk`-Datei herunterladen und per SFTP, zum Beispiel nach `/tmp` auf den Fernseher übertragen.
2. Per SSH als root mit dem Fernseher verbinden.
3. Den Befehl ausführen und `DATEINAME.ipk` durch den genauen Dateinamen ersetzen:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/DATEINAME.ipk","subscribe":true}'
```

Der Installationsdienst zeigt den Fortschritt im Terminal an. Nach erfolgreicher Installation erscheint die App im Launcher. Root-Zugriff und eine funktionierende Homebrew-Umgebung sind erforderlich.

## Weitere Apps hinzufügen

Jede neue App erhält ein eigenes Verzeichnis unter `apps/<app-name>/`. Ergänze sie anschließend als neue Tabellenzeile mit Links zum Quellcode, Paket, zur Dokumentation und zum Arbeitskontext.

Im Repository bleiben pro App die drei neuesten IPK-Pakete und die zugehörigen Quellcode-ZIPs verfügbar, einschließlich Testversionen.

## Themes für den G5 TV Launcher

[Themes herunterladen, importieren und selbst erstellen](apps/g5-tv-launcher/themes/README.de.md). Der Theme-Import ist ab Version 0.2.70 im verlinkten Paket enthalten.
