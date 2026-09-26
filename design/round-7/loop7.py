"""Round 7, batch 2: the loop, deeper. The lesson player, comparing versions, a what-if simulator,
"Check an offer" (AI, guarded), the printable DIVA report and the hard moments."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, back, sub_header, mark, R_S, R_M, R_L, LINE7  # noqa: E402
from kit7 import board7, KIT7_CSS  # noqa: E402
from auth7 import primary, with_css  # noqa: E402

HF = "font-family: '[[ handFont ]]', cursive"
RNG_CSS = KIT7_CSS[KIT7_CSS.index('.rng{'):]
FMT = "const fmt = (n) => 'R ' + String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' ');"


def fmt(n):
    return 'R ' + f'{n:,}'.replace(',', ' ')


# ---------------------------------------------------------------- The lesson player (Learn, night)

def lesson():
    bars = ''.join(f'<span style="flex: 1 1 0; height: 4px; border-radius: 2px; background: [[ bar{i} ]]; transition: background-color .28s"></span>' for i in range(5))
    circle = ''
    import math
    for k in range(12):
        a = math.radians(k * 30 - 90)
        x, y = 150 + 110 * math.cos(a), 130 + 110 * math.sin(a)
        circle += f'<span style="position: absolute; left: {x - 13:.0f}px; top: {y - 13:.0f}px; width: 26px; height: 26px; border-radius: 999px; background: {RAISED}; box-shadow: inset 0 0 0 2px {NLINE}"></span>'
    pot = (f'<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 300px; height: 260px; animation: potTurn 6s steps(12) infinite; transform-origin: 150px 130px">'
           f'<span style="position: absolute; left: 134px; top: 4px; width: 32px; height: 32px; border-radius: 999px; background: {LIME}; box-shadow: 0 0 20px rgba(216,243,106,.5)"></span></div>')
    opts = ''.join(f'<button onClick="[[ q{i} ]]" aria-pressed="[[ qOn{i} ]]" style="min-height: 56px; padding: 0 16px; border-radius: {R_M}px; background: {RAISED}; box-shadow: inset 0 0 0 [[ qBw{i} ]]px [[ qBd{i} ]]; display: flex; align-items: center; justify-content: space-between; font-size: 18px; font-weight: 600; font-variant-numeric: tabular-nums; transition: box-shadow .18s">{t}<sc-if value="[[ qTick{i} ]]" hint-placeholder-val="[[ false ]]">{icon("check", 20, LIME, 2.8)}</sc-if></button>'
                   for i, t in enumerate(['R 300', 'R 3 000', 'R 30 000']))
    parts = ''.join(f'<span aria-hidden="true" style="position: absolute; left: 50%; top: 50%; width: {s}px; height: {s}px; margin: -{s // 2}px 0 0 -{s // 2}px; border-radius: {2 if k % 2 else 999}px; background: {c}; --dx: {dx}px; --dy: {dy}px; animation: burst .8s cubic-bezier(.2,.8,.2,1) .2s both"></span>'
                    for k, (dx, dy, s, c) in enumerate([(-80, -50, 10, LIME), (70, -60, 8, MINT), (-60, 50, 8, MINT), (84, 34, 10, LIME), (0, -84, 7, LIME), (-90, 4, 7, MOON), (24, 74, 9, LIME)]))
    moons = ''.join(f'<span style="{"animation: pop .6s cubic-bezier(.34,1.56,.64,1) .5s both" if k == 2 else ""}">{moon(30, p, now=(k == 2))}</span>' for k, p in enumerate(['full', 'full', 'full', 'new', 'new', 'new']))
    body = f'''  <div style="position: absolute; inset: 0; padding: 52px 20px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
    <div style="display: flex; gap: 4px" role="img" aria-label="[[ progressLabel ]]">{bars}</div>
    <header style="display: flex; align-items: center; justify-content: space-between">
      <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Savings groups</span><span style="font-size: 13px; color: {NMUTED}">Lesson 3 of 6</span></span>
      <a href="R7-Learn.dc.html" aria-label="Close the lesson" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('close', 20, MOON, 2.2)}</a>
    </header>
    <div style="position: relative; flex-grow: 1; display: flex; flex-direction: column">
      <sc-if value="[[ c0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 18px; animation: storyIn .35s cubic-bezier(.2,.8,.2,1) both">
        <img src="{IMG['thandi_window']}" alt="Thandi at her window" style="width: 100%; height: 400px; object-fit: cover; object-position: 50% 30%; border-radius: {R_L}px">
        <h1 class="d" style="font-size: 34px">Thandi's stokvel has twelve members.</h1>
        <p style="font-size: 17px; line-height: 1.45; color: {NMUTED}">They have met on the first Sunday of every month for six years.</p></div></sc-if>
      <sc-if value="[[ c1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 22px; animation: storyIn .35s cubic-bezier(.2,.8,.2,1) both">
        <div role="img" aria-label="Twelve members in a circle. The pot moves from one to the next each month." style="position: relative; width: 300px; height: 260px; align-self: center; margin-top: 20px">{circle}{pot}
          <span style="position: absolute; left: 90px; top: 104px; width: 120px; text-align: center; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 26px; font-weight: 600; letter-spacing: -0.03em; color: {LIME}">R 6 000</span><span style="font-size: 13px; color: {NMUTED}">the pot</span></span></div>
        <h1 class="d" style="font-size: 32px">Each month, all twelve pay in R 500.</h1>
        <p style="font-size: 17px; line-height: 1.45; color: {NMUTED}">One member takes the whole pot home. Next month, it's someone else's turn.</p></div></sc-if>
      <sc-if value="[[ c2 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 18px; padding-top: 30px; animation: storyIn .35s cubic-bezier(.2,.8,.2,1) both">
        <span style="align-self: center; animation: bob 3.6s ease-in-out infinite">{ola('ls', 120)}</span>
        <div style="border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: {RAISED}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
          <span style="font-size: 14px; font-weight: 600; color: {MINT}">Ola</span>
          <p style="font-size: 19px; line-height: 1.45">Think of the pot moving around the circle. Everyone pays in the same amount, and everyone gets a turn to take it home.</p>
          <span class="chip" style="align-self: flex-start; background: {EVG}; color: #FFFFFF">{icon('check', 13, '#FFFFFF', 2.6)}Reviewed by AWO</span></div>
        <button onClick="[[ save ]]" aria-pressed="[[ saved ]]" style="align-self: flex-start; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ saveBg ]]; color: [[ saveFg ]]; display: flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 600; transition: background-color .18s">{icon('arch', 18)}[[ saveLabel ]]</button></div></sc-if>
      <sc-if value="[[ c3 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; padding-top: 24px; animation: storyIn .35s cubic-bezier(.2,.8,.2,1) both">
        <span class="lbl" style="color: {MINT}">Quick check</span>
        <h1 class="d" style="font-size: 30px">Ten women each pay R 300 a month. How big is the pot?</h1>
        <div role="radiogroup" aria-label="Your answer" style="display: flex; flex-direction: column; gap: 8px">{opts}</div>
        <p style="font-size: 16px; line-height: 1.45; color: [[ fbCol ]]; min-height: 46px">[[ feedback ]]</p></div></sc-if>
      <sc-if value="[[ c4 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; padding-top: 36px">
        <span style="position: relative; width: 88px; height: 88px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">{parts}{icon('check', 40, EVG, 2.8)}</span>
        <h1 class="d" style="font-size: 38px">Lesson done.</h1>
        <div role="img" aria-label="Three of six lessons done" style="display: flex; gap: 8px">{moons}</div>
        <div style="width: 100%; border-radius: {R_L}px; background: {RAISED}; padding: 16px; display: flex; flex-direction: column; gap: 8px; text-align: left; margin-top: 8px">
          <span style="font-size: 13px; font-weight: 600; color: {MINT}">Your small action</span>
          <span style="font-size: 17px; line-height: 1.4">Ask a friend in a stokvel what happens when someone misses a month.</span></div></div></sc-if>
      <sc-if value="[[ tapZones ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ prev ]]" aria-label="Previous card" style="position: absolute; left: 0; top: 0; bottom: 0; width: 30%"></button><button onClick="[[ next ]]" aria-label="Next card" style="position: absolute; right: 0; top: 0; bottom: 0; width: 70%"></button></sc-if>
    </div>
    <sc-if value="[[ notLast ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ next ]]" aria-disabled="[[ blocked ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: [[ nextBg ]]; color: [[ nextFg ]]; font-size: 16px; font-weight: 600; flex-shrink: 0">[[ nextLabel ]]</button></sc-if>
    <sc-if value="[[ last ]]" hint-placeholder-val="[[ false ]]"><a href="R7-Learn.dc.html" style="height: 56px; flex-shrink: 0; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">Back to Learn</a></sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const c = st.c || 0, q = st.q == null ? -1 : st.q, saved = !!st.saved;
    const blocked = c === 3 && q !== 1;
    const v = {
      progressLabel: 'Card ' + (c + 1) + ' of 5', tapZones: c < 2,
      prev: () => this.setState({ c: Math.max(0, c - 1) }), next: () => { if (!blocked) this.setState({ c: Math.min(4, c + 1) }); },
      notLast: c < 4, last: c === 4, blocked, nextLabel: c === 3 ? 'Continue' : 'Next',
      nextBg: blocked ? '%(raised)s' : '%(lime)s', nextFg: blocked ? '%(nm)s' : '%(evg)s',
      saved, save: () => this.setState({ saved: !saved }), saveLabel: saved ? 'Saved to your Vault' : 'Save "stokvel" to your Vault',
      saveBg: saved ? '%(lime)s' : '%(raised)s', saveFg: saved ? '%(evg)s' : '%(moon)s',
      feedback: q === 1 ? 'Yes. Ten times R 300 is R 3 000, and one member takes it home.' : (q >= 0 ? "Not quite. Everyone's R 300 goes into one pot: ten times R 300 is R 3 000." : ''),
      fbCol: q === 1 ? '%(lime)s' : '%(blush)s'
    };
    for (let i = 0; i < 5; i++) { v['c' + i] = c === i; v['bar' + i] = i <= c ? '%(moon)s' : '%(nline)s'; }
    for (let i = 0; i < 3; i++) {
      v['q' + i] = () => this.setState({ q: i }); v['qOn' + i] = q === i; v['qBw' + i] = q === i ? 2 : 0;
      v['qBd' + i] = q === i ? (i === 1 ? '%(lime)s' : '%(blush)s') : 'transparent'; v['qTick' + i] = q === 1 && i === 1;
    }
    return v;
  }
}''' % dict(raised=RAISED, lime=LIME, nm=NMUTED, evg=EVG, moon=MOON, blush=BLUSH, nline=NLINE)
    css = ('@keyframes potTurn{from{transform:rotate(0)}to{transform:rotate(360deg)}}'
           '@keyframes burst{0%{transform:translate(0,0) scale(.4);opacity:1}100%{transform:translate(var(--dx),var(--dy)) scale(1);opacity:0}}')
    return with_css(phone('Lesson: savings groups', body, logic, h=844, bg=NIGHT, dark=True, defs=ola_defs('ls')), css)


# ---------------------------------------------------------------- Compare two versions (Me)

VERS = [('Version 1', '13 Jul', 55, [66, 41, 57, 60], 'Early'), ('Version 2', '13 Aug', 59, [69, 44, 56, 64], 'Early'), ('Version 3', '13 Sep', 63, [71, 48, 60, 69], 'Building')]
DIM_NAMES = ['Everyday money', 'Ready for surprises', 'Knowing your options', 'Clear goals']


def compare():
    pick = lambda side, opts: ''.join(f'<button onClick="[[ {side}{i} ]]" aria-pressed="[[ {side}On{i} ]]" style="flex: 1 1 0; height: 52px; border-radius: 8px; background: [[ {side}Bg{i} ]]; box-shadow: [[ {side}Sh{i} ]]; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1px; transition: background-color .18s"><span style="font-size: 14px; font-weight: 600">{VERS[i][0]}</span><span style="font-size: 12px; color: {MUTED}">{VERS[i][1]}</span></button>' for i in opts)
    rows = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 10px 0; {f"border-bottom: 1px solid {LINE7};" if i < 3 else ""}">
          <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 13px; color: {MUTED}; font-variant-numeric: tabular-nums">[[ va{i} ]] to <b style="color: {INK}">[[ vb{i} ]]</b></span><span class="chip" style="height: 24px; background: [[ dBg{i} ]]; color: [[ dFg{i} ]]; font-variant-numeric: tabular-nums">[[ dt{i} ]]</span></span></span>
          <span aria-hidden="true" style="display: flex; flex-direction: column; gap: 3px"><span style="height: 6px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: [[ va{i} ]]%; background: #BFD9D2; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span><span style="height: 6px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: [[ vb{i} ]]%; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span></span></div>''' for i, n in enumerate(DIM_NAMES))
    changes = ''.join(f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 8px 0"><span style="width: 32px; height: 32px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; color: {EVG}; display: flex; align-items: center; justify-content: center">{g}</span><span style="font-size: 15px; line-height: 1.4; padding-top: 5px">{t}</span></div>'
                      for g, bg, t in [(icon('pool', 18), LIME, 'You now keep a separate pocket for surprises.'), (icon('moon', 18, MOON), NIGHT, 'You finished six lessons.'), (icon('stones', 18), POOL, 'Your savings goal now has a date.')])
    body = f'''  <div class="scr" style="bottom: 0; gap: 14px">
    {sub_header('R7-Progress.dc.html', 'Compare versions')}
    <div style="display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 8px 10px; align-items: center">
      <span style="font-size: 13px; font-weight: 600; color: {MUTED}">From</span><div role="group" aria-label="Compare from" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: #DCE4DF">{pick('a', [0, 1])}</div>
      <span style="font-size: 13px; font-weight: 600; color: {MUTED}">To</span><div role="group" aria-label="Compare to" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: #DCE4DF">{pick('b', [1, 2])}</div>
    </div>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 18px 16px; display: flex; flex-direction: column; gap: 8px">
      <span class="lbl">DIVA score</span>
      <span style="display: flex; align-items: baseline; gap: 12px"><span style="font-size: 28px; font-weight: 600; color: #6C8F84; font-variant-numeric: tabular-nums">[[ ra ]]</span>{icon('send', 22, EVG)}<span class="d" style="font-size: 64px; font-variant-numeric: tabular-nums">[[ rb ]]</span><span class="chip" style="background: {LIME}; color: {EVG}">[[ rdelta ]]</span></span>
      <span style="font-size: 14px; color: {SEC}">Stage 2 in both. Evidence: [[ ea ]] to [[ eb ]].</span>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 6px 16px">{rows}</section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 12px 16px; display: flex; flex-direction: column">
      <span style="font-size: 16px; font-weight: 600; padding: 4px 0">What changed in your answers</span>{changes}</section>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}; padding: 0 4px">{icon('lock', 16, MUTED)}Each version is kept exactly as it was. Nothing is recalculated.</span>
    <a href="R7-Report.dc.html" style="height: 52px; flex-shrink: 0; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600">{ic('download', 18, INK)}Download the one-page report</a>
  </div>'''
    vers = [[r, d, e] for _n, _d, r, d, e in VERS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const vs = %(vs)s;
    let a = st.a == null ? 0 : st.a, b = st.b == null ? 2 : st.b;
    if (b <= a) b = a + 1;
    const A = vs[a], B = vs[b];
    const d = B[0] - A[0];
    const v = { ra: A[0], rb: B[0], rdelta: (d >= 0 ? '+' : '') + d, ea: A[2].toLowerCase(), eb: B[2].toLowerCase() };
    for (const i of [0, 1]) { v['a' + i] = () => this.setState({ a: i, b: Math.max(b, i + 1) }); v['aOn' + i] = a === i; v['aBg' + i] = a === i ? '#FFFFFF' : 'transparent'; v['aSh' + i] = a === i ? '0 1px 3px rgba(16,24,20,.12)' : 'none'; }
    for (const i of [1, 2]) { v['b' + i] = () => this.setState({ b: i, a: Math.min(a, i - 1) }); v['bOn' + i] = b === i; v['bBg' + i] = b === i ? '#FFFFFF' : 'transparent'; v['bSh' + i] = b === i ? '0 1px 3px rgba(16,24,20,.12)' : 'none'; }
    for (let i = 0; i < 4; i++) {
      const x = A[1][i], y = B[1][i], dd = y - x;
      v['va' + i] = x; v['vb' + i] = y; v['dt' + i] = dd > 0 ? '+' + dd : (dd < 0 ? String(dd).replace('-', '\\u2212') : 'same');
      v['dBg' + i] = dd > 0 ? '%(lime)s' : '%(mist)s'; v['dFg' + i] = dd > 0 ? '%(evg)s' : '%(sec)s';
    }
    return v;
  }
}''' % dict(vs=vers, lime=LIME, mist='#E4EAE6', evg=EVG, sec=SEC)
    return phone('Compare versions', body, logic, h=1060)


# ---------------------------------------------------------------- What if (simulator)

def simulator():
    tabs = ''.join(f'<button onClick="[[ tab{i} ]]" aria-pressed="[[ tabOn{i} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ tabBg{i} ]]; box-shadow: [[ tabSh{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{t}</button>' for i, t in enumerate(['Safety net', "A loan's real cost"]))
    adds = ''.join(f'<button onClick="[[ ad{i} ]]" aria-pressed="[[ adOn{i} ]]" style="flex: 1 1 0; height: 44px; border-radius: {R_M}px; background: [[ adBg{i} ]]; color: [[ adFg{i} ]]; font-size: 14px; font-weight: 600">{fmt(a) if a else "Nothing"}</button>' for i, a in enumerate([0, 100, 250, 500]))
    terms = ''.join(f'<button onClick="[[ tm{i} ]]" aria-pressed="[[ tmOn{i} ]]" style="flex: 1 1 0; height: 44px; border-radius: {R_M}px; background: [[ tmBg{i} ]]; color: [[ tmFg{i} ]]; font-size: 14px; font-weight: 600">{m} months</button>' for i, m in enumerate([6, 12, 24]))

    def slider(sid, label, hole, lo, hi, step, text):
        return f'''<div style="display: flex; flex-direction: column; gap: 2px">
          <span style="display: flex; justify-content: space-between; align-items: baseline"><label for="{sid}" style="font-size: 14px; font-weight: 600">{label}</label><span style="font-size: 17px; font-weight: 600; font-variant-numeric: tabular-nums">[[ {text} ]]</span></span>
          <input id="{sid}" class="rng" style="--p: [[ {hole}Pct ]]%" type="range" min="{lo}" max="{hi}" step="{step}" value="[[ {hole} ]]" onInput="[[ set{hole} ]]" aria-valuetext="[[ {text} ]]"></div>'''
    body = f'''  <div class="scr" style="bottom: 0; gap: 14px">
    {sub_header('R7-Home.dc.html', 'What if')}
    <div role="group" aria-label="Choose a calculator" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: #DCE4DF">{tabs}</div>
    <sc-if value="[[ t0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 14px">
      <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 18px 16px; display: flex; gap: 18px; align-items: center">
        <div style="width: 70px; height: 150px; flex-shrink: 0">{pool(70, 150, 'simPool', rimw=2.5)}</div>
        <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {ON_EVG}">Your safety net would cover</span><span class="d" style="font-size: 50px; color: {LIME}">[[ runway ]]</span><span style="font-size: 14px; color: {ON_EVG}">of essentials, if your income stopped.</span></div>
      </section>
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 14px">
        {slider('sim-net', 'In your safety net', 'net', 0, 20000, 100, 'netText')}
        {slider('sim-ess', 'Essentials each month', 'ess', 1000, 30000, 500, 'essText')}
        <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 14px; font-weight: 600">Add each month</span><div role="group" aria-label="Add each month" style="display: flex; gap: 6px">{adds}</div></div>
        <p style="font-size: 16px; line-height: 1.45; border-top: 1px solid {LINE7}; padding-top: 12px">[[ addLine ]]</p>
      </section></div></sc-if>
    <sc-if value="[[ t1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 14px">
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 18px 16px; display: flex; flex-direction: column; gap: 10px">
        <span style="font-size: 14px; color: {SEC}">You'd pay back</span><span class="d" style="font-size: 50px; font-variant-numeric: tabular-nums">[[ total ]]</span>
        <div aria-hidden="true" style="display: flex; height: 16px; border-radius: 2px; overflow: hidden"><span style="width: [[ borrowPct ]]%; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span><span style="flex-grow: 1; background: #A9B6AF"></span></div>
        <span style="display: flex; justify-content: space-between; font-size: 14px"><span><b style="color: {EVG}">[[ amtText ]]</b> borrowed</span><span><b>[[ cost ]]</b> the cost of borrowing</span></span>
        <span style="font-size: 14px; color: {SEC}">[[ monthly ]] a month, for [[ months ]] months.</span>
      </section>
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 14px">
        {slider('sim-amt', 'Amount', 'amt', 1000, 50000, 500, 'amtText')}
        {slider('sim-rate', 'Interest a year', 'rate', 5, 60, 1, 'rateText')}
        <div role="group" aria-label="How long" style="display: flex; gap: 6px">{terms}</div>
      </section></div></sc-if>
    <div style="border-radius: {R_M}px; background: #E4EAE6; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start"><span class="chip" style="flex-shrink: 0; border: 1px dashed {SEC}; color: {SEC}">Illustration</span><span style="font-size: 13px; line-height: 1.45; color: {SEC}">[[ note ]]</span></div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(fmt)s
    const t = st.t || 0;
    const net = st.net == null ? 3100 : st.net, ess = st.ess == null ? 6000 : st.ess, add = st.add == null ? 100 : st.add;
    const amt = st.amt == null ? 5000 : st.amt, rate = st.rate == null ? 28 : st.rate, n = st.n == null ? 12 : st.n;
    const weeks = net / ess * 52 / 12;
    const runway = weeks < 1 ? 'Under a week' : (weeks < 8 ? Math.floor(weeks) + (Math.floor(weeks) === 1 ? ' week' : ' weeks') : (net / ess).toFixed(1).replace('.0', '') + ' months');
    const gap = Math.max(0, ess - net), toMonth = add > 0 ? Math.ceil(gap / add) : null;
    const r = rate / 100 / 12, pay = r > 0 ? amt * r / (1 - Math.pow(1 + r, -n)) : amt / n, total = pay * n;
    const adds = [0, 100, 250, 500], terms = [6, 12, 24];
    const v = {
      t0: t === 0, t1: t === 1, runway,
      net, netText: fmt(net), netPct: Math.round(net / 200), setnet: (e) => this.setState({ net: Number(e.target.value) }),
      ess, essText: fmt(ess), essPct: Math.round((ess - 1000) / 290), setess: (e) => this.setState({ ess: Number(e.target.value) }),
      waterY: Math.round(146 - Math.min(1, net / ess) * 140), poolLabel: 'Safety net ' + fmt(net) + ' against ' + fmt(ess) + ' of essentials a month',
      addLine: gap === 0 ? 'That already covers a full month of essentials.' : (add ? 'Adding ' + fmt(add) + ' a month, you would cover one month in ' + toMonth + ' months.' : 'Adding even a little each month makes the gap smaller.'),
      amt, amtText: fmt(amt), amtPct: Math.round((amt - 1000) / 490), setamt: (e) => this.setState({ amt: Number(e.target.value) }),
      rate, rateText: rate + '%%', ratePct: Math.round((rate - 5) / .55), setrate: (e) => this.setState({ rate: Number(e.target.value) }),
      total: fmt(total), cost: fmt(total - amt), monthly: fmt(pay), months: n, borrowPct: Math.round(amt / total * 100),
      note: t === 0 ? 'Simple arithmetic with no interest or fees. It shows how the numbers relate, not what you should do.' : 'Example rates. Real loans add fees and insurance; ask the lender for the total cost before you sign.'
    };
    for (const i of [0, 1]) { v['tab' + i] = () => this.setState({ t: i }); v['tabOn' + i] = t === i; v['tabBg' + i] = t === i ? '#FFFFFF' : 'transparent'; v['tabSh' + i] = t === i ? '0 1px 3px rgba(16,24,20,.12)' : 'none'; }
    for (let i = 0; i < 4; i++) { v['ad' + i] = () => this.setState({ add: adds[i] }); v['adOn' + i] = add === adds[i]; v['adBg' + i] = add === adds[i] ? '%(evg)s' : '%(mist)s'; v['adFg' + i] = add === adds[i] ? '#FFFFFF' : '%(ink)s'; }
    for (let i = 0; i < 3; i++) { v['tm' + i] = () => this.setState({ n: terms[i] }); v['tmOn' + i] = n === terms[i]; v['tmBg' + i] = n === terms[i] ? '%(evg)s' : '%(mist)s'; v['tmFg' + i] = n === terms[i] ? '#FFFFFF' : '%(ink)s'; }
    return v;
  }
}''' % dict(fmt=FMT, evg=EVG, mist=MIST, ink=INK)
    return with_css(phone('What if', body, logic, h=900), RNG_CSS)


# ---------------------------------------------------------------- Check an offer (Ask, AI with guard rails)

OFFER = [('Invest R 1 000 today and get R 5 000 back in 2 weeks, ', None), ('guaranteed', 0), ('! ', None), ('Only 3 spots left', 1), (' so reply fast. ', None),
         ('Bring 2 friends and earn a bonus', 2), ('. Pay by e-wallet to Coach Mike.', 3)]
FLAGS = [('Guaranteed returns', 'No real investment can promise what you will get back.'),
         ('Pressure to hurry', 'Scarcity and deadlines stop you from checking.'),
         ('Paid to recruit', 'Earning from new members is how pyramid schemes grow.'),
         ('No company you can look up', 'It names a person, not a registered provider.')]


def offer():
    text = ''.join(f'<span style="{f"background: [[ hl ]]; box-shadow: 0 2px 0 [[ ul ]]; border-radius: 3px; padding: 0 2px" if k is not None else ""}">{t}</span>' + (f'<sup style="font-size: 12px; font-weight: 700; color: {BLUSH}; display: [[ supShow ]]">{k + 1}</sup>' if k is not None else '') for t, k in OFFER)
    flags = ''.join(f'''<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; {f"border-bottom: 1px solid {NLINE};" if i < 3 else ""}">
          <span style="width: 26px; height: 26px; flex-shrink: 0; border-radius: {R_S}px; background: {BLUSH}; color: {BLUSH_INK}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700">{i + 1}</span>
          <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {NMUTED}">{d}</span></span></div>''' for i, (t, d) in enumerate(FLAGS))
    dots = ''.join(f'<span style="width: 8px; height: 8px; border-radius: 999px; background: {MINT}; animation: pulse 1.2s ease-in-out {d}s infinite"></span>' for d in (0, .2, .4))
    body = f'''  <div class="scr" style="bottom: 0; gap: 14px">
    <header style="display: flex; align-items: center; justify-content: space-between"><a href="R7-Ask.dc.html" aria-label="Back to Ask" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('back', 20, MOON, 2.2)}</a><span style="font-size: 17px; font-weight: 600">Check an offer</span><span class="chip" style="border: 1px dashed {MINT}; color: {MINT}">AI-assisted</span></header>
    <div style="display: flex; gap: 12px; align-items: center"><span style="flex-shrink: 0">{ola('of', 52)}</span><p style="font-size: 16px; line-height: 1.45">Paste a message or describe an offer. I'll look for the warning signs on AWO's list.</p></div>
    <div style="border-radius: {R_L}px; background: {RAISED}; padding: 16px; display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 13px; color: {NMUTED}">Pasted message</span>
      <p style="font-size: 17px; line-height: 1.6">{text}</p></div>
    <sc-if value="[[ idle ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ check ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600">Check for warning signs</button></sc-if>
    <sc-if value="[[ busy ]]" hint-placeholder-val="[[ false ]]"><div role="status" style="height: 56px; display: flex; align-items: center; gap: 10px; padding: 0 4px"><span style="display: flex; gap: 6px">{dots}</span><span style="font-size: 15px; color: {NMUTED}">Ola is checking</span></div></sc-if>
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 12px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
      <span style="display: flex; align-items: baseline; gap: 10px"><span class="d" style="font-size: 44px; color: {BLUSH}">4</span><span style="font-size: 20px; font-weight: 600">warning signs</span></span>
      <section style="border-radius: {R_L}px; background: {RAISED}; padding: 4px 16px">{flags}</section>
      <p style="font-size: 16px; line-height: 1.45">I can't tell you an offer is safe. I can only show the warning signs. Before paying anyone, look them up.</p>
      <a href="https://www.fsca.co.za" style="height: 52px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600">{ic('search', 18, EVG)}Look up a provider on the FSCA register</a>
      <a href="R7-Lesson.dc.html" style="min-height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600">{icon('moon', 18, MOON)}Learn how pyramid schemes work</a>
      <span style="font-size: 13px; line-height: 1.45; color: {NMUTED}">Checked against AWO's reviewed red-flag list, not the internet. This check is saved in your history, and you can delete it.</span>
      <button onClick="[[ reset ]]" style="height: 44px; align-self: flex-start; font-size: 15px; font-weight: 600; color: {MINT}">Check another</button></div></sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const phase = st.phase || 0;
    return {
      idle: phase === 0, busy: phase === 1, done: phase === 2,
      check: () => { this.setState({ phase: 1 }); setTimeout(() => this.setState({ phase: 2 }), 1400); },
      reset: () => this.setState({ phase: 0 }),
      hl: phase === 2 ? 'rgba(255,199,214,.16)' : 'transparent', ul: phase === 2 ? '%(blush)s' : 'transparent', supShow: phase === 2 ? 'inline' : 'none'
    };
  }
}''' % dict(blush=BLUSH)
    return phone('Check an offer', body, logic, h=1180, bg=NIGHT, dark=True, defs=ola_defs('of'))


# ---------------------------------------------------------------- The one-page DIVA report (A4)

DIMS = [('Everyday money', 'Financial Health, 40%', 71, 'Bills get paid and most spending is planned.'),
        ('Ready for surprises', 'Risk and Resilience, 25%', 48, 'A surprise cost would be hard to cover right now.'),
        ('Knowing your options', 'Capital Positioning, 20%', 60, "You know some ways to save and borrow, and you're exploring more."),
        ('Clear goals', 'Goal Clarity, 15%', 69, 'Your goals are clear. A date and an amount would sharpen them.')]


def report():
    pts = [(30, 70, 22, 9), (96, 52, 24, 10), (164, 34, 24, 10), (226, 16, 20, 8)]
    dash = ' stroke-dasharray="4 4"'
    st_svg = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[EVG, LIME, "none", "none"][i]}" stroke="{EVG}" stroke-width="2"{dash if i > 1 else ""}></ellipse>' for i, (x, y, rx, ry) in enumerate(pts))
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 190px 1fr 44px; gap: 16px; align-items: center; padding: 12px 0; border-bottom: 1px solid {LINE7}">
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{n}</span><span style="font-size: 12px; color: {MUTED}">{d}</span></span>
        <span style="display: flex; flex-direction: column; gap: 6px"><span style="height: 8px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: {v}%; background: {EVG}"></span></span><span style="font-size: 13px; line-height: 1.4; color: {SEC}">{t}</span></span>
        <span style="font-size: 20px; font-weight: 600; text-align: right; font-variant-numeric: tabular-nums">{v}</span></div>''' for n, d, v, t in DIMS)
    spark = (f'<svg width="200" height="60" viewBox="0 0 200 60" aria-hidden="true"><path d="M10 46L100 32L190 16" fill="none" stroke="{EVG}" stroke-width="2"></path>'
             + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{EVG if x == 190 else "#FFFFFF"}" stroke="{EVG}" stroke-width="2"></circle>' for x, y in [(10, 46), (100, 32), (190, 16)]) + '</svg>')
    inner = f'''<div style="position: absolute; inset: 0; padding: 56px 60px 44px; box-sizing: border-box; display: flex; flex-direction: column; gap: 22px; background: #FFFFFF">
  <header style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 18px; border-bottom: 2px solid {EVG}">
    <span style="display: flex; flex-direction: column; gap: 10px"><span style="display: flex; align-items: center; gap: 8px; color: {EVG}">{mark(34, EVG, LIME)}<span style="font-size: 26px; font-weight: 600; letter-spacing: -0.05em">awo</span></span><span style="font-size: 30px; font-weight: 600; letter-spacing: -0.03em">DIVA profile report</span></span>
    <span style="display: flex; flex-direction: column; align-items: flex-end; gap: 6px; font-size: 13px; color: {SEC}"><span style="font-size: 16px; font-weight: 600; color: {INK}">Naledi</span><span>Version 3, 13 September 2026</span>{sample_chip()}</span>
  </header>
  <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 20px">
    <div style="border-radius: 14px; background: {POOL}; padding: 18px 20px; display: flex; flex-direction: column; gap: 6px; color: {EVG}"><span style="font-size: 13px; font-weight: 600">Where you stand</span><span style="display: flex; align-items: baseline; gap: 8px"><span class="d" style="font-size: 56px">Stage 2</span><span style="font-size: 16px; font-weight: 600">of 4</span></span><svg width="250" height="84" viewBox="0 0 250 84" aria-hidden="true">{st_svg}</svg></div>
    <div style="display: flex; flex-direction: column; gap: 12px">
      <div style="border-radius: 14px; box-shadow: inset 0 0 0 1px {LINE7}; padding: 16px 18px; display: flex; align-items: center; gap: 14px"><div style="position: relative; width: 64px; height: 64px">{arc(64, 63, '#DCE4DF', EVG, sw=6)}<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 600">63</span></div><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">DIVA score 63</span><span style="font-size: 12px; color: {SEC}">Learning readiness, not a credit score.</span></span></div>
      <div style="border-radius: 14px; box-shadow: inset 0 0 0 1px {LINE7}; padding: 16px 18px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 15px; font-weight: 600">Evidence: building</span><span style="font-size: 12px; line-height: 1.4; color: {SEC}">Two check-ins included things you did, not only what you said. Kept apart from the score.</span></div>
    </div>
  </div>
  <section style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600; padding-bottom: 4px">Your four dimensions</span>{rows}</section>
  <section style="border-radius: 14px; background: {MIST}; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px">
    <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 600">What this means</span><span class="chip" style="background: {EVG}; color: #FFFFFF">{icon('check', 13, '#FFFFFF', 2.6)}Reviewed by AWO</span></span>
    <p style="font-size: 14px; line-height: 1.55">Your everyday money habits are a real strength. The most room to grow is being ready for surprises: an unexpected cost would likely knock your plans off course. A small, separate cushion, built a little at a time, is the next thing to learn about.</p></section>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px">
    <section style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; font-weight: 600">Your next step</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">Start a starter safety net: move R 100 into a separate pocket on payday. Next check-in: 13 October.</span></section>
    <section style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 14px; font-weight: 600">Your versions</span><span style="display: flex; align-items: center; gap: 14px">{spark}<span style="font-size: 12px; color: {SEC}; line-height: 1.5">55 in July<br>59 in August<br>63 in September</span></span></section>
  </div>
  <div style="flex-grow: 1"></div>
  <footer style="display: flex; justify-content: space-between; gap: 20px; padding-top: 14px; border-top: 1px solid {LINE7}; font-size: 12px; line-height: 1.5; color: {MUTED}"><span style="max-width: 560px">AWO gives education, not financial advice. This report describes learning readiness; it is not a credit score and says nothing about loans or eligibility. Your data is stored in South Africa. Sample data.</span><span>Page 1 of 1</span></footer>
</div>'''
    from marketing import canvas_board
    html = canvas_board('DIVA report, one page (A4)', 794, 1123, '#FFFFFF', inner)
    return html


# ---------------------------------------------------------------- The hard moments

def hard():
    def ph(inner, bg=MIST, dark=False):
        return f'<div class="ph{" dk" if dark else ""}" style="background: {bg}; color: {MOON if dark else INK}"><div style="position: absolute; inset: 0; padding: 56px 20px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">{inner}</div></div>'

    def cap(t, d):
        return f'<span style="display: flex; flex-direction: column; gap: 4px; height: 68px"><span style="font-size: 18px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">{d}</span></span>'
    card = f'border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 10px'
    empty_pool = pool(56, 110, 'hpA', rimw=2.5, static=True, hole='hA', label='hAL').replace('{{ hA }}', '106').replace('{{ hAL }}', 'An empty safety net')
    day1 = ph(f'''<span style="font-size: 14px; color: {MUTED}">Thursday 25 September</span><h1 class="d" style="font-size: 36px">Hi Naledi.</h1>
      <p style="font-size: 17px; line-height: 1.4; color: {SEC}; margin-top: -6px">Your first week starts with one small thing.</p>
      <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 18px; display: flex; gap: 18px; align-items: center">{empty_pool}<span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; color: {ON_EVG}">Safety net</span><span class="d" style="font-size: 36px; color: {LIME}">R 0 so far</span><span style="font-size: 14px; line-height: 1.4; color: {ON_EVG}">It starts with your first R 100.</span></span></section>
      <section style="{card}"><span style="font-size: 13px; color: {MUTED}">This week</span><span style="font-size: 18px; font-weight: 600">Start a starter safety net</span>{primary('Open this step', '#', h=48)}</section>
      <section style="{card}; flex-direction: row; align-items: center; gap: 14px"><span style="width: 52px; height: 52px; flex-shrink: 0; box-sizing: border-box; border-radius: 999px; border: 2px dashed {BLUSH_2}"></span><span style="font-size: 15px; line-height: 1.4; color: {SEC}">Wins from your circle will show up here.</span></section>''')
    missed = ph(f'''<h1 class="d" style="font-size: 36px">Hey Naledi.</h1>
      <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; align-items: center; gap: 10px">{icon('stones', 24, EVG)}<span style="font-size: 18px; font-weight: 600">Your check-in is ready.</span></span>
        <span style="font-size: 16px; line-height: 1.45; color: {INK}">Three questions, whenever it suits you. It was due on 13 October; take it when you're ready.</span>
        <span style="display: flex; gap: 8px"><a href="R7-Checkin.dc.html" style="flex: 1 1 0; height: 48px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">Start</a><button style="flex: 1 1 0; height: 48px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {EVG}; font-size: 15px; font-weight: 600">Tomorrow</button></span>
        <span style="font-size: 13px; color: {SEC}">Last month's version stays exactly as it was.</span></section>
      <div style="opacity: .45; display: flex; flex-direction: column; gap: 12px"><section style="{card}; height: 150px"></section><section style="{card}; height: 110px"></section></div>''')
    comeback = ph(f'''<h1 class="d" style="font-size: 36px">Welcome back, Naledi.</h1>
      <span class="hand" style="font-size: 26px; color: {EVG}; {HF}; margin-top: -4px">Good to see you.</span>
      <p style="font-size: 16px; line-height: 1.45; color: {SEC}">It's been five weeks. Nothing was lost, and nothing needs catching up.</p>
      <section style="border-radius: {R_L}px; background: {NIGHT}; color: {MOON}; padding: 16px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; color: {NMUTED}">Pick up where you left off</span><span style="font-size: 18px; font-weight: 600">Savings groups, lesson 3 of 6</span><span style="display: flex; gap: 6px">{moon(20, 'full')}{moon(20, 'full')}{moon(20, 'half', now=True)}{moon(20, 'new')}{moon(20, 'new')}{moon(20, 'new')}</span></section>
      <section style="{card}; flex-direction: row; align-items: center; gap: 14px"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; display: flex; align-items: center; justify-content: center">{icon('pool', 20, LIME)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Safety net: R 1 800</span><span style="font-size: 13px; color: {MUTED}">Just as you left it.</span></span></section>
      <section style="{card}; flex-direction: row; align-items: center; gap: 12px"><span style="display: flex">{''.join(f'<img class="face" src="{IMG[k]}" alt="" style="width: 32px; height: 32px; margin-left: {0 if j == 0 else -9}px; box-shadow: 0 0 0 2px #FFFFFF">' for j, k in enumerate(("wanjiru", "amara", "thandi")))}</span><span style="font-size: 15px">3 new wins in your circle</span></section>''')
    down_pool = pool(64, 140, 'hpD', rimw=2.5, static=True, hole='hD', label='hDL').replace('{{ hD }}', '112').replace('{{ hDL }}', 'The safety net, lower than last month')
    down = ph(f'''<span class="lbl" style="color: {EVG}">Check-in, this month</span>
      <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 20px; display: flex; gap: 20px; align-items: center">{down_pool}<span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {ON_EVG}">Safety net</span><span style="font-size: 20px; color: #9FB8AE; text-decoration: line-through; font-variant-numeric: tabular-nums">R 1 800</span><span class="d" style="font-size: 42px; color: #FFFFFF; font-variant-numeric: tabular-nums">R 900</span></span></section>
      <h1 class="d" style="font-size: 30px">It went down by R 900. That's what it's for.</h1>
      <p style="font-size: 16px; line-height: 1.45; color: {SEC}">It covered a surprise, so the month didn't knock you off course. Topping it up can start small.</p>
      {primary('Plan the top-up', '#', h=52)}<button style="height: 44px; font-size: 15px; font-weight: 600; color: {EVG}">Not this month</button>''')
    offline = ph(f'''<div style="border-radius: {R_M}px; background: {INK}; color: {MOON}; padding: 12px 14px; display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 500"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M2 8.8a15 15 0 0 1 4.2-2.6M9.8 5.2A15 15 0 0 1 22 8.8M8.5 16.4a5 5 0 0 1 7 0M12 20h.01M3 3l18 18"></path></svg>You're offline. Saved lessons still work.</div>
      <h1 class="d" style="font-size: 36px">Learn</h1>
      {''.join(f'<section style="border-radius: {R_L}px; background: {RAISED}; padding: 14px 16px; display: flex; align-items: center; gap: 12px">{moon(26, p)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MINT if s else NMUTED}">{"Saved on this phone" if s else "Needs a connection"}</span></span></section>' for t, p, s in [("Savings groups", "half", True), ("Sending money home", "cres", True), ("Your first payslip", "new", False)])}
      <section style="border-radius: {R_L}px; box-shadow: inset 0 0 0 1px {NLINE}; padding: 16px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 16px; font-weight: 600">That didn't load.</span><span style="font-size: 14px; line-height: 1.4; color: {NMUTED}">Your answers are safe on this phone. We'll send them when you're back online.</span><button style="align-self: flex-start; height: 44px; padding: 0 16px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 14px; font-weight: 600">Try again</button></section>''', bg=NIGHT, dark=True)
    cols = [('Day one', 'Nothing to show yet, so show the first step, not empty charts.', day1),
            ('A check-in waiting', 'No red, no countdown and no penalty. Last month stays as it was.', missed),
            ('Coming back after weeks', 'No streak lost, nothing to catch up. The hand says hello.', comeback),
            ('A month that went down', 'Grey, not red. A safety net that gets used did its job.', down),
            ('Offline, or failed', 'Say what still works. Answers wait on the phone.', offline)]
    body = f'<div style="display: flex; gap: 48px">' + ''.join(f'<div style="display: flex; flex-direction: column; gap: 16px; width: 390px">{cap(t, d)}{p}</div>' for t, d, p in cols) + '</div>'
    return board7('Hard moments', "The screens that decide whether she trusts us: the first empty day, a late check-in, coming back after weeks away, a month that went down, and no signal.", body, static_logic(), 2254, 1200, chip='Sample content')


BOARDS = [('R7-Lesson', lesson), ('R7-Compare', compare), ('R7-Simulator', simulator), ('R7-Offer', offer), ('R7-Report', report), ('R7-Hard', hard)]
