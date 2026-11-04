const fs = require('fs');
const source = fs.readFileSync('app/script.js', 'utf8');
const start = source.indexOf('  function checkedScene(');
const end = source.indexOf('  function themes()', start);
if (start < 0 || end < 0) throw new Error('Theme validator not found');
eval(source.slice(start, end));
const theme = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
if (!checkedTheme(theme)) throw new Error('Theme rejected');
for (const image of ['https://example.com/a.png', 'data:image/svg+xml;base64,PHN2Zz4=']) {
  const invalid = JSON.parse(JSON.stringify(theme));
  invalid.scene.find(x => x.type === 'image').image = image;
  if (checkedTheme(invalid)) throw new Error('Unsafe image accepted');
}
const invalid = JSON.parse(JSON.stringify(theme));
invalid.scene.find(x => x.type === 'image').animation.rotation = 361;
if (checkedTheme(invalid)) throw new Error('Invalid animation accepted');
console.log('JavaScript theme validation passed');
