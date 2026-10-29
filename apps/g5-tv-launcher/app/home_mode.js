/* Direct Home integration: actual status comes from the TV, never preferences. */
(function () {
  'use strict';
  var helper = '/media/developer/apps/usr/palm/applications/org.schrotty74.g5launcher/home_mode_helper.py';
  var ready = false, busy = false, saveTimer = null, lastSettings = null, pending = null;
  var direct = window.G5_DIRECT_HOME === true;
  var legacyBlocked = direct;
  var messages = {
    checking: ['Status wird geprüft …', 'Checking actual TV status …'],
    changing: ['Methode wird gewechselt. Bitte warten …', 'Switching method. Please wait …'],
    direct: ['Direkte Home-Übernahme aktiv – webOS-Eintrag und Oberfläche geprüft.', 'Direct Home active – webOS registration and page response verified.'],
    incomplete: ['Home-Übernahme ist unvollständig. Status prüfen oder LG Home wiederherstellen.', 'Home takeover is incomplete. Refresh status or restore LG Home.'],
    legacy: ['Bisherige Methode aktiv. Home-Taste und Autostart werden separat angezeigt.', 'Legacy method active. Home mapping and autostart are shown separately.'],
    lg: ['Keine Home-Übernahme durch diesen Launcher aktiv.', 'This launcher is not taking over Home.'],
    conflict: ['Glasshouse oder eine andere Home-Übernahme ist aktiv. Bitte dort zuerst ausschalten.', 'Glasshouse or another Home takeover is active. Switch it off there first.'],
    error: ['Fehler: ', 'Error: '],
    timeout: ['Keine Antwort. Der Vorgang kann noch laufen. Nicht erneut anwenden; später Status prüfen.', 'No response. The operation may still be running. Do not apply again; refresh status later.'],
    confirm: ['Zum Bestätigen dieselbe Schaltfläche erneut drücken. Home-Belegung und Autostart werden angepasst; andere Tasten bleiben erhalten.', 'Press the same button again to confirm. Home mapping and autostart will change; other buttons are preserved.'],
    warning: ['Gemeinsame Einstellungen konnten nicht geladen werden. Lokale Einstellungen bleiben erhalten.', 'Shared settings could not be loaded. Local settings are preserved.'],
    saving: ['Gemeinsame Einstellungen konnten nicht gespeichert werden.', 'Shared settings could not be saved.']
  };
  function language() { return document.documentElement.lang === 'de' ? 0 : 1; }
  function msg(key) { return messages[key][language()]; }
  function status(text) { var el = document.getElementById('home-method-status'); if (el) el.textContent = text; }
  function encode(value) { return btoa(unescape(encodeURIComponent(JSON.stringify(value)))); }
  function request(action, value, done) {
    if (!/^(status|direct|legacy|lg|recover|prefs-load|prefs-save|heartbeat)$/.test(action)) return done(new Error('Invalid operation'));
    var suffix = value == null ? '' : " '" + encode(value) + "'";
    var command = "python3 '" + helper + "' " + action + suffix;
    var bridge, finished = false;
    var timer = setTimeout(function () { finish(new Error(msg('timeout'))); }, action === 'prefs-load' ? 8000 : action === 'status' ? 20000 : 100000);
    function finish(error, result) { if (finished) return; finished = true; clearTimeout(timer); done(error, result); }
    function success(res) {
      try {
        var result = JSON.parse(res.stdoutString || '');
        if (result.ok !== true) throw new Error(result.message || 'Home operation failed');
        finish(null, result);
      } catch (e) { finish(e); }
    }
    function failure(res) { finish(new Error(res.errorText || 'Homebrew service unavailable')); }
    try {
      if (direct) {
        return G5Bridge.request({action:'home',operation:action,settings:value},success,failure);
      }
      if (window.webOS && webOS.service && webOS.service.request) {
        webOS.service.request('luna://org.webosbrew.hbchannel.service', { method: 'exec', parameters: {command: command}, onSuccess: success, onFailure: failure });
      } else {
        bridge = new PalmServiceBridge();
        bridge.onservicecallback = function (raw) {
          try { var data = JSON.parse(raw); if (data.returnValue === false) failure(data); else success(data); }
          catch (e) { finish(e); }
        };
        bridge.call('luna://org.webosbrew.hbchannel.service/exec', JSON.stringify({command: command}));
      }
    } catch (e) { finish(e); }
  }
  function controlBusy(value) {
    busy = value;
    ['home-method-apply', 'home-method', 'home-method-refresh', 'home-method-recover', 'home-key-enable', 'home-key-restore', 'autostart-enable', 'autostart-disable'].forEach(function (id) {
      var el = document.getElementById(id); if (el) el.disabled = value;
    });
  }
  function show(result) {
    var choose = document.getElementById('home-method');
    if (choose) choose.value = result.method;
    var owns = result.mounted || result.configured === 'direct' || result.transition;
    legacyBlocked = !!owns || !!result.conflict;
    ['home-key-enable', 'home-key-restore', 'autostart-enable', 'autostart-disable'].forEach(function (id) {
      var el = document.getElementById(id); if (el) el.disabled = busy || legacyBlocked;
    });
    var key = result.conflict ? 'conflict' : (result.transition || (result.configured === 'direct' && (!result.mounted || !result.registered || !result.startup || !result.watching))) ? 'incomplete' : result.method;
    if (key === 'direct' && !result.verified) key = 'incomplete';
    status(msg(key) + (result.error ? ' ' + result.error : ''));
  }
  function refresh() {
    if (busy) return;
    status(msg('checking'));
    request('status', null, function (error, result) { if (error) status(msg('error') + error.message); else show(result); });
  }
  function change(recover) {
    if (busy) return;
    var choose = document.getElementById('home-method');
    var action = recover ? 'recover' : choose.value;
    if (pending !== action) { pending = action; status(msg('confirm')); return; }
    pending = null;
    controlBusy(true); status(msg('changing'));
    request(action, lastSettings, function (error, result) {
      controlBusy(false);
      if (error) { status(msg('error') + error.message); return; }
      if (recover) refresh(); else show(result);
    });
  }
  function beat() {
    if (!direct || document.hidden) return;
    request('heartbeat', null, function (error) { if (error) status(msg('error') + error.message); });
  }
  window.G5HomeMode = {
    load: function (done) {
      request('prefs-load', null, function (error, result) {
        // On failure do not overwrite an unreadable shared store with local defaults.
        ready = !error;
        done(!error && result.settings ? result.settings : null);
        if (error) status(msg('warning'));
      });
    },
    save: function (prefs) {
      lastSettings = JSON.parse(JSON.stringify(prefs));
      if (!ready || document.hidden) return;
      clearTimeout(saveTimer);
      saveTimer = setTimeout(function () {
        request('prefs-save', lastSettings, function (error) { if (error) status(msg('saving')); });
      }, 400);
    },
    init: function () {
      document.getElementById('home-method-apply').addEventListener('click', function () { change(false); });
      document.getElementById('home-method-recover').addEventListener('click', function () { change(true); });
      document.getElementById('home-method-refresh').addEventListener('click', function(){ pending=null; refresh(); });
      document.getElementById('home-method').addEventListener('change', function(){ pending=null; });
      document.addEventListener('visibilitychange', function () { if (!document.hidden) { beat(); refresh(); } });
      beat(); setInterval(beat, 10000); refresh();
    },
    blockLegacy: function(){return busy || legacyBlocked;},
    refresh: refresh
  };
})();
