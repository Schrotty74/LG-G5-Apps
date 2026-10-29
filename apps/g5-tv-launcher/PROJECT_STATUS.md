# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Entwicklungsstand nach 0.2.50:** Direct Home Takeover, Wettersymbol-Sets Meteocons und Makin’ Things sowie GeoSphere Austria über Open-Meteo. Das getrennte [Testpaket](g5-launcher-direct-home-wetter-test.ipk) enthält diesen Stand; die veröffentlichte IPK 0.2.50 bleibt unverändert.
- Direct Home und der Wechsel der Wettersymbol-Sets wurden auf dem Fernseher ausprobiert. Start nach kurzem Ausschalten funktionierte; der Test nach mehreren Stunden Standby steht aus. Die bisherige Home-Methode bleibt als Rückfalllösung erhalten. Die Ursache eines früheren Absturzes ist ungeklärt; derzeit tritt er laut Nutzer nicht mehr auf.
- Wettersymbol-Animationen und der aktualisierte Wetterdienst wurden nicht umfassend auf dem Fernseher geprüft.

- Autostart ist optional: Der Nutzer hat das korrigierte Paket auf seinem Fernseher erfolgreich getestet, einschließlich Start aus tiefem Standby. Vor der Deinstallation Autostart ausschalten.
- IPK-Bauvorgaben für beide Apps und künftige Apps: [IPK_PACKAGING.md](../../IPK_PACKAGING.md).

- Version: **0.2.50**; App-ID: `org.schrotty74.g5launcher`.
- Eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Der Nutzer meldete, dass die Ortsanzeige beim Wechsel auf Englisch richtig war. Gerätetests einzelner Funktionen gelten für den verwendeten Fernseher.
- Der vollständige Quellcode liegt unter [app/](app/); die IPK und das Quellcode-ZIP liegen im App-Verzeichnis. Die Anwendung ist eine Web-App mit HTML, CSS, JavaScript und lokalen SVG-Szenen.

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

- Bei ausdrücklich beauftragten Releases die Versionsnummer erhöhen; `app/appinfo.json`, `build.py`, Versionsprüfung, Paketnamen und Dokumentation aufeinander abstimmen. Das englische [Changelog](CHANGELOG.md) nur für veröffentlichte Versionen führen und darunter sämtliche Änderungen seit der vorherigen veröffentlichten Version zusammenfassen; Zwischenbuilds erhalten keine eigenen Versionsüberschriften. Wenn der Nutzer eine kleine veröffentlichte Version ersetzen und zusammenfassen möchte, wird der Eintrag in die Ersatzversion übernommen.
- Pro App im aktuellen Repository-Stand höchstens die **drei neuesten IPK-Pakete und die drei neuesten Quellcode-ZIPs** behalten. Ältere Pakete und ZIPs bei einer Veröffentlichung entfernen und auf veraltete Download-Links prüfen. Dateien bleiben ohne gesonderte Bereinigung in der Git-Historie erhalten.
- Die deutschen und englischen Launcher-Anleitungen und bei Bedarf beide Startseiten aktualisieren. Screenshots der tatsächlichen Oberfläche als Fotos kennzeichnen; die Vorschau des System Monitors verwendet dagegen Demodaten.
- Keine persönlichen Zugangsdaten, persönlichen IP-Adressen oder festen lokalen Computerpfade veröffentlichen. Die plattformbedingten webOS-Pfade im Code sind davon zu unterscheiden.
- Bestehende Einstellungen, Favoriten und Backups beim Weiterentwickeln berücksichtigen. Bildlauf, Fokusrahmen, Mauszeiger, Steuerkreuz, Home-Relaunch und beide Sprachen auf dem Fernseher überprüfen; lokale Syntax- oder Paketprüfungen ersetzen keinen Gerätetest.
- Vor einem Upload Paketinhalt mit dem Quellcode vergleichen und den Befehl zum Bauen mit Python 3 ohne rechnergebundene Pfade erhalten. Der Nutzer installiert und testet die IPK auf dem Fernseher.
