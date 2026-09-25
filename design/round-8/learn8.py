"""Round 8, batch 2: Learn with three tabs (Paths, Words, Stories) and the animated switch, a topic page
("Shares and dividends") and the buzzword decoder. Writes R8-Learn, R8-Topic-Shares, R8-Words-Decoder.

Learn stays night (Q-30) and is Ola's home (D-021). Words keeps the Vault's lime arch."""
import json

from lib8 import *  # noqa: F401,F403

PHONE_CSS = """
.scr>*,.pane>*{flex-shrink:0}
@keyframes inR{from{opacity:0;transform:translateX(28px)}to{opacity:1;transform:none}}
@keyframes inL{from{opacity:0;transform:translateX(-28px)}to{opacity:1;transform:none}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes archRise{from{opacity:0;transform:translateY(24px) scaleY(.86)}to{opacity:1;transform:none}}
@keyframes ringOut{from{transform:scale(1);opacity:.8}to{transform:scale(1.35);opacity:0}}
@keyframes dotDrop{from{opacity:0;transform:translateY(-14px)}to{opacity:1;transform:none}}
@keyframes draw{from{stroke-dashoffset:1.05}to{stroke-dashoffset:0}}
.tabbtn{transition:color .2s}
"""

LEARN_TABS = [('Paths', 'moon'), ('Words', 'arch'), ('Stories', 'ring')]
TAB_W = 114  # each of the three tabs, inside a 350px control with 4px padding


def learn_tabs():
    """The switch: a mint pill that stretches towards the tab she chose, then catches up."""
    btns = ''.join(f'<button role="tab" class="tabbtn" onClick="[[ tab{i} ]]" aria-selected="[[ tOn{i} ]]" style="position: relative; z-index: 1; flex: 1 1 0; height: 44px; display: flex; align-items: center; justify-content: center; gap: 7px; font-size: 15px; font-weight: 600; color: [[ tFg{i} ]]">{ic8(g, 18)}{n}</button>'
                   for i, (n, g) in enumerate(LEARN_TABS))
    return (f'<div role="tablist" aria-label="Learn" style="position: relative; display: flex; padding: 4px; border-radius: {R_M}px; background: {DEEP}">'
            f'<span aria-hidden="true" style="position: absolute; top: 4px; bottom: 4px; left: [[ indL ]]px; right: [[ indR ]]px; border-radius: 8px; background: {MINT}; '
            f'transition: left .34s cubic-bezier(.2,.8,.2,1) [[ dl ]]s, right .34s cubic-bezier(.2,.8,.2,1) [[ dr ]]s"></span>{btns}</div>')


def learn_tabs_js():
    return '''    const t = st.t || 0, from = st.from == null ? t : st.from;
    const dir = t > from ? 1 : (t < from ? -1 : 0);
    v.indL = 4 + t * %(w)d; v.indR = 346 - %(w)d * (t + 1);
    v.dl = dir > 0 ? .08 : 0; v.dr = dir < 0 ? .08 : 0;
    v.paneAnim = dir > 0 ? 'inR' : (dir < 0 ? 'inL' : 'fadeIn');
    for (let i = 0; i < 3; i++) {
      v['tab' + i] = () => { if (i !== t) this.setState({ from: t, t: i }); };
      v['tOn' + i] = t === i; v['p' + i] = t === i; v['tFg' + i] = t === i ? '%(night)s' : '%(muted)s';
    }''' % dict(w=TAB_W, night=NIGHT, muted=NMUTED)


def ola_pill(href='R7-Ask.dc.html', label='Ask Ola', p='l'):
    return (f'<a href="{href}" style="height: 44px; padding: 0 16px 0 6px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; gap: 8px; '
            f'font-size: 14px; font-weight: 600">{ola(p, 32)}{label}</a>')


def chip_dark(text, col=NMUTED):
    return f'<span class="chip" style="border: 1px dashed {col}; color: {col}">{text}</span>'


REVIEWED_D = f'<span class="chip" style="background: {MINT}; color: {NIGHT}">{icon("check", 14, NIGHT, 2.6)}Reviewed by AWO</span>'


# ---------------------------------------------------------------- Paths

TOPICS = [('Investing', 'grow', LIME, EVG, 'Shares, ETFs, fees', 'R8-Topic-Shares.dc.html', None),
          ('Crypto', 'hexa', IRIS, NIGHT, 'What it is, and the scams', None, 'Scam checks'),
          ('Forex', 'swap', IRIS, NIGHT, 'Why most traders lose', None, 'Scam checks'),
          ('Companies explained', 'building', MINT, NIGHT, 'How they make money', None, None),
          ('Pay and tax', 'doc', MINT, NIGHT, 'Your payslip, line by line', None, None),
          ('Debt and credit', 'down', BLUSH, BLUSH_INK, 'Getting out, staying out', None, None),
          ('Saving together', 'people', LIME, EVG, 'Stokvels and chamas', None, None),
          ('Your business', 'shop', MINT, NIGHT, 'Prices, invoices, profit', None, None)]


def topic_tile(name, g, bg, fg, sub, href, tag):
    tag_html = f'<span class="chip" style="position: absolute; right: 10px; top: 12px; height: 24px; padding: 0 8px; background: {NWARN_BG}; color: {NWARN_FG}">{tag}</span>' if tag else ''
    inner = (f'<span style="width: 40px; height: 40px; border-radius: {R_M}px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic8(g, 22)}</span>'
             f'<span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 15px; font-weight: 600; line-height: 1.2">{name}</span><span style="font-size: 13px; line-height: 1.3; color: {NMUTED}">{sub}</span></span>{tag_html}')
    st = f'position: relative; min-height: 118px; box-sizing: border-box; border-radius: {R_L}px; background: {RAISED}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px; text-align: left'
    if href:
        return f'<a href="{href}" style="{st}; box-shadow: inset 0 0 0 1.5px {LIME}">{inner}</a>'
    return f'<button style="{st}">{inner}</button>'


