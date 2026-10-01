"""Export one canvas page for download, step 2 of 2 (step 1 is scripts/export-page.mjs, which renders the boards).

Builds, in <out dir>:
  <name>.pdf             every board as one page at its own size, a divider page per section, bookmarks for both
  sections/NN-....pdf    the same, one PDF per section, for sharing a part
  <name>-offline.zip     an offline viewer: index.html with every section and a thumbnail of every board; click one to
                         open its page in the bundled PDF. The live boards are in live/: browsers block the canvas
                         runtime on double-clicked files, so serve the folder (python3 -m http.server) to use them.

Usage:
  python3 scripts/export-page.py <out dir from step 1> <folder of boards and support.js> <blob dir> <name> "<title>"
Needs pypdf and Pillow; with PyMuPDF too, images are recompressed as JPEG (quality 82, at most 150 dpi on the page),
which halves the PDF (37 MB to 18 MB for the Round 7 board) with no visible change. Chromium stores them losslessly."""
import html
import json
import os
import re
import shutil
import sys
import zipfile

from PIL import Image
from pypdf import PdfReader, PdfWriter

out, proj, blobs, name, title = sys.argv[1:6]
plan = json.load(open(os.path.join(out, 'plan.json')))
pdfs = sorted(os.listdir(os.path.join(out, 'pdf')))


def label(b):
    return b.get('title') or b['file'].replace('.dc.html', '')


def slug(t):
    return re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-')[:60]


# ---------------------------------------------------------------- PDFs

def shrink(path):
    try:
        import pymupdf
    except ImportError:
        return
    d = pymupdf.open(path)
    d.rewrite_images(quality=82, dpi_threshold=200, dpi_target=150)
    d.save(path + '.tmp', garbage=4, deflate=True, use_objstms=1)
    d.close()
    os.replace(path + '.tmp', path)


def build_pdf(path, sections):
    w = PdfWriter()
    for si, sec in sections:
        n = f'{si + 1:02d}'
        files = [f for f in pdfs if f.startswith(n + '-')]
        start = len(w.pages)
        for f in files:
            w.append(PdfReader(os.path.join(out, 'pdf', f)))
        parent = w.add_outline_item(f'{si + 1}. {sec["title"]}', start)
        for bi, b in enumerate(sec['boards']):
            w.add_outline_item(label(b), start + 1 + bi, parent=parent)
    w.compress_identical_objects(remove_identicals=True, remove_unreferenced=True)
    with open(path, 'wb') as f:
        w.write(f)
    shrink(path)
    return os.path.getsize(path)


full = os.path.join(out, name + '.pdf')
print(f'{name}.pdf: {build_pdf(full, list(enumerate(plan))) / 1e6:.1f} MB')
os.makedirs(os.path.join(out, 'sections'), exist_ok=True)
for si, sec in enumerate(plan):
    p = os.path.join(out, 'sections', f'{si + 1:02d}-{slug(sec["title"])}.pdf')
    build_pdf(p, [(si, sec)])

# ---------------------------------------------------------------- The offline viewer

site = os.path.join(out, 'offline')
shutil.rmtree(site, ignore_errors=True)
for d in ('live/project', 'live/_blob', 'thumbs'):
    os.makedirs(os.path.join(site, d))
used = set()
for sec in plan:
    for b in sec['boards']:
        s = open(os.path.join(proj, b['file'])).read()
        ids = set(re.findall(r'/_blob/([0-9a-f]{32})', s))
        for i in ids:
            src = next(os.path.join(blobs, f) for f in os.listdir(blobs) if f.startswith(i + '.'))
            ext = os.path.splitext(src)[1]
            s = s.replace(f'/_blob/{i}', f'../_blob/{i}{ext}')
            if i not in used:
                shutil.copy(os.path.realpath(src), os.path.join(site, 'live', '_blob', i + ext))
                used.add(i)
        open(os.path.join(site, 'live', 'project', b['file']), 'w').write(s)
        im = Image.open(os.path.join(out, 'jpg', b['file'].replace('.dc.html', '.jpg'))).convert('RGB')
        im.thumbnail((720, 1400))
        im.save(os.path.join(site, 'thumbs', b['file'].replace('.dc.html', '.jpg')), quality=80, optimize=True)
shutil.copy(os.path.join(proj, 'support.js'), os.path.join(site, 'live', 'project', 'support.js'))
shutil.copy(full, os.path.join(site, name + '.pdf'))

