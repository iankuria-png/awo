// Capture Round 8 screens for the marketing boards: 390 by 844 at device scale 2, reduce-motion on, saved as JPEG
// (quality 88), the size the canvas asset store takes well. The boards must be served locally first:
//   python3 scripts/serve-boards.py <project dir> <blobs dir> 8792
//   python3 design/round-8/marketing8.py specs > caps.json
//   NODE_PATH=$(npm root -g) node design/round-8/capture8.mjs caps.json <out dir> [port=8792]
// Then upload the JPEGs to the canvas and put their /_blob/ ids in CAPS8 (marketing8.py).
import { createRequire } from 'module';
import { existsSync, readdirSync, readFileSync } from 'fs';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const [, , specFile, out, port = '8792'] = process.argv;
const specs = JSON.parse(readFileSync(specFile, 'utf8'));

const args = [];
const proxyCa = '/root/.ccr/agent-proxy-ca.crt';
if (existsSync(proxyCa)) {
  // Pin the egress proxy's CA key so TLS stays verified (never ignore all errors).
  const spki = execSync(`openssl x509 -in ${proxyCa} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim();
  args.push(`--ignore-certificate-errors-spki-list=${spki}`);
}
if (process.env.HTTPS_PROXY) {
  args.push(`--proxy-server=${process.env.HTTPS_PROXY}`, '--proxy-bypass-list=127.0.0.1;localhost');
}
let executablePath;
if (existsSync('/opt/pw-browsers')) {
  const dir = readdirSync('/opt/pw-browsers').find((d) => /^chromium-\d+$/.test(d));
  if (dir) executablePath = `/opt/pw-browsers/${dir}/chrome-linux/chrome`;
}

const browser = await chromium.launch({ headless: true, args, executablePath });
for (const s of specs) {
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, reducedMotion: 'reduce' });
  const page = await ctx.newPage();
  await page.goto(`http://127.0.0.1:${port}/project/${s.board}.dc.html`, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(2200);
  // `click` names a tab; `clicks` names buttons, pressed in order.
  for (const name of s.clicks || (s.click ? [s.click] : [])) {
    await page.getByRole(s.click ? 'tab' : 'button', { name, exact: true }).first().click({ timeout: 4000 });
    await page.waitForTimeout(700);
  }
  if (s.js) {
    await page.evaluate(s.js);
    await page.waitForTimeout(300);
  }
  // Keep the screen at phone height: nothing shrinks, and the frame is cut at 844.
  await page.evaluate(() => {
    document.querySelectorAll('.scr > *, .pane > *').forEach((e) => { e.style.flexShrink = '0'; });
    const root = [...document.querySelectorAll('div')].find((d) => d.style.width === '390px' && d.style.position === 'relative');
    if (root) root.style.height = '844px';
  });
  await page.waitForTimeout(400);
  await page.screenshot({ path: `${out}/${s.key}.jpg`, type: 'jpeg', quality: 88, clip: { x: 0, y: 0, width: 390, height: 844 } });
  console.log('captured', s.key);
  await ctx.close();
}
await browser.close();
