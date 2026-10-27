# Entwicklungsnotizen – G5 System Monitor

Diese Datei hält den technischen Stand und die Entscheidungen fest, damit spätere Arbeit am Projekt darauf aufbauen kann.

## Aktueller Stand

- Version: **0.9.2**
- Paket-ID: `org.schrotty74.g5systemmonitor`
- Zielgerät: gerooteter LG G5 mit webOS 25 und Homebrew Channel
- GitHub: [`Schrotty74/LG-G5-Apps`](https://github.com/Schrotty74/LG-G5-Apps), App-Verzeichnis `apps/system-monitor/`
- Die App ist eine schlanke Web-App aus HTML, CSS und JavaScript. Es gibt keine zusätzlichen Framework-Abhängigkeiten.
- Das Dashboard zeigt CPU und RAM samt Verlauf, Laufzeit, Kernel, Root-Status, Modell/Firmware/SDK/Board, Dateisysteme, Netzwerk und Prozessmomentaufnahme.
- Aktualisierungsintervall: 3, 5 oder 10 Sekunden; die Auswahl gilt nur während der Sitzung.
- Fernbedienungsnavigation, Zurück-/Beenden-Schaltfläche und Mausrad-Scrollen sind enthalten.
- Es gibt kein Temperaturfeld. Am G5 waren über `/sys/class/thermal` und `/sys/class/hwmon` keine nutzbaren Sensorwerte auffindbar; die geprüfte `dmesg`-Ausgabe lieferte ebenfalls keinen Temperaturwert.

## Aufbau und Datenquellen

- `app/index.html`: Dashboard-Kacheln, Diagramme, Prozessliste und Aktionsschaltflächen.
- `app/style.css`: dunkles blaues Dashboard, responsive Kachelraster, Speicherbalken, Fokus- und Scrollgestaltung.
- `app/script.js`: Abfragen, Parsing, Aktualisierung, Diagrammverläufe und Bedienlogik.
- `app/appinfo.json`: webOS-Metadaten und App-Version.
- `app/icon.png`: App-Symbol.
- `g5-system-monitor_0.9.2_all.ipk`: installierbares Paket.
- `g5-system-monitor-source-v0.9.2.zip`: Quellcode-Archiv.

Für Messwerte wird ein fest kodierter, ausschließlich lesender Shell-Befehl über `org.webosbrew.hbchannel.service/exec` ausgeführt. Die App verwendet `webOS.service.request` und fällt auf `PalmServiceBridge` zurück. Systemwerte stammen unter anderem aus `/proc/stat`, `/proc/meminfo`, `/proc/uptime`, `uname`, `id`, `top`, `df`, `/sys/class/net`, `ip` und ersatzweise `ifconfig`. Modell, Firmware, SDK- und Boardangaben werden über `com.webos.service.tv.systemproperty/getSystemInfo` abgefragt.

Die CPU-Werte aus `top` sind Momentaufnahmen. Es sind keine Langzeitmittelwerte. Die Verläufe speichern höchstens 30 Messpunkte nur im Arbeitsspeicher der laufenden App.

## Stand und bekannte UI-Beobachtung

Der Nutzer hat frühere Builds am Fernseher verwendet und CPU, RAM, Laufzeit, Firmware-/Modellinformationen, Prozessliste sowie Fernbedienungs- und Mausradbedienung gesehen. Beim Speicherplatz gab es zunächst überlagerte Werte durch lange Mount-Pfade; die aktuelle Darstellung bricht Pfad und Werte in der Kachel untereinander um.

Die Entwicklung seit dem ersten dokumentierten Build ist in `CHANGELOG.md` nach Versionen festgehalten. In der Reihenfolge kamen hinzu: Scrollen zur Prozessliste; Firmware-/SDK-Abfrage und Prüfung der Sensorschnittstellen; Temperaturfeld entfernen und App sauber über Zurück-Taste/Beenden verlassen; Mausradbedienung; Modell-, Firmware- und Boarddaten sowie Speicher- und Netzwerkwerte; RAM-Verlauf, Speicherbalken und einstellbares Messintervall; räumlichere Kacheln; robustes Layout langer Mount-Pfade; Abschwächung der Schattenkante.

> Das aktuelle Foto zeigt an Kacheln eine zweite Kontur beziehungsweise einen Schatten, der wie eine überlagerte Kachel wirkt. Version 0.9.2 schwächt die harten, versetzten Schlagschatten ab. Beim nächsten TV-Test sollte geprüft werden, ob die Kontur damit verschwunden ist. Falls noch sichtbar, gezielt `box-shadow` und Randgestaltung in `app/style.css` prüfen; das dunkle Dashboard-Design beibehalten.

Die README-Datei beschreibt Installation und Nutzung. Dieses Dokument ist die technische Übergabe für spätere Weiterentwicklung; `CHANGELOG.md` bewahrt die Entwicklungsschritte und Nutzeranforderungen über die Versionen.

## Paket und Prüfungen

Für einen normalen webOS-CLI-Build:

```sh
ares-package ./app -o ./dist
```

Das hier veröffentlichte IPK wurde in der Build-Umgebung ohne `ares-package` im üblichen IPK-Archivformat erzeugt. Geprüft wurden Paketmetadaten und Archivstruktur, die Übereinstimmung der enthaltenen App-Dateien mit dem Quellcode, JavaScript-Syntax (`node --check`) und ZIP-Integrität (`unzip -t`). Diese Prüfungen ersetzen keinen Test des konkreten Pakets auf dem Fernseher.

Installationshinweise und der bisher verwendete Luna-Installationsbefehl stehen in `README.md`. Installation auf dem TV nur nach ausdrücklicher Zustimmung des Nutzers durchführen.

## Leitplanken für weitere Änderungen

- Dunkles Dashboard und deutsche Beschriftungen erhalten.
- Keine Änderungen an Systempartitionen, Firmware, Root-Konfiguration oder Autostart. Keine dauerhaften Hintergrunddienste.
- Keine frei eingebbaren Shell-Befehle in die App aufnehmen; die privilegierte Luna-Exec-Schnittstelle muss auf feste, lesende Abfragen begrenzt bleiben.
- Keine Temperaturanzeige ergänzen, solange kein realer Sensorpfad samt plausibler Messwerte nachgewiesen ist.
- Keine privaten IP-Adressen, Zugangsdaten, SSH-Schlüssel, internen Pfade oder TV-Kennungen in Quellcode oder öffentliche Dokumente aufnehmen.
- Version, Paketdateiname und Dokumentation zusammenhalten. Versionsnummern nur nach ausdrücklichem Auftrag ändern.
- Vor dem Hochladen Quellcode, Paket und Dokumentation auf private Daten prüfen. Ein Build allein gilt nicht als erfolgreicher Gerätetest.
