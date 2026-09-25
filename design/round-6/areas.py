"""R6-Learn, R6-Ask, R6-Vault, R6-Community, R6-Me at Volume 1 (Clean).
Ask and Me borrow Round 1 Night Oasis's structure (Ian liked both), in the Round 5 language."""
from lib6 import *


def row(lead, title, sub, last=False, chev=True, dark=False, href=None):
    line = NLINE if dark else '#EEF2EF'
    mut = NMUTED if dark else MUTED
    border = '' if last else f'border-bottom: 1px solid {line}; '
    c = icon('chev', 18, mut) if chev else ''
    inner = (f'{lead}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{title}</span>'
             f'<span style="font-size: 13px; color: {mut}">{sub}</span></span>{c}')
    if href:
        return f'<a href="{href}" style="{border}min-height: 64px; display: flex; align-items: center; gap: 12px">{inner}</a>'
    return f'<div style="{border}min-height: 64px; display: flex; align-items: center; gap: 12px">{inner}</div>'


def dot(bg, inner, size=38):
    return f'<span aria-hidden="true" style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: 999px; background: {bg}; display: flex; align-items: center; justify-content: center">{inner}</span>'


def seg_buttons(names, active_bg, active_fg, idle_fg, bg, key='tab'):
    btns = ''.join(f'<button onClick="[[ {key}{i} ]]" aria-pressed="[[ {key}On{i} ]]" style="flex: 1 1 0; height: 40px; border-radius: 999px; background: [[ {key}Bg{i} ]]; color: [[ {key}Fg{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s">{n}</button>' for i, n in enumerate(names))
    return f'<div role="group" style="display: flex; gap: 4px; padding: 4px; border-radius: 999px; background: {bg}">{btns}</div>'


def seg_logic(n, key, active_bg, active_fg, idle_fg, state='tab'):
    return f'''    for (let i = 0; i < {n}; i++) {{
      v['{key}' + i] = () => this.setState({{ {state}: i }});
      v['{key}On' + i] = {state} === i;
      v['{key}Bg' + i] = {state} === i ? '{active_bg}' : 'transparent';
      v['{key}Fg' + i] = {state} === i ? '{active_fg}' : '{idle_fg}';
    }}'''


# ---------------------------------------------------------------- Learn

LEARN_LISTS = [
    [('half', 'Saving together', '3 of 6 lessons. Next: savings groups'), ('cres', 'Sending money home', '1 of 4 lessons'), ('cres', 'Your first profile, explained', '1 of 2 lessons')],
    [('new', 'Business money', '5 lessons, about 20 minutes'), ('new', 'When business is slow', 'One lesson, 5 minutes'), ('new', 'Reading a loan offer', 'One lesson, 4 minutes')],
    [('full', 'Safety nets', '4 of 4 lessons, finished 20 September'), ('full', 'Where money goes', '3 of 3 lessons, finished in August')],
]