def paths_pane():
    moons = ''.join(f'<span style="animation: rise .4s cubic-bezier(.2,.8,.2,1) {0.08 + i * 0.06:.2f}s both">{moon(24, p, now=(i == 1))}</span>'
                    for i, p in enumerate(['full', 'half', 'new', 'new', 'new', 'new']))
    tiles = ''.join(topic_tile(*t) for t in TOPICS)
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px; font-weight: 600">Investing, from zero</span><span style="font-size: 13px; color: {NMUTED}">Lesson 2 of 6</span></div>
        <div role="img" aria-label="Lesson 1 done, lesson 2 next, 4 more to come" style="display: flex; gap: 10px">{moons}</div>
        <div style="height: 1px; background: {NLINE}; margin: 2px 0"></div>
        <h2 class="d" style="font-size: 32px">Shares and dividends, in four minutes</h2>
        <span style="font-size: 14px; line-height: 1.4; color: {NMUTED}">Told through Lindiwe's first R 200 of shares. One question at the end.</span>
        <div style="display: flex; gap: 8px; margin-top: 4px">
          <a href="R7-Lesson.dc.html" style="flex: 1.3 1 0; height: 52px; border-radius: {R_M}px; background: {LIME}; color: {INK}; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{icon('play', 16, INK)}Start the lesson</a>
          <a href="R8-Topic-Shares.dc.html" style="flex: 1 1 0; height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">The topic</a>
        </div>
      </section>
      <a href="R8-Words-Decoder.dc.html" style="min-height: 60px; border-radius: {R_L}px; background: {RAISED}; padding: 0 14px; display: flex; align-items: center; gap: 12px">
        <span style="color: {LIME}">{icon('arch', 22, LIME)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Heard a word you didn't know?</span><span style="font-size: 13px; color: {NMUTED}">Decode it in Words</span></span>{icon('chev', 18, NMUTED)}</a>
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 4px"><span style="font-size: 17px; font-weight: 600">Explore paths</span><span style="font-size: 13px; color: {NMUTED}">Sample list</span></div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
      <p class="hand" style="font-size: 24px; color: {MOON}; padding: 0 4px; white-space: nowrap; {HF}">Three evenings this week.</p>
    </div>'''


# ---------------------------------------------------------------- Words

W_COLLECTIONS = [('Investing', 'Dividend', 5), ('Scams and red flags', 'Pyramid scheme', 6), ('Saving together', 'Stokvel', 3), ('Sending home', 'Exchange rate', 2)]


def words_pane():
    tiles = ''.join(f'''<a href="R8-Words-Decoder.dc.html" style="height: 120px; box-sizing: border-box; border-radius: {R_L}px; background: {RAISED}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between">
          <span aria-hidden="true" style="position: relative; height: 46px; display: block">
            <span style="position: absolute; left: 14px; top: 0; width: 96px; height: 38px; border-radius: {R_S}px; background: #2E3A36; transform: rotate(6deg)"></span>
            <span style="position: absolute; left: 0; top: 6px; width: 110px; height: 38px; box-sizing: border-box; border-radius: {R_S}px; background: {DEEP}; box-shadow: 0 0 0 1px {NLINE}; display: flex; align-items: center; padding: 0 10px; font-size: 13px; font-weight: 600; color: {LIME}">{first}</span>
          </span>
          <span style="display: flex; justify-content: space-between; align-items: baseline; gap: 6px"><span style="font-size: 15px; font-weight: 600; line-height: 1.2">{name}</span><span style="font-size: 13px; color: {NMUTED}">{n}</span></span>
        </a>''' for name, first, n in W_COLLECTIONS)
    tries = ''.join(f'<a href="R8-Words-Decoder.dc.html" class="chip" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {DEEP}; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 14px; color: {MOON}">{w}</a>' for w in ('ETF', 'Pips', 'Black tax'))
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <div style="position: relative; height: 340px; perspective: 1400px; animation: archRise .5s cubic-bezier(.2,.8,.2,1) .06s both; transform-origin: 50% 100%">
        <div class="flipper" style="transform: [[ flipTf ]]">
          <section class="face-f" aria-hidden="[[ flipped ]]" style="border-radius: 175px 175px {R_L}px {R_L}px; background: {LIME}; color: {EVG}; padding: 64px 28px 22px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px">
            <span class="lbl">Word of the week</span>
            <span class="d" style="font-size: 58px">Dividend</span>
            <span style="font-size: 15px">div-i-dend</span>
            <span style="font-size: 17px; line-height: 1.35; color: {INK}; max-width: 260px">A share of a company's profit, paid to the people who own its shares.</span>
            <button tabindex="[[ frontTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{icon('flip', 18, '#FFFFFF')}See an example</button>
          </section>
          <section class="face-b" aria-hidden="[[ notFlipped ]]" style="border-radius: 175px 175px {R_L}px {R_L}px; background: {EVG}; color: #FFFFFF; padding: 78px 28px 20px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px">
            <span class="lbl" style="color: {LIME}">For example</span>
            <span style="font-size: 18px; line-height: 1.45">Lindiwe owns 20 shares. This year the company pays R 2 a share, so R 40 lands in her account.</span>
            <span class="chip" style="border: 1px dashed {ON_EVG}; color: {ON_EVG}">Sample</span>
            <button tabindex="[[ backTab ]]" onClick="[[ doFlip ]]" style="margin-top: auto; height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{icon('flip', 18, EVG)}Flip back</button>
          </section>
        </div>
      </div>
      <a href="R8-Words-Decoder.dc.html" style="height: 56px; border-radius: {R_M}px; background: {RAISED}; padding: 0 16px; display: flex; align-items: center; gap: 12px; color: {NMUTED}">{icon('search', 20, MOON)}<span style="font-size: 16px">Heard a word? Decode it.</span></a>
      <div style="display: flex; gap: 8px; align-items: center; margin-top: -6px"><span style="font-size: 13px; color: {NMUTED}; margin-right: 2px">Try</span>{tries}</div>
      <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 14px 14px 14px 18px; display: flex; align-items: center; gap: 14px">
        <span aria-hidden="true" style="position: relative; width: 44px; height: 40px; flex-shrink: 0"><span style="position: absolute; left: 8px; top: 0; width: 30px; height: 38px; border-radius: {R_S}px; background: {LIME}; opacity: .45; transform: rotate(10deg)"></span><span style="position: absolute; left: 2px; top: 2px; width: 30px; height: 38px; border-radius: {R_S}px; background: {LIME}"></span></span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">3 words to practise</span><span style="font-size: 13px; color: {ON_EVG}">About two minutes</span></span>
        <a href="R7-Vault.dc.html" style="height: 44px; padding: 0 18px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Start</a>
      </section>
      <span style="font-size: 17px; font-weight: 600; margin-top: 4px">Your collections</span>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{tiles}</div>
    </div>'''


# ---------------------------------------------------------------- Stories

def stories_pane():
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <a href="R8-Podcast.dc.html" style="position: relative; height: 262px; border-radius: {R_L}px; overflow: hidden; display: block; color: #FFFFFF">
        <img src="{IMG['amara_coat']}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 22%">
        <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(11,15,14,.94) 0, rgba(11,15,14,.55) 55%, rgba(11,15,14,.05) 100%)"></span>
        <span style="position: absolute; left: 16px; top: 14px; display: flex; gap: 6px"><span class="chip" style="background: {LIME}; color: {EVG}">The AWO Podcast</span><span class="chip" style="background: rgba(11,15,14,.6); color: #FFFFFF; border: 1px dashed #FFFFFF">Sample guest</span></span>
        <span style="position: absolute; left: 16px; right: 84px; bottom: 16px; display: flex; flex-direction: column; gap: 6px">
          <span class="d" style="font-size: 28px">Closing a shop, and opening a better one</span>
          <span style="font-size: 13px; color: #DDE3E0">Episode 12, with Amara. 32 minutes, four chapters</span>
        </span>
        <span aria-label="Play" style="position: absolute; right: 16px; bottom: 16px; width: 56px; height: 56px; border-radius: 999px; background: {LIME}; color: {INK}; display: flex; align-items: center; justify-content: center">{icon('play', 22, INK)}</span>
      </a>
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 2px"><span style="font-size: 17px; font-weight: 600">Rise</span><span style="font-size: 13px; color: {NMUTED}">Failure, then rising</span></div>
      <div style="display: flex; gap: 12px; margin-right: -20px; overflow: hidden">
        <a href="R8-Story.dc.html" style="width: 286px; flex-shrink: 0; border-radius: {R_L}px; background: {RAISED}; overflow: hidden; display: flex; flex-direction: column">
          <span style="position: relative; height: 170px; display: block">
            <img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her market stall" style="width: 100%; height: 100%; object-fit: cover; display: block">
            <span aria-hidden="true" style="position: absolute; left: 14px; bottom: -22px; width: 48px; height: 48px; border-radius: 999px; box-shadow: 0 0 0 3px {LIME}; animation: ringOut 1.2s cubic-bezier(.2,.8,.2,1) .3s both"></span>
            <img class="face" src="{IMG['wanjiru']}" alt="" style="position: absolute; left: 14px; bottom: -22px; width: 48px; height: 48px; box-shadow: 0 0 0 3px {LIME}">
          </span>
          <span style="padding: 30px 16px 16px; display: flex; flex-direction: column; gap: 6px">
            <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; color: {NMUTED}">Wanjiru, Nairobi</span><span class="chip" style="background: {BLUSH}; color: {BLUSH_INK}">Member story</span></span>
            <span style="font-size: 19px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.25">My first stall closed in four months.</span>
            <span class="hand" style="font-size: 24px; color: {LIME}; {HF}">Then I started again.</span>
          </span>
        </a>
        <a href="R8-Story.dc.html" style="width: 286px; flex-shrink: 0; border-radius: {R_L}px; background: {RAISED}; overflow: hidden; display: flex; flex-direction: column">
          <span style="height: 170px; display: block"><img src="{IMG['thandi_window']}" alt="Thandi by a window" style="width: 100%; height: 100%; object-fit: cover; display: block"></span>
          <span style="padding: 16px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; color: {NMUTED}">Thandi, Durban</span><span style="font-size: 19px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.25">I lent my savings to a cousin. Here's what I'd do now.</span></span>
        </a>
      </div>
      <section style="border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span class="lbl">My worst money mistake</span><span class="chip" style="border: 1px dashed {BLUSH_INK}; color: {BLUSH_INK}">Sample</span></span>
        <p style="font-size: 18px; line-height: 1.4; font-weight: 500">"I signed for a store card to get a free blender. It cost me R 4 000."</p>
        <span style="display: flex; align-items: center; gap: 8px; font-size: 13px"><img class="face" src="{IMG['zodwa']}" alt="" style="width: 28px; height: 28px">Zodwa, Soweto</span>
        <div style="height: 1px; background: rgba(42,15,24,.15)"></div>
        <p style="font-size: 16px; line-height: 1.4">"I paid a 'forex mentor' R 1 500 for signals. Then he stopped answering."</p>
        <span style="display: flex; align-items: center; gap: 8px; font-size: 13px"><img class="face" src="{IMG['grace']}" alt="" style="width: 28px; height: 28px">Grace, Kampala</span>
        <a href="R8-Mistake.dc.html" style="margin-top: 4px; height: 48px; border-radius: {R_M}px; background: {BLUSH_INK}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">Tell yours</a>
        <span style="font-size: 13px; line-height: 1.4">Told by members, edited with them, first names only.</span>
      </section>
    </div>'''


def learn():
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <h1 class="d" style="font-size: 44px">Learn</h1>
      {ola_pill()}
    </header>
    {learn_tabs()}
    <sc-if value="[[ p0 ]]" hint-placeholder-val="[[ true ]]">{paths_pane()}</sc-if>
    <sc-if value="[[ p1 ]]" hint-placeholder-val="[[ false ]]">{words_pane()}</sc-if>
    <sc-if value="[[ p2 ]]" hint-placeholder-val="[[ false ]]">{stories_pane()}</sc-if>
  </div>
  {tabbar8('Learn', dark=True)}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%s
    const flipped = !!st.flipped;
    v.flipTf = flipped ? 'rotateY(180deg)' : 'rotateY(0deg)'; v.flipped = flipped; v.notFlipped = !flipped;
    v.frontTab = flipped ? -1 : 0; v.backTab = flipped ? 0 : -1; v.doFlip = () => this.setState({ flipped: !flipped });
    return v;
  }
}''' % learn_tabs_js()
    return with_css(phone('Learn', body, logic, h=1330, bg=NIGHT, dark=True, defs=ola_defs('l')), PHONE_CSS + HUB_CSS)


