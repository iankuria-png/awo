"""Round 8 shared pieces: the new tab bar (Home, Learn, Hub, Community, Me), the three Hub icon
directions, and imports from Rounds 6 and 7 so every board speaks the Round 7 language
(Geist, Kalam for rare moments, corners 6/10/14 and a circle)."""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
sys.path.insert(0, os.path.join(HERE, '..', 'round-7'))

from lib6 import *  # noqa: E402,F401,F403  (tokens, icon(), pool(), moon(), stones(), ola(), phone(), arc(), write())
from screens7 import ic, EXTRA_ICONS, switch, switch_js, mark, back, R_S, R_M, R_L, LINE7  # noqa: E402,F401
from kit7 import board7, chip7, PROVENANCE, ALERT  # noqa: E402,F401

HF = "font-family: '[[ handFont ]]', cursive"
NB = ' '

# ---------------------------------------------------------------- the Hub icon, three directions
# Drawn on the same 24 grid as the five shapes: 2px line, round ends. Each part carries a class so
# it can move once, meaningfully, when the tab is chosen (see HUB_CSS). The resting state is the
# drawing itself, so with reduce motion on the icon simply appears, complete.

HUB_PARTS = {
    # A keystone: the wedge that locks an arch, shown at the arch's crown. The Vault's arch moves into Learn;
    # its keystone becomes the Hub. The two halves draw first; the keystone drops in last and locks them.
    'keystone': [('kl', '<path pathLength="1" d="M2.00 20.50A10 10 0 0 1 9.75 10.76L11.25 15.15A5.4 5.4 0 0 0 6.60 20.50z"></path>'),
                 ('kl', '<path pathLength="1" d="M22.00 20.50A10 10 0 0 0 14.25 10.76L12.75 15.15A5.4 5.4 0 0 1 17.40 20.50z"></path>'),
                 ('ks', '<path d="M8.65 6.16L15.35 6.16L12.75 15.15L11.25 15.15z"></path>')],
    # A dial: tools that adjust to her numbers.
    'dial': [('dr', '<circle cx="12" cy="13.5" r="7"></circle>'),
             ('dt', '<path d="M4.4 9.1 3 8.3M12 4.7V3.1M19.6 9.1 21 8.3"></path>'),
             ('dp', '<path d="M12 13.5l3.6-3.6"></path>'),
             ('dc', '<circle cx="12" cy="13.5" r="1.3" fill="currentColor"></circle>')],
    # A market awning: things you do; open for business.
    'awning': [('aw', '<path d="M5.2 3.5h13.6l2.6 5.5H2.6z"></path><path d="M2.6 9a2.35 2.35 0 0 0 4.7 0 2.35 2.35 0 0 0 4.7 0 2.35 2.35 0 0 0 4.7 0 2.35 2.35 0 0 0 4.7 0"></path>'),
               ('ap', '<path pathLength="1" d="M4.6 12.2v8.3M19.4 12.2v8.3"></path>'),
               ('ap', '<path pathLength="1" d="M3 20.5h18"></path>')],
}

HUB_NAMES = {'keystone': 'Keystone', 'dial': 'Dial', 'awning': 'Market awning'}

# The icon the other Round 8 boards use until Ian picks one (Claude's recommendation).
HUB_KIND = 'keystone'

