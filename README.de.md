![LG G5 Apps](assets/lg-g5-apps-logo.jpg)

# LG-G5-Apps

Kleine Homebrew-Apps und Werkzeuge für LG-Fernseher der G-Serie. Jede App liegt mit Quellcode und Downloads in einem eigenen Verzeichnis unter `apps/`.

[English](README.md) | [Deutsch](README.de.md)

## Apps

### G5 System Monitor

Ein lokales, nur lesendes Dashboard für einen gerooteten LG G5 mit webOS 25. Es zeigt CPU- und RAM-Auslastung, Systemlaufzeit, Firmware- und Modellinformationen, Dateisystembelegung, Netzwerkstatus sowie eine Prozessmomentaufnahme. CPU- und RAM-Verläufe, ein einstellbares Aktualisierungsintervall und die Bedienung per Fernbedienung und Mausrad sind enthalten.

- **Aktuelle Version:** 0.9.2
- **IPK herunterladen:** [G5 System Monitor 0.9.2](https://github.com/Schrotty74/LG-G5-Apps/raw/refs/heads/main/apps/system-monitor/g5-system-monitor_0.9.2_all.ipk)
- **Quellcode und Installationshinweise:** [apps/system-monitor](apps/system-monitor/)
- **Änderungsprotokoll:** [Changelog (English): alle Versionen und Änderungen](apps/system-monitor/CHANGELOG.md)

Die App benötigt den Homebrew Channel und dessen Luna-Exec-Dienst. Sie startet keine Hintergrunddienste und verändert keine Systemdateien oder Autostart-Einstellungen. Temperaturwerte werden nicht angezeigt, weil am getesteten Gerät kein auslesbarer Sensor verfügbar war.

## IPK auf webOS installieren

1. Die gewünschte `.ipk`-Datei herunterladen und per SFTP, zum Beispiel mit Termius, nach `/tmp` auf den Fernseher übertragen.
2. Per SSH als root mit dem Fernseher verbinden.
3. Den folgenden Befehl ausführen und `DATEINAME.ipk` durch den tatsächlichen Dateinamen ersetzen:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/DATEINAME.ipk","subscribe":true}'
```

Der Installationsdienst meldet den Status im Terminal. Bei Erfolg erscheint die App im Launcher. Dieser Weg setzt Root-Zugriff und eine installierte Homebrew-Umgebung voraus. Die Pakete in diesem Repository sind webOS-IPKs, keine Android-APKs.

## Weitere Apps hinzufügen

Jede weitere App erhält ein eigenes Verzeichnis unter `apps/<app-name>/`; die Übersicht wird anschließend hier ergänzt.