# ---------------------------------------------------------------- Topic: shares and dividends

STEPS = [('A company is cut into shares', 'Sample Bakery is cut into 100 equal pieces, called shares. Whoever holds a share owns a piece of the bakery.'),
         ('You buy two', 'You buy two shares at R 100 each. You now own 2% of the bakery: two pieces out of a hundred.'),
         ('It makes a profit', 'This year the bakery makes R 50 000 after paying for flour, rent and wages. That is its profit.'),
         ('It pays some of it out', 'The bakery keeps half to grow, and pays out half: R 250 for each share. Your two shares get R 500. That is a dividend.'),
         ('And the price can move', 'The price of a share goes up and down with how people rate the business. You can get back less than you put in.')]
MINE = (44, 45)
LESSONS = [('full', 'What you own when you own a share', '4 min'), ('half', 'Dividends: when a company pays you', '4 min'),
           ('new', 'How a stock exchange works', '5 min'), ('new', 'ETFs: many shares in one', '4 min'),
           ('new', 'Fees, the quiet cost', '3 min'), ('new', 'Before you start', '4 min')]
TOPIC_WORDS = ['Share', 'Dividend', 'Stock exchange', 'ETF', 'Index', 'Capital gains']


def share_grid():
    cells, dots = '', ''
    for k in range(100):
        r, c = divmod(k, 10)
        x, y = c * 29, r * 29
        if k in MINE:
            cells += f'<span style="position: absolute; left: {x}px; top: {y}px; width: 24px; height: 24px; border-radius: {R_S}px; background: [[ mineBg ]]; box-shadow: inset 0 0 0 1.5px [[ mineBd ]]; transition: background-color .3s"></span>'
        else:
            cells += f'<span style="position: absolute; left: {x}px; top: {y}px; width: 24px; height: 24px; border-radius: {R_S}px; background: [[ cellBg ]]; box-shadow: inset 0 0 0 1.5px #33413C; transition: background-color .5s {(r + c) * 0.015:.3f}s"></span>'
        col = NIGHT if k in MINE else MINT
        dots += f'<span style="position: absolute; left: {x + 8}px; top: {y + 8}px; width: 8px; height: 8px; border-radius: 999px; background: {col}; animation: dotDrop .4s cubic-bezier(.2,.8,.2,1) {(r + c) * 0.025:.3f}s both"></span>'
    price = (f'<svg width="285" height="96" viewBox="0 0 285 96" aria-hidden="true" style="display: block; overflow: visible">'
             f'<path d="M0 60H285" stroke="{NLINE}" stroke-width="1" stroke-dasharray="3 5"></path>'
             f'<path pathLength="1" d="M0 60C30 52 50 40 80 44S120 78 150 74 200 30 230 26 270 34 285 20" fill="none" stroke="{LIME}" stroke-width="3" stroke-linecap="round" style="stroke-dasharray: 1.05 1.05; animation: draw 1.1s cubic-bezier(.2,.8,.2,1) both"></path></svg>')
    return f'''<div role="img" aria-label="[[ gridLabel ]]" style="position: relative; width: 285px; height: 285px; margin: 0 auto">{cells}
          <sc-if value="[[ showDots ]]" hint-placeholder-val="[[ false ]]"><span style="position: absolute; inset: 0">{dots}</span></sc-if>
        </div>
        <sc-if value="[[ showPrice ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 4px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">{price}<span style="display: flex; justify-content: space-between; font-size: 12px; color: {NMUTED}"><span>R 100 when you bought</span><span>R 91</span><span>R 124 today</span></span></div></sc-if>'''


