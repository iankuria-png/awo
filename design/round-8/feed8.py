"""Round 8, batch 4: Community as a feed to read and post in (D-038). Writes R8-Feed ("For you" and "Circles"),
R8-Compose (Note, Letter, Milestone, Question, with the AI rule check), R8-Post (a question with replies, a hidden
reply and reporting) and R8-Feed-Parts (the five post kinds, reactions, and what the feed never shows).

Rules as in Round 7: no advice to buy or switch, no recruiting, first names only; AI flags and people decide.
No follower counts and no public reaction totals: the author alone sees how many."""
import json

from lib8 import *  # noqa: F401,F403
from learn8 import PHONE_CSS
from stories8 import reactions, reactions_js, STORY_CSS
from biz8 import crop, PRODUCTS

FEED_CSS = """
@keyframes stoneDrop{0%{transform:translateY(-46px);opacity:0}60%{transform:translateY(3px);opacity:1}80%{transform:translateY(-2px)}100%{transform:none;opacity:1}}
@keyframes ripOut{from{transform:scale(.6);opacity:.8}to{transform:scale(1.9);opacity:0}}
.drop8{animation:stoneDrop .8s cubic-bezier(.2,.8,.2,1) .5s both}
.rip8{transform-box:fill-box;transform-origin:center;animation:ripOut .9s cubic-bezier(.2,.8,.2,1) 1.1s both}
"""
REASONS = ['Advice to buy, sell or switch', 'Recruiting, or a scheme that promises returns', 'Unkind or unsafe', "Someone's private information", 'Something else']
RULES_LINE = 'No advice to buy or switch. No recruiting. First names only. AI flags posts; people decide.'


def kind_chip(text, bg=MIST, fg=SEC):
    return f'<span class="chip" style="background: {bg}; color: {fg}">{text}</span>'


def more_btn(hole, label):
    return (f'<button onClick="[[ {hole} ]]" aria-label="{label}" style="width: 44px; height: 44px; flex-shrink: 0; margin: -6px -10px 0 0; border-radius: {R_M}px; '
            f'display: flex; align-items: center; justify-content: center; color: {MUTED}">{ic8("more", 22, MUTED, 3)}</button>')


