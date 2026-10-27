# G5 System Monitor 0.9.2

Homebrew-Dashboard für LG G5 mit webOS 25. Die Oberfläche zeigt Systemwerte in einem dunklen, TV-gerechten Layout.

## Funktionen

- CPU- und RAM-Auslastung mit Verläufen der letzten 30 Messungen
- Laufzeit, Kernel, Root-Status, Modell, Firmware, SDK- und Boardinformationen
- Dateisysteme mit freier/belegter Kapazität und Balkenanzeige
- Aktive Netzwerkschnittstelle, IPv4-Adresse und Standard-Gateway
- Prozessmomentaufnahme und Swap-Belegung
- Aktualisierungsintervall von 3, 5 oder 10 Sekunden
- Scrollen per Magic Remote, Zurück-/Beenden-Schaltfläche und Mausrad
- Kein Temperaturfeld: auf dem getesteten G5 ließ sich kein Sensorwert auslesen

## Dateien

- `app/` enthält den vollständigen App-Quellcode einschließlich Symbol
- [IPK herunterladen](g5-system-monitor_0.9.2_all.ipk)
- [Quellcode als ZIP herunterladen](g5-system-monitor-source-v0.9.2.zip)

## Installation

Die IPK-Datei auf den Fernseher übertragen, zum Beispiel nach `/tmp`, und anschließend als root über den webOS-Installationsdienst installieren:

```sh
luna-send-pub -i 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-system-monitor_0.9.2_all.ipk","subscribe":true}'
```

Die App-ID lautet `org.schrotty74.g5systemmonitor`. Bei einer Aktualisierung die vorhandene Installation mit derselben Paket-ID aktualisieren. Vor dem Befehl den tatsächlichen Dateipfad prüfen.

## Sicherheit und Grenzen

Die App liest Werte über den vorhandenen Homebrew-Luna-Dienst und lokale Systemdateien. Sie stellt keine frei eingebbaren Shell-Befehle bereit, startet keinen Hintergrunddienst und ändert weder Systempartitionen noch Firmware, Root-Konfiguration oder Autostart. Die Aktualisierungseinstellung gilt nur für die laufende Sitzung.

## Version 0.9.2

- Harte, versetzte Schlagschatten entfernt, die wie eine zweite Kachelkante wirkten.
- Weiche Schatten behalten den räumlichen Eindruck.
