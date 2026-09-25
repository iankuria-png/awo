"""Round 7, batch 3: entrepreneurs (D-018). Wanjiru runs a homeware stall in Nairobi, so money is in KSh.
The business check's questions and stages are samples: the real assessment content is AWO's to supply."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, sub_header, R_S, R_M, R_L, LINE7  # noqa: E402
from auth7 import primary, disabled, title  # noqa: E402

HF = "font-family: '[[ handFont ]]', cursive"
NB = ' '

GROUPS = [('What kind of business?', ['Market stall', 'Shop', 'Services', 'Online', 'Farming', 'Something else'], False, [0]),
          ('How long has it been running?', ['Under a year', '1 to 3 years', 'Over 3 years'], False, [1]),
          ('How does money come in?', ['Cash', 'Mobile money', 'Bank transfer', 'Card'], True, [0, 1]),
          ('Who works in it?', ['Just me', 'Me and family', 'Staff too'], False, [0])]


def profile():
    blocks = ''
    for g, (q, opts, multi, _d) in enumerate(GROUPS):
        chips = ''.join(f'<button onClick="[[ g{g}o{i} ]]" aria-pressed="[[ g{g}On{i} ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ g{g}Bg{i} ]]; color: [[ g{g}Fg{i} ]]; box-shadow: inset 0 0 0 1px [[ g{g}Bd{i} ]]; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 6px; transition: background-color .18s"><sc-if value="[[ g{g}On{i} ]]" hint-placeholder-val="[[ false ]]">{icon("check", 14, LIME, 3)}</sc-if>{o}</button>' for i, o in enumerate(opts))
        blocks += f'''<div style="display: flex; flex-direction: column; gap: 10px"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600">{q}</span>{f'<span style="font-size: 12px; color: {MUTED}">Pick any</span>' if multi else ''}</span><div role="group" aria-label="{q}" style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div></div>'''
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 18px">
    {sub_header('R7-Me.dc.html', 'Your business')}
    <div style="display: flex; flex-direction: column; gap: 10px">{title('Tell us about your business.', 'Two minutes. It shapes your business lessons and your business check.', 34)}</div>
    <div style="display: flex; flex-direction: column; gap: 6px"><label for="bz-name" style="font-size: 13px; font-weight: 600">Business name <span style="font-weight: 400; color: {MUTED}">(optional)</span></label>
      <input id="bz-name" value="Wanjiru's Homeware" style="height: 52px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 0 16px; font-size: 17px; font-weight: 500; color: {INK}"></div>
    {blocks}
    <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}">{icon('lock', 16, MUTED)}Only you see these answers.</span>
    {primary('Start the business check', 'R7-Biz-Check.dc.html')}
  </div>'''
    defaults = {g: d for g, (_q, _o, _m, d) in enumerate(GROUPS)}
    sizes = [len(o) for _q, o, _m, _d in GROUPS]
    multi = [m for _q, _o, m, _d in GROUPS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const sizes = %(sizes)s, multi = %(multi)s, defs = %(defs)s;
    const v = {};
    for (let g = 0; g < sizes.length; g++) {
      const sel = st['g' + g] || defs[g];
      for (let i = 0; i < sizes[g]; i++) {
        const on = sel.indexOf(i) >= 0;
        v['g' + g + 'o' + i] = () => { let n = multi[g] ? (on ? sel.filter((x) => x !== i) : sel.concat([i])) : [i]; this.setState({ ['g' + g]: n }); };
        v['g' + g + 'On' + i] = on; v['g' + g + 'Bg' + i] = on ? '%(evg)s' : '#FFFFFF'; v['g' + g + 'Fg' + i] = on ? '#FFFFFF' : '%(ink)s'; v['g' + g + 'Bd' + i] = on ? '%(evg)s' : '#C9D3CE';
      }
    }
    return v;
  }
}''' % dict(sizes=sizes, multi=str(multi).lower(), defs=[defaults[g] for g in range(len(GROUPS))], evg=EVG, ink=INK)
    return phone('Your business', body, logic, h=1000)


# ---------------------------------------------------------------- The business check (sample questions)

QS = [('Do you keep business money apart from home money?', ['Yes, always', 'Sometimes', 'Not yet']),
      ('Do you know what the stall made last month, after costs?', ['Yes, exactly', 'Roughly', 'Not really']),
      ('If sales dropped for a month, could the business keep going?', ['Yes', 'For a few weeks', 'Not really']),
      ('Do you write down what you sell?', ['Every day', 'Some days', 'Not yet'])]
AREAS_B = [('Money kept apart', 72), ('Knowing your numbers', 38), ('Ready for a slow month', 50), ('Records', 44)]


def check():
    qcards = ''
    for k, (q, opts) in enumerate(QS):
        os_ = ''.join(f'<button onClick="[[ a{k}_{j} ]]" aria-pressed="[[ s{k}_{j} ]]" style="min-height: 60px; padding: 0 16px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ b{k}_{j} ]]px {EVG}; display: flex; align-items: center; justify-content: space-between; font-size: 16px; font-weight: 500; text-align: left; transition: box-shadow .18s">{o}<span aria-hidden="true" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 999px; border: 2px solid [[ rc{k}_{j} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: [[ rf{k}_{j} ]]"></span></span></button>' for j, o in enumerate(opts))
        qcards += f'''<sc-if value="[[ q{k} ]]" hint-placeholder-val="[[ {'true' if k == 0 else 'false'} ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
          <span class="lbl" style="color: {EVG}">Question {k + 1} of 4</span><h1 class="d" style="font-size: 32px">{q}</h1>
          <div role="radiogroup" aria-label="Your answer" style="display: flex; flex-direction: column; gap: 8px">{os_}</div></div></sc-if>'''
    bars = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 6px"><span style="display: flex; justify-content: space-between; font-size: 14px"><span style="font-weight: 600">{n}</span><span style="color: {MUTED}">{"Your focus" if i == 1 else ""}</span></span>
          <span style="height: 8px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="display: block; height: 100%; width: {v}%; background: {LIME if i == 1 else EVG}; transform-origin: left; animation: fill .6s cubic-bezier(.2,.8,.2,1) {0.2 + i * 0.1:.1f}s both"></span></span></div>''' for i, (n, v) in enumerate(AREAS_B))
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 18px">
    <header style="display: flex; align-items: center; gap: 14px"><a href="R7-Biz-Profile.dc.html" aria-label="Back" style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('back', 20, INK, 2.2)}</a>
      <div role="img" aria-label="[[ stepLabel ]]" style="flex-grow: 1; display: flex; gap: 6px">{''.join(f'<span style="flex: 1 1 0; height: 6px; border-radius: 2px; background: [[ seg{i} ]]"></span>' for i in range(4))}</div>{sample_chip(MUTED, 'Sample questions')}</header>
    {qcards}
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 14px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
      <span class="lbl" style="color: {EVG}">Your business check</span>
      <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 20px 18px; display: flex; flex-direction: column; gap: 10px">
        <span style="font-size: 15px; color: {ON_EVG}">Wanjiru's Homeware is at</span>
        <span style="display: flex; align-items: baseline; gap: 10px"><span class="d" style="font-size: 60px; color: {LIME}">Stage 2</span><span style="font-size: 18px; font-weight: 600">of 4</span></span>
        <span style="font-size: 14px; line-height: 1.4; color: {ON_EVG}">This describes learning readiness for your business. It isn't a loan or credit decision.</span></section>
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 14px">{bars}</section>
      <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 16px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; font-weight: 600">A first business step</span><span style="font-size: 18px; font-weight: 600; color: {INK}">Keep a sales notebook for seven evenings.</span><span style="font-size: 14px; color: {INK}">Write what came in and what went out. That's all.</span></section>
    </div></sc-if>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ notDone ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ next ]]" aria-disabled="[[ blocked ]]" style="height: 56px; width: 100%; flex-shrink: 0; border-radius: {R_M}px; background: [[ nextBg ]]; color: [[ nextFg ]]; font-size: 16px; font-weight: 600">[[ nextLabel ]]</button></sc-if>
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]">{primary('Go to my business', 'R7-Biz-Home.dc.html')}</sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const q = st.q || 0, ans = st.ans || [-1, -1, -1, -1];
    const blocked = q < 4 && ans[q] < 0;
    const v = {
      done: q === 4, notDone: q < 4, blocked, stepLabel: q < 4 ? 'Question ' + (q + 1) + ' of 4' : 'Done',
      next: () => { if (!blocked) this.setState({ q: q + 1 }); }, nextLabel: q === 3 ? 'See my business check' : 'Next',
      nextBg: blocked ? '#DCE4DF' : '%(evg)s', nextFg: blocked ? '%(mut)s' : '#FFFFFF'
    };
    for (let i = 0; i < 4; i++) { v['q' + i] = q === i; v['seg' + i] = i <= q ? '%(evg)s' : '#DCE4DF'; }
    for (let k = 0; k < 4; k++) for (let j = 0; j < 3; j++) {
      const on = ans[k] === j;
      v['a' + k + '_' + j] = () => { const n = ans.slice(); n[k] = j; this.setState({ ans: n }); };
      v['s' + k + '_' + j] = on; v['b' + k + '_' + j] = on ? 2 : 0; v['rc' + k + '_' + j] = on ? '%(evg)s' : '#A9B6AF'; v['rf' + k + '_' + j] = on ? '%(evg)s' : 'transparent';
    }
    return v;
  }
}''' % dict(evg=EVG, mut=MUTED)
    return phone('Business check', body, logic, h=900)


# ---------------------------------------------------------------- Home, business view

WEEK = [('Mon', 3800, 1200), ('Tue', 2900, 900), ('Wed', 4100, 2600), ('Thu', 3300, 700), ('Fri', 5200, 1500), ('Sat', 6400, 3100), ('Sun', 0, 0)]


def biz_home():
    mx = 6400
    chart = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px">
          <span style="height: 96px; display: flex; align-items: flex-end; gap: 3px"><span style="width: 10px; height: {max(2, round(i_ / mx * 96))}px; border-radius: 2px 2px 0 0; background: {EVG}; transform-origin: bottom; animation: grow .6s cubic-bezier(.2,.8,.2,1) {0.1 + k * 0.05:.2f}s both"></span><span style="width: 10px; height: {max(2, round(o_ / mx * 96))}px; border-radius: 2px 2px 0 0; background: #A9B6AF; transform-origin: bottom; animation: grow .6s cubic-bezier(.2,.8,.2,1) {0.12 + k * 0.05:.2f}s both"></span></span>
          <span style="font-size: 12px; color: {INK if d == 'Sat' else MUTED}; font-weight: {600 if d == 'Sat' else 400}">{d}</span></div>''' for k, (d, i_, o_) in enumerate(WEEK))
    days = ''.join(f'<span style="flex: 1 1 0; height: 30px; border-radius: {R_S}px; background: {LIME if k < 4 else "rgba(255,255,255,.14)"}; color: {EVG if k < 4 else ON_EVG}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600">{d[0]}</span>' for k, (d, _i, _o) in enumerate(WEEK))
    body = f'''  <div class="scr" style="gap: 14px">
    <div role="group" aria-label="View" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: #DCE4DF">
      <a href="R7-Home.dc.html" style="flex: 1 1 0; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; color: {MUTED}">Me</a>
      <span aria-current="page" style="flex: 1 1 0; height: 40px; border-radius: 8px; background: #FFFFFF; box-shadow: 0 1px 3px rgba(16,24,20,.12); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600">My business</span></div>
    <header style="display: flex; align-items: center; gap: 12px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 44px; height: 44px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.03em">Wanjiru's Homeware</span><span style="font-size: 13px; color: {MUTED}">Market stall, Nairobi</span></span>{sample_chip()}</header>
    <section style="position: relative; border-radius: {R_L}px; overflow: hidden; background: {EVG}; color: #FFFFFF">
      <img src="{IMG['wanjiru_stall']}" alt="Wanjiru's homeware stall" style="width: 100%; height: 150px; object-fit: cover; object-position: 60% 38%; display: block">
      <div style="padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 10px">
        <span style="font-size: 13px; color: {ON_EVG}">This week's business step</span>
        <span style="font-size: 20px; font-weight: 600; line-height: 1.25">Keep a sales notebook for seven evenings.</span>
        <div role="img" aria-label="Done four evenings of seven" style="display: flex; gap: 4px">{days}</div></div>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600">Your notebook, this week</span><span style="font-size: 12px; color: {MUTED}">Your own notes</span></span>
      <span style="display: flex; gap: 22px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {MUTED}">Came in</span><span style="font-size: 22px; font-weight: 600; color: {EVG}; font-variant-numeric: tabular-nums">KSh{NB}25{NB}700</span></span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: {MUTED}">Went out</span><span style="font-size: 22px; font-weight: 600; color: {SEC}; font-variant-numeric: tabular-nums">KSh{NB}10{NB}000</span></span></span>
      <div role="img" aria-label="Daily money in and out, Monday to Saturday. Saturday was the busiest day." style="display: flex; gap: 4px; border-bottom: 1px solid {LINE7}; padding-bottom: 2px">{chart}</div>
      <span style="display: flex; gap: 14px; font-size: 12px; color: {MUTED}"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {EVG}"></span>In</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: #A9B6AF"></span>Out</span></span>
      <sc-if value="[[ notAdded ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ add ]]" style="height: 48px; border-radius: {R_M}px; background: {MIST}; font-size: 15px; font-weight: 600">Add today's numbers</button></sc-if>
      <sc-if value="[[ added ]]" hint-placeholder-val="[[ false ]]"><div role="status" style="height: 48px; border-radius: {R_M}px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 14px; font-size: 14px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both"><span style="width: 24px; height: 24px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 14, EVG, 3)}</span>Saved. Only you see your notebook.</div></sc-if>
    </section>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
      <a href="R7-Vault.dc.html" style="border-radius: 60px 60px {R_L}px {R_L}px; background: {LIME}; color: {EVG}; padding: 26px 14px 14px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 4px; min-height: 150px; box-sizing: border-box"><span style="font-size: 12px; font-weight: 600">Word for your business</span><span class="d" style="font-size: 30px">Float</span><span style="font-size: 13px; color: {INK}">Cash in the till for change</span></a>
      <a href="R7-Lesson.dc.html" style="border-radius: {R_L}px; background: {NIGHT}; color: {MOON}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; min-height: 150px; box-sizing: border-box">{moon(28, 'cres')}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Pricing for profit</span><span style="font-size: 12px; color: {NMUTED}">Lesson 1 of 5, 4 min</span></span></a>
    </div>
    <a href="R7-Community.dc.html" style="border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 14px 16px; display: flex; align-items: center; gap: 12px"><span style="display: flex">{''.join(f'<img class="face" src="{IMG[k]}" alt="" style="width: 30px; height: 30px; margin-left: {0 if j == 0 else -9}px; box-shadow: 0 0 0 2px {BLUSH}">' for j, k in enumerate(('zodwa', 'lindiwe', 'grace')))}</span><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Side hustles circle</span><span class="chip" style="background: {BLUSH_INK}; color: {BLUSH}">2 new</span></a>
  </div>
  {tabbar6('Home')}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    return { added: !!st.added, notAdded: !st.added, add: () => this.setState({ added: true }) };
  }
}'''
    html = phone('My business', body, logic, h=1140)
    return html.replace('href="R6-', 'href="R7-')


BOARDS = [('R7-Biz-Profile', profile), ('R7-Biz-Check', check), ('R7-Biz-Home', biz_home)]