def author(face, name, meta, chip='', more=''):
    return (f'<div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG[face]}" alt="" style="width: 40px; height: 40px">'
            f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-size: 15px; font-weight: 600">{name}</span><span style="font-size: 13px; color: {MUTED}">{meta}</span></span>{chip}{more}</div>')


def report_sheet():
    """One report sheet for any post or reply: a reason, then a plain promise."""
    radios = ''.join(f'''<button role="radio" aria-checked="[[ rr{i} ]]" onClick="[[ rPick{i} ]]" style="width: 100%; min-height: 52px; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 999px; box-shadow: inset 0 0 0 2px {BLUSH_INK}; display: flex; align-items: center; justify-content: center"><span style="width: 10px; height: 10px; border-radius: 999px; background: [[ rDot{i} ]]"></span></span>{r}</button>''' for i, r in enumerate(REASONS))
    return f'''<sc-if value="[[ reporting ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 30; background: rgba(11,15,14,.5); animation: fadeIn .2s ease-out both">
      <div role="dialog" aria-label="Report" style="position: absolute; left: 0; right: 0; bottom: 0; border-radius: {R_L}px {R_L}px 0 0; background: #FFFFFF; padding: 16px 20px 30px; display: flex; flex-direction: column; gap: 12px; animation: sheetUp .3s cubic-bezier(.2,.8,.2,1) both">
        <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 18px; font-weight: 600">[[ reportTitle ]]</span><button onClick="[[ closeReport ]]" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</button></div>
        <sc-if value="[[ notReported ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 12px">
          <span style="font-size: 14px; color: {SEC}">What's wrong with it?</span>
          <div role="radiogroup" aria-label="Reason">{radios}</div>
          <button onClick="[[ sendReport ]]" aria-disabled="[[ noReason ]]" style="height: 52px; width: 100%; border-radius: {R_M}px; background: [[ repBg ]]; color: [[ repFg ]]; font-size: 16px; font-weight: 600">Send report</button>
        </div></sc-if>
        <sc-if value="[[ reported ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding: 10px 0 6px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
          <span style="width: 56px; height: 56px; border-radius: 999px; background: {BLUSH}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 26, BLUSH_INK, 2.8)}</span>
          <span style="font-size: 18px; font-weight: 600">Thank you. It's with a person at AWO.</span>
          <span style="font-size: 15px; line-height: 1.45; color: {SEC}">They'll look at it within a day. Nobody is told who reported it.</span>
          <button onClick="[[ closeReport ]]" style="margin-top: 4px; height: 48px; padding: 0 24px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 15px; font-weight: 600">Done</button>
        </div></sc-if>
      </div>
    </div>
  </sc-if>'''


def report_js(titles):
    return '''    const RT = %s;
    const rp = st.rp == null ? -1 : st.rp, rr = st.rr == null ? -1 : st.rr, rdone = !!st.rdone;
    v.reporting = rp >= 0; v.reportTitle = rp >= 0 ? RT[rp] : ''; v.reported = rdone; v.notReported = !rdone;
    v.closeReport = () => this.setState({ rp: -1, rr: -1, rdone: false });
    v.noReason = rr < 0 ? 'true' : 'false'; v.repBg = rr < 0 ? '#DCE4DF' : '%s'; v.repFg = rr < 0 ? '%s' : '#FFFFFF';
    v.sendReport = () => { if (rr >= 0) this.setState({ rdone: true }); };
    for (let i = 0; i < %d; i++) { v['rr' + i] = rr === i; v['rPick' + i] = () => this.setState({ rr: i }); v['rDot' + i] = rr === i ? '%s' : 'transparent'; }
    for (let i = 0; i < RT.length; i++) v['rep' + i] = () => this.setState({ rp: i, rr: -1, rdone: false });''' % (json.dumps(titles), BLUSH_INK, MUTED, len(REASONS), BLUSH_INK)


# ---------------------------------------------------------------- the pieces of the feed

def milestone_post(k='m'):
    stones_svg = (f'<svg width="200" height="84" viewBox="0 0 200 84" aria-hidden="true" style="display: block; overflow: visible">'
                  f'<ellipse cx="36" cy="70" rx="28" ry="10" fill="{EVG_D}"></ellipse><ellipse cx="36" cy="66" rx="28" ry="10" fill="{LIME}"></ellipse>'
                  f'<ellipse cx="100" cy="50" rx="30" ry="11" fill="{EVG_D}"></ellipse><ellipse cx="100" cy="46" rx="30" ry="11" fill="{LIME}"></ellipse>'
                  f'<g class="drop8"><ellipse cx="164" cy="30" rx="28" ry="10" fill="{EVG_D}"></ellipse><ellipse cx="164" cy="26" rx="28" ry="10" fill="{LIME}"></ellipse></g>'
                  f'<ellipse class="rip8" cx="164" cy="28" rx="28" ry="10" fill="none" stroke="{LIME}" stroke-width="2"></ellipse></svg>')
    return f'''<article class="card8" style="gap: 14px">
      {author('thandi', 'Thandi', 'Safety net circle, 2 hours ago', kind_chip('Milestone', LIME, EVG), more_btn('rep0', 'More about this post'))}
      <div style="border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
        <div role="img" aria-label="A third stone lands: a goal reached" style="height: 84px">{stones_svg}</div>
        <span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">Thandi filled her safety net</span>
        <span style="display: flex; gap: 6px; flex-wrap: wrap"><span class="chip" style="background: {LIME}; color: {EVG}">Goal reached</span><span class="chip" style="background: rgba(255,255,255,.12); color: {ON_EVG}">{ic8('eye-off', 14)}Amount hidden</span></span>
      </div>
      <p class="hand" style="font-size: 26px; color: {BLUSH_INK}; {HF}">Full. Finally. Took me a year.</p>
      {reactions(k)}
    </article>'''


def note_post(k='n'):
    return f'''<article class="card8" style="gap: 12px">
      {author('adaeze', 'Adaeze', 'For you, 5 hours ago', kind_chip('Note'), more_btn('rep1', 'More about this post'))}
      <p style="font-size: 17px; line-height: 1.45">Six months of the pay-day plan. This is the first December I'm not borrowing for.</p>
      <img src="{IMG['adaeze']}" alt="Adaeze at home" style="width: 100%; height: 220px; object-fit: cover; object-position: 50% 30%; border-radius: {R_M}px; display: block">
      {reactions(k)}
    </article>'''


def shop_card(compact=False):
    thumbs = ''.join(crop(*box, 100, 96, R_M, alt=n) for n, _p, box, _d, _s in PRODUCTS)
    return f'''<article class="card8" style="gap: 12px">
      {author('wanjiru', "Wanjiru's Homeware", 'Member shop, Nairobi', kind_chip('Shop local', BLUSH, BLUSH_INK), '' if compact else more_btn('rep2', 'More about this shop'))}
      <div style="display: flex; gap: 8px; overflow: hidden">{thumbs}</div>
      <span style="font-size: 15px; line-height: 1.4; color: {SEC}">Handmade baskets, vases and carvings. Pick up at the stall, or delivery in Nairobi.</span>
      <a href="R8-Shop-Public.dc.html" style="height: 48px; border-radius: {R_M}px; background: {BLUSH_INK}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('shop', 18, '#FFFFFF')}See the shop</a>
      <span style="font-size: 12px; color: {MUTED}">Listed by a member. Orders go to her WhatsApp; AWO doesn't handle payments.</span>
    </article>'''


def letter_post(k='l'):
    more = ("<p style=\"font-size: 16px; line-height: 1.6; color: " + INK + "\">She kept the book in a biscuit tin and read it out at every meeting. Nobody could lie about a contribution, and nobody wanted to.</p>"
            "<p style=\"font-size: 16px; line-height: 1.6; color: " + INK + "\">What she got wrong was the cash. Twelve women's money sat in one tin for a month at a time. When the house was broken into in 2009, the tin went too. Now our stokvel keeps a bank account with two signatures, and I still keep a book.</p>")
    return f'''<article class="card8" style="gap: 12px">
      {author('lindiwe', 'Lindiwe', 'For you, yesterday', kind_chip('Letter', NIGHT, MOON), more_btn('rep3', 'More about this letter'))}
      <h2 class="d" style="font-size: 26px">What my mother taught me about stokvels, and what she got wrong</h2>
      <p style="font-size: 16px; line-height: 1.6; color: {INK}">My mother ran our street's stokvel for eleven years. She taught me that trust is written down: every rand, every month, in a book everyone could see.</p>
      <sc-if value="[[ letterOpen ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 12px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">{more}</div></sc-if>
      <button onClick="[[ toggleLetter ]]" aria-expanded="[[ letterOpen ]]" style="align-self: flex-start; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {MIST}; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 8px">[[ letterLabel ]]<span style="font-weight: 400; color: {MUTED}">Four minutes</span></button>
      {reactions(k)}
    </article>'''


def question_post():
    return f'''<article class="card8" style="gap: 12px">
      {author('zodwa', 'Zodwa', 'Stokvel treasurers, 3 hours ago', kind_chip('Question', POOL, EVG), more_btn('rep4', 'More about this question'))}
      <p style="font-size: 18px; font-weight: 600; line-height: 1.35">Our stokvel wants a bank account. What did your bank ask for?</p>
      <a href="R8-Post.dc.html" style="border-radius: {R_M}px; background: {MIST}; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start">
        <img class="face" src="{IMG['thandi']}" alt="" style="width: 28px; height: 28px"><span style="flex-grow: 1; font-size: 14px; line-height: 1.45; color: {SEC}"><b style="color: {INK}; font-weight: 600">Thandi:</b> Ours asked for our constitution, the minutes of the meeting that chose the signatories...</span></a>
      <a href="R8-Post.dc.html" style="height: 44px; display: flex; align-items: center; justify-content: space-between; font-size: 15px; font-weight: 600; color: {EVG}">Read all four replies{icon('chev', 18, EVG)}</a>
    </article>'''


def feed_tabs():
    btns = ''.join(f'<button role="tab" class="tabbtn" onClick="[[ tab{i} ]]" aria-selected="[[ tOn{i} ]]" style="position: relative; z-index: 1; flex: 1 1 0; height: 44px; font-size: 15px; font-weight: 600; color: [[ tFg{i} ]]">{n}</button>' for i, n in enumerate(['For you', 'Circles']))
    return (f'<div role="tablist" aria-label="Community" style="position: relative; display: flex; padding: 4px; border-radius: {R_M}px; background: #FFFFFF">'
            f'<span aria-hidden="true" style="position: absolute; top: 4px; bottom: 4px; left: [[ indL ]]px; right: [[ indR ]]px; border-radius: 8px; background: {BLUSH_INK}; '
            f'transition: left .34s cubic-bezier(.2,.8,.2,1) [[ dl ]]s, right .34s cubic-bezier(.2,.8,.2,1) [[ dr ]]s"></span>{btns}</div>')


CIRCLES = [(('thandi', 'grace', 'amara'), 'Safety net', '8 women', '2 new'), (('wanjiru', 'zodwa', 'lindiwe'), 'Side hustles', '24 women', ''),
           (('grace', 'thandi', 'lindiwe'), 'Stokvel treasurers', '12 women', '4 new')]


def circles_pane():
    def cluster(keys):
        faces = ''.join(f'<img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: {[34, 8, 58][j]}px; top: {[6, 34, 36][j]}px; width: {[40, 34, 34][j]}px; height: {[40, 34, 34][j]}px; box-shadow: 0 0 0 2px #FFFFFF">' for j, k in enumerate(keys))
        return (f'<span aria-hidden="true" style="position: relative; width: 104px; height: 76px; display: block"><span style="position: absolute; left: 2px; top: -6px; width: 88px; height: 88px; border-radius: 999px; border: 1.5px solid {BLUSH}"></span>'
                f'<span style="position: absolute; left: 14px; top: 6px; width: 64px; height: 64px; border-radius: 999px; border: 1.5px solid {BLUSH}"></span>{faces}</span>')
    cards = ''.join(f'''<a href="{"R8-Post.dc.html" if name == "Stokvel treasurers" else "R7-Buddy.dc.html" if name == "Safety net" else "R8-Feed.dc.html"}" style="position: relative; min-height: 150px; box-sizing: border-box; border-radius: {R_L}px; background: #FFFFFF; padding: 16px 14px 14px; display: flex; flex-direction: column; gap: 10px">
        {f'<span class="chip" style="position: absolute; right: 10px; top: 10px; height: 24px; padding: 0 8px; background: {BLUSH}; color: {BLUSH_INK}">{new}</span>' if new else ''}{cluster(keys)}
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{name}</span><span style="font-size: 13px; color: {MUTED}">{count}</span></span></a>''' for keys, name, count, new in CIRCLES)
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{cards}
        <button style="min-height: 150px; border-radius: {R_L}px; box-shadow: inset 0 0 0 1.5px #C9D3CE; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; font-size: 15px; font-weight: 600; color: {BLUSH_INK}"><span style="width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic8('plus', 22, BLUSH_INK)}</span>Find a circle</button></div>
      <span style="font-size: 17px; font-weight: 600; margin-top: 4px">Latest in your circles</span>
      {question_post()}
      {milestone_post('mc')}
    </div>'''


def feed():
    faces = ''.join(f'<img class="face" src="{IMG[k]}" alt="" style="width: 24px; height: 24px; margin-left: {0 if j == 0 else -7}px; box-shadow: 0 0 0 2px {BLUSH}">' for j, k in enumerate(('wanjiru', 'grace', 'amara')))
    for_you = f'''<div class="pane" style="display: flex; flex-direction: column; gap: 14px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <section style="border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 16px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; justify-content: space-between; align-items: center"><span class="lbl" style="color: {BLUSH_2}">This week's question, pinned</span>{icon('ripple', 20, BLUSH_INK)}</div>
        <span class="d" style="font-size: 28px">What did you say no to this week?</span>
        <sc-if value="[[ answered ]]" hint-placeholder-val="[[ false ]]"><div style="align-self: flex-end; max-width: 280px; padding: 10px 14px; border-radius: {R_L}px {R_S}px {R_L}px {R_L}px; background: {BLUSH_INK}; color: {BLUSH}; font-size: 15px; line-height: 1.4; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both">[[ answer ]]</div></sc-if>
        <sc-if value="[[ notAnswered ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; gap: 8px">
          <label for="f-ans" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your answer</label>
          <input id="f-ans" value="[[ answer ]]" onInput="[[ typeAns ]]" placeholder="Share yours" style="flex-grow: 1; min-width: 0; height: 44px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 15px; color: {INK}">
          <button onClick="[[ postAns ]]" aria-label="Share your answer" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</button></div></sc-if>
        <span style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="display: flex">{faces}</span><span style="font-size: 13px; color: {BLUSH_2}">[[ ansCount ]]</span></span>
      </section>
      {milestone_post()}
      {note_post()}
      {shop_card()}
      {letter_post()}
      {question_post()}
      <a href="R8-Podcast.dc.html" style="border-radius: {R_L}px; background: {NIGHT}; color: {MOON}; padding: 14px; display: flex; align-items: center; gap: 12px">
        <img src="{IMG['amara_coat']}" alt="" style="width: 56px; height: 56px; border-radius: {R_M}px; object-fit: cover; object-position: 50% 20%">
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {MINT}">From Learn: the AWO Podcast</span><span style="font-size: 15px; font-weight: 600; line-height: 1.3">Closing a shop, and opening a better one</span></span>
        <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('play', 18, INK)}</span></a>
      <p style="font-size: 13px; line-height: 1.5; color: {MUTED}; text-align: center; padding: 4px 12px">{RULES_LINE}</p>
    </div>'''
    body = f'''  <div class="scr" style="gap: 14px">
    <header style="display: flex; align-items: center; gap: 10px">
      <h1 class="d" style="font-size: 44px; flex-grow: 1">Community</h1>
      <a href="R8-Compose.dc.html" aria-label="New post" style="width: 48px; height: 48px; border-radius: {R_M}px; background: {BLUSH_INK}; color: {BLUSH}; display: flex; align-items: center; justify-content: center">{ic8('plus', 24, BLUSH, 2.4)}</a>
      <a href="R7-Buddy.dc.html" aria-label="Your buddy, Wanjiru" style="position: relative; width: 48px; height: 48px; flex-shrink: 0"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid #F29BB5"></span><img class="face" src="{IMG['wanjiru']}" alt="" style="position: absolute; left: 5px; top: 5px; width: 38px; height: 38px"></a>
    </header>
    {feed_tabs()}
    <sc-if value="[[ p0 ]]" hint-placeholder-val="[[ true ]]">{for_you}</sc-if>
    <sc-if value="[[ p1 ]]" hint-placeholder-val="[[ false ]]">{circles_pane()}</sc-if>
  </div>
  {tabbar8('Community')}
  {report_sheet()}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
    const t = st.t == null ? 0 : st.t, from = st.from == null ? t : st.from;
    const dir = t > from ? 1 : (t < from ? -1 : 0);
    v.indL = 4 + t * 171; v.indR = 346 - 171 * (t + 1); v.dl = dir > 0 ? .08 : 0; v.dr = dir < 0 ? .08 : 0;
    v.paneAnim = dir > 0 ? 'inR' : (dir < 0 ? 'inL' : 'fadeIn');
    for (let i = 0; i < 2; i++) { v['tab' + i] = () => { if (i !== t) this.setState({ from: t, t: i }); }; v['tOn' + i] = t === i; v['p' + i] = t === i; v['tFg' + i] = t === i ? '#FFFFFF' : '%(muted)s'; }
    const answered = !!st.answered, answer = st.answer == null ? 'A second takeaway on Friday. Cooked instead.' : st.answer;
    v.answered = answered; v.notAnswered = !answered; v.answer = answer; v.typeAns = (e) => this.setState({ answer: e.target.value });
    v.postAns = () => { if (answer.trim()) this.setState({ answered: true }); };
    v.ansCount = answered ? 'You and 38 women answered' : '38 women answered';
    const lo = !!st.lo; v.letterOpen = lo; v.toggleLetter = () => this.setState({ lo: !lo }); v.letterLabel = lo ? 'Show less' : 'Read the letter';
