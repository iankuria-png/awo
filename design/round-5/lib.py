# Shared pieces for the Round 5 boards (design language: pool, moon, arch, ripple, stones).
# Output is .dc.html for the Design canvas. DC holes ({{ x }}) are written literally.

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800'
         '&amp;family=Geist:wght@300..700&amp;display=swap" rel="stylesheet">')

# Colour tokens
EVG, EVG_D, LIME, BLUSH, BLUSH_INK, BLUSH_2 = '#0F4A36', '#0A3326', '#D8F36A', '#FFC7D6', '#2A0F18', '#6B2B40'
MIST, POOL, INK, SEC, MUTED, LINE = '#EEF3F0', '#D3E8E4', '#101814', '#3F4B45', '#56625C', '#DCE4DF'
NIGHT, DEEP, RAISED, NLINE, MOON, NMUTED, MINT, IRIS = '#0B0F0E', '#151B19', '#1C2421', '#2E3A36', '#F2F1EC', '#9AA39F', '#86E3C4', '#A99BFF'
ON_EVG = '#BFDCCF'

# Photos already in the canvas asset store (nappy.co, CC0 stand-ins)
IMG = {
    'naledi': '/_blob/a1c6d27055f330029a50e20d5163113f',
    'naledi_table': '/_blob/6c931acfd633d8490000e4f4faa1b8a6',
    'wanjiru': '/_blob/18c9f6030b6eabb32eba39b3c6825506',
    'wanjiru_stall': '/_blob/46d15728a12cc0a992dfc48cf3f11362',
    'amara': '/_blob/1708e7afa42863658d9439e542a15a5c',
    'thandi': '/_blob/f8021d36aaa6e41b5716f012f39438cb',
    'grace': '/_blob/876a6c76dcee466c2a8bb01c6c3a3d7d',
    'lindiwe': '/_blob/87835fd30cadd081b87b7e4942e8d0f0',
    'zodwa': '/_blob/343a6db78dab25ba6b74287530e953d6',
}

BASE_CSS = """
body{margin:0;font-family:'Geist',ui-sans-serif,system-ui,sans-serif;color:#101814}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit;padding:0;margin:0}
button:focus-visible{outline:2px solid #0F4A36;outline-offset:3px}
.dk button:focus-visible{outline-color:#86E3C4}
h1,h2,h3,p{margin:0}
.d{font-family:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif;font-weight:800;font-stretch:82%;letter-spacing:-0.03em;line-height:.9}
.ph{position:relative;width:390px;height:844px;border-radius:44px;overflow:hidden;flex-shrink:0;box-shadow:0 0 0 1px rgba(16,24,20,.16)}
.scr{position:absolute;left:0;right:0;top:0;bottom:84px;box-sizing:border-box;padding:52px 20px 16px;display:flex;flex-direction:column;gap:12px}
.tab{position:absolute;left:0;right:0;bottom:0;height:84px;box-sizing:border-box;padding:8px 8px 18px;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));font-size:12px;text-align:center}
.ti{display:flex;flex-direction:column;align-items:center;gap:4px}
.tp{width:52px;height:30px;border-radius:999px;display:flex;align-items:center;justify-content:center}
.pill{height:52px;border-radius:999px;font-size:16px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;width:100%}
.chip{height:28px;padding:0 11px;border-radius:999px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:6px;white-space:nowrap}
.face{border-radius:999px;object-fit:cover;display:block}
.wave{animation:waveX 3.2s linear infinite}
.blink{transform-box:fill-box;transform-origin:center;animation:blink 4.2s ease-in-out infinite}
.drop{position:absolute;width:9px;height:13px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:#D8F36A;animation:drop .8s cubic-bezier(.5,0,.8,.4) both}
.splash{position:absolute;border:2px solid #D8F36A;border-radius:50%;animation:splash .9s .55s cubic-bezier(.2,.8,.2,1) both}
.rp{position:absolute;border-radius:999px;border:2px solid currentColor;animation:rp 1s cubic-bezier(.2,.8,.2,1) both}
.flipper{position:relative;height:100%;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.34,1.3,.64,1)}
.face-f,.face-b{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden}
.face-b{transform:rotateY(180deg)}
.jump{animation:jump .9s cubic-bezier(.2,.8,.2,1) both;transform-origin:50% 90%}
@keyframes waveX{to{transform:translateX(-56px)}}
@keyframes blink{0%,91%,100%{transform:scaleY(1)}94%{transform:scaleY(.08)}}
@keyframes drop{0%{transform:translateY(-70px);opacity:0}25%{opacity:1}100%{transform:translateY(0);opacity:0}}
@keyframes splash{from{transform:scale(.3);opacity:1}to{transform:scale(1.5);opacity:0}}
@keyframes rp{from{transform:scale(1);opacity:.7}to{transform:scale(2.1);opacity:0}}
@keyframes jump{0%,100%{transform:translateY(0) scale(1,1)}14%{transform:translateY(0) scale(1.14,.86)}36%{transform:translateY(-26px) scale(.9,1.12)}52%{transform:translateY(-30px) scale(1,1)}70%{transform:translateY(0) scale(1.12,.88)}84%{transform:translateY(0) scale(.97,1.03)}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
@keyframes pulse{0%,100%{transform:scale(1);opacity:.5}50%{transform:scale(1.06);opacity:.9}}
@keyframes spread{from{transform:scale(.6);opacity:.55}to{transform:scale(1.35);opacity:0}}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.drop,.splash,.rp{display:none}}
"""


