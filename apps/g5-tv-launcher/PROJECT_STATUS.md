# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Testversion 0.2.60 nach 0.2.50:** Direct Home Takeover, Wettersymbol-Sets Meteocons und Makin’ Things sowie GeoSphere Austria über Open-Meteo. Das getrennte [Testpaket](g5-tv-launcher_0.2.60_all.ipk) enthält diesen Stand; die veröffentlichte IPK 0.2.50 bleibt unverändert.
- Direct Home und der Wechsel der Wettersymbol-Sets wurden auf dem Fernseher ausprobiert. Start nach kurzem Ausschalten funktionierte; der Test nach mehreren Stunden Standby steht aus. Die bisherige Home-Methode bleibt als Rückfalllösung erhalten. Die Ursache eines früheren Absturzes ist ungeklärt; derzeit tritt er laut Nutzer nicht mehr auf.
- Wettersymbol-Animationen und der aktualisierte Wetterdienst wurden nicht umfassend auf dem Fernseher geprüft.

- Der optionale Autostart der bisherigen Methode wurde auf dem Fernseher getestet, einschließlich Start aus tiefem Standby. Dieser Test bezieht sich nicht auf Direct Home; dessen Langzeittest steht noch aus. Vor der Deinstallation Autostart ausschalten.
- IPK-Bauvorgaben für beide Apps und künftige Apps: [IPK_PACKAGING.md](../../IPK_PACKAGING.md).

- Version: **0.2.60**; App-ID: `org.schrotty74.g5launcher`.
- Eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Der Nutzer meldete, dass die Ortsanzeige beim Wechsel auf Englisch richtig war. Gerätetests einzelner Funktionen gelten für den verwendeten Fernseher.
- Der vollständige Quellcode liegt unter [app/](app/); die IPK und das Quellcode-ZIP liegen im App-Verzeichnis. Die Anwendung ist eine Web-App mit HTML, CSS, JavaScript und lokalen SVG-Szenen.

## Übergabe für den nächsten Chat

- Letzter auf GitHub gesicherter Launcher-Stand: 0.2.60 mit zugehöriger IPK und Quellcode-ZIP. Die Dateien unter `app/` sind der maßgebliche Quellcode auf GitHub.
- Auf dem Fernseher läuft laut Nutzer noch der funktional gleiche Teststand mit interner Version 0.2.50. Die später erstellte 0.2.60 unterscheidet sich durch Versionsangaben und Updateprüfung; sie wurde nicht auf diesem Fernseher getestet.
- Direct Home startet nach kurzem Ausschalten; der Test nach mehreren Stunden Standby steht noch aus. Die bisherige Methode bleibt als Rückfalllösung erhalten.
- Nach wichtigen Arbeitsschritten diesen Abschnitt knapp aktualisieren: Was geändert wurde, welche lokale Testversion vorliegt, was tatsächlich getestet wurde, was offen ist und ob der Quellcode bereits auf GitHub liegt. Veraltete Zwischenstände ersetzen; keine persönlichen Daten eintragen.
- Ein Markdown-Zwischenstand beschreibt die Arbeit, sichert aber keinen nicht hochgeladenen Quellcode und keine IPK. Lokale Quellcode- und Paketstände bis zu einem ausdrücklichen Upload-Auftrag gesondert sichern.

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

- Unter TV-Homescreen stehen LG Home, die bisherige Methode und die direkte Home-Übernahme zur Auswahl. Direct Home benötigt keinen Magic Mapper; vor Updates oder der Deinstallation LG Home wiederherstellen. Der Langzeittest nach mehrstündigem Standby steht aus.

- Das Installieren allein ändert die Home-Taste nicht. Die bisherige optionale Belegung wird in den Einstellungen des Launchers gesetzt und benötigt [Magic Mapper 1.1.2](https://github.com/afonsojramos/magic-mapper-webos/releases/tag/v1.1.2), installiert, aktiv und bereits für den Start eingerichtet. Die Home-Taste muss nicht zuerst manuell in Magic Mapper zugewiesen werden.
- Die bisherige Home-Zuordnung wird gesichert und kann im Launcher wiederhergestellt werden. Andere Tastenbelegungen bleiben erhalten. Vor der Deinstallation die frühere Zuordnung wiederherstellen; andere Home-Mapper können in Konflikt stehen.
- Einstellungen liegen im lokalen Speicher unter `g5home.prefs`. Das JSON-Backup wird über den Homebrew-Dienst nach `/media/developer/g5-tv-launcher/backup.json` geschrieben und von dort wiederhergestellt. Erneutes Speichern ersetzt das vorige Backup; die Datei kann per SFTP kopiert werden.
- Die Updateprüfung ist manuell, liest öffentliche Versionsdaten von GitHub und installiert keine Updates selbst.

## Wichtige Regeln für künftige Änderungen

- Lokale Testversionen fortlaufend in der letzten Versionsstelle um eins erhöhen (nach 0.2.60 beispielsweise 0.2.61, 0.2.62). App-Metadaten, Build, Updateprüfung und Paketname auf dieselbe Testversion abstimmen. Lokale Teststände nicht ohne ausdrücklichen Auftrag auf GitHub hochladen.
- Für einen ausdrücklich beauftragten GitHub-Upload eine gemeinsame Versionsnummer für den hochzuladenden Stand festlegen (beispielsweise 0.2.70); keine automatische Aufrundungsregel annehmen. Der Changelog fasst nur die Änderungen des hochgeladenen Stands gegenüber der letzten auf GitHub dokumentierten Version zusammen, ohne einzelne lokale Zwischenversionen oder später verworfene Änderungen. Bei einem Release die Versionsangaben und Dokumentation aufeinander abstimmen. Ein unveröffentlichter Teststand kann gesammelt unter „Unreleased“ dokumentiert werden. Wenn der Nutzer eine kleine veröffentlichte Version ausdrücklich ersetzen und zusammenfassen möchte, wird der Eintrag in die Ersatzversion übernommen.

- Pro App im aktuellen Repository-Stand höchstens die **drei neuesten IPK-Pakete und die drei neuesten Quellcode-ZIPs** behalten. Ältere Pakete und ZIPs bei einer Veröffentlichung entfernen und auf veraltete Download-Links prüfen. Dateien bleiben ohne gesonderte Bereinigung in der Git-Historie erhalten.
- Die deutschen und englischen Launcher-Anleitungen und bei Bedarf beide Startseiten aktualisieren. Screenshots der tatsächlichen Oberfläche als Fotos kennzeichnen; die Vorschau des System Monitors verwendet dagegen Demodaten.
- Keine persönlichen Zugangsdaten, persönlichen IP-Adressen oder festen lokalen Computerpfade veröffentlichen. Die plattformbedingten webOS-Pfade im Code sind davon zu unterscheiden.
- Bestehende Einstellungen, Favoriten und Backups beim Weiterentwickeln berücksichtigen. Bildlauf, Fokusrahmen, Mauszeiger, Steuerkreuz, Home-Relaunch und beide Sprachen auf dem Fernseher überprüfen; lokale Syntax- oder Paketprüfungen ersetzen keinen Gerätetest.
- Vor einem Upload Paketinhalt mit dem Quellcode vergleichen und den Befehl zum Bauen mit Python 3 ohne rechnergebundene Pfade erhalten. Der Nutzer installiert und testet die IPK auf dem Fernseher.
