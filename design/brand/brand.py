"""The Brand System page: AWO's suggested Visual Brand System Brief (Instagram and LinkedIn), laid out as boards in the
brief's own system, one board per section with its key elements and worked examples.

The brief (AWO_Brand_System_Brief_1.docx, "Deliverable 4 of 4" of the social content strategy, shared by Ian on
1 October 2026) is summarised in docs/00-discovery/16-brand-system-brief.md, with where it differs from the app's
design language (Q-49). Everything here is sample content; the wordmark is a stand-in (Q-25).

Usage:
  python3 design/brand/brand.py build <project dir>
  python3 design/brand/brand.py layout <live canvas.json> <out canvas.json> <project dir>
"""
import json
import os
import re
import sys

PAGE, PAGE_NAME = 'brand', 'Brand system (suggested)'
STONE, PLUM, TERRA, SAGE, BLUSH, WGREY, BODY, WHITE = '#F5EBE3', '#4A2D4E', '#B85C38', '#8FA586', '#D4A8A0', '#C8BFB0', '#2A1F2E', '#FFFFFF'
SERIF = "font-family: 'Playfair Display', Georgia, serif"
SANS = "font-family: 'Montserrat', Arial, sans-serif"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..800;1,400..600'
         '&amp;family=Montserrat:wght@400;500;600;700&amp;display=swap" rel="stylesheet">')
IMG = {'naledi_cafe': '/_blob/3516f95638e577416b41d1104229fc6d', 'wanjiru_stall': '/_blob/46d15728a12cc0a992dfc48cf3f11362',
       'amara_coat': '/_blob/71e35f317a0dafb009047be52f43856e', 'thandi_window': '/_blob/8a4fe9524d9d7c8777bfeef767169841',
       'adaeze': '/_blob/9c152c6cbc7132bf3de3951867a33d31', 'naledi_table': '/_blob/6c931acfd633d8490000e4f4faa1b8a6'}
CSS = f"""
body{{margin:0;{SANS};color:{BODY}}}
h1,h2,h3,p{{margin:0}}
button{{font:inherit;cursor:pointer;border:0;background:none;color:inherit;padding:0;margin:0}}
button:focus-visible{{outline:2px solid {PLUM};outline-offset:3px}}
.ser{{{SERIF};font-weight:500;letter-spacing:-0.01em}}
@keyframes fadeRise{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
@keyframes drawOn{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes drift{{from{{transform:scale(1.04) translateX(-8px)}}to{{transform:scale(1.08) translateX(8px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
"""


def js(o):
    return json.dumps(o, ensure_ascii=False)


def holes(s):
    return s.replace('[[ ', '{{ ').replace(' ]]', ' }}')


def static_logic(extra=''):
    return 'class Component extends DCLogic {\n  renderVals() { return { %s }; }\n}' % extra


def page_html(title, w, h, bg, inner, logic=None):
    return f'''<!doctype html>
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
<style>{CSS}
body{{background:{bg}}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {bg}; color: {BODY}; {SANS}">
{holes(inner)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
{logic or static_logic()}
</script>
</body>
</html>
'''


# ---------------------------------------------------------------- Shared pieces

def rule(w=64, col=TERRA, h=3):
    return f'<span aria-hidden="true" style="display: block; width: {w}px; height: {h}px; background: {col}"></span>'


def wordmark(size, col, accent=TERRA):
    """A stand-in wordmark: the brief sets clear space by the height of the A but doesn't include the artwork (Q-25)."""
    return (f'<span role="img" aria-label="AWO" style="display: inline-flex; align-items: center; gap: {round(size * .32)}px">'
            f'<span aria-hidden="true" style="width: {max(2, round(size * .07))}px; height: {round(size * .82)}px; background: {accent}"></span>'
            f'<span style="{SERIF}; font-weight: 600; font-size: {size}px; line-height: 1; letter-spacing: .06em; color: {col}">AWO</span></span>')


def keys(items, title='Key elements from the brief'):
    li = ''.join(f'<li style="display: flex; gap: 14px; font-size: 18px; line-height: 1.5; color: {BODY}"><span aria-hidden="true" style="flex-shrink: 0; width: 18px; height: 2px; margin-top: 13px; background: {TERRA}"></span><span>{t}</span></li>' for t in items)
    return (f'<section style="background: {WHITE}; padding: 28px 32px; display: flex; flex-direction: column; gap: 14px">'
            f'<span style="font-size: 16px; font-weight: 600; color: {PLUM}">{title}</span><ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px">{li}</ul></section>')


def board(num, title_text, intro, key_items, content, h, logic=None, w=1920, bg=STONE):
    head = f'''<div style="padding: 72px 80px 0; display: grid; grid-template-columns: minmax(0, 1fr) 640px; gap: 80px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 22px">
    <span style="font-size: 18px; font-weight: 600; color: {TERRA}">{num}</span>
    <h1 class="ser" style="font-size: 72px; line-height: 1.04; color: {PLUM}">{title_text}</h1>
    {rule(72)}
    <p style="font-size: 21px; line-height: 1.6; color: {BODY}; max-width: 880px">{intro}</p>
  </div>
  {keys(key_items)}
</div>
<div style="padding: 56px 80px 72px">{content}</div>'''
    return page_html(f'{num}. {title_text}' if num[0].isdigit() else title_text, w, h, bg, head, logic)


def label(t, col=PLUM):
    return f'<span style="font-size: 15px; font-weight: 600; color: {col}">{t}</span>'


def scaled(inner, w, h, sc, shadow=True):
    sh = 'box-shadow: 0 1px 2px rgba(42,31,46,.12), 0 18px 40px rgba(42,31,46,.12);' if shadow else ''
    return (f'<div style="width: {w * sc:.0f}px; height: {h * sc:.0f}px; overflow: hidden; flex-shrink: 0; {sh}">'
            f'<div style="width: {w}px; height: {h}px; transform: scale({sc}); transform-origin: 0 0">{inner}</div></div>')


def frame(bg, inner, w=1080, h=1350, fg=BODY):
    return f'<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {bg}; color: {fg}; {SANS}">{inner}</div>'


def slide_no(n, total, col):
    return f'<span style="position: absolute; right: 90px; top: 84px; font-size: 26px; font-weight: 600; letter-spacing: .04em; color: {col}">{n:02d} / {total:02d}</span>'


def foot_mark(col, accent=TERRA, left='90px', bottom='80px'):
    return f'<span style="position: absolute; left: {left}; bottom: {bottom}">{wordmark(30, col, accent)}</span>'


def sample_note(col, t='Sample figures, for layout only'):
    return f'<span style="font-size: 22px; color: {col}">{t}</span>'


# ---------------------------------------------------------------- Cover

def cover():
    meta = [('For', 'The designer and content producer'), ('Covers', 'Palette, type, templates, grid logic, imagery, specs'),
            ('Principle', 'An intelligence brand, not a money-tips account'), ('Pairs with', 'The content calendar, content bank and community playbook'),
            ('Prepared for', 'AWO Holdings (Pty) Ltd, phase 1 to 2, before licensing')]
    rows = ''.join(f'<div style="display: grid; grid-template-columns: 200px 1fr; gap: 24px; padding: 18px 0; border-top: 1px solid rgba(143,165,134,.45)">'
                   f'<span style="font-size: 20px; font-weight: 700; color: {SAGE}">{k}</span><span style="font-size: 20px; line-height: 1.45; color: {STONE}">{v}</span></div>' for k, v in meta)
    inner = f'''<div style="position: absolute; left: 120px; top: 110px">{wordmark(54, STONE)}</div>
<div style="position: absolute; left: 120px; top: 300px; width: 900px; display: flex; flex-direction: column; gap: 34px">
  <h1 class="ser" style="font-size: 132px; line-height: .98; color: {STONE}">Visual brand<br>system</h1>
  <p style="font-size: 28px; line-height: 1.45; color: {STONE}">Instagram and LinkedIn: design standards for the feed. Palette: the Cultural Archive.</p>
  <p class="ser" style="font-style: italic; font-size: 40px; line-height: 1.3; color: {STONE}"><span style="box-shadow: inset 0 -4px 0 {TERRA}">An intelligence brand,</span> not a money-tips account.</p>
</div>
<div style="position: absolute; right: 120px; top: 300px; width: 600px">{rows}</div>
<p style="position: absolute; left: 120px; right: 120px; bottom: 80px; font-size: 18px; line-height: 1.5; color: {STONE}">AWO's suggested brand guide (social content strategy, deliverable 4 of 4), shared 1 October 2026. Laid out from the brief, one board per section. Sample content throughout; the wordmark is a stand-in.</p>'''
    return page_html('Visual brand system: cover', 1920, 1080, PLUM, inner)


# ---------------------------------------------------------------- 1. The bar to clear

