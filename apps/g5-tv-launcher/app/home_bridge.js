/* A typed loopback-only bridge. The TV never receives an arbitrary shell command. */
(function () {
  'use strict';
  function request(body, success, failure) {
    if (!window.G5_BRIDGE || !Number.isInteger(window.G5_BRIDGE.port)) return failure({errorText:'Local bridge unavailable'});
    fetch('http://127.0.0.1:' + window.G5_BRIDGE.port + '/api', {
      method:'POST', headers:{'Content-Type':'application/json','X-G5-Token':window.G5_BRIDGE.token},
      body:JSON.stringify(body), cache:'no-store'
    }).then(function(r){if(!r.ok)throw new Error('Local bridge HTTP '+r.status);return r.json();})
      .then(function(r){if(r.returnValue===false)failure(r);else success(r);})
      .catch(function(e){failure({errorText:e.message});});
  }
  function command(c, success, failure) {
    var m;
    if (c.indexOf('listLaunchPoints')>=0) return request({action:'apps'},success,failure);
    m=c.match(/base64 '([^']+)'/);
    if(m)return request({action:'icon',path:m[1]},success,failure);
    if(c.indexOf('com.webos.service.applicationManager/launch')>=0)return request({action:'settings'},success,failure);
    if(/home_key_helper\.py' status$/.test(c))return request({action:'legacy-status'},success,failure);
    if(/autostart_helper\.py' status$/.test(c))return request({action:'autostart-status'},success,failure);
    if(c.indexOf('/backup.json')>=0 && c.indexOf('cat ')>=0)return request({action:'backup-read'},success,failure);
    m=c.match(/printf '%s' '([A-Za-z0-9+/=]+)' \| base64 -d/);
    if(m){try{return request({action:'backup-write',backup:JSON.parse(decodeURIComponent(escape(atob(m[1]))))},success,failure);}catch(e){return failure({errorText:e.message});}}
    failure({errorText:'Unsupported operation in direct Home'});
  }
  window.G5Bridge={request:request,command:command};
})();
