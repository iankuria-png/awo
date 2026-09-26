"""Round 9 shared pieces. Round 9 connects what Rounds 7 and 8 built: the 30-day loop end to end, sharing,
help and search, the rest of the Hub tools, other channels and sizes, components, and the material around the
app (emails, print, social, merchandise). Everything is written natively in the Round 7 language and passed
through Round 7's transform, like Round 8.

Sample member: Naledi, employed in Johannesburg. Her fourth check-in is on 13 October 2026."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-8'))

from lib8 import *  # noqa: E402,F401,F403
from learn8 import PHONE_CSS  # noqa: E402,F401
from tools8 import (TOOL_CSS, REVIEWED, AI_CHIP, beat, means, learn_this, make_goal, foot, result,  # noqa: E402,F401
                    rands_js, fmt_r, tool_head)
from auth7 import title, primary, disabled, SR  # noqa: E402,F401
from marketing import canvas_board, device  # noqa: E402,F401
from brand7 import app_icon, lockup  # noqa: E402,F401

HF = "font-family: '[[ handFont ]]', cursive"

EXTRA8.update({
    'scale': '<path d="M12 4v16M7 20h10"></path><path d="M4.5 7.5h15"></path><path d="M4.5 7.5 2 13a2.6 2.6 0 0 0 5 0zM19.5 7.5 17 13a2.6 2.6 0 0 0 5 0z"></path>',
})

# Version 3 (13 Sep) and version 4 (13 Oct) of Naledi's DIVA profile. The score is the weighted sum of the four
# areas with the sample weights (40, 25, 20, 15): 63 then 64. The month that went down is version 4 after a car repair.
AREAS9 = [('Everyday money', 'Financial Health, 40%', 71, 71, 70),
          ('Ready for surprises', 'Risk and Resilience, 25%', 48, 53, 40),
          ('Knowing your options', 'Capital Positioning, 20%', 60, 60, 60),
          ('Clear goals', 'Goal Clarity, 15%', 69, 70, 69)]
SCORE_V3, SCORE_V4, SCORE_DOWN = 63, 64, 60

CSS9 = """
@keyframes toastIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes sheetIn{from{transform:translateY(100%)}to{transform:none}}
@keyframes dimIn{from{opacity:0}to{opacity:1}}
@keyframes countUp{from{opacity:.2;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes grow9{from{transform:scaleX(var(--from,0))}to{transform:scaleX(1)}}
.sheet{position:absolute;z-index:41;left:0;right:0;bottom:0;border-radius:14px 14px 0 0;background:#FFFFFF;box-shadow:0 -12px 40px rgba(16,24,20,.18);animation:sheetIn .32s cubic-bezier(.2,.8,.2,1) both}
.dim{position:absolute;z-index:40;inset:0;background:rgba(11,15,14,.45);animation:dimIn .2s ease-out both}
.toast{position:absolute;z-index:42;left:16px;right:16px;bottom:100px;border-radius:10px;background:#101814;color:#FFFFFF;padding:12px 14px;display:flex;align-items:center;gap:10px;font-size:15px;box-shadow:0 12px 32px rgba(16,24,20,.28);animation:toastIn .3s cubic-bezier(.2,.8,.2,1) both}
.row9{min-height:56px;display:flex;align-items:center;gap:12px}
.seg9{display:flex;gap:4px;padding:4px;border-radius:10px;background:#EEF3F0}
.hscroll::-webkit-scrollbar{display:none}
.seg9 button{flex:1 1 0;height:40px;border-radius:8px;font-size:14px;font-weight:600;transition:background-color .18s,color .18s}
"""

# Area colours, used to tag results by where they live (search, notifications, the flow board).
AREA_TAG = {'Home': (EVG, LIME, 'pool'), 'Learn': (NIGHT, MOON, 'moon'), 'Words': (MINT, NIGHT, 'arch'), 'Hub': (LIME, EVG, 'hub'),
            'Community': (BLUSH, BLUSH_INK, 'ripple'), 'Me': (POOL, EVG, 'stones'), 'Help': ('#DCE4DF', EVG, 'question')}


def area_badge(area, size=40, radius=R_M):
    bg, fg, g = AREA_TAG[area]
    glyph = hub_icon(None, round(size * .5), fg) if g == 'hub' else (icon(g, round(size * .5), fg) if g in ('pool', 'moon', 'arch', 'ripple', 'stones') else ic8(g, round(size * .5), fg))
    return (f'<span aria-hidden="true" style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: {radius}px; background: {bg}; '
            f'display: flex; align-items: center; justify-content: center">{glyph}</span>')


def app_badge(size=36):
    """AWO's app icon at notification size: the three stones on evergreen."""
    s = round(size * .62)
    return (f'<span aria-hidden="true" style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: {round(size * .28)}px; background: {EVG}; display: flex; align-items: center; justify-content: center">'
            f'{mark(s, "#FFFFFF", LIME)}</span>')


def head9(back_href, title_text, right='', back_label='Back'):
    right = right or '<span style="width: 44px"></span>'
    return (f'<header style="display: flex; align-items: center; justify-content: space-between; gap: 12px">{back(back_href, back_label)}'
            f'<span style="font-size: 17px; font-weight: 600">{title_text}</span>{right}</header>')


def icon_btn(g, label, href=None, hole=None, bg='#FFFFFF', fg=INK, extra=''):
    inner = ic8(g, 20, fg, 2)
    style = f'width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center; position: relative'
    if href:
        return f'<a href="{href}" aria-label="{label}" style="{style}">{inner}{extra}</a>'
    return f'<button onClick="[[ {hole} ]]" aria-label="{label}" style="{style}">{inner}{extra}</button>'


def page9(title_text, body, logic, h=844, tab=None, bg=MIST, dark=False, css='', scr_style='gap: 16px'):
    """A phone board. With a tab, the Round 8 tab bar sits at the bottom; without, the screen runs full height."""
    if tab:
        inner = f'  <div class="scr" style="{scr_style}">\n{body}\n  </div>\n  {tabbar8(tab, dark=dark)}'
    else:
        inner = f'  <div class="scr" style="bottom: 0; padding-bottom: 24px; {scr_style}">\n{body}\n  </div>'
    return with_css(phone(title_text, inner, logic, h=h, bg=bg, dark=dark), PHONE_CSS + HUB_CSS + TOOL_CSS + CSS9 + css)


def free_page(title_text, inner, logic, h=844, bg=MIST, dark=False, css=''):
    """A phone board whose layout is all its own (lock screens, full-bleed moments)."""
    return with_css(phone(title_text, inner, logic, h=h, bg=bg, dark=dark), PHONE_CSS + HUB_CSS + TOOL_CSS + CSS9 + css)


def static_logic9(extra=''):
    return 'class Component extends DCLogic {\n  renderVals() { return { %s }; }\n}' % extra


def stones_svg(n_done, w=320, h=120, new_last=False, dark=False):
    """n stepping stones rising left to right; the last one lime when new_last."""
    rx = min(w / (n_done * 3.1), 90)
    ry, sw, dy = rx * .38, max(1.2, rx * .1), rx * .23
    pts = []
    for i in range(n_done):
        x = rx + 2 + i * (w - 2 * rx - 4) / max(1, n_done - 1) if n_done > 1 else w / 2
        y = h - ry - dy - 2 - i * (h - 2 * ry - dy - 4) / max(1, n_done - 1) if n_done > 1 else h / 2
        pts.append((round(x), round(y)))
    out = ''
    for i, (x, y) in enumerate(pts):
        last = new_last and i == n_done - 1
        fill = LIME if last else (MOON if dark else EVG)
        shadow = '#2E3A36' if dark else '#BFD9D2'
        anim = f' style="animation: pop .6s cubic-bezier(.34,1.56,.64,1) {0.25 + i * 0.12:.2f}s both; transform-box: fill-box; transform-origin: center"'
        out += (f'<ellipse cx="{x}" cy="{y + dy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{shadow}"></ellipse>'
                f'<ellipse cx="{x}" cy="{y}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" stroke="{EVG if not dark else MOON}" stroke-width="{sw:.1f}"{anim}></ellipse>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; overflow: visible">{out}</svg>'
