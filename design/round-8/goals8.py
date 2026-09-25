"""Round 8, batch 3: goals of every kind (D-038), and Home with several goals. Writes R8-Goals and R8-Home.

AWO holds no money: a goal is a pool she fills herself, and AWO never picks a product for it."""
import os
import re
import sys

from lib8 import *  # noqa: F401,F403
from tools8 import tool_page, beat, foot, fmt_r, rands_js, TOOL_CSS  # noqa: F401
from hub8 import mini_pool
from learn8 import PHONE_CSS

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
sys.path.insert(0, os.path.join(HERE, '..', 'round-7'))

MINE = [('Safety net', 1800, 5000, 'pool'), ('Moving out', 1900, 16200, 'key'), ('A trip home', 2600, 6500, 'plane')]
TEMPLATES = [('A car', 'car'), ('Moving out', 'key'), ('Start investing', 'grow'), ('School fees', 'school'),
             ('A trip home', 'plane'), ('A home deposit', 'home'), ('Business stock', 'shop'), ('A safety net', 'pool')]
# per template: goal amount, months to it, what the goal is, the lesson, the words
SETUP = {
    0: (22000, 15, 'Save the deposit', 'Buying a car without regret', ['Deposit', 'Balloon payment', 'Interest']),
    1: (16200, 9, 'Save the first month', 'Your first place', ['Deposit', 'Lease']),
    2: (1500, 3, 'A first R 1 500 to invest', 'Shares and dividends', ['ETF', 'Fees', 'Compound interest']),
    3: (9000, 4, 'January school fees', 'Planning for January', ['Sinking fund']),
    4: (6500, 8, 'The bus and gifts, for December', 'Sending money home', ['Exchange rate']),
    5: (60000, 36, 'A 10% deposit', 'Your first home', ['Bond', 'Transfer costs']),
    6: (20000, 6, 'Stock for the busy season', 'Knowing your numbers', ['Cash flow', 'Float']),
    7: (5000, 10, 'Three weeks of needs, for surprises', 'Ready for surprises', ['Safety net']),
}


def rows(items, total_label, total):
    out = ''.join(f'<div style="min-height: 44px; display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 15px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span>{n}</span><span style="font-weight: 600; font-variant-numeric: tabular-nums">{v}</span></div>' for i, (n, v) in enumerate(items))
    return out + f'<div style="min-height: 48px; display: flex; align-items: center; justify-content: space-between; border-top: 2px solid {INK}; font-size: 16px; font-weight: 600"><span>{total_label}</span><span>{total}</span></div>'


def reality(k):
    if k == 0:
        return f'''<span style="font-size: 16px; font-weight: 600">The real cost of a R 220 000 car</span>
        <div>{rows([('Deposit, 10%', fmt_r(22000, False)), ('Licence and registration', fmt_r(1600, False))], 'Before you drive', fmt_r(23600, False))}</div>
        <div>{rows([('Instalment, over six years', fmt_r(4300, False)), ('Insurance', fmt_r(1100, False)), ('Fuel', fmt_r(1800, False)), ('Services and tyres', fmt_r(400, False))], 'Every month', fmt_r(7600, False))}</div>
        <div style="border-radius: {R_M}px; background: {WARN_BG}; color: {WARN_FG}; padding: 12px 14px; display: flex; gap: 10px; font-size: 14px; line-height: 1.45">{ALERT}<span>A balloon payment makes the instalment smaller, and leaves a big bill at the end. With a 30% balloon, R 66 000 is due in the last month.</span></div>'''
    if k == 1:
        first = rows([("Deposit, one month's rent", fmt_r(4500, False)), ("First month's rent", fmt_r(4500, False)), ('A bakkie and two friends', fmt_r(1200, False)), ('Bed, stove and pots', fmt_r(6000, False))], 'The first month', fmt_r(16200, False))
        return f'''<span style="font-size: 16px; font-weight: 600">What moving out costs, before the first night</span>
        <div>{first}</div>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}">After that, about R 8 900 a month, from your pay-day plan.</span>'''
    if k == 2:
        checks = [('A safety net for surprises', 'Yours is 36% full', 36), ('No expensive debt', 'R 26 600 left, in three debts', 0), ("Money you won't need for five years", 'Your call', 100)]
        items = ''.join(f'<div style="min-height: 56px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span role="img" aria-label="{p}%" style="position: relative; width: 36px; height: 36px; flex-shrink: 0">{arc(36, max(p, 1), "#DCE4DF", EVG, sw=5)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MUTED}">{d}</span></span></div>' for i, (t, d, p) in enumerate(checks))
        return f'''<span style="font-size: 16px; font-weight: 600">Before you start</span>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}">Many people check three things first. This is from your own numbers, not advice.</span>
        <div>{items}</div>
        <a href="R8-Tool-Fees.dc.html" style="min-height: 52px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; padding: 0 14px; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600">{hub_icon(None, 20, EVG)}<span style="flex-grow: 1">Fee eater: what fees would cost</span>{icon('chev', 16, EVG)}</a>
        <span style="font-size: 13px; color: {MUTED}">AWO never picks a fund, a share or a platform for you.</span>'''
    return f'<span style="font-size: 15px; line-height: 1.45; color: {SEC}">Set the amount and the date. AWO works out each month, and shows the pool on Home.</span>'


