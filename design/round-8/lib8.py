"""Round 8 shared pieces: the new tab bar (Home, Learn, Hub, Community, Me), the three Hub icon
directions, and imports from Rounds 6 and 7 so every board speaks the Round 7 language
(Geist, Kalam for rare moments, corners 6/10/14 and a circle)."""
import os
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


def ic8(name, size=20, stroke='currentColor', sw=2):
    if name == 'hub':
        return hub_icon(None, size, stroke, sw)
    return ic(name, size, stroke, sw)


# ---------------------------------------------------------------- the Round 8 tab bar

AREAS8 = [('Home', 'pool'), ('Learn', 'moon'), ('Hub', 'hub'), ('Community', 'ripple'), ('Me', 'stones')]
ACTIVE8 = {
    'Home': (EVG, LIME, EVG),
    'Learn': (MINT, NIGHT, MOON),
    'Hub': (LIME, EVG, EVG),
    'Community': (BLUSH, BLUSH_INK, BLUSH_INK),
    'Me': (POOL, EVG, EVG),
}
PAGES8 = {'Home': 'R8-Home.dc.html', 'Learn': 'R8-Learn-Paths.dc.html', 'Hub': 'R8-Hub-Job.dc.html',
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


def with_css(html, css):
    """Add board-specific CSS to a page built by phone() or board7()."""
    return html.replace('</style>', css + '</style>', 1)
