# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Lokaler Teststand 0.2.91:** Importierte Themes können eigene eingebettete Bildobjekte und einen begrenzten Bewegungsablauf mit Drehung, Verzögerung und Ausblenden verwenden. Test-IPK bleibt lokal. [Quellcode-Zwischenstand](zwischenstaende/g5-launcher-zwischenstand_0.2.91.zip).

- **Veröffentlichung 0.2.90:** Boot-Pfad-Korrektur und fünf Sekunden Direct-Home-Boot-Wartezeit.

- **Lokaler Teststand 0.2.82:** Nur die Direct-Home-Boot-Wartezeit von zehn auf fünf Sekunden verkürzt; Testversion und Paketnummer entsprechend erhöht. [Gesicherter Quellstand](zwischenstaende/g5-launcher-zwischenstand_0.2.82.zip).

- **Lokaler Teststand 0.2.81:** Nach erneutem Boot-Recovery dokumentierte das TV-Protokoll `sys.executable` leer und `PATH` nicht gesetzt; der Bridge-Prozess konnte deshalb nicht starten. Fester Python-Pfad als Rückfall und gesetzter Boot-PATH; [Gesicherter Quellstand](zwischenstaende/g5-launcher-zwischenstand_0.2.81.zip).

- **Veröffentlichung 0.2.80:** Aus Teststand 0.2.72 neu gebaut.
- **Direct Home:** Nach Browserstart wurde zuvor automatisch LG Home wiederhergestellt. Der Laufzeitmonitor setzt bei fehlendem Lebenszeichen nicht mehr automatisch zurück; manuelle Wiederherstellung bleibt verfügbar. Bei tatsächlich eingefrorener Oberfläche erfolgt ebenfalls keine automatische Rücksetzung. Der Grund der früheren fehlenden Rückmeldung ist nicht bestätigt.
- **Updateprüfung:** Der alte Versionsvergleich (0.2.60 in 0.2.70) wurde unabhängig vom Direct-Home-Vorfall korrigiert.
- **Themes:** Cyberpunk ist integriert; importierte Themes unterstützen voreingestellte Effekte mit Optionen sowie Szenen aus Formen und Einzelanimationen. Höchstens drei importierte Themes sind gleichzeitig gespeichert. [Vorlage und Anleitung](themes/README.de.md).
- Version: **0.2.90**; App-ID: `org.schrotty74.g5launcher`. Die aktuell veröffentlichten IPK- und Quellcode-Dateien liegen im App-Verzeichnis.

## Offene Punkte

- **Für später: einfacher Theme-Editor.** Browserbasierter Baukasten, in gängigen Browsern auf Smartphone, Tablet und Desktop gut bedienbar; für Touch, Maus und Tastatur geeignet: Hintergrund und Farben wählen, Objekte oder eigene Bilder hinzufügen, per Touch oder Maus positionieren und ihre Größe ändern; Animationen wie Fallen, Schweben, Blinken und Drehen über verständliche Auswahl und einfache Einstellungen erstellen. Änderungen und Animationen sofort in einer Vorschau zeigen. Bestehende Themes öffnen und bearbeiten, fertige Themes als kompatible JSON-Datei exportieren. Formatgrenzen prüfen und verständlich anzeigen; JSON und Bildkodierung im Hintergrund erledigen. Keine Umsetzung beauftragt.

- Für später vormerken: eigene, frei programmierbare Animationsskripte für importierte Themes prüfen. Noch nicht umgesetzt; Sicherheitsmodell, Prüfung und Bedienung vor einer Umsetzung festlegen.

## Übergabe für den nächsten Chat

- Vor einem Glasshouse-Server-Update Direct Home auf LG Home umstellen. Bei einer gegenseitigen Blockade durch Glasshouses `restorePending` und die G5-Home-Übernahme die Voraussetzungen und den dokumentierten Wiederherstellungsweg beachten: [Glasshouse und LG Home](GLASSHOUSE_WIEDERHERSTELLUNG.md). Die Ursache des damaligen Updatefehlers ist nicht abschließend geklärt.

- Das eigenständige Wintertheme liegt im Theme-Ordner. Die Theme-Übersichten enthalten den Download.
- Regulärer Launcher-Stand unter `app/`: 0.2.90. Die ZIP-Dateien im Zwischenstandsordner bleiben separate lokale Teststände.
- Die bisherige Home-Methode bleibt als Rückfalllösung erhalten.
- Nach wichtigen Arbeitsschritten diesen Abschnitt knapp aktualisieren: Was geändert wurde, welche lokale Testversion vorliegt, und ob der Quellcode bereits auf GitHub liegt. Veraltete Zwischenstände ersetzen; keine persönlichen Daten eintragen.
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

