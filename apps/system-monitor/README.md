# G5 System Monitor 0.8.0

Read-only System-Dashboard für den LG G5 mit webOS 25 und Homebrew Channel.

## Funktionen

- CPU- und RAM-Auslastung mit jeweils bis zu 30 Verlaufsmessungen
- Systemlaufzeit, Kernel, Root-Status und Momentaufnahme der zehn Prozesse aus `top`
- Modell, Firmware-, SDK- und Board-Informationen über den webOS-Systemproperty-Dienst
- Belegung erkannter Dateisysteme als Balken
- Aktive Netzwerkschnittstellen, IPv4-Adressen und Standard-Gateway
- Aktualisierungsintervall im Dashboard zwischen 3, 5 und 10 Sekunden umschaltbar
- Navigation per Steuerkreuz und Mausrad; Beenden per Fernbedienung-Zurück-Taste oder Schaltfläche

Temperatur wird nicht angezeigt, weil auf dem getesteten Gerät über die geprüften Sensor-Schnittstellen kein Messwert verfügbar war.

## Download und Installation

Das webOS-Paket ist eine `.ipk`-Datei, keine Android-APK. Lade [g5-system-monitor_0.8.0_all.ipk](g5-system-monitor_0.8.0_all.ipk) herunter und übertrage sie per SFTP nach `/tmp/g5-system-monitor_0.8.0_all.ipk`. Dann per SSH auf dem Fernseher installieren:

```sh
luna-send -i -f 'luna://com.webos.appInstallService/dev/install' '{"id":"com.ares.defaultName","ipkUrl":"/tmp/g5-system-monitor_0.8.0_all.ipk","subscribe":true}'
```

Erfordert Root-Zugriff und den Homebrew-Luna-Dienst. Dieses Paket wurde noch nicht auf dem Fernseher getestet; vorherige App-Versionen wurden dort vom Nutzer erfolgreich geprüft.

## Quellcode und Paket bauen

- `app/appinfo.json` – webOS-App-Metadaten
- `app/index.html`, `app/style.css`, `app/script.js` – Oberfläche, Darstellung und Messlogik
- `app/icon.png` – App-Symbol

Mit der LG webOS TV CLI im App-Verzeichnis bauen:

```sh
ares-package ./app -o ./dist
```

## Sicherheitsverhalten

Die App führt über den Homebrew-Dienst ausschließlich fest vorgegebene, lesende Systemabfragen aus. Sie ändert keine Systempartitionen, Firmware, Root-Konfiguration oder Autostart-Einstellungen und startet keinen Hintergrunddienst. Sie enthält keine frei eingebbare Shell.
