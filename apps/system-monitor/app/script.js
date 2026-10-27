/* G5 System Monitor — read-only requests through webOS Homebrew service. */
(function () {
  'use strict';
  var SERVICE = 'luna://org.webosbrew.hbchannel.service';
  // This command has no user input and never writes files or changes system settings.
  var COMMAND = 'printf "STAT\\n"; head -n 1 /proc/stat; printf "MEM\\n"; cat /proc/meminfo; printf "UPTIME\\n"; cat /proc/uptime; printf "KERNEL\\n"; uname -r; printf "UID\\n"; id -u; printf "PROC\\n"; top -b -n 1 | head -n 20; printf "DISK\\n"; df -kP 2>/dev/null; printf "NET\\n"; for p in /sys/class/net/*; do [ -e "$p" ] || continue; n=${p##*/}; [ "$n" = "lo" ] && continue; printf "%s " "$n"; cat "$p/operstate" 2>/dev/null; done; printf "ADDR\\n"; (ip -o -4 addr show scope global 2>/dev/null || ifconfig 2>/dev/null); printf "ROUTE\\n"; ip route show default 2>/dev/null';
  var $ = function (id) { return document.getElementById(id); };
  var prior = null, points = [], ramPoints = [], busy = false, requestId = 0;
  var intervalSeconds = 3, intervalChoices = [3,5,10], refreshTimer = null;
  function set(id, value) { $(id).textContent = value; }
  function pct(id, value) { $(id).style.width = Math.max(0, Math.min(100, value)) + '%'; }
  function state(label, cls) { $('state').textContent = label; $('state').className = 'status ' + (cls || ''); }
  function parse(raw) {
    var parts = raw.split(/\r?\n/), sections = {}, key = null;
    parts.forEach(function (line) {
      if (/^(STAT|MEM|UPTIME|KERNEL|UID|PROC|DISK|NET|ADDR|ROUTE)$/.test(line)) { key = line; sections[key] = []; }
      else if (key) sections[key].push(line);
    });
    if (!sections.STAT || !sections.MEM || !sections.UPTIME) throw Error('Unvollständige Messdaten');
    var nums = sections.STAT[0].trim().split(/\s+/).slice(1).map(Number);
    if (nums.length < 5 || nums.some(function (n) { return !isFinite(n); })) throw Error('CPU-Daten nicht lesbar');
    var total = nums.reduce(function (a, b) { return a + b; }, 0);
    var idle = nums[3] + (nums[4] || 0); var cpu = null;
    if (prior && total > prior.total) cpu = (1 - (idle - prior.idle) / (total - prior.total)) * 100;
    prior = {total:total, idle:idle};
    var memory = {};
    sections.MEM.forEach(function (line) { var m = line.match(/^([^:]+):\s*(\d+)/); if (m) memory[m[1]] = +m[2]; });
    var mt = memory.MemTotal, ma = memory.MemAvailable;
    if (!ma && ma !== 0) ma = (memory.MemFree || 0) + (memory.Buffers || 0) + (memory.Cached || 0);
    var used = mt > 0 ? 100 * (mt - ma) / mt : null;
    return { cpu:cpu, mem:used, ramTotal:mt, ramAvailable:ma,
      swapTotal:memory.SwapTotal, swapFree:memory.SwapFree, processes: parseProcesses(sections.PROC || []),
      disks:parseDisks(sections.DISK || []), network:parseNetwork(sections.NET || [], sections.ADDR || [], sections.ROUTE || []),
      uptime:parseFloat(sections.UPTIME[0]), kernel:(sections.KERNEL || ['–'])[0], uid:(sections.UID || ['–'])[0] };
  }
  function parseDisks(lines) {
    var rows = [], seen = {};
    lines.forEach(function (line) {
      var cols = line.trim().split(/\s+/);
      if (cols.length < 6 || !/^\d+%$/.test(cols[4])) return;
      var mount = cols[cols.length - 1];
      if (mount.charAt(0) !== '/') return;
      if (/^(tmpfs|devtmpfs|proc|sysfs|cgroup|cgroup2|devpts|mqueue|securityfs|debugfs|tracefs|pstore|configfs|fusectl)$/.test(cols[0])) return;
      var total = Number(cols[1]), used = Number(cols[2]), available = Number(cols[3]);
      if (!isFinite(total) || total <= 0 || !isFinite(used) || !isFinite(available)) return;
      var signature = cols[0] + ':' + total + ':' + used + ':' + available;
      if (seen[signature]) return;
      seen[signature] = true;
      rows.push({mount:mount, total:total, used:used, available:available, percent:parseInt(cols[4],10)});
    });
    var priority = {'/media/developer':0,'/media/internal':1,'/mnt/lg':2,'/var':3,'/':4};
    rows.sort(function (a,b) {
      var ap = Object.prototype.hasOwnProperty.call(priority,a.mount) ? priority[a.mount] : 20;
      var bp = Object.prototype.hasOwnProperty.call(priority,b.mount) ? priority[b.mount] : 20;
      return ap - bp || a.mount.localeCompare(b.mount);
    });
    return rows.slice(0,5);
  }
  function parseNetwork(netLines, addressLines, routeLines) {
    var interfaces = {}, order = [];
    netLines.forEach(function (line) {
      var m = line.trim().match(/^([^\s]+)\s+(up|down|unknown|dormant|lowerlayerdown)$/i);
      if (!m) return;
      interfaces[m[1]] = {name:m[1], state:m[2], ip:''}; order.push(m[1]);
    });
    var current = '';
    addressLines.forEach(function (line) {
      var m = line.match(/^\s*\d+:\s+([^\s]+)\s+.*\binet\s+(\d+\.\d+\.\d+\.\d+)(?:\/\d+)?/);
      if (m) {
        current = m[1].replace(/@.*$/,'');
        if (!interfaces[current]) {interfaces[current]={name:current,state:'up',ip:''};order.push(current);}
        if (m[2] !== '127.0.0.1') interfaces[current].ip=m[2];
        return;
      }
      m = line.match(/^([^\s]+)\s+Link\b/);
      if (m) current=m[1];
      m = line.match(/\binet addr:(\d+\.\d+\.\d+\.\d+)/);
      if (m && current && m[1] !== '127.0.0.1') {
        if (!interfaces[current]) {interfaces[current]={name:current,state:'up',ip:''};order.push(current);}
        interfaces[current].ip=m[1];
      }
    });
    var active = order.map(function(name){return interfaces[name];}).filter(function(item){return item && (item.state === 'up' || item.ip);});
    var route = routeLines.join(' '), gatewayMatch = route.match(/\bdefault\s+via\s+(\d+\.\d+\.\d+\.\d+)/);
    return {interfaces:active, gateway:gatewayMatch ? gatewayMatch[1] : ''};
  }
  function parseProcesses(lines) {
    var header = null, result = [];
    lines.forEach(function (line) {
      var cols = line.trim().split(/\s+/);
      if (/^PID$/i.test(cols[0])) { header = cols.map(function (v) { return v.toUpperCase(); }); return; }
      if (!/^\d+$/.test(cols[0]) || cols.length < 2) return;
      var cpuIndex = header ? header.indexOf('%CPU') : -1;
      if (cpuIndex < 0 && header) cpuIndex = header.indexOf('CPU%');
      var cmdIndex = header ? header.indexOf('COMMAND') : -1;
      if (cmdIndex < 0 && header) cmdIndex = header.indexOf('CMD');
      // BusyBox top variants commonly end with %CPU COMMAND; process names may contain spaces.
      if (cmdIndex < 0) cmdIndex = cols.length - 1;
      var nameStart = cmdIndex;
      var cpu = cpuIndex >= 0 && cols[cpuIndex] ? cols[cpuIndex] : '–';
      var name = cols.slice(nameStart).join(' ');
      if (nameStart === cols.length - 1 && cmdIndex < cols.length - 1) name = cols.slice(cmdIndex).join(' ');
      result.push([cols[0], cpu, name.slice(0, 100)]);
    });
    return result.slice(0, 10);
  }
  function draw(data) {
    set('cpu', data.cpu === null ? 'Messung …' : data.cpu.toFixed(1) + ' %');
    if (data.cpu !== null) { pct('cpu-bar', data.cpu); points.push(Math.max(0, Math.min(100, data.cpu))); if (points.length > 30) points.shift(); }
    $('line').setAttribute('points', points.map(function (value,i) {return (i * 620 / 29).toFixed(1) + ',' + (170 - value * 1.7).toFixed(1);}).join(' '));
    set('ram', data.mem === null ? '–' : data.mem.toFixed(1) + ' %'); pct('ram-bar', data.mem || 0);
    if (data.mem !== null) { ramPoints.push(Math.max(0, Math.min(100, data.mem))); if (ramPoints.length > 30) ramPoints.shift(); }
    $('ram-line').setAttribute('points', ramPoints.map(function (value,i) {return (i * 620 / 29).toFixed(1) + ',' + (170 - value * 1.7).toFixed(1);}).join(' '));
    if (data.swapTotal) set('swap', Math.round((data.swapTotal - data.swapFree) / 1024) + ' / ' + Math.round(data.swapTotal / 1024) + ' MiB');
    var body = $('process-rows'); body.textContent = '';
    (data.processes || []).forEach(function(row){var tr=document.createElement('tr');row.forEach(function(v){var td=document.createElement('td');td.textContent=v;tr.appendChild(td);});body.appendChild(tr);});
    if (!body.childNodes.length) {var tr=document.createElement('tr'),td=document.createElement('td');td.colSpan=3;td.textContent='Prozessliste nicht verfügbar';tr.appendChild(td);body.appendChild(tr);}
    if (data.ramTotal) set('memory', Math.round((data.ramTotal - data.ramAvailable) / 1024) + ' / ' + Math.round(data.ramTotal / 1024) + ' MiB');
    drawDisks(data.disks || []); drawNetwork(data.network || {interfaces:[],gateway:''});
    var s = Math.floor(data.uptime); set('uptime', Math.floor(s / 86400) + 'd ' + Math.floor(s % 86400 / 3600) + 'h ' + Math.floor(s % 3600 / 60) + 'm');
    set('kernel', data.kernel || '–'); set('root', data.uid === '0' ? 'Aktiv (UID 0)' : 'Nicht bestätigt (UID ' + data.uid + ')');
    set('updated', new Date().toLocaleTimeString('de-AT'));
    state(data.uid === '0' ? 'ROOT OK' : 'LIVE · UID ' + data.uid, data.uid === '0' ? '' : 'warning');
    set('notice', 'Live-Messwerte vom Fernseher · nur lesend · Aktualisierung alle ' + intervalSeconds + ' Sekunden');
  }
  function formatGiB(kib) { return (kib / 1048576).toFixed(kib / 1048576 >= 10 ? 0 : 1) + ' GiB'; }
  function drawDisks(disks) {
    var host=$('disk-rows'); host.textContent='';
    if (!disks.length) {var row=document.createElement('div'),label=document.createElement('span'),value=document.createElement('strong');row.className='detail';label.textContent='Status';value.textContent='Nicht verfügbar';row.appendChild(label);row.appendChild(value);host.appendChild(row);return;}
    disks.forEach(function(disk){
      var entry=document.createElement('div'),row=document.createElement('div'),label=document.createElement('span'),value=document.createElement('strong');
      var bar=document.createElement('div'),fill=document.createElement('div');
      entry.className='storage-entry';row.className='storage-row';label.className='storage-mount';value.className='storage-value';label.textContent=disk.mount;label.title=disk.mount;
      value.textContent=formatGiB(disk.available)+' frei / '+formatGiB(disk.total)+' · '+disk.percent+' % belegt';
      row.appendChild(label);row.appendChild(value);
      bar.className='storage-bar';bar.setAttribute('role','progressbar');bar.setAttribute('aria-valuemin','0');bar.setAttribute('aria-valuemax','100');bar.setAttribute('aria-valuenow',String(disk.percent));
      fill.className='storage-fill';fill.style.width=Math.max(0,Math.min(100,disk.percent))+'%';bar.appendChild(fill);
      entry.appendChild(row);entry.appendChild(bar);host.appendChild(entry);
    });
  }
  function drawNetwork(network) {
    var active=network.interfaces || [];
    set('network-interface',active.length ? active.map(function(item){return item.name;}).join(', ') : 'Keine aktive Schnittstelle');
    var ips=active.filter(function(item){return item.ip;}).map(function(item){return item.name+': '+item.ip;});
    set('network-ip',ips.length ? ips.join(' · ') : 'Nicht verfügbar');
    set('network-gateway',network.gateway || 'Nicht verfügbar');
  }
  function showSystemInfo(result) {
    if (!result || result.returnValue === false) {
      set('model','Nicht verfügbar'); set('webos-version','Nicht verfügbar'); set('firmware','Nicht verfügbar'); set('board','Nicht verfügbar'); return;
    }
    set('model',result.modelName || 'Nicht verfügbar');
    var sdk=result.sdkVersion || '';
    set('webos-version',sdk || 'Nicht verfügbar');
    set('firmware',result.firmwareVersion || 'Nicht verfügbar');
    set('board',result.boardType || 'Nicht verfügbar');
  }
  function readSystemInfo() {
    var uri = 'luna://com.webos.service.tv.systemproperty';
    var parameters = {keys:['modelName','firmwareVersion','sdkVersion','boardType'], subscribe:false};
    try {
      if (window.webOS && webOS.service && typeof webOS.service.request === 'function') {
        webOS.service.request(uri, {
          method:'getSystemInfo', parameters:parameters,
          onSuccess:showSystemInfo,
          onFailure:function () { showSystemInfo(null); }
        });
      } else if (typeof window.PalmServiceBridge === 'function') {
        var bridge = new PalmServiceBridge();
        bridge.onservicecallback = function (response) {
          try { showSystemInfo(JSON.parse(response)); }
          catch (e) { showSystemInfo(null); }
        };
        bridge.call(uri + '/getSystemInfo', JSON.stringify(parameters));
      } else {
        showSystemInfo(null);
      }
    } catch (e) { showSystemInfo(null); }
  }
  function changeInterval() {
    var index=intervalChoices.indexOf(intervalSeconds);
    intervalSeconds=intervalChoices[(index+1)%intervalChoices.length];
    set('interval','Intervall: '+intervalSeconds+' s');
    $('interval').setAttribute('aria-label','Aktualisierungsintervall wechseln, aktuell '+intervalSeconds+' Sekunden');
    if (refreshTimer !== null) clearInterval(refreshTimer);
    refreshTimer=setInterval(poll,intervalSeconds*1000);
    set('notice','Live-Messwerte vom Fernseher · nur lesend · Aktualisierung alle '+intervalSeconds+' Sekunden');
  }
  function poll() {
    if (busy) return;
    if (!(window.webOS && webOS.service && typeof webOS.service.request === 'function') && typeof window.PalmServiceBridge !== 'function') {
      state('KEINE VERBINDUNG', 'bad');
      set('notice', 'Homebrew-Luna-Dienst nicht verfügbar. Die App benötigt einen gerooteten webOS-TV mit Homebrew Channel.');
      return;
    }
    busy = true;
    var currentRequest = ++requestId;
    var timeout = setTimeout(function () { if (currentRequest !== requestId) return; busy=false; state('ZEITÜBERSCHREITUNG','bad'); set('notice','Der Homebrew-Luna-Dienst hat nicht rechtzeitig geantwortet.'); }, 2300);
    function finishRequest() { if (currentRequest !== requestId) return false; clearTimeout(timeout); busy=false; return true; }
    try {
      var requestOptions = {
        method: 'exec', parameters: {command: COMMAND},
        onSuccess: function (result) {
          if (!finishRequest()) return;
          if (!result || result.returnValue === false || result.error || typeof result.stdoutString !== 'string') {state('ABFRAGEFEHLER','bad');set('notice', String((result && (result.error || result.errorText)) || 'Keine lesbaren Daten zurückgegeben'));return;}
          try {draw(parse(result.stdoutString));} catch (e) {state('DATENFEHLER','bad');set('notice',e.message);}
        },
        onFailure: function (err) {if (!finishRequest()) return;state('ABFRAGEFEHLER','bad');set('notice', (err && (err.errorText || err.message)) || 'Zugriff auf den Homebrew-Dienst fehlgeschlagen');}
      };
      if (window.webOS && webOS.service && typeof webOS.service.request === 'function') {
        webOS.service.request(SERVICE, requestOptions);
      } else {
        // Built-in Luna bridge: no external library or network dependency.
        var bridge = new PalmServiceBridge();
        bridge.onservicecallback = function (response) {
          var result;
          try { result = JSON.parse(response); } catch (e) { result = {error:'Ungültige Luna-Antwort'}; }
          if (result.returnValue === false || result.error) requestOptions.onFailure({errorText:result.error || result.errorText || 'Luna-Zugriff verweigert'});
          else requestOptions.onSuccess(result);
        };
        bridge.call(SERVICE + '/exec', JSON.stringify({command:COMMAND}));
      }
    } catch(e) {finishRequest();state('ABFRAGEFEHLER','bad');set('notice',e.message);}
  }
  function exitApp() {
    if (window.webOS && typeof webOS.platformBack === 'function') webOS.platformBack();
    else window.close();
  }
  $('refresh').addEventListener('click', poll);
  $('interval').addEventListener('click', changeInterval);
  $('exit').addEventListener('click', exitApp);
  document.addEventListener('keydown', function (e) {
    if ((e.keyCode || e.which) === 461) { e.preventDefault(); exitApp(); return; }
    if (e.key === 'Enter' && document.activeElement === $('refresh')) { e.preventDefault(); poll(); return; }
    if (e.key === 'Enter' && document.activeElement === $('interval')) { e.preventDefault(); changeInterval(); return; }
    if (e.key === 'Enter' && document.activeElement === $('exit')) { e.preventDefault(); exitApp(); return; }
    var target = e.target;
    if (target && /^(INPUT|TEXTAREA|SELECT|BUTTON)$/.test(target.tagName)) return;
    var key = e.key || '';
    var code = e.keyCode || 0;
    if (key === 'ArrowDown' || key === 'PageDown' || code === 40 || code === 34) {
      e.preventDefault(); window.scrollBy(0, key === 'PageDown' || code === 34 ? window.innerHeight * 0.78 : window.innerHeight * 0.35);
    } else if (key === 'ArrowUp' || key === 'PageUp' || code === 38 || code === 33) {
      e.preventDefault(); window.scrollBy(0, -(key === 'PageUp' || code === 33 ? window.innerHeight * 0.78 : window.innerHeight * 0.35));
    }
  });
  // Some LG remote pointers emit wheel events that webOS does not pass through
  // to the document's native scroller. Forward them explicitly to the page.
  window.addEventListener('wheel', function (e) {
    var delta = e.deltaY || 0;
    if (!delta) return;
    if (e.deltaMode === 1) delta *= 40;
    else if (e.deltaMode === 2) delta *= window.innerHeight;
    e.preventDefault();
    window.scrollBy(0, delta);
  }, {passive:false});
  readSystemInfo(); poll(); refreshTimer=setInterval(poll,intervalSeconds*1000);
}());