%(rx)s
%(rep)s
    return v;
  }
}''' % dict(muted=MUTED, rx=reactions_js(['m', 'n', 'l', 'mc']), rep=report_js(['Report this milestone', 'Report this note', 'Report this shop', 'Report this letter', 'Report this question']))
    return with_css(phone('Community', body, logic, h=3000), PHONE_CSS + HUB_CSS + STORY_CSS + FEED_CSS + TOOL_CSS8)


TOOL_CSS8 = '.card8{border-radius:14px;background:#FFFFFF;padding:16px;display:flex;flex-direction:column;gap:12px}'


# ---------------------------------------------------------------- the composer

KINDS = [('Note', 'note', 'Short, with a photo if you like'), ('Letter', 'letter', 'Long, with a title'), ('Milestone', 'stones', 'From a tool; amounts hidden'), ('Question', 'question', 'To one circle')]
MILESTONES = [('down', 'Paid off the clothing account', 'Debt payoff'), ('calc', 'Planned my first pay-day', 'Pay-day plan'), ('doc', 'Read my payslip, line by line', 'Payslip decoder')]
TO = ['For you', 'Safety net', 'Side hustles']
RISKY = 'Join my savings group: 30% a month, guaranteed. DM me before Friday.'


def compose():
    kinds = ''.join(f'''<button role="radio" aria-checked="[[ kOn{i} ]]" onClick="[[ k{i} ]]" style="min-height: 84px; border-radius: {R_L}px; background: [[ kBg{i} ]]; color: [[ kFg{i} ]]; box-shadow: inset 0 0 0 [[ kBw{i} ]]px {BLUSH_INK}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s">{ic8(g, 22)}{n}</button>''' for i, (n, g, _d) in enumerate(KINDS))
    to = ''.join(f'<button role="radio" aria-checked="[[ toOn{i} ]]" onClick="[[ to{i} ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ toBg{i} ]]; color: [[ toFg{i} ]]; box-shadow: inset 0 0 0 1px [[ toBd{i} ]]; font-size: 14px; font-weight: 600">{n}</button>' for i, n in enumerate(TO))
    ms = ''.join(f'''<button role="radio" aria-checked="[[ msOn{i} ]]" onClick="[[ ms{i} ]]" style="width: 100%; min-height: 64px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ msBw{i} ]]px {EVG}; padding: 0 14px; display: flex; align-items: center; gap: 12px; text-align: left">
          <span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span>
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MUTED}">From {src}</span></span></button>''' for i, (g, t, src) in enumerate(MILESTONES))
    field = f'width: 100%; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 14px; font: inherit; font-size: 16px; line-height: 1.5; color: {INK}; resize: none'
    body = f'''  <div class="scr" style="bottom: 0; gap: 16px">
    <header style="display: flex; align-items: center; gap: 10px">
      <a href="R8-Feed.dc.html" aria-label="Close" style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</a>
      <span style="flex-grow: 1; font-size: 17px; font-weight: 600">New post</span>
      <button onClick="[[ post ]]" aria-disabled="[[ cantPost ]]" style="height: 44px; padding: 0 18px; border-radius: {R_M}px; background: [[ postBg ]]; color: [[ postFg ]]; font-size: 15px; font-weight: 600">[[ postLabel ]]</button>
    </header>
    <div role="radiogroup" aria-label="What kind of post" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px">{kinds}</div>
    <span style="font-size: 14px; color: {SEC}; margin-top: -6px">[[ kindNote ]]</span>
    <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; font-weight: 600; color: {MUTED}">[[ toLabel ]]</span><div role="radiogroup" aria-label="Where it goes" style="display: flex; gap: 8px; flex-wrap: wrap">{to}</div></div>
    <sc-if value="[[ isNote ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <label for="c-note" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your note</label>
      <textarea id="c-note" rows="5" value="[[ text ]]" onInput="[[ type ]]" placeholder="What's on your mind about money?" style="{field}"></textarea>
      <span style="display: flex; justify-content: space-between; align-items: center"><button style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{ic8('image', 18, EVG)}Add a photo</button><span style="font-size: 13px; color: {MUTED}">[[ count ]] of 500</span></span>
    </div></sc-if>
    <sc-if value="[[ isLetter ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <label for="c-title" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Title</label>
      <input id="c-title" placeholder="A title" value="[[ title ]]" onInput="[[ typeTitle ]]" style="height: 56px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 20px; font-weight: 600; color: {INK}">
      <textarea rows="8" aria-label="Your letter" value="[[ text ]]" onInput="[[ type ]]" placeholder="Tell it at your own pace." style="{field}"></textarea>
      <span style="font-size: 13px; color: {MUTED}">Letters of 300 words or more show a reading time.</span>
    </div></sc-if>
    <sc-if value="[[ isMilestone ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <span style="font-size: 14px; color: {SEC}">Milestones come from what you did in AWO, so they're real.</span>
      <div role="radiogroup" aria-label="Your milestones" style="display: flex; flex-direction: column; gap: 8px">{ms}</div>
      <div style="min-height: 60px; border-radius: {R_M}px; background: #FFFFFF; padding: 0 4px 0 14px; display: flex; align-items: center; gap: 10px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Show the amount</span><span style="font-size: 13px; color: {MUTED}">Off unless you choose it</span></span>{switch(0, 'Show the amount')}</div>
      <input aria-label="In your own words" placeholder="In your own words (optional)" value="[[ text ]]" onInput="[[ type ]]" style="height: 56px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 16px; color: {INK}">
    </div></sc-if>
    <sc-if value="[[ isQuestion ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <textarea rows="4" aria-label="Your question" value="[[ text ]]" onInput="[[ type ]]" placeholder="Ask your circle" style="{field}"></textarea>
      <div style="min-height: 60px; border-radius: {R_M}px; background: #FFFFFF; padding: 0 4px 0 14px; display: flex; align-items: center; gap: 10px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Ask without my name</span><span style="font-size: 13px; color: {MUTED}">Shown as "A member of this circle"</span></span>{switch(1, 'Ask without my name')}</div>
    </div></sc-if>
    <sc-if value="[[ flagged ]]" hint-placeholder-val="[[ false ]]"><section style="border-radius: {R_L}px; background: {WARN_BG}; color: {WARN_FG}; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
      <span style="display: flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 600">{ALERT}This may break a Community rule<span class="chip" style="border: 1px dashed {WARN_FG}; color: {WARN_FG}">AI-assisted check</span></span>
      <span style="font-size: 14px; line-height: 1.45">It looks like it promises returns or asks people to join something. Edit it, or send it to a person at AWO, who'll check it before anyone sees it.</span>
    </section></sc-if>
    <button onClick="[[ tryRisky ]]" style="align-self: flex-start; min-height: 44px; font-size: 14px; font-weight: 600; color: {BLUSH_INK}; text-decoration: underline; text-underline-offset: 3px">See what the AI check does</button>
    <p style="font-size: 13px; line-height: 1.5; color: {MUTED}">{RULES_LINE}</p>
  </div>
  <sc-if value="[[ posted ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 20; background: {MIST}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; padding: 32px; text-align: center; animation: fadeIn .25s ease-out both">
      <span style="position: relative; width: 72px; height: 72px; border-radius: 999px; background: {BLUSH}; display: flex; align-items: center; justify-content: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span>{icon('check', 34, BLUSH_INK, 2.8)}</span>
      <span class="d" style="font-size: 32px">[[ doneTitle ]]</span>
      <span style="font-size: 16px; line-height: 1.45; color: {SEC}">[[ doneText ]]</span>
      <a href="R8-Feed.dc.html" style="margin-top: 8px; height: 52px; padding: 0 22px; border-radius: {R_M}px; background: {BLUSH_INK}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center">See the feed</a>
      <button onClick="[[ again ]]" style="min-height: 44px; font-size: 14px; font-weight: 600; color: {BLUSH_INK}">Write another</button>
    </div>
  </sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const K = %(kinds)s, TO = %(to)s, RISKY = %(risky)s;
    const k = st.k == null ? 0 : st.k, to = st.to == null ? (k === 3 ? 2 : 0) : st.to, ms = st.ms == null ? -1 : st.ms;
    const text = st.text == null ? 'Six months of the pay-day plan. This is the first December I\\'m not borrowing for.' : st.text;
    const title = st.title || '';
    const flagged = k !== 2 && /guarant|double your|join my|dm me|%% a (week|month|day)|signals|recruit/i.test(text + ' ' + title);
    const ok = k === 2 ? ms >= 0 : (k === 1 ? title.trim().length > 0 && text.trim().length > 0 : text.trim().length > 0);
    const v = {
      text, title, type: (e) => this.setState({ text: e.target.value }), typeTitle: (e) => this.setState({ title: e.target.value }),
      count: text.length, isNote: k === 0, isLetter: k === 1, isMilestone: k === 2, isQuestion: k === 3,
      kindNote: K[k][2], toLabel: k === 3 ? 'Which circle' : 'Posting to', flagged,
      cantPost: ok ? 'false' : 'true', postBg: ok ? '%(bi)s' : '#DCE4DF', postFg: ok ? '#FFFFFF' : '%(muted)s',
      postLabel: flagged ? 'Send for a check' : 'Post',
      post: () => { if (ok) this.setState({ posted: true, held: flagged }); },
      posted: !!st.posted, doneTitle: st.held ? 'Sent for a check' : 'Posted',
      doneText: st.held ? 'A person at AWO will read it before anyone sees it, usually within a day. You\\'ll hear what they decide, and why.' : 'It\\'s in ' + (to === 0 ? 'For you' : TO[to]) + ' now. Amounts stay hidden unless you chose to show them.',
      again: () => this.setState({ posted: false, held: false, text: '', title: '', ms: -1 }),
      tryRisky: () => this.setState({ k: 0, text: RISKY })
    };
    for (let i = 0; i < 4; i++) {
      v['k' + i] = () => this.setState({ k: i, to: null, text: i === 0 ? text : '', title: '' }); v['kOn' + i] = k === i;
      v['kBg' + i] = k === i ? '%(blush)s' : '#FFFFFF'; v['kFg' + i] = k === i ? '%(bi)s' : '%(ink)s'; v['kBw' + i] = k === i ? 2 : 0;
    }
    for (let i = 0; i < 3; i++) {
      const on = to === i, dis = k === 3 && i === 0;
      v['to' + i] = () => { if (!dis) this.setState({ to: i }); }; v['toOn' + i] = on;
      v['toBg' + i] = on ? '%(bi)s' : (dis ? '%(mist)s' : '#FFFFFF'); v['toFg' + i] = on ? '#FFFFFF' : (dis ? '%(muted)s' : '%(ink)s'); v['toBd' + i] = on ? '%(bi)s' : '#C9D3CE';
      v['ms' + i] = () => this.setState({ ms: i }); v['msOn' + i] = ms === i; v['msBw' + i] = ms === i ? 2 : 0;
    }
%(sw)s
    return v;
  }
}''' % dict(kinds=json.dumps(KINDS), to=json.dumps(TO), risky=json.dumps(RISKY), bi=BLUSH_INK, blush=BLUSH, muted=MUTED, ink=INK, mist=MIST, sw=switch_js(2, [False, False]))
    return with_css(phone('New post', body, logic, h=1160), PHONE_CSS + HUB_CSS + FEED_CSS)


