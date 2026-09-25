# Round 6 shared pieces. Builds on Round 5's language (design/round-5/lib.py) at Volume 1 (Clean).
# Holes are written as [[ name ]] and become {{ name }} in the output, so the HTML stays readable.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'round-5'))
from lib import *  # noqa: E402,F401,F403  (tokens, icons, pool, moon, stones, ola)

IMG.update({
    'adaeze': '/_blob/9c152c6cbc7132bf3de3951867a33d31',
    'wanjiru_stall': '/_blob/46d15728a12cc0a992dfc48cf3f11362',
    'amara_coat': '/_blob/71e35f317a0dafb009047be52f43856e',
    'thandi_window': '/_blob/8a4fe9524d9d7c8777bfeef767169841',
    'grace_dancing': '/_blob/1a37ae97aad3499ce9a14ff441f771d5',
    'naledi_cafe': '/_blob/3516f95638e577416b41d1104229fc6d',
})

PAGES = {
    'Home': 'R6-Home.dc.html', 'Learn': 'R6-Learn.dc.html', 'Vault': 'R6-Vault.dc.html',
    'Community': 'R6-Community.dc.html', 'Me': 'R6-Me.dc.html',
}

EXTRA_CSS = """
a{color:inherit;text-decoration:none}
a:focus-visible,input:focus-visible,textarea:focus-visible{outline:2px solid #0F4A36;outline-offset:3px}
.dk a:focus-visible,.dk input:focus-visible{outline-color:#86E3C4}
input{font:inherit;color:inherit}
.lbl{font-size:13px;font-weight:600}
.cap{font-size:13px;line-height:1.4}
.ring{position:absolute;inset:-5px;border-radius:999px;border:2.5px solid currentColor}
.tile{border-radius:24px;padding:16px;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;overflow:hidden;position:relative}
@keyframes fill{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes wax{from{clip-path:inset(0 0 0 100%)}to{clip-path:inset(0 0 0 0)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes stepIn{from{opacity:0;transform:translate(-18px,18px) scale(.8)}to{opacity:1;transform:none}}
@keyframes sheetUp{from{transform:translateY(24px);opacity:0}to{transform:none;opacity:1}}
@keyframes storyIn{from{opacity:0;transform:scale(.96)}to{opacity:1;transform:none}}
@keyframes pop{0%{transform:scale(.6)}60%{transform:scale(1.12)}100%{transform:scale(1)}}
@keyframes arcIn{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}
"""


def holes(html):
    return html.replace('[[', '{{').replace(']]', '}}')


def tabbar6(active, dark=False):
    bg = DEEP if dark else '#FFFFFF'
    line = NLINE if dark else '#E1E8E4'
    idle = NMUTED if dark else MUTED
    out = [f'<nav aria-label="Main" class="tab" style="background: {bg}; border-top: 1px solid {line}; color: {idle}">']
    for name, ic in AREAS:
        if name == active:
            pb, fg, lc = ACTIVE[name]
            out.append(f'<a href="{PAGES[name]}" class="ti" aria-current="page" style="color: {lc}; font-weight: 600"><span class="tp" style="background: {pb}; color: {fg}">{icon(ic)}</span>{name}</a>')
        else:
            out.append(f'<a href="{PAGES[name]}" class="ti"><span class="tp">{icon(ic)}</span>{name}</a>')
    out.append('</nav>')
    return ''.join(out)


def sample_chip(col=MUTED, text='Sample'):
    return f'<span class="chip" style="border: 1px dashed {col}; color: {col}">{text}</span>'


def phone(title, body, logic, h=844, bg=MIST, dark=False, defs=''):
    """One artboard that is one phone screen, 390 wide."""
    fg = MOON if dark else INK
    cls = ' class="dk"' if dark else ''
    body = holes(body)
    return (f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{BASE_CSS}{EXTRA_CSS}
body{{background:{bg}}}
</style>
</helmet>
<div{cls} style="position: relative; width: 390px; height: {h}px; overflow: hidden; background: {bg}; color: {fg}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif">
  <svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs>{defs}</defs></svg>
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":{h}}}}}'>
{logic}
</script>
</body>
</html>
''')


def static_logic():
    return 'class Component extends DCLogic {\n  renderVals() { return {}; }\n}'


def arc(size, value, track, fill, sw=12, span=270):
    """A single readiness arc (not rings): value 0-100 over a 270-degree track."""
    import math
    r = (size - sw) / 2
    c = size / 2
    start = 90 + (360 - span) / 2

    def pt(a):
        rad = math.radians(a)
        return c + r * math.cos(rad), c + r * math.sin(rad)

    def path(a0, a1):
        x0, y0 = pt(a0)
        x1, y1 = pt(a1)
        large = 1 if (a1 - a0) > 180 else 0
        return f'M{x0:.1f} {y0:.1f}A{r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f}'
    end = start + span * value / 100
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true" style="display: block">'
            f'<path d="{path(start, start + span)}" fill="none" stroke="{track}" stroke-width="{sw}" stroke-linecap="round"></path>'
            f'<path d="{path(start, end)}" fill="none" stroke="{fill}" stroke-width="{sw}" stroke-linecap="round" pathLength="100" '
            f'style="stroke-dasharray: 100; stroke-dashoffset: 0; animation: arcIn 1s cubic-bezier(.2,.8,.2,1) .2s both"></path></svg>')



def write(path, html):
    with open(path, 'w') as f:
        f.write(html)
    print('wrote', os.path.basename(path), len(html))
