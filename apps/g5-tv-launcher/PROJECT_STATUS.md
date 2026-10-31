# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Testversion 0.2.72:** Importierbare Themes unterstützen optional Szenen mit bis zu 100 Rechtecken, Ellipsen oder Polygonen und einzelnen Bewegungs-, Blink- und Schwenkeffekten. Enthält bildfreies Strand-Beispiel, Vorlage und Anleitung. Bestehende Themes und globale Effekte bleiben unterstützt. JS-/Python-Validierung, simulierte DOM-Erzeugung, 31 Bestandstests und Paket-/ZIP-Prüfung bestanden; keine visuelle Browser- oder Fernseherprüfung. [Quellcode-ZIP](zwischenstaende/g5-launcher-zwischenstand_0.2.72.zip); IPK bleibt lokal.

- **Testversion 0.2.71:** Aktueller Teststand mit Cyberpunk-Stadt und konfigurierbaren Animationseffekten. Paketname, App-Metadaten und Updateprüfung sind auf 0.2.71 abgestimmt. Der vorherige Assistent hatte mehrere unterschiedliche Tests fälschlich intern 0.2.70 genannt; diese wurden nicht rückwirkend umnummeriert. 31 automatisierte Tests und Paket-/ZIP-Prüfung bestanden; Fernsehtest von 0.2.71 steht aus. [Quellcode-ZIP](zwischenstaende/g5-launcher-zwischenstand_0.2.71.zip); Test-IPK bleibt lokal.

- **Konfigurierbare Theme-Effekte, Teststand (intern 0.2.70):** Importierte Themes können die vorhandenen Animationen optional über Farbe, Dauer, Deckkraft und Richtung konfigurieren. Bisherige Themes bleiben verwendbar. Validierungsprüfungen und 31 bestehende Tests sowie IPK-/ZIP-Prüfung bestanden; Bedienungs- und Fernsehtest stehen aus. Vorlage und Anleitung liegen im Test-Quellcode. [Test-Quellcode](zwischenstaende/g5-launcher-zwischenstand_0.2.70-effect-options.zip); Test-IPK bleibt lokal.

- **Cyberpunk-Stadt-Test (intern 0.2.70):** Ergänzt Fenster an bisher fensterlosen Gebäuden und animiert die Bodenlinien im integrierten Cyberpunk-Theme. Animationen sind über die vorhandene Einstellung steuerbar. 31 automatisierte Tests sowie SVG-, IPK- und ZIP-Prüfung bestanden; Fernsehtest steht aus. [Test-Quellcode](zwischenstaende/g5-launcher-zwischenstand_0.2.70-cyber-city-test.zip); Test-IPK bleibt lokal.

- **Cyberpunk-Fenster-Test (intern 0.2.70):** Das eingebaute Cyberpunk-Theme hat kräftigere Neonfarben, ein verstärktes Neonlicht und zwei wechselnd leuchtende Fenstergruppen; die Animationseinstellung steuert beide Effekte. 31 automatisierte Tests sowie IPK- und ZIP-Prüfung bestanden; Fernsehtest steht aus. [Test-Quellcode](zwischenstaende/g5-launcher-zwischenstand_0.2.70-cyberwindows-test.zip); Test-IPK bleibt lokal.

- **Cyberpunk-Leuchteffekt-Test (intern 0.2.70):** Nutzer meldete, dass das importierte Cyberpunk-Theme animiert ist, das integrierte jedoch nicht sichtbar. Dessen schwacher Lichteffekt wurde verstärkt. 31 automatisierte Tests und Paketprüfung bestanden; Fernsehtest steht aus. [Quellcode-ZIP](zwischenstaende/g5-launcher-zwischenstand_0.2.70-cyberglow-test.zip); Test-IPK bleibt lokal.

