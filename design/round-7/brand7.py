"""Round 7 brand boards, from Round 2's wordmark, icon and motion boards and Round 6's foundations:
R7-Brand (mark, wordmark, app icon A), R7-Icons, R7-Motion (M1 to M6, live) and R7-Foundations."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, EXTRA_ICONS, switch, switch_js, mark, R_S, R_M, R_L, LINE7  # noqa: E402
from kit7 import board7  # noqa: E402
from foundations import AREA_INFO, FOUND_CSS_KEYS  # noqa: E402

HF = "font-family: '[[ handFont ]]', cursive"


def app_icon(size, mask='square'):
    """App icon A (D-031): two stones she has stood on, and the next one, dashed."""
    r = {'square': round(size * .22), 'circle': size // 2, 'r7': round(size * .14)}[mask]
    art = (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">'
           f'<ellipse cx="28" cy="72" rx="15" ry="6.5" fill="{EVG_D}"></ellipse><ellipse cx="28" cy="69" rx="15" ry="6.5" fill="{LIME}"></ellipse>'
           f'<ellipse cx="52" cy="55" rx="16" ry="7" fill="{EVG_D}"></ellipse><ellipse cx="52" cy="52" rx="16" ry="7" fill="{LIME}"></ellipse>'
           f'<ellipse cx="75" cy="36" rx="14" ry="6.5" fill="none" stroke="{LIME}" stroke-width="3" stroke-dasharray="4 4"></ellipse></svg>')
    return f'<span role="img" aria-label="AWO app icon" style="width: {size}px; height: {size}px; border-radius: {r}px; background: {EVG}; display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0">{art}</span>'


def lockup(size, col, accent, stacked=False):
    word = f'<span style="font-size: {size}px; font-weight: 600; letter-spacing: -0.055em; line-height: .9; color: {col}">awo</span>'
    m = mark(round(size * 1.25), col, accent)
    if stacked:
        return f'<span style="display: inline-flex; flex-direction: column; align-items: center; gap: {round(size * .2)}px">{m}{word}</span>'
    return f'<span style="display: inline-flex; align-items: center; gap: {round(size * .28)}px">{m}{word}</span>'


# ---------------------------------------------------------------- Brand

def brand():
    grounds = [(EVG, '#FFFFFF', LIME, 'On evergreen'), (MIST, EVG, LIME, 'On mist'), (LIME, EVG, '#FFFFFF', 'On lime'), (NIGHT, MOON, LIME, 'On night')]
    tiles = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 150px; border-radius: {R_L}px; background: {bg}; display: flex; align-items: center; justify-content: center; {"box-shadow: inset 0 0 0 1px #C9D3CE;" if bg == MIST else ""}">{lockup(48, fg, ac)}</div><span style="font-size: 13px; color: {MUTED}">{n}</span></div>'
                    for bg, fg, ac, n in grounds)
    sizes = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px">{app_icon(s)}<span style="font-size: 12px; color: {MUTED}">{s}</span></span>' for s in (96, 64, 48, 32))
    masks = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px">{app_icon(120, m)}<span style="font-size: 13px; color: {MUTED}">{n}</span></span>'
                    for m, n in [('square', 'Rounded square'), ('circle', 'Circle mask'), ('r7', 'In the app, 14%')])
    marks = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px"><span style="height: 40px; display: flex; align-items: center">{mark(s, EVG, LIME)}</span><span style="font-size: 12px; color: {MUTED}">{s}px</span></span>' for s in (56, 40, 28, 20))
    body = f'''<div style="display: grid; grid-template-columns: 560px minmax(0, 1fr); gap: 24px; align-items: start">
    <section class="card" style="gap: 24px">
      <span class="ktitle">App icon A: stepping stones</span>
      <div style="display: flex; gap: 24px; align-items: flex-end">{app_icon(300)}<div style="display: flex; flex-direction: column; gap: 14px; align-items: center">{sizes}</div></div>
      <div style="display: flex; gap: 20px; justify-content: space-between">{masks}</div>
      <span class="knote">Two stones she has stood on and the next one, dashed. It is the Me shape, so the icon means "where you stand, and the next step". Chosen in Round 6 (D-031). No letters, so nothing to translate, and it survives every mask.</span>
    </section>
    <div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card" style="gap: 20px">
        <span class="ktitle">The wordmark, in Geist</span>
        <div style="display: flex; gap: 40px; align-items: center; padding: 12px 0">{lockup(120, EVG, LIME)}<span style="width: 1px; align-self: stretch; background: {LINE7}"></span>{lockup(56, EVG, LIME, stacked=True)}</div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px">{tiles}</div>
        <span class="knote">Lowercase awo in Geist 600 with tight tracking, beside the mark. It is a working lockup: the wordmark itself is still open (Q-25). Lime is only the next stone, and only on evergreen, night or mist.</span>
      </section>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px">
        <section class="card">
          <span class="ktitle">The mark, small</span>
          <div style="display: flex; gap: 22px; align-items: flex-end">{marks}</div>
          <span class="knote">Below 20px the stones merge, so the mark stops there. Clear space all round is one stone's height.</span>
        </section>
        <section class="card">
          <span class="ktitle">The voice, in two faces</span>
          <span class="d" style="font-size: 40px">Know where you stand.</span>
          <span class="hand" style="font-size: 30px; color: {EVG}; {HF}">Here's where you start.</span>
          <span class="knote">Geist says what is true. The hand says it warmly, once, at a moment that matters (the rules are on the type board). Switch the hand in Tweaks.</span>
        </section>
      </div>
    </div>
  </div>'''
    return board7('Brand', 'The mark, the wordmark and the app icon, carried from Round 2 into Round 7: Geist, the stepping stones, and lime for the next step.', body, static_logic(), 1600, 1040)


# ---------------------------------------------------------------- Icons

UI_ICONS = [('search', 'Search'), ('send', 'Send'), ('check', 'Done'), ('back', 'Back'), ('close', 'Close'), ('chev', 'Open'),
            ('flip', 'Flip'), ('lock', 'Private'), ('gear', 'Settings'), ('bell', 'Reminder'), ('heart', 'Cheer'), ('people', 'Buddy'),
            ('shield', 'Evidence'), ('pin', 'Stored in SA'), ('download', 'Download'), ('shop', 'Business'), ('doc', 'Payslip'), ('home', 'Send home'),
            ('down', 'Debt'), ('text', 'Text size'), ('motion', 'Motion'), ('calendar', 'Check-in date'), ('info', 'Why this'), ('play', 'Play')]

EXTRA_ICONS.update({
    'calendar': '<rect x="4" y="5.5" width="16" height="14.5" rx="2"></rect><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"></path>',
    'info': '<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5.5M12 7.8h.01"></path>',
})


def icons():
    shapes = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px">
        <span style="height: 120px; border-radius: {R_L}px; background: {bg}; color: {sh}; display: flex; align-items: center; justify-content: center; {"box-shadow: inset 0 0 0 1px #C9D3CE;" if bg == POOL else ""}">{icon(icn, 56, sh, 1.6)}</span>
        <span style="font-size: 15px; font-weight: 600">{n}</span><span class="knote">{m}</span></div>''' for n, bg, _fg, sh, icn, _hx, m, _mv in AREA_INFO)
    grid = ''.join(f'<div style="height: 96px; border-radius: {R_M}px; background: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px">{ic(n, 24, INK)}<span style="font-size: 12px; color: {MUTED}">{t}</span></div>' for n, t in UI_ICONS)
    sizes = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px">{icon("arch", s, EVG, sw)}<span style="font-size: 12px; color: {MUTED}">{s}, {sw}px</span></span>' for s, sw in [(16, 2), (20, 2), (24, 2), (32, 1.8), (48, 1.6)])
    tiles = ''.join(f'<span style="width: 44px; height: 44px; border-radius: {R_M}px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic(n, 22)}</span>'
                    for n, bg, fg in [('pool', LIME, EVG), ('shop', MIST, EVG), ('people', BLUSH, BLUSH_INK), ('stones', POOL, EVG), ('moon', NIGHT, MOON), ('arch', LIME, EVG)])
    body = f'''<section class="card">
      <span class="ktitle">The five shapes are the tab icons</span>
      <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">{shapes}</div>
    </section>
    <div style="display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); gap: 24px; align-items: start">
      <section class="card" style="background: {MIST}">
        <span class="ktitle">Everything else, one line</span>
        <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 10px">{grid}</div>
      </section>
      <div style="display: flex; flex-direction: column; gap: 24px">
        <section class="card">
          <span class="ktitle">Sizes</span>
          <div style="display: flex; gap: 24px; align-items: flex-end">{sizes}</div>
          <span class="knote">Drawn on a 24 grid with round ends. The stroke thins a little as icons grow, so they weigh the same as Geist beside them.</span>
        </section>
        <section class="card">
          <span class="ktitle">In a tile</span>
          <div style="display: flex; gap: 10px; flex-wrap: wrap">{tiles}</div>
          <span class="knote">A 44px tile with 10px corners, in the colour of what it opens. Only the play button and the cheer heart are filled.</span>
        </section>
        <section class="card">
          <span class="ktitle">Why not hand-drawn</span>
          <span class="knote">Round 2 drew the icons by hand. In Round 7 the hand is kept for people's words, so icons stay geometric and never compete with it.</span>
        </section>
      </div>
    </div>'''
    return board7('Icons', 'One family of line icons: the five area shapes lead, and every other icon is drawn the same way.', body, static_logic(), 1600, 1130)


# ---------------------------------------------------------------- Motion

MOTION_CSS = f"""
.mv *{{animation-play-state:var(--play,running)}}
@keyframes tapRing{{from{{transform:scale(.2);opacity:.55}}to{{transform:scale(3.2);opacity:0}}}}
@keyframes burst{{0%{{transform:translate(0,0) scale(.4);opacity:1}}100%{{transform:translate(var(--dx),var(--dy)) scale(1);opacity:0}}}}
@keyframes slideIn{{from{{transform:translateX(60px);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes dot{{0%,20%{{transform:translateX(0)}}50%,70%{{transform:translateX(var(--run))}}100%{{transform:translateX(0)}}}}
"""


def motion():
    def card(n, t, d, demo, dark=False):
        bg = NIGHT if dark else '#FFFFFF'
        fg = MOON if dark else INK
        sub = NMUTED if dark else MUTED
        return f'''<section class="card" style="background: {bg}; color: {fg}; padding: 20px">
        <div style="height: 220px; border-radius: {R_M}px; background: {RAISED if dark else MIST}; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center">{demo}</div>
        <span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; font-weight: 600; color: {sub}">{n}</span><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">{t}</span><span style="font-size: 14px; line-height: 1.45; color: {sub}">{d}</span></span>
      </section>'''
    m1 = f'''<button class="press" onClick="[[ tap ]]" style="position: relative; overflow: hidden; height: 56px; width: 220px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600">
          <sc-if value="[[ tapped ]]" hint-placeholder-val="[[ false ]]"><span aria-hidden="true" style="position: absolute; left: [[ tx ]]px; top: [[ ty ]]px; width: 40px; height: 40px; margin: -20px 0 0 -20px; border-radius: 999px; background: {LIME}; animation: tapRing .6s cubic-bezier(.2,.8,.2,1) both"></span></sc-if><span style="position: relative">Continue</span></button>'''
    m2 = f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 12px"><sc-if value="[[ ringOn ]]" hint-placeholder-val="[[ true ]]"><div role="img" aria-label="Day 12 of 30" style="position: relative; width: 120px; height: 120px">{arc(120, 40, '#DCE4DF', EVG, sw=10)}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; animation: rise .6s cubic-bezier(.2,.8,.2,1) .3s both"><span style="font-size: 36px; font-weight: 600; letter-spacing: -0.04em">12</span><span style="font-size: 12px; color: {MUTED}">of 30 days</span></span></div></sc-if>
          <button onClick="[[ replay ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: #FFFFFF; font-size: 14px; font-weight: 600">Open the screen again</button></div>'''
    dots = ''.join(f'<span style="width: 12px; height: 12px; border-radius: 999px; background: {MINT}; animation: pulse 1.2s ease-in-out {d}s infinite"></span>' for d in (0, .2, .4))
    m3 = f'<div style="display: flex; flex-direction: column; align-items: center; gap: 14px"><span style="width: 72px; height: 72px; border-radius: 999px; background: radial-gradient(circle at 35% 30%, {MINT}, #2E8F75 70%); box-shadow: 0 0 40px rgba(134,227,196,.35); animation: pulse 2.4s ease-in-out infinite"></span><span style="display: flex; gap: 8px">{dots}</span><span style="font-size: 13px; color: {NMUTED}">Ola is thinking</span></div>'
    parts = ''.join(f'<span aria-hidden="true" style="position: absolute; left: 50%; top: 50%; width: {s}px; height: {s}px; margin: -{s // 2}px 0 0 -{s // 2}px; border-radius: {2 if k % 2 else 999}px; background: {c}; --dx: {dx}px; --dy: {dy}px; animation: burst .7s cubic-bezier(.2,.8,.2,1) both"></span>'
                    for k, (dx, dy, s, c) in enumerate([(-70, -40, 10, LIME), (64, -52, 8, EVG), (-50, 46, 8, EVG), (72, 30, 10, LIME), (0, -70, 7, LIME), (-80, 4, 7, EVG), (20, 64, 9, LIME)]))
    m4 = f'''<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 14px">
          <sc-if value="[[ won ]]" hint-placeholder-val="[[ false ]]"><span style="position: relative; width: 72px; height: 72px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">{parts}{icon('check', 34, EVG, 2.8)}</span><span style="font-size: 15px; font-weight: 600">Step done</span></sc-if>
          <sc-if value="[[ notWon ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ win ]]" style="height: 48px; padding: 0 18px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600">Mark this week's step done</button></sc-if>
          <sc-if value="[[ won ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ unwin ]]" style="height: 44px; padding: 0 12px; font-size: 14px; font-weight: 600; color: {EVG}">Again</button></sc-if></div>'''
    navicons = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 2px; color: {EVG if i == 0 else MUTED}">{icon(n, 20)}<span style="font-size: 12px; max-height: [[ labelH ]]px; overflow: hidden; transition: max-height .28s cubic-bezier(.2,.8,.2,1)">{t}</span></span>' for i, (t, n) in enumerate(AREAS))
    m5 = f'''<div style="position: absolute; inset: 0; display: flex; flex-direction: column; padding: 14px 14px 0; gap: 8px">
          <span style="height: 12px; width: 70%; border-radius: 2px; background: #DCE4DF"></span><span style="height: 10px; width: 90%; border-radius: 2px; background: #DCE4DF"></span><span style="height: 10px; width: 80%; border-radius: 2px; background: #DCE4DF"></span><span style="height: 10px; width: 60%; border-radius: 2px; background: #DCE4DF"></span>
          <button onClick="[[ read ]]" style="align-self: flex-start; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: #FFFFFF; font-size: 14px; font-weight: 600; margin-top: 4px">[[ readLabel ]]</button>
          <nav aria-label="Demo tab bar" style="position: absolute; left: [[ navInset ]]px; right: [[ navInset ]]px; bottom: 10px; height: [[ navH ]]px; border-radius: {R_L}px; background: rgba(255,255,255,.82); backdrop-filter: blur(10px); box-shadow: 0 6px 18px rgba(16,24,20,.12); display: flex; justify-content: space-around; align-items: center; transition: all .28s cubic-bezier(.2,.8,.2,1)">{navicons}</nav></div>'''
    m6 = f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 16px">
          <sc-if value="[[ calm ]]" hint-placeholder-val="[[ false ]]"><span style="width: 200px; height: 64px; border-radius: {R_M}px; background: {LIME}; display: flex; align-items: center; padding: 0 14px; font-size: 14px; font-weight: 600; color: {EVG}; animation: fadeIn .6s ease-out both">Up next: one small action</span></sc-if>
          <sc-if value="[[ notCalm ]]" hint-placeholder-val="[[ true ]]"><span style="width: 200px; height: 64px; border-radius: {R_M}px; background: {LIME}; display: flex; align-items: center; padding: 0 14px; font-size: 14px; font-weight: 600; color: {EVG}; animation: slideIn .6s cubic-bezier(.2,.8,.2,1) both">Up next: one small action</span></sc-if>
          <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">Reduce motion{switch(0, 'Reduce motion')}</span></div>'''
    speeds = ''.join(f'''<div style="border-radius: {R_M}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; align-items: baseline; gap: 8px"><span class="d" style="font-size: 32px">{ms}</span><span style="font-size: 13px; color: {MUTED}">ms, {w}</span></span>
        <span style="height: 32px; border-radius: {R_S}px; background: {MIST}; display: flex; align-items: center; padding: 0 4px"><span style="width: 24px; height: 24px; border-radius: {R_S}px; background: {c}; --run: 150px; animation: dot {dur} {ease} infinite"></span></span></div>'''
                     for ms, w, c, dur, ease in [('90', 'a touch', EVG, '1.2s', 'cubic-bezier(.2,.8,.2,1)'), ('180', 'a toggle or chip', EVG, '1.4s', 'cubic-bezier(.2,.8,.2,1)'),
                                                 ('280', 'a card or sheet', EVG, '1.8s', 'cubic-bezier(.2,.8,.2,1)'), ('600', 'a win, springs', LIME, '2.6s', 'cubic-bezier(.34,1.56,.64,1)')])
    curves = ''.join(f'''<div style="border-radius: {R_M}px; background: #FFFFFF; padding: 16px; display: flex; align-items: center; gap: 14px">
        <svg width="72" height="56" viewBox="0 0 72 56" aria-hidden="true" style="flex-shrink: 0; overflow: visible"><path d="M4 52 L68 52 M4 52 L4 4" stroke="#DCE4DF" stroke-width="1.5" fill="none"></path><path d="{p}" stroke="{EVG}" stroke-width="2.5" fill="none" stroke-linecap="round"></path></svg>
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 12px; color: {MUTED}">{c}</span></span></div>'''
                     for t, c, p in [('Ease out, for arrivals', 'cubic-bezier(.2, .8, .2, 1)', 'M4 52 C 17 14, 17 4, 68 4'), ('Spring, for wins only', 'cubic-bezier(.34, 1.56, .64, 1)', 'M4 52 C 26 -10, 44 -2, 68 4')])
    grid = ''.join([
        card('M1', 'Every tap answers back', 'A ring spreads from the touch point and the button squeezes a little. Tap it anywhere.', m1),
        card('M2', 'Progress grows once', 'Arcs fill and numbers count up when a screen opens, never again on every scroll.', m2),
        card('M3', 'Waiting feels alive', "While AI works, Ola breathes and the dots move. Never a bare spinner. Only in Learn and Ask.", m3, dark=True),
        card('M4', 'Celebrate the step, not the score', 'Finishing a lesson or a step earns a burst. A DIVA result never does: results are not prizes.', m4),
        card('M5', 'The bar floats, then gets out of the way', 'While she reads, the tab bar shrinks to its shapes. It comes back when she stops.', m5),
        card('M6', 'Less motion, same meaning', 'With reduce motion on, slides become fades and loops stop. Nothing depends on animation.', m6),
    ])
    body = f'''<div class="mv" style="--play: [[ play ]]; display: flex; flex-direction: column; gap: 24px">
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">{grid}</div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)) repeat(2, minmax(0, 1.2fr)); gap: 12px">{speeds}{curves}</div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {
      tapped: !!st.tapped, tx: st.tx || 110, ty: st.ty || 28,
      tap: (e) => { const x = e && e.offsetX != null ? e.offsetX : 110, y = e && e.offsetY != null ? e.offsetY : 28; this.setState({ tapped: false }, () => this.setState({ tapped: true, tx: x, ty: y })); },
      ringOn: st.ring !== false, replay: () => this.setState({ ring: false }, () => this.setState({ ring: true })),
      won: !!st.won, notWon: !st.won, win: () => this.setState({ won: true }), unwin: () => this.setState({ won: false }),
      readLabel: st.reading ? 'Stop reading' : 'Start reading', read: () => this.setState({ reading: !st.reading }),
      navH: st.reading ? 44 : 60, navInset: st.reading ? 60 : 12, labelH: st.reading ? 0 : 16
    };
%(sw)s
    v.calm = v.sw0; v.notCalm = !v.sw0; v.play = v.sw0 ? 'paused' : 'running';
    return v;
  }
}''' % dict(sw=switch_js(1, [False]))
    return board7('Motion that means something', 'Motion answers a touch, shows progress or marks a win (M1 to M6). Every card works; reduce motion on the last one pauses the loops on this board.', body, logic, 1600, 1160, css=MOTION_CSS)


# ---------------------------------------------------------------- Foundations

def foundations():
    areas = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 12px">
        <div style="height: 200px; border-radius: {R_L}px; background: {bg}; color: {fg}; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; {'box-shadow: inset 0 0 0 1px #C9D3CE;' if bg == POOL else ''}">
          <span style="display: flex; justify-content: space-between; align-items: center"><span class="d" style="font-size: 36px">{n}</span>{icon(icn, 34, sh, 1.8)}</span>
          <span style="font-size: 14px; font-weight: 600">{hx}</span>
        </div>
        <span style="font-size: 15px; line-height: 1.45"><strong>Means:</strong> {m}</span>
        <span style="font-size: 15px; line-height: 1.45; color: {SEC}"><strong style="color: {INK}">Moves:</strong> {mv}</span>
      </div>''' for n, bg, fg, sh, icn, hx, m, mv in AREA_INFO)
    neutrals = ''.join(f'<div style="display: flex; align-items: center; gap: 12px"><span style="width: 48px; height: 48px; flex-shrink: 0; border-radius: {R_M}px; background: {c}; box-shadow: inset 0 0 0 1px #C9D3CE"></span><span style="font-size: 14px; line-height: 1.35"><strong>{n}</strong><br>{r}</span></div>'
                       for c, n, r in [(MIST, 'Mist #EEF3F0', 'every light ground'), ('#FFFFFF', 'White', 'cards and sheets'), (INK, 'Ink #101814', 'text, 16 to 1'), (SEC, 'Secondary #3F4B45', 'supporting text'), (MUTED, 'Muted #56625C', 'captions, 5.7 to 1'), (MINT, 'Mint', "Ola's glow only")])
    pool_demo = pool(64, 150, 'fPool', rimw=2.5).replace('transform: translateY({{ waterY }}px); transition: transform .6s cubic-bezier(.34,1.56,.64,1)', 'animation: fillLoop 5s ease-in-out infinite').replace('{{ poolLabel }}', 'A pool filling and emptying')
    phases = ''.join(f'<span style="animation: waxLoop 4s ease-out {k * 0.4:.1f}s infinite">{moon(40, p)}</span>' for k, p in enumerate(['new', 'cres', 'half', 'full']))
    stones_demo = ''.join(f'<ellipse cx="{x}" cy="{y + 4}" rx="{rx}" ry="{ry}" fill="{EVG_D}"></ellipse><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#FFFFFF" stroke="{EVG}" stroke-width="2.5" style="animation: stepLoop 4s ease-out {k * 0.5:.1f}s infinite"></ellipse>'
                          for k, (x, y, rx, ry) in enumerate([(26, 110, 20, 8), (78, 82, 22, 9), (132, 54, 22, 9), (184, 26, 18, 7)]))
    rip = ''.join(f'<span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 999px; border: 2px solid {BLUSH_INK}; animation: spread 2.4s ease-out {d}s infinite"></span>' for d in (0, .8, 1.6))
    shape_cards = [
        ('The pool', 'Home', EVG, f'{pool_demo}'),
        ('The moon', 'Learn', NIGHT, f'<span style="display: flex; gap: 12px">{phases}</span>'),
        ('The arch', 'Vault', MIST, f'<span style="width: 96px; height: 120px; border-radius: 48px 48px {R_S}px {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: flipLoop 4s cubic-bezier(.34,1.3,.64,1) infinite"><span style="width: 56px; height: 76px; margin-top: 18px; box-sizing: border-box; border-radius: 28px 28px {R_S}px {R_S}px; border: 2px solid {EVG}"></span></span>'),
        ('The ripple', 'Community', BLUSH, f'{rip}<img class="face" src="{IMG["thandi"]}" alt="" style="position: relative; width: 56px; height: 56px">'),
        ('The stones', 'Me', POOL, f'<svg width="210" height="130" viewBox="0 0 210 130" aria-hidden="true">{stones_demo}</svg>'),
    ]
    shapes = ''.join(f'<div style="display: flex; flex-direction: column; gap: 10px"><div style="position: relative; overflow: hidden; height: 170px; border-radius: {R_L}px; background: {bg}; display: flex; align-items: center; justify-content: center; perspective: 600px">{demo}</div><span style="font-size: 16px; font-weight: 600">{t} <span style="font-weight: 400; color: {MUTED}">{a}</span></span></div>' for t, a, bg, demo in shape_cards)
    moods = ''.join(f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 8px"><img src="{src}" alt="{alt}" style="width: 100%; height: 200px; object-fit: cover; object-position: {pos}; border-radius: {R_L}px"><figcaption style="font-size: 14px; font-weight: 600">{cap}</figcaption></figure>'
                    for src, alt, pos, cap in [
                        (IMG['naledi_cafe'], 'A woman absorbed in her tablet', '45% 30%', 'Focused'),
                        (IMG['amara_coat'], 'A woman in a winter coat', '60% 40%', 'Determined'),
                        (IMG['wanjiru_stall'], 'A woman at her market stall', '62% 35%', 'At work'),
                        (IMG['grace_dancing'], 'An older woman dancing in the street', '40% 20%', 'Joy at sixty'),
                    ])
    space = ''.join(f'<div style="display: flex; align-items: center; gap: 14px"><span style="width: 48px; font-size: 14px; font-weight: 600">{s}</span><span style="height: 16px; width: {s * 6}px; border-radius: 2px; background: {EVG}"></span><span style="font-size: 13px; color: {MUTED}">{u}</span></div>'
                    for s, u in [(4, 'inside chips'), (8, 'between chips and tiles'), (12, 'between cards on a screen'), (16, 'card padding'), (20, 'the screen edge'), (24, 'between sections')])
    phone_grid = f'''<div style="position: relative; width: 195px; height: 300px; border-radius: 22px; background: {MIST}; box-shadow: 0 0 0 1px #C9D3CE; overflow: hidden; flex-shrink: 0">
        <span style="position: absolute; left: 10px; top: 0; bottom: 0; width: 1px; background: {LIME}"></span><span style="position: absolute; right: 10px; top: 0; bottom: 0; width: 1px; background: {LIME}"></span>
        <span style="position: absolute; left: 10px; right: 10px; top: 30px; height: 22px; border-radius: 3px; background: #DCE4DF"></span>
        <span style="position: absolute; left: 10px; right: 10px; top: 60px; height: 96px; border-radius: 7px; background: {EVG}"></span>
        <span style="position: absolute; left: 10px; width: 84px; top: 162px; height: 60px; border-radius: 7px; background: #FFFFFF"></span><span style="position: absolute; right: 10px; width: 84px; top: 162px; height: 60px; border-radius: 7px; background: {LIME}"></span>
        <span style="position: absolute; left: 0; right: 0; bottom: 0; height: 42px; background: #FFFFFF; border-top: 1px solid #DCE4DF"></span></div>'''
    body = f'''<section style="display: flex; flex-direction: column; gap: 18px">
    <h2 class="d" style="font-size: 40px">Colour: five areas, one job each</h2>
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px">{areas}</div>
    <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; padding-top: 6px">{neutrals}</div>
    <p style="font-size: 15px; line-height: 1.45; color: {SEC}; max-width: 1100px">Lime marks progress and wins, and is the main button on dark grounds; evergreen is the main button on light ones. No red for a month that went down: decreases are grey. The wine colour appears only for warnings and deleting.</p>
  </section>
  <section class="card">
    <h2 class="d" style="font-size: 40px">Shapes</h2>
    <span class="knote">Each shape means one thing and moves one way. The tab bar is made of them, so the navigation teaches the language. Shapes keep their own curves; everything else uses the three corner sizes.</span>
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px">{shapes}</div>
  </section>
  <div style="display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 24px; align-items: start">
    <section class="card"><h2 class="d" style="font-size: 40px">People</h2><span class="knote">Real women, ages 25 to 65, at work and at home. Focused, tired, determined and calm, not only laughing. Faces are never covered by chips, and Community shows first names only.</span>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px">{moods}</div>
      <span class="knote">Stand-ins from nappy.co until AWO photographs real members (Q-27).</span></section>
    <section class="card"><h2 class="d" style="font-size: 40px">Space</h2>
      <div style="display: flex; gap: 28px; align-items: center">{phone_grid}<div style="display: flex; flex-direction: column; gap: 12px">{space}</div></div>
      <span class="knote">Screens are 390 wide with 20px edges. Touch targets are at least 44px. Type and corners are on the board to the left.</span></section>
  </div>'''
    return board7('Foundations', 'Colour, shapes, people and space for Round 7. Type and corners have their own board.', body, static_logic(), 1600, 1580, css=FOUND_CSS_KEYS, chip='Sample content')


BOARDS = [('R7-Brand', brand), ('R7-Icons', icons), ('R7-Motion', motion), ('R7-Foundations', foundations)]