HUB_CSS = """
.hk .kl{stroke-dasharray:1.05 1.05;animation:draw .3s cubic-bezier(.2,.8,.2,1) both}
.hk .ks{transform-box:fill-box;transform-origin:50% 100%;animation:ksDrop .45s cubic-bezier(.2,.8,.2,1) .24s both}
.hd .dp{transform-box:view-box;transform-origin:12px 13.5px;animation:dialTurn .7s cubic-bezier(.2,.8,.2,1) both}
.hd .dt{animation:fadeIn .3s ease-out .35s both}
.ha .aw{transform-box:fill-box;transform-origin:50% 0;animation:unroll .45s cubic-bezier(.2,.8,.2,1) both}
.ha .ap{stroke-dasharray:1.05 1.05;animation:draw .34s cubic-bezier(.2,.8,.2,1) .32s both}
.lp.hk .ks{animation:ksLoop 3.6s cubic-bezier(.2,.8,.2,1) infinite}
.lp.hk .kl{animation:drawLoop 3.6s cubic-bezier(.2,.8,.2,1) infinite}
.lp.hd .dp{animation:dialLoop 3.6s cubic-bezier(.2,.8,.2,1) infinite}
.lp.hd .dt{animation:none}
.lp.ha .aw{animation:unrollLoop 3.6s cubic-bezier(.2,.8,.2,1) infinite}
.lp.ha .ap{animation:drawLoop 3.6s cubic-bezier(.2,.8,.2,1) infinite}
@keyframes ksDrop{from{transform:translateY(-70%);opacity:0}55%{opacity:1}to{transform:none;opacity:1}}
@keyframes draw{from{stroke-dashoffset:1.05}to{stroke-dashoffset:0}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes dialTurn{from{transform:rotate(-120deg)}70%{transform:rotate(8deg)}to{transform:none}}
@keyframes unroll{from{transform:scaleY(.08);opacity:.4}to{transform:none;opacity:1}}
@keyframes ksLoop{0%,8%{transform:translateY(-70%);opacity:0}22%{transform:none;opacity:1}84%{transform:none;opacity:1}96%,100%{transform:translateY(-70%);opacity:0}}
@keyframes drawLoop{0%{stroke-dashoffset:1.05}10%,84%{stroke-dashoffset:0}96%,100%{stroke-dashoffset:1.05}}
@keyframes dialLoop{0%{transform:rotate(-120deg)}16%{transform:rotate(8deg)}22%,84%{transform:none}100%{transform:rotate(-120deg)}}
@keyframes unrollLoop{0%{transform:scaleY(.08);opacity:.4}14%,84%{transform:none;opacity:1}96%,100%{transform:scaleY(.08);opacity:0}}
[data-calm="true"] *{animation:none!important;transition:none!important}
"""

HUB_ANIM = {'keystone': 'hk', 'dial': 'hd', 'awning': 'ha'}


def hub_icon(kind=None, size=20, stroke='currentColor', sw=2, anim=False, loop=False):
    """The Hub's icon. anim=True plays its one move when it appears; loop=True repeats it (boards only)."""
    kind = kind or HUB_KIND
    cls = ''
    if anim or loop:
        cls = f' class="{HUB_ANIM[kind]}{" lp" if loop else ""}"'
    parts = ''.join(f'<g class="{c}">{p}</g>' for c, p in HUB_PARTS[kind])
    return (f'<svg{cls} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; overflow: visible">{parts}</svg>')


