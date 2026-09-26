"""Round 8, batch 4: real human stories (D-038), in Learn (night). Writes R8-Story (a Rise story, read or heard),
R8-Podcast (the AWO Podcast player: chapters, a synced transcript, key lessons, low data and offline) and
R8-Mistake ("My worst money mistake", told by a member and edited with her).

Guests and members are samples (Q-39, Q-42). The hand appears only in someone's own words, or AWO's short note at a milestone."""
import json

from lib8 import *  # noqa: F401,F403
from learn8 import PHONE_CSS, ola_pill, chip_dark, REVIEWED_D

STORY_CSS = """
@keyframes eq{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
.eq span{transform-origin:50% 100%;animation:eq 1s ease-in-out infinite;animation-play-state:var(--play,paused)}
@keyframes prog{from{width:var(--from)}to{width:var(--to)}}
"""

REACTIONS = [('Cheer', 'heart'), ('Same here', 'people'), ('Taught me', 'moon')]


def reactions(k, dark=False, note=None):
    """Cheer, Same here, Taught me. Only the author sees how many; everyone else sees what they gave."""
    idle_bg = RAISED if dark else MIST
    btns = ''.join(f'<button onClick="[[ rx{k}_{j} ]]" aria-pressed="[[ rxOn{k}_{j} ]]" style="position: relative; height: 44px; padding: 0 10px; border-radius: {R_M}px; background: [[ rxBg{k}_{j} ]]; color: [[ rxFg{k}_{j} ]]; display: flex; align-items: center; gap: 5px; font-size: 13px; font-weight: 600; white-space: nowrap; transition: background-color .18s, color .18s">'
                   f'<sc-if value="[[ rxOn{k}_{j} ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; color: {BLUSH_INK if not dark else BLUSH}"></span></sc-if>{(moon(16, "half", lit="currentColor", dark=idle_bg) if g == "moon" else ic8(g, 16))}{n}</button>'
                   for j, (n, g) in enumerate(REACTIONS))
    extra = f'<span style="font-size: 12px; color: {NMUTED if dark else MUTED}">{note}</span>' if note else ''
    return f'<div style="display: flex; flex-direction: column; gap: 6px"><div role="group" aria-label="React" style="display: flex; gap: 4px; flex-wrap: wrap">{btns}</div>{extra}</div>'


def reactions_js(keys, dark=False):
    idle_bg, idle_fg = (RAISED, MOON) if dark else (MIST, INK)
    on_bg, on_fg = (BLUSH, BLUSH_INK)
    return '''    for (const k of %s) for (let j = 0; j < 3; j++) {
      const key = 'rx' + k + '_' + j, on = !!(st.rx || {})[key];
      v[key] = () => this.setState({ rx: Object.assign({}, st.rx || {}, { [key]: !on }) });
      v['rxOn' + k + '_' + j] = on; v['rxBg' + k + '_' + j] = on ? '%s' : '%s'; v['rxFg' + k + '_' + j] = on ? '%s' : '%s';
    }''' % (json.dumps(keys), on_bg, idle_bg, on_fg, idle_fg)


# ---------------------------------------------------------------- A Rise story

LESSONS = ['Tell your circle early. Hiding cost more than the debt.', 'Restock what sells twice, not what you love.', "Keep the stall's money apart from your own."]