def bar():
    feel = ['Sophisticated', 'Structured', 'Intriguing', 'Credible', 'Empowering', 'Quietly premium']
    never = ['Loud', 'Hype-driven', 'Emoji-saturated', 'Templated-default', '"Money-girlie"', 'Cheap']
    col = lambda words, c, sz: ''.join(f'<span class="ser" style="font-size: {sz}px; line-height: 1.25; color: {c}">{w}</span>' for w in words)
    good = frame(STONE, f'''<span style="position: absolute; left: 90px; top: 90px; font-size: 26px; font-weight: 600; color: {PLUM}">Remittances</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 330px; font-size: 104px; line-height: 1.08; color: {PLUM}">The fee is the part you <span style="color: {TERRA}">see</span>.</h2>
      <p style="position: absolute; left: 90px; right: 160px; top: 760px; font-size: 32px; line-height: 1.5; color: {BODY}">The rest hides in the exchange rate. Compare what arrives, not what you pay.</p>{foot_mark(PLUM)}''')
    loud = frame('linear-gradient(135deg,#FF4FA3,#FFB800)', f'''<span style="position: absolute; left: 70px; top: 80px; font-size: 64px">💸💸🔥</span>
      <h2 style="position: absolute; left: 70px; right: 70px; top: 300px; font-size: 120px; font-weight: 800; line-height: 1; color: #FFFFFF; text-transform: uppercase; text-shadow: 0 6px 0 #7A1FA2">Stop being BROKE!!</h2>
      <p style="position: absolute; left: 70px; right: 70px; top: 820px; font-size: 44px; font-weight: 700; color: #FFFFFF">5 money hacks rich girls know 👀✨</p>''', fg=WHITE)
    content = f'''<div style="display: grid; grid-template-columns: 1fr 1fr 1.25fr; gap: 56px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 14px">{label('It should feel')}<div style="display: flex; flex-direction: column">{col(feel, PLUM, 48)}</div></div>
  <div style="display: flex; flex-direction: column; gap: 14px">{label('It must never feel')}<div style="display: flex; flex-direction: column">{col(never, '#8A7F86', 48)}</div></div>
  <div style="display: flex; flex-direction: column; gap: 16px">{label('The test: next to a finance publication, or a budgeting influencer?')}
    <div style="display: flex; gap: 24px">
      <div style="display: flex; flex-direction: column; gap: 10px">{scaled(good, 1080, 1350, .3)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">On brand: restraint</span></div>
      <div style="display: flex; flex-direction: column; gap: 10px">{scaled(loud, 1080, 1350, .3)}<span style="font-size: 15px; font-weight: 600; color: {TERRA}">Off brand, even if it would perform</span></div>
    </div></div>
</div>
<div style="margin-top: 56px; background: {PLUM}; padding: 44px 56px; display: flex; gap: 40px; align-items: center">
  <span class="ser" style="font-size: 44px; color: {STONE}; flex-shrink: 0">The discipline is the brand.</span>
  <span style="width: 2px; align-self: stretch; background: {TERRA}"></span>
  <span style="font-size: 20px; line-height: 1.6; color: {STONE}">If a piece drifts into bright, busy, hype territory, it is off brand even if it would perform. AWO wins on restraint: a single slide should be recognisable as AWO before anyone reads the handle.</span>
</div>'''
    return board('1', 'The bar to clear', 'Everything AWO publishes should look at home next to a sophisticated finance publication, not next to a budgeting influencer. That single test settles most design decisions.',
                 ['Composed, confident, feminine without being soft, data-forward without being cold.', 'Six words it should feel, six it must never feel.',
                  'Restraint wins, even over reach: off brand is off brand if it would perform.', 'Recognisable as AWO before the handle is read.'], content, 1180)


# ---------------------------------------------------------------- 2. Colour

PALETTE = [('Warm stone', STONE, 'The dominant ground. Holds plum and terracotta without competing.', PLUM, 'Ground'),
           ('Deep plum', PLUM, 'Structural anchor: the dark ground, headers and framing.', STONE, 'Anchor'),
           ('Terracotta', TERRA, 'Signature accent: a key word, the CTA, the rule. One per view.', WHITE, 'Accent'),
           ('Dusty sage', SAGE, 'Secondary labels and chrome on plum; fine rules; the Silver tier.', BODY, 'Quiet'),
           ('Blush', BLUSH, 'Community layer only, always with bold type.', PLUM, 'Community'),
           ('Warm grey', WGREY, 'Hairline dividers within cards. Never text.', PLUM, 'Hairline'),
           ('Body text', BODY, 'Plum-tinted near-dark. Body copy on light grounds only.', STONE, 'Text')]