# ---------------------------------------------------------------- a question, with replies

REPLIES = [('thandi', 'Thandi', '2 hours ago', 'Ours asked for our constitution, the minutes of the meeting that chose the signatories, and ID for the three of us.'),
           ('grace', 'Grace', '2 hours ago', 'Ask for a group or society account. Each bank calls it something different, so the words on its website may not match.'),
           (None, None, None, None),
           ('lindiwe', 'Lindiwe', '1 hour ago', 'Make two signatures a rule for every withdrawal. It protects the treasurer as much as the money.')]


def post():
    reps = ''
    j = 0
    for i, (face, name, when, text) in enumerate(REPLIES):
        if face is None:
            reps += f'''<div style="border-radius: {R_M}px; background: {MIST}; box-shadow: inset 0 0 0 1px #DCE4DF; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start; font-size: 14px; line-height: 1.45; color: {SEC}">
          {ic8('eye-off', 18, MUTED)}<span>A reply is hidden while a person at AWO checks it. <span class="chip" style="height: 22px; padding: 0 6px; border: 1px dashed {MUTED}; color: {MUTED}">AI-flagged</span> It mentioned guaranteed returns.</span></div>'''
            continue
        reps += f'''<article style="display: flex; gap: 10px; align-items: flex-start">
          <img class="face" src="{IMG[face]}" alt="" style="width: 36px; height: 36px; margin-top: 4px">
          <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px">
            <div style="border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: #FFFFFF; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px">
              <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 14px; font-weight: 600">{name} <span style="font-weight: 400; color: {MUTED}">{when}</span></span>{more_btn(f'rep{j + 1}', f'More about {name} reply')}</span>
              <span style="font-size: 15px; line-height: 1.5">{text}</span>
            </div>
            <span style="display: flex; gap: 6px"><button onClick="[[ tm{j} ]]" aria-pressed="[[ tmOn{j} ]]" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: [[ tmBg{j} ]]; color: [[ tmFg{j} ]]; display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600">{moon(14, 'half', lit='currentColor', dark=MIST)}Taught me</button><button onClick="[[ replyTo{j} ]]" style="height: 44px; padding: 0 12px; font-size: 13px; font-weight: 600; color: {SEC}">Reply</button></span>
          </div></article>'''
        j += 1
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: center; gap: 10px">
      <a href="R8-Feed.dc.html" aria-label="Back to the feed" style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('back', 20, INK, 2.2)}</a>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 13px; color: {MUTED}">A circle of 12 women</span><span style="font-size: 17px; font-weight: 600">Stokvel treasurers</span></span>
      {more_btn('rep0', 'More about this question')}
    </header>
    <article class="card8" style="gap: 12px">
      {author('zodwa', 'Zodwa', 'Soweto, 3 hours ago', kind_chip('Question', POOL, EVG))}
      <p style="font-size: 21px; font-weight: 600; line-height: 1.3; letter-spacing: -0.01em">Our stokvel wants a bank account. What did your bank ask for?</p>
      {reactions('q')}
    </article>
    <div style="display: flex; gap: 8px; flex-wrap: wrap">
      <a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{icon('arch', 16, LIME)}Words: stokvel constitution</a>
      <a href="R8-Learn.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{moon(16, 'half')}Learn: saving together</a>
    </div>
    <span style="font-size: 17px; font-weight: 600">Four replies</span>
    <div style="display: flex; flex-direction: column; gap: 14px">{reps}
      <sc-if value="[[ replied ]]" hint-placeholder-val="[[ false ]]"><article style="display: flex; gap: 10px; align-items: flex-start; animation: rise .35s cubic-bezier(.2,.8,.2,1) both"><img class="face" src="{IMG['naledi']}" alt="" style="width: 36px; height: 36px; margin-top: 4px"><div style="flex-grow: 1; border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 14px; font-weight: 600">You <span style="font-weight: 400">just now</span></span><span style="font-size: 15px; line-height: 1.5">[[ sentText ]]</span></div></article></sc-if>
    </div>
    <div style="display: flex; gap: 8px; align-items: center; margin-top: 4px">
      <label for="p-reply" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your reply</label>
      <input id="p-reply" value="[[ reply ]]" onInput="[[ typeReply ]]" placeholder="[[ replyPh ]]" style="flex-grow: 1; min-width: 0; height: 52px; box-sizing: border-box; border: 0; border-radius: {R_M}px; background: #FFFFFF; padding: 0 14px; font-size: 15px; color: {INK}">
      <button onClick="[[ sendReply ]]" aria-label="Send reply" style="width: 52px; height: 52px; border-radius: {R_M}px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 20, BLUSH)}</button>
    </div>
    <p style="font-size: 13px; line-height: 1.5; color: {MUTED}">{RULES_LINE} Replies share experience, not advice about which bank to choose.</p>
  </div>
  {tabbar8('Community')}
  {report_sheet()}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
    const N = %(names)s;
    const reply = st.reply == null ? '' : st.reply, sent = st.sent || '', to = st.rto == null ? 'Zodwa' : st.rto;
    v.reply = reply; v.replied = !!sent; v.sentText = sent; v.typeReply = (e) => this.setState({ reply: e.target.value });
    v.replyPh = 'Reply to ' + to; v.sendReply = () => { if (reply.trim()) this.setState({ sent: reply, reply: '' }); };
    for (let j = 0; j < 3; j++) {
      const on = !!(st.tm || {})[j];
      v['tm' + j] = () => this.setState({ tm: Object.assign({}, st.tm || {}, { [j]: !on }) }); v['tmOn' + j] = on;
      v['tmBg' + j] = on ? '%(blush)s' : '#FFFFFF'; v['tmFg' + j] = on ? '%(bi)s' : '%(ink)s';
      v['replyTo' + j] = () => this.setState({ rto: N[j] });
    }
