const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1920,height:1080}});
  const errors=[];
  page.on('pageerror', e=>errors.push(e.message));
  await page.addInitScript(() => {
    window.confirm=()=>true;
    window._mockMethod='lg';
    window._commands=[];
    window.PalmServiceBridge=function(){this.call=(uri,raw)=>{
      const params=JSON.parse(raw), c=params.command||'';
      window._commands.push(c);
      let result={ok:true};
      if(c.includes('home_mode_helper.py')){
        const action=c.match(/home_mode_helper.py' (\S+)/)[1];
        if(action==='prefs-load')result.settings={showClock:true,city:'',favorites:[],language:'en'};
        if(['direct','legacy','lg','recover'].includes(action))window._mockMethod=action==='recover'?'lg':action;
        if(['status','direct','legacy','lg'].includes(action)){
          const direct=window._mockMethod==='direct';
          Object.assign(result,{method:window._mockMethod,configured:window._mockMethod,mounted:direct,registered:direct,verified:direct,startup:direct,watching:direct,conflict:false});
        }
      }else if(c.includes('home_key_helper.py'))Object.assign(result,{active:true,installed:true,mapped:false,canRestore:true});
      else if(c.includes('autostart_helper.py'))Object.assign(result,{enabled:false,running:false});
      else if(c.includes('listLaunchPoints'))result={returnValue:true,launchPoints:[]};
      setTimeout(()=>this.onservicecallback(JSON.stringify({returnValue:true,stdoutString:JSON.stringify(result)})),5);
    };};
  });
  await page.goto('file://'+path.resolve(__dirname,'app/index.html'));
  await page.waitForFunction(()=>document.getElementById('home-method-status').textContent.includes('not taking over'));
  await page.click('#settings-open');
  await page.getByRole('button',{name:'Start & Home',exact:true}).click();
  await page.selectOption('#home-method','direct');
  await page.click('#home-method-apply');
  await page.waitForFunction(()=>document.getElementById('home-method-status').textContent.includes('Direct Home active'));
  if(!await page.isDisabled('#home-key-enable')||!await page.isDisabled('#autostart-enable'))throw Error('Legacy controls not blocked');
  await page.getByRole('button',{name:'General',exact:true}).click();
  await page.selectOption('#language-select','de');
  await page.getByRole('button',{name:'Start & Home',exact:true}).click();
  await page.click('#home-method-refresh');
  await page.waitForFunction(()=>document.getElementById('home-method-status').textContent.includes('Direkte Home-Übernahme aktiv'));
  const options=await page.locator('#home-method option').allTextContents();
  if(options.join('|')!=='LG Home|Bisherige Methode|Direkte Home-Übernahme')throw Error('German options missing');
  if(errors.length)throw Error(errors.join('\n'));
  console.log('UI OK: English/German menu, method switch, observed status, legacy controls disabled. Service responses mocked; no TV test.');
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