def lum(h):
    r, g, b = [int(h.lstrip('#')[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + .05) / (lb + .05)


def colour():
    sw = ''.join(f'''<div style="display: flex; flex-direction: column; background: {WHITE}">
        <div style="height: 210px; background: {hx}; padding: 22px; display: flex; flex-direction: column; justify-content: space-between; {"box-shadow: inset 0 0 0 1px " + WGREY + ";" if hx == STONE else ""}">
          <span style="font-size: 15px; font-weight: 600; color: {tc}">{role}</span><span class="ser" style="font-size: 30px; line-height: 1.1; color: {tc}">{n}</span></div>
        <div style="padding: 16px 18px 20px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 17px; font-weight: 600; color: {PLUM}; letter-spacing: .03em">{hx}</span><span style="font-size: 15px; line-height: 1.5; color: {BODY}">{job}</span></div></div>'''
                 for n, hx, job, tc, role in PALETTE)
    share = [(STONE, 52, 'Warm stone'), (PLUM, 28, 'Deep plum'), (BODY, 8, 'Text'), (SAGE, 5, 'Sage'), (TERRA, 3, 'Terracotta'), (WGREY, 2, 'Grey'), (BLUSH, 2, 'Blush')]
    bar = ''.join(f'<span title="{n}" style="flex: {p} 1 0; background: {c}; {"box-shadow: inset 0 0 0 1px " + WGREY if c == STONE else ""}"></span>' for c, p, n in share)
    pairs = [(BODY, STONE, 'Body text on warm stone'), (PLUM, STONE, 'Deep plum on warm stone'), (STONE, PLUM, 'Warm stone on deep plum'),
             (PLUM, BLUSH, 'Deep plum on blush'), (TERRA, WHITE, 'Terracotta on white'), (TERRA, STONE, 'Terracotta on warm stone'),
             (SAGE, PLUM, 'Dusty sage on deep plum'), (TERRA, PLUM, 'Terracotta on deep plum'), (SAGE, STONE, 'Dusty sage on warm stone')]

    def verdict(r):
        if r >= 4.5:
            return 'Any size', PLUM
        if r >= 3:
            return 'Large text only (24 px, or 19 px bold)', TERRA
        return 'Not for text: a rule or underline', BODY
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 96px 1fr 90px 1.2fr; gap: 20px; align-items: center; padding: 12px 0; {"border-top: 1px solid " + WGREY + ";" if i else ""}">
          <span style="height: 56px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center; {SERIF}; font-size: 28px; {"box-shadow: inset 0 0 0 1px " + WGREY + ";" if bg in (STONE, WHITE) else ""}">Aa</span>
          <span style="font-size: 17px; color: {BODY}">{n}</span><span style="font-size: 18px; font-weight: 600; color: {PLUM}; font-variant-numeric: tabular-nums">{contrast(fg, bg):.2f}:1</span>
          <span style="font-size: 16px; font-weight: 600; color: {verdict(contrast(fg, bg))[1]}">{verdict(contrast(fg, bg))[0]}</span></div>''' for i, (fg, bg, n) in enumerate(pairs))
    rules = [('Two grounds per piece', 'Warm stone dominant, deep plum the anchor. Alternate for rhythm.', f'<span style="display: flex; height: 100%"><span style="flex: 1; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}"></span><span style="flex: 1; background: {PLUM}"></span><span style="flex: 1; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}"></span></span>'),
             ('One terracotta focal point', 'A key word, the CTA or a rule. Detail reads premium; blocks read heavy.', f'<span style="display: flex; height: 100%; align-items: center; justify-content: center; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}; {SERIF}; font-size: 28px; color: {PLUM}">Read the <span style="color: {TERRA}; margin-left: 8px">rate</span></span>'),
             ('On plum, terracotta is a line', 'Too low in contrast for type there, so it becomes a rule or underline.', f'<span style="display: flex; height: 100%; flex-direction: column; align-items: center; justify-content: center; gap: 10px; background: {PLUM}; {SERIF}; font-size: 28px; color: {STONE}">Quiet confidence{rule(90)}</span>'),
             ('Sage stays quiet', 'Labels and chrome on plum, fine rules. Never the loudest thing.', f'<span style="display: flex; height: 100%; flex-direction: column; justify-content: center; gap: 8px; padding: 0 22px; background: {PLUM}"><span style="font-size: 19px; font-weight: 600; color: {SAGE}">Data brief</span><span style="height: 1px; background: {SAGE}"></span><span class="ser" style="font-size: 24px; color: {STONE}">Where the cost hides</span></span>'),
             ('Blush is community only', 'Never in educational or data content.', f'<span style="display: flex; height: 100%; align-items: center; justify-content: center; background: {BLUSH}; font-size: 24px; font-weight: 700; color: {PLUM}">Your circle asked</span>'),
             ('No new hues, no gradients', 'The restraint is the differentiator.', f'<span style="display: flex; height: 100%; gap: 6px; align-items: center; justify-content: center; background: {WHITE}; box-shadow: inset 0 0 0 1px {WGREY}">' + ''.join(f'<span style="width: 44px; height: 44px; background: {c}"></span>' for c in [STONE, PLUM, TERRA, SAGE]) + '</span>')]
    rl = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px"><div style="height: 120px">{v}</div><span style="font-size: 17px; font-weight: 600; color: {PLUM}">{t}</span><span style="font-size: 15px; line-height: 1.5; color: {BODY}">{d}</span></div>' for t, d, v in rules)
    content = f'''<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 16px">{sw}</div>
<div style="margin-top: 28px; display: flex; flex-direction: column; gap: 10px">{label('How much of each, roughly: our reading of "dominant", "anchor" and "accent"')}<div style="display: flex; height: 36px">{bar}</div></div>
<div style="margin-top: 48px; display: grid; grid-template-columns: 1.15fr 1fr; gap: 56px; align-items: start">
  <section style="background: {WHITE}; padding: 26px 30px; display: flex; flex-direction: column; gap: 8px">{label('Contrast, checked against WCAG 2.2 AA')}{rows}
    <span style="margin-top: 8px; font-size: 15px; line-height: 1.5; color: {BODY}">Two pairs the brief uses need care: terracotta key words on warm stone must be large, and sage labels on plum must be 24 px or 19 px bold. The CTA line is safest in terracotta on white, or large.</span></section>
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px 24px">{rl}</div>
</div>'''
    return board('2', 'Colour: the Cultural Archive', 'Deep plum and terracotta on a warm stone ground, used with restraint. Plum carries authority and depth; terracotta stops it reading as austere; warm stone gives the work room to breathe. Every colour has exactly one job.',
                 ['Seven colours, one job each.', 'Two grounds per piece: warm stone or deep plum. Never more.', 'Terracotta is an accent, never a fill: one focal point per view.',
                  'Blush belongs to the community layer only.', 'Never a hue outside the set: no teal, no gradient.'], content, 1880)


# ---------------------------------------------------------------- 3. Typography

def typography():
    scale = [('Hook, on a 1080 slide', 104, SERIF, 500, 'The fee is the part you see.'), ('Pull quote', 64, SERIF, 400, '“Know where you stand.”'),
             ('Body on a card', 32, SANS, 400, 'Compare the rate you are given with the mid-market rate on the same day.'), ('Label', 24, SANS, 600, 'Remittances'),
             ('Data', 150, SERIF, 500, 'R 130')]
    sc = ''.join(f'''<div style="display: grid; grid-template-columns: 240px 1fr; gap: 28px; align-items: baseline; padding: 18px 0; border-top: 1px solid {WGREY}">
          <span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600; color: {PLUM}">{n}</span><span style="font-size: 14px; color: {BODY}">{"Playfair Display" if f == SERIF else "Montserrat"} {w}, {sz} px</span></span>
          <span style="{f}; font-weight: {w}; font-size: {min(sz, 96) * .62:.0f}px; line-height: 1.15; color: {PLUM if f == SERIF else BODY}">{t}</span></div>''' for n, sz, f, w, t in scale)
    spec = lambda f, name, roles, licensed, free, sample: f'''<section style="background: {WHITE}; padding: 32px; display: flex; flex-direction: column; gap: 18px">
        <span style="display: flex; justify-content: space-between; align-items: baseline">{label(roles)}<span style="font-size: 15px; color: {BODY}">{name}</span></span>
        <span style="{f}; font-size: 160px; line-height: 1; color: {PLUM}">Aa</span>
        <span style="{f}; font-size: 30px; line-height: 1.35; color: {BODY}">{sample}</span>
        <span style="font-size: 15px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Primary:</b> {licensed}<br><b style="font-weight: 600; color: {PLUM}">Free fallback, used in the live assets:</b> {free}</span></section>'''
    rules = ['One display size and one body size per slide.', 'Left-aligned by default: centred type reads less editorial.', 'The en-dash (–), never the em-dash.',
             'British and South African spelling.', 'Numerals are a design feature: set data large and confidently.', 'Display never all-caps for long phrases; body never in thin weights at small sizes.']
    rl = ''.join(f'<li style="display: flex; gap: 12px; font-size: 18px; line-height: 1.5"><span style="color: {SAGE}; font-weight: 600">–</span>{r}</li>' for r in rules)
    content = f'''<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 28px; align-items: start">
  {spec(SERIF, 'Playfair Display', 'Display: headlines and hooks', 'a refined high-contrast serif: Canela, Noe Display or Fraunces.', 'Playfair Display (or Fraunces).', 'Slide-one hooks, quote cards and pull quotes, with generous line spacing.')}
  {spec(SANS, 'Montserrat', 'Body and UI: everything else', "a neutral grotesque: Inter, Söhne or Suisse Int'l.", 'Montserrat (or Inter).', 'Body copy, captions on cards, labels and data, in regular and medium.')}
  <section style="background: {PLUM}; padding: 32px; display: flex; flex-direction: column; gap: 16px; color: {STONE}">
    <span style="font-size: 20px; font-weight: 700; color: {SAGE}">Type rules</span>
    <ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 12px">{rl}</ul>
    <span style="font-size: 15px; line-height: 1.5; color: {STONE}">Internal documents use Arial, per AWO house style; this pairing is for social and marketing only.</span></section>
</div>
<section style="margin-top: 36px; background: {WHITE}; padding: 12px 32px 20px">{sc}</section>'''
    return board('3', 'Typography', 'A two-typeface system: a high-contrast serif for display, a clean grotesque for everything else. The serif carries the feminine, editorial, premium feeling; the sans keeps it institutional and legible. The pairing is the biggest single driver of the intelligence-brand look.',
                 ['Display: a high-contrast serif; Playfair Display in the live assets.', 'Body and UI: a neutral grotesque; Montserrat in the live assets.',
                  'One display size and one body size per slide, left-aligned.', 'En-dashes, British and South African spelling, and big confident numerals.'], content, 1560)


# ---------------------------------------------------------------- 4. Wordmark

def wordmark_board():
    ways = [(PLUM, STONE, 'Deep plum on warm stone', 'Primary'), (STONE, PLUM, 'Warm stone on deep plum', ''), (SAGE, PLUM, 'Dusty sage on deep plum', '')]
    tiles = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px"><div style="height: 230px; background: {bg}; display: flex; align-items: center; justify-content: center; {"box-shadow: inset 0 0 0 1px " + WGREY if bg == STONE else ""}">{wordmark(64, fg)}</div><span style="font-size: 16px; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">{n}</b>{", the primary" if p else ""}</span></div>' for fg, bg, n, p in ways)
    clear = f'''<div style="position: relative; width: 520px; height: 300px; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}; display: flex; align-items: center; justify-content: center">
        <div style="position: relative; padding: 56px; outline: 1px dashed {TERRA}">{wordmark(64, PLUM)}
          <span style="position: absolute; left: 0; top: 0; width: 56px; height: 56px; background: rgba(184,92,56,.12); display: flex; align-items: center; justify-content: center; {SERIF}; font-size: 22px; color: {TERRA}">A</span>
          <span style="position: absolute; right: 0; bottom: 0; width: 56px; height: 56px; background: rgba(184,92,56,.12); display: flex; align-items: center; justify-content: center; {SERIF}; font-size: 22px; color: {TERRA}">A</span></div></div>'''
    place_car = frame(STONE, f'''<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 380px; font-size: 100px; line-height: 1.08; color: {PLUM}">Where the cost <span style="color: {TERRA}">hides</span>.</h2>{foot_mark(PLUM)}<span style="position: absolute; right: 90px; bottom: 84px; font-size: 26px; font-weight: 600; color: {PLUM}">Swipe</span>''')
    place_quote = frame(PLUM, f'''<p class="ser" style="position: absolute; left: 110px; right: 110px; top: 360px; font-size: 84px; line-height: 1.2; color: {STONE}">“Know where you stand. Grow from there.”</p><span style="position: absolute; left: 110px; top: 300px">{rule(110)}</span><span style="position: absolute; right: 90px; bottom: 80px">{wordmark(30, STONE)}</span>''', fg=STONE)
    donts = [('Stretched', f'<span style="display: inline-block; transform: scaleX(1.6)">{wordmark(40, PLUM)}</span>', STONE),
             ('Recoloured outside the palette', wordmark(40, '#1C9C9C', '#1C9C9C'), STONE),
             ('With effects', f'<span style="filter: drop-shadow(4px 6px 0 #E8A33D)">{wordmark(40, PLUM)}</span>', STONE),
             ('All terracotta on plum', wordmark(40, TERRA), PLUM)]
    dn = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px"><div style="position: relative; height: 150px; background: {bg}; display: flex; align-items: center; justify-content: center; overflow: hidden; {"box-shadow: inset 0 0 0 1px " + WGREY if bg == STONE else ""}">{v}
          <svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true" style="position: absolute; right: 12px; top: 12px"><circle cx="20" cy="20" r="18" fill="{WHITE}" stroke="{TERRA}" stroke-width="2"></circle><path d="M13 13l14 14M27 13 13 27" stroke="{TERRA}" stroke-width="2.4" stroke-linecap="round"></path></svg></div>
          <span style="font-size: 15px; color: {BODY}">{t}</span></div>''' for t, v, bg in donts)
    busy = f'''<div style="display: flex; flex-direction: column; gap: 10px"><div style="position: relative; height: 150px; overflow: hidden"><img src="{IMG['wanjiru_stall']}" alt="" style="width: 100%; height: 100%; object-fit: cover"><span style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%)">{wordmark(40, PLUM)}</span>
          <svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true" style="position: absolute; right: 12px; top: 12px"><circle cx="20" cy="20" r="18" fill="{WHITE}" stroke="{TERRA}" stroke-width="2"></circle><path d="M13 13l14 14M27 13 13 27" stroke="{TERRA}" stroke-width="2.4" stroke-linecap="round"></path></svg></div><span style="font-size: 15px; color: {BODY}">On a busy photo with no scrim</span></div>'''
    content = f'''<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">{tiles}</div>
<div style="margin-top: 44px; display: grid; grid-template-columns: 520px 1fr; gap: 56px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 12px">{label('Clear space: the height of the A on every side')}{clear}
    <span style="font-size: 15px; line-height: 1.5; color: {BODY}">The terracotta rule beside the mark is the only terracotta in the lockup.</span></div>
  <div style="display: flex; flex-direction: column; gap: 12px">{label('Placement: small and consistent')}
    <div style="display: flex; gap: 24px; align-items: flex-end">
      <div style="display: flex; flex-direction: column; gap: 8px">{scaled(place_car, 1080, 1350, .32)}<span style="font-size: 15px; color: {BODY}">A discreet footer on carousels</span></div>
      <div style="display: flex; flex-direction: column; gap: 8px">{scaled(place_quote, 1080, 1350, .32)}<span style="font-size: 15px; color: {BODY}">Bottom corner on quote cards</span></div>
    </div></div>
</div>
<div style="margin-top: 44px; display: flex; flex-direction: column; gap: 12px">{label("Don't")}<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">{dn}{busy}</div></div>'''
    return board('4', 'Wordmark and lockup', 'Confidence is quiet: the work doesn\'t need a large logo. The brief sets clear space, colourways and placement; the wordmark artwork itself wasn\'t in it, so a stand-in is used here (Q-25).',
                 ['Clear space equal to the height of the A, on all sides.', 'Three colourways: plum on stone (primary), stone on plum, sage on plum.',
                  'Terracotta only as the accent rule beside the mark.', 'Small and consistent: a footer or top mark, or the bottom corner.', "Never stretched, recoloured, given effects or set on a busy photo without a scrim."], content, 1600)


# ---------------------------------------------------------------- 5.1 Carousel

def carousel_slides():
    T = 6
    s = [frame(STONE, f'''<span style="position: absolute; left: 90px; top: 90px; font-size: 26px; font-weight: 600; color: {PLUM}">Remittances</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 360px; font-size: 112px; line-height: 1.06; color: {PLUM}">Sending money home costs <span style="color: {TERRA}">more</span> than the fee.</h2>
      {foot_mark(PLUM)}<span style="position: absolute; right: 90px; bottom: 84px; display: flex; align-items: center; gap: 12px; font-size: 26px; font-weight: 600; color: {PLUM}">Swipe<span style="width: 40px; height: 2px; background: {PLUM}"></span></span>''')]
    s.append(frame(PLUM, f'''{slide_no(2, T, SAGE)}<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 380px; font-size: 96px; line-height: 1.1; color: {STONE}">The fee is the part you see.</h2>
      <span style="position: absolute; left: 90px; top: 720px">{rule(120)}</span>
      <p style="position: absolute; left: 90px; right: 180px; top: 790px; font-size: 34px; line-height: 1.5; color: {STONE}">It is printed on the quote. It is rarely the whole cost.</p>''', fg=STONE))
    s.append(frame(STONE, f'''{slide_no(3, T, PLUM)}<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 250px; font-size: 96px; line-height: 1.1; color: {PLUM}">The rest hides in the rate.</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 640px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px">
        <span style="display: flex; flex-direction: column; gap: 10px; padding-top: 24px; border-top: 2px solid {WGREY}"><span style="font-size: 26px; font-weight: 600; color: {BODY}">Mid-market, same day</span><span class="ser" style="font-size: 84px; color: {PLUM}">R 23.05</span><span style="font-size: 24px; color: {BODY}">for £1</span></span>
        <span style="display: flex; flex-direction: column; gap: 10px; padding-top: 24px; border-top: 2px solid {TERRA}"><span style="font-size: 26px; font-weight: 600; color: {BODY}">The rate quoted</span><span class="ser" style="font-size: 84px; color: {PLUM}">R 22.40</span><span style="font-size: 24px; color: {BODY}">for £1</span></span></div>
      <span style="position: absolute; left: 90px; bottom: 90px">{sample_note(BODY)}</span>'''))
    s.append(frame(PLUM, f'''{slide_no(4, T, SAGE)}<span style="position: absolute; left: 90px; top: 300px; font-size: 30px; font-weight: 600; color: {SAGE}">On £200, the gap in the rate is</span>
      <span class="ser" style="position: absolute; left: 84px; top: 380px; font-size: 300px; line-height: 1; color: {STONE}">R 130</span>
      <span style="position: absolute; left: 90px; top: 720px">{rule(160)}</span>
      <p style="position: absolute; left: 90px; right: 180px; top: 790px; font-size: 34px; line-height: 1.5; color: {STONE}">A cost too, even when the fee says zero.</p>
      <span style="position: absolute; left: 90px; bottom: 90px">{sample_note(STONE)}</span>''', fg=STONE))
    s.append(frame(STONE, f'''{slide_no(5, T, PLUM)}<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 380px; font-size: 96px; line-height: 1.1; color: {PLUM}">Ask one question: how much arrives?</h2>
      <p style="position: absolute; left: 90px; right: 180px; top: 760px; font-size: 34px; line-height: 1.5; color: {BODY}">Two quotes, the same amount, the same day. The one that delivers more costs less.</p>'''))
    s.append(frame(STONE, f'''<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 330px; font-size: 100px; line-height: 1.1; color: {PLUM}">Work it out with your own quotes.</h2>
      <span style="position: absolute; left: 90px; top: 680px">{rule(220)}</span>
      <span style="position: absolute; left: 90px; top: 730px; font-size: 40px; font-weight: 600; color: {TERRA}">The calculator – link in bio</span>
      <p style="position: absolute; left: 90px; right: 180px; top: 820px; font-size: 28px; line-height: 1.5; color: {BODY}">AWO explains. It never names or ranks a provider.</p>
      {foot_mark(PLUM)}'''))
    return s


def carousel():
    S = carousel_slides()
    sc = .4
    grid = ('<span aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; opacity: [[ gridO ]]; transition: opacity .25s; '
            'background: linear-gradient(rgba(184,92,56,.16), rgba(184,92,56,.16)) 0 0 / 100% 36px no-repeat, linear-gradient(rgba(184,92,56,.16), rgba(184,92,56,.16)) 0 100% / 100% 32px no-repeat, '
            'linear-gradient(rgba(184,92,56,.16), rgba(184,92,56,.16)) 0 0 / 36px 100% no-repeat, linear-gradient(rgba(184,92,56,.16), rgba(184,92,56,.16)) 100% 0 / 36px 100% no-repeat"></span>')
    names = ['Hook', 'Content, plum', 'Content, stone', 'Data, plum', 'Content, stone', 'Call to action']
    tiles = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px"><div style="position: relative">{scaled(h, 1080, 1350, sc)}{grid}</div><span style="font-size: 15px; font-weight: 600; color: {PLUM}">{i + 1}. {n}</span></div>' for i, (h, n) in enumerate(zip(S, names)))
    anat = [('Slide 1, the hook', 'Warm stone, a serif headline in plum with one terracotta key word, a discreet wordmark, a quiet swipe cue bottom right.'),
            ('Content slides', 'Alternate stone and plum for rhythm; one idea each; the slide number top corner (plum on stone, sage on plum); generous margins.'),
            ('The last slide', 'Warm stone, the terracotta CTA line, "link in bio", the wordmark and the terracotta rule: visibly different, so the swipe lands on an action.')]
    an = ''.join(f'<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 17px; font-weight: 600; color: {PLUM}">{t}</span><span style="font-size: 16px; line-height: 1.55; color: {BODY}">{d}</span></div>' for t, d in anat)
    content = f'''<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px">{label('A sample carousel on sending money home, 1080 by 1350 (4:5)')}
  <button onClick="[[ toggleGrid ]]" aria-pressed="[[ gridOn ]]" style="height: 48px; padding: 0 20px; background: [[ gridBg ]]; color: [[ gridFg ]]; box-shadow: inset 0 0 0 1.5px {PLUM}; font-size: 16px; font-weight: 600">Show the margin grid</button></div>
<div style="display: flex; gap: 24px">{tiles}</div>
<div style="margin-top: 40px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 40px">{an}</div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const on = !!(this.state || {}).g;
    return { gridO: on ? 1 : 0, gridOn: on, gridBg: on ? '%s' : 'transparent', gridFg: on ? '%s' : '%s', toggleGrid: () => this.setState({ g: !on }) };
  }
}''' % (PLUM, STONE, PLUM)
    return board('5.1', 'Instagram: the carousel', 'The save-and-authority engine and the most recognisable AWO asset. A fixed anatomy makes any single slide identifiably AWO.',
                 ['4:5 portrait, 1080 by 1350, up to ten slides.', 'One focal idea per slide; two thoughts need two slides.', 'The same margin grid on every slide, so the set feels engineered.',
                  'At most one terracotta accent per slide; no shadows, gradients or clip-art icons.', 'No paragraph dumping: an essay belongs in the caption.'], content, 1300, logic, w=2960)


# ---------------------------------------------------------------- 5.2 Reels and 5.3 Quote and data cards

def reels_cards():
    reel_cover = frame(PLUM, f'''<span style="position: absolute; left: 90px; top: 140px; font-size: 30px; font-weight: 600; color: {SAGE}">A word, explained</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 700px; font-size: 128px; line-height: 1.05; color: {STONE}">What is a stokvel, really?</h2>
      <span style="position: absolute; left: 90px; top: 1130px">{rule(160)}</span>{foot_mark(STONE, bottom='140px')}''', 1080, 1920, STONE)
    caption = frame(PLUM, f'''<img src="{IMG['naledi_cafe']}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 35% 30%; filter: saturate(.78) sepia(.1)">
      <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(74,45,78,0) 45%, rgba(74,45,78,.88))"></span>
      <span style="position: absolute; left: 80px; right: 80px; bottom: 300px; background: rgba(42,31,46,.82); padding: 26px 32px; font-size: 46px; font-weight: 600; line-height: 1.35; color: {WHITE}">A stokvel is a savings group that takes turns with the pot.</span>''', 1080, 1920, STONE)
    motion = f'''<div style="position: absolute; inset: 0; background: {PLUM}"></div>
      <span style="position: absolute; left: 90px; top: 300px; font-size: 30px; font-weight: 600; color: {SAGE}; animation: fadeRise .7s cubic-bezier(.2,.7,.2,1) .1s both">Number of the week</span>
      <span class="ser" style="position: absolute; left: 84px; top: 380px; font-size: 260px; line-height: 1; color: {STONE}; animation: fadeRise .8s cubic-bezier(.2,.7,.2,1) .35s both">27.75%</span>
      <span style="position: absolute; left: 90px; top: 720px; width: 200px; height: 4px; background: {TERRA}; transform-origin: 0 50%; animation: drawOn .9s cubic-bezier(.6,0,.2,1) .9s both"></span>
      <p style="position: absolute; left: 90px; right: 180px; top: 780px; margin: 0; font-size: 36px; line-height: 1.5; color: {STONE}; animation: fadeRise .8s cubic-bezier(.2,.7,.2,1) 1.2s both">The rate on a sample R 8 000 loan. Read what it costs in all.</p>'''
    motion_card = ''.join(f'<sc-if value="[[ run{k} ]]" hint-placeholder-val="[[ {"true" if k == 0 else "false"} ]]">{scaled(frame(PLUM, motion, fg=STONE), 1080, 1350, .3)}</sc-if>' for k in (0, 1))
    quote = frame(PLUM, f'''<span style="position: absolute; left: 110px; top: 330px">{rule(110)}</span><p class="ser" style="position: absolute; left: 110px; right: 110px; top: 390px; font-size: 88px; line-height: 1.2; color: {STONE}">“Know where you stand. Grow from there.”</p><span style="position: absolute; right: 90px; bottom: 80px">{wordmark(30, STONE)}</span>''', fg=STONE)
    data = frame(STONE, f'''<span style="position: absolute; left: 90px; top: 110px; font-size: 26px; font-weight: 600; color: {PLUM}">Remittances</span>
      <span class="ser" style="position: absolute; left: 84px; top: 330px; font-size: 330px; line-height: 1; color: {PLUM}">R 130</span>
      <span style="position: absolute; left: 90px; top: 700px">{rule(160)}</span>
      <p style="position: absolute; left: 90px; right: 200px; top: 760px; margin: 0; font-size: 38px; line-height: 1.45; color: {BODY}">hidden in the rate on £200, with a "no fee" quote.</p>
      <span style="position: absolute; left: 90px; bottom: 90px; font-size: 22px; color: #6E6470">Sample quotes, 1 October 2026. Every real figure carries its source.</span>
      <span style="position: absolute; right: 90px; bottom: 80px">{wordmark(30, PLUM)}</span>''')
    reel_rules = [('Cover frame', 'Designed like a slide-one hook, so Reels sit cleanly in the grid.'), ('Captions', 'Burned in, sans, high contrast, lower third: most viewing is sound-off.'),
                  ('Talking heads', 'Clean, well lit, a neutral or on-brand background. A recognisable AWO face builds trust.'),
                  ('Motion', 'Restrained: staggered fade-and-rise on type, the terracotta rule drawing on, gentle drift, soft cross-dissolves. Never bouncy.')]
    rr = ''.join(f'<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 17px; font-weight: 600; color: {PLUM}">{t}</span><span style="font-size: 16px; line-height: 1.55; color: {BODY}">{d}</span></div>' for t, d in reel_rules)
    content = f'''<div style="display: grid; grid-template-columns: auto auto auto minmax(0, 1fr); gap: 32px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(reel_cover, 1080, 1920, .25)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Reel cover, 9:16</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(caption, 1080, 1920, .25)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Burned-in caption, scrimmed</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{motion_card}<span style="display: flex; justify-content: space-between; align-items: center; gap: 10px"><span style="font-size: 15px; font-weight: 600; color: {PLUM}">The motion, live</span>
      <button onClick="[[ replay ]]" style="height: 44px; padding: 0 16px; box-shadow: inset 0 0 0 1.5px {PLUM}; font-size: 15px; font-weight: 600; color: {PLUM}">Play again</button></span></div>
  <div style="display: flex; flex-direction: column; gap: 22px">{label('5.2 Reels: 9:16, 1080 by 1920; the hook lands in the first 1.5 seconds')}{rr}</div>
</div>
<div style="margin-top: 48px; display: grid; grid-template-columns: auto auto minmax(0, 1fr); gap: 32px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(quote, 1080, 1350, .34)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Quote card</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(data, 1080, 1350, .34)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Data card</span></div>
  <div style="display: flex; flex-direction: column; gap: 18px">{label('5.3 Quote and data cards: 4:5, or 1:1 square')}
    <span style="font-size: 17px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Quote cards:</b> a serif line in stone on plum, or plum on stone; plenty of space; a small wordmark; a terracotta rule for the accent. The brand line as a designed object.</span>
    <span style="font-size: 17px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Data cards:</b> one statistic set large in the serif, the source small in grey sans, a single terracotta accent. Restraint makes the number land.</span>
    <span style="font-size: 17px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Our note:</b> the source line in grey must stay readable. #6E6470 on warm stone is 4.7:1; the brief's warm grey (1.55:1) is for hairlines only.</span></div>
</div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const n = (this.state || {}).n || 0;
    return { run0: n %% 2 === 0, run1: n %% 2 === 1, replay: () => this.setState({ n: n + 1 }) };
  }
}'''.replace('%%', '%')
    return board('5.2–5.3', 'Reels, quote cards and data cards', 'Reels sit in the grid like any slide; quote and data cards turn one line or one number into a designed object.',
                 ['Reel covers designed like a hook; captions always burned in.', 'Motion restrained and editorial: fade-and-rise, the rule drawing on.',
                  'Quote cards: one serif line, lots of space, a terracotta rule.', 'Data cards: one number large, a small source, one accent.'], content, 1560, logic)


# ---------------------------------------------------------------- 5.4 Stories and 5.5 Feed grid

def stories_grid():
    st = []
    st.append(('Poll', frame(PLUM, f'''<span style="position: absolute; left: 90px; top: 200px; font-size: 32px; font-weight: 600; color: {SAGE}">Poll</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 420px; font-size: 96px; line-height: 1.12; color: {STONE}">Do you know what your stokvel's rules say about a late payment?</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 1080px; display: flex; flex-direction: column; gap: 24px">
        <span style="height: 120px; border: 3px solid {TERRA}; display: flex; align-items: center; padding: 0 40px; font-size: 40px; font-weight: 600; color: {STONE}">Yes, by heart</span>
        <span style="height: 120px; border: 3px solid {SAGE}; display: flex; align-items: center; padding: 0 40px; font-size: 40px; font-weight: 600; color: {STONE}">Not really</span></div>''', 1080, 1920, STONE)))
    st.append(('Question box', frame(STONE, f'''<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 360px; font-size: 104px; line-height: 1.1; color: {PLUM}">Ask us anything about your payslip.</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 900px; background: {WHITE}; border-top: 6px solid {TERRA}; padding: 50px; display: flex; flex-direction: column; gap: 30px">
        <span style="font-size: 36px; font-weight: 600; color: {PLUM}">Your question</span><span style="height: 90px; background: {STONE}"></span></div>{foot_mark(PLUM, bottom='160px')}''', 1080, 1920)))
    st.append(('Number of the week', frame(PLUM, f'''<span style="position: absolute; left: 90px; top: 360px; font-size: 32px; font-weight: 600; color: {SAGE}">Number of the week</span>
      <span class="ser" style="position: absolute; left: 84px; top: 470px; font-size: 300px; line-height: 1; color: {STONE}">3</span>
      <span style="position: absolute; left: 90px; top: 820px">{rule(180)}</span>
      <p style="position: absolute; left: 90px; right: 160px; top: 880px; margin: 0; font-size: 44px; line-height: 1.45; color: {STONE}">minutes: the length of an AWO lesson. One fits in a taxi ride.</p>''', 1080, 1920, STONE)))
    st.append(('Re-share frame', frame(STONE, f'''<span style="position: absolute; left: 90px; top: 220px; font-size: 32px; font-weight: 600; color: {PLUM}">New on the feed</span>
      <div style="position: absolute; left: 160px; top: 420px; box-shadow: 0 0 0 3px {PLUM}">{scaled(carousel_slides()[0], 1080, 1350, .7, shadow=False)}</div>
      <span style="position: absolute; left: 160px; top: 1430px">{rule(180)}</span>''', 1080, 1920)))
    st.append(('Countdown', frame(PLUM, f'''<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 420px; font-size: 104px; line-height: 1.1; color: {STONE}">Live: reading a payslip, line by line.</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 960px; border: 3px solid {TERRA}; padding: 44px; display: flex; flex-direction: column; gap: 16px">
        <span style="font-size: 32px; font-weight: 600; color: {SAGE}">Countdown</span><span class="ser" style="font-size: 92px; color: {STONE}">Thursday, 19:00</span></div>''', 1080, 1920, STONE)))
    stories = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px">{scaled(h, 1080, 1920, .2)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">{n}</span></div>' for n, h in st)
    S = carousel_slides()
    q = frame(PLUM, f'<p class="ser" style="position: absolute; left: 100px; right: 100px; top: 420px; font-size: 92px; line-height: 1.2; color: {STONE}">“Know where you stand.”</p><span style="position: absolute; left: 100px; top: 360px">{rule(110)}</span>', fg=STONE)
    reel = frame(PLUM, f'<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 520px; font-size: 120px; line-height: 1.05; color: {STONE}">What is a stokvel, really?</h2><svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="{STONE}" stroke-width="1.2" aria-hidden="true" style="position: absolute; right: 90px; top: 90px"><path d="M8 5.5v13l10.5-6.5z"></path></svg>', fg=STONE)
    datac = frame(STONE, f'<span class="ser" style="position: absolute; left: 84px; top: 380px; font-size: 330px; line-height: 1; color: {PLUM}">R 130</span><span style="position: absolute; left: 90px; top: 760px">{rule(160)}</span>')
    qs = frame(STONE, f'<p class="ser" style="position: absolute; left: 100px; right: 100px; top: 420px; font-size: 92px; line-height: 1.2; color: {PLUM}">“Restraint is the brand.”</p><span style="position: absolute; left: 100px; top: 360px">{rule(110)}</span>')
    cells = [S[0], reel, datac, q, S[2], S[3], S[4], reel.replace('What is a stokvel, really?', 'What does a payslip owe you?'), qs]
    grid = ''.join(scaled(c, 1080, 1350, .15, shadow=False) for c in cells)
    rules = ['Alternate plum and stone, so the grid has rhythm, not blocks of one tone.', 'Rotate a carousel hook, a Reel cover and a quote or data card: varied texture, one visual language.',
             'Plan three posts ahead; keep the latest nine cohesive. That is what a new visitor judges before following.']
    rl = ''.join(f'<li style="display: flex; gap: 12px; font-size: 17px; line-height: 1.55"><span style="color: {TERRA}; font-weight: 600">–</span>{r}</li>' for r in rules)
    content = f'''<div style="display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 56px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 14px">{label('5.4 Stories: a small reusable set, lighter than the feed, 9:16')}<div style="display: flex; gap: 20px">{stories}</div>
    <span style="font-size: 16px; line-height: 1.55; color: {BODY}; max-width: 1150px">Plum or stone grounds, terracotta on interactive stickers, the same type. Blush appears only when a Story is explicitly community content.</span></div>
  <div style="display: flex; flex-direction: column; gap: 14px">{label('5.5 The feed grid, the latest nine')}
    <div style="background: {WHITE}; padding: 20px; display: flex; flex-direction: column; gap: 16px; width: 524px">
      <span style="display: flex; align-items: center; gap: 14px"><span style="width: 64px; height: 64px; border-radius: 999px; background: {PLUM}; display: flex; align-items: center; justify-content: center">{wordmark(16, STONE)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">African Wealth Oasis</span><span style="font-size: 14px; color: {BODY}">Financial intelligence for African women</span></span></span>
      <div style="display: grid; grid-template-columns: repeat(3, 162px); gap: 3px">{grid}</div></div>
    <ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; width: 524px">{rl}</ul></div>
</div>'''
    return board('5.4–5.5', 'Stories and the feed grid', 'Stories are lower production than the feed but never off brand. The grid is composed, not random: the profile should read as one designed whole when a new visitor lands.',
                 ['Five Story templates: poll, question box, number of the week, re-share frame, countdown.', 'Terracotta on interactive stickers; blush only for community Stories.',
                  'Alternate plum and stone posts; rotate hooks, Reel covers and cards.', 'Compose three posts ahead; keep the latest nine cohesive.'], content, 1440)


# ---------------------------------------------------------------- 6. LinkedIn

def linkedin():
    cov = frame(PLUM, f'''<span style="position: absolute; left: 90px; top: 110px">{wordmark(32, STONE)}</span>
      <span style="position: absolute; left: 90px; top: 380px; font-size: 28px; font-weight: 600; color: {SAGE}">Data brief, October 2026</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 440px; font-size: 104px; line-height: 1.08; color: {STONE}">Sending money home: where the cost hides</h2>
      <span style="position: absolute; left: 90px; top: 860px">{rule(160)}</span><span style="position: absolute; left: 90px; bottom: 100px; font-size: 26px; font-weight: 600; color: {SAGE}">Sources inside</span>''', fg=STONE)
    bars = [('Quote A', 45, 60, False), ('Quote B, "no fee"', 0, 130, True), ('Quote C', 70, 20, False)]
    mx = 160
    chart = ''.join(f'''<div style="display: grid; grid-template-columns: 300px 1fr 120px; gap: 24px; align-items: center">
          <span style="font-size: 28px; font-weight: 600; color: {BODY}">{n}</span>
          <span style="display: flex; height: 64px"><span style="width: {f / mx * 100:.1f}%; background: {SAGE}"></span><span style="width: {g / mx * 100:.1f}%; background: {TERRA if hl else PLUM}"></span></span>
          <span class="ser" style="font-size: 44px; color: {PLUM}">R {f + g}</span></div>''' for n, f, g, hl in bars)
    gridlines = ''.join(f'<span style="position: absolute; top: 0; bottom: 0; left: calc(324px + (100% - 468px) * {k / 4}); border-left: 1px solid {WGREY}"></span>' for k in range(5))
    dslide = frame(STONE, f'''{slide_no(3, 8, PLUM)}<h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 150px; font-size: 76px; line-height: 1.1; color: {PLUM}">What £200 really costs to send, three sample quotes</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 520px; display: flex; flex-direction: column; gap: 46px">{gridlines}{chart}</div>
      <span style="position: absolute; left: 90px; top: 960px; display: flex; gap: 40px; font-size: 24px; color: {BODY}"><span style="display: flex; align-items: center; gap: 12px"><span style="width: 26px; height: 26px; background: {SAGE}"></span>Fee</span><span style="display: flex; align-items: center; gap: 12px"><span style="width: 26px; height: 26px; background: {PLUM}"></span>Hidden in the rate</span><span style="display: flex; align-items: center; gap: 12px"><span style="width: 26px; height: 26px; background: {TERRA}"></span>The highlight</span></span>
      <span style="position: absolute; left: 90px; right: 90px; bottom: 90px; font-size: 22px; line-height: 1.5; color: #6E6470">Source: sample quotes for illustration; mid-market rate R 23.05 for £1 (sample), 1 October 2026.</span>''')
    close = frame(STONE, f'''<span style="position: absolute; left: 90px; top: 300px; font-size: 28px; font-weight: 600; color: {PLUM}">The takeaway</span>
      <h2 class="ser" style="position: absolute; left: 90px; right: 90px; top: 360px; font-size: 92px; line-height: 1.12; color: {PLUM}">Compare what arrives, <span style="box-shadow: inset 0 -6px 0 {TERRA}">not the fee</span>.</h2>
      <div style="position: absolute; left: 90px; right: 90px; top: 800px; padding-top: 30px; border-top: 1px solid {WGREY}; display: flex; flex-direction: column; gap: 14px; font-size: 24px; line-height: 1.5; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Sources</b><span>1. Sample provider quotes, 1 October 2026, for illustration.</span><span>2. Mid-market rate, sample, same day.</span></div>
      {foot_mark(PLUM)}''')
    single = frame(PLUM, f'''<h2 class="ser" style="position: absolute; left: 100px; right: 100px; top: 520px; font-size: 104px; line-height: 1.15; color: {STONE}">Financial intelligence starts with <span style="box-shadow: inset 0 -6px 0 {TERRA}">reading the rate</span>.</h2>{foot_mark(STONE, bottom='100px', left='100px')}''', 1200, 1500, STONE)
    banner = lambda w, h, s: f'''<div style="position: relative; width: {w}px; height: {h}px; background: {PLUM}; overflow: hidden">
        <span style="position: absolute; left: {round(h * .32)}px; top: 50%; transform: translateY(-50%); display: flex; align-items: center; gap: {round(h * .16)}px">{wordmark(round(h * s), STONE)}
          <span style="width: {round(h * .3)}px; height: 2px; background: {TERRA}"></span><span style="font-size: {round(h * s * .5)}px; font-weight: 500; color: {SAGE}">Financial intelligence for African women</span></span></div>'''
    content = f'''<div style="display: grid; grid-template-columns: auto auto auto auto; gap: 28px; align-items: start">
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(cov, 1080, 1350, .3)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Document post: cover</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(dslide, 1080, 1350, .3)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">A data slide, in palette only</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(close, 1080, 1350, .3)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">The close: takeaway and sources</span></div>
  <div style="display: flex; flex-direction: column; gap: 10px">{scaled(single, 1200, 1500, .27)}<span style="font-size: 15px; font-weight: 600; color: {PLUM}">Single image, 1200 by 1500</span></div>
</div>
<div style="margin-top: 44px; display: flex; flex-direction: column; gap: 22px">
  <div style="display: flex; flex-direction: column; gap: 10px">{label('Company page banner, 1128 by 191, at full size')}{banner(1128, 191, .26)}</div>
  <div style="display: flex; flex-direction: column; gap: 10px">{label('Founder profile banner, 1584 by 396, shown at 70%')}<div style="width: 1109px; height: 277px; overflow: hidden"><div style="transform: scale(.7); transform-origin: 0 0">{banner(1584, 396, .2)}</div></div>
    <span style="font-size: 16px; line-height: 1.55; color: {BODY}; max-width: 1100px">The founder profile is the primary authority engine: a professional headshot, this banner and a headline that names the mission.</span></div>
</div>'''
    return board('6', 'LinkedIn: the authority engine', 'More institutional and more restrained than Instagram: closer to a research house than a lifestyle brand. The same palette and type, dialled toward credibility, with deep plum doing more of the work.',
                 ['Document posts: 4:5 PDFs that look like a report cover, not a meme.', 'Charts in palette only: plum bars, one terracotta highlight, warm grey gridlines, sage second series.',
                  'Always cite: rigour is the LinkedIn differentiator.', 'Single images: stone on plum with a terracotta underline, slightly more conservative sizes.', 'Banners: plum, the wordmark, the category line and a terracotta rule.'], content, 1620)


# ---------------------------------------------------------------- 7. Photography

def imagery():
    photos = [(IMG['naledi_cafe'], '30% 30%', 'Considered'), (IMG['amara_coat'], '55% 25%', 'Capable'), (IMG['thandi_window'], '50% 30%', 'At ease'), (IMG['adaeze'], '50% 30%', 'At work')]
    ph = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px"><div style="height: 300px; overflow: hidden"><img src="{s}" alt="" style="width: 100%; height: 100%; object-fit: cover; object-position: {p}; filter: [[ grade ]]; transition: filter .4s"></div><span style="font-size: 15px; font-weight: 600; color: {PLUM}">{t}</span></div>''' for s, p, t in photos)
    hero = f'''<div style="position: relative; height: 560px; overflow: hidden">
      <img src="{IMG['naledi_table']}" alt="A woman working at her dining table" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 25% 50%; filter: [[ grade ]]; transition: filter .4s">
      <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to left, rgba(74,45,78,.94) 0, rgba(74,45,78,.8) 40%, rgba(74,45,78,0) 68%); opacity: [[ scrimO ]]; transition: opacity .4s"></span>
      <div style="position: absolute; right: 56px; top: 50%; transform: translateY(-50%); width: 500px; display: flex; flex-direction: column; gap: 22px">
        <h2 class="ser" style="font-size: 64px; line-height: 1.1; color: {STONE}">Read your payslip, line by line.</h2>{rule(110)}
        <span style="font-size: 20px; line-height: 1.5; color: {STONE}">The subject off-centre, the space left for type, a plum scrim underneath it.</span></div></div>'''
    avoid = ['Cash fans and luxury bait', 'Generic finance stock: suited men, rising arrows, gold coins', 'Stock-cliché "excited about money" poses', 'Heavy filters and high-saturation looks']
    av = ''.join(f'<li style="display: flex; gap: 12px; font-size: 17px; line-height: 1.5"><span style="color: {TERRA}; font-weight: 600">–</span>{a}</li>' for a in avoid)
    content = f'''<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px">{label('Subjects: African women, real and dignified')}
  <button onClick="[[ toggle ]]" aria-pressed="[[ on ]]" style="height: 48px; padding: 0 20px; background: [[ bBg ]]; color: [[ bFg ]]; box-shadow: inset 0 0 0 1.5px {PLUM}; font-size: 16px; font-weight: 600">Apply the AWO grade and scrim</button></div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">{ph}</div>
<div style="margin-top: 40px; display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr); gap: 48px; align-items: start">
  {hero}
  <div style="display: flex; flex-direction: column; gap: 22px">
    <span style="font-size: 17px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Treatment:</b> warm, natural light; a muted, slightly desaturated grade that sits with plum and terracotta. Earthy, not glossy.</span>
    <span style="font-size: 17px; line-height: 1.6; color: {BODY}"><b style="font-weight: 600; color: {PLUM}">Composition:</b> space for type, subjects off-centre, and always a deep plum scrim before text goes on a photo.</span>
    <section style="background: {WHITE}; padding: 22px 26px; display: flex; flex-direction: column; gap: 12px">{label('Avoid: these undercut the positioning')}<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 8px">{av}</ul></section>
    <span style="font-size: 15px; line-height: 1.5; color: {BODY}">These are the canvas's stand-in photos (nappy.co) with the grade applied in the browser; real AWO photography comes later.</span>
  </div>
</div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const on = (this.state || {}).on == null ? true : this.state.on;
    return { on, grade: on ? 'saturate(.72) sepia(.14) contrast(.96) brightness(1.02)' : 'none', scrimO: on ? 1 : .35,
      bBg: on ? '%s' : 'transparent', bFg: on ? '%s' : '%s', toggle: () => this.setState({ on: !on }) };
  }
}''' % (PLUM, STONE, PLUM)
    return board('7', 'Photography and imagery', 'Real African women, considered and capable, in warm natural light with a muted grade. Never stock clichés.',
                 ['Subjects: real and dignified; considered, capable, at ease.', 'Treatment: warm light, slightly desaturated, earthy rather than glossy.',
                  'Composition: room for type, subjects off-centre, a plum scrim under any text.', 'Avoid cash fans, luxury bait and generic finance stock.'], content, 1480, logic)


# ---------------------------------------------------------------- 8. Graphic elements

ICONS = {'book': '<path d="M4 5.5c3-1.3 5.5-1.3 8 0v14c-2.5-1.3-5-1.3-8 0z"></path><path d="M20 5.5c-3-1.3-5.5-1.3-8 0v14c2.5-1.3 5-1.3 8 0z"></path>',
         'calc': '<rect x="5" y="3" width="14" height="18" rx="1"></rect><path d="M8 7h8M8 11h2M12 11h2M16 11h0M8 15h2M12 15h2M8 18h2M12 18h2M16 15v3"></path>',
         'people': '<circle cx="9" cy="8" r="3"></circle><path d="M3.5 19c.8-3.2 3-5 5.5-5s4.7 1.8 5.5 5"></path><circle cx="17" cy="9" r="2.4"></circle><path d="M15.5 14.3c2.4-.4 4.4 1.2 5 4.2"></path>',
         'shield': '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path>',
         'chart': '<path d="M4 20V4M4 20h16"></path><path d="M8 16v-4M12 16V8M16 16v-6"></path>',
         'calendar': '<rect x="4" y="5" width="16" height="15" rx="1"></rect><path d="M4 10h16M8 3v4M16 3v4"></path>'}


def elements():
    ic = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 10px"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg><span style="font-size: 14px; color: {BODY}">{n}</span></span>'
                 for (n, p), c in zip(ICONS.items(), [PLUM, PLUM, PLUM, TERRA, PLUM, PLUM]))
    pts = [(0, 55), (1, 59), (2, 63), (3, 64), (4, 68), (5, 70)]
    W, Hh = 620, 260
    line = ' '.join(f'{"M" if i == 0 else "L"}{40 + x * (W - 80) / 5:.0f} {Hh - 30 - (y - 50) * 9:.0f}' for i, (x, y) in enumerate(pts))
    grid = ''.join(f'<path d="M40 {Hh - 30 - k * 45:.0f} H{W - 40}" stroke="{WGREY}" stroke-width="1"></path>' for k in range(5))
    dots = ''.join(f'<circle cx="{40 + x * (W - 80) / 5:.0f}" cy="{Hh - 30 - (y - 50) * 9:.0f}" r="{7 if i == 5 else 5}" fill="{TERRA if i == 5 else PLUM}"></circle>' for i, (x, y) in enumerate(pts))
    chart = f'<svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" role="img" aria-label="A sample line chart rising from 55 to 70, the last point highlighted" style="display: block">{grid}<path d="{line}" fill="none" stroke="{PLUM}" stroke-width="3"></path>{dots}</svg>'
    tex = ('<svg width="100%" height="100%" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; inset: 0"><filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="4"></feTurbulence>'
           '<feColorMatrix values="0 0 0 0 0.29  0 0 0 0 0.18  0 0 0 0 0.3  0 0 0 0.07 0"></feColorMatrix></filter><rect width="100%" height="100%" filter="url(#paper)"></rect></svg>')
    content = f'''<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 32px">
  <section style="background: {WHITE}; padding: 30px; display: flex; flex-direction: column; gap: 22px">{label('Rules and lines: the signature device')}
    <div style="display: flex; flex-direction: column; gap: 10px"><span class="ser" style="font-size: 40px; color: {PLUM}">A heading, then a rule</span>{rule(72)}</div>
    <div style="background: {PLUM}; padding: 24px 28px; display: flex; flex-direction: column; gap: 14px"><span style="font-size: 19px; font-weight: 600; color: {SAGE}">On plum, sage hairlines divide</span><span style="height: 1px; background: {SAGE}"></span><span style="font-size: 18px; color: {STONE}">Thin terracotta or sage rules structure and divide; never thick bars.</span></div></section>
  <section style="background: {WHITE}; padding: 30px; display: flex; flex-direction: column; gap: 22px">{label('Icons, if used at all: fine line, one weight, one colour')}
    <div style="display: flex; justify-content: space-between">{ic}</div>
    <span style="font-size: 16px; line-height: 1.55; color: {BODY}">Monochrome, in plum or terracotta. No filled, multicolour or 3D icons.</span></section>
  <section style="background: {WHITE}; padding: 30px; display: flex; flex-direction: column; gap: 16px">{label('Data viz: palette only, clean, labelled, sourced')}{chart}
    <span style="font-size: 15px; line-height: 1.5; color: #6E6470">Sample series, for layout only. Source line here on every real chart.</span></section>
  <section style="padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px">
    <div style="position: relative; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}; display: flex; align-items: flex-end; padding: 24px"><span style="font-size: 16px; font-weight: 600; color: {PLUM}">Warm stone, plain</span></div>
    <div style="position: relative; background: {STONE}; box-shadow: inset 0 0 0 1px {WGREY}; display: flex; align-items: flex-end; padding: 24px; overflow: hidden">{tex}<span style="position: relative; font-size: 16px; font-weight: 600; color: {PLUM}">With a subtle paper texture (optional)</span></div></section>
</div>'''
    return board('8', 'Graphic elements and icons', 'A few quiet devices do the structural work: thin rules, fine-line icons, charts in palette, and an optional paper texture for warmth.',
                 ['Thin terracotta or sage rules to structure and divide.', 'Icons fine line, single weight, monochrome; or none at all.',
                  'Charts: plum, one terracotta highlight, sage and warm grey in support; labelled and sourced.', 'Optional subtle paper or linen texture on stone; never busy patterns.'], content, 1260)


