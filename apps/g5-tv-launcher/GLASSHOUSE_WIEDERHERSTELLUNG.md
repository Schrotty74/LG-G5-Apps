# G5 Launcher: Glasshouse und LG Home

Beim Glasshouse-Server-Update am 2. November 2026 kam es zu einem Konflikt: G5 Direct Home war eingebunden; Glasshouse Home war deaktiviert, aber `restorePending` war noch aktiv. Der Wechsel auf LG Home und die Glasshouse-Wiederherstellung blockierten sich. Nach der unten beschriebenen Rückkehr zu LG Home konnte die Wiederherstellung in Glasshouse erneut erfolgreich ausgeführt und das Update installiert werden. Die ursprüngliche Ursache des Updatefehlers ist nicht bewiesen.

Vor künftigen Glasshouse-Server-Updates: im G5 Launcher auf LG Home umstellen; nach Abschluss des Updates kann Direct Home erneut aktiviert werden.

## Wiederherstellung bei demselben Konflikt

Nur verwenden, wenn der Zustand erneut geprüft wurde: G5 Direct Home besitzt den Home-Mount und Glasshouse Home ist wirklich deaktiviert. Der Befehl prüft dies und umgeht die Glasshouse-Statusprüfung nur für diesen einzelnen Prozess; er ändert Glasshouses `home.json` nicht. Er wurde vom Nutzer am 2. November 2026 ausgeführt und meldete `{'ok': True, 'method': 'lg'}`; LG Home erschien wieder. Anschließend wurde in Glasshouse „Retry restoring LG Home“ erfolgreich ausgeführt. Nicht als allgemeine Lösung für andere Fehler verwenden.

```sh
cd /media/developer/apps/usr/palm/applications/org.schrotty74.g5launcher && python3 -c "import home_mode_helper as h; assert h.owned_mount() and not h.foreign_mount() and h.load('/var/lib/tvweb/home.json',{}).get('enabled') is False, 'Sicherheitsprüfung fehlgeschlagen'; h.glasshouse_enabled=lambda:False; print(h.recover())"
```
