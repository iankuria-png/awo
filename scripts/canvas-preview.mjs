// Render Design-canvas boards (.dc.html) locally and screenshot them, so Claude can check its own work.
//
// Why: the canvas runtime only runs inside claude.ai. This serves a board folder with the runtime as
// `support.js`, maps uploaded images (`/_blob/<id>`) to local files, and screenshots each board at its
// exact size. Optional click steps capture interactive states.
//
// Setup (once per session):
//   1. Artifact read the canvas's `artifact-type/dc-runtime.js` (it saves under the scratchpad).
//   2. Keep a JSON map of uploaded blob ids to local files: {"<id>": "/abs/path/image.jpg"}.
//
// Usage:
//   RUNTIME=/path/dc-runtime.js ROOT=/path/to/project BLOBS=/path/blobs.json OUT=/path/shots \
//   NODE_PATH=$(npm root -g) node scripts/canvas-preview.mjs "Board.dc.html|390|844|2500|sel1,sel2" ...
//
//   Each spec is file|width|height|waitMs|clicks. `clicks` is an optional comma list of Playwright
//   selectors (e.g. button:has-text("Next")); every click saves an extra shot (<name>-s1.png, ...).
//   Set RM=1 to emulate prefers-reduced-motion, SCALE=2 for retina shots.
import http from 'http';
import { createRequire } from 'module';
import { existsSync, readFileSync, readdirSync, mkdirSync } from 'fs';
import { execSync } from 'child_process';
import { extname, join, basename } from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const { RUNTIME, ROOT, BLOBS, OUT = 'shots' } = process.env;
if (!RUNTIME || !ROOT) {
  console.error('Set RUNTIME (path to dc-runtime.js) and ROOT (folder with the .dc.html boards).');
  process.exit(1);
}
mkdirSync(OUT, { recursive: true });

const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.css': 'text/css' };
const server = http.createServer((req, res) => {
  const p = decodeURIComponent(req.url.split('?')[0]);
  let file = null;
  if (p.endsWith('/support.js')) file = RUNTIME;
  else if (p.startsWith('/_blob/') && BLOBS && existsSync(BLOBS)) file = JSON.parse(readFileSync(BLOBS, 'utf8'))[p.slice(7)] || null;
  else file = join(ROOT, p);
  if (!file || !existsSync(file)) { res.writeHead(404); return res.end('not found'); }
  res.writeHead(200, { 'content-type': types[extname(file).toLowerCase()] || 'application/octet-stream' });
  res.end(readFileSync(file));
});
await new Promise((resolve) => server.listen(0, resolve));
const port = server.address().port;

// Trust the cloud session's egress proxy by its key pin, so TLS stays verified (Google Fonts, CDN).
const args = [];
const proxyCa = '/root/.ccr/agent-proxy-ca.crt';
if (existsSync(proxyCa)) {
  const spki = execSync(`openssl x509 -in ${proxyCa} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim();
  args.push(`--ignore-certificate-errors-spki-list=${spki}`);
}
let executablePath;
if (existsSync('/opt/pw-browsers')) {
  const dir = readdirSync('/opt/pw-browsers').find((d) => /^chromium-\d+$/.test(d));
  if (dir) executablePath = `/opt/pw-browsers/${dir}/chrome-linux/chrome`;
}
const browser = await chromium.launch({ headless: true, args, executablePath });

for (const spec of process.argv.slice(2)) {
  const [file, w, h, wait = '2500', clicks = ''] = spec.split('|');
  const page = await browser.newPage({
    viewport: { width: Number(w), height: Number(h) },
    deviceScaleFactor: Number(process.env.SCALE || 1),
    reducedMotion: process.env.RM ? 'reduce' : 'no-preference',
  });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message.slice(0, 200)));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|404/.test(m.text())) errors.push(m.text().slice(0, 200)); });
  await page.goto(`http://localhost:${port}/${file}`, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(Number(wait));
  const stem = join(OUT, basename(file).replace(/\.dc\.html$|\.html$/, ''));
  await page.screenshot({ path: `${stem}.png` });
  console.log(`${stem}.png`, errors.length ? `ERRORS: ${errors.join(' | ')}` : 'ok');
  let i = 0;
  for (const selector of clicks.split(',').filter(Boolean)) {
    i += 1;
    try { await page.click(selector, { timeout: 5000 }); } catch (e) { console.log('click failed:', selector); }
    await page.waitForTimeout(Number(process.env.STEPWAIT || 1200));
    await page.screenshot({ path: `${stem}-s${i}.png` });
    console.log(`${stem}-s${i}.png`);
  }
  await page.close();
}
await browser.close();
server.close();