EXTRA8 = {
    'ring': '<circle cx="12" cy="12" r="9.2"></circle><circle cx="12" cy="10" r="3"></circle><path d="M6.8 18.2a6.4 6.4 0 0 1 10.4 0"></path>',
    'grow': '<path d="M4 18l5-5 4 3 7-8"></path><path d="M15 8h5v5"></path>',
    'hexa': '<path d="M12 3l7.8 4.5v9L12 21l-7.8-4.5v-9z"></path><path d="M12 8.2l3.3 1.9v3.8L12 15.8l-3.3-1.9v-3.8z"></path>',
    'swap': '<path d="M4 8h15l-3.5-3.5"></path><path d="M20 16H5l3.5 3.5"></path>',
    'building': '<path d="M4.5 21V6l7.5-3v18"></path><path d="M12 8.5l7.5 2.5v10"></path><path d="M3 21h18"></path><path d="M8 9v.01M8 13v.01M8 17v.01M15.8 14v.01M15.8 17.5v.01"></path>',
    'speaker': '<path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"></path><path d="M15.5 9a4.2 4.2 0 0 1 0 6M18.2 6.5a8 8 0 0 1 0 11"></path>',
    'mic': '<rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0M12 18v3"></path>',
    'bookmark': '<path d="M6.5 3.5h11v17L12 16.5l-5.5 4z"></path>',
    'flag': '<path d="M5 21V4"></path><path d="M5 4.5h11.5l-2 4 2 4H5"></path>',
    'pause': '<path d="M8.5 5.5v13M15.5 5.5v13"></path>',
    'back15': '<path d="M4.5 12a7.5 7.5 0 1 0 2.2-5.3"></path><path d="M4 3.5v4h4"></path><path d="M10 10.5v5M13.2 10.5h2.8v1.8h-1.6a1.4 1.4 0 0 1 0 2.8h-1.2"></path>',
    'fwd15': '<path d="M19.5 12a7.5 7.5 0 1 1-2.2-5.3"></path><path d="M20 3.5v4h-4"></path><path d="M8.6 10.5v5M11.8 10.5h2.8v1.8H13a1.4 1.4 0 0 1 0 2.8h-1.2"></path>',
    'plus': '<path d="M12 5v14M5 12h14"></path>',
    'wifi-off': '<path d="M3 3l18 18"></path><path d="M8.5 16.4a5 5 0 0 1 7 0M5.2 13a9.6 9.6 0 0 1 5-2.6M13.8 10.5a9.6 9.6 0 0 1 5 2.5M2 9.6a14 14 0 0 1 4.4-2.8M11 5.6A14 14 0 0 1 22 9.6"></path><path d="M12 20h.01"></path>',
    'camera': '<path d="M4 8h3l1.8-2.5h6.4L17 8h3v11H4z"></path><circle cx="12" cy="13.3" r="3.4"></circle>',
    'upload': '<path d="M12 16V4M7 8.5l5-5 5 5"></path><path d="M5 20h14"></path>',
    'share': '<circle cx="6" cy="12" r="2.4"></circle><circle cx="17.5" cy="5.8" r="2.4"></circle><circle cx="17.5" cy="18.2" r="2.4"></circle><path d="M8.2 10.8l7.1-3.8M8.2 13.2l7.1 3.8"></path>',
    'whatsapp': '<path d="M4.5 20l1.2-4.2A8 8 0 1 1 8.6 18.8z"></path><path d="M9.2 8.6c-.3 1.6.8 3.8 2.6 5.2 1.4 1.1 2.8 1.4 3.5 1l.7-1.2-1.8-1-1 .8a5.4 5.4 0 0 1-2.8-2.8l.8-1-1-1.8z"></path>',
    'calc': '<rect x="5" y="3" width="14" height="18" rx="2"></rect><path d="M8 7h8M8 11h.01M12 11h.01M16 11h.01M8 14.5h.01M12 14.5h.01M16 14.5h.01M8 18h.01M12 18h.01M16 18v-.01"></path>',
    'eye-off': '<path d="M3 3l18 18"></path><path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7a13 13 0 0 1-2.7 3.6M6.4 6.5A13 13 0 0 0 2.5 12c1 2.5 4.5 7 9.5 7a9.6 9.6 0 0 0 4.3-1"></path><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"></path>',
    'more': '<path d="M5.5 12h.01M12 12h.01M18.5 12h.01"></path>',
    'reply': '<path d="M9.5 7 4.5 12l5 5"></path><path d="M4.5 12H14a5.5 5.5 0 0 1 5.5 5.5V19"></path>',
    'image': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"></rect><circle cx="9" cy="10" r="1.8"></circle><path d="M20.5 16l-5-5-8.5 8.5"></path>',
    'letter': '<path d="M6 3.5h9l3.5 3.5V20.5H6z"></path><path d="M9 11h6.5M9 14.5h6.5M9 18h4"></path>',
    'question': '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.6 2.6 0 0 1 5 .9c0 1.8-2.5 2.2-2.5 4"></path><path d="M12 17.3h.01"></path>',
    'note': '<path d="M4.5 5.5h15v10h-7l-4.5 4v-4H4.5z"></path>',
    'tag': '<path d="M3.5 12.5V4h8.5l8.5 8.5-8.5 8.5z"></path><circle cx="8" cy="8.5" r="1.4"></circle>',
    'list': '<path d="M9 6.5h11M9 12h11M9 17.5h11"></path><path d="M4.5 6.5h.01M4.5 12h.01M4.5 17.5h.01"></path>',
    'clock': '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>',
    'car': '<path d="M4 16.5V12l2-5h12l2 5v4.5"></path><path d="M3 16.5h18v2.5H3z"></path><circle cx="7.5" cy="14" r=".6"></circle><circle cx="16.5" cy="14" r=".6"></circle><path d="M6 12h12"></path>',
    'key': '<circle cx="8" cy="15" r="4"></circle><path d="M11 12l8-8M16 7l2.5 2.5M14 9l2 2"></path>',
    'plane': '<path d="M3 13.5l7-2.5 3.5-7 2 .5-1.5 6 5.5-2 1.5 1.5-17 8z"></path><path d="M4 20.5h16"></path>',
    'eye': '<path d="M2.5 12c1-2.5 4.5-7 9.5-7s8.5 4.5 9.5 7c-1 2.5-4.5 7-9.5 7s-8.5-4.5-9.5-7z"></path><circle cx="12" cy="12" r="3"></circle>',
    'school': '<path d="M2.5 9 12 4.5 21.5 9 12 13.5z"></path><path d="M6.5 11v5c1.5 1.5 3.5 2.2 5.5 2.2s4-.7 5.5-2.2v-5"></path><path d="M21.5 9v5"></path>',
}


