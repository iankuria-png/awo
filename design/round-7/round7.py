"""Round 7: the Round 6 screens with three changes, applied as a transform so both rounds stay comparable.

1. Type: Geist does everything, as on Round 1's Oasis board (display 600, tight tracking). No condensed face.
2. A handwritten face only for a few special moments (Kalam by default; switch in each board's Tweaks).
3. Corners: three radii and a circle (6, 10, 14). Bars get square ends.

Usage: python3 round7.py <project dir>
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))

import areas  # noqa: E402
import home  # noqa: E402
import kit  # noqa: E402
import onboarding  # noqa: E402
import areas7  # noqa: E402  (Vault, Me, Community redesigned natively in Round 7 style)
import screens7  # noqa: E402  (screens Round 6 never had, from Round 3's E set)
import kit7  # noqa: E402  (controls, data and feedback)
import brand7  # noqa: E402  (brand, icons, motion, foundations)
import marketing7  # noqa: E402  (store, listing, feature graphic, icon, hero, ads)
import auth7  # noqa: E402  (accounts and the first loop)
import loop7  # noqa: E402  (the loop, deeper)
import biz7  # noqa: E402  (entrepreneurs)
from screens7 import mark  # noqa: E402
from lib6 import EVG, LIME, MOON, BLUSH_INK, write  # noqa: E402

HANDS = ['Kalam', 'Nanum Pen Script', 'Delicious Handrawn']
HAND_LINK = ('<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&amp;family=Nanum+Pen+Script'
             '&amp;family=Delicious+Handrawn&amp;display=swap" rel="stylesheet">')
HF = "font-family: '{{ handFont }}', cursive"

R7_CSS = """
.d{font-family:'Geist',ui-sans-serif,system-ui,sans-serif;font-weight:600;font-stretch:100%;letter-spacing:-0.045em;line-height:.95}
.pill{border-radius:10px}
.chip{border-radius:6px}
.tp{border-radius:8px}
.tile{border-radius:14px}
.rp{border-radius:inherit}
.card{border-radius:14px}
.hand{font-weight:400;letter-spacing:0;line-height:1.15;font-size-adjust:.5}
"""

DISPLAY_SCALE = 0.86


# ---------------------------------------------------------------- the special moments

def moments(name, html):
    """Put the handwritten face on the few moments that earn it. Each replacement must match once."""
    def sub(old, new):
        nonlocal html
        assert old in html, f'{name}: moment anchor not found: {old[:70]}'
        html = html.replace(old, new, 1)

    if name == 'R7-Welcome':
        # A note and an arrow pointing at the first stepping stone.
        sub('<div style="position: absolute; left: 0; right: 0; top: 60px"><svg width="390" height="420"',
            f'<div style="position: absolute; left: 0; right: 0; top: 60px">'
            f'<span class="hand" style="position: absolute; left: 22px; top: 222px; font-size: 30px; color: {LIME}; transform: rotate(-7deg); {HF}; animation: rise .6s cubic-bezier(.2,.8,.2,1) .9s both">start here</span>'
            f'<svg aria-hidden="true" width="70" height="70" viewBox="0 0 70 70" style="position: absolute; left: 36px; top: 256px; animation: rise .6s cubic-bezier(.2,.8,.2,1) 1.1s both"><path d="M14 4c-6 18 0 34 22 44" fill="none" stroke="{LIME}" stroke-width="2.6" stroke-linecap="round"></path><path d="M28 50l9-1-3-9" fill="none" stroke="{LIME}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
            f'<svg width="390" height="420"')
    elif name == 'R7-Starter':
        sub('<span class="lbl">Your first profile</span>',
            f'<span class="hand" style="font-size: 30px; color: {EVG}; {HF}">Here\'s where you start.</span>')
        sub('<a href="R6-Me.dc.html" class="pill"', '<a href="R7-Reveal.dc.html" class="pill"')
    elif name == 'R7-Home':
        # Her circle's wins are their own words.
        for s in home.STORIES:
            sub(f'<p class="d" style="font-size: 36px; line-height: .95">{s["text"]}</p>',
                f'<p class="hand" style="font-size: 38px; {HF}">{s["text"]}</p>')
        # Finishing the week's step earns a short note.
        sub('<span style="flex-grow: 1">{{ amountLine }}</span>',
            '<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px">{{ amountLine }}'
            '<sc-if value="{{ chosen }}" hint-placeholder-val="{{ false }}">'
            f'<span class="hand" style="font-size: 24px; color: {EVG}; {HF}; animation: rise .6s cubic-bezier(.2,.8,.2,1) .2s both">Done for this week. Nicely done!</span>'
            '</sc-if></span>')
    elif name == 'R7-Learn':
        sub('<p style="font-size: 14px; color: #9AA39F; padding: 0 4px">You showed up three evenings this week.</p>',
            f'<p class="hand" style="font-size: 24px; color: {MOON}; padding: 0 4px; {HF}">You showed up three evenings this week.</p>')
    elif name == 'R7-Widgets':
        sub(f'<span class="d" style="font-size: 16px; color: {LIME}">awo</span>', mark(24, '#FFFFFF', LIME))
    # Vault, Me and Community are written natively (areas7.py) and carry their own moments.
    # Me and Ask stay typeset: results and AI answers are never handwritten.
    return html


# ---------------------------------------------------------------- corners

def radius_value(v):
    """Map one radius to the restricted set: 6, 10, 14 (circles are handled by the caller)."""
    if v >= 20:
        return 14
    if v >= 11:
        return 10
    if v > 0:
        return 6
    return 0


def restyle_radius(style):
    m = re.search(r'border-radius:\s*([^;"]+)', style)
    if not m:
        return style
    raw = m.group(1).strip()
    if '%' in raw:
        return style
    vals = [int(float(x[:-2])) for x in raw.split() if x.endswith('px')]
    if not vals:
        return style
    w = re.search(r'(?:^|;)\s*width:\s*(\d+)px', style)
    h = re.search(r'(?:^|;)\s*height:\s*(\d+)px', style)
    wv, hv = (int(w.group(1)) if w else None), (int(h.group(1)) if h else None)
    if any(v >= 99 for v in vals):
        if 'inset:' in style or (wv and hv and wv == hv):
            return style                                   # a circle or a ring: keep it round
        if hv is not None and hv <= 12:
            new = '2px'                                    # bars and tracks: square ends
        elif hv is not None and hv <= 32:
            new = '6px'                                    # chips and tags
        else:
            new = '10px'                                   # buttons, inputs, pills
    else:
        new = ' '.join(f'{radius_value(v)}px' for v in vals)
    return style[:m.start(1)] + new + style[m.end(1):]


def restyle_display(tag):
    fs = re.search(r'font-size:\s*(\d+)px', tag)
    if not fs:
        return tag
    n = max(14, round(int(fs.group(1)) * DISPLAY_SCALE))
    return tag[:fs.start(1)] + str(n) + tag[fs.end(1):]


def transform(name, html, native=False):
    if not native:
        html = moments(name, html)
    html = re.sub(r'href="R6-', 'href="R7-', html)
    head, rest = html.split('</helmet>', 1)
    head = head.replace('</style>', R7_CSS + '</style>\n' + HAND_LINK, 1)
    body, tail = rest.split('</x-dc>', 1)
    if not native:
        body = re.sub(r'style="([^"]*)"', lambda m: 'style="' + restyle_radius(m.group(1)) + '"', body)
        body = re.sub(r'<[a-z0-9]+ [^>]*class="d"[^>]*>', lambda m: restyle_display(m.group(0)), body)
    # The handwriting tweak: every board gets the same lever.
    tail = tail.replace('\n  renderVals()',
                        "\n  renderVals() {\n    const v = this.baseVals();\n    v.handFont = this.props.hand ?? 'Kalam';\n    return v;\n  }\n  baseVals()", 1)
    assert 'baseVals' in tail, f'{name}: logic not patched'
    prop = '{"hand":{"editor":"enum","options":' + str(HANDS).replace("'", '"') + ',"default":"Kalam","section":"Round 7"},"$preview"'
    tail = tail.replace('data-props=\'{"$preview"', "data-props='" + prop, 1)
    return head + '</helmet>' + body + '</x-dc>' + tail


BOARDS = [
    ('R7-Welcome', onboarding.welcome), ('R7-Starter', onboarding.starter), ('R7-Home', home.build),
    ('R7-Learn', areas.learn), ('R7-Ask', areas.ask), ('R7-Vault', areas7.vault), ('R7-Community', areas7.community),
    ('R7-Me', areas7.me), ('R7-Widgets', kit.widgets),
] + screens7.BOARDS + kit7.BOARDS + brand7.BOARDS + marketing7.BOARDS + auth7.BOARDS + loop7.BOARDS + biz7.BOARDS

if __name__ == '__main__':
    out = sys.argv[1]
    for name, fn in BOARDS:
        write(os.path.join(out, name + '.dc.html'), transform(name, fn(), native=fn.__module__ in ('areas7', 'screens7', 'kit7', 'brand7', 'marketing7', 'auth7', 'loop7', 'biz7')))