def learn():
    lists = ''
    for t, items in enumerate(LEARN_LISTS):
        rows = ''.join(row(dot(RAISED, moon(22, p, dark='#3A4541')), title, sub, last=(i == len(items) - 1), dark=True) for i, (p, title, sub) in enumerate(items))
        lists += f'<sc-if value="[[ tabOn{t} ]]" hint-placeholder-val="[[ {"true" if t == 0 else "false"} ]]"><section style="border-radius: 20px; background: {RAISED}; padding: 0 16px; display: flex; flex-direction: column; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{rows}</section></sc-if>'
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <h1 class="d" style="font-size: 50px">Learn</h1>
      <a href="R6-Ask.dc.html" style="height: 44px; padding: 0 16px 0 6px; border-radius: 999px; background: {RAISED}; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{ola('l', 32)}Ask Ola</a>
    </header>
    <section style="border-radius: 28px; background: {DEEP}; padding: 20px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px; font-weight: 600">Saving together</span><span class="cap" style="color: {NMUTED}">Lesson 3 of 6</span></div>
      <div role="img" aria-label="Lessons 1 and 2 done, lesson 3 next, 3 more to come" style="display: flex; gap: 10px">{moon(24, 'full')}{moon(24, 'full')}{moon(24, 'half', now=True)}{moon(24, 'new')}{moon(24, 'new')}{moon(24, 'new')}</div>
      <div style="height: 1px; background: {NLINE}; margin: 4px 0"></div>
      <h2 class="d" style="font-size: 36px">Savings groups, in three minutes</h2>
      <span style="font-size: 14px; color: {NMUTED}">Told through Thandi's story. One question at the end.</span>
      <a href="R4-M4-Lesson.dc.html" class="pill" style="margin-top: 4px; height: 52px; background: {LIME}; color: {INK}">{icon('play', 16, INK)}Start the lesson</a>
    </section>
    {seg_buttons(['In progress', 'New', 'Finished'], MINT, NIGHT, NMUTED, DEEP)}
    {lists}
    <p style="font-size: 14px; color: {NMUTED}; padding: 0 4px">You showed up three evenings this week.</p>
  </div>
  {tabbar6('Learn', dark=True)}'''
    logic = f'''class Component extends DCLogic {{
  renderVals() {{
    const st = this.state || {{}};
    const tab = st.tab || 0;
    const v = {{}};
{seg_logic(3, 'tab', MINT, NIGHT, NMUTED)}
    return v;
  }}
}}'''
    return phone('Learn', body, logic, h=844, bg=NIGHT, dark=True, defs=ola_defs('l'))


# ---------------------------------------------------------------- Ask

ASKS = [
    ('Explain my result', 'In plain language', 'stones',
     'Your profile is at stage 2 of 4. Your everyday habits are strong: bills get paid and most spending is planned. The area with the most room to grow is being ready for surprises. That usually starts with a small cushion kept only for the unexpected.',
     'Your profile, version 3', ['Say it more simply', 'What is a cushion?']),
    ("What's an emergency fund?", 'From the Vault', 'arch',
     "It's money kept aside only for surprises, like a broken geyser or a missed shift. Many people start with a small, fixed amount and build from there. Where you keep it matters: somewhere you can reach quickly, but not so easily that it gets spent.",
     'Vault: Safety net', ['Where could I keep it?', 'How is it different from savings?']),
    ('Check an offer', 'Spot common red flags', 'search',
     "Share the offer and I'll point out what's worth checking: the total you'd repay, the fees, the interest rate and what happens if a payment is late. I won't tell you whether to take it; that's your call.",
     'Lesson: Reading a loan offer', ['What fees are common?', 'What is interest?']),
    ('Prepare my check-in', 'Due on 13 October', 'pool',
     'Your check-in asks three things: how much is in your safety net today, whether anything big happened this month, and how money feels. Having your balance handy makes it quicker. It takes about two minutes.',
     'Check-ins, how they work', ['What changes after it?', 'Can I skip a month?']),
]


def ask():
    tiles = ''.join(f'''<button onClick="[[ ask{i} ]]" style="border-radius: 20px; background: {DEEP}; padding: 14px; min-height: 104px; display: flex; flex-direction: column; align-items: flex-start; gap: 8px; text-align: left">
          <span style="color: {MINT}">{icon(ic, 20, MINT)}</span><span style="font-size: 15px; font-weight: 600; line-height: 1.25">{t}</span><span class="cap" style="color: {NMUTED}">{s}</span></button>''' for i, (t, s, ic, *_rest) in enumerate(ASKS))
    answers = ''
    for i, (t, s, ic, a, src, follow) in enumerate(ASKS):
        fchips = ''.join(f'<span style="height: 40px; padding: 0 14px; border-radius: 999px; border: 1px solid {NLINE}; display: inline-flex; align-items: center; font-size: 14px; font-weight: 500">{f}</span>' for f in follow)
        answers += f'''<sc-if value="[[ a{i} ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; gap: 14px">
        <div style="align-self: flex-end; max-width: 270px; padding: 12px 16px; border-radius: 20px 20px 6px 20px; background: {RAISED}; font-size: 15px; line-height: 1.4; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{t}</div>
        <div style="display: flex; align-items: center; gap: 10px; animation: rise .28s cubic-bezier(.2,.8,.2,1) .3s both"><span class="jump" style="display: block">{ola('a', 34, happy=True)}</span><span style="font-size: 15px; font-weight: 600">Ola</span><span class="chip" style="border: 1px dashed {MINT}; color: {MINT}">AI-assisted</span></div>
        <section style="border-radius: 24px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 14px; animation: rise .45s cubic-bezier(.2,.8,.2,1) .5s both">
          <p style="font-size: 16px; line-height: 1.55">{a}</p>
          <div style="display: flex; align-items: center; gap: 8px; padding-top: 12px; border-top: 1px solid {NLINE}; font-size: 13px; color: {MINT}">{icon(ic, 16, MINT)}Source: {src}</div>
        </section>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; animation: rise .45s cubic-bezier(.2,.8,.2,1) .7s both">{fchips}</div>
      </div>
    </sc-if>'''
    body = f'''  <div class="scr" style="bottom: 0; padding-bottom: 20px; gap: 16px">
    <div style="display: flex; align-items: center; gap: 12px">
      <a href="R6-Learn.dc.html" aria-label="Back to Learn" style="width: 44px; height: 44px; flex-shrink: 0; box-sizing: border-box; border-radius: 999px; border: 1px solid {NLINE}; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"></path></svg></a>
      <span style="flex-grow: 1; font-size: 17px; font-weight: 600">Ask Ola</span>
      <sc-if value="[[ answering ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ reset ]]" style="height: 44px; padding: 0 14px; border-radius: 999px; background: {RAISED}; font-size: 14px; font-weight: 600">New question</button></sc-if>
    </div>
    <sc-if value="[[ idle ]]" hint-placeholder-val="[[ true ]]">
      <div style="display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding-top: 6px">
        <span style="position: relative; width: 132px; height: 132px; display: flex; align-items: center; justify-content: center">
          <span aria-hidden="true" style="position: absolute; inset: -18px; border-radius: 999px; background: radial-gradient(circle, rgba(134,227,196,.26) 0, rgba(169,155,255,.1) 45%, rgba(11,15,14,0) 70%); animation: pulse 3.6s ease-in-out infinite"></span>
          <span style="position: relative; display: block; animation: bob 3.6s ease-in-out infinite">{ola('a', 112)}</span>
        </span>
        <h1 class="d" style="font-size: 36px">What would you like to understand today?</h1>
        <p style="font-size: 15px; line-height: 1.45; color: {NMUTED}">Ask about your result, a money word, or an offer someone sent you.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
    </sc-if>
    {answers}
    <div style="flex-grow: 1"></div>
    <div style="height: 56px; border-radius: 999px; background: {RAISED}; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 18px">
      <label for="ask-in" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Ask anything about money</label>
      <input id="ask-in" placeholder="Ask anything about money" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 15px; color: {MOON}">
      <button aria-label="Ask by voice" style="width: 44px; height: 44px; border-radius: 999px; display: flex; align-items: center; justify-content: center; color: {NMUTED}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0M12 18v3"></path></svg></button>
      <button aria-label="Send" style="width: 44px; height: 44px; border-radius: 999px; background: {LIME}; color: {INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, INK)}</button>
    </div>
    <p style="font-size: 12px; line-height: 1.4; color: {NMUTED}; text-align: center">AWO explains and teaches. It doesn't give personal financial advice. Answers are AI-assisted and logged.</p>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const q = st.q == null ? -1 : st.q;
    const v = { idle: q === -1, answering: q !== -1, reset: () => this.setState({ q: -1 }) };
    for (let i = 0; i < %d; i++) { v['a' + i] = q === i; v['ask' + i] = () => this.setState({ q: i }); }
    return v;
  }
}''' % len(ASKS)
    return phone('Ask Ola', body, logic, h=844, bg=NIGHT, dark=True, defs=ola_defs('a'))


# ---------------------------------------------------------------- Vault

WORDS = [('Safety net', 'Saving', 0), ('Stokvel', 'Saving together', 0), ('Chama', 'Saving together', 0), ('Interest', 'Borrowing', 1),
         ('Credit record', 'Borrowing', 1), ('Cash flow', 'Business', 2), ('Float', 'Business', 2), ('Remittance fee', 'Sending money home', 3), ('Exchange rate', 'Sending money home', 3)]
CATS = ['All', 'Saving', 'Borrowing', 'Business', 'Sending home']


def vault():
    rows = ''
    for i, (w, c, k) in enumerate(WORDS):
        rows += f'<sc-if value="[[ w{i} ]]" hint-placeholder-val="[[ true ]]"><div style="border-bottom: 1px solid #EEF2EF; min-height: 62px; display: flex; align-items: center; gap: 12px">{dot(MIST, icon("arch", 18, EVG))}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{w}</span><span style="font-size: 13px; color: {MUTED}">{c}</span></span>{icon("chev", 18, MUTED)}</div></sc-if>'
    chips = ''.join(f'<button onClick="[[ cat{i} ]]" aria-pressed="[[ catOn{i} ]]" style="flex-shrink: 0; height: 44px; padding: 0 16px; border-radius: 999px; background: [[ catBg{i} ]]; color: [[ catFg{i} ]]; box-shadow: inset 0 0 0 1px [[ catBd{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{c}</button>' for i, c in enumerate(CATS))
    body = f'''  <div class="scr" style="gap: 14px">
    <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h1 class="d" style="font-size: 50px">Vault</h1><span style="font-size: 14px; color: {MUTED}; padding-bottom: 6px">12 words kept</span></header>
    <label for="v-search" style="height: 48px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 16px; color: {MUTED}">{icon('search', 20, MUTED)}<input id="v-search" placeholder="Search money words" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 15px; color: {INK}"></label>
    <div style="position: relative; height: 262px; perspective: 1400px; flex-shrink: 0">
      <div class="flipper" style="transform: [[ flipTf ]]">
        <section class="face-f" aria-hidden="[[ flipped ]]" style="border-radius: 28px; background: {LIME}; color: {EVG}; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px">
          <div style="display: flex; justify-content: space-between; align-items: flex-start"><span class="lbl">Word of the week</span>{icon('arch', 24, EVG)}</div>
          <span class="d" style="font-size: 54px">Stokvel</span>
          <span style="font-size: 14px">Say it: stok-fel</span>
          <span style="font-size: 15px; line-height: 1.45; color: {INK}">A savings group. Members pay in every month and take turns to receive the pot.</span>
          <button class="pill" tabindex="[[ frontTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; background: {EVG}; color: #FFFFFF">{icon('flip', 18, '#FFFFFF')}Flip for an example</button>
        </section>
        <section class="face-b" aria-hidden="[[ notFlipped ]]" style="border-radius: 28px; background: {EVG}; color: #FFFFFF; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
          <div style="display: flex; justify-content: space-between; align-items: center"><span class="lbl" style="color: {LIME}">For example</span><span class="chip" style="border: 1px dashed {ON_EVG}; color: {ON_EVG}">Sample</span></div>
          <span style="font-size: 18px; line-height: 1.45">Thandi and eleven neighbours each pay R 500 a month. Each month one of them takes home R 6 000. December is Thandi's turn.</span>
          <button class="pill" tabindex="[[ backTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; background: {LIME}; color: {EVG}">{icon('flip', 18, EVG)}Flip back</button>
        </section>
      </div>
    </div>
    <div role="group" aria-label="Filter words" style="display: flex; gap: 8px; overflow: hidden; margin-right: -20px">{chips}</div>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column; margin-bottom: -1px">{rows}</section>
  </div>
  {tabbar6('Vault')}'''
    cats = [k for _, _, k in WORDS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const cat = st.cat || 0, flipped = !!st.flipped;
    const cats = %(cats)s;
    const v = {
      flipTf: flipped ? 'rotateY(180deg)' : 'rotateY(0deg)', flipped, notFlipped: !flipped,
      frontTab: flipped ? -1 : 0, backTab: flipped ? 0 : -1,
      doFlip: () => this.setState({ flipped: !flipped })
    };
    for (let i = 0; i < cats.length; i++) v['w' + i] = cat === 0 || cats[i] === cat - 1;
    for (let i = 0; i < 5; i++) {
      v['cat' + i] = () => this.setState({ cat: i });
      v['catOn' + i] = cat === i;
      v['catBg' + i] = cat === i ? '%(evg)s' : '#FFFFFF';
      v['catFg' + i] = cat === i ? '#FFFFFF' : '%(ink)s';
      v['catBd' + i] = cat === i ? '%(evg)s' : '#DCE4DF';
    }
    return v;
  }
}''' % dict(cats=cats, evg=EVG, ink=INK)
    return phone('Vault', body, logic, h=1160)