def story():
    cards = ''.join(f'''<div style="border-radius: {R_L}px; background: {DEEP}; padding: 16px; display: flex; gap: 12px; align-items: flex-start">
        <span style="width: 32px; height: 32px; flex-shrink: 0; border-radius: 999px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{icon('check', 18, EVG, 2.6)}</span>
        <span style="flex-grow: 1; font-size: 17px; font-weight: 600; line-height: 1.35">{t}</span>
        <button onClick="[[ keep{i} ]]" aria-pressed="[[ kept{i} ]]" aria-label="Save this lesson" style="width: 44px; height: 44px; flex-shrink: 0; margin: -8px -8px 0 0; border-radius: {R_M}px; background: [[ keepBg{i} ]]; color: [[ keepFg{i} ]]; display: flex; align-items: center; justify-content: center">{ic8('bookmark', 20)}</button></div>''' for i, t in enumerate(LESSONS))
    p = 'font-size: 17px; line-height: 1.65; color: #DDE3E0'
    h = 'font-size: 20px; font-weight: 600; letter-spacing: -0.02em; margin-top: 6px'
    body = f'''  <div style="position: absolute; left: 0; right: 0; top: 0; height: 380px"><img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her stall today" style="width: 100%; height: 100%; object-fit: cover; object-position: 60% 30%"><span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(11,15,14,.55) 0, rgba(11,15,14,0) 25%, rgba(11,15,14,0) 55%, {NIGHT} 100%)"></span></div>
  <div class="scr" style="gap: 18px">
    <header style="display: flex; align-items: center; gap: 8px">
      <a href="R8-Learn.dc.html" aria-label="Back to Stories" style="width: 44px; height: 44px; border-radius: {R_M}px; background: rgba(11,15,14,.6); display: flex; align-items: center; justify-content: center">{ic('back', 20, '#FFFFFF', 2.2)}</a>
      <span style="flex-grow: 1"></span>
      <button onClick="[[ listen ]]" aria-pressed="[[ listening ]]" style="height: 44px; padding: 0 14px 0 10px; border-radius: {R_M}px; background: [[ lisBg ]]; color: [[ lisFg ]]; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{ic8('speaker', 18)}[[ lisLabel ]]</button>
      <button onClick="[[ save ]]" aria-pressed="[[ saved ]]" aria-label="Save for offline" style="width: 44px; height: 44px; border-radius: {R_M}px; background: [[ saveBg ]]; color: [[ saveFg ]]; display: flex; align-items: center; justify-content: center">{ic8('download', 20)}</button>
    </header>
    <div style="height: 200px"></div>
    <div style="display: flex; gap: 6px"><span class="chip" style="background: {LIME}; color: {EVG}">Rise</span><span class="chip" style="background: {BLUSH}; color: {BLUSH_INK}">Member story</span>{chip_dark('Sample')}</div>
    <h1 class="d" style="font-size: 40px">My first stall closed in four months</h1>
    <div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 40px; height: 40px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Wanjiru, Nairobi</span><span style="font-size: 13px; color: {NMUTED}">Told to AWO, edited with her. Six minutes.</span></span></div>
    <sc-if value="[[ saved ]]" hint-placeholder-val="[[ false ]]"><span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MINT}; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">{icon('check', 16, MINT, 2.6)}Saved. It reads offline, and uses no data.</span></sc-if>
    <p style="{p}">I opened my first stall in 2023 with savings from three years of cleaning jobs. I bought what I liked, not what sold. By the fourth month I owed my supplier more than the stall had taken.</p>
    <h2 style="{h}">The month I closed</h2>
    <p style="{p}">I told no one. My chama asked why I'd missed two contributions, and I made up a reason. That was the worst part: not the stall, the hiding.</p>
    <p class="hand" style="font-size: 32px; color: {LIME}; padding: 8px 0; {HF}">Then I started again.</p>
    <h2 style="{h}">What I changed</h2>
    <p style="{p}">The second time, I kept a notebook from the first day: money in, money out, every evening. I only restocked what sold twice. And the stall's money went into its own mobile-money wallet, not mine.</p>
    <h2 style="{h}">Where I am now</h2>
    <p style="{p}">Two years on, the stall pays my rent and my son's school fees. Some months are slow. The notebook tells me before I panic.</p>
    <span style="font-size: 17px; font-weight: 600; margin-top: 8px">Three things to keep</span>
    {cards}
    <span style="font-size: 17px; font-weight: 600; margin-top: 8px">Try what she did</span>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
      <a href="R7-Biz-Home.dc.html" style="min-height: 120px; box-sizing: border-box; border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600">{hub_icon(None, 18, EVG)}In the Hub</span><span style="font-size: 16px; font-weight: 600">Money in and out: the notebook</span></a>
      <a href="R8-Tool-Price.dc.html" style="min-height: 120px; box-sizing: border-box; border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600">{hub_icon(None, 18, EVG)}In the Hub</span><span style="font-size: 16px; font-weight: 600">Price it right</span></a>
    </div>
    <section style="border-top: 1px solid {NLINE}; padding-top: 16px; display: flex; flex-direction: column; gap: 12px">
      {reactions('s', dark=True, note='Only Wanjiru sees how many people reacted.')}
      <a href="R8-Mistake.dc.html" style="height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">Tell your own story</a>
      <span style="font-size: 13px; line-height: 1.5; color: {NMUTED}">A member story, published with Wanjiru's consent. She approved every edit, and can take it down.</span>
    </section>
  </div>
  {tabbar8('Learn', dark=True)}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%(rx)s
    const listening = !!st.listening, saved = !!st.saved, kept = st.kept || [false, false, false];
    v.listening = listening; v.listen = () => this.setState({ listening: !listening });
    v.lisLabel = listening ? 'Listening' : 'Listen'; v.lisBg = listening ? '%(lime)s' : 'rgba(11,15,14,.6)'; v.lisFg = listening ? '%(evg)s' : '#FFFFFF';
    v.saved = saved; v.save = () => this.setState({ saved: !saved }); v.saveBg = saved ? '%(lime)s' : 'rgba(11,15,14,.6)'; v.saveFg = saved ? '%(evg)s' : '#FFFFFF';
    for (let i = 0; i < 3; i++) { v['kept' + i] = kept[i]; v['keep' + i] = () => { const k = kept.slice(); k[i] = !k[i]; this.setState({ kept: k }); }; v['keepBg' + i] = kept[i] ? '%(lime)s' : '%(raised)s'; v['keepFg' + i] = kept[i] ? '%(evg)s' : '%(moon)s'; }
    return v;
  }
}''' % dict(rx=reactions_js(['s'], dark=True), lime=LIME, evg=EVG, raised=RAISED, moon=MOON)
    return with_css(phone('A Rise story', body, logic, h=2140, bg=NIGHT, dark=True), PHONE_CSS + HUB_CSS + STORY_CSS)