- Unter TV-Homescreen stehen LG Home, die bisherige Methode und die direkte Home-Übernahme zur Auswahl. Direct Home benötigt keinen Magic Mapper; vor Updates oder der Deinstallation LG Home wiederherstellen.

- Das Installieren allein ändert die Home-Taste nicht. Die bisherige optionale Belegung wird in den Einstellungen des Launchers gesetzt und benötigt [Magic Mapper 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2), installiert, aktiv und bereits für den Start eingerichtet. Die Home-Taste muss nicht zuerst manuell in Magic Mapper zugewiesen werden.
- Die bisherige Home-Zuordnung wird gesichert und kann im Launcher wiederhergestellt werden. Andere Tastenbelegungen bleiben erhalten. Vor der Deinstallation die frühere Zuordnung wiederherstellen; andere Home-Mapper können in Konflikt stehen.
- Einstellungen liegen im lokalen Speicher unter `g5home.prefs`. Das JSON-Backup wird über den Homebrew-Dienst nach `/media/developer/g5-tv-launcher/backup.json` geschrieben und von dort wiederhergestellt. Erneutes Speichern ersetzt das vorige Backup; die Datei kann per SFTP kopiert werden.
- Die Updateprüfung ist manuell, liest öffentliche Versionsdaten von GitHub und installiert keine Updates selbst.

## Wichtige Regeln für künftige Änderungen

- Keine Testergebnisse oder Testaufforderungen für Launcher oder Themes öffentlich dokumentieren, außer der Nutzer verlangt dies ausdrücklich. Testergebnisse werden im Chat besprochen; nicht geprüfte Funktionen nicht als geprüft darstellen.

- Lokale Testversionen fortlaufend in der letzten Versionsstelle um eins erhöhen (nach 0.2.60 beispielsweise 0.2.61, 0.2.62). App-Metadaten, Build, Updateprüfung und Paketname auf dieselbe Testversion abstimmen. Lokale Test-IPKs nicht ohne ausdrücklichen Auftrag auf GitHub hochladen. Für jede Testversion das zugehörige Quellcode-ZIP separat im Zwischenstandsordner sichern. Dort nur die drei neuesten Quellcode-Zwischenstände behalten; ältere Zwischenstands-ZIPs nach erfolgreicher Sicherung entfernen.
- Für einen ausdrücklich beauftragten GitHub-Upload eine gemeinsame Versionsnummer für den hochzuladenden Stand festlegen (beispielsweise 0.2.70); keine automatische Aufrundungsregel annehmen. Der Changelog fasst nur die Änderungen des hochgeladenen Stands gegenüber der letzten auf GitHub dokumentierten Version zusammen, ohne einzelne lokale Zwischenversionen oder später verworfene Änderungen. Bei einem Release die Versionsangaben und Dokumentation aufeinander abstimmen. Ein unveröffentlichter Teststand kann gesammelt unter „Unreleased“ dokumentiert werden. Wenn der Nutzer eine kleine veröffentlichte Version ausdrücklich ersetzen und zusammenfassen möchte, wird der Eintrag in die Ersatzversion übernommen.

- Pro App im aktuellen Repository-Stand höchstens die **drei neuesten IPK-Pakete und die drei neuesten Quellcode-ZIPs** behalten. Ältere Pakete und ZIPs bei einer Veröffentlichung entfernen und auf veraltete Download-Links prüfen. Dateien bleiben ohne gesonderte Bereinigung in der Git-Historie erhalten.
- Die deutschen und englischen Launcher-Anleitungen und bei Bedarf beide Startseiten aktualisieren. Screenshots der tatsächlichen Oberfläche als Fotos kennzeichnen; die Vorschau des System Monitors verwendet dagegen Demodaten.
- Keine persönlichen Zugangsdaten, persönlichen IP-Adressen oder festen lokalen Computerpfade veröffentlichen. Die plattformbedingten webOS-Pfade im Code sind davon zu unterscheiden.
- Bestehende Einstellungen, Favoriten und Backups beim Weiterentwickeln berücksichtigen. 
- Vor einem Upload Paketinhalt mit dem Quellcode vergleichen und den Befehl zum Bauen mit Python 3 ohne rechnergebundene Pfade erhalten. Der Nutzer installiert und testet die IPK auf dem Fernseher.
