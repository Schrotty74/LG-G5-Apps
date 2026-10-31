# G5 TV Launcher – Projektstand

Diese Datei hält den Stand und wichtige Entscheidungen für spätere Weiterentwicklungen fest. Änderungen je Version stehen im [Changelog](CHANGELOG.md); technische Einzelheiten und der Bauprozess stehen in den [Entwicklungsnotizen](DEVELOPMENT.md).

## Aktueller Stand

- **Standby-Test am 31. Oktober 2026:** Laut Nutzer erschien der installierte G5 TV Launcher 0.2.63 nach dem Ausschalten über Nacht sofort. Zunächst meldete die Wetteranzeige „Wetter nicht verfügbar“; nach erneutem Speichern des unveränderten Wetterstandorts funktionierte sie sofort. Ursache offen. Der Code startet die Wetterabfrage sofort; eine noch nicht bereite Netzwerkverbindung ist eine mögliche Erklärung, kein gesicherter Befund. Die geplante Wartezeit im Boot-Skript beschreibt nicht notwendigerweise das sichtbare Aufwachen aus Standby.

- **Lokaler Teststand 0.2.63 (30. Oktober 2026):** Vom Nutzer installiert. Direct Home prüft Magic Mapper beim Start nicht mehr; ein erweitertes Startprotokoll dokumentiert Ablaufschritt und Fehler-Traceback. Nach kurzem Aus- und Einschalten erschien LG Home; die Ursache ist offen. Der anschließende längere Standby-Test am 31. Oktober verlief laut Nutzer beim Start des Launchers erfolgreich; siehe aktuellen Eintrag oben. Glasshouse Home und dessen experimentelle Home-Anpassung waren laut Anzeige ausgeschaltet. Der Fernseher soll für den Test Home beim Einschalten öffnen. Der [Quellcode-Zwischenstand](zwischenstaende/g5-launcher-zwischenstand_0.2.63.zip) ist separat gesichert; die Test-IPK bleibt lokal.
- Der frühere Startfehler lautete `Boot recovery: [Errno 13] Permission denied: ''`; dessen genaue Ursache ist offen. Die vorherige Vermutung zu einem leeren Python-Pfad ist nicht belegt.

- **Testversion 0.2.60 nach 0.2.50:** Direct Home Takeover, Wettersymbol-Sets Meteocons und Makin’ Things sowie GeoSphere Austria über Open-Meteo. Das getrennte [Testpaket](g5-tv-launcher_0.2.60_all.ipk) enthält diesen Stand; die veröffentlichte IPK 0.2.50 bleibt unverändert.
- Direct Home und der Wechsel der Wettersymbol-Sets wurden auf dem Fernseher ausprobiert. Start nach kurzem Ausschalten funktionierte; der Test nach mehreren Stunden Standby steht aus. Die bisherige Home-Methode bleibt als Rückfalllösung erhalten. Die Ursache eines früheren Absturzes ist ungeklärt; derzeit tritt er laut Nutzer nicht mehr auf.
- Wettersymbol-Animationen und der aktualisierte Wetterdienst wurden nicht umfassend auf dem Fernseher geprüft.

- Der optionale Autostart der bisherigen Methode wurde auf dem Fernseher getestet, einschließlich Start aus tiefem Standby. Dieser Test bezieht sich nicht auf Direct Home; dessen Langzeittest steht noch aus. Vor der Deinstallation Autostart ausschalten.
- IPK-Bauvorgaben für beide Apps und künftige Apps: [IPK_PACKAGING.md](../../IPK_PACKAGING.md).

- Version: **0.2.60**; App-ID: `org.schrotty74.g5launcher`.
- Eigenständiger Homebrew-Launcher für einen gerooteten LG G5 mit webOS 25. Der Nutzer meldete, dass die Ortsanzeige beim Wechsel auf Englisch richtig war. Gerätetests einzelner Funktionen gelten für den verwendeten Fernseher.
- Der vollständige Quellcode liegt unter [app/](app/); die IPK und das Quellcode-ZIP liegen im App-Verzeichnis. Die Anwendung ist eine Web-App mit HTML, CSS, JavaScript und lokalen SVG-Szenen.

## Wünsche für später

- Nach dem Ergebnis des Standby-Tests gemeinsam ansehen: Apps auf der Startseite ausblenden und sortieren sowie Apps bei den Favoriten ausblenden. Favoriten lassen sich laut Nutzer bereits einzeln nach oben und unten verschieben; diese vorhandene Sortierung berücksichtigen.
- Eine Notfallrückkehr zu LG Home per Fernbedienung prüfen. Geste und Umsetzung gemeinsam festlegen und auf dem TV testen.
- Ein Theme-System nach dem Vorbild von Clean Your TV prüfen: Nutzer sollen eigene Themes im Launcher installieren können; eine Theme-Vorlage und Anleitung sollen anderen das Erstellen eigener Themes ermöglichen. Umfang und Umsetzung nach dem Standby-Test gemeinsam besprechen.
- Uhranzeige: Eine analoge Uhr als wählbare Alternative zur vorhandenen digitalen Anzeige prüfen.
- Diese Wünsche sind vorgemerkt, nicht implementiert. Erst das Ergebnis des längeren Standby-Tests abwarten.

## Übergabe für den nächsten Chat

- Regulärer Launcher-Stand unter `app/`: 0.2.60. Der aktuellere lokale Teststand 0.2.63 ist als separates Quellcode-ZIP im Zwischenstandsordner gesichert; seine IPK wurde nicht auf GitHub hochgeladen.
- Auf dem Fernseher ist laut Nutzer inzwischen die lokale Testversion 0.2.63 installiert; der zugehörige Quellcode liegt separat im Zwischenstandsordner.
- Direct Home startet nach kurzem Ausschalten; der Test nach mehreren Stunden Standby steht noch aus. Die bisherige Methode bleibt als Rückfalllösung erhalten.
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

- Unter TV-Homescreen stehen LG Home, die bisherige Methode und die direkte Home-Übernahme zur Auswahl. Direct Home benötigt keinen Magic Mapper; vor Updates oder der Deinstallation LG Home wiederherstellen. Der Langzeittest nach mehrstündigem Standby steht aus.

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
