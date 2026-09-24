// Screenshot any page with headless Chromium (works in cloud sessions).
// Usage: node scripts/screenshot.mjs <url> <out.png> [waitMs=6000] [fullPage=false] [width=1440] [height=1000]
// Run with: NODE_PATH=$(npm root -g) node scripts/screenshot.mjs ...
import { createRequire } from 'module';
import { existsSync, readdirSync } from 'fs';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const [, , url, out, wait = '6000', full = 'false', w = '1440', h = '1000'] = process.argv;

const args = [];
const proxyCa = '/root/.ccr/agent-proxy-ca.crt';
if (existsSync(proxyCa)) {
  // Pin the egress proxy's CA key so TLS stays verified (never ignore all errors).
  const spki = execSync(`openssl x509 -in ${proxyCa} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim();
  args.push(`--ignore-certificate-errors-spki-list=${spki}`);
}
let executablePath;
if (existsSync('/opt/pw-browsers')) {
  const dir = readdirSync('/opt/pw-browsers').find((d) => /^chromium-\d+$/.test(d));
  if (dir) executablePath = `/opt/pw-browsers/${dir}/chrome-linux/chrome`;
}

const browser = await chromium.launch({ headless: true, args, executablePath });
const page = await browser.newPage({
  viewport: { width: Number(w), height: Number(h) },
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36',
});
try {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(Number(wait));
  console.log('status', res && res.status(), '| title', await page.title());
  await page.screenshot({ path: out, fullPage: full === 'true' });
} catch (e) {
  console.log('ERR', e.message.split('\n')[0]);
}
await browser.close();
