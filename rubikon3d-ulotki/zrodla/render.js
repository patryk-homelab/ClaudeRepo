// Render each leaflet HTML to: print PDF (111x154 mm incl. 3 mm bleed) + PNG preview cropped to trim (105x148).
const { chromium } = require('playwright');
const path = require('path');
const dir = __dirname;
const out = process.argv[2];
const names = process.argv.length > 3 ? process.argv.slice(3) : ['A-paczka', 'A-paczka-bardzo-dziekujemy', 'D-pomysly'];
(async () => {
  const b = await chromium.launch();
  for (const n of names) {
    const url = 'file://' + path.join(dir, n + '.html');
    const p = await b.newPage();
    await p.goto(url); await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(out, `Rubikon3D-ulotka-A6-${n}-druk-spad3mm.pdf`), width: '111mm', height: '154mm', printBackground: true, pageRanges: '1' });
    const px = 96 / 25.4; // css px per mm
    const v = await b.newPage({ viewport: { width: Math.round(111 * px), height: Math.round(154 * px) }, deviceScaleFactor: 4 });
    await v.goto(url); await v.evaluate(() => document.fonts.ready);
    await v.screenshot({ path: path.join(out, `Rubikon3D-ulotka-A6-${n}-podglad.png`), clip: { x: 3 * px, y: 3 * px, width: 105 * px, height: 148 * px } });
  }
  await b.close();
})();