def icon(name, size=20, stroke='currentColor', sw=2):
    paths = {
        'pool': '<rect x="6.5" y="2.5" width="11" height="19" rx="5.5"></rect><path d="M6.5 13.5c1.8-1.3 3.7-1.3 5.5 0s3.7 1.3 5.5 0"></path>',
        'moon': '<path d="M20 15.5A8.5 8.5 0 1 1 8.5 4 6.5 6.5 0 0 0 20 15.5z"></path>',
        'arch': '<path d="M5.5 21V11a6.5 6.5 0 0 1 13 0v10"></path><path d="M3 21h18"></path>',
        'ripple': '<circle cx="12" cy="12" r="2.2"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="9.6" stroke-opacity=".45"></circle>',
        'stones': '<ellipse cx="5.6" cy="18.4" rx="3.4" ry="1.9"></ellipse><ellipse cx="12" cy="13.4" rx="3.8" ry="2.1"></ellipse><ellipse cx="18.4" cy="8" rx="3.6" ry="2.1"></ellipse>',
        'search': '<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>',
        'send': '<path d="M5 12h13M13 6l6 6-6 6"></path>',
        'check': '<path d="m5 12.5 4.5 4.5L19 7.5"></path>',
        'gear': '<circle cx="12" cy="12" r="3"></circle><path d="M12 2.8v2.4M12 18.8v2.4M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M2.8 12h2.4M18.8 12h2.4M4.9 19.1l1.7-1.7M17.4 6.6l1.7-1.7"></path>',
        'play': '<path d="M8 5.5v13l10.5-6.5z" fill="currentColor"></path>',
        'lock': '<rect x="5" y="11" width="14" height="10" rx="2"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>',
        'chev': '<path d="m9 6 6 6-6 6"></path>',
        'flip': '<path d="M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3"></path><path d="M18 3v4h-4M6 21v-4h4"></path>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0">{paths[name]}</svg>')


AREAS = [('Home', 'pool'), ('Learn', 'moon'), ('Vault', 'arch'), ('Community', 'ripple'), ('Me', 'stones')]
# Active tab: (pill background, icon colour, label colour) per area
ACTIVE = {
    'Home': (EVG, LIME, EVG),
    'Learn': (MINT, NIGHT, MOON),
    'Vault': (LIME, EVG, EVG),
    'Community': (BLUSH, BLUSH_INK, BLUSH_INK),
    'Me': (POOL, EVG, EVG),
}


def tabbar(active, dark=False, bg=None, line=None):
    bg = bg or (DEEP if dark else '#FFFFFF')
    line = line or (NLINE if dark else '#E1E8E4')
    idle = NMUTED if dark else MUTED
    out = [f'<nav aria-label="Main" class="tab" style="background: {bg}; border-top: 1px solid {line}; color: {idle}">']
    for name, ic in AREAS:
        if name == active:
            pb, fg, lc = ACTIVE[name]
            out.append(f'<span class="ti" aria-current="page" style="color: {lc}; font-weight: 600"><span class="tp" style="background: {pb}; color: {fg}">{icon(ic)}</span>{name}</span>')
        else:
            out.append(f'<span class="ti"><span class="tp">{icon(ic)}</span>{name}</span>')
    out.append('</nav>')
    return ''.join(out)


