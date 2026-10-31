# Launcher-Quellcode-Zwischenstände

Dieser Ordner ist für Quellcode-ZIPs lokaler Testversionen vorgesehen. Der Dateiname enthält die Testversion, zum Beispiel `g5-launcher-zwischenstand_0.2.61.zip`.

- Nach jeder lokalen Testversion ein zugehöriges Quellcode-ZIP erstellen und hier sichern.
- Nur die drei neuesten Quellcode-Zwischenstände im aktuellen Ordner behalten; ältere Zwischenstands-ZIPs erst nach erfolgreicher Sicherung des neuen Stands entfernen. Die regulären IPK-/Quellcode-Paare zählen separat.
- Vor dem Upload Inhalt und Metadaten auf private Daten und Zugangsdaten prüfen. Keine TV-Einstellungen, Nutzerdaten, Zugangsdaten oder privaten Pfade veröffentlichen.
- Test-IPKs bleiben lokal, bis ihr Upload ausdrücklich beauftragt wird.
- Die Zwischenstände ersetzen weder die regulären IPK-/Quellcode-Paare im Launcher-Verzeichnis noch einen Release-Changelog. Der [Projektstand](../PROJECT_STATUS.md) hält fest, was getestet wurde und was noch offen ist.

## Gesicherte Zwischenstände vom 30. Oktober 2026


Die Angaben beschreiben lokale Tests, keine veröffentlichten Versionen. Bei allen drei Versionen wurden automatisierte lokale Prüfungen durchgeführt; sie ersetzen keinen Fernsehtest.











- **Cyberpunk-Fenster-Test (intern 0.2.70):** Kräftigere Neonfarben, verstärktes Neonlicht und wechselnd leuchtende Fenster im integrierten Cyberpunk-Theme. Die allgemeine Animationseinstellung steuert beides. Lokale Tests und Paketprüfung bestanden; Fernsehtest steht aus. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.70-cyberwindows-test.zip).

- **Cyberpunk-Stadt-Test (intern 0.2.70):** Fenster in allen Gebäuden, leuchtende Fenstergruppen und animierte Bodenlinien. 31 automatisierte Tests sowie SVG-, IPK- und ZIP-Prüfung bestanden; Fernsehtest steht aus. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.70-cyber-city-test.zip).

- **Konfigurierbare Theme-Effekte (intern 0.2.70):** Optionale Farbe, Dauer, Deckkraft und Richtung für importierte Animationen. Vorhandene Themes bleiben kompatibel. Lokale Validierungs- und Paketprüfungen bestanden; Fernsehtest steht aus. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.70-effect-options.zip).

## Verbindlicher Ablauf je Testversion

Vor der Übergabe einer Test-IPK: Versionsnummern abgleichen, den dazugehörigen Quellcode als ZIP erstellen und prüfen, hier auf GitHub sichern, den Projektstand samt Änderungen und tatsächlichem Teststatus aktualisieren und die veröffentlichten Dateien überprüfen. Nur die drei neuesten Zwischenstands-ZIPs behalten. Die Test-IPK selbst bleibt lokal. Wenn die GitHub-Sicherung scheitert, den Fehler ausdrücklich melden und nicht behaupten, das Backup sei abgeschlossen.
