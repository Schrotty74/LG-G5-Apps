# LG-G5-Apps

[English](README.md) · [Deutsch](README.de.md)

Homebrew-Apps und Werkzeuge für LG-Fernseher der G-Serie. Jede App hat ein eigenes Verzeichnis mit vollständigem Quellcode, Bau- und Installationshinweisen sowie herunterladbaren webOS-Paketen.

| Icon | App | Kurzbeschreibung | Quellcode, Downloads und Anleitung | Kontext |
|---|---|---|---|---|
| <img src="apps/system-monitor/app/icon.png" width="72" alt="G5 System Monitor"> | [G5 System Monitor](apps/system-monitor/README.de.md) | Nur lesendes Dashboard für CPU, RAM, Laufzeit, Systeminformationen, Speicherplatz, Netzwerk und aktive Prozesse | [English](apps/system-monitor/README.md) · [Deutsch](apps/system-monitor/README.de.md) · [IPK 0.9.2](https://github.com/Schrotty74/LG-G5-Apps/raw/refs/heads/main/apps/system-monitor/g5-system-monitor_0.9.2_all.ipk) · [Quellcode-ZIP](apps/system-monitor/g5-system-monitor-source-v0.9.2.zip) · [Quellcode](apps/system-monitor/app/) | [Entwicklungsnotizen](apps/system-monitor/DEVELOPMENT.md) · [Changelog (English)](apps/system-monitor/CHANGELOG.md) · [Vorschau](apps/system-monitor/preview.png) |
| <img src="apps/g5-tv-launcher/app/icon.png" width="72" alt="G5 TV Launcher"> | [G5 TV Launcher](apps/g5-tv-launcher/README.de.md) | Anpassbarer Homebrew-Launcher mit Favoriten, illustrierten Hintergründen, Wetter und Eingängen | [English](apps/g5-tv-launcher/README.md) · [Deutsch](apps/g5-tv-launcher/README.de.md) · [IPK 0.2.21](apps/g5-tv-launcher/g5-tv-launcher_0.2.21_all.ipk) · [Quellcode-ZIP](apps/g5-tv-launcher/g5-tv-launcher-source_0.2.21.zip) · [Quellcode](apps/g5-tv-launcher/app/) | [Entwicklungsnotizen (English)](apps/g5-tv-launcher/DEVELOPMENT.md) |

G5 System Monitor 0.9.2 ist das aktuelle Paket. Die UI-Vorschau ist eine Darstellung anhand des App-Quellcodes. Alle darin gezeigten Werte sind Demodaten und keine Aufnahme vom Fernseher.

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
