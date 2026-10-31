# Launcher-Quellcode-Zwischenstände

Dieser Ordner ist für Quellcode-ZIPs lokaler Testversionen vorgesehen. Der Dateiname enthält die Testversion, zum Beispiel `g5-launcher-zwischenstand_0.2.61.zip`.

- Nach jeder lokalen Testversion ein zugehöriges Quellcode-ZIP erstellen und hier sichern.
- Nur die drei neuesten Quellcode-Zwischenstände im aktuellen Ordner behalten; ältere Zwischenstands-ZIPs erst nach erfolgreicher Sicherung des neuen Stands entfernen. Die regulären IPK-/Quellcode-Paare zählen separat.
- Vor dem Upload Inhalt und Metadaten auf private Daten und Zugangsdaten prüfen. Keine TV-Einstellungen, Nutzerdaten, Zugangsdaten oder privaten Pfade veröffentlichen.
- Test-IPKs bleiben lokal, bis ihr Upload ausdrücklich beauftragt wird.
- Die Zwischenstände ersetzen weder die regulären IPK-/Quellcode-Paare im Launcher-Verzeichnis noch einen Release-Changelog. Der [Projektstand](../PROJECT_STATUS.md) hält fest, was getestet wurde und was noch offen ist.

## Gesicherte Zwischenstände vom 30. Oktober 2026

- **0.2.63:** Prüft Magic Mapper beim Direct-Home-Start nicht mehr; Diagnoseprotokoll bleibt erhalten. Übergang von der älteren Methode berücksichtigt deren Rückbau. Vom Nutzer installiert; Kurztest zeigte nach dem Einschalten LG Home, genaue Ursache offen. Der längere Standby-Test am 31. Oktober war beim Launcher-Start erfolgreich; Wetter zunächst nicht verfügbar.

Die Angaben beschreiben lokale Tests, keine veröffentlichten Versionen. Bei allen drei Versionen wurden automatisierte lokale Prüfungen durchgeführt; sie ersetzen keinen Fernsehtest.

- **0.2.64:** Zusätzliche Wetterabfrage fünf Sekunden nach Start, Wiederöffnen oder Sichtbarwerden; reguläres Intervall bleibt erhalten. Lokale Tests bestanden; Fernsehtest steht aus.

- **0.2.65:** Wetter-Nachabruf aus 0.2.64 und zusätzliche Option für analoge Uhr; laufender Entwicklungsstand, Gerätetest steht aus.

## Verbindlicher Ablauf je Testversion

Vor der Übergabe einer Test-IPK: Versionsnummern abgleichen, den dazugehörigen Quellcode als ZIP erstellen und prüfen, hier auf GitHub sichern, den Projektstand samt Änderungen und tatsächlichem Teststatus aktualisieren und die veröffentlichten Dateien überprüfen. Nur die drei neuesten Zwischenstands-ZIPs behalten. Die Test-IPK selbst bleibt lokal. Wenn die GitHub-Sicherung scheitert, den Fehler ausdrücklich melden und nicht behaupten, das Backup sei abgeschlossen.