# ---------------------------------------------------------------- 9. Specs and 10. At a glance

SPECS = [('Carousel slide', 'Instagram', 1080, 1350, 'Up to 10 slides; hook, content, CTA'), ('Reel', 'Instagram', 1080, 1920, 'Designed cover; burned-in captions'),
         ('Quote or data card', 'Instagram', 1080, 1080, 'Or 1080 by 1350; serif focal, one accent'), ('Story', 'Instagram', 1080, 1920, 'Reusable set; lighter production'),
         ('Document post', 'LinkedIn', 1080, 1350, 'PDF, report style; sources mandatory'), ('Single image', 'LinkedIn', 1200, 1500, 'Or 1200 by 627; conservative sizing'),
         ('Page banner', 'LinkedIn (page)', 1128, 191, 'Wordmark and category line'), ('Profile banner', 'LinkedIn (personal)', 1584, 396, 'The founder authority asset')]


def specs():
    k = .16
    frames = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px; align-items: flex-start">
          <span style="width: {w * k:.0f}px; height: {h * k:.0f}px; background: {PLUM if i % 2 else WHITE}; box-shadow: inset 0 0 0 1.5px {PLUM}; display: flex; align-items: flex-end; padding: 8px; box-sizing: border-box; font-size: 13px; font-weight: 600; color: {STONE if i % 2 else PLUM}">{w} by {h}</span>
          <span style="font-size: 15px; font-weight: 600; color: {PLUM}">{n}</span><span style="font-size: 14px; color: {BODY}">{p}</span></div>''' for i, (n, p, w, h, _note) in enumerate(SPECS))
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 1.2fr 1.1fr .9fr 2fr; gap: 20px; padding: 14px 0; border-top: 1px solid {WGREY}; font-size: 17px">
          <span style="font-weight: 600; color: {PLUM}">{n}</span><span>{p}</span><span style="font-variant-numeric: tabular-nums">{w} × {h}</span><span>{note}</span></div>''' for n, p, w, h, note in SPECS)
    content = f'''<div style="display: flex; gap: 28px; align-items: flex-end; flex-wrap: wrap">{frames}</div>
<section style="margin-top: 40px; background: {WHITE}; padding: 14px 32px 24px">
  <div style="display: grid; grid-template-columns: 1.2fr 1.1fr .9fr 2fr; gap: 20px; padding: 12px 0; font-size: 15px; font-weight: 600; color: {PLUM}"><span>Asset</span><span>Platform</span><span>Pixels</span><span>Notes</span></div>{rows}</section>'''
    return board('9', 'Asset specifications', 'Every format the brief names, drawn to the same scale, so the proportions are easy to compare.',
                 ['Instagram: 4:5 carousels and cards, 9:16 Reels and Stories, 1:1 cards.', 'LinkedIn: 4:5 document PDFs, 1200-wide single images, two banner sizes.',
                  'Document posts always carry their sources.'], content, 1360)


