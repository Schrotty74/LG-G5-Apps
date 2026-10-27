# Änderungsprotokoll

## 0.9.2

- Harte, versetzte Kachelschatten abgeschwächt, die wie eine zweite Kachelkontur wirkten.
- Weiche Schatten erhalten den räumlichen Eindruck.
- Anlass war das Nutzerfoto mit doppelter Kachelkontur nach den Layout-Verbesserungen. Beim TV-Test prüfen, ob der Schatten jetzt passt.

## 0.9.1

- Speicherplatz-Einträge zeigen Mount-Pfad und Kapazitätswerte untereinander.
- Lange Mount-Pfade umbrechen innerhalb der Kachel.
- Damit werden lange Mount-Namen nicht mehr in die Nachbarkachel oder über die Balken gedrückt.

## 0.9.0

- Räumlichere Kacheln, Glanzkanten und dezente Perspektive ergänzt.
- Fokus auf Schaltflächen hebt diese optisch hervor; reduzierte Bewegung wird berücksichtigt.
- Die bestehende dunkle Dashboard-Optik und die Messfunktionen blieben erhalten.

## 0.8.0

- RAM-Verlauf mit bis zu 30 Messpunkten ergänzt.
- Dateisystembelegung wird zusätzlich als Balken angezeigt.
- Aktualisierungsintervall zwischen 3, 5 und 10 Sekunden wählbar.
- Das Intervall ändert sich nur für die aktuelle Sitzung; die Wahl wird nicht gespeichert.

## 0.7.0

- Modell, SDK-/webOS-TV-Version, Firmware und Boardtyp ergänzt.
- Speicherplatz und Netzwerkstatus ergänzt.
- Speicherwerte kommen aus `df -kP`; Netzwerk wird aus Schnittstellen, IPv4-Adressen und Standardroute zusammengesetzt.

## 0.6.0

- Nicht verfügbare Temperatur-Kachel entfernt.
- Beenden-Schaltfläche und Zurück-Taste der Magic Remote schließen die App über `webOS.platformBack()`.
- Mausrad-Scrollen ergänzt.
- Temperatur wurde nach einer schreibgeschützten Prüfung der verfügbaren Systempfade weggelassen.

## 0.5.0

- Firmware- und SDK-Information über `com.webos.service.tv.systemproperty/getSystemInfo` ergänzt.
- Sensorpfade unter `/sys/class/thermal` und `/sys/class/hwmon` geprüft.
- Der Nutzer hat Modell, Firmware, Boardtyp und SDK-Version über den Luna-Dienst am Gerät ausgelesen. SDK-Version und Marketingname webOS 25 sind unterschiedliche Bezeichnungen; die App zeigt die getrennten Systemfelder.

## 0.4.0

- Scrollen mit Steuerkreuz und Bild-auf/Bild-ab ergänzt.
- Prozessbereich fokussierbar gemacht.
- Damit wurde die Prozessliste am Fernseher auch außerhalb des ersten sichtbaren Bildschirms erreichbar.

## 0.3.0

- Grundlage: CPU-Auslastung, RAM, Systemlaufzeit, Kernel, Root-Status, CPU-Verlauf und Prozessmomentaufnahme.
- Homebrew-Luna-Endpunkt und Antwortverarbeitung angepasst.
- Parsing der Prozessliste für unterschiedliche `top`-Ausgaben robuster gemacht.
- Verspätete Antworten nach Zeitüberschreitung werden ignoriert.
- Erstes installierbares IPK erstellt.
