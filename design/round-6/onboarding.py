"""R6-Welcome and R6-Starter: Oasis v2's welcome and starter check, at Volume 1 (Clean).
Each welcome slide takes the colour and shape of the area it introduces."""
from lib6 import *

SLIDES = [
    dict(bg=EVG, title='Know where you stand. Grow from there.',
         sub='Free money learning and insight for women building their financial lives, at home and abroad.'),
    dict(bg=NIGHT, title='Learn money in three minutes a day.',
         sub='Short lessons told through real stories. No jargon, no judgement.'),
    dict(bg=BLUSH, title='Grow with women who get it.',
         sub='Circles of women on the same step. They see your first name, never your numbers.'),
]


def art_stones():
    # Stepping stones rising out of water towards a lime sun: "know where you stand".
    st = [(70, 330, 44, 15), (150, 280, 48, 16), (232, 228, 50, 17), (300, 170, 44, 15)]
    stones_svg = ''.join(
        f'<g style="animation: stepIn .6s cubic-bezier(.2,.8,.2,1) {0.15 + i * 0.14:.2f}s both">'
        f'<ellipse cx="{x}" cy="{y + 7}" rx="{rx}" ry="{ry}" fill="{EVG_D}"></ellipse>'
        f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{LIME}"></ellipse></g>' for i, (x, y, rx, ry) in enumerate(st))
    return f'''<svg width="390" height="420" viewBox="0 0 390 420" aria-hidden="true" style="display: block">
      <circle cx="300" cy="80" r="34" fill="none" stroke="{LIME}" stroke-width="3"></circle>
      <circle cx="300" cy="80" r="18" fill="{EVG_D}"></circle>
      <g fill="none" stroke="{LIME}" stroke-opacity=".28" stroke-width="2"><ellipse cx="150" cy="286" rx="92" ry="30"></ellipse><ellipse cx="232" cy="234" rx="110" ry="36"></ellipse></g>
      {stones_svg}
      <g style="transform-origin: 300px 170px"><ellipse cx="300" cy="170" rx="44" ry="15" fill="none" stroke="{LIME}" stroke-width="2" style="transform-box: fill-box; transform-origin: center; animation: spread 2.4s ease-out 1s infinite"></ellipse></g>
      <g style="animation: float 3.2s ease-in-out 1.2s infinite"><path d="M300 166c0-18 0-26 0-34" stroke="{LIME}" stroke-width="3" stroke-linecap="round"></path><path d="M300 142c-12-2-18-10-18-18 10 0 17 6 18 18zM300 136c10-3 16-10 16-18-9 0-15 7-16 18z" fill="{LIME}"></path></g>
    </svg>'''


def art_moons():
    phases = ['new', 'cres', 'half', 'half', 'full']
    xs = [40, 115, 195, 275, 350]
    ys = [300, 230, 196, 230, 300]
    out = []
    for i, (p, x, y) in enumerate(zip(phases, xs, ys)):
        size = 58 if i != 2 else 84
        out.append(f'<div style="position: absolute; left: {x - size / 2:.0f}px; top: {y - size / 2:.0f}px; animation: rise .6s cubic-bezier(.2,.8,.2,1) {0.1 + i * 0.12:.2f}s both">{moon(size, p, now=(i == 2), craters=(i == 4))}</div>')
    return f'''<div aria-hidden="true" style="position: relative; width: 390px; height: 420px">
      <svg width="390" height="420" viewBox="0 0 390 420" style="position: absolute; inset: 0"><path d="M40 300Q195 120 350 300" fill="none" stroke="{NLINE}" stroke-width="2" stroke-dasharray="4 7"></path></svg>
      {''.join(out)}
      <span style="position: absolute; left: 60px; top: 90px; width: 4px; height: 4px; border-radius: 9px; background: {MOON}; opacity: .6"></span>
      <span style="position: absolute; left: 320px; top: 120px; width: 3px; height: 3px; border-radius: 9px; background: {MOON}; opacity: .5"></span>
      <span style="position: absolute; left: 250px; top: 70px; width: 5px; height: 5px; border-radius: 9px; background: {LIME}; opacity: .8"></span>
    </div>'''


def art_ripple():
    faces = [('thandi', 90, 250, 84), ('wanjiru', 196, 190, 112), ('amara', 300, 262, 78), ('grace', 150, 330, 64), ('lindiwe', 256, 344, 60)]
    rings = ''.join(f'<span style="position: absolute; left: {196 - r}px; top: {220 - r}px; width: {2 * r}px; height: {2 * r}px; box-sizing: border-box; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .22; animation: spread 3.2s ease-out {d}s infinite"></span>'
                    for r, d in ((120, 0), (120, 1.6)))
    imgs = ''.join(f'<img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: {x - s / 2:.0f}px; top: {y - s / 2:.0f}px; width: {s}px; height: {s}px; box-shadow: 0 0 0 4px {BLUSH}; animation: pop .6s cubic-bezier(.34,1.56,.64,1) {0.1 + i * 0.1:.2f}s both">'
                   for i, (k, x, y, s) in enumerate(faces))
    return f'<div aria-hidden="true" style="position: relative; width: 390px; height: 420px">{rings}{imgs}</div>'


def welcome():
    arts = [art_stones(), art_moons(), art_ripple()]
    slides = ''
    for i, (s, art) in enumerate(zip(SLIDES, arts)):
        slides += f'''<sc-if value="[[ s{i} ]]" hint-placeholder-val="[[ {'true' if i == 0 else 'false'} ]]">
      <div style="position: absolute; left: 0; right: 0; top: 60px">{art}</div>
    </sc-if>'''
    texts = ''
    for i, s in enumerate(SLIDES):
        texts += f'''<sc-if value="[[ s{i} ]]" hint-placeholder-val="[[ {'true' if i == 0 else 'false'} ]]">
        <div style="display: flex; flex-direction: column; gap: 12px; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
          <h1 class="d" style="font-size: 40px">{s['title']}</h1>
          <p style="font-size: 16px; line-height: 1.5; color: {SEC}">{s['sub']}</p>
        </div>
      </sc-if>'''
    dots = ''.join(f'<button onClick="[[ go{i} ]]" aria-label="Show slide {i + 1} of 3" aria-current="[[ cur{i} ]]" style="height: 44px; min-width: 44px; display: flex; align-items: center; justify-content: center"><span style="display: block; height: 6px; width: [[ w{i} ]]px; border-radius: 99px; background: [[ c{i} ]]; transition: width .28s, background-color .28s"></span></button>' for i in range(3))
    body = f'''  <div style="position: absolute; left: 0; right: 0; top: 0; height: 500px; background: [[ topBg ]]; transition: background-color .6s cubic-bezier(.2,.8,.2,1)">
    <div style="position: absolute; left: 20px; right: 20px; top: 50px; display: flex; align-items: center; justify-content: space-between; z-index: 2">
      <span class="d" style="font-size: 32px; color: [[ markCol ]]; transition: color .6s">awo</span>
      <button style="height: 44px; padding: 0 14px; border-radius: 999px; background: [[ chipBg ]]; color: [[ chipFg ]]; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"></path></svg>English</button>
    </div>
    <button onClick="[[ nextSlide ]]" aria-label="Next slide" style="position: absolute; left: 0; right: 0; top: 104px; bottom: 90px"></button>
    {slides}
  </div>
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 412px; border-radius: 32px 32px 0 0; background: #FFFFFF; padding: 14px 24px 28px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px">
    <div role="group" aria-label="Slides" style="display: flex; gap: 0; margin-left: -14px">{dots}</div>
    <div style="min-height: 176px">{texts}</div>
    <div style="flex-grow: 1"></div>
    <a href="R6-Starter.dc.html" class="pill" style="height: 56px; background: {EVG}; color: #FFFFFF">Get started</a>
    <a href="R6-Home.dc.html" style="min-height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600; color: {EVG}">I already have an account</a>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const i = st.i || 0;
    const bg = ['%(evg)s', '%(night)s', '%(blush)s'];
    const v = {
      topBg: bg[i],
      markCol: i === 2 ? '%(blushInk)s' : '%(lime)s',
      chipBg: i === 2 ? 'rgba(42,15,24,.1)' : 'rgba(255,255,255,.12)',
      chipFg: i === 2 ? '%(blushInk)s' : '#FFFFFF',
      nextSlide: () => this.setState({ i: (i + 1) %% 3 })
    };
    for (let k = 0; k < 3; k++) {
      v['s' + k] = i === k;
      v['go' + k] = () => this.setState({ i: k });
      v['cur' + k] = i === k ? 'step' : 'false';
      v['w' + k] = i === k ? 22 : 6;
      v['c' + k] = i === k ? '%(evg)s' : '#C9D3CE';
    }
    return v;
  }
}''' % dict(evg=EVG, night=NIGHT, blush=BLUSH, blushInk=BLUSH_INK, lime=LIME)
    return phone('Welcome', body, logic, h=844, bg='#FFFFFF')


QS = [
    dict(n=6, icon='<path d="M3 12a9 9 0 0 1 18 0z"></path><path d="M12 12v6a2 2 0 0 0 4 0"></path>',
         q='An unexpected R 3 000 cost comes up this month. What would most likely happen?',
         opts=["I'd cover it from savings", "I'd borrow from family or friends", "I'd use credit or a loan", "I'd have to skip something important"]),
    dict(n=7, icon='<rect x="3.5" y="5" width="17" height="15" rx="3"></rect><path d="M3.5 10h17M8 3v4M16 3v4"></path>',
         q='How does your income usually arrive?',
         opts=['The same amount on the same day', 'It changes from month to month', 'A salary plus something on the side', 'Someone else manages it']),
    dict(n=8, icon='<circle cx="8" cy="9" r="3"></circle><circle cx="16" cy="9" r="3"></circle><path d="M2.5 19c.7-3 3-4.5 5.5-4.5s4.8 1.5 5.5 4.5M11.5 16c.9-1 2.4-1.5 4.5-1.5 2.5 0 4.8 1.5 5.5 4.5"></path>',
         q='Do you belong to a savings group, like a stokvel or a chama?',
         opts=['Yes, one', 'Yes, more than one', "Not now, but I have before", 'Never'])]


def starter():
    qblocks = ''
    for k, q in enumerate(QS):
        opts = ''.join(f'''<button onClick="[[ pick{k}_{j} ]]" aria-pressed="[[ sel{k}_{j} ]]" style="min-height: 58px; padding: 10px 16px; border-radius: 18px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ bw{k}_{j} ]]px {EVG}; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; font-weight: 500; transition: box-shadow .18s">
            <span style="flex-grow: 1">{o}</span>
            <span aria-hidden="true" style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 99px; border: 2px solid [[ rc{k}_{j} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 10px; height: 10px; border-radius: 99px; background: [[ rf{k}_{j} ]]"></span></span></button>''' for j, o in enumerate(q['opts']))
        qblocks += f'''<sc-if value="[[ q{k} ]]" hint-placeholder-val="[[ {'true' if k == 0 else 'false'} ]]">
      <div style="display: flex; flex-direction: column; gap: 14px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
        <span aria-hidden="true" style="width: 52px; height: 52px; border-radius: 16px; background: {POOL}; color: {EVG}; display: flex; align-items: center; justify-content: center"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{q['icon']}</svg></span>
        <h1 class="d" style="font-size: 34px">{q['q']}</h1>
        <p style="font-size: 14px; color: {MUTED}">There's no wrong answer. Only you see this.</p>
        <div role="group" aria-label="Answers" style="display: flex; flex-direction: column; gap: 8px">{opts}</div>
      </div>
    </sc-if>'''
    segs = ''.join(f'<span style="flex-grow: 1; height: 4px; border-radius: 99px; background: [[ seg{i} ]]; transition: background-color .28s"></span>' for i in range(8))
    st4 = [(40, 150, 30, 11), (130, 116, 34, 12), (220, 82, 36, 13), (304, 46, 32, 11)]
    work_stones = ''.join(
        f'<ellipse cx="{x}" cy="{y + 6}" rx="{rx}" ry="{ry}" fill="#BFD9D2"></ellipse><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{EVG}" style="animation: pulse 1.6s ease-in-out {i * 0.3:.1f}s infinite"></ellipse>'
        for i, (x, y, rx, ry) in enumerate(st4))
    ready_stones = stones(300, 120, [(40, 96, 30, 11), (130, 70, 34, 12), (220, 44, 36, 13), (290, 18, 22, 8)],
                          [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='5 5')
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 28px; gap: 16px">
    <sc-if value="[[ asking ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; align-items: center; gap: 12px">
        <a href="R6-Welcome.dc.html" aria-label="Close" style="width: 44px; height: 44px; flex-shrink: 0; box-sizing: border-box; border-radius: 999px; border: 1px solid #C9D3CE; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></a>
        <div aria-hidden="true" style="flex-grow: 1; display: flex; gap: 4px">{segs}</div>
        <span style="font-size: 13px; font-weight: 600; color: {MUTED}; width: 40px; text-align: right">[[ countText ]]</span>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center"><span class="cap" style="color: {MUTED}">[[ leftText ]]</span>{sample_chip(MUTED, 'Sample question')}</div>
      {qblocks}
      <div style="flex-grow: 1"></div>
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
        <button onClick="[[ skip ]]" style="height: 44px; padding: 0 4px; font-size: 15px; font-weight: 600; color: {EVG}">Prefer not to say</button>
        <button onClick="[[ next ]]" disabled="[[ noPick ]]" style="height: 52px; padding: 0 28px; border-radius: 999px; background: [[ ctaBg ]]; color: [[ ctaFg ]]; font-size: 16px; font-weight: 600; transition: background-color .18s">[[ ctaLabel ]]</button>
      </div>
    </sc-if>
    <sc-if value="[[ working ]]" hint-placeholder-val="[[ false ]]">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center; gap: 22px; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
        <svg width="350" height="180" viewBox="0 0 350 180" aria-hidden="true" style="display: block">{work_stones}</svg>
        <h1 class="d" style="font-size: 44px">Working out your profile</h1>
        <p style="font-size: 16px; line-height: 1.5; color: {SEC}">On AWO's servers in South Africa. The same answers always give the same result, and every version is kept.</p>
      </div>
    </sc-if>
    <sc-if value="[[ ready ]]" hint-placeholder-val="[[ false ]]">
      <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 18px; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
        <div style="flex-grow: 1; border-radius: 32px; background: {POOL}; color: {EVG}; padding: 24px; display: flex; flex-direction: column; justify-content: flex-end; gap: 14px">
          <span role="img" aria-label="Stage 2 of 4 as stepping stones" style="animation: stepIn .6s cubic-bezier(.2,.8,.2,1) .2s both">{ready_stones}</span>
          <span class="lbl">Your first profile</span>
          <span class="d" style="font-size: 56px">Stage 2 of 4</span>
          <span style="font-size: 16px; line-height: 1.45; color: {INK}">Your everyday money habits are a real strength. The most room to grow is being ready for a surprise.</span>
          <span style="display: flex; gap: 6px">{sample_chip(EVG)}<span class="chip" style="background: rgba(255,255,255,.6); color: {SEC}">Evidence: early</span></span>
        </div>
        <a href="R6-Me.dc.html" class="pill" style="height: 56px; background: {EVG}; color: #FFFFFF">See what it means</a>
        <button onClick="[[ restart ]]" style="height: 44px; font-size: 14px; font-weight: 500; color: {MUTED}">Start over</button>
      </div>
    </sc-if>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const q = st.q || 0;
    const phase = st.phase || 'asking';
    const picks = st.picks || [-1, -1, -1];
    const N = 3, first = %(first)d;
    const cur = picks[q];
    const advance = () => {
      if (q < N - 1) { this.setState({ q: q + 1 }); return; }
      this.setState({ phase: 'working' });
      setTimeout(() => this.setState({ phase: 'ready' }), 2400);
    };
    const v = {
      asking: phase === 'asking', working: phase === 'working', ready: phase === 'ready',
      countText: (first + q) + ' of 8',
      leftText: ['About a minute left', 'Nearly there', 'Last question'][q],
      noPick: cur === -1,
      ctaBg: cur === -1 ? '#DCE4DF' : '%(evg)s', ctaFg: cur === -1 ? '#56625C' : '#FFFFFF',
      ctaLabel: q === N - 1 ? 'Finish' : 'Continue',
      next: () => { if (cur !== -1) advance(); },
      skip: advance,
      restart: () => this.setState({ q: 0, phase: 'asking', picks: [-1, -1, -1] })
    };
    for (let i = 0; i < 8; i++) v['seg' + i] = i < first + q ? '%(evg)s' : '#D5DFDA';
    for (let k = 0; k < N; k++) {
      v['q' + k] = q === k;
      for (let j = 0; j < 4; j++) {
        const on = picks[k] === j;
        v['pick' + k + '_' + j] = () => { const p = picks.slice(); p[k] = j; this.setState({ picks: p }); };
        v['sel' + k + '_' + j] = on;
        v['bw' + k + '_' + j] = on ? 2 : 0;
        v['rc' + k + '_' + j] = on ? '%(evg)s' : '#A9B6AF';
        v['rf' + k + '_' + j] = on ? '%(evg)s' : 'transparent';
      }
    }
    return v;
  }
}''' % dict(first=QS[0]['n'], evg=EVG)
    return phone('Starter check', body, logic, h=844)


if __name__ == '__main__':
    out = sys.argv[1]
    write(os.path.join(out, 'R6-Welcome.dc.html'), welcome())
    write(os.path.join(out, 'R6-Starter.dc.html'), starter())