def ic8(name, size=20, stroke='currentColor', sw=2):
    if name == 'hub':
        return hub_icon(None, size, stroke, sw)
    if name in EXTRA8:
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0">{EXTRA8[name]}</svg>')
    return ic(name, size, stroke, sw)


# Warnings on night use blush on a wine-dark ground (never red); on light grounds, wine on pale blush.
NWARN_BG, NWARN_FG = '#35202A', BLUSH
WARN_BG, WARN_FG = '#F7E6EC', BLUSH_2


# ---------------------------------------------------------------- the Round 8 tab bar

AREAS8 = [('Home', 'pool'), ('Learn', 'moon'), ('Hub', 'hub'), ('Community', 'ripple'), ('Me', 'stones')]
ACTIVE8 = {
    'Home': (EVG, LIME, EVG),
    'Learn': (MINT, NIGHT, MOON),
    'Hub': (LIME, EVG, EVG),
    'Community': (BLUSH, BLUSH_INK, BLUSH_INK),
    'Me': (POOL, EVG, EVG),
}
PAGES8 = {'Home': 'R8-Home.dc.html', 'Learn': 'R8-Learn.dc.html', 'Hub': 'R8-Hub.dc.html',
          'Community': 'R8-Feed.dc.html', 'Me': 'R7-Me.dc.html'}


def tabbar8(active, dark=False, kind=None, links=True):
    """The five tabs with the Hub in the centre. The active Hub icon plays its move once."""
    bg = DEEP if dark else '#FFFFFF'
    line = NLINE if dark else '#E1E8E4'
    idle = NMUTED if dark else MUTED
    out = [f'<nav aria-label="Main" class="tab" style="background: {bg}; border-top: 1px solid {line}; color: {idle}">']
    for name, icn in AREAS8:
        glyph = hub_icon(kind, 20, anim=(name == active)) if icn == 'hub' else icon(icn)
        tag = 'a' if links else 'span'
        href = f' href="{PAGES8[name]}"' if links else ''
        if name == active:
            pb, fg, lc = ACTIVE8[name]
            if dark and name == 'Learn':
                lc = MOON
            out.append(f'<{tag}{href} class="ti" aria-current="page" style="color: {lc}; font-weight: 600"><span class="tp" style="background: {pb}; color: {fg}">{glyph}</span>{name}</{tag}>')
        else:
            out.append(f'<{tag}{href} class="ti"><span class="tp">{glyph}</span>{name}</{tag}>')
    out.append('</nav>')
    return ''.join(out)


def nbs(text):
    """Keep amounts and their currency on one line: R\u00a0500, KSh\u00a012\u00a0000, 4\u00a0000."""
    text = re.sub(r'(R|KSh|P|N\$|£|₦) (?=\d)', lambda m: m.group(1) + NB, text)
    return re.sub(r'(?<=\d) (?=\d{3}(?!\d))', NB, text)


def nb_text(html):
    """Apply nbs() to the text between tags in a board's body only (never to attributes, CSS or scripts)."""
    head, rest = html.split('</helmet>', 1)
    body, tail = rest.split('<script type="text/x-dc"', 1)
    body = re.sub(r'>([^<]+)<', lambda m: '>' + nbs(m.group(1)) + '<', body)
    return head + '</helmet>' + body + '<script type="text/x-dc"' + tail


def with_css(html, css):
    """Add board-specific CSS to a page built by phone() or board7()."""
    return html.replace('</style>', css + '</style>', 1)
