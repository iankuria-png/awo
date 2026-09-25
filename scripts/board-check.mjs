// Render Design-canvas boards locally, click through their states and flag problems (D-026).
// Serve the boards first with scripts/serve-boards.py, then run from a work folder (shots go to ./shots):
//   NODE_PATH=$(npm root -g) PORT=8792 node /path/to/scripts/board-check.mjs plan.json [BoardName ...]
// plan.json: [{"name": "R7-Me", "w": 390, "h": 1390, "wait": 2500, "scale": 1, "reduced": false,
//              "out": "optional-shot-prefix",
//              "steps": [{"click": "Button name", "role": "button|switch|tab|checkbox", "exact": false},
//                        {"sel": "css selector"}, {"fill": ["#input", "text"]}, {"range": ["#slider", "3200"]},
//                        {"js": "code to run"}, {"wait": 900, "shot": false}]}]
// For each board it prints unresolved {{holes}}, text under 12px, targets under 40px, overflow and broken images.
import { createRequire } from 'module';
import { existsSync, readdirSync, readFileSync, writeFileSync } from 'fs';
import { execSync } from 'child_process';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const R = process.cwd();
const PORT = process.env.PORT || 8790;
const plan = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const only = process.argv.slice(3);
const args = [];
const ca = '/root/.ccr/agent-proxy-ca.crt';
if (existsSync(ca)) {
  const spki = execSync(`openssl x509 -in ${ca} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim();
  args.push(`--ignore-certificate-errors-spki-list=${spki}`);
}
if (process.env.HTTPS_PROXY) { args.push('--proxy-server=' + process.env.HTTPS_PROXY); args.push('--proxy-bypass-list=127.0.0.1;localhost'); }
const dir = readdirSync('/opt/pw-browsers').find((d) => /^chromium-\d+$/.test(d));
const browser = await chromium.launch({ headless: true, args, executablePath: `/opt/pw-browsers/${dir}/chrome-linux/chrome` });
for (const b of plan) {
  if (only.length && !only.includes(b.name)) continue;
  const ctx = await browser.newContext({ viewport: { width: b.w, height: b.h }, deviceScaleFactor: b.scale || 1, reducedMotion: b.reduced ? 'reduce' : 'no-preference' });
  const page = await ctx.newPage();
  const errs = [];
  page.on('console', (m) => { if (m.type() === 'error' && !/status of 404/.test(m.text())) errs.push(m.text().slice(0, 200)); });
  page.on('pageerror', (e) => errs.push('pageerror ' + String(e.message).slice(0, 200)));
  page.on('response', (r) => { if (r.status() >= 400 && !r.url().endsWith('favicon.ico')) errs.push(r.status() + ' ' + r.url().slice(0, 100)); });
  await page.goto(`http://127.0.0.1:${PORT}/project/${b.name}.dc.html`, { waitUntil: 'networkidle', timeout: 60000 }).catch((e) => errs.push('goto ' + e.message.split('\n')[0]));
  await page.waitForTimeout(b.wait || 2200);
  const check = async () => page.evaluate(() => {
    const t = document.body.innerText;
    const small = [...document.querySelectorAll('body *')].filter((el) => {
      if (!el.childNodes.length || ![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) return false;
      const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
      return r.width > 0 && parseFloat(cs.fontSize) < 12;
    }).map((el) => el.textContent.trim().slice(0, 30) + '@' + getComputedStyle(el).fontSize);
    const tiny = [...document.querySelectorAll('button, a[href], input, textarea')].filter((el) => { const r = el.getBoundingClientRect(); return r.width > 0 && (r.height < 40 || r.width < 40); }).map((el) => (el.textContent.trim() || el.getAttribute('aria-label') || el.tagName).slice(0, 24) + ' ' + Math.round(el.getBoundingClientRect().width) + 'x' + Math.round(el.getBoundingClientRect().height));
    const over = document.documentElement.scrollHeight > window.innerHeight + 2 || document.documentElement.scrollWidth > window.innerWidth + 2;
    const broken = [...document.querySelectorAll('img')].filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.getAttribute('src'));
    return { braces: (t.match(/\{\{[^}]{0,30}/g) || []).slice(0, 3), small: [...new Set(small)].slice(0, 6), tiny: [...new Set(tiny)].slice(0, 6), over, broken };
  });
  const shots = [];
  const snap = async (i) => { const p = `${R}/shots/${b.out || b.name}-${i}.png`; await page.screenshot({ path: p }); shots.push(await check()); };
  await snap(0);
  let i = 1;
  for (const s of (b.steps || [])) {
    try {
      if (s.click) await page.getByRole(s.role || 'button', { name: s.click, exact: !!s.exact }).first().click({ timeout: 4000 });
      if (s.sel) await page.locator(s.sel).first().click({ timeout: 4000 });
      if (s.js) await page.evaluate(s.js);
      if (s.fill) await page.locator(s.fill[0]).first().fill(s.fill[1]);
      if (s.range) await page.locator(s.range[0]).first().evaluate((el, v) => { const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set; set.call(el, v); el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }, s.range[1]);
    } catch (e) { errs.push(`step ${i} ${JSON.stringify(s)}: ${e.message.split('\n')[0]}`); }
    await page.waitForTimeout(s.wait || 900);
    if (s.shot !== false) { await snap(i); i++; }
  }
  const agg = { braces: [...new Set(shots.flatMap((x) => x.braces))], small: [...new Set(shots.flatMap((x) => x.small))], tiny: [...new Set(shots.flatMap((x) => x.tiny))], over: shots.some((x) => x.over), broken: [...new Set(shots.flatMap((x) => x.broken))] };
  console.log(b.name, 'shots', i, JSON.stringify(agg), errs.length ? 'ERRS ' + JSON.stringify(errs.slice(0, 5)) : '');
  await ctx.close();
}
await browser.close();