def ola_defs(p):
    return (f'<radialGradient id="{p}Body" cx="40%" cy="34%" r="68%"><stop offset="0" stop-color="#F2FFF9"></stop><stop offset="0.22" stop-color="#C9F6E6"></stop>'
            f'<stop offset="0.55" stop-color="#86E3C4"></stop><stop offset="0.9" stop-color="#A99BFF"></stop><stop offset="1" stop-color="#B7A9FF"></stop></radialGradient>'
            f'<radialGradient id="{p}Rim" cx="50%" cy="50%" r="50%"><stop offset="0.8" stop-color="#FFC7D6" stop-opacity="0"></stop><stop offset="0.97" stop-color="#FFC7D6" stop-opacity="0.5"></stop>'
            f'<stop offset="1" stop-color="#FFC7D6" stop-opacity="0"></stop></radialGradient>'
            f'<radialGradient id="{p}Bounce" cx="68%" cy="86%" r="40%"><stop offset="0" stop-color="#FFC7D6" stop-opacity="0.55"></stop><stop offset="1" stop-color="#FFC7D6" stop-opacity="0"></stop></radialGradient>')


def ola(p, size, happy=False, look=0):
    body = (f'<circle cx="120" cy="124" r="78" fill="url(#{p}Body)"></circle><circle cx="120" cy="124" r="78" fill="url(#{p}Bounce)"></circle>'
            f'<circle cx="120" cy="124" r="78" fill="url(#{p}Rim)"></circle>')
    if happy:
        eyes = '<path d="M96 130q8-14 16 0M128 130q8-14 16 0" fill="none" stroke="#0B1A16" stroke-width="7" stroke-linecap="round"></path>'
    else:
        eyes = (f'<g transform="translate({look} 0)"><g class="blink"><rect x="98" y="107" width="14" height="32" rx="7" fill="#0B1A16"></rect>'
                f'<rect x="128" y="107" width="14" height="32" rx="7" fill="#0B1A16"></rect></g></g>')
    return f'<svg width="{size}" height="{size}" viewBox="36 40 168 168" aria-hidden="true" style="display: block; overflow: visible">{body}{eyes}</svg>'


def moon(size, phase, now=False, lit=MOON, dark=RAISED, craters=False):
    """phase: 'full', 'half' (right half lit), 'new' (outline), 'cres' (thin crescent)."""
    parts = []
    if phase == 'full':
        parts.append(f'<circle cx="50" cy="50" r="46" fill="{lit}"></circle>')
    elif phase == 'half':
        parts.append(f'<circle cx="50" cy="50" r="46" fill="{dark}"></circle><path d="M50 4a46 46 0 0 1 0 92z" fill="{lit}"></path>')
    elif phase == 'cres':
        parts.append(f'<circle cx="50" cy="50" r="46" fill="{dark}"></circle><path d="M50 4a46 46 0 0 1 0 92a30 46 0 0 0 0-92z" fill="{lit}"></path>')
    else:
        parts.append(f'<circle cx="50" cy="50" r="45" fill="none" stroke="{lit}" stroke-opacity="0.45" stroke-width="3"></circle>')
    if craters and phase in ('full', 'half'):
        parts.append('<circle cx="68" cy="34" r="7" fill="#E1E0D5"></circle><circle cx="74" cy="62" r="5" fill="#E1E0D5"></circle><circle cx="60" cy="78" r="3.5" fill="#E1E0D5"></circle>')
    if now:
        parts.append(f'<circle cx="50" cy="50" r="49" fill="none" stroke="{MINT}" stroke-width="3"></circle>')
    return f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true" style="display: block; flex-shrink: 0; overflow: visible">{"".join(parts)}</svg>'


