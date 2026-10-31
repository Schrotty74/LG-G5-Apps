# Launcher-Quellcode-Zwischenstände

Dieser Ordner ist für Quellcode-ZIPs lokaler Testversionen vorgesehen. Der Dateiname enthält die Testversion, zum Beispiel `g5-launcher-zwischenstand_0.2.61.zip`.

- Nach jeder lokalen Testversion ein zugehöriges Quellcode-ZIP erstellen und hier sichern.
- Nur die drei neuesten Quellcode-Zwischenstände im aktuellen Ordner behalten; ältere Zwischenstands-ZIPs erst nach erfolgreicher Sicherung des neuen Stands entfernen. Die regulären IPK-/Quellcode-Paare zählen separat.
- Vor dem Upload Inhalt und Metadaten auf private Daten und Zugangsdaten prüfen. Keine TV-Einstellungen, Nutzerdaten, Zugangsdaten oder privaten Pfade veröffentlichen.
- Test-IPKs bleiben lokal, bis ihr Upload ausdrücklich beauftragt wird.
- Die Zwischenstände ersetzen weder die regulären IPK-/Quellcode-Paare im Launcher-Verzeichnis noch einen Release-Changelog. Der [Projektstand](../PROJECT_STATUS.md) hält fest, was getestet wurde und was noch offen ist.

## Gesicherte Zwischenstände vom 30. Oktober 2026


Die Angaben beschreiben lokale Tests, keine veröffentlichten Versionen. Bei allen drei Versionen wurden automatisierte lokale Prüfungen durchgeführt; sie ersetzen keinen Fernsehtest.





- **0.2.68:** Getrennte Theme-Kategorien und Anzeige nur gültiger Theme-JSON-Dateien aus /tmp. Nutzer meldet 0.2.67-Import erfolgreich. Lokal geprüft, TV-Test der Änderungen steht aus.

- **0.2.69:** Theme-JSON-Eingabefeld nach erfolgreichem Import leeren; ungültige Eingaben zur Korrektur erhalten. Simulierter Oberflächentest und lokale Tests bestanden; TV-Test steht aus.

- **0.2.70 Watch-Fix-Test:** Verhindert die automatische Home-Rücksetzung allein wegen fehlender Lebenszeichen; die manuelle Wiederherstellung bleibt verfügbar. Die Updateprüfung verwendet 0.2.70 als Vergleichsversion. Intern weiterhin 0.2.70; keine veröffentlichte IPK. Automatisierte Prüfungen bestanden, Fernsehtest steht aus. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.70-watch-fix.zip).

## Verbindlicher Ablauf je Testversion

Vor der Übergabe einer Test-IPK: Versionsnummern abgleichen, den dazugehörigen Quellcode als ZIP erstellen und prüfen, hier auf GitHub sichern, den Projektstand samt Änderungen und tatsächlichem Teststatus aktualisieren und die veröffentlichten Dateien überprüfen. Nur die drei neuesten Zwischenstands-ZIPs behalten. Die Test-IPK selbst bleibt lokal. Wenn die GitHub-Sicherung scheitert, den Fehler ausdrücklich melden und nicht behaupten, das Backup sei abgeschlossen.