- **Animierte Import-Themes, Teststand (intern 0.2.70):** Optionale vorgegebene Effekte `neon`, `rain`, `snow`, `particles` und `none`; die allgemeine Animationseinstellung steuert die Darstellung. Statische Themes ohne Feld bleiben gültig. Lokale Tests der Theme-Validierung und bestehende Tests sowie IPK-/ZIP-Prüfung bestanden. Vorlage, zweisprachige Anleitung und importierbares Cyberpunk-Beispiel im Test-Quellcode; UI- und Fernsehtest ausständig. [Quellcode-ZIP](zwischenstaende/g5-launcher-zwischenstand_0.2.70-animated-themes.zip). IPK nicht veröffentlicht.

- **Cyberpunk-Test (interne Version 0.2.70):** Neues Cyberpunk-Spezial-Theme mit Neon-Animation, gesteuert über die vorhandene Animationseinstellung; enthält den vorherigen Watch-Fix. 31 automatisierte Tests, JavaScript-Syntax, IPK-Inhalt und ZIP lokal geprüft. Fernsehtest steht aus. [Test-Quellcode](zwischenstaende/g5-launcher-zwischenstand_0.2.70-cyberpunk-test.zip); Test-IPK nicht veröffentlicht.

- **Lokaler Watch-Fix-Test (interne Version 0.2.70):** Nach dem Öffnen des Browsers meldete die Überwachung „Home page stopped answering; LG Home restored“. Der Teststand stellt LG Home nicht mehr allein wegen fehlender Lebenszeichen automatisch wieder her; die manuelle Rückkehr bleibt verfügbar. Die automatische Wiederherstellung bei tatsächlich eingefrorener Oberfläche entfällt damit ebenfalls. Die Updateprüfung vergleicht nun mit 0.2.70 statt 0.2.60. 30 bestehende automatisierte Tests sowie ein gezielter Überwachungstest bestanden; Paketinhalt und ZIP geprüft. Fernsehtest steht aus. [Gesicherter Quellcode](zwischenstaende/g5-launcher-zwischenstand_0.2.70-watch-fix.zip); Test-IPK bleibt außerhalb von GitHub.

- **Wintertheme:** Das eigenständige [Wintertheme](themes/winter.json) ergänzt Frühling, Sommer und Herbst im öffentlichen Theme-Ordner. JSON-Format, Bild und Größenbegrenzungen wurden lokal geprüft; ein Import auf dem Fernseher wurde noch nicht getestet. Höchstens drei eigene Themes können gleichzeitig gespeichert werden.

- **Launcher-Funktionen seit der vorigen veröffentlichten Version:** Direct Home startet ohne Magic-Mapper-Prüfung und schreibt bei Startfehlern genauere Diagnoseinformationen. Wetter wird zusätzlich fünf Sekunden nach Start, erneutem Öffnen oder Sichtbarwerden abgefragt. Die Uhr kann digital oder analog angezeigt werden. Apps auf der Übersicht lassen sich ausblenden, wieder einblenden und sortieren; die Favoritensortierung bleibt erhalten. Eigene JSON-Themes lassen sich über `/tmp` oder das Eingabefeld importieren, auswählen und entfernen; die Auswahl ist in Standard, Spezial und Importiert gegliedert. Eine experimentelle Home-Notfallgeste ist vorhanden.
- **Nutzertests der vorherigen Teststände:** Umschalten der Uhr, App-Verwaltung auf der Übersicht, Theme-Import, Kategorien, Dateifilter, Theme-Entfernung und Leeren des Eingabefelds wurden laut Nutzer erfolgreich am Fernseher ausprobiert. Diese Rückmeldungen belegen keinen Test des später neu gebauten Pakets 0.2.70.

- **Veröffentlichung 0.2.70:** Aus dem lokalen Teststand 0.2.69 neu gebaut. Die IPK 0.2.70 selbst wurde noch nicht auf dem Fernseher getestet; Nutzer bestätigte die Theme-Kategorien, Dateifilter, Import, Entfernung und Leeren des Eingabefelds im vorherigen Test. Der Wetter-Nachabruf und die experimentelle Notfallgeste benötigen noch einen Gerätetest.