# ---------------------------------------------------------------- Community

def community():
    def trio(a, b, c, ring='#FFFFFF'):
        return ('<span aria-hidden="true" style="display: flex; flex-shrink: 0">' + ''.join(
            f'<img class="face" src="{IMG[x]}" alt="" style="width: 30px; height: 30px; margin-left: {0 if i == 0 else -10}px; box-shadow: 0 0 0 2px {ring}">'
            for i, x in enumerate((a, b, c))) + '</span>')
    circles = [(('thandi', 'grace', 'amara'), 'Safety net circle', '8 women, week 3 of 6', 'R4-M5-Seen.dc.html'),
               (('wanjiru', 'zodwa', 'lindiwe'), 'Side hustles', '24 women', None),
               (('grace', 'thandi', 'lindiwe'), 'Stokvel treasurers', '12 women', None)]
    rows = ''.join(row(trio(*f), t, s, last=(i == 2), href=h) for i, (f, t, s, h) in enumerate(circles))
    body = f'''  <div class="scr" style="gap: 14px">
    <h1 class="d" style="font-size: 50px">Community</h1>
    <section style="border-radius: 28px; background: {BLUSH}; color: {BLUSH_INK}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; justify-content: space-between; align-items: center"><span class="lbl" style="color: {BLUSH_2}">This week's question</span>{icon('ripple', 22, BLUSH_INK)}</div>
      <span class="d" style="font-size: 34px">What did you say no to this week?</span>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <div style="display: flex; gap: 8px; align-items: flex-start"><img class="face" src="{IMG['thandi']}" alt="" style="width: 28px; height: 28px"><span style="padding: 9px 13px; border-radius: 6px 16px 16px 16px; background: rgba(255,255,255,.7); font-size: 14px; line-height: 1.4"><strong>Thandi</strong> A second pair of work shoes. The first pair is fine.</span></div>
        <div style="display: flex; gap: 8px; align-items: flex-start"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 28px; height: 28px"><span style="padding: 9px 13px; border-radius: 6px 16px 16px 16px; background: rgba(255,255,255,.7); font-size: 14px; line-height: 1.4"><strong>Wanjiru</strong> Lending to my cousin again. I said: after the school fees.</span></div>
        <sc-if value="[[ posted ]]" hint-placeholder-val="[[ false ]]"><div style="position: relative; align-self: flex-end; max-width: 260px; padding: 9px 13px; border-radius: 16px 6px 16px 16px; background: {BLUSH_INK}; color: {BLUSH}; font-size: 14px; line-height: 1.4; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span>[[ answer ]]</div></sc-if>
      </div>
      <sc-if value="[[ notPosted ]]" hint-placeholder-val="[[ true ]]">
        <div style="display: flex; gap: 8px">
          <label for="c-ans" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your answer</label>
          <input id="c-ans" value="[[ answer ]]" onInput="[[ type ]]" placeholder="Share yours" style="flex-grow: 1; min-width: 0; height: 44px; box-sizing: border-box; border: 0; border-radius: 999px; background: #FFFFFF; padding: 0 16px; font-size: 15px; color: {INK}">
          <button onClick="[[ post ]]" aria-label="Share your answer" style="width: 44px; height: 44px; border-radius: 999px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</button>
        </div>
      </sc-if>
      <span class="cap" style="color: {BLUSH_2}">[[ countText ]]</span>
    </section>
    <span style="font-size: 15px; font-weight: 600; padding: 2px 4px 0">Your circles</span>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">{rows}</section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; gap: 10px">
        <img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px">
        <span style="flex-grow: 1; font-size: 15px; font-weight: 600">Wanjiru <span style="font-weight: 400; color: {MUTED}">Nairobi</span></span>
        <button onClick="[[ doCheer ]]" aria-pressed="[[ cheered ]]" style="position: relative; height: 44px; padding: 0 14px; border-radius: 999px; background: [[ cheerBg ]]; color: [[ cheerFg ]]; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s">
          <sc-if value="[[ cheered ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span></sc-if>
          {icon('ripple', 18)}[[ cheerLabel ]]<span style="font-weight: 500; opacity: .75">[[ cheerCount ]]</span>
        </button>
      </div>
      <img src="{IMG['wanjiru_stall']}" alt="Wanjiru's homeware stall" style="width: 100%; height: 170px; object-fit: cover; object-position: 60% 40%; border-radius: 16px">
      <span style="font-size: 15px; line-height: 1.4">Seven evenings of notes. Now I know what the stall really earns.</span>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 16px; display: flex; align-items: center; gap: 14px">
      <span aria-hidden="true" style="width: 52px; height: 56px; flex-shrink: 0; border-radius: 14px; background: {MIST}; display: flex; flex-direction: column; align-items: center; justify-content: center"><span style="font-size: 12px; font-weight: 600; color: {MUTED}">Thu</span><span class="d" style="font-size: 24px">2</span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Ask a stokvel treasurer</span><span style="font-size: 13px; color: {MUTED}">Live, 19:00. Grace and Thandi host.</span></span>
      <button onClick="[[ remind ]]" aria-pressed="[[ reminded ]]" style="flex-shrink: 0; white-space: nowrap; height: 44px; padding: 0 14px; border-radius: 999px; background: [[ remBg ]]; color: [[ remFg ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">[[ remLabel ]]</button>
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
      countText: posted ? 'You and 38 women answered. First names only.' : '38 women answered. First names only, never amounts.',
      cheered, cheerLabel: cheered ? 'Cheered' : 'Cheer', cheerCount: cheered ? 25 : 24,
      cheerBg: cheered ? '%(blushInk)s' : '%(blush)s', cheerFg: cheered ? '%(blush)s' : '%(blushInk)s',
      doCheer: () => this.setState({ cheered: !cheered }),
      reminded, remind: () => this.setState({ reminded: !reminded }),
      remLabel: reminded ? 'Reminder set' : 'Remind me',
      remBg: reminded ? '%(evg)s' : '%(mist)s', remFg: reminded ? '#FFFFFF' : '%(ink)s'
    };
  }
}''' % dict(blush=BLUSH, blushInk=BLUSH_INK, evg=EVG, mist=MIST, ink=INK)
    return phone('Community', body, logic, h=1290)


