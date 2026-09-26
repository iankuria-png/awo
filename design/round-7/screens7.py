"""Round 7 screens that Round 6 never had, brought over from Round 3's E set and written natively in
Round 7 style: progress over time, the 30-day check-in, the buddy, settings, onboarding goals and a
photo-led welcome. Same rules as areas7.py: one hero per screen (the area's shape doing a job),
objects instead of rows, short copy, the hand only where the rules allow it."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403

IMG.update({
    'phone_smile': '/_blob/d52cdc4b08597f0ff8bc6e1c58f129dd',
    'hero_photo': '/_blob/2c5815c8e5a96112594e520c65e4ac76',
})

HF = "font-family: '[[ handFont ]]', cursive"
R_S, R_M, R_L = 6, 10, 14
LINE7 = '#EEF2EF'

EXTRA_ICONS = {
    'back': '<path d="m15 6-6 6 6 6"></path>',
    'close': '<path d="M6 6l12 12M18 6L6 18"></path>',
    'shop': '<path d="M4 9.5 5.5 4h13L20 9.5"></path><path d="M4 9.5a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0"></path><path d="M5.5 12v8h13v-8"></path><path d="M10 20v-4.5h4V20"></path>',
    'doc': '<path d="M6.5 3h8l3 3v15h-11z"></path><path d="M9.5 10.5h5M9.5 14h5M9.5 17.5h3"></path>',
    'home': '<path d="M4 11 12 4l8 7"></path><path d="M6 9.5V20h12V9.5"></path><path d="M10 20v-5h4v5"></path>',
    'down': '<path d="M3 7l6 6 4-4 8 8"></path><path d="M21 11v6h-6"></path>',
    'shield': '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path>',
    'pin': '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"></path><circle cx="12" cy="10" r="2.3"></circle>',
    'download': '<path d="M12 4v11M7 10.5l5 5 5-5"></path><path d="M5 20h14"></path>',
    'heart': '<path d="M12 20s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.6-7.5 10-7.5 10z" fill="currentColor"></path>',
    'bell': '<path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"></path><path d="M10 20.5a2.2 2.2 0 0 0 4 0"></path>',
    'text': '<path d="M4 18 8.5 6h1L14 18M5.6 14h6.8"></path><path d="M15 18l3-7.5h.6L21.5 18M16 15.5h4.6"></path>',
    'motion': '<path d="M3 12c2.5-4 5-4 7.5 0s5 4 7.5 0 2.5-2 3-2"></path>',
    'people': '<circle cx="9" cy="8.5" r="3.2"></circle><path d="M3.5 19a5.5 5.5 0 0 1 11 0"></path><circle cx="16.5" cy="9.5" r="2.6"></circle><path d="M15.5 14.2a4.6 4.6 0 0 1 5 4.8"></path>',
}


def ic(name, size=20, stroke='currentColor', sw=2):
    if name in EXTRA_ICONS:
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0">{EXTRA_ICONS[name]}</svg>')
    return icon(name, size, stroke, sw)


def back(href, label='Back'):
    return (f'<a href="{href}" aria-label="{label}" style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: #FFFFFF; '
            f'display: flex; align-items: center; justify-content: center">{ic("back", 20, INK, 2.2)}</a>')


def sub_header(href, title, chip=True):
    right = sample_chip() if chip else '<span style="width: 44px"></span>'
    return (f'<header style="display: flex; align-items: center; justify-content: space-between; gap: 12px">{back(href)}'
            f'<span style="font-size: 17px; font-weight: 600">{title}</span>{right}</header>')


def switch(i, label):
    """A switch in Round 7 corners: 10px track, 6px thumb. The whole 60x44 box is the target."""
    return (f'<button role="switch" aria-checked="[[ sw{i} ]]" aria-label="{label}" onClick="[[ toggle{i} ]]" style="width: 60px; height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center">'
            f'<span style="width: 52px; height: 32px; border-radius: {R_M}px; background: [[ swBg{i} ]]; position: relative; transition: background-color .18s">'
            f'<span style="position: absolute; top: 4px; left: 4px; width: 24px; height: 24px; border-radius: {R_S}px; background: #FFFFFF; box-shadow: 0 1px 3px rgba(16,24,20,.25); '
            f'transform: translateX([[ swX{i} ]]px); transition: transform .18s cubic-bezier(.2,.8,.2,1)"></span></span></button>')


def switch_js(n, on):
    """Logic lines for n switches whose starting states are in `on`."""
    return '''    for (let i = 0; i < %d; i++) {
      const on = st['sw' + i] == null ? %s[i] : st['sw' + i];
      v['sw' + i] = on; v['toggle' + i] = () => this.setState({ ['sw' + i]: !on });
      v['swBg' + i] = on ? '%s' : '#C9D3CE'; v['swX' + i] = on ? 20 : 0;
    }''' % (n, str(on).lower().replace('true', 'true').replace('false', 'false'), EVG)


# ---------------------------------------------------------------- Progress over time

VERSIONS = [(1, '13 Jul', 55, 'Your first profile'), (2, '13 Aug', 59, 'up 4'), (3, '13 Sep', 63, 'up 4')]
MOVED = [('Everyday money', 66, 71), ('Ready for surprises', 41, 48), ('Knowing your options', 57, 60), ('Clear goals', 60, 69)]


def progress():
    # Stones rise with the value: x by date, y by readiness.
    xs = [40, 142, 244]
    ys = [round(150 - (val - 50) * 6.5) for _n, _d, val, _t in VERSIONS]
    nx, ny = 304, ys[-1] - 6
    path = f'M{xs[0]} {ys[0]}' + ''.join(f'L{x} {y}' for x, y in zip(xs[1:], ys[1:]))
    chart_svg = (f'<svg width="318" height="172" viewBox="0 0 318 172" aria-hidden="true" style="position: absolute; left: 0; top: 0; overflow: visible">'
                 f'<path d="{path}" fill="none" stroke="{EVG}" stroke-width="2" stroke-opacity=".35"></path>'
                 f'<path d="M{xs[-1]} {ys[-1]}L{nx} {ny}" fill="none" stroke="{EVG}" stroke-width="2" stroke-dasharray="4 5" stroke-opacity=".5"></path>'
                 f'<ellipse cx="{nx}" cy="{ny}" rx="17" ry="7" fill="none" stroke="{EVG}" stroke-width="2" stroke-dasharray="4 4"></ellipse></svg>')
    stones_html = ''
    for i, ((n, d, val, _t), x, y) in enumerate(zip(VERSIONS, xs, ys)):
        stones_html += (f'<button onClick="[[ pick{i} ]]" aria-pressed="[[ on{i} ]]" aria-label="Version {n}, {d}, DIVA score {val}" '
                        f'style="position: absolute; left: {x - 30}px; top: {y - 26}px; width: 60px; height: 52px; display: flex; align-items: center; justify-content: center">'
                        f'<span style="width: 40px; height: 16px; border-radius: 50%; background: [[ stFill{i} ]]; box-shadow: 0 0 0 2.5px {EVG}, 0 0 0 [[ stRing{i} ]]px {LIME}; '
                        f'transition: background-color .18s, box-shadow .18s; animation: stepIn .5s cubic-bezier(.2,.8,.2,1) {0.15 + i * 0.12:.2f}s both"></span></button>'
                        f'<span style="position: absolute; left: {x - 30}px; top: 150px; width: 60px; text-align: center; font-size: 12px; color: {SEC}">{d}</span>')
    stones_html += f'<span style="position: absolute; left: {nx - 30}px; top: 150px; width: 60px; text-align: center; font-size: 12px; color: {SEC}">13 Oct</span>'
    tip = (f'<div style="position: absolute; left: [[ tipX ]]px; top: [[ tipY ]]px; width: 120px; box-sizing: border-box; border-radius: {R_M}px; background: {INK}; color: #FFFFFF; '
           f'padding: 8px 10px; display: flex; flex-direction: column; gap: 2px; transition: left .28s cubic-bezier(.2,.8,.2,1), top .28s cubic-bezier(.2,.8,.2,1); pointer-events: none">'
           f'<span style="font-size: 12px; color: #C9D3CE">[[ tipDate ]]</span><span style="font-size: 15px; font-weight: 600">[[ tipVal ]]</span></div>')
    moved = ''
    for name, old, new in MOVED:
        moved += f'''<div style="display: flex; flex-direction: column; gap: 6px">
          <span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 15px; font-weight: 600">{name}</span><span style="font-size: 13px; color: {MUTED}">{old} to <b style="color: {INK}; font-weight: 600">{new}</b></span></span>
          <span aria-hidden="true" style="position: relative; height: 8px; border-radius: 2px; background: {LINE7}; overflow: hidden">
            <span style="position: absolute; left: 0; top: 0; bottom: 0; width: {new}%; background: {EVG}; transform-origin: left; animation: fill .6s cubic-bezier(.2,.8,.2,1) .2s both"></span>
            <span style="position: absolute; left: 0; top: 0; bottom: 0; width: {old}%; background: #BFD9D2"></span>
          </span>
        </div>'''
    tiles = ''.join(f'<div style="border-radius: {R_L}px; background: {bg}; padding: 14px; display: flex; flex-direction: column; gap: 4px"><span class="d" style="font-size: 36px; color: {EVG}">{n}</span><span style="font-size: 13px; color: {SEC}">{t}</span></div>'
                    for n, t, bg in [('9', 'lessons done', '#FFFFFF'), ('4', 'small actions', '#FFFFFF'), ('3', 'check-ins', LIME)])
    body = f'''  <div class="scr" style="bottom: 0; gap: 14px">
    {sub_header('R7-Me.dc.html', 'Your progress')}
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 20px 16px 18px; display: flex; flex-direction: column; gap: 14px">
      <div style="display: flex; flex-direction: column; gap: 6px">
        <span class="lbl">DIVA score</span>
        <span style="display: flex; align-items: center; gap: 12px"><span class="d" style="font-size: 72px">63</span><span class="chip" style="background: {LIME}; color: {EVG}">+8 since July</span></span>
      </div>
      <div role="group" aria-label="Your versions. Tap one." style="position: relative; height: 172px">{chart_svg}{stones_html}{tip}</div>
      <span style="font-size: 13px; color: {SEC}">Each check-in makes a new version. Old ones never change.</span>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 14px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">What moved since July</span><span style="font-size: 13px; color: {MUTED}">Out of 100</span></span>
      {moved}
    </section>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{tiles}</div>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 16px; display: flex; align-items: center; gap: 12px">
      <span style="color: {EVG}; display: flex">{ic('shield', 22)}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Evidence grew to building</span><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">Two check-ins included things you did. Kept apart from the score.</span></span>
      <span role="img" aria-label="2 of 3" style="display: flex; gap: 3px"><span style="width: 16px; height: 6px; border-radius: 2px; background: {EVG}"></span><span style="width: 16px; height: 6px; border-radius: 2px; background: {EVG}"></span><span style="width: 16px; height: 6px; border-radius: 2px; background: #DCE4DF"></span></span>
    </section>
    <a href="R7-Checkin.dc.html" style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 14px 14px 14px 18px; display: flex; align-items: center; gap: 14px">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Next check-in on 13 Oct</span><span style="font-size: 13px; color: {ON_EVG}">Three questions, about two minutes</span></span>
      <span style="height: 44px; padding: 0 16px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Preview</span>
    </a>
  </div>'''
    vs = [[d, val, t, x, y] for (_n, d, val, t), x, y in zip(VERSIONS, xs, ys)]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const sel = st.sel == null ? 2 : st.sel;
    const vs = %(vs)s;
    const s = vs[sel];
    const v = {
      tipX: Math.max(0, Math.min(170, s[3] - 60)), tipY: s[4] - 64,
      tipDate: s[0] + ', version ' + (sel + 1), tipVal: s[1] + (sel === 0 ? ', your first' : ', ' + s[2])
    };
    for (let i = 0; i < 3; i++) {
      v['pick' + i] = () => this.setState({ sel: i }); v['on' + i] = sel === i;
      v['stFill' + i] = sel === i ? '%(evg)s' : (i < sel ? '#BFD9D2' : '#FFFFFF'); v['stRing' + i] = sel === i ? 7 : 0;
    }
    return v;
  }
}''' % dict(vs=vs, evg=EVG)
    return phone('Your progress', body, logic, h=1040)


# ---------------------------------------------------------------- The 30-day check-in

Q2 = ['Yes, every payday', 'Some of it', 'Not this time']
Q3 = [('Calmer', 'Money felt more in hand'), ('About the same', 'Nothing much changed'), ('Harder', 'It was a tight month')]


def checkin():
    segs = ''.join(f'<span style="flex: 1 1 0; height: 6px; border-radius: 2px; background: [[ seg{i} ]]; transition: background-color .28s"></span>' for i in range(3))
    chips = ''.join(f'<button onClick="[[ amt{i} ]]" aria-pressed="[[ amtOn{i} ]]" style="flex: {"1.5" if i == 0 else "1"} 1 0; height: 44px; border-radius: {R_M}px; background: [[ amtBg{i} ]]; color: [[ amtFg{i} ]]; font-size: 14px; font-weight: 600; white-space: nowrap; transition: background-color .18s">{t}</button>'
                    for i, t in enumerate(['Nothing yet', 'R 500', 'R 1 000', 'R 2 000']))
    q2 = ''.join(f'''<button onClick="[[ a2_{i} ]]" aria-pressed="[[ a2On{i} ]]" style="min-height: 60px; padding: 0 16px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ a2Bw{i} ]]px {EVG}; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 16px; font-weight: 500">
            <span style="flex-grow: 1">{t}</span><span aria-hidden="true" style="width: 24px; height: 24px; border-radius: {R_S}px; background: [[ a2Dot{i} ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center"><sc-if value="[[ a2On{i} ]]" hint-placeholder-val="[[ false ]]">{icon('check', 16, '#FFFFFF', 3)}</sc-if></span></button>''' for i, t in enumerate(Q2))
    q3 = ''.join(f'''<button onClick="[[ a3_{i} ]]" aria-pressed="[[ a3On{i} ]]" style="min-height: 72px; padding: 0 16px; border-radius: {R_M}px; background: [[ a3Bg{i} ]]; color: [[ a3Fg{i} ]]; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; gap: 2px; text-align: left; transition: background-color .18s">
            <span style="font-size: 17px; font-weight: 600">{t}</span><span style="font-size: 13px; opacity: .8">{d}</span></button>''' for i, (t, d) in enumerate(Q3))
    st_pts = [(34, 104, 24, 9), (110, 82, 26, 10), (190, 58, 28, 11), (272, 30, 32, 12)]
    pop_new = ' style="animation: pop .6s cubic-bezier(.34,1.56,.64,1) .5s both; transform-box: fill-box; transform-origin: center"'
    st_svg = ''.join(
        f'<ellipse cx="{x}" cy="{y + 6}" rx="{rx}" ry="{ry}" fill="#BFD9D2"></ellipse>'
        f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{LIME if i == 3 else EVG}" stroke="{EVG}" stroke-width="2.5"{pop_new if i == 3 else ""}></ellipse>'
        for i, (x, y, rx, ry) in enumerate(st_pts))
    face = IMG['naledi']
    st_new = (f'<div role="img" aria-label="A fourth stone for this check-in, with you on it" style="position: relative; width: 320px; height: 130px">'
              f'<svg width="320" height="130" viewBox="0 0 320 130" aria-hidden="true" style="position: absolute; inset: 0; overflow: visible">{st_svg}</svg>'
              f'<img class="face" src="{face}" alt="" style="position: absolute; left: 252px; top: -16px; width: 40px; height: 40px; box-shadow: 0 0 0 3px {LIME}; animation: stepIn .7s cubic-bezier(.2,.8,.2,1) .9s both">'
              f'<span style="position: absolute; left: 244px; top: 52px; width: 56px; text-align: center; font-size: 13px; font-weight: 600; color: {EVG}">New</span></div>')
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 18px">
    <header style="display: flex; align-items: center; gap: 16px">
      <div role="img" aria-label="[[ stepLabel ]]" style="flex-grow: 1; display: flex; gap: 6px">{segs}</div>
      <a href="R7-Progress.dc.html" aria-label="Close the check-in" style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</a>
    </header>
    <sc-if value="[[ isQ0 ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; flex-direction: column; gap: 18px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <span class="lbl" style="color: {EVG}">Question 1 of 3</span>
        <h1 class="d" style="font-size: 32px">Since 13 Sep, how much did you put aside for your safety net?</h1>
        <div style="display: flex; align-items: center; gap: 24px; padding: 6px 0 0 8px">
          <div style="width: 116px; height: 220px; flex-shrink: 0">{pool(116, 220, 'ckPool', water=POOL, wave=EVG, vessel='#FFFFFF', rim=EVG, rimw=3)}</div>
          <div style="display: flex; flex-direction: column; gap: 6px"><span class="d" style="font-size: 56px; color: {EVG}; font-variant-numeric: tabular-nums">[[ amtText ]]</span><span style="font-size: 15px; color: {SEC}">this month</span></div>
        </div>
        <label for="ck-amt" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Amount put aside</label>
        <input id="ck-amt" class="rng" type="range" min="0" max="5000" step="100" value="[[ amt ]]" onInput="[[ slide ]]" aria-valuetext="[[ amtText ]]">
        <span style="display: flex; justify-content: space-between; font-size: 12px; color: {MUTED}; margin-top: -12px"><span>R 0</span><span>R 5 000</span></span>
        <div role="group" aria-label="Quick amounts" style="display: flex; gap: 6px">{chips}</div>
      </div>
    </sc-if>
    <sc-if value="[[ isQ1 ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; gap: 16px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <span class="lbl" style="color: {EVG}">Question 2 of 3</span>
        <h1 class="d" style="font-size: 32px">Did you try this month's step?</h1>
        <div style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 14px 16px; display: flex; align-items: center; gap: 12px"><span style="width: 36px; height: 36px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{icon('pool', 20, EVG)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Build a starter safety net</span><span style="font-size: 13px; color: {ON_EVG}">Move R 100 on payday</span></span></div>
        <div role="group" aria-label="Your answer" style="display: flex; flex-direction: column; gap: 8px">{q2}</div>
        <sc-if value="[[ q2Honest ]]" hint-placeholder-val="[[ false ]]"><p style="font-size: 15px; line-height: 1.4; color: {SEC}; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">Thanks for saying so. It still counts as a check-in.</p></sc-if>
      </div>
    </sc-if>
    <sc-if value="[[ isQ2 ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; gap: 16px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <span class="lbl" style="color: {EVG}">Question 3 of 3</span>
        <h1 class="d" style="font-size: 32px">How did money feel this month?</h1>
        <div role="group" aria-label="Your answer" style="display: flex; flex-direction: column; gap: 8px">{q3}</div>
      </div>
    </sc-if>
    <sc-if value="[[ isDone ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; padding-top: 72px">
        {st_new}
        <h1 class="d" style="font-size: 40px; margin-top: 20px; animation: rise .45s cubic-bezier(.2,.8,.2,1) .15s both">Check-in done.</h1>
        <span class="hand" style="font-size: 28px; color: {EVG}; {HF}; animation: rise .45s cubic-bezier(.2,.8,.2,1) .35s both">One month, kept.</span>
        <p style="font-size: 16px; line-height: 1.45; color: {SEC}; max-width: 300px">Your answers make a new version of your profile. You'll find it on Me.</p>
      </div>
    </sc-if>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ notDone ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}">{icon('lock', 16, MUTED)}Honest answers make your profile more useful. Nothing here is shared.</span>
        <button onClick="[[ next ]]" aria-disabled="[[ blocked ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: [[ nextBg ]]; color: [[ nextFg ]]; font-size: 16px; font-weight: 600; transition: background-color .18s">[[ nextLabel ]]</button>
      </div>
    </sc-if>
    <sc-if value="[[ isDone ]]" hint-placeholder-val="[[ false ]]"><a href="R7-Me.dc.html" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">See your profile</a></sc-if>
  </div>'''
    css = f'''
.rng{{-webkit-appearance:none;appearance:none;width:100%;height:44px;background:transparent;margin:0}}
.rng::-webkit-slider-runnable-track{{height:8px;border-radius:2px;background:linear-gradient(to right,{EVG} 0,{EVG} var(--p),#DCE4DF var(--p))}}
.rng::-webkit-slider-thumb{{-webkit-appearance:none;width:30px;height:30px;margin-top:-11px;border-radius:{R_S}px;background:{LIME};box-shadow:0 0 0 3px {EVG}}}
.rng::-moz-range-track{{height:8px;border-radius:2px;background:#DCE4DF}}
.rng::-moz-range-progress{{height:8px;border-radius:2px;background:{EVG}}}
.rng::-moz-range-thumb{{width:28px;height:28px;border:0;border-radius:{R_S}px;background:{LIME};box-shadow:0 0 0 3px {EVG}}}
.rng:focus-visible{{outline:2px solid {EVG};outline-offset:4px}}
'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const q = st.q || 0, amt = st.amt == null ? 1800 : st.amt;
    const a2 = st.a2 == null ? -1 : st.a2, a3 = st.a3 == null ? -1 : st.a3;
    const fmt = (n) => n === 0 ? 'R 0' : 'R ' + String(n).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' ');
    const blocked = (q === 1 && a2 < 0) || (q === 2 && a3 < 0);
    const v = {
      isQ0: q === 0, isQ1: q === 1, isQ2: q === 2, isDone: q === 3, notDone: q < 3,
      stepLabel: q < 3 ? 'Question ' + (q + 1) + ' of 3' : 'All three answered',
      amt, amtText: fmt(amt), slide: (e) => this.setState({ amt: Number(e.target.value) }),
      waterY: Math.round(214 - (amt / 5000) * 196), poolLabel: fmt(amt) + ' put aside this month',
      q2Honest: a2 === 2, blocked,
      next: () => { if (!blocked) this.setState({ q: q + 1 }); },
      nextLabel: q === 2 ? 'Finish check-in' : 'Continue',
      nextBg: blocked ? '#DCE4DF' : '%(evg)s', nextFg: blocked ? '%(mut)s' : '#FFFFFF'
    };
    for (let i = 0; i < 3; i++) v['seg' + i] = i <= q ? '%(evg)s' : '#DCE4DF';
    const quick = [0, 500, 1000, 2000];
    for (let i = 0; i < 4; i++) {
      v['amt' + i] = () => this.setState({ amt: quick[i] }); v['amtOn' + i] = amt === quick[i];
      v['amtBg' + i] = amt === quick[i] ? '%(evg)s' : '#FFFFFF'; v['amtFg' + i] = amt === quick[i] ? '#FFFFFF' : '%(ink)s';
    }
    for (let i = 0; i < 3; i++) {
      v['a2_' + i] = () => this.setState({ a2: i }); v['a2On' + i] = a2 === i; v['a2Bw' + i] = a2 === i ? 2 : 0;
      v['a2Dot' + i] = a2 === i ? '%(evg)s' : '#FFFFFF';
      v['a3_' + i] = () => this.setState({ a3: i }); v['a3On' + i] = a3 === i;
      v['a3Bg' + i] = a3 === i ? '%(evg)s' : '#FFFFFF'; v['a3Fg' + i] = a3 === i ? '#FFFFFF' : '%(ink)s';
    }
    return v;
  }
}''' % dict(evg=EVG, mut=MUTED, ink=INK)
    html = phone('30-day check-in', body, logic, h=844)
    html = html.replace('</style>', css + '</style>', 1)
    # The slider's filled part follows the value.
    html = html.replace('class="rng" type="range"', 'class="rng" style="--p: {{ amtPct }}%" type="range"', 1)
    html = html.replace("amt, amtText: fmt(amt),", "amt, amtText: fmt(amt), amtPct: Math.round(amt / 50),", 1)
    return html


# ---------------------------------------------------------------- The buddy

def buddy():
    weeks = ['W1', 'W2', 'W3', 'Now']
    marks = {'You': ['done', 'done', 'done', 'done'], 'Wanjiru': ['done', 'done', 'miss', 'wait']}

    def mark(kind):
        if kind == 'done':
            return f'<span style="width: 30px; height: 30px; border-radius: 999px; background: {EVG}; display: flex; align-items: center; justify-content: center">{icon("check", 16, LIME, 2.8)}</span>'
        if kind == 'miss':
            return '<span style="width: 30px; height: 30px; box-sizing: border-box; border-radius: 999px; border: 2px solid #C9D3CE"></span>'
        return f'<span style="width: 30px; height: 30px; box-sizing: border-box; border-radius: 999px; border: 2px dashed {EVG}"></span>'
    grid = f'<span></span>' + ''.join(f'<span style="font-size: 12px; color: {MUTED if w != "Now" else EVG}; font-weight: {400 if w != "Now" else 600}; text-align: center">{w}</span>' for w in weeks)
    for who, ms in marks.items():
        grid += f'<span style="font-size: 14px; font-weight: 600">{who}</span>' + ''.join(f'<span style="display: flex; justify-content: center">{mark(k)}</span>' for k in ms)
    goal_rows = ''.join(f'''<div style="display: flex; align-items: center; gap: 10px">
          <img class="face" src="{IMG[k]}" alt="" style="width: 28px; height: 28px">
          <span style="width: 64px; font-size: 14px; font-weight: 600">{who}</span>
          <span aria-hidden="true" style="flex-grow: 1; height: 8px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: {round(n / 6 * 100)}%; background: {EVG}; transform-origin: left; animation: fill .6s cubic-bezier(.2,.8,.2,1) .2s both"></span></span>
          <span style="width: 40px; text-align: right; font-size: 13px; color: {MUTED}">{n} of 6</span>
        </div>''' for who, k, n in [('You', 'naledi', 3), ('Wanjiru', 'wanjiru', 2)])
    rings = ''.join(f'<span style="position: absolute; left: 50%; top: 50%; width: {s}px; height: {s}px; margin: -{s // 2}px 0 0 -{s // 2}px; border-radius: 999px; border: 1.5px solid {BLUSH_2}; opacity: {o}"></span>'
                    for s, o in [(150, .35), (210, .22), (270, .12)])
    body = f'''  <div class="scr" style="bottom: 0; gap: 14px">
    {sub_header('R7-Community.dc.html', 'Your buddy')}
    <section style="position: relative; overflow: hidden; border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 22px 18px 18px; display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center">
      <div aria-hidden="true" style="position: relative; width: 170px; height: 112px">{rings}
        <img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 8px; top: 8px; width: 96px; height: 96px; box-shadow: 0 0 0 4px {BLUSH}">
        <img class="face" src="{IMG['wanjiru']}" alt="" style="position: absolute; left: 66px; top: 8px; width: 96px; height: 96px; box-shadow: 0 0 0 4px {BLUSH}">
      </div>
      <h1 class="d" style="font-size: 36px">You and Wanjiru</h1>
      <span style="font-size: 15px; line-height: 1.4; color: {BLUSH_2}">Buddies since 14 Sep. Both on the safety net path.</span>
      <button onClick="[[ cheer ]]" aria-pressed="[[ cheered ]]" style="position: relative; height: 48px; padding: 0 20px; border-radius: {R_M}px; background: {BLUSH_INK}; color: {BLUSH}; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">
        <sc-if value="[[ cheered ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; border-radius: {R_M}px; color: {BLUSH_INK}"></span></sc-if>{ic('heart', 16)}[[ cheerLabel ]]</button>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Weekly check-ins</span><span style="font-size: 13px; color: {MUTED}">Last four weeks</span></span>
      <div role="img" aria-label="You checked in all four weeks. Wanjiru checked in weeks 1 and 2, and hasn't yet this week." style="display: grid; grid-template-columns: 72px repeat(4, minmax(0, 1fr)); row-gap: 10px; align-items: center">{grid}</div>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: center; gap: 8px"><span style="font-size: 13px; font-weight: 600; color: {MUTED}">Shared goal</span><span class="chip" style="background: {MIST}; color: {SEC}">{icon('lock', 13, SEC)}Lessons only, never amounts</span></span>
      <span class="d" style="font-size: 26px">Build a starter safety net</span>
      {goal_rows}
    </section>
    <div style="display: flex; gap: 10px; align-items: flex-end"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 32px; height: 32px"><span style="padding: 10px 14px; border-radius: {R_L}px {R_L}px {R_L}px {R_S}px; background: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 250px">Lesson 2 done! Choosing my small action tonight.</span></div>
    <sc-if value="[[ sent ]]" hint-placeholder-val="[[ false ]]"><span style="align-self: flex-end; padding: 10px 14px; border-radius: {R_L}px {R_L}px {R_S}px {R_L}px; background: {EVG}; color: #FFFFFF; font-size: 15px; line-height: 1.4; max-width: 250px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">[[ msg ]]</span></sc-if>
    <sc-if value="[[ notSent ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; gap: 8px">
        <label for="bd-msg" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Write to Wanjiru</label>
        <input id="bd-msg" value="[[ msg ]]" onInput="[[ type ]]" placeholder="Write to Wanjiru" style="flex-grow: 1; min-width: 0; height: 48px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 15px">
        <button onClick="[[ send ]]" aria-label="Send" style="width: 48px; height: 48px; border-radius: {R_M}px; background: {EVG}; display: flex; align-items: center; justify-content: center">{icon('send', 18, '#FFFFFF')}</button>
      </div>
    </sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const cheered = !!st.cheered, sent = !!st.sent;
    const msg = st.msg == null ? "Same. Let's check in on Sunday?" : st.msg;
    return {
      cheered, cheer: () => this.setState({ cheered: true }), cheerLabel: cheered ? 'Cheer sent' : 'Send Wanjiru a cheer',
      sent, notSent: !sent, msg, type: (e) => this.setState({ msg: e.target.value }),
      send: () => { if (msg.trim()) this.setState({ sent: true }); }
    };
  }
}'''
    return phone('Your buddy', body, logic, h=960)


# ---------------------------------------------------------------- Settings

SETTINGS = [
    ('Reminders', [('Lesson reminders', 'A nudge on the days you usually learn', True),
                   ('Check-in reminder', 'Three days before your 30-day check-in', True),
                   ('Community replies', 'When someone answers your post', False)]),
    ('Privacy', [('Show my first name only', 'Your surname never appears in Community', True),
                 ('Share lesson progress with my buddy', 'Lessons and actions only, never amounts', True),
                 ('Help improve AWO with my answers', 'Anonymised, and you can stop at any time', False)]),
    ('Comfort', [('Reduce motion', 'Loops stop and slides become fades', False),
                 ('Larger text', 'Follows your phone setting by default', False)]),
]


def settings():
    groups = ''
    k = 0
    for gname, rows in SETTINGS:
        rhtml = ''
        for j, (t, d, _on) in enumerate(rows):
            sep = f'border-bottom: 1px solid {LINE7};' if j < len(rows) - 1 else ''
            extra = ''
            if t == 'Reduce motion':
                extra = f'<span aria-hidden="true" style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {MIST}; overflow: hidden; display: flex; align-items: center; justify-content: center"><span style="width: 22px; height: 30px">{pool(22, 30, "setPool", rimw=2, hole="setWaterY", label="setPoolLabel", static=False)}</span></span>'
            if t == 'Larger text':
                extra = f'<span aria-hidden="true" style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {MIST}; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: [[ aaSize ]]px; transition: font-size .18s">Aa</span>'
            rhtml += f'''<div style="min-height: 64px; display: flex; align-items: center; gap: 12px; padding: 8px 0; {sep}">
          {extra}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: [[ tSize ]]px; font-weight: 600; line-height: 1.3">{t}</span><span style="font-size: [[ dSize ]]px; line-height: 1.35; color: {MUTED}">{d}</span></span>
          {switch(k, t)}
        </div>'''
            k += 1
        groups += f'''<span style="font-size: 15px; font-weight: 600; margin: 6px 0 -4px 4px">{gname}</span>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 12px 0 16px; display: flex; flex-direction: column">{rhtml}</section>'''
    ons = [on for _g, rows in SETTINGS for (_t, _d, on) in rows]
    body = f'''  <div class="scr" style="bottom: 0; gap: 12px">
    <header style="display: flex; align-items: center; gap: 12px">{back('R7-Me.dc.html')}<h1 class="d" style="font-size: 40px">Settings</h1></header>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 14px 14px 16px; display: flex; align-items: center; gap: 12px">
      <img class="face" src="{IMG['naledi']}" alt="" style="width: 52px; height: 52px">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">Naledi</span><span style="font-size: 13px; color: {MUTED}">naledi@example.com</span></span>
      <button style="height: 44px; padding: 0 16px; border-radius: {R_M}px; background: {MIST}; font-size: 14px; font-weight: 600">Edit</button>
    </section>
    {groups}
    <span style="font-size: 15px; font-weight: 600; margin: 6px 0 -4px 4px">Your data</span>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">
      <div style="min-height: 64px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid {LINE7}"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {POOL}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic('pin', 20)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Stored in South Africa</span><span style="font-size: 13px; color: {MUTED}">Your data and its backups stay in the country</span></span></div>
      <button style="min-height: 56px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid {LINE7}; text-align: left"><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Download my data</span>{ic('download', 18, MUTED)}</button>
      <button style="min-height: 56px; display: flex; align-items: center; gap: 12px; text-align: left; color: {BLUSH_2}"><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Delete my account</span>{icon('chev', 18, BLUSH_2)}</button>
    </section>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%(sw)s
    const calm = v.sw6, big = v.sw7;
    v.setWaterY = 14; v.setPoolLabel = 'A moving pool'; v.wave = calm ? 'none' : '';
    v.aaSize = big ? 20 : 15; v.tSize = big ? 17 : 15; v.dSize = big ? 15 : 13;
    return v;
  }
}''' % dict(sw=switch_js(len(ons), ons))
    html = phone('Settings', body, logic, h=1260)
    # Reduce motion is live: the little pool stops moving.
    html = html.replace('<g class="wave">', '<g class="wave" style="animation: {{ wave }}">', 1)
    return html


# ---------------------------------------------------------------- Onboarding: what brings you here

GOALS = [('Build a safety net', 'pool'), ('Grow my business', 'shop'), ('Understand my payslip', 'doc'),
         ('Save with my stokvel', 'people'), ('Send money home', 'home'), ('Get on top of debt', 'down')]


def goals():
    tiles = ''.join(f'''<button onClick="[[ g{i} ]]" aria-pressed="[[ gOn{i} ]]" style="position: relative; height: 128px; border-radius: {R_L}px; background: [[ gBg{i} ]]; color: [[ gFg{i} ]]; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; text-align: left; transition: background-color .18s, color .18s">
          <span style="width: 44px; height: 44px; border-radius: {R_M}px; background: [[ gIc{i} ]]; color: {EVG}; display: flex; align-items: center; justify-content: center; transition: background-color .18s">{ic(icn, 22)}</span>
          <span style="font-size: 16px; font-weight: 600; line-height: 1.2">{t}</span>
          <sc-if value="[[ gOn{i} ]]" hint-placeholder-val="[[ {'true' if i < 2 else 'false'} ]]"><span aria-hidden="true" style="position: absolute; right: 12px; top: 12px; width: 26px; height: 26px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .4s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 16, EVG, 2.8)}</span></sc-if>
        </button>''' for i, (t, icn) in enumerate(GOALS))
    segs = ''.join(f'<span style="flex: 1 1 0; height: 6px; border-radius: 2px; background: {EVG}"></span>' for i in range(4))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    <header style="display: flex; align-items: center; gap: 14px">{back('R7-Auth-Consent.dc.html')}<div role="img" aria-label="Step 4 of 4" style="flex-grow: 1; display: flex; gap: 6px">{segs}</div><span style="font-size: 13px; color: {MUTED}">4 of 4</span></header>
    <h1 class="d" style="font-size: 40px; margin-top: 4px">What brings you here?</h1>
    <p style="font-size: 16px; line-height: 1.4; color: {SEC}; margin-top: -4px">Pick as many as you like. You can change this later.</p>
    <div role="group" aria-label="Your reasons" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ some ]]" hint-placeholder-val="[[ true ]]"><a href="R7-Starter.dc.html" style="height: 56px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">[[ goLabel ]]</a></sc-if>
    <sc-if value="[[ none ]]" hint-placeholder-val="[[ false ]]"><button disabled style="height: 56px; border-radius: {R_M}px; background: #DCE4DF; color: {MUTED}; font-size: 16px; font-weight: 600">Pick at least one</button></sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const on = st.on || [true, true, false, false, false, false];
    const n = on.filter(Boolean).length;
    const v = { some: n > 0, none: n === 0, goLabel: 'Continue with ' + n };
    for (let i = 0; i < 6; i++) {
      v['g' + i] = () => { const next = on.slice(); next[i] = !next[i]; this.setState({ on: next }); };
      v['gOn' + i] = on[i]; v['gBg' + i] = on[i] ? '%(evg)s' : '#FFFFFF'; v['gFg' + i] = on[i] ? '#FFFFFF' : '%(ink)s';
      v['gIc' + i] = on[i] ? '%(lime)s' : '%(mist)s';
    }
    return v;
  }
}''' % dict(evg=EVG, ink=INK, lime=LIME, mist=MIST)
    return phone('What brings you here', body, logic, h=844)


# ---------------------------------------------------------------- Welcome, photo-led

def mark(size, col, accent):
    """App icon A as a small mark: three stepping stones, each a little bigger."""
    return (f'<svg width="{size}" height="{size * 0.6:.0f}" viewBox="0 0 40 24" aria-hidden="true" style="display: block">'
            f'<ellipse cx="7" cy="19" rx="5" ry="3" fill="{col}"></ellipse><ellipse cx="19" cy="13" rx="6" ry="3.4" fill="{col}"></ellipse>'
            f'<ellipse cx="32" cy="6.5" rx="7" ry="4" fill="{accent}"></ellipse></svg>')


def welcome_photo():
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    <header style="display: flex; align-items: center; justify-content: space-between; height: 44px">
      <span style="display: flex; align-items: center; gap: 8px; color: {EVG}">{mark(34, EVG, LIME)}<span style="font-size: 26px; font-weight: 600; letter-spacing: -0.05em">awo</span></span>
      {sample_chip()}
    </header>
    <div style="position: relative; height: 350px; flex-shrink: 0">
      <img src="{IMG['phone_smile']}" alt="A woman laughing on a phone call" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 22%; border-radius: {R_L}px">
      <span style="position: absolute; left: 12px; top: 16px; height: 44px; padding: 0 14px 0 8px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: 0 6px 20px rgba(16,24,20,.14); display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; animation: rise .5s cubic-bezier(.2,.8,.2,1) .4s both"><span style="width: 28px; height: 28px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 16, EVG, 2.8)}</span>Lesson done</span>
      <span style="position: absolute; right: 12px; bottom: 14px; border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 12px 14px 12px 12px; display: flex; align-items: center; gap: 12px; box-shadow: 0 8px 24px rgba(10,51,38,.3); animation: rise .5s cubic-bezier(.2,.8,.2,1) .7s both">
        <span style="width: 26px; height: 44px">{pool(26, 44, 'wpPool', rimw=2, hole='wpY', label='wpLabel', static=True)}</span>
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {ON_EVG}">Safety net</span><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.03em">R 3 100</span></span>
      </span>
    </div>
    <h1 class="d" style="font-size: 42px">Money gets easier when we talk about it.</h1>
    <p style="font-size: 16px; line-height: 1.45; color: {SEC}">Learn with women who get it. See where you stand, then grow from there.</p>
    <div style="flex-grow: 1"></div>
    <a href="R7-Auth-Signin.dc.html" style="height: 56px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">Join for free</a>
    <a href="R7-Auth-Back.dc.html" style="height: 52px; flex-shrink: 0; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; margin-top: -6px">I have an account</a>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() { return { wpY: 18, wpLabel: 'Safety net, R 3 100' }; }
}'''
    return phone('Welcome, photo-led', body, logic, h=844)


BOARDS = [('R7-Entry', welcome_photo), ('R7-Goals', goals), ('R7-Progress', progress), ('R7-Checkin', checkin),
          ('R7-Buddy', buddy), ('R7-Settings', settings)]
