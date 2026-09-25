"""Round 7 redesigns of Vault, Me and Community, written natively in Round 7 style
(Geist, corners 6/10/14, the area shape as the hero, far less text). Ian: "the weakest in hierarchy,
design and UI/UX: generic and text heavy". Rules: one hero per screen, objects instead of rows,
short copy, handwriting only where the rules allow it."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403

HF = "font-family: '[[ handFont ]]', cursive"
R_S, R_M, R_L = 6, 10, 14


# ---------------------------------------------------------------- Vault

COLLECTIONS = [
    ('Saving together', [('Stokvel', 'Members take turns with the pot'), ('Chama', 'A savings group, in Kenya'), ('Safety net', 'Money kept only for surprises')]),
    ('Borrowing', [('Interest', 'The price of borrowing'), ('Credit record', 'How lenders see your history')]),
    ('Business', [('Cash flow', 'Money in and out, over time'), ('Float', 'Cash in the till for change')]),
    ('Sending home', [('Remittance fee', 'The cost of sending money'), ('Exchange rate', 'What one currency buys of another')]),
]
PRACTICE = [('Interest', 'The price of borrowing money, or the reward for saving it.'),
            ('Float', 'Cash kept in the till to give change and run the day.'),
            ('Remittance fee', 'What it costs to send money home.')]


def vault():
    tiles = ''
    for i, (name, words) in enumerate(COLLECTIONS):
        tiles += f'''<button onClick="[[ col{i} ]]" aria-pressed="[[ colOn{i} ]]" style="height: 128px; border-radius: {R_L}px; background: [[ colBg{i} ]]; box-shadow: inset 0 0 0 [[ colBw{i} ]]px {EVG}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; text-align: left; transition: background-color .18s">
          <span aria-hidden="true" style="position: relative; height: 50px; display: block">
            <span style="position: absolute; left: 14px; top: 2px; width: 96px; height: 40px; border-radius: {R_S}px; background: #DCE4DF; transform: rotate(6deg)"></span>
            <span style="position: absolute; left: 6px; top: 4px; width: 96px; height: 40px; border-radius: {R_S}px; background: #EAF0EC; transform: rotate(-3deg)"></span>
            <span style="position: absolute; left: 0; top: 8px; width: 104px; height: 40px; box-sizing: border-box; border-radius: {R_S}px; background: #FFFFFF; box-shadow: 0 0 0 1px #DCE4DF; display: flex; align-items: center; padding: 0 10px; font-size: 13px; font-weight: 600; color: {EVG}">{words[0][0]}</span>
          </span>
          <span style="display: flex; justify-content: space-between; align-items: baseline; gap: 6px"><span style="font-size: 15px; font-weight: 600; line-height: 1.2">{name}</span><span style="font-size: 13px; color: {MUTED}">{len(words)}</span></span>
        </button>'''
    panels = ''
    for i, (name, words) in enumerate(COLLECTIONS):
        cards = ''.join(f'<div style="border-radius: {R_M}px; background: #FFFFFF; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600">{w}</span><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{m}</span></div>' for w, m in words)
        panels += f'<sc-if value="[[ colOn{i} ]]" hint-placeholder-val="[[ {"true" if i == 0 else "false"} ]]"><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{cards}</div></sc-if>'
    cards_overlay = ''
    for k, (w, m) in enumerate(PRACTICE):
        cards_overlay += f'''<sc-if value="[[ p{k} ]]" hint-placeholder-val="[[ false ]]">
          <div style="display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
            <span style="font-size: 13px; color: {ON_EVG}">{k + 1} of 3</span>
            <span class="d" style="font-size: 44px; color: {LIME}">{w}</span>
            <sc-if value="[[ revealed ]]" hint-placeholder-val="[[ false ]]"><p style="font-size: 17px; line-height: 1.45; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{m}</p></sc-if>
          </div>
        </sc-if>'''
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: center; justify-content: space-between">
      <h1 class="d" style="font-size: 44px">Vault</h1>
      <span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 14px; color: {MUTED}">9 words kept</span>
        <button aria-label="Search money words" style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('search', 20, INK)}</button></span>
    </header>
    <div style="position: relative; height: 322px; perspective: 1400px; flex-shrink: 0">
      <div class="flipper" style="transform: [[ flipTf ]]">
        <section class="face-f" aria-hidden="[[ flipped ]]" style="border-radius: 175px 175px {R_L}px {R_L}px; background: {LIME}; color: {EVG}; padding: 72px 28px 22px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px">
          <span class="lbl">Word of the week</span>
          <span class="d" style="font-size: 60px">Stokvel</span>
          <span style="font-size: 15px">stok-fel</span>
          <span style="font-size: 17px; line-height: 1.35; color: {INK}; max-width: 250px">A savings group that takes turns with the pot.</span>
          <button tabindex="[[ frontTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{icon('flip', 18, '#FFFFFF')}See an example</button>
        </section>
        <section class="face-b" aria-hidden="[[ notFlipped ]]" style="border-radius: 175px 175px {R_L}px {R_L}px; background: {EVG}; color: #FFFFFF; padding: 76px 28px 22px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px">
          <span class="lbl" style="color: {LIME}">For example</span>
          <span style="font-size: 18px; line-height: 1.45">Thandi and eleven neighbours each pay R 500 a month. Each month one of them takes home R 6 000.</span>
          <span class="chip" style="border: 1px dashed {ON_EVG}; color: {ON_EVG}">Sample</span>
          <button tabindex="[[ backTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{icon('flip', 18, EVG)}Flip back</button>
        </section>
      </div>
    </div>
    <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 14px 14px 14px 18px; display: flex; align-items: center; gap: 14px">
      <span aria-hidden="true" style="position: relative; width: 44px; height: 40px; flex-shrink: 0"><span style="position: absolute; left: 8px; top: 0; width: 30px; height: 38px; border-radius: {R_S}px; background: {LIME}; opacity: .45; transform: rotate(10deg)"></span><span style="position: absolute; left: 2px; top: 2px; width: 30px; height: 38px; border-radius: {R_S}px; background: {LIME}"></span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">3 words to practise</span><span style="font-size: 13px; color: {ON_EVG}">About two minutes</span></span>
      <button onClick="[[ startPractice ]]" style="height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600">Start</button>
    </section>
    <span style="font-size: 17px; font-weight: 600; margin-top: 4px">Your collections</span>
    <div role="group" aria-label="Collections" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
    {panels}
  </div>
  {tabbar6('Vault')}
  <sc-if value="[[ practising ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 20; background: rgba(11,15,14,.55)">
      <div role="dialog" aria-label="Practise three words" style="position: absolute; left: 16px; right: 16px; top: 150px; min-height: 420px; border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px; animation: storyIn .28s cubic-bezier(.2,.8,.2,1) both">
        <div style="display: flex; justify-content: flex-end"><button onClick="[[ stopPractice ]]" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div>
        {cards_overlay}
        <sc-if value="[[ pDone ]]" hint-placeholder-val="[[ false ]]">
          <div style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
            <span style="width: 64px; height: 64px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 30, EVG, 2.8)}</span>
            <span class="d" style="font-size: 34px">Three words, practised.</span>
            <span class="hand" style="font-size: 26px; color: {LIME}; {HF}">See you tomorrow.</span>
          </div>
        </sc-if>
        <div style="flex-grow: 1"></div>
        <sc-if value="[[ askReveal ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ reveal ]]" style="height: 52px; width: 100%; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600">Show the meaning</button></sc-if>
        <sc-if value="[[ askKnow ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; gap: 10px"><button onClick="[[ nextCard ]]" style="flex: 1 1 0; height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {ON_EVG}; font-size: 16px; font-weight: 600">Not yet</button><button onClick="[[ nextCard ]]" style="flex: 1 1 0; height: 52px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600">I knew it</button></div></sc-if>
        <sc-if value="[[ pDone ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ stopPractice ]]" style="height: 52px; width: 100%; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600">Done</button></sc-if>
      </div>
    </div>
  </sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const col = st.col || 0, flipped = !!st.flipped;
    const p = st.p == null ? -1 : st.p, revealed = !!st.revealed;
    const v = {
      flipTf: flipped ? 'rotateY(180deg)' : 'rotateY(0deg)', flipped, notFlipped: !flipped,
      frontTab: flipped ? -1 : 0, backTab: flipped ? 0 : -1, doFlip: () => this.setState({ flipped: !flipped }),
      practising: p !== -1, startPractice: () => this.setState({ p: 0, revealed: false }), stopPractice: () => this.setState({ p: -1 }),
      revealed, pDone: p === 3, askReveal: p >= 0 && p < 3 && !revealed, askKnow: p >= 0 && p < 3 && revealed,
      reveal: () => this.setState({ revealed: true }), nextCard: () => this.setState({ p: p + 1, revealed: false })
    };
    for (let k = 0; k < 3; k++) v['p' + k] = p === k;
    for (let i = 0; i < 4; i++) {
      v['col' + i] = () => this.setState({ col: i }); v['colOn' + i] = col === i;
      v['colBg' + i] = col === i ? '%(mist)s' : '#FFFFFF'; v['colBw' + i] = col === i ? 2 : 0;
    }
    return v;
  }
}''' % dict(mist=POOL)
    return phone('Vault', body, logic, h=1130)


# ---------------------------------------------------------------- Me

DIMS = [('Everyday money', 'Everyday', 71, 'Financial Health, 40% of the score', 'Bills get paid and most spending is planned.'),
        ('Ready for surprises', 'Surprises', 48, 'Risk and Resilience, 25% of the score', 'A surprise cost would be hard to cover right now.'),
        ('Knowing your options', 'Options', 60, 'Capital Positioning, 20% of the score', "You know some ways to save and borrow, and you're exploring more."),
        ('Clear goals', 'Goals', 69, 'Goal Clarity, 15% of the score', 'Your goals are clear. A date and an amount would sharpen them.')]


def me():
    bars = ''.join(f'''<button onClick="[[ dim{i} ]]" aria-pressed="[[ dimOn{i} ]]" aria-label="{n}, {v}" style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 8px; height: 190px">
          <span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; color: [[ dimTx{i} ]]">{v}</span>
          <span aria-hidden="true" style="width: 100%; max-width: 58px; height: {round(v * 1.3)}px; border-radius: {R_S}px {R_S}px 2px 2px; background: [[ dimFill{i} ]]; transform-origin: bottom; animation: grow .6s cubic-bezier(.2,.8,.2,1) {0.1 + i * 0.08:.2f}s both; transition: background-color .18s"></span>
          <span style="font-size: 13px; font-weight: [[ dimW{i} ]]; color: {INK}">{short}</span>
        </button>''' for i, (n, short, v, _w, _t) in enumerate(DIMS))
    st_pts = [(40, 62, 30, 11), (126, 46, 32, 12), (212, 30, 32, 12), (292, 14, 24, 9)]
    dash = ' stroke-dasharray="5 5"'
    stones_svg = ''.join(
        f'<ellipse cx="{x}" cy="{y + 6}" rx="{rx}" ry="{ry}" fill="{"#BFD9D2" if i < 2 else "none"}"></ellipse>'
        f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[EVG, LIME, "none", "none"][i]}" stroke="{EVG}" stroke-width="2.5"{dash if i > 1 else ""}></ellipse>'
        for i, (x, y, rx, ry) in enumerate(st_pts))
    spark_pts = [(40, 55, 'Jul'), (140, 59, 'Aug'), (240, 63, 'Sep')]
    ys = {v: 50 - (v - 53) * 3.2 for _x, v, _m in spark_pts}
    spark = (f'<svg width="318" height="64" viewBox="0 0 318 64" aria-hidden="true" style="display: block; overflow: visible">'
             f'<path d="M40 {ys[55]:.0f}L140 {ys[59]:.0f}L240 {ys[63]:.0f}" fill="none" stroke="{EVG}" stroke-width="2.5"></path>'
             f'<path d="M240 {ys[63]:.0f}L300 {ys[63] - 8:.0f}" fill="none" stroke="{EVG}" stroke-width="2" stroke-dasharray="4 5"></path>'
             + ''.join(f'<circle cx="{x}" cy="{ys[v]:.0f}" r="5" fill="{EVG if v == 63 else "#FFFFFF"}" stroke="{EVG}" stroke-width="2.5"></circle>' for x, v, _m in spark_pts)
             + f'<circle cx="300" cy="{ys[63] - 8:.0f}" r="5" fill="#FFFFFF" stroke="{EVG}" stroke-width="2" stroke-dasharray="3 3"></circle></svg>')
    spark_lbl = ''.join(f'<span style="position: absolute; left: {x - 30}px; top: {ys[v] - 30:.0f}px; width: 60px; text-align: center; font-size: 15px; font-weight: 600">{v}</span><span style="position: absolute; left: {x - 30}px; top: 70px; width: 60px; text-align: center; font-size: 12px; color: {MUTED}">{m}</span>' for x, v, m in spark_pts)
    spark_lbl += f'<span style="position: absolute; left: 270px; top: 70px; width: 60px; text-align: center; font-size: 12px; color: {MUTED}">13 Oct</span>'
    body = f'''  <div class="scr" style="gap: 14px">
    <header style="display: flex; align-items: center; gap: 12px">
      <img class="face" src="{IMG['naledi']}" alt="" style="width: 44px; height: 44px">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">Naledi</span><span style="font-size: 13px; color: {MUTED}">Johannesburg</span></span>
      <a href="R7-Settings.dc.html" aria-label="Settings" style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('gear', 20, INK)}</a>
    </header>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 20px 16px 18px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px">
        <div style="display: flex; flex-direction: column; gap: 6px"><span class="lbl">Your DIVA profile</span><span class="d" style="font-size: 60px">Stage 2</span><span style="font-size: 17px; font-weight: 600">of 4 stages</span></div>
        <div role="img" aria-label="Readiness 63 of 100" style="position: relative; width: 84px; height: 84px; flex-shrink: 0">{arc(84, 63, '#B7D5CE', EVG, sw=8)}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 4px"><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.03em">63</span><span style="font-size: 12px">readiness</span></span></div>
      </div>
      <div role="img" aria-label="Stepping stones: stage 1 behind you, you are on stage 2, stages 3 and 4 ahead" style="position: relative; height: 92px">
        <svg width="318" height="80" viewBox="0 0 318 80" aria-hidden="true" style="position: absolute; left: 0; top: 12px; overflow: visible">{stones_svg}</svg>
        <img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 110px; top: 6px; width: 32px; height: 32px; box-shadow: 0 0 0 3px {LIME}; animation: stepIn .6s cubic-bezier(.2,.8,.2,1) .3s both">
        <span style="position: absolute; left: 150px; top: 12px; font-size: 13px; font-weight: 600">You are here</span>
      </div>
      <p style="font-size: 16px; line-height: 1.4; color: {INK}">Everyday money is your strength. Next: a cushion for surprises.</p>
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 12px; color: {SEC}">Learning readiness, not a credit score.</span><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">Sample</span></span>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Your shape</span><span style="font-size: 13px; color: {MUTED}">Tap a bar</span></span>
      <div role="group" aria-label="Your four dimensions" style="display: flex; gap: 12px; align-items: flex-end; padding: 0 6px">{bars}</div>
      <div style="border-top: 1px solid #EEF2EF; padding-top: 12px; display: flex; flex-direction: column; gap: 4px; min-height: 64px">
        <span style="font-size: 16px; line-height: 1.4">[[ dimText ]]</span>
        <span style="font-size: 12px; color: {MUTED}">[[ dimMeta ]]</span>
      </div>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 16px; display: flex; align-items: center; gap: 12px">
      <span aria-hidden="true" style="color: {EVG}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path></svg></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Evidence: early</span><span style="font-size: 13px; color: {MUTED}">Check-ins add more. Kept apart from the score.</span></span>
      <span role="img" aria-label="1 of 3" style="display: flex; gap: 3px"><span style="width: 16px; height: 6px; border-radius: 2px; background: {EVG}"></span><span style="width: 16px; height: 6px; border-radius: 2px; background: #DCE4DF"></span><span style="width: 16px; height: 6px; border-radius: 2px; background: #DCE4DF"></span></span>
    </section>
    <a href="R7-Progress.dc.html" style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px 16px 12px; display: flex; flex-direction: column; gap: 8px">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Your versions</span><span style="display: flex; align-items: center; gap: 2px; font-size: 13px; color: {MUTED}">See progress{icon('chev', 16, MUTED)}</span></span>
      <div role="img" aria-label="Readiness 55 in July, 59 in August, 63 in September; next check-in 13 October" style="position: relative; height: 92px; margin-top: 22px">{spark}{spark_lbl}</div>
    </a>
    <button onClick="[[ toggleMean ]]" aria-expanded="[[ mean ]]" style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 16px; min-height: 56px; display: flex; align-items: center; justify-content: space-between; font-size: 15px; font-weight: 600">What this means, in full<span style="display: flex; transform: rotate([[ meanRot ]]deg); transition: transform .28s">{icon('chev', 18, MUTED)}</span></button>
    <sc-if value="[[ mean ]]" hint-placeholder-val="[[ false ]]">
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px; margin-top: -8px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <p style="font-size: 16px; line-height: 1.5">[[ meanText ]]</p>
        <span style="display: flex; align-items: center; gap: 8px"><button onClick="[[ toggleSimple ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 14px; font-weight: 600">[[ simpleLabel ]]</button><sc-if value="[[ simple ]]" hint-placeholder-val="[[ false ]]"><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span></sc-if></span>
      </section>
    </sc-if>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">
      <div style="min-height: 56px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid #EEF2EF"><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Download my report</span>{icon('chev', 18, MUTED)}</div>
      <div style="min-height: 56px; display: flex; align-items: center; gap: 12px">{icon('lock', 18, EVG)}<span style="flex-grow: 1; font-size: 15px; font-weight: 600">Your data stays in South Africa</span>{icon('chev', 18, MUTED)}</div>
    </section>
  </div>
  {tabbar6('Me')}'''
    dims_js = [[n, t, meta] for (n, _s, _v, meta, t) in DIMS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const sel = st.sel == null ? 1 : st.sel;
    const mean = !!st.mean, simple = !!st.simple;
    const dims = %(dims)s;
    const v = {
      dimText: dims[sel][1], dimMeta: dims[sel][0] + '. ' + dims[sel][2] + '.',
      mean, toggleMean: () => this.setState({ mean: !mean }), meanRot: mean ? 90 : 0,
      simple, toggleSimple: () => this.setState({ simple: !simple }),
      simpleLabel: simple ? 'Show the original' : 'Explain it more simply',
      meanText: simple ? 'You handle day-to-day money well. What is missing is a cushion for surprises. Building one, a little at a time, is the next thing to learn.'
        : 'Your everyday money habits are a real strength. The most room to grow is being ready for surprises: right now, an unexpected cost would likely knock your plans off course.'
    };
    for (let i = 0; i < 4; i++) {
      v['dim' + i] = () => this.setState({ sel: i }); v['dimOn' + i] = sel === i;
      v['dimFill' + i] = sel === i ? '%(evg)s' : '#BFD9D2'; v['dimTx' + i] = sel === i ? '%(evg)s' : '%(mut)s';
      v['dimW' + i] = sel === i ? 600 : 400;
    }
    return v;
  }
}''' % dict(dims=dims_js, evg=EVG, mut=MUTED)
    return phone('Me, your DIVA profile', body, logic, h=1330)


# ---------------------------------------------------------------- Community

def community():
    def cluster(keys, n):
        faces = ''.join(f'<img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: {[34, 8, 58][j]}px; top: {[6, 34, 36][j]}px; width: {[40, 34, 34][j]}px; height: {[40, 34, 34][j]}px; box-shadow: 0 0 0 2px #FFFFFF">' for j, k in enumerate(keys))
        return (f'<span aria-hidden="true" style="position: relative; width: 104px; height: 76px; display: block">'
                f'<span style="position: absolute; left: 2px; top: -6px; width: 88px; height: 88px; border-radius: 999px; border: 1.5px solid {BLUSH}"></span>'
                f'<span style="position: absolute; left: 14px; top: 6px; width: 64px; height: 64px; border-radius: 999px; border: 1.5px solid {BLUSH}"></span>{faces}</span>')
    circles = [(('thandi', 'grace', 'amara'), 'Safety net', '8 women', '2 new', 'R4-M5-Seen.dc.html'),
               (('wanjiru', 'zodwa', 'lindiwe'), 'Side hustles', '24 women', '', None),
               (('grace', 'thandi', 'lindiwe'), 'Stokvel treasurers', '12 women', '', None)]
    ccards = ''
    for keys, name, count, new, href in circles:
        tag = 'a href="' + href + '"' if href else 'div'
        end = 'a' if href else 'div'
        badge = f'<span class="chip" style="position: absolute; right: 10px; top: 10px; height: 24px; padding: 0 8px; background: {BLUSH}; color: {BLUSH_INK}">{new}</span>' if new else ''
        ccards += f'<{tag} style="position: relative; flex-shrink: 0; width: 152px; border-radius: {R_L}px; background: #FFFFFF; padding: 16px 14px 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">{badge}{cluster(keys, 3)}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{name}</span><span style="font-size: 13px; color: {MUTED}">{count}</span></span></{end}>'
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: center; justify-content: space-between"><h1 class="d" style="font-size: 44px">Community</h1>
      <a href="R7-Buddy.dc.html" aria-label="Your buddy, Wanjiru" style="position: relative; width: 48px; height: 48px; flex-shrink: 0"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid #F29BB5"></span><img class="face" src="{IMG['wanjiru']}" alt="" style="position: absolute; left: 5px; top: 5px; width: 38px; height: 38px"></a></header>
    <section style="border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 18px; display: flex; flex-direction: column; gap: 14px">
      <div style="display: flex; justify-content: space-between; align-items: center"><span class="lbl" style="color: {BLUSH_2}">This week's question</span>{icon('ripple', 22, BLUSH_INK)}</div>
      <span class="d" style="font-size: 32px">What did you say no to this week?</span>
      <div style="display: flex; gap: 10px; align-items: flex-start"><img class="face" src="{IMG['thandi']}" alt="" style="width: 32px; height: 32px"><span style="padding: 10px 14px; border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: rgba(255,255,255,.75); font-size: 15px; line-height: 1.4">A second pair of work shoes. The first pair is fine.</span></div>
      <sc-if value="[[ posted ]]" hint-placeholder-val="[[ false ]]"><div style="position: relative; align-self: flex-end; max-width: 270px; padding: 10px 14px; border-radius: {R_L}px {R_S}px {R_L}px {R_L}px; background: {BLUSH_INK}; color: {BLUSH}; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span><span class="hand" style="font-size: 22px; {HF}">[[ answer ]]</span></div></sc-if>
      <sc-if value="[[ notPosted ]]" hint-placeholder-val="[[ true ]]">
        <div style="display: flex; gap: 8px">
          <label for="c7-ans" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your answer</label>
          <input id="c7-ans" value="[[ answer ]]" onInput="[[ type ]]" placeholder="Share yours" style="flex-grow: 1; min-width: 0; height: 44px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 15px; color: {INK}">
          <button onClick="[[ post ]]" aria-label="Share your answer" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</button>
        </div>
      </sc-if>
      <span style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="display: flex">{''.join(f'<img class="face" src="{IMG[k]}" alt="" style="width: 24px; height: 24px; margin-left: {0 if j == 0 else -7}px; box-shadow: 0 0 0 2px {BLUSH}">' for j, k in enumerate(('wanjiru', 'grace', 'amara')))}</span><span style="font-size: 13px; color: {BLUSH_2}">[[ countText ]]</span></span>
    </section>
    <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Your circles</span><span style="font-size: 13px; color: {MUTED}">First names only</span></span>
    <div style="display: flex; gap: 10px; overflow: hidden; margin-right: -20px">{ccards}</div>
    <article style="border-radius: {R_L}px; background: #FFFFFF; overflow: hidden; display: flex; flex-direction: column">
      <img src="{IMG['wanjiru_stall']}" alt="Wanjiru's homeware stall" style="width: 100%; height: 190px; object-fit: cover; object-position: 60% 38%; display: block">
      <div style="padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 12px">
        <span style="font-size: 17px; line-height: 1.35; font-weight: 500">Seven evenings of notes. Now I know what the stall really earns.</span>
        <div style="display: flex; align-items: center; gap: 10px">
          <img class="face" src="{IMG['wanjiru']}" alt="" style="width: 32px; height: 32px"><span style="flex-grow: 1; font-size: 14px; font-weight: 600">Wanjiru <span style="font-weight: 400; color: {MUTED}">Nairobi</span></span>
          <button onClick="[[ doCheer ]]" aria-pressed="[[ cheered ]]" style="position: relative; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ cheerBg ]]; color: [[ cheerFg ]]; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s"><sc-if value="[[ cheered ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span></sc-if>{icon('ripple', 18)}[[ cheerLabel ]]<span style="font-weight: 500; opacity: .75">[[ cheerCount ]]</span></button>
        </div>
      </div>
    </article>
    <section style="border-radius: {R_L}px; background: {NIGHT}; color: {MOON}; padding: 16px; display: flex; align-items: center; gap: 14px">
      <span aria-hidden="true" style="width: 52px; height: 56px; flex-shrink: 0; border-radius: {R_M}px; background: {RAISED}; display: flex; flex-direction: column; align-items: center; justify-content: center"><span style="font-size: 12px; color: {NMUTED}">Thu</span><span style="font-size: 22px; font-weight: 600">2</span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Ask a stokvel treasurer</span><span style="font-size: 13px; color: {NMUTED}">Live at 19:00, with Grace</span></span>
      <button onClick="[[ remind ]]" aria-pressed="[[ reminded ]]" style="flex-shrink: 0; white-space: nowrap; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ remBg ]]; color: [[ remFg ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">[[ remLabel ]]</button>
    </section>
  </div>
  {tabbar6('Community')}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const cheered = !!st.cheered, posted = !!st.posted, reminded = !!st.reminded;
    const answer = st.answer == null ? 'Takeaway on Friday. Cooked instead, and it was nicer.' : st.answer;
    return {
      posted, notPosted: !posted, answer,
      type: (e) => this.setState({ answer: e.target.value }),
      post: () => { if (answer.trim()) this.setState({ posted: true }); },
      countText: posted ? 'You and 38 women answered' : '38 women answered',
      cheered, cheerLabel: cheered ? 'Cheered' : 'Cheer', cheerCount: cheered ? 25 : 24,
      cheerBg: cheered ? '%(bi)s' : '%(b)s', cheerFg: cheered ? '%(b)s' : '%(bi)s',
      doCheer: () => this.setState({ cheered: !cheered }),
      reminded, remind: () => this.setState({ reminded: !reminded }),
      remLabel: reminded ? 'Reminder set' : 'Remind me',
      remBg: reminded ? '%(lime)s' : '%(raised)s', remFg: reminded ? '%(evg)s' : '%(moon)s'
    };
  }
}''' % dict(bi=BLUSH_INK, b=BLUSH, lime=LIME, raised=RAISED, evg=EVG, moon=MOON)
    return phone('Community', body, logic, h=1190)