- **Lokaler Teststand 0.2.69:** Theme-Eingabefeld wird nach erfolgreicher Installation geleert; fehlerhafte Eingaben bleiben erhalten. Nutzer bestätigte die Theme-Kategorien, Dateifilterung und das Entfernen; ebenso bestätigte er nach der Änderung das Leeren des Eingabefelds. Lokale und simulierte Prüfungen wurden durchgeführt.

- **Lokaler Teststand 0.2.68:** Getrennte Auswahl für Standard-, Spezial- und importierte Themes; Dateisuche zeigt nur gültige Theme-JSON-Dateien. Der Nutzer bestätigte Theme-Import, Kategorien, Dateifilterung und Entfernung am Fernseher; lokale Prüfungen wurden durchgeführt.

- **Lokaler Teststand 0.2.67:** Theme-JSON aus /tmp am Fernseher auswählen und importieren; Nutzer meldet Uhrwechsel und App-Auswahl von 0.2.66 als funktionierend. Funktion aus 0.2.67 lokal mit simulierten Diensten und Direct-Home-Bridge geprüft, Fernsehtest steht aus. Die unabhängige Notfallrückkehr und das vollständige austauschbare Theme-Layout sind weiterhin nicht nachgewiesen.

- **Lokaler Teststand 0.2.66:** Wetter-Nachabruf, analoge Uhr, Apps in Übersicht verwalten, experimenteller Theme-JSON-Import samt Vorlage und experimentelle Notfallgeste. Lokale Tests und simulierte DOM-Tests durchgeführt; kein Test auf dem Fernseher. Notfallgeste hängt von Home-Relaunch-Ereignissen ab und bietet keine unabhängig geprüfte Wiederherstellung, wenn die Oberfläche nicht reagiert. Der Nutzer meldete 0.2.63 als installiert.

- **Lokaler Zwischenstand 0.2.65:** Zusätzlich zu 0.2.64 analoge Uhr als wählbare Alternative eingebaut. In Entwicklung; UI- und TV-Test stehen aus. Weitere beauftragte Funktionen sind noch offen. Auf dem TV läuft laut Nutzer weiterhin 0.2.63.

- **Lokaler Zwischenstand 0.2.64:** Zusätzlicher Wetterabruf fünf Sekunden nach Start, Wiederöffnen oder Sichtbarwerden; das eingestellte Intervall bleibt erhalten. Lokale Prüfungen bestanden; Browser- und Fernsehtest stehen aus. Laut Nutzer ist 0.2.63 installiert.

- **Standby-Test am 31. Oktober 2026:** Laut Nutzer erschien der installierte G5 TV Launcher 0.2.63 nach dem Ausschalten über Nacht sofort. Zunächst meldete die Wetteranzeige „Wetter nicht verfügbar“; nach erneutem Speichern des unveränderten Wetterstandorts funktionierte sie sofort. Ursache offen. Der Code startet die Wetterabfrage sofort; eine noch nicht bereite Netzwerkverbindung ist eine mögliche Erklärung, kein gesicherter Befund. Die geplante Wartezeit im Boot-Skript beschreibt nicht notwendigerweise das sichtbare Aufwachen aus Standby.

- **Lokaler Teststand 0.2.63 (30. Oktober 2026):** Vom Nutzer installiert. Direct Home prüft Magic Mapper beim Start nicht mehr; ein erweitertes Startprotokoll dokumentiert Ablaufschritt und Fehler-Traceback. Nach kurzem Aus- und Einschalten erschien LG Home; die Ursache ist offen. Der anschließende längere Standby-Test am 31. Oktober verlief laut Nutzer beim Start des Launchers erfolgreich; siehe aktuellen Eintrag oben. Glasshouse Home und dessen experimentelle Home-Anpassung waren laut Anzeige ausgeschaltet. Der Fernseher soll für den Test Home beim Einschalten öffnen. Die Test-IPK blieb lokal; ältere Zwischenstände werden gemäß Drei-Dateien-Regel entfernt.
- Der frühere Startfehler lautete `Boot recovery: [Errno 13] Permission denied: ''`; dessen genaue Ursache ist offen. Die vorherige Vermutung zu einem leeren Python-Pfad ist nicht belegt.