def topic():
    lessons = ''.join(f'''<a href="R7-Lesson.dc.html" style="min-height: 60px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + NLINE + ";" if i else ""}">
          {moon(24, p, now=(p == 'half'))}<span style="flex-grow: 1; font-size: 15px; font-weight: {600 if p == 'half' else 500}; line-height: 1.3">{t}</span><span style="flex-shrink: 0; white-space: nowrap; font-size: 13px; color: {NMUTED}">{m}</span></a>''' for i, (p, t, m) in enumerate(LESSONS))
    words = ''.join(f'<a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {RAISED}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{icon("arch", 16, LIME)}{w}</a>' for w in TOPIC_WORDS)
    checks = ''.join(f'<span style="display: flex; align-items: center; gap: 12px; font-size: 16px; line-height: 1.35"><span style="width: 28px; height: 28px; flex-shrink: 0; border-radius: 999px; box-shadow: inset 0 0 0 2px {MINT}; display: flex; align-items: center; justify-content: center">{icon("check", 16, MINT, 2.4)}</span>{t}</span>'
                     for t in ('A safety net for surprises, first', 'No expensive debt, like a store card', "Money you won't need for five years or more"))
    body = f'''  <div class="scr" style="gap: 18px">
    <header style="display: flex; align-items: center; gap: 10px">
      <a href="R8-Learn.dc.html" aria-label="Back to Learn" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('back', 20, MOON, 2.2)}</a>
      <span class="chip" style="background: {LIME}; color: {EVG}">{ic8('grow', 14, EVG, 2.2)}Investing</span>
      <span style="flex-grow: 1"></span>
      <button onClick="[[ toggleSave ]]" aria-pressed="[[ saved ]]" aria-label="Save this topic" style="width: 44px; height: 44px; border-radius: {R_M}px; background: [[ saveBg ]]; color: [[ saveFg ]]; display: flex; align-items: center; justify-content: center; transition: background-color .18s">{ic8('bookmark', 20)}</button>
    </header>
    <div style="display: flex; flex-direction: column; gap: 10px">
      <h1 class="d" style="font-size: 46px">Shares and dividends</h1>
      <p style="font-size: 16px; line-height: 1.45; color: {NMUTED}">What you own when you own a share, and the two ways it can pay you. Six short lessons, about 25 minutes.</p>
    </div>
    <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px 16px 16px; display: flex; flex-direction: column; gap: 16px">
      <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 13px; font-weight: 600; color: {MINT}">[[ stepLabel ]]</span>{chip_dark('Sample')}</div>
      <h2 class="d" style="font-size: 28px; min-height: 28px">[[ stepTitle ]]</h2>
      {share_grid()}
      <p style="font-size: 16px; line-height: 1.5; min-height: 72px">[[ stepText ]]</p>
      <div style="display: flex; gap: 8px">
        <button onClick="[[ prev ]]" aria-disabled="[[ atStart ]]" style="flex: 1 1 0; height: 48px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; opacity: [[ prevOp ]]">Back</button>
        <button onClick="[[ next ]]" style="flex: 1.6 1 0; height: 48px; border-radius: {R_M}px; background: {LIME}; color: {INK}; font-size: 15px; font-weight: 600">[[ nextLabel ]]</button>
      </div>
    </section>
    <section style="display: flex; flex-direction: column; gap: 4px">
      <span style="font-size: 17px; font-weight: 600; margin-bottom: 6px">In this topic</span>
      <div style="border-radius: {R_L}px; background: {RAISED}; padding: 0 16px; display: flex; flex-direction: column">{lessons}</div>
    </section>
    <section style="display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 17px; font-weight: 600">Words in this topic</span>
      <div style="display: flex; flex-wrap: wrap; gap: 8px">{words}</div>
    </section>
    <section style="display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 17px; font-weight: 600">Try it with your own numbers</span>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
        <a href="R8-Tool-Fees.dc.html" style="min-height: 150px; box-sizing: border-box; border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px">
          <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600">{hub_icon(None, 18, EVG)}In the Hub</span>
          <span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 17px; font-weight: 600">Fee eater</span><span style="font-size: 13px; line-height: 1.35; color: {INK}">What a 1% yearly fee costs over 20 years</span></span></a>
        <a href="R8-Goals.dc.html" style="min-height: 150px; box-sizing: border-box; border-radius: {R_L}px; background: {RAISED}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px">
          <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: {MINT}">{icon('pool', 18, MINT)}A goal</span>
          <span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 17px; font-weight: 600">Start investing</span><span style="font-size: 13px; line-height: 1.35; color: {NMUTED}">A goal template, with its own pool</span></span></a>
      </div>
    </section>
    <section style="border-radius: {R_L}px; box-shadow: inset 0 0 0 1.5px {MINT}; padding: 18px; display: flex; flex-direction: column; gap: 14px">
      <span style="font-size: 17px; font-weight: 600">Before you start</span>
      <span style="font-size: 15px; line-height: 1.45; color: {NMUTED}">Many people check three things before they buy a first share:</span>
      {checks}
      <span style="font-size: 13px; line-height: 1.45; color: {NMUTED}">A way to think it through, not advice for you. Lesson 6 goes deeper.</span>
    </section>
    <a href="R8-Story.dc.html" style="border-radius: {R_L}px; background: {RAISED}; padding: 16px; display: flex; gap: 12px; align-items: flex-start">
      <img class="face" src="{IMG['grace']}" alt="" style="width: 44px; height: 44px">
      <span style="display: flex; flex-direction: column; gap: 6px"><span style="display: flex; gap: 6px; align-items: center"><span style="font-size: 13px; color: {NMUTED}">A painful lesson, from Grace</span>{chip_dark('Sample')}</span><span style="font-size: 17px; font-weight: 600; line-height: 1.3">"I bought what a WhatsApp group told me to buy."</span></span>
    </a>
    <section style="border-top: 1px solid {NLINE}; padding-top: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; gap: 8px; flex-wrap: wrap">{REVIEWED_D}{chip_dark('Sample')}</span>
      <p style="font-size: 14px; line-height: 1.5; color: {NMUTED}">Education, not a recommendation. AWO never tells you what to buy, and no platform pays to appear here.</p>
      {ola_pill(label='Ask Ola about shares', p='t')}
    </section>
  </div>
  {tabbar8('Learn', dark=True)}'''
    steps = json.dumps([[nbs(a), nbs(b)] for a, b in STEPS], ensure_ascii=False)
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const S = %(steps)s;
    const s = st.s || 0, saved = !!st.saved;
    return {
      stepLabel: 'Step ' + (s + 1) + ' of ' + S.length, stepTitle: S[s][0], stepText: S[s][1],
      next: () => this.setState({ s: s === S.length - 1 ? 0 : s + 1 }), prev: () => this.setState({ s: Math.max(0, s - 1) }),
      nextLabel: s === S.length - 1 ? 'Start again' : 'Next', atStart: s === 0 ? 'true' : 'false', prevOp: s === 0 ? .45 : 1,
      mineBg: s >= 1 ? '%(lime)s' : 'transparent', mineBd: s >= 1 ? '%(lime)s' : '#33413C',
      cellBg: s === 2 ? '#1E3B32' : 'transparent', showDots: s === 3, showPrice: s === 4,
      gridLabel: ['100 squares, one for each share', 'Two of the 100 squares are yours', 'The whole company made a profit', 'Every share gets R 250; your two get R 500', 'The share price moved from R 100 to R 91, then R 124'][s],
      saved, toggleSave: () => this.setState({ saved: !saved }), saveBg: saved ? '%(lime)s' : '%(raised)s', saveFg: saved ? '%(evg)s' : '%(moon)s'
    };
  }
}''' % dict(steps=steps, lime=LIME, raised=RAISED, evg=EVG, moon=MOON)
    return with_css(phone('Shares and dividends', body, logic, h=2470, bg=NIGHT, dark=True, defs=ola_defs('t')), PHONE_CSS + HUB_CSS)


# ---------------------------------------------------------------- Words: the buzzword decoder

WORDS = [
    dict(k='etf', word='ETF', full='Exchange-traded fund', say='E-T-F', coll='Investing', alias=['exchange traded fund', 'exchange-traded', 'index tracker'],
         depths=['One thing you can buy that holds many shares at once, like a basket.',
                 'An ETF usually follows an index, such as the 40 biggest companies on an exchange. It trades like a share, and its price moves all day.',
                 'ETFs often cost less than other funds because nobody picks the shares. Check the yearly fee (the TER): small differences grow over 20 years.'],
         places=['In South Africa, ETFs trade on the JSE. Many people hold them inside a tax-free savings account.',
                 'In Kenya, a few ETFs trade on the Nairobi Securities Exchange.',
                 'In the UK, ETFs are often held inside an ISA, where growth is tax-free.'],
         confused=['unittrust', 'dividend'], flag=None, weave=[('Shares and dividends', 'R8-Topic-Shares.dc.html', 'moon'), ('Fee eater', 'R8-Tool-Fees.dc.html', 'hub')]),
    dict(k='dividend', word='Dividend', full='A share of a company\'s profit', say='div-i-dend', coll='Investing', alias=['dividends', 'payout'],
         depths=["A share of a company's profit, paid to the people who own its shares.",
                 "Companies may pay once or twice a year. They don't have to: some keep the profit to grow instead.",
                 'Tax is usually taken before it reaches you, and the rules differ by country. A share that pays a big dividend is not always a good business.'],
         places=['In South Africa, dividends are usually taxed at 20% before they reach you, except inside a tax-free savings account.',
                 'In Kenya, a withholding tax is taken from dividends before they are paid.',
                 'In the UK, a small yearly dividend allowance is tax-free.'],
         confused=['etf'], flag=None, weave=[('Shares and dividends', 'R8-Topic-Shares.dc.html', 'moon')]),
    dict(k='pips', word='Pips', full='The smallest usual move in a currency price', say='pips', coll='Scams and red flags', alias=['pip', 'forex', 'fx'],
         depths=['The smallest usual move in a currency price. Forex traders count wins and losses in pips.',
                 'Most currency pairs are priced to four decimal places. One pip is the fourth: 0.0001.',
                 'Retail forex is usually traded with borrowed money (leverage), so a few pips can wipe out a deposit. EU regulators found 74 to 89% of retail accounts lose money.'],
         places=['In South Africa, anyone selling forex advice or signals needs an FSCA licence.',
                 "In Kenya, forex brokers are licensed by the Capital Markets Authority.",
                 'In the UK, firms must be authorised by the FCA. Check its register.'],
         confused=['cryptoscam'], flag='Heard in a scam? Signal sellers promise "100 pips a day". Selling trading signals without a licence is illegal in South Africa. Check the FSCA register before you pay anyone.',
         weave=[('Forex: why most traders lose', 'R8-Learn.dc.html', 'moon'), ('Check an offer', 'R7-Offer.dc.html', 'hub')]),
    dict(k='blacktax', word='Black tax', full='Family support', say='black tax', coll='Sending home', alias=['family support', 'supporting family', 'sending money home'],
         depths=["Money you regularly give to family: a parent's rent, a sibling's fees, a cousin's emergency.",
                 "It's common and often expected. Planning it as its own line in your budget makes it easier to keep giving without falling behind.",
                 'In 2025, 44% of South African households supported more than one generation (Old Mutual Savings and Investment Monitor).'],
         places=["In South Africa it's often called black tax.", 'In Kenya it often means supporting family upcountry.', 'For the diaspora, it often travels as money sent home.'],
         confused=[], flag=None, weave=[('Pay-day plan, with family support', 'R8-Tool-Payday.dc.html', 'hub'), ('Thandi\'s story', 'R8-Story.dc.html', 'ring')]),
    dict(k='compound', word='Compound interest', full='Interest on interest', say='com-pound', coll='Investing', alias=['compounding', 'compound growth'],
         depths=['Interest earned on interest. Your money grows on what it has already grown.',
                 'The longer it has, the more it compounds. Starting early matters more than starting big.',
                 'It works against you on debt too: unpaid interest on a store card earns interest of its own.'],
         places=['In South Africa, a tax-free savings account lets growth compound without tax.', 'In Kenya, money market funds pay interest that can compound monthly.', 'In the UK, an ISA lets growth compound without tax.'],
         confused=['etf'], flag=None, weave=[('Fee eater', 'R8-Tool-Fees.dc.html', 'hub')]),
    dict(k='unittrust', word='Unit trust', full='A pooled fund', say='yoo-nit trust', coll='Investing', alias=['mutual fund', 'collective investment', 'money market fund'],
         depths=["A pot of many people's money, invested together by a manager.",
                 'You own units of the pot. Its price is worked out once a day.',
                 'Unlike most ETFs, a manager picks what goes in, and that usually costs more each year.'],
         places=['In South Africa they are called unit trusts or collective investment schemes.', 'In Kenya, money market funds are a popular kind.', 'In the UK the closest are unit trusts and OEICs.'],
         confused=['etf'], flag=None, weave=[('Shares and dividends', 'R8-Topic-Shares.dc.html', 'moon')]),
    dict(k='crypto', word='Crypto', full='Cryptocurrency', say='krip-toe', coll='Investing', alias=['cryptocurrency', 'bitcoin', 'coin', 'token', 'stablecoin'],
         depths=['Digital money that lives on a shared online record instead of in a bank. Its price can swing a lot in a day.',
                 'Bitcoin is the best known. Prices are set by what buyers will pay, so they can rise or fall fast, and no bank guarantees your money.',
                 'In South Africa, crypto counts as a financial product: providers need an FSCA licence, and SARS may tax your gains.'],
         places=['In South Africa, check that a crypto provider is on the FSCA register. Gains may be taxed by SARS.',
                 'In Kenya, the rules for crypto providers are new and still being set up.',
                 "In the UK, crypto firms must register with the FCA, and most crypto isn't protected if a firm fails."],
         confused=['cryptoscam'], flag=None, weave=[('Crypto: what it is, and the scams', 'R8-Learn.dc.html', 'moon'), ('Check an offer', 'R7-Offer.dc.html', 'hub')]),
    dict(k='cryptoscam', word='Crypto scam', full='A scheme that uses crypto as bait', say='krip-toe scam', coll='Scams and red flags', alias=['rug pull', 'crypto fraud', 'mining scheme'],
         depths=['A scheme that uses crypto as bait: guaranteed returns, "mining" plans, or a coin that vanishes.',
                 'One kind is a "rug pull": the people behind a new coin sell everything at once, and the price falls to nothing.',
                 'In South Africa, crypto providers need an FSCA licence. A guarantee, a deadline or a reward for recruiting are all red flags.'],
         places=['In South Africa, check the FSCA register for licensed crypto providers.', "In Kenya, the Capital Markets Authority warns about unlicensed platforms.", 'In the UK, check the FCA register and its warning list.'],
         confused=['pips'], flag='If someone promises a fixed return on crypto, or pays you for bringing friends, stop. Both are on AWO\'s red-flag list.',
         weave=[('Check an offer', 'R7-Offer.dc.html', 'hub'), ('Crypto: what it is, and the scams', 'R8-Learn.dc.html', 'moon')]),
]
TRY = [('ETF', 'etf'), ('Pips', 'pips'), ('Black tax', 'blacktax'), ('Rug pull', None), ('Staking', None), ('Dividend', 'dividend')]
PLACES = ['South Africa', 'Kenya', 'UK']
DEPTHS = ['New to this', 'The basics', 'Go deeper']


def word_card(w):
    k = w['k']
    depths = ''.join(f'<sc-if value="[[ d{j} ]]" hint-placeholder-val="[[ {"true" if j == 0 else "false"} ]]"><p style="font-size: 17px; line-height: 1.5; animation: fadeIn .25s ease-out both">{t}</p></sc-if>' for j, t in enumerate(w['depths']))
    places = ''.join(f'<sc-if value="[[ pl{j} ]]" hint-placeholder-val="[[ {"true" if j == 0 else "false"} ]]"><p style="font-size: 15px; line-height: 1.45; color: {NMUTED}; animation: fadeIn .25s ease-out both">{t}</p></sc-if>' for j, t in enumerate(w['places']))
    by_k = {x['k']: x for x in WORDS}
    conf = ''
    if w['confused']:
        chips = ''.join(f'<button onClick="[[ pick_{c} ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {RAISED}; font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 8px">{icon("arch", 16, LIME)}{by_k[c]["word"]}</button>' for c in w['confused'])
        conf = f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; font-weight: 600; color: {NMUTED}">Often confused with</span><div style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div></div>'
    flag = ''
    if w['flag']:
        flag = f'<div style="border-radius: {R_M}px; background: {NWARN_BG}; color: {NWARN_FG}; padding: 12px 14px; display: flex; gap: 10px; font-size: 15px; line-height: 1.45"><span style="padding-top: 2px">{ALERT}</span><span>{w["flag"]}</span></div>'
    weave = ''.join(f'<a href="{href}" style="min-height: 48px; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600; {"border-top: 1px solid " + NLINE + ";" if i else ""}"><span style="width: 32px; height: 32px; border-radius: 8px; background: {LIME if g == "hub" else RAISED}; color: {EVG if g == "hub" else MINT}; display: flex; align-items: center; justify-content: center">{ic8(g, 18)}</span><span style="flex-grow: 1">{t}</span>{icon("chev", 16, NMUTED)}</a>'
                    for i, (t, href, g) in enumerate(w['weave']))
    return f'''<sc-if value="[[ sel_{k} ]]" hint-placeholder-val="[[ {"true" if k == "etf" else "false"} ]]">
      <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 14px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
        <div style="display: flex; gap: 6px; flex-wrap: wrap"><span class="chip" style="background: {RAISED}; color: {MOON}">{icon('arch', 14, LIME)}{w['coll']}</span>{REVIEWED_D}{chip_dark('Sample')}</div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <span class="d" style="font-size: 50px; color: {LIME}">{w['word']}</span>
          <span style="font-size: 17px; font-weight: 500">{w['full']}</span>
        </div>
        <button aria-label="Hear it said: {w['say']}" style="align-self: flex-start; height: 44px; padding: 0 14px 0 10px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; gap: 8px; font-size: 14px; color: {MOON}">{ic8('speaker', 20, MINT)}Say it: {w['say']}</button>
        <div role="tablist" aria-label="How deep" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {RAISED}">[[ DEPTHS ]]</div>
        <div style="min-height: 104px">{depths}</div>
        <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; font-weight: 600; color: {NMUTED}">Where you live</span><div style="display: flex; gap: 6px">[[ PLACES ]]</div>{places}</div>
        {conf}
        {flag}
        <div style="display: flex; flex-direction: column; border-top: 1px solid {NLINE}; padding-top: 4px">{weave}</div>
        <div style="display: flex; gap: 8px">
          <button onClick="[[ toggleKeep ]]" aria-pressed="[[ kept ]]" style="flex: 1 1 0; height: 52px; border-radius: {R_M}px; background: [[ keepBg ]]; color: [[ keepFg ]]; box-shadow: inset 0 0 0 1px [[ keepBd ]]; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px; transition: background-color .18s">[[ keepLabel ]]</button>
          <a href="R7-Ask.dc.html" style="flex: 1 1 0; height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 6px">{ola('w' + k, 26)}An example</a>
        </div>
      </section>
    </sc-if>'''


def decoder():
    depth_btns = ''.join(f'<button role="tab" onClick="[[ dep{j} ]]" aria-selected="[[ d{j} ]]" style="flex: 1 1 0; height: 40px; border-radius: 8px; background: [[ dBg{j} ]]; color: [[ dFg{j} ]]; font-size: 13px; font-weight: 600; transition: background-color .18s">{n}</button>' for j, n in enumerate(DEPTHS))
    place_btns = ''.join(f'<button onClick="[[ pla{j} ]]" aria-pressed="[[ pl{j} ]]" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: [[ plBg{j} ]]; color: [[ plFg{j} ]]; box-shadow: inset 0 0 0 1px [[ plBd{j} ]]; font-size: 14px; font-weight: 600">{n}</button>' for j, n in enumerate(PLACES))
    cards = ''.join(word_card(w) for w in WORDS).replace('[[ DEPTHS ]]', depth_btns).replace('[[ PLACES ]]', place_btns)
    # every word card holds its own "pick" buttons for the words it's confused with
    tries = ''.join(f'<button onClick="[[ try{i} ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {RAISED}; font-size: 15px; font-weight: 600">{t}</button>' for i, (t, _k) in enumerate(TRY))
    sugg = ''.join(f'''<sc-if value="[[ m_{w['k']} ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ pick_{w['k']} ]]" style="width: 100%; min-height: 60px; border-radius: {R_M}px; background: {RAISED}; padding: 8px 14px; display: flex; align-items: center; gap: 12px; text-align: left">
          {icon('arch', 20, LIME)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{w['word']}</span><span style="font-size: 13px; color: {NMUTED}">{w['full']}</span></span>
          <sc-if value="[[ fz_{w['k']} ]]" hint-placeholder-val="[[ false ]]"><span class="chip" style="border: 1px dashed {MINT}; color: {MINT}">AI-assisted match</span></sc-if></button></sc-if>''' for w in WORDS)
    body = f'''  <div class="scr" style="gap: 14px">
    <header style="display: flex; align-items: center; gap: 12px">
      <a href="R8-Learn.dc.html" aria-label="Back to Learn" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('back', 20, MOON, 2.2)}</a>
      <span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 13px; color: {NMUTED}">Words</span><span style="font-size: 18px; font-weight: 600">Decode a word</span></span>
    </header>
    <label for="dec-q" style="height: 56px; border-radius: {R_M}px; background: {RAISED}; box-shadow: inset 0 0 0 2px {MINT}; padding: 0 6px 0 16px; display: flex; align-items: center; gap: 10px">
      {icon('search', 20, MOON)}
      <input id="dec-q" value="[[ q ]]" onInput="[[ type ]]" placeholder="A word you heard" autocomplete="off" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 17px; color: {MOON}; outline: none">
      <sc-if value="[[ hasQ ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ clear ]]" aria-label="Clear" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('close', 18, NMUTED, 2.2)}</button></sc-if>
    </label>
    <sc-if value="[[ idle ]]" hint-placeholder-val="[[ false ]]">
      <div style="display: flex; flex-direction: column; gap: 14px; animation: fadeIn .25s ease-out both">
        <span style="font-size: 15px; color: {NMUTED}">Type a word you heard, or try one:</span>
        <div style="display: flex; flex-wrap: wrap; gap: 8px">{tries}</div>
        <section style="border-radius: {R_L}px; background: {DEEP}; padding: 16px; display: flex; flex-direction: column; gap: 8px; margin-top: 6px">
          <span style="font-size: 15px; font-weight: 600">How the decoder works</span>
          <span style="font-size: 14px; line-height: 1.5; color: {NMUTED}">A person at AWO writes every word, and a second person checks it. AI only helps match what you typed, like "exchange traded" to ETF. It never writes a meaning.</span>
        </section>
      </div>
    </sc-if>
    <sc-if value="[[ listing ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 8px; animation: fadeIn .2s ease-out both">{sugg}</div></sc-if>
    <sc-if value="[[ missing ]]" hint-placeholder-val="[[ false ]]">
      <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 12px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
        <span class="d" style="font-size: 30px">"[[ q ]]" isn't in Words yet</span>
        <span style="font-size: 15px; line-height: 1.5; color: {NMUTED}">A person at AWO writes every word, and a second person checks it. Ask for it and we'll tell you when it's in.</span>
        <sc-if value="[[ notAsked ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ ask ]]" style="height: 52px; width: 100%; border-radius: {R_M}px; background: {LIME}; color: {INK}; font-size: 16px; font-weight: 600">Ask for this word</button></sc-if>
        <sc-if value="[[ asked ]]" hint-placeholder-val="[[ false ]]"><span style="display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 600; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="width: 32px; height: 32px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 18, EVG, 2.8)}</span>Asked. We'll let you know.</span></sc-if>
        <sc-if value="[[ hasClosest ]]" hint-placeholder-val="[[ true ]]"><div style="border-top: 1px solid {NLINE}; padding-top: 12px; display: flex; flex-direction: column; gap: 8px">
          <span style="font-size: 13px; font-weight: 600; color: {NMUTED}">[[ closestLabel ]]</span>
          <button onClick="[[ pickClosest ]]" style="min-height: 56px; border-radius: {R_M}px; background: {RAISED}; padding: 0 14px; display: flex; align-items: center; gap: 12px; text-align: left">{icon('arch', 20, LIME)}<span style="flex-grow: 1; font-size: 16px; font-weight: 600">[[ closestWord ]]</span><span class="chip" style="border: 1px dashed {MINT}; color: {MINT}">AI-assisted match</span></button>
        </div></sc-if>
      </section>
    </sc-if>
    {cards}
  </div>
  {tabbar8('Learn', dark=True)}'''
    data = json.dumps([dict(k=w['k'], word=w['word'], alias=w['alias']) for w in WORDS])
    tries_js = json.dumps(TRY)
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const W = %(data)s, T = %(tries)s;
    const q = st.q == null ? 'ETF' : st.q, sel = st.sel === undefined ? 'etf' : st.sel;
    const norm = (s) => s.toLowerCase().replace(/[^a-z0-9 ]/g, ' ').replace(/ +/g, ' ').trim();
    const qq = norm(q);
    const v = { q, hasQ: q.length > 0, idle: !q.length && !sel };
    let any = false;
    W.forEach((w) => {
      const exact = qq.length > 0 && norm(w.word).startsWith(qq);
      const fuzzy = qq.length > 1 && !exact && w.alias.some((a) => norm(a).includes(qq) || qq.includes(norm(a)));
      v['m_' + w.k] = exact || fuzzy; v['fz_' + w.k] = fuzzy; any = any || exact || fuzzy;
      v['sel_' + w.k] = sel === w.k;
      v['pick_' + w.k] = () => this.setState({ sel: w.k, q: w.word, d: 0 });
    });
    v.listing = !sel && qq.length > 0 && any;
    v.missing = !sel && qq.length > 2 && !any;
    const asked = !!st.asked;
    v.asked = asked; v.notAsked = !asked; v.ask = () => this.setState({ asked: true });
    const closest = /rug|pull|scam|mining|ponzi/.test(qq) ? 'cryptoscam' : (/stak|coin|token|chain|wallet|nft|defi/.test(qq) ? 'crypto' : (/pip|forex|fx|lot|leverage/.test(qq) ? 'pips' : null));
    v.hasClosest = !!closest; v.closestLabel = 'The closest word we have'; v.closestWord = closest ? W.find((w) => w.k === closest).word : '';
    v.pickClosest = () => this.setState({ sel: closest, q: v.closestWord, d: 0 });
    v.type = (e) => this.setState({ q: e.target.value, sel: null, asked: false });
    v.clear = () => this.setState({ q: '', sel: null, asked: false });
    T.forEach((t, i) => { v['try' + i] = () => this.setState(t[1] ? { q: t[0], sel: t[1], d: 0 } : { q: t[0], sel: null, asked: false }); });
    const d = st.d || 0, pl = st.pl || 0;
    for (let j = 0; j < 3; j++) {
      v['d' + j] = d === j; v['dep' + j] = () => this.setState({ d: j });
      v['dBg' + j] = d === j ? '%(mint)s' : 'transparent'; v['dFg' + j] = d === j ? '%(night)s' : '%(muted)s';
      v['pl' + j] = pl === j; v['pla' + j] = () => this.setState({ pl: j });
      v['plBg' + j] = pl === j ? '%(moon)s' : 'transparent'; v['plFg' + j] = pl === j ? '%(night)s' : '%(moon)s'; v['plBd' + j] = pl === j ? '%(moon)s' : '%(line)s';
    }
    const kept = !!(st.kept || {})[sel];
    v.kept = kept; v.keepLabel = kept ? 'Kept in your Words' : 'Keep this word';
    v.keepBg = kept ? '%(lime)s' : 'transparent'; v.keepFg = kept ? '%(evg)s' : '%(moon)s'; v.keepBd = kept ? '%(lime)s' : '%(line)s';
    v.toggleKeep = () => this.setState({ kept: Object.assign({}, st.kept || {}, { [sel]: !kept }) });
    return v;
  }
}''' % dict(data=data, tries=tries_js, mint=MINT, night=NIGHT, muted=NMUTED, moon=MOON, line=NLINE, lime=LIME, evg=EVG)
    defs = ''.join(ola_defs('w' + w['k']) for w in WORDS)
    return with_css(phone('Decode a word', body, logic, h=1330, bg=NIGHT, dark=True, defs=defs), PHONE_CSS + HUB_CSS)


BOARDS = [('R8-Learn', learn), ('R8-Topic-Shares', topic), ('R8-Words-Decoder', decoder)]