def goals():
    mine = ''.join(f'''<a href="R8-Home.dc.html" style="flex: 1 1 0; border-radius: {R_L}px; background: #FFFFFF; padding: 12px 8px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
        {mini_pool(round(have / want * 100), f"g{i}", i)}<span style="font-size: 14px; font-weight: 600; line-height: 1.2">{n}</span><span style="font-size: 12px; color: {MUTED}">{fmt_r(have, False)} of {fmt_r(want, False)}</span></a>''' for i, (n, have, want, _g) in enumerate(MINE))
    new_pool = f'''<sc-if value="[[ made ]]" hint-placeholder-val="[[ false ]]"><span style="flex: 1 1 0; border-radius: {R_L}px; background: {LIME}; padding: 12px 8px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; animation: pop .6s cubic-bezier(.34,1.56,.64,1) both">
        {mini_pool(2, 'gnew', 0)}<span style="font-size: 14px; font-weight: 600; line-height: 1.2; color: {EVG}">[[ madeName ]]</span><span style="font-size: 12px; color: {EVG}">New</span></span></sc-if>'''
    tiles = ''.join(f'<button onClick="[[ tp{i} ]]" aria-pressed="[[ tpOn{i} ]]" style="min-height: 84px; border-radius: {R_L}px; background: [[ tpBg{i} ]]; color: [[ tpFg{i} ]]; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; font-size: 13px; font-weight: 600; line-height: 1.2; text-align: center; padding: 8px 4px; transition: background-color .18s">{ic8(g, 24)}{n}</button>' for i, (n, g) in enumerate(TEMPLATES))
    panels = ''
    for k in range(8):
        amt, months, what, lesson, words = SETUP[k]
        chips = ''.join(f'<a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {MIST}; display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600">{icon("arch", 16, EVG)}{w}</a>' for w in words)
        panels += f'''<sc-if value="[[ tpOn{k} ]]" hint-placeholder-val="[[ {"true" if k == 0 else "false"} ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
      <section class="card8">{reality(k)}</section>
      {beat("Your goal", "pool")}
      <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 10px">
        <span style="font-size: 14px; font-weight: 600">{what}: {fmt_r(amt, False)}</span>
        <span class="d" style="font-size: 52px">[[ monthly ]]</span>
        <span style="font-size: 16px; color: {INK}">a month, to reach it by [[ byDate ]]</span>
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; border-top: 1px solid rgba(15,74,54,.2); padding-top: 10px"><span style="font-size: 15px; font-weight: 600">By when</span>
          <span style="display: flex; align-items: center; gap: 6px"><button onClick="[[ sooner ]]" aria-label="Sooner" style="width: 44px; height: 44px; border-radius: {R_M}px; background: rgba(255,255,255,.6); font-size: 22px">−</button><span style="min-width: 88px; text-align: center; font-size: 16px; font-weight: 600">[[ byDate ]]</span><button onClick="[[ later ]]" aria-label="Later" style="width: 44px; height: 44px; border-radius: {R_M}px; background: rgba(255,255,255,.6); font-size: 22px">+</button></span></div>
      </section>
      <sc-if value="[[ notMade ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ make ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600">Make it a goal</button></sc-if>
      <sc-if value="[[ made ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="flex-direction: row; gap: 12px; align-items: center; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 20, EVG, 2.8)}</span><span style="font-size: 15px; line-height: 1.4">On Home now, as its own pool. You move the money yourself and tap to top it up.</span></section></sc-if>
      {beat("Learn this", "moon")}
      <section class="card8"><a href="R7-Lesson.dc.html" style="min-height: 56px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; padding: 0 14px; display: flex; align-items: center; gap: 12px">{moon(24, 'half', now=True)}<span style="flex-grow: 1; font-size: 15px; font-weight: 600">{lesson}</span>{icon('play', 16, LIME)}</a><div style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div></section>
    </div></sc-if>'''
    body = f'''    <h1 class="d" style="font-size: 40px; margin-top: 4px">Goals of every kind</h1>
    <span style="font-size: 17px; font-weight: 600">Your goals</span>
    <div style="display: flex; gap: 8px; margin-top: -8px">{mine}{new_pool}</div>
    <span style="font-size: 17px; font-weight: 600; margin-top: 4px">Start a goal</span>
    <div role="group" aria-label="Goal templates" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin-top: -8px">{tiles}</div>
    {panels}
    {foot("Goals studio, version 0.1. Costs are samples for Johannesburg in 2026. AWO holds no money and never picks a car, a loan, a fund or an account for a goal.")}'''
    names = [n for n, _g in TEMPLATES]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const S = %(setup)s, N = %(names)s;
    const tp = st.tp == null ? 0 : st.tp;
    const months = st.mo == null ? S[tp][1] : st.mo;
    const M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const t = 8 + months;
    const v = {
      monthly: R(Math.ceil(S[tp][0] / months / 10) * 10), byDate: M[t %% 12] + ' ' + (2026 + Math.floor(t / 12)),
      sooner: () => this.setState({ mo: Math.max(1, months - 1) }), later: () => this.setState({ mo: months + 1 }),
      made: st.made === tp, notMade: st.made !== tp, madeName: st.made == null ? '' : N[st.made],
      make: () => this.setState({ made: tp })
    };
    v.made = st.made != null && st.made === tp; v.notMade = !v.made;
    v.madeName = st.made == null ? '' : N[st.made];
    for (let i = 0; i < 8; i++) {
      v['tp' + i] = () => this.setState({ tp: i, mo: null }); v['tpOn' + i] = tp === i;
      v['tpBg' + i] = tp === i ? '%(evg)s' : '#FFFFFF'; v['tpFg' + i] = tp === i ? '%(lime)s' : '%(ink)s';
    }
    return v;
  }
}''' % dict(R=rands_js(), setup=json.dumps([SETUP[k][:2] for k in range(8)]), names=json.dumps(names), evg=EVG, lime=LIME, ink=INK)
    return tool_page('Goals studio', body, logic, h=2020)


# ---------------------------------------------------------------- Home, with several goals

def home():
    """Round 7's Home (D-031: keep it as it is), with two Round 8 changes: several goals instead of one safety
    net, and the Hub's next useful thing. The tab bar becomes Round 8's."""
    import round7
    import home as home6
    html = round7.transform('R7-Home', home6.build())
    start = html.index('<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: 156px 156px; gap: 12px">')
    end = html.index('</a>\n    </div>', start) + len('</a>\n    </div>')
    old = html[start:end]
    word = re.search(r'<a href="R7-Vault\.dc\.html" class="tile".*?</a>', old, re.S).group(0)
    plan = re.search(r'<section class="tile" style="background: #FFFFFF">.*?</section>', old, re.S).group(0)
    word = word.replace('R7-Vault.dc.html', 'R8-Learn.dc.html').replace('>Stokvel<', '>Dividend<').replace('Say it: stok-fel. Tap to learn it.', 'Say it: div-i-dend. In Learn, under Words.')
    cards = ''
    for i, (n, have, want, g) in enumerate(MINE):
        first = i == 0
        pool_svg = pool(56, 118, 'hPool' + ('' if first else str(i)), rimw=2.5, hole='waterY' + ('' if first else str(i)), label='poolLabel' + ('' if first else str(i)))
        bg, fg, sub = (EVG, '#FFFFFF', ON_EVG) if first else ('#FFFFFF', INK, MUTED)
        amt_col = LIME if first else EVG
        cards += f'''<a href="R8-Goals.dc.html" style="width: 148px; flex-shrink: 0; box-sizing: border-box; border-radius: 14px; background: {bg}; color: {fg}; padding: 14px; display: flex; flex-direction: column; gap: 8px">
          <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: {sub}">{ic8(g, 16)}{n}</span>
          <span style="height: 118px; display: flex; align-items: center">{pool_svg}</span>
          <span style="font-size: 26px; font-weight: 600; letter-spacing: -0.04em; color: {amt_col}">{fmt_r(have, False)}</span>
          <span style="font-size: 12px; color: {sub}">of {fmt_r(want, False)}</span></a>'''
    cards += f'''<a href="R8-Goals.dc.html" style="width: 120px; flex-shrink: 0; box-sizing: border-box; border-radius: 14px; box-shadow: inset 0 0 0 1.5px #C9D3CE; padding: 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; text-align: center; color: {EVG}">
          <span style="width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic8('plus', 22, EVG)}</span><span style="font-size: 14px; font-weight: 600; line-height: 1.3">A new goal</span></a>'''
    new = f'''<section aria-label="Your goals" style="display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Your goals</span><a href="R8-Goals.dc.html" style="min-height: 44px; display: flex; align-items: center; font-size: 14px; font-weight: 600; color: {EVG}">Goals studio</a></span>
      <div style="display: flex; gap: 10px; margin: -8px -20px 0 0; overflow: hidden">{cards}</div>
    </section>
    <a href="R8-Tool-Payslip.dc.html" style="border-radius: 14px; background: {LIME}; color: {EVG}; padding: 14px 16px; display: flex; align-items: center; gap: 12px">
      <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 10px; background: {EVG}; color: {LIME}; display: flex; align-items: center; justify-content: center">{hub_icon(None, 22, LIME, anim=True)}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; font-weight: 600">From the Hub</span><span style="font-size: 16px; font-weight: 600; color: {INK}">Pay-day was today. Decode your payslip.</span></span>{icon('chev', 18, EVG)}</a>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: 156px; gap: 12px">
      {plan}
      {word}
    </div>'''
    html = html[:start] + new + html[end:]
    ns, ne = html.index('<nav aria-label="Main" class="tab"'), html.index('</nav>', html.index('<nav aria-label="Main" class="tab"')) + len('</nav>')
    html = html[:ns] + tabbar8('Home') + html[ne:]
    extra = ', '.join(f"waterY{i}: {round(118 * (1 - have / want))}, poolLabel{i}: '{n}: {fmt_r(have, False)} of {fmt_r(want, False)}'" for i, (n, have, want, _g) in enumerate(MINE) if i)
    html = html.replace("waterY: Math.round(150 * (1 - 1800 / 5000))", "waterY: Math.round(118 * (1 - 1800 / 5000)), " + extra)
    html = re.sub(r'"height":1580\}', '"height":1740}', html)
    html = html.replace('height: 1580px', 'height: 1740px')
    assert 'height: 1740px' in html
    return with_css(html, HUB_CSS + '.scr>*{flex-shrink:0}')


import json  # noqa: E402

BOARDS = [('R8-Goals', goals), ('R8-Home', home)]