def glance():
    always = ['Deep plum and terracotta on warm stone; terracotta a single accent per view.', 'The serif and sans pairing; left-aligned, with generous space.', 'One idea per slide; recognisable as AWO before the handle is read.',
              'En-dashes, British and South African spelling, sourced data.', 'Compose the grid three posts ahead.']
    never = ['Hues outside the set, gradients, drop shadows or multicolour icons.', 'Terracotta type on deep plum, terracotta fills, large logos or busy backgrounds.', 'Blush anywhere outside the community layer.',
             'Cash or luxury-bait imagery, or generic finance stock.', 'Hype styling, emoji saturation or an essay on a slide.']
    lst = lambda items, col, dash=TERRA: ''.join(f'<li style="display: flex; gap: 14px; font-size: 21px; line-height: 1.5; padding: 14px 0; border-top: 1px solid {col}"><span style="flex-shrink: 0; color: {dash}; font-weight: 600">–</span>{t}</li>' for t in items)
    content = f'''<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px">
  <section style="background: {WHITE}; padding: 32px 36px; display: flex; flex-direction: column; gap: 10px"><span class="ser" style="font-size: 44px; color: {PLUM}">Always</span><ul style="margin: 0; padding: 0; list-style: none">{lst(always, WGREY)}</ul></section>
  <section style="background: {PLUM}; padding: 32px 36px; display: flex; flex-direction: column; gap: 10px; color: {STONE}"><span class="ser" style="font-size: 44px; color: {STONE}">Never</span><ul style="margin: 0; padding: 0; list-style: none">{lst(never, 'rgba(143,165,134,.5)', SAGE)}</ul></section>
</div>
<div style="margin-top: 40px; padding: 48px 0 8px; display: flex; flex-direction: column; gap: 20px; border-top: 1px solid {WGREY}">
  <span style="font-size: 17px; font-weight: 600; color: {TERRA}">One line to keep on the wall</span>
  <p class="ser" style="font-size: 54px; line-height: 1.25; color: {PLUM}; max-width: 1500px">AWO is an intelligence brand. Restraint, structure and quiet confidence, not noise, are how the design earns trust before a single word is read.</p></div>'''
    return board('10', 'At a glance: always and never', 'The whole system on one board: what every piece does, and what none of them ever does.',
                 ['Plum and terracotta on stone, one accent per view.', 'Serif and sans, left-aligned, generous space.', 'One idea per slide; sourced data.', 'Nothing outside the palette; no hype.'], content, 1240)