# ---------------------------------------------------------------- The AWO Podcast

CHAPTERS = [('0:00', 'The first shop', 460), ('7:40', 'The month it closed', 450), ('15:10', 'What the numbers said', 560), ('24:30', 'Opening again, smaller', 455)]
TOTAL = sum(c[2] for c in CHAPTERS)
TRANSCRIPT = [(0, 'Thandeka', 'Amara, you closed your first studio after a year. What was the first sign?'),
              (0, 'Amara', 'Orders were fine. Cash wasn\'t. I was paying for fabric before customers paid me.'),
              (1, 'Thandeka', 'How did you decide to close, and not hold on?'),
              (1, 'Amara', 'Every month open cost more than the month before. So I stopped. It was the best money decision I made.'),
              (2, 'Amara', 'I wrote down every cost for one dress. My price didn\'t even cover the thread and my time.'),
              (3, 'Amara', 'The second studio is half the size. I asked my first ten customers what they\'d pay, and they told me.')]
POD_LESSONS = ['Close fast, not slowly: every month open cost more.', 'Your first customers will tell you the price, if you ask.', "A small shop you can afford beats a big one you can't."]


def podcast():
    ticks = ''
    acc = 0
    for i, (_t, _n, d) in enumerate(CHAPTERS):
        if i:
            ticks += f'<span aria-hidden="true" style="position: absolute; top: -3px; left: {acc / TOTAL * 100:.1f}%; width: 2px; height: 14px; background: {NIGHT}"></span>'
        acc += d
    chap = ''.join(f'''<button onClick="[[ ch{i} ]]" aria-pressed="[[ chOn{i} ]]" style="width: 100%; min-height: 60px; display: flex; align-items: center; gap: 12px; text-align: left; {"border-top: 1px solid " + NLINE + ";" if i else ""}">
          <span style="width: 52px; flex-shrink: 0; font-size: 14px; font-variant-numeric: tabular-nums; color: [[ chT{i} ]]">{t}</span>
          <span style="flex-grow: 1; font-size: 16px; font-weight: [[ chW{i} ]]; color: [[ chC{i} ]]">{n}</span>
          <sc-if value="[[ chOn{i} ]]" hint-placeholder-val="[[ {"true" if i == 1 else "false"} ]]"><span class="eq" aria-hidden="true" style="display: flex; gap: 2px; align-items: flex-end; height: 16px; --play: [[ play ]]">{''.join(f'<span style="width: 3px; height: 16px; border-radius: 1px; background: {LIME}; animation-delay: {k * .15:.2f}s"></span>' for k in range(4))}</span></sc-if>
        </button>''' for i, (t, n, _d) in enumerate(CHAPTERS))
    trans = ''.join(f'''<p style="border-radius: {R_M}px; padding: 10px 12px; background: [[ trBg{i} ]]; font-size: 16px; line-height: 1.55; color: [[ trFg{i} ]]; transition: background-color .25s, color .25s"><b style="font-weight: 600">{who}:</b> {line}</p>''' for i, (_c, who, line) in enumerate(TRANSCRIPT))
    lessons = ''.join(f'''<div style="border-radius: {R_L}px; background: {DEEP}; padding: 16px; display: flex; gap: 12px; align-items: flex-start">
        <span style="flex-grow: 1; font-size: 17px; font-weight: 600; line-height: 1.35">{t}</span>
        <button onClick="[[ keep{i} ]]" aria-pressed="[[ kept{i} ]]" aria-label="Save this lesson" style="width: 44px; height: 44px; flex-shrink: 0; margin: -8px -8px 0 0; border-radius: {R_M}px; background: [[ keepBg{i} ]]; color: [[ keepFg{i} ]]; display: flex; align-items: center; justify-content: center">{ic8('bookmark', 20)}</button></div>''' for i, t in enumerate(POD_LESSONS))
    tabs = ''.join(f'<button role="tab" onClick="[[ tb{j} ]]" aria-selected="[[ tbOn{j} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ tbBg{j} ]]; color: [[ tbFg{j} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{t}</button>' for j, t in enumerate(['Chapters', 'Transcript', 'Key lessons']))
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: center; gap: 10px">
      <a href="R8-Learn.dc.html" aria-label="Back to Stories" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('back', 20, MOON, 2.2)}</a>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 13px; color: {NMUTED}">Stories</span><span style="font-size: 17px; font-weight: 600">The AWO Podcast</span></span>
      {chip_dark('Sample guest')}
    </header>
    <div style="position: relative; height: 280px; border-radius: {R_L}px; overflow: hidden">
      <img src="{IMG['amara_coat']}" alt="Amara, this episode's guest" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 20%">
      <span class="chip" style="position: absolute; left: 12px; bottom: 12px; background: {LIME}; color: {EVG}">Episode 12</span>
    </div>
    <div style="display: flex; flex-direction: column; gap: 6px">
      <h1 class="d" style="font-size: 30px">Closing a shop, and opening a better one</h1>
      <span style="font-size: 15px; line-height: 1.4; color: {NMUTED}">Amara runs a tailoring studio in Accra. She closed her first one after a year. With Thandeka.</span>
    </div>
    <div style="display: flex; flex-direction: column; gap: 8px">
      <div role="slider" aria-label="Where you are in the episode" aria-valuetext="[[ nowTxt ]] of 32:05" tabindex="0" style="position: relative; height: 8px; border-radius: 2px; background: {RAISED}">
        <span style="position: absolute; left: 0; top: 0; bottom: 0; width: [[ prog ]]%; border-radius: 2px; background: {LIME}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span>{ticks}
        <span aria-hidden="true" style="position: absolute; top: -6px; left: [[ prog ]]%; width: 20px; height: 20px; margin-left: -10px; border-radius: 6px; background: {LIME}; box-shadow: 0 0 0 3px {NIGHT}; transition: left .4s cubic-bezier(.2,.8,.2,1)"></span>
      </div>
      <span style="display: flex; justify-content: space-between; font-size: 13px; color: {NMUTED}; font-variant-numeric: tabular-nums"><span>[[ nowTxt ]]</span><span>[[ chName ]]</span><span>32:05</span></span>
    </div>
    <div style="display: flex; align-items: center; justify-content: space-between">
      <button onClick="[[ speed ]]" aria-label="Playback speed" style="width: 56px; height: 44px; border-radius: {R_M}px; background: {RAISED}; font-size: 14px; font-weight: 600">[[ speedTxt ]]</button>
      <button onClick="[[ back15 ]]" aria-label="Back 15 seconds" style="width: 52px; height: 52px; display: flex; align-items: center; justify-content: center">{ic8('back15', 30, MOON, 1.8)}</button>
      <button onClick="[[ toggle ]]" aria-label="[[ playLabel ]]" style="width: 76px; height: 76px; border-radius: 999px; background: {LIME}; color: {INK}; display: flex; align-items: center; justify-content: center">
        <sc-if value="[[ playing ]]" hint-placeholder-val="[[ false ]]">{ic8('pause', 30, INK, 3)}</sc-if><sc-if value="[[ paused ]]" hint-placeholder-val="[[ true ]]">{icon('play', 30, INK)}</sc-if></button>
      <button onClick="[[ fwd15 ]]" aria-label="Forward 15 seconds" style="width: 52px; height: 52px; display: flex; align-items: center; justify-content: center">{ic8('fwd15', 30, MOON, 1.8)}</button>
      <button onClick="[[ dl ]]" aria-pressed="[[ saved ]]" aria-label="[[ dlLabel ]]" style="width: 56px; height: 44px; border-radius: {R_M}px; background: [[ dlBg ]]; color: [[ dlFg ]]; display: flex; align-items: center; justify-content: center">{ic8('download', 20)}</button>
    </div>
    <div style="border-radius: {R_M}px; background: {RAISED}; padding: 4px 4px 4px 14px; display: flex; align-items: center; gap: 10px">
      {ic8('wifi-off', 20, MINT)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Low-data audio</span><span style="font-size: 13px; color: {NMUTED}">[[ dataTxt ]]</span></span>{switch(0, 'Low-data audio')}
    </div>
    <div role="tablist" aria-label="Episode" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {DEEP}">{tabs}</div>
    <sc-if value="[[ t0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; animation: fadeIn .25s ease-out both">{chap}</div></sc-if>
    <sc-if value="[[ t1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 6px; animation: fadeIn .25s ease-out both">
      <span style="display: flex; gap: 6px; align-items: center; margin-bottom: 4px"><span class="chip" style="border: 1px dashed {MINT}; color: {MINT}">AI-assisted transcript</span><span style="font-size: 13px; color: {NMUTED}">Checked by a person</span></span>{trans}</div></sc-if>
    <sc-if value="[[ t2 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">{lessons}
      <span style="display: flex; gap: 6px">{REVIEWED_D}</span></div></sc-if>
    <section style="border-top: 1px solid {NLINE}; padding-top: 16px; display: flex; flex-direction: column; gap: 12px">
      {ola_pill(label='Ask Ola about this episode', p='p')}
      <span style="font-size: 13px; line-height: 1.5; color: {NMUTED}">Guests share their own experience, not advice for you. Amara is a sample guest: real guests, their consent and rights are still open (Q-39).</span>
    </section>
  </div>
  {tabbar8('Learn', dark=True)}'''
    starts = []
    acc = 0
    for _t, _n, d in CHAPTERS:
        starts.append(acc)
        acc += d
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const C = %(chap)s, S = %(starts)s, TOT = %(tot)d, TL = %(tl)s;
    const ch = st.ch == null ? 1 : st.ch, off = st.off || 95, playing = !!st.playing, sp = st.sp || 0, tb = st.tb || 0, saved = !!st.saved;
    const t = Math.min(TOT, S[ch] + off);
    const mmss = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s %% 60)).padStart(2, '0');
    const v = {
      prog: Math.round(t / TOT * 1000) / 10, nowTxt: mmss(t), chName: C[ch],
      playing, paused: !playing, play: playing ? 'running' : 'paused', playLabel: playing ? 'Pause' : 'Play', toggle: () => this.setState({ playing: !playing }),
      back15: () => this.setState({ off: Math.max(0, off - 15) }), fwd15: () => this.setState({ off: off + 15 }),
      speedTxt: ['1×', '1.25×', '1.5×'][sp], speed: () => this.setState({ sp: (sp + 1) %% 3 }),
      saved, dl: () => this.setState({ saved: !saved }), dlLabel: saved ? 'Saved for offline' : 'Save for offline',
      dlBg: saved ? '%(lime)s' : '%(raised)s', dlFg: saved ? '%(evg)s' : '%(moon)s'
    };
%(sw)s
    v.dataTxt = (v.sw0 ? 'About 8 MB for this episode' : 'About 30 MB for this episode') + (saved ? '. Saved for offline' : '');
    for (let i = 0; i < 4; i++) {
      v['ch' + i] = () => this.setState({ ch: i, off: 0 }); v['chOn' + i] = ch === i;
      v['chT' + i] = ch === i ? '%(lime)s' : '%(nmuted)s'; v['chC' + i] = ch === i ? '%(moon)s' : '#C9D0CC'; v['chW' + i] = ch === i ? 600 : 500;
    }
    let cur = TL.findIndex((c) => c === ch); if (ch === 1 && off > 60) cur = cur + 1;
    for (let i = 0; i < TL.length; i++) { v['trBg' + i] = i === cur ? '%(deep)s' : 'transparent'; v['trFg' + i] = i === cur ? '%(moon)s' : '%(nmuted)s'; }
    for (let j = 0; j < 3; j++) { v['tb' + j] = () => this.setState({ tb: j }); v['tbOn' + j] = tb === j; v['t' + j] = tb === j; v['tbBg' + j] = tb === j ? '%(mint)s' : 'transparent'; v['tbFg' + j] = tb === j ? '%(night)s' : '%(nmuted)s'; }
    const kept = st.kept || [false, false, false];
    for (let i = 0; i < 3; i++) { v['kept' + i] = kept[i]; v['keep' + i] = () => { const k = kept.slice(); k[i] = !k[i]; this.setState({ kept: k }); }; v['keepBg' + i] = kept[i] ? '%(lime)s' : '%(raised)s'; v['keepFg' + i] = kept[i] ? '%(evg)s' : '%(moon)s'; }
    return v;
  }
}''' % dict(chap=json.dumps([n for _t, n, _d in CHAPTERS]), starts=json.dumps(starts), tot=TOTAL, tl=json.dumps([c for c, _w, _l in TRANSCRIPT]),
            lime=LIME, raised=RAISED, evg=EVG, moon=MOON, nmuted=NMUTED, deep=DEEP, mint=MINT, night=NIGHT, sw=switch_js(1, [True]))
    return with_css(phone('The AWO Podcast', body, logic, h=1720, bg=NIGHT, dark=True, defs=ola_defs('p')), PHONE_CSS + HUB_CSS + STORY_CSS)


# ---------------------------------------------------------------- My worst money mistake

SHOW = [('First name and city', 'Zodwa, Soweto'), ('First name only', 'Zodwa'), ('Anonymous', 'A member in Gauteng')]


def mistake():
    steps_bar = ''.join(f'<span style="flex: 1 1 0; height: 6px; border-radius: 2px; background: [[ sb{i} ]]; transition: background-color .3s"></span>' for i in range(3))
    prompts = ''.join(f'<button onClick="[[ pr{i} ]]" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {RAISED}; font-size: 14px; font-weight: 600">{t}</button>' for i, t in enumerate(['What did it cost?', 'How did it feel?', 'What happened next?']))
    radios = ''.join(f'''<button role="radio" aria-checked="[[ sh{i} ]]" onClick="[[ pick{i} ]]" style="width: 100%; min-height: 60px; border-radius: {R_M}px; background: [[ shBg{i} ]]; box-shadow: inset 0 0 0 [[ shBw{i} ]]px {MINT}; padding: 0 14px; display: flex; align-items: center; gap: 12px; text-align: left">
          <span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 999px; box-shadow: inset 0 0 0 2px {MINT}; display: flex; align-items: center; justify-content: center"><span style="width: 10px; height: 10px; border-radius: 999px; background: [[ shDot{i} ]]"></span></span>
          <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {NMUTED}">Shown as "{ex}"</span></span></button>''' for i, (n, ex) in enumerate(SHOW))
    field = f'width: 100%; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: {RAISED}; padding: 14px; font: inherit; font-size: 16px; line-height: 1.55; color: {MOON}; resize: none'
    body = f'''  <div class="scr" style="gap: 18px">
    <header style="display: flex; align-items: center; gap: 10px">
      <a href="R8-Learn.dc.html" aria-label="Close" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('close', 20, MOON, 2.2)}</a>
      <span style="flex-grow: 1; font-size: 17px; font-weight: 600">My worst money mistake</span>{chip_dark('Sample')}
    </header>
    <sc-if value="[[ notDone ]]" hint-placeholder-val="[[ true ]]"><div role="img" aria-label="[[ stepLabel ]]" style="display: flex; gap: 6px">{steps_bar}</div></sc-if>
    <sc-if value="[[ s0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: inR .32s cubic-bezier(.2,.8,.2,1) both">
      <h1 class="d" style="font-size: 34px">What happened?</h1>
      <p style="font-size: 16px; line-height: 1.5; color: {NMUTED}">Women learn most from what went wrong. Tell it your way; an editor helps with the rest.</p>
      <label for="mk-a" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">What happened</label>
      <textarea id="mk-a" rows="7" value="[[ a ]]" onInput="[[ typeA ]]" style="{field}"></textarea>
      <div style="display: flex; flex-wrap: wrap; gap: 8px">{prompts}</div>
      <span style="font-size: 13px; line-height: 1.45; color: {NMUTED}">Leave out anything that could identify someone else.</span>
    </div></sc-if>
    <sc-if value="[[ s1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: inR .32s cubic-bezier(.2,.8,.2,1) both">
      <h1 class="d" style="font-size: 34px">What would you tell someone about to do the same?</h1>
      <label for="mk-b" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your lesson</label>
      <textarea id="mk-b" rows="4" value="[[ b ]]" onInput="[[ typeB ]]" style="{field}"></textarea>
      <span style="font-size: 13px; line-height: 1.45; color: {NMUTED}">This becomes the lesson at the top of your story.</span>
    </div></sc-if>
    <sc-if value="[[ s2 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 14px; animation: inR .32s cubic-bezier(.2,.8,.2,1) both">
      <h1 class="d" style="font-size: 34px">How should we show it?</h1>
      <div role="radiogroup" aria-label="Your name" style="display: flex; flex-direction: column; gap: 8px">{radios}</div>
      <div style="min-height: 60px; border-radius: {R_M}px; background: {RAISED}; padding: 0 4px 0 14px; display: flex; align-items: center; gap: 10px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Leave out my amounts</span><span style="font-size: 13px; color: {NMUTED}">"R 4 000" becomes "a lot"</span></span>{switch(0, 'Leave out my amounts')}</div>
      <button role="checkbox" aria-checked="[[ agreed ]]" onClick="[[ agree ]]" style="min-height: 60px; display: flex; align-items: flex-start; gap: 12px; text-align: left; font-size: 15px; line-height: 1.45; padding-top: 8px"><span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: {R_S}px; background: [[ agreeBg ]]; box-shadow: inset 0 0 0 2px {MINT}; display: flex; align-items: center; justify-content: center">{icon('check', 16, NIGHT, 3)}</span>An editor may shorten it. I'll see the edit and approve it before anything is published, and I can take it down at any time.</button>
    </div></sc-if>
    <sc-if value="[[ done ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding-top: 40px; animation: rise .45s cubic-bezier(.2,.8,.2,1) both">
      <span style="width: 72px; height: 72px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 34, EVG, 2.8)}</span>
      <h1 class="d" style="font-size: 34px">Sent to an editor</h1>
      <p class="hand" style="font-size: 28px; color: {LIME}; {HF}">Thank you for telling it.</p>
      <p style="font-size: 16px; line-height: 1.5; color: {NMUTED}; max-width: 300px">You'll hear back within a week with the edit to approve. Nothing is published until you say yes.</p>
      <a href="R8-Learn.dc.html" style="margin-top: 8px; height: 52px; padding: 0 20px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Read other stories</a>
    </div></sc-if>
    <div style="flex-grow: 1"></div>
    <sc-if value="[[ notDone ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; gap: 8px">
      <sc-if value="[[ canBack ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ back ]]" style="flex: 1 1 0; height: 56px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 16px; font-weight: 600">Back</button></sc-if>
      <button onClick="[[ next ]]" aria-disabled="[[ blocked ]]" style="flex: 1.6 1 0; height: 56px; border-radius: {R_M}px; background: [[ nextBg ]]; color: [[ nextFg ]]; font-size: 16px; font-weight: 600">[[ nextLabel ]]</button>
    </div></sc-if>
    <span style="font-size: 12px; line-height: 1.5; color: {NMUTED}">A sample flow. Who may edit members' stories, how they're credited and whether contributors are paid are open (Q-42). AI never rewrites her words.</span>
  </div>
  {tabbar8('Learn', dark=True)}'''
    a0 = "My cousin said a store card would get me a free blender. I signed in the shop, and didn't read past the first page. The card had a monthly fee and credit life cover. A year later I had paid about R 4 000, and still owed the blender."
    b0 = "Read the whole agreement, even the page about the 'free' thing. Ask what it costs a month, not what it costs today."
    adds = ['It cost me about R 4 000 over a year.', 'I felt stupid, and I hid it from my husband.', 'I paid it off, then closed the card.']
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const s = st.s || 0, sh = st.sh == null ? 0 : st.sh, agreed = !!st.agreed;
    const a = st.a == null ? %(a0)s : st.a, b = st.b == null ? %(b0)s : st.b, ADD = %(adds)s;
    const blocked = s === 2 && !agreed;
    const v = {
      a, b, typeA: (e) => this.setState({ a: e.target.value }), typeB: (e) => this.setState({ b: e.target.value }),
      s0: s === 0, s1: s === 1, s2: s === 2, done: s === 3, notDone: s < 3, canBack: s > 0 && s < 3,
      stepLabel: 'Step ' + Math.min(3, s + 1) + ' of 3',
      back: () => this.setState({ s: s - 1 }), next: () => { if (!blocked) this.setState({ s: s + 1 }); },
      nextLabel: s === 2 ? 'Send to an editor' : 'Next', blocked: blocked ? 'true' : 'false',
      nextBg: blocked ? '%(raised)s' : '%(lime)s', nextFg: blocked ? '%(nmuted)s' : '%(ink)s',
      agreed, agree: () => this.setState({ agreed: !agreed }), agreeBg: agreed ? '%(mint)s' : 'transparent'
    };
    for (let i = 0; i < 3; i++) {
      v['sb' + i] = i <= s ? '%(lime)s' : '%(raised)s';
      v['pr' + i] = () => this.setState({ a: a + ' ' + ADD[i] });
      v['sh' + i] = sh === i; v['pick' + i] = () => this.setState({ sh: i }); v['shBg' + i] = sh === i ? '%(deep)s' : '%(raised)s'; v['shBw' + i] = sh === i ? 2 : 0; v['shDot' + i] = sh === i ? '%(mint)s' : 'transparent';
    }
%(sw)s
    return v;
  }
}''' % dict(a0=json.dumps(nbs(a0), ensure_ascii=False), b0=json.dumps(b0), adds=json.dumps([nbs(x) for x in adds], ensure_ascii=False), raised=RAISED, nmuted=NMUTED, lime=LIME, ink=INK, mint=MINT, deep=DEEP, sw=switch_js(1, [False]))
    return with_css(phone('My worst money mistake', body, logic, h=1180, bg=NIGHT, dark=True), PHONE_CSS + HUB_CSS + STORY_CSS)


BOARDS = [('R8-Story', story), ('R8-Podcast', podcast), ('R8-Mistake', mistake)]
