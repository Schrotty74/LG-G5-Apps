# Launcher-Quellcode-Zwischenstände

Dieser Ordner ist für Quellcode-ZIPs lokaler Testversionen vorgesehen. Der Dateiname enthält die Testversion, zum Beispiel `g5-launcher-zwischenstand_0.2.61.zip`.

- Nach jeder lokalen Testversion ein zugehöriges Quellcode-ZIP erstellen und hier sichern.
- Nur die drei neuesten Quellcode-Zwischenstände im aktuellen Ordner behalten; ältere Zwischenstands-ZIPs erst nach erfolgreicher Sicherung des neuen Stands entfernen. Die regulären IPK-/Quellcode-Paare zählen separat.
- Vor dem Upload Inhalt und Metadaten auf private Daten und Zugangsdaten prüfen. Keine TV-Einstellungen, Nutzerdaten, Zugangsdaten oder privaten Pfade veröffentlichen.
- Test-IPKs bleiben lokal, bis ihr Upload ausdrücklich beauftragt wird.
- Die Zwischenstände ersetzen weder die regulären IPK-/Quellcode-Paare im Launcher-Verzeichnis noch einen Release-Changelog. Der [Projektstand](../PROJECT_STATUS.md) hält fest, was getestet wurde und was noch offen ist.

## Gesicherte Zwischenstände


Die Angaben beschreiben lokale Tests, keine veröffentlichten Versionen. Bei allen drei Versionen wurden automatisierte lokale Prüfungen durchgeführt; sie ersetzen keinen Fernsehtest.
















- **0.2.81 (1. November 2026):** Behebt den anhand des Boot-Protokolls festgestellten leeren Python-Pfad bei Direct Home; fester Interpreterpfad und Boot-PATH, Regressionstest für leere Umgebung bestanden. Der Nutzer meldete einen erfolgreichen Start nach längerem Standby mit diesem Teststand. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.81.zip).

- **0.2.82 (2. November 2026):** Direct-Home-Boot-Wartezeit von zehn auf fünf Sekunden verkürzt. Der Nutzer bestätigte den Start nach längerer Standby-Zeit mit dem vorherigen Teststand; die neue Wartezeit wurde lokal geprüft, ein Fernsehtest steht aus. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.82.zip).

- **0.2.91:** Eingebettete Bildobjekte und vielseitige Bewegung für importierte Themes; China-Theme mit Blütenblättern. Lokal geprüft, nicht am Fernseher getestet. [Quellcode-ZIP](g5-launcher-zwischenstand_0.2.91.zip).

## Verbindlicher Ablauf je Testversion

Vor der Übergabe einer Test-IPK: Versionsnummern abgleichen, den dazugehörigen Quellcode als ZIP erstellen und prüfen, hier auf GitHub sichern, den Projektstand samt Änderungen und tatsächlichem Teststatus aktualisieren und die veröffentlichten Dateien überprüfen. Nur die drei neuesten Zwischenstands-ZIPs behalten. Die Test-IPK selbst bleibt lokal. Wenn die GitHub-Sicherung scheitert, den Fehler ausdrücklich melden und nicht behaupten, das Backup sei abgeschlossen.