%(rx)s
%(rep)s
    return v;
  }
}''' % dict(names=json.dumps([r[1] for r in REPLIES if r[0]]), blush=BLUSH, bi=BLUSH_INK, ink=INK, rx=reactions_js(['q']),
            rep=report_js(['Report this question', "Report Thandi's reply", "Report Grace's reply", "Report Lindiwe's reply"]))
    return with_css(phone('A question, with replies', body, logic, h=1560), PHONE_CSS + HUB_CSS + STORY_CSS + FEED_CSS + TOOL_CSS8)


# ---------------------------------------------------------------- the parts of the feed

def parts():
    kinds = [
        ('Note', 'Short: up to 500 characters, and a photo if she likes. The everyday post.', note_post('pn')),
        ('Letter', 'Long, with a title and a reading time. It opens in place, like a newsletter.', letter_post('pl')),
        ('Milestone', 'Made from something she did in AWO, so it is real. Amounts are hidden unless she shows them. The stone lands once.', milestone_post('pm')),
        ('Question', 'Asked to one circle, with or without her name. Replies share experience, not advice.', question_post()),
        ('Shop local', 'From her Shop. Orders go to her WhatsApp; AWO takes no payment.', shop_card(compact=True)),
    ]
    cols = ''.join(f'<div style="display: flex; flex-direction: column; gap: 14px"><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em">{t}</span><span class="knote">{d}</span></span><div style="background: {MIST}; border-radius: {R_L}px; padding: 10px">{card}</div></div>' for t, d, card in kinds)
    rx = ''.join(f'<div style="display: flex; gap: 12px; align-items: flex-start"><span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {BLUSH}; color: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{g}</span><span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 16px; font-weight: 600">{n}</span><span class="knote">{d}</span></span></div>'
                 for n, g, d in [('Cheer', ic8('heart', 20), 'For a win, big or small.'), ('Same here', ic8('people', 20), "For \"that's me too\": a mistake, a worry, a month."), ('Taught me', moon(20, 'half', lit=BLUSH_INK, dark=BLUSH), 'For a post that taught her something. It helps others find useful posts.')])
    never = ''.join(f'<span style="display: flex; gap: 10px; font-size: 15px; line-height: 1.45"><span aria-hidden="true" style="width: 6px; height: 6px; flex-shrink: 0; margin-top: 8px; border-radius: 999px; background: {BLUSH_INK}"></span>{t}</span>' for t in
                    ['Follower counts, or who follows whom', 'Public reaction totals: only the author sees hers', 'Trending, or "most popular"', 'Amounts she did not choose to show', 'Surnames, employers or neighbourhoods by default'])
    flow = ''.join(f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 6px; text-align: center; align-items: center"><span style="width: 44px; height: 44px; border-radius: 999px; background: {bg}; color: {fg}; box-shadow: inset 0 0 0 2px {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span><span style="font-size: 14px; font-weight: 600; line-height: 1.3">{t}</span><span style="font-size: 13px; color: {MUTED}; line-height: 1.35">{d}</span></div>'
                   for g, t, d, bg, fg in [('flag', 'AI flags it, or a member reports it', 'With the reason', '#FFFFFF', BLUSH_INK), ('eye-off', 'Held, not deleted', 'Shown as hidden', '#FFFFFF', BLUSH_INK), ('people', 'A person decides', 'Keep, hide or remove', BLUSH, BLUSH_INK), ('letter', 'The author hears why', 'And can ask again', '#FFFFFF', BLUSH_INK)])
    body = f'''<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px; align-items: start">{cols}</div>
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1.4fr); gap: 24px; align-items: start">
      <section class="card" style="gap: 16px"><span class="ktitle">Three reactions, not likes</span>{rx}</section>
      <section class="card" style="gap: 12px"><span class="ktitle">What the feed never shows</span>{never}</section>
      <section class="card" style="gap: 18px"><span class="ktitle">AI flags; people decide</span><div style="position: relative; display: flex; gap: 8px"><span aria-hidden="true" style="position: absolute; left: 12%; right: 12%; top: 21px; height: 2px; background: {BLUSH_INK}"></span>{flow}</div>
        <span class="knote">Reasons a member can report: advice to buy, sell or switch; recruiting, or a scheme that promises returns; unkind or unsafe; someone's private information; something else. The same queue feeds AWO Admin's moderation screen (Round 7).</span></section>
    </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%(rx)s
    const lo = !!st.lo; v.letterOpen = lo; v.toggleLetter = () => this.setState({ lo: !lo }); v.letterLabel = lo ? 'Show less' : 'Read the letter';
    for (let i = 0; i < 6; i++) v['rep' + i] = () => {};
    return v;
  }
}''' % dict(rx=reactions_js(['pn', 'pl', 'pm']))
    desc = ('Community becomes a feed to read and post in, unique to AWO: five kinds of post, three reactions instead of likes, no counts '
            'to chase, and people, not AI, deciding what stays.')
    return with_css(board7('The feed, in parts', desc, body, logic, 2000, 1130), PHONE_CSS + STORY_CSS + FEED_CSS + TOOL_CSS8)


BOARDS = [('R8-Feed', feed), ('R8-Compose', compose), ('R8-Post', post), ('R8-Feed-Parts', parts)]