- **Testversion 0.2.60 nach 0.2.50:** Direct Home Takeover, Wettersymbol-Sets Meteocons und Makin’ Things sowie GeoSphere Austria über Open-Meteo. Das getrennte [Testpaket](g5-tv-launcher_0.2.60_all.ipk) enthält diesen Stand; die veröffentlichte IPK 0.2.50 bleibt unverändert.
- Direct Home und der Wechsel der Wettersymbol-Sets wurden auf dem Fernseher ausprobiert. Ein späterer Teststand startete nach einer Nacht im Standby. Die bisherige Home-Methode bleibt als Rückfalllösung erhalten. Die Ursache eines früheren Absturzes ist ungeklärt; derzeit tritt er laut Nutzer nicht mehr auf.
- Wettersymbol-Animationen und der aktualisierte Wetterdienst wurden nicht umfassend auf dem Fernseher geprüft.

- Der optionale Autostart der bisherigen Methode wurde auf dem Fernseher getestet, einschließlich Start aus tiefem Standby. Dieser Test bezieht sich nicht auf Direct Home; dessen Langzeittest steht noch aus. Vor der Deinstallation Autostart ausschalten.
- IPK-Bauvorgaben für beide Apps und künftige Apps: [IPK_PACKAGING.md](../../IPK_PACKAGING.md).

- Version: **0.2.70**; App-ID: `org.schrotty74.g5launcher`.
- Eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Der Nutzer meldete, dass die Ortsanzeige beim Wechsel auf Englisch richtig war. Gerätetests einzelner Funktionen gelten für den verwendeten Fernseher.
- Der vollständige Quellcode liegt unter [app/](app/); die IPK und das Quellcode-ZIP liegen im App-Verzeichnis. Die Anwendung ist eine Web-App mit HTML, CSS, JavaScript und lokalen SVG-Szenen.

## Offene Punkte

- Für später vormerken: eigene, frei programmierbare Animationsskripte für importierte Themes prüfen. Noch nicht umgesetzt; Sicherheitsmodell, Prüfung und Bedienung vor einer Umsetzung festlegen.

- Apps in den Favoriten gezielt ausblenden: Der ursprüngliche Wunsch ist von der umgesetzten App-Verwaltung in der Übersicht getrennt zu betrachten; eine gesonderte Umsetzung ist nicht bestätigt.
- Wetter-Nachabruf nach längerem Standby und experimentelle Notfallgeste auf dem Fernseher prüfen. Die Geste benötigt Home-Relaunch-Ereignisse und ist keine unabhängig geprüfte Rückfallebene bei eingefrorener Oberfläche.
- Das separate Wintertheme auf dem Fernseher importieren und seine Darstellung prüfen. Bis zu drei importierte Themes können gleichzeitig gespeichert werden.
- Ein vollständiges austauschbares Theme-Layout ist nicht umgesetzt; das vorhandene JSON-Format ändert Farben und Hintergrundbild.

## Übergabe für den nächsten Chat

- Das eigenständige Wintertheme liegt auf GitHub im Theme-Ordner; Format und Bild wurden lokal geprüft, der Fernsehtest steht aus. Die Theme-Übersichten enthalten den Download.
- Launcher-Änderungen und bestätigte Gerätetests stehen im Abschnitt „Aktueller Stand“; Wetter-Nachabruf und Notfallgeste bleiben zu prüfen.
- Regulärer Launcher-Stand unter `app/`: 0.2.70. Die ZIP-Dateien im Zwischenstandsordner bleiben separate lokale Teststände.
- Der Nutzer testete die Funktionen des vorherigen lokalen Stands; die neu gebaute Veröffentlichung 0.2.70 selbst ist noch nicht auf dem Fernseher getestet.
- Direct Home startete im Teststand 0.2.63 nach einer Nacht im Standby. Das neu gebaute Paket 0.2.70 ist noch nicht auf dem Fernseher getestet. Die bisherige Methode bleibt als Rückfalllösung erhalten.
- Nach wichtigen Arbeitsschritten diesen Abschnitt knapp aktualisieren: Was geändert wurde, welche lokale Testversion vorliegt, was tatsächlich getestet wurde, was offen ist und ob der Quellcode bereits auf GitHub liegt. Veraltete Zwischenstände ersetzen; keine persönlichen Daten eintragen.
- Ein Markdown-Zwischenstand beschreibt die Arbeit, ersetzt aber keine Sicherung des Quellcodes. Nach jeder lokalen Testversion ein separates versioniertes Quellcode-ZIP erstellen und im [Zwischenstandsordner](zwischenstaende/) sichern. Die zugehörige IPK bleibt lokal, bis ihr Upload ausdrücklich beauftragt wird.

