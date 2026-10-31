# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Veröffentlichung 0.2.80:** Aus Teststand 0.2.72 neu gebaut; die Release-IPK selbst wurde noch nicht am Fernseher getestet. Nutzer bestätigte Cyberpunk-Darstellung und Animationen sowie Import und grundsätzliche Darstellung der Strand-Szene. Nicht jede Effektoption wurde am Fernseher geprüft.
- **Direct Home:** Nach Browserstart wurde zuvor automatisch LG Home wiederhergestellt. Der Laufzeitmonitor setzt bei fehlendem Lebenszeichen nicht mehr automatisch zurück; manuelle Wiederherstellung bleibt verfügbar. Bei tatsächlich eingefrorener Oberfläche erfolgt ebenfalls keine automatische Rücksetzung. Der Grund der früheren fehlenden Rückmeldung ist nicht bestätigt.
- **Updateprüfung:** Der alte Versionsvergleich (0.2.60 in 0.2.70) wurde unabhängig vom Direct-Home-Vorfall korrigiert.
- **Themes:** Cyberpunk ist integriert; importierte Themes unterstützen voreingestellte Effekte mit Optionen sowie Szenen aus Formen und Einzelanimationen. Höchstens drei importierte Themes sind gleichzeitig gespeichert. [Vorlage und Anleitung](themes/README.de.md).
- Version: **0.2.80**; App-ID: `org.schrotty74.g5launcher`. Die aktuell veröffentlichten IPK- und Quellcode-Dateien liegen im App-Verzeichnis.

## Offene Punkte

- Für später vormerken: eigene, frei programmierbare Animationsskripte für importierte Themes prüfen. Noch nicht umgesetzt; Sicherheitsmodell, Prüfung und Bedienung vor einer Umsetzung festlegen.

- Apps in den Favoriten gezielt ausblenden: Der ursprüngliche Wunsch ist von der umgesetzten App-Verwaltung in der Übersicht getrennt zu betrachten; eine gesonderte Umsetzung ist nicht bestätigt.
- Wetter-Nachabruf nach längerem Standby und experimentelle Notfallgeste auf dem Fernseher prüfen. Die Geste benötigt Home-Relaunch-Ereignisse und ist keine unabhängig geprüfte Rückfallebene bei eingefrorener Oberfläche.
- Das separate Wintertheme auf dem Fernseher importieren und seine Darstellung prüfen. Bis zu drei importierte Themes können gleichzeitig gespeichert werden.
- Ein vollständiges austauschbares Theme-Layout ist nicht umgesetzt; das JSON-Format unterstützt Farben, Hintergrundbilder, vorgegebene Effekte und einfache Szenen.

## Übergabe für den nächsten Chat

- Das eigenständige Wintertheme liegt auf GitHub im Theme-Ordner; Format und Bild wurden lokal geprüft, der Fernsehtest steht aus. Die Theme-Übersichten enthalten den Download.
- Launcher-Änderungen und bestätigte Gerätetests stehen im Abschnitt „Aktueller Stand“; Wetter-Nachabruf und Notfallgeste bleiben zu prüfen.
- Regulärer Launcher-Stand unter `app/`: 0.2.80. Die ZIP-Dateien im Zwischenstandsordner bleiben separate lokale Teststände.
- Der Nutzer testete Teile des vorherigen Teststands; die neu gebaute Veröffentlichung 0.2.80 selbst ist noch nicht auf dem Fernseher getestet.
- Direct Home startete im Teststand 0.2.63 nach einer Nacht im Standby. Das neu gebaute Paket 0.2.80 ist noch nicht auf dem Fernseher getestet. Die bisherige Methode bleibt als Rückfalllösung erhalten.
- Nach wichtigen Arbeitsschritten diesen Abschnitt knapp aktualisieren: Was geändert wurde, welche lokale Testversion vorliegt, was tatsächlich getestet wurde, was offen ist und ob der Quellcode bereits auf GitHub liegt. Veraltete Zwischenstände ersetzen; keine persönlichen Daten eintragen.
- Ein Markdown-Zwischenstand beschreibt die Arbeit, ersetzt aber keine Sicherung des Quellcodes. Nach jeder lokalen Testversion ein separates versioniertes Quellcode-ZIP erstellen und im [Zwischenstandsordner](zwischenstaende/) sichern. Die zugehörige IPK bleibt lokal, bis ihr Upload ausdrücklich beauftragt wird.

## Oberfläche und Bedienung

- Drei Seiten: Übersicht, Favoriten und Eingänge. Die Startseite ist auswählbar und gilt auch beim erneuten Öffnen.
- Übersicht mit App-Sammlung, App-Suche und drei anpassbaren Schnellzugriffen für Apps, HDMI-Eingänge oder TV-Einstellungen. HDMI-Eingänge und Live TV gehören zur Eingangsseite und erscheinen nicht als normale Apps in der Sammlung.
- Favoriten hinzufügen, entfernen und sortieren; echte App-Symbole soweit verfügbar, sonst ein Ersatzsymbol. Namen können unter den Symbolen angezeigt oder ausgeblendet werden; ohne Namen gibt es drei Symbolgrößen.
- Glas-Dock mit einstellbarem Abstand, Transparenz und Position. Bei aktivierten dezenten Animationen vergrößert sich der fokussierte Favorit unter dem Zeiger oder bei Steuerkreuzbedienung. Animationen lassen sich abschalten.
- Magic Remote: Steuerkreuz und Zeiger; horizontaler Bildlauf in den App- und Favoritenleisten auch mit dem Mausrad. Fokusrahmen benötigen innerhalb scrollbarer Bereiche ausreichend Platz.
- Vier HDMI-Eingänge und Live TV liegen in einer Reihe. Namen der HDMI-Eingänge können aus den webOS-Startpunkten übernommen oder im Launcher selbst gesetzt werden.
- Acht illustrierte Szenen im Banner aller drei Seiten; feste Szene, Wechsel beim Öffnen oder Auswahl nach Tageszeit. Uhr und Wetter sind separat abschaltbar; das Wetter nutzt Open-Meteo oder das GeoSphere-Modell über Open-Meteo und einen gewählten Ort.
- Halloween, Weihnachten und Cyberpunk stehen in der Hintergrundauswahl unter Spezial-Themes. Bei eingeschalteten Animationen bewegt sich eine Spinne, Hausfenster und Kürbisgesicht flackern, und im Weihnachtstheme fällt Schnee. Der Rentierschlitten fliegt abwechselnd in beide Richtungen, zwölf Sekunden lang mit fünf Sekunden Pause. Animationen lassen sich abschalten.
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
