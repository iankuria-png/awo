// Export one canvas page (e.g. the Round 7 board) for download, since the canvas's own export is too large for a
// page of 160 boards. Step 1 of 2: render every board on the page, in section order, to its own PDF page at its exact
// size (vector text, live fonts) and to a JPEG thumbnail; plus one divider page per section title.
// Step 2 is scripts/export-page.py, which merges the PDFs and builds the offline HTML viewer.
//
// Serve the boards first (live files read from the artifact, with support.js and the images):
//   python3 scripts/serve-boards.py <root> <blob dir> 8797
//   NODE_PATH=$(npm root -g) node scripts/export-page.mjs <canvas.json> r7 <out dir> [port=8797]
import { createRequire } from 'module';
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from 'fs';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const [, , canvasFile, pageId, out, port = '8797'] = process.argv;
const c = JSON.parse(readFileSync(canvasFile, 'utf8'));

// Sections are the page's title notes (empty ones are skipped); a board belongs to the last title above it.
const titles = Object.values(c.notes).filter((n) => n.page === pageId && n.kind === 'title1' && (n.text || '').trim()).sort((a, b) => a.y - b.y);
const boards = Object.entries(c.boards).filter(([, b]) => b.page === pageId).map(([file, b]) => ({ file, ...b }))
  .sort((a, b) => a.y - b.y || a.x - b.x);
const plan = titles.map((t) => ({ title: t.text, boards: [] }));
for (const b of boards) {
  let i = titles.length - 1;
  while (i > 0 && titles[i].y > b.y) i--;
  plan[Math.max(0, i)].boards.push(b);
}
for (const d of ['pdf', 'jpg']) mkdirSync(`${out}/${d}`, { recursive: true });
writeFileSync(`${out}/plan.json`, JSON.stringify(plan, null, 1));

const args = [];
const proxyCa = '/root/.ccr/agent-proxy-ca.crt';
if (existsSync(proxyCa)) {
  // Pin the egress proxy's CA key so TLS stays verified (never ignore all errors).
  const spki = execSync(`openssl x509 -in ${proxyCa} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim();
  args.push(`--ignore-certificate-errors-spki-list=${spki}`);
}
if (process.env.HTTPS_PROXY) args.push(`--proxy-server=${process.env.HTTPS_PROXY}`, '--proxy-bypass-list=127.0.0.1;localhost');
let executablePath;
if (existsSync('/opt/pw-browsers')) {
  const dir = readdirSync('/opt/pw-browsers').find((d) => /^chromium-\d+$/.test(d));
  if (dir) executablePath = `/opt/pw-browsers/${dir}/chrome-linux/chrome`;
}
const browser = await chromium.launch({ headless: true, args, executablePath });

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
let n = 0;
for (const [si, sec] of plan.entries()) {
  // A divider page: the section's number, title and what it holds.
  const ctx0 = await browser.newContext({ viewport: { width: 1600, height: 900 } });
  const p0 = await ctx0.newPage();
  const list = sec.boards.map((b) => `<li>${esc(b.title || b.file.replace('.dc.html', ''))}</li>`).join('');
  await p0.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&display=swap" rel="stylesheet">
    <style>body{margin:0;width:1600px;height:900px;background:#0F4A36;color:#fff;font-family:Geist,sans-serif;box-sizing:border-box;padding:110px 120px;display:flex;flex-direction:column;gap:36px}
    .n{font-size:28px;color:#D8F36A;font-weight:600}h1{margin:0;font-size:76px;line-height:1;letter-spacing:-.04em;font-weight:600;max-width:1300px}
    ul{margin:0;padding:0;list-style:none;columns:2;column-gap:60px;font-size:22px;line-height:1.6;color:#BFDCCF}</style></head>
    <body><span class="n">Section ${si + 1} of ${plan.length}</span><h1>${esc(sec.title)}</h1><ul>${list}</ul></body></html>`, { waitUntil: 'networkidle' });
  await p0.evaluate(() => document.fonts.ready);
  await p0.pdf({ path: `${out}/pdf/${String(si + 1).padStart(2, '0')}-000-section.pdf`, width: '1600px', height: '900px', printBackground: true });
  await ctx0.close();
  for (const [bi, b] of sec.boards.entries()) {
    const ctx = await browser.newContext({ viewport: { width: b.w, height: b.h }, reducedMotion: 'reduce' });
    const page = await ctx.newPage();
    await page.emulateMedia({ media: 'screen', reducedMotion: 'reduce' });
    await page.goto(`http://127.0.0.1:${port}/project/${b.file}`, { waitUntil: 'networkidle', timeout: 90000 });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(1200);
    const base = `${String(si + 1).padStart(2, '0')}-${String(bi + 1).padStart(3, '0')}-${b.file.replace('.dc.html', '')}`;
    await page.pdf({ path: `${out}/pdf/${base}.pdf`, width: `${b.w}px`, height: `${b.h}px`, printBackground: true, pageRanges: '1' });
    await page.screenshot({ path: `${out}/jpg/${b.file.replace('.dc.html', '')}.jpg`, type: 'jpeg', quality: 82 });
    await ctx.close();
    n++;
    if (n % 20 === 0) console.log(`${n} of ${boards.length}`);
  }
}
await browser.close();
console.log(`rendered ${n} boards in ${plan.length} sections`);