## Oberfläche und Bedienung

- Drei Seiten: Übersicht, Favoriten und Eingänge. Die Startseite ist auswählbar und gilt auch beim erneuten Öffnen.
- Übersicht mit App-Sammlung, App-Suche und drei anpassbaren Schnellzugriffen für Apps, HDMI-Eingänge oder TV-Einstellungen. HDMI-Eingänge und Live TV gehören zur Eingangsseite und erscheinen nicht als normale Apps in der Sammlung.
- Favoriten hinzufügen, entfernen und sortieren; echte App-Symbole soweit verfügbar, sonst ein Ersatzsymbol. Namen können unter den Symbolen angezeigt oder ausgeblendet werden; ohne Namen gibt es drei Symbolgrößen.
- Glas-Dock mit einstellbarem Abstand, Transparenz und Position. Bei aktivierten dezenten Animationen vergrößert sich der fokussierte Favorit unter dem Zeiger oder bei Steuerkreuzbedienung. Animationen lassen sich abschalten.
- Magic Remote: Steuerkreuz und Zeiger; horizontaler Bildlauf in den App- und Favoritenleisten auch mit dem Mausrad. Fokusrahmen benötigen innerhalb scrollbarer Bereiche ausreichend Platz.
- Vier HDMI-Eingänge und Live TV liegen in einer Reihe. Namen der HDMI-Eingänge können aus den webOS-Startpunkten übernommen oder im Launcher selbst gesetzt werden.
- Sieben illustrierte Szenen im Banner aller drei Seiten; feste Szene, Wechsel beim Öffnen oder Auswahl nach Tageszeit. Uhr und Wetter sind separat abschaltbar; das Wetter nutzt Open-Meteo oder das GeoSphere-Modell über Open-Meteo und einen gewählten Ort.
- Halloween und Weihnachten stehen in der Hintergrundauswahl unter Spezial-Themes. Bei eingeschalteten Animationen bewegt sich eine Spinne, Hausfenster und Kürbisgesicht flackern, und im Weihnachtstheme fällt Schnee. Der Rentierschlitten fliegt abwechselnd in beide Richtungen, zwölf Sekunden lang mit fünf Sekunden Pause. Animationen lassen sich abschalten.
- Uhr- und Wettergröße sind unabhängig einstellbar. Das Wetterintervall ist wählbar; Sonnenauf- und -untergang bestimmen den Tag-Nacht-Wechsel. Wettersymbole von Meteocons und Makin’ Things sind auswählbar; ihre Animation lässt sich je Set unabhängig aktivieren.
- Die Wetterortsuche fragt Treffer auf Deutsch und Englisch ab und bevorzugt die TV-Zeitzone. Der Treffer lässt sich anhand von Ort, Region und Land auswählen; Auswahl und Einstellungen werden gespeichert. Wetterdaten werden über Open-Meteo abgerufen.
- Das Einstellungsmenü ist in Kategorien gegliedert.
- Englisch und Deutsch sind verfügbar; Englisch ist Standard. App-Namen vom Fernseher und eigene Eingangsbezeichnungen werden nicht übersetzt.

## Home-Taste, Einstellungen und Backup

- Unter TV-Homescreen stehen LG Home, die bisherige Methode und die direkte Home-Übernahme zur Auswahl. Direct Home benötigt keinen Magic Mapper; vor Updates oder der Deinstallation LG Home wiederherstellen. Ein früherer Teststand startete nach einer Nacht im Standby; für das veröffentlichte Paket steht dieser Test noch aus.