BOARDS = [('BS-Cover', cover), ('BS-Bar', bar), ('BS-Colour', colour), ('BS-Type', typography), ('BS-Wordmark', wordmark_board),
          ('BS-Carousel', carousel), ('BS-Reels-Cards', reels_cards), ('BS-Stories-Grid', stories_grid), ('BS-LinkedIn', linkedin),
          ('BS-Imagery', imagery), ('BS-Elements', elements), ('BS-Specs', specs), ('BS-Glance', glance)]
TITLES = {'BS-Cover': 'Cover: the brief', 'BS-Bar': '1. The bar to clear', 'BS-Colour': '2. Colour: the Cultural Archive (contrast checked)',
          'BS-Type': '3. Typography', 'BS-Wordmark': '4. Wordmark and lockup (stand-in mark)', 'BS-Carousel': '5.1 Instagram carousel (try the margin grid)',
          'BS-Reels-Cards': '5.2 to 5.3 Reels, quote and data cards (play the motion)', 'BS-Stories-Grid': '5.4 to 5.5 Stories and the feed grid',
          'BS-LinkedIn': '6. LinkedIn: document posts, single images, banners', 'BS-Imagery': '7. Photography (toggle the grade)',
          'BS-Elements': '8. Graphic elements and icons', 'BS-Specs': '9. Asset specifications, to scale', 'BS-Glance': '10. At a glance: always and never'}