nav = ''.join(f'<a href="#s{i + 1}"><span>{i + 1}</span>{html.escape(sec["title"])}</a>' for i, sec in enumerate(plan))
secs = ''
pg = 1  # each section starts with its divider page
for i, sec in enumerate(plan):
    cards = ''
    for b in sec['boards']:
        pg += 1
        cards += (f'<div class="card"><a class="open" href="{name}.pdf#page={pg}" target="_blank" rel="noopener">'
                  f'<span class="thumb" style="aspect-ratio: {b["w"]} / {b["h"]}"><img loading="lazy" src="thumbs/{b["file"].replace(".dc.html", ".jpg")}" alt=""></span>'
                  f'<span class="name">{html.escape(label(b))}</span></a>'
                  f'<span class="meta"><span>{b["w"]} by {b["h"]}, page {pg}</span><a href="live/project/{b["file"]}" target="_blank" rel="noopener">Live</a></span></div>')
    pg += 1
    secs += f'<section id="s{i + 1}"><h2><span>{i + 1}</span>{html.escape(sec["title"])}</h2><div class="grid">{cards}</div></section>'
count = sum(len(s['boards']) for s in plan)
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{{--evg:#0F4A36;--lime:#D8F36A;--ink:#101814;--sec:#3F4B45;--mist:#EEF3F0;--line:#DCE4DF}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Geist,system-ui,sans-serif;color:var(--ink);background:var(--mist)}}
header{{background:var(--evg);color:#fff;padding:40px 32px 32px}}header h1{{margin:0 0 8px;font-size:40px;letter-spacing:-.03em;font-weight:600}}
header p{{margin:0;color:#BFDCCF;font-size:16px;line-height:1.5;max-width:860px}}
.wrap{{display:grid;grid-template-columns:300px 1fr;gap:0}}
nav{{position:sticky;top:0;align-self:start;height:100vh;overflow:auto;padding:20px 12px;border-right:1px solid var(--line);background:#fff}}
nav a{{display:flex;gap:10px;padding:8px 10px;border-radius:8px;color:var(--ink);text-decoration:none;font-size:14px;line-height:1.35}}
nav a:hover,nav a:focus-visible{{background:var(--mist)}}nav a span{{color:var(--evg);font-weight:600;min-width:20px}}
main{{padding:24px 32px 80px;min-width:0}}section{{padding-top:20px}}
h2{{display:flex;gap:12px;font-size:24px;letter-spacing:-.02em;font-weight:600;margin:12px 0 18px}}h2 span{{color:var(--evg)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:18px;align-items:start}}
.card{{display:flex;flex-direction:column;gap:6px}}.open{{display:flex;flex-direction:column;gap:6px;color:var(--ink);text-decoration:none}}
.meta{{display:flex;justify-content:space-between;gap:8px;font-size:12px;color:var(--sec)}}.meta a{{color:var(--evg);font-weight:600}}
.thumb{{display:block;border-radius:10px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px rgba(16,24,20,.08),0 6px 18px rgba(16,24,20,.08)}}
.thumb img{{display:block;width:100%;height:100%;object-fit:cover}}
.open:hover .thumb,.open:focus-visible .thumb{{box-shadow:0 0 0 3px var(--evg)}}
.name{{font-size:14px;font-weight:600;line-height:1.3}}
a:focus-visible{{outline:2px solid var(--evg);outline-offset:3px}}
@media (max-width:800px){{.wrap{{grid-template-columns:1fr}}nav{{position:static;height:auto;border-right:0}}main{{padding:16px}}}}
</style></head><body>
<header><h1>{html.escape(title)}</h1><p>{count} boards in {len(plan)} sections, exported from the AWO Direction Explorations canvas. Click a board to open its page in the PDF. To use a board live (tabs, switches, links between boards), open a terminal in this folder, run <code>python3 -m http.server</code>, visit <code>http://localhost:8000</code> and click Live. All content is sample content.</p></header>
<div class="wrap"><nav aria-label="Sections">{nav}</nav><main>{secs}</main></div>
</body></html>'''
open(os.path.join(site, 'index.html'), 'w').write(page)
z = os.path.join(out, name + '-offline.zip')
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, _dirs, files in os.walk(site):
        for f in files:
            p = os.path.join(root, f)
            zf.write(p, os.path.join(name, os.path.relpath(p, site)))
print(f'{name}-offline.zip: {os.path.getsize(z) / 1e6:.1f} MB ({count} boards, {len(used)} images)')