- Das Installieren allein ändert die Home-Taste nicht. Die bisherige optionale Belegung wird in den Einstellungen des Launchers gesetzt und benötigt [Magic Mapper 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2), installiert, aktiv und bereits für den Start eingerichtet. Die Home-Taste muss nicht zuerst manuell in Magic Mapper zugewiesen werden.
- Die bisherige Home-Zuordnung wird gesichert und kann im Launcher wiederhergestellt werden. Andere Tastenbelegungen bleiben erhalten. Vor der Deinstallation die frühere Zuordnung wiederherstellen; andere Home-Mapper können in Konflikt stehen.
- Einstellungen liegen im lokalen Speicher unter `g5home.prefs`. Das JSON-Backup wird über den Homebrew-Dienst nach `/media/developer/g5-tv-launcher/backup.json` geschrieben und von dort wiederhergestellt. Erneutes Speichern ersetzt das vorige Backup; die Datei kann per SFTP kopiert werden.
- Die Updateprüfung ist manuell, liest öffentliche Versionsdaten von GitHub und installiert keine Updates selbst.

## Wichtige Regeln für künftige Änderungen

- Lokale Testversionen fortlaufend in der letzten Versionsstelle um eins erhöhen (nach 0.2.60 beispielsweise 0.2.61, 0.2.62). App-Metadaten, Build, Updateprüfung und Paketname auf dieselbe Testversion abstimmen. Lokale Test-IPKs nicht ohne ausdrücklichen Auftrag auf GitHub hochladen. Für jede Testversion das zugehörige Quellcode-ZIP separat im Zwischenstandsordner sichern. Dort nur die drei neuesten Quellcode-Zwischenstände behalten; ältere Zwischenstands-ZIPs nach erfolgreicher Sicherung entfernen.
- Für einen ausdrücklich beauftragten GitHub-Upload eine gemeinsame Versionsnummer für den hochzuladenden Stand festlegen (beispielsweise 0.2.70); keine automatische Aufrundungsregel annehmen. Der Changelog fasst nur die Änderungen des hochgeladenen Stands gegenüber der letzten auf GitHub dokumentierten Version zusammen, ohne einzelne lokale Zwischenversionen oder später verworfene Änderungen. Bei einem Release die Versionsangaben und Dokumentation aufeinander abstimmen. Ein unveröffentlichter Teststand kann gesammelt unter „Unreleased“ dokumentiert werden. Wenn der Nutzer eine kleine veröffentlichte Version ausdrücklich ersetzen und zusammenfassen möchte, wird der Eintrag in die Ersatzversion übernommen.

- Pro App im aktuellen Repository-Stand höchstens die **drei neuesten IPK-Pakete und die drei neuesten Quellcode-ZIPs** behalten. Ältere Pakete und ZIPs bei einer Veröffentlichung entfernen und auf veraltete Download-Links prüfen. Dateien bleiben ohne gesonderte Bereinigung in der Git-Historie erhalten.
- Die deutschen und englischen Launcher-Anleitungen und bei Bedarf beide Startseiten aktualisieren. Screenshots der tatsächlichen Oberfläche als Fotos kennzeichnen; die Vorschau des System Monitors verwendet dagegen Demodaten.
- Keine persönlichen Zugangsdaten, persönlichen IP-Adressen oder festen lokalen Computerpfade veröffentlichen. Die plattformbedingten webOS-Pfade im Code sind davon zu unterscheiden.
- Bestehende Einstellungen, Favoriten und Backups beim Weiterentwickeln berücksichtigen. Bildlauf, Fokusrahmen, Mauszeiger, Steuerkreuz, Home-Relaunch und beide Sprachen auf dem Fernseher überprüfen; lokale Syntax- oder Paketprüfungen ersetzen keinen Gerätetest.
- Vor einem Upload Paketinhalt mit dem Quellcode vergleichen und den Befehl zum Bauen mit Python 3 ohne rechnergebundene Pfade erhalten. Der Nutzer installiert und testet die IPK auf dem Fernseher.