# ---------------------------------------------------------------- Me (DIVA profile)

DIMS = [
    ('Everyday money', 'Financial Health', 40, 71,
     'Bills are paid on time and most spending is planned. This is your strongest area.',
     'You pay your bills and plan your spending. Keep doing that.'),
    ('Ready for surprises', 'Risk and Resilience', 25, 48,
     'A surprise cost would be hard to cover right now. A small safety net makes the biggest difference here.',
     'If something unexpected costs money, it would be hard right now. A small cushion helps most.'),
    ('Knowing your options', 'Capital Positioning', 20, 60,
     "You know a few ways to save and borrow, and you're still exploring which fit your life.",
     'You know some ways to save and borrow. There are more to learn about.'),
    ('Clear goals', 'Goal Clarity', 15, 69,
     'You have clear goals for the year. Adding a date and an amount makes them easier to track.',
     'You know what you want this year. Give each goal a date and an amount.'),
]
OVERALL = ('Your everyday money habits are a real strength. The most room to grow is being ready for surprises: right now, an unexpected cost would likely knock your plans off course.',
           'You handle day-to-day money well. What is missing is a cushion for surprises. Building one, a little at a time, is the next thing to learn.')


def me():
    tiles = ''.join(f'''<button onClick="[[ dim{i} ]]" aria-pressed="[[ dimOn{i} ]]" style="border-radius: 20px; background: [[ dimBg{i} ]]; box-shadow: inset 0 0 0 [[ dimBw{i} ]]px {EVG}; padding: 14px; display: flex; flex-direction: column; align-items: stretch; gap: 6px; text-align: left; transition: background-color .18s, box-shadow .18s">
          <span style="display: flex; justify-content: space-between; align-items: center; gap: 6px"><span style="font-size: 14px; font-weight: 600; line-height: 1.2">{n}</span>{'<span class="chip" style="height: 24px; padding: 0 8px; background: ' + EVG + '; color: #FFFFFF">Focus</span>' if s == 48 else ''}</span>
          <span class="d" style="font-size: 44px; font-variant-numeric: tabular-nums">{s}</span>
          <span aria-hidden="true" style="height: 6px; border-radius: 3px; background: #E4ECE7; overflow: hidden"><span style="display: block; width: {s}%; height: 100%; border-radius: 3px; background: {EVG}; transform-origin: left; animation: fill .6s cubic-bezier(.2,.8,.2,1) {0.2 + i * 0.08:.2f}s both"></span></span>
          <span style="font-size: 12px; color: {MUTED}">{d}, {w}% of the score</span>
        </button>''' for i, (n, d, w, s, *_t) in enumerate(DIMS))
    vst = [(42, 96, 30, 12), (124, 70, 32, 13), (206, 44, 34, 13), (280, 18, 22, 8)]
    dash = ' stroke-dasharray="5 5"'
    vsvg = ''.join(f'<ellipse cx="{x}" cy="{y + 6}" rx="{rx}" ry="{ry}" fill="{"#BFD9D2" if i < 3 else "none"}"></ellipse>'
                   f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[POOL, POOL, LIME, "none"][i]}" stroke="{EVG}" stroke-width="2.5"{dash if i == 3 else ""}></ellipse>'
                   for i, (x, y, rx, ry) in enumerate(vst))
    vlabels = ''.join(f'<span style="position: absolute; left: {x - 40}px; top: {y + 22}px; width: 80px; text-align: center; display: flex; flex-direction: column; gap: 1px"><span class="d" style="font-size: {26 if i < 3 else 16}px; color: {EVG if i < 3 else MUTED}">{v}</span><span style="font-size: 12px; color: {MUTED}">{m}</span></span>'
                      for i, ((x, y, _rx, _ry), (v, m)) in enumerate(zip(vst, [('55', 'July'), ('59', 'August'), ('63', 'September'), ('Next', '13 October')])))
    body = f'''  <div class="scr" style="gap: 14px">
    <header style="display: flex; align-items: center; gap: 12px">
      <img class="face" src="{IMG['naledi']}" alt="Naledi" style="width: 48px; height: 48px">
      <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><h1 class="d" style="font-size: 42px">Naledi</h1><span style="font-size: 13px; color: {MUTED}">Johannesburg, a member since July</span></div>
      <button aria-label="Settings" style="width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('gear', 20, INK)}</button>
    </header>
    <section style="border-radius: 28px; background: {POOL}; color: {EVG}; padding: 20px; display: flex; flex-direction: column; align-items: center; gap: 12px">
      <div style="display: flex; width: 100%; justify-content: space-between; align-items: center"><span class="lbl">Your DIVA profile</span>{sample_chip(EVG)}</div>
      <div role="img" aria-label="Overall readiness 63 out of 100" style="position: relative; width: 210px; height: 190px">
        <div style="position: absolute; left: 0; top: 0">{arc(210, 63, '#B7D5CE', EVG, sw=14)}</div>
        <div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; padding-top: 8px"><span class="d" style="font-size: 76px; color: {EVG}">63</span><span style="font-size: 13px; font-weight: 600">overall readiness</span></div>
      </div>
      <span class="d" style="font-size: 34px; margin-top: -8px">Stage 2 of 4</span>
      <span class="cap" style="color: {SEC}; text-align: center">Readiness to learn and act, not a credit score. Worked out from your answers on AWO's servers.</span>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; box-shadow: inset 0 0 0 1.5px {EVG}; padding: 14px 16px; display: flex; align-items: flex-start; gap: 12px">
      <span aria-hidden="true" style="color: {EVG}; margin-top: 1px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path></svg></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Evidence: early</span><span role="img" aria-label="1 of 3" style="display: flex; gap: 4px"><span style="width: 18px; height: 6px; border-radius: 3px; background: {EVG}"></span><span style="width: 18px; height: 6px; border-radius: 3px; background: #DCE4DF"></span><span style="width: 18px; height: 6px; border-radius: 3px; background: #DCE4DF"></span></span></span>
        <span class="cap" style="color: {SEC}">Mostly your own answers. Check-ins and quiz answers add evidence. This is separate from the score.</span>
      </span>
    </section>
    <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 4px 4px 0"><span style="font-size: 15px; font-weight: 600">Your four dimensions</span><span class="cap" style="color: {MUTED}">Tap one</span></div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">[[ meaningTitle ]]</span><sc-if value="[[ simple ]]" hint-placeholder-val="[[ false ]]"><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span></sc-if></div>
      <p style="font-size: 16px; line-height: 1.5">[[ meaning ]]</p>
      <button onClick="[[ toggleSimple ]]" aria-pressed="[[ simple ]]" style="align-self: flex-start; height: 44px; padding: 0 16px; border-radius: 999px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 8px">{icon('flip', 16, EVG)}[[ simpleLabel ]]</button>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 8px">
      <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Your versions</span><span class="cap" style="color: {MUTED}">Each check-in adds one. Old ones never change.</span></span>
      <div role="img" aria-label="Readiness 55 in July, 59 in August, 63 in September; next check-in on 13 October" style="position: relative; height: 170px"><svg width="318" height="120" viewBox="0 0 318 120" aria-hidden="true" style="display: block; overflow: visible">{vsvg}</svg>{vlabels}</div>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">
      {row(dot(MIST, '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="' + EVG + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"></path></svg>'), 'Download my report', 'A PDF of version 3')}
      {row(dot(MIST, icon('lock', 18, EVG)), 'Your data', 'Stored in South Africa. Yours to download or delete.', last=True)}
    </section>
  </div>
  {tabbar6('Me')}'''
    dims_js = [[n, t, s] for (n, _d, _w, _v, t, s) in DIMS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const sel = st.sel == null ? -1 : st.sel;
    const simple = !!st.simple;
    const dims = %(dims)s;
    const overall = %(overall)s;
    const v = {
      meaningTitle: sel === -1 ? 'What this means' : dims[sel][0] + ', in plain words',
      meaning: sel === -1 ? overall[simple ? 1 : 0] : dims[sel][simple ? 2 : 1],
      simple, toggleSimple: () => this.setState({ simple: !simple }),
      simpleLabel: simple ? 'Show the original wording' : 'Explain it more simply'
    };
    for (let i = 0; i < 4; i++) {
      v['dim' + i] = () => this.setState({ sel: sel === i ? -1 : i });
      v['dimOn' + i] = sel === i;
      v['dimBg' + i] = sel === i ? '%(pool)s' : '#FFFFFF';
      v['dimBw' + i] = sel === i ? 2 : 0;
    }
    return v;
  }
}''' % dict(dims=dims_js, overall=list(OVERALL), pool=POOL)
    return phone('Me, your DIVA profile', body, logic, h=1720)


if __name__ == '__main__':
    out = sys.argv[1]
    for name, fn in [('R6-Learn', learn), ('R6-Ask', ask), ('R6-Vault', vault), ('R6-Community', community), ('R6-Me', me)]:
        write(os.path.join(out, name + '.dc.html'), fn())