ROWS = [('bst1', "AWO's suggested brand system (social): the brief, the bar, colour and type", ['BS-Cover', 'BS-Bar', 'BS-Colour', 'BS-Type']),
        ('bst2', 'The wordmark and the Instagram templates', ['BS-Wordmark', 'BS-Carousel', 'BS-Reels-Cards', 'BS-Stories-Grid']),
        ('bst3', 'LinkedIn, imagery, elements, specs and the whole system at a glance', ['BS-LinkedIn', 'BS-Imagery', 'BS-Elements', 'BS-Specs', 'BS-Glance'])]
HOWTO = ("AWO's suggested Visual Brand System (the brief for Instagram and LinkedIn, shared 1 October 2026), laid out one board per "
         "section in its own system: deep plum, terracotta and warm stone, Playfair Display and Montserrat. Each board lists the key "
         "elements from the brief and shows them applied.\n\n"
         "What we added: contrast checks on every colour pair (terracotta text on warm stone and sage labels on plum are large-text only), "
         "worked sample templates, and a stand-in wordmark (the artwork wasn't in the brief).\n\n"
         "The last four rows apply the system to the app: onboarding, the major screens, the Play Store set, the website and two ads, "
         "with the same sample member and numbers as the Round 7 board, so the two can be compared side by side.\n\n"
         "It differs from the app's design language on the Round 7 board (evergreen, lime, Geist, the stepping-stones mark), and its "
         "warm stone ground is the kind of cream ground rule D13 avoids. Which leads, or how they meet, is Ian's call: Q-49.\n\n"
         "All content is sample content. Summary in docs/00-discovery/16-brand-system-brief.md.")