def pool(w, h, clip, water=POOL, wave=LIME, vessel=EVG_D, rim=LIME, rimw=3, static=False, hole='waterY', label='poolLabel'):
    """A capsule vessel whose water level follows the {{ waterY }} hole (px from the top)."""
    n = int((w + 72) / 28) + 1
    crest = 'q14-8 28 0' + ' t28 0' * n
    wavecls = '' if static else ' class="wave"'
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{{{{ {label} }}}}" style="display: block; overflow: visible">'
            f'<defs><clipPath id="{clip}"><rect x="0" y="0" width="{w}" height="{h}" rx="{w / 2}"></rect></clipPath></defs>'
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="{w / 2}" fill="{vessel}"></rect>'
            f'<g clip-path="url(#{clip})"><g style="transform: translateY({{{{ {hole} }}}}px); transition: transform .6s cubic-bezier(.34,1.56,.64,1)">'
            f'<g{wavecls}><path d="M-4 0{crest}V{h + 40}H-4z" fill="{water}"></path>'
            f'<path d="M-4 0{crest}" fill="none" stroke="{wave}" stroke-width="3"></path></g></g></g>'
            f'<rect x="{rimw / 2}" y="{rimw / 2}" width="{w - rimw}" height="{h - rimw}" rx="{(w - rimw) / 2}" fill="none" stroke="{rim}" stroke-width="{rimw}"></rect></svg>')


def stones(w, h, pts, fills, strokes, dash=None):
    """pts: list of (cx, cy, rx, ry)."""
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; overflow: visible">']
    for i, (cx, cy, rx, ry) in enumerate(pts):
        d = f' stroke-dasharray="{dash}"' if (dash and fills[i] == 'none') else ''
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fills[i]}" stroke="{strokes[i]}" stroke-width="2.5"{d}></ellipse>')
    out.append('</svg>')
    return ''.join(out)


def board(title_html, desc, labels_bg, phones, width, height, bg, logic, fg=INK, desc_col=SEC, extra_defs=''):
    heads = ''.join(
        f'<div style="display: flex; flex-direction: column; gap: 14px; width: 390px">'
        f'<span style="display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600; color: {fg}">{icon(ic, 18)}{name}</span>{ph}</div>'
        for (name, ic), ph in zip(AREAS, phones))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title_html}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{BASE_CSS}
body{{background:{bg}}}
</style>
</helmet>
<div style="position: relative; width: {width}px; height: {height}px; box-sizing: border-box; padding: 56px; background: {bg}; color: {fg}; display: flex; flex-direction: column; gap: 36px">
  <svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs>{extra_defs}</defs></svg>
  <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
    <div style="display: flex; flex-direction: column; gap: 12px">
      <h1 class="d" style="font-size: 64px">{title_html}</h1>
      <p style="max-width: 1100px; font-size: 19px; line-height: 1.45; color: {desc_col}">{desc}</p>
    </div>
    <span style="flex-shrink: 0; font-size: 14px; font-weight: 500; color: {desc_col}; padding: 7px 14px; border: 1px dashed {desc_col}; border-radius: 999px">Sample content. Try tapping.</span>
  </header>
  <div style="display: flex; gap: 32px">{heads}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{width},"height":{height}}}}}'>
{logic}
</script>
</body>
</html>
'''


LOGIC = """class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const moved = !!st.moved, flipped = !!st.flipped, cheered = !!st.cheered, ola = !!st.ola;
    const amount = moved ? 1900 : 1800;
    const fmt = (n) => 'R ' + String(n).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' ');
    const H = %(poolH)s;
    return {
      moved, notMoved: !moved, amountText: fmt(amount),
      waterY: Math.round(H * (1 - amount / 5000)),
      poolLabel: 'Safety net pool: ' + fmt(amount) + ' of R 5 000',
      doMove: () => this.setState({ moved: true }),
      undoMove: () => this.setState({ moved: false }),
      flipTf: flipped ? 'rotateY(180deg)' : 'rotateY(0deg)',
      flipped, notFlipped: !flipped,
      frontTab: flipped ? -1 : 0, backTab: flipped ? 0 : -1,
      doFlip: () => this.setState({ flipped: !flipped }),
      cheered, notCheered: !cheered, cheerCount: cheered ? 25 : 24,
      cheerLabel: cheered ? 'Cheered' : 'Cheer',
      cheerBg: cheered ? '%(cheerOn)s' : '%(cheerOff)s', cheerFg: cheered ? '%(cheerOnFg)s' : '%(cheerOffFg)s',
      doCheer: () => this.setState({ cheered: !cheered }),
      ola, olaIdle: !ola,
      doOla: () => this.setState({ ola: !ola })
    };
  }
}"""