def size(proj, name):
    s = open(os.path.join(proj, name + '.dc.html')).read()
    m = re.search(r'"\$preview"\s*:\s*\{\s*"width"\s*:\s*(\d+)\s*,\s*"height"\s*:\s*(\d+)', s)
    return int(m.group(1)), int(m.group(2))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import applied  # the system applied to the app, the store and marketing (Q-49)
    BOARDS = BOARDS + applied.BOARDS
    TITLES.update(applied.TITLES)
    ROWS = ROWS + applied.ROWS
    mode = sys.argv[1]
    if mode == 'build':
        out = sys.argv[2]
        only = sys.argv[3:]
        for name, fn in BOARDS:
            if only and name not in only:
                continue
            open(os.path.join(out, name + '.dc.html'), 'w').write(fn())
            print('wrote', name)
    else:
        src, dst, proj = sys.argv[2:5]
        c = json.load(open(src))
        B, N = c['boards'], c['notes']
        if not any(p['id'] == PAGE for p in c['pages']):
            c['pages'].append({'id': PAGE, 'name': PAGE_NAME})
        c['launch'] = {'view': 'canvas', 'page': PAGE}
        N.setdefault('bshowto', {'fill': 'gray', 'page': PAGE, 'w': 400, 'x': -480, 'y': 0})
        N['bshowto']['text'] = HOWTO
        y = 0
        for key, text, boards in ROWS:
            N[key] = {'kind': 'title1', 'page': PAGE, 'w': 240, 'x': 0, 'y': y, 'text': text}
            by, x, bottom = y + 300, 0, y + 300
            for b in boards:
                w, h = size(proj, b)
                e = {'x': x, 'y': by, 'w': w, 'h': h, 'page': PAGE, 'title': TITLES[b]}
                if b in ('BS-Carousel', 'BS-Reels-Cards', 'BS-Imagery'):
                    e['is_interactive'] = True
                B[b + '.dc.html'] = e
                if b + '.dc.html' not in c['order']:
                    c['order'].append(b + '.dc.html')
                x += w + 120
                bottom = max(bottom, by + h)
            N[key]['maxW'] = min(8000, x - 120)
            y = bottom + 300
        json.dump(c, open(dst, 'w'), ensure_ascii=False)
        print('page', PAGE, 'laid out; ends at', y - 300)
