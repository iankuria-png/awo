"""Round 8, batch 3: the Hub landing in both modes, and the shared tool skeleton.
Writes R8-Hub (Naledi: employed, Johannesburg; opens on Me), R8-Hub-Biz (Wanjiru: a market stall in Nairobi;
opens on My business) and R8-Tool-Skeleton.

The modes are "Me" and "My business", as on Round 7's business Home, so members without a payslip are included.
The mode reorders the Hub; it never hides a tool. Stay safe is always last."""
from lib8 import *  # noqa: F401,F403
from learn8 import PHONE_CSS  # noqa: F401

GROUP_STYLE = {'Understand': (POOL, EVG), 'Plan': (LIME, EVG), 'Grow': (MIST, EVG), 'Run my business': (EVG, LIME), 'Stay safe': (WARN_BG, WARN_FG)}
GROUP_NOTE = {'Understand': 'Read what you were given', 'Plan': 'Decide where money goes', 'Grow': 'See further ahead',
              'Run my business': 'The everyday jobs', 'Stay safe': 'Before you sign or send'}

# (name, icon, value, href or None, ai)
T = {
    'payslip': ('Payslip decoder', 'doc', 'Every line, in plain words', 'R8-Tool-Payslip.dc.html', True),
    'statement': ('Statement insights', 'list', 'Debit orders and fees, from one statement', 'R8-Tool-Statement.dc.html', True),
    'explain': ('Explain a document', 'letter', 'A contract or policy, in plain words', None, True),
    'payday': ('Pay-day plan', 'calc', 'Every rand a job, family included', 'R8-Tool-Payday.dc.html', False),
    'payyou': ('Pay yourself', 'calc', 'Business money and home money, apart', 'R8-Tool-Payday.dc.html', False),
    'debt': ('Debt payoff', 'down', 'Your debt-free date', 'R8-Tool-Debt.dc.html', False),
    'goals': ('Goals studio', 'pool', 'A car, moving out, investing', 'R8-Goals.dc.html', False),
    'fees': ('Fee eater', 'grow', 'What fees cost over 20 years', 'R8-Tool-Fees.dc.html', False),
    'offers': ('Two job offers', 'swap', 'The whole package, side by side', None, False),
    'pension': ('Retirement pulse', 'clock', 'What your pension might pay', None, False),
    'offer': ('Check an offer', 'shield', "AWO's red-flag list, with the offer in hand", 'R7-Offer.dc.html', True),
    'loan': ("A loan's real cost", 'calc', 'The total you would repay', 'R7-Simulator.dc.html', False),
    'home': ('Sending money home', 'home', 'The fee and the rate: the real cost', None, False),
    'invoice': ('Quotes and invoices', 'letter', 'A quote becomes an invoice in one tap', 'R8-Tool-Invoice.dc.html', False),
    'notebook': ('Money in and out', 'list', 'Your notebook, and a profit page each month', 'R7-Biz-Home.dc.html', False),
    'shop': ('Shop', 'shop', 'A catalogue and a link; orders by WhatsApp', 'R8-Shop-Edit.dc.html', False),
    'price': ('Price it right', 'tag', 'Cost, margin, and how many to break even', 'R8-Tool-Price.dc.html', False),
    'worth': ('Is it worth it?', 'grow', 'When a new machine pays for itself', None, False),
    'setup': ('Business setup checklist', 'list', 'Registration, tax, a business account', None, False),
}

MEMBERS = {
    'naledi': dict(
        name='Naledi', face='naledi', place='Johannesburg', default=0,
        me=dict(next=('Pay-day was on Thursday', "Decode September's payslip: what came off, and why. About two minutes.", 'Decode my payslip', 'R8-Tool-Payslip.dc.html'),
                pickup=[('down', 'Debt plan', '2 of 3 debts added', 66, 'R8-Tool-Debt.dc.html'), ('key', 'Moving-out goal', 'Add the first-month costs', 30, 'R8-Goals.dc.html')],
                goals=[('Safety net', 36), ('Moving out', 12), ('A trip home', 40)],
                groups=[('Understand', ['payslip', 'statement', 'explain']), ('Plan', ['payday', 'debt', 'goals']), ('Grow', ['fees', 'offers', 'pension']), ('Stay safe', ['offer', 'loan', 'home'])]),
        biz=None),
    'wanjiru': dict(
        name='Wanjiru', face='wanjiru', place='Nairobi', default=1,
        me=dict(next=('School fees are due in January', 'Your school-fees pool is at 45%. See what each month needs to reach it.', 'Open the goal', 'R8-Goals.dc.html'),
                pickup=[('down', 'Debt plan', 'The stock loan, added', 50, 'R8-Tool-Debt.dc.html')],
                goals=[('School fees', 45), ('Safety net', 20), ('A trip home', 8)],
                groups=[('Plan', ['payyou', 'debt', 'goals']), ('Understand', ['statement', 'explain']), ('Grow', ['fees']), ('Stay safe', ['offer', 'home', 'loan'])]),
        biz=dict(next=('Two invoices are unpaid', "KSh 9 300 from two customers. Achieng's is nine days late.", 'See who owes me', 'R8-Tool-Invoice.dc.html'),
                 pickup=[('letter', 'Quote for the Serena order', 'Draft, three items', 40, 'R8-Tool-Invoice.dc.html'), ('tag', 'Price it right', 'Woven baskets: 3 of 4 costs', 75, 'R8-Tool-Price.dc.html')],
                 goals=[('Business stock', 64), ("A month's float", 30), ('School fees', 45)],
                 groups=[('Run my business', ['invoice', 'notebook', 'shop']), ('Plan', ['price', 'payyou', 'worth']), ('Grow', ['setup']), ('Stay safe', ['offer', 'loan', 'explain'])])),
}
MODE_W = 171


def mini_pool(pct, k, delay=0):
    h, w = 64, 34
    water = round(h * (1 - pct / 100))
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; flex-shrink: 0">'
            f'<defs><clipPath id="mp{k}"><rect width="{w}" height="{h}" rx="{w / 2}"></rect></clipPath></defs>'
            f'<rect width="{w}" height="{h}" rx="{w / 2}" fill="{EVG_D}"></rect>'
            f'<g clip-path="url(#mp{k})"><rect x="0" y="{water}" width="{w}" height="{h}" fill="{POOL}" style="transform-origin: 0 {h}px; animation: grow .8s cubic-bezier(.2,.8,.2,1) {0.2 + delay * 0.1:.1f}s both"></rect>'
            f'<path d="M0 {water}q{w / 4} -4 {w / 2} 0t{w / 2} 0" fill="none" stroke="{LIME}" stroke-width="2"></path></g>'
            f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="{(w - 3) / 2}" fill="none" stroke="{LIME}" stroke-width="3"></rect></svg>')


def tool_row(key, i, first):
    name, g, value, href, ai = T[key]
    ai_chip = f'<span class="chip" style="height: 24px; padding: 0 7px; border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span>' if ai else ''
    inner = (f'<span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: [[ gbg ]]; color: [[ gfg ]]; display: flex; align-items: center; justify-content: center">{ic8(g, 22)}</span>'
             f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0"><span style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap"><span style="font-size: 16px; font-weight: 600">{name}</span>{ai_chip}</span>'
             f'<span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{value}</span></span>{icon("chev", 18, MUTED)}')
    st = f'min-height: 68px; display: flex; align-items: center; gap: 12px; text-align: left; width: 100%; {"" if first else "border-top: 1px solid " + LINE7 + ";"}'
    return f'<a href="{href}" style="{st}">{inner}</a>' if href else f'<button style="{st}">{inner}</button>'


def group(title, keys):
    bg, fg = GROUP_STYLE[title]
    rows = ''.join(tool_row(k, i, i == 0) for i, k in enumerate(keys)).replace('[[ gbg ]]', bg).replace('[[ gfg ]]', fg)
    return (f'<section style="display: flex; flex-direction: column; gap: 8px">'
            f'<span style="display: flex; justify-content: space-between; align-items: baseline; padding: 0 2px"><span style="font-size: 17px; font-weight: 600">{title}</span><span style="font-size: 13px; color: {MUTED}">{GROUP_NOTE[title]}</span></span>'
            f'<div style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 14px">{rows}</div></section>')


def pane(m, mode, key):
    nt, ntext, cta, href = m['next']
    pick = ''.join(f'''<a href="{h}" style="width: 200px; flex-shrink: 0; box-sizing: border-box; border-radius: {R_L}px; background: #FFFFFF; padding: 14px; display: flex; flex-direction: column; gap: 10px">
          <span style="display: flex; align-items: center; gap: 8px; color: {EVG}">{ic8(g, 18)}<span style="font-size: 15px; font-weight: 600; color: {INK}">{t}</span></span>
          <span style="font-size: 13px; color: {MUTED}">{sub}</span>
          <span aria-hidden="true" style="height: 6px; border-radius: 2px; background: {MIST}; overflow: hidden"><span style="display: block; height: 100%; width: {p}%; background: {EVG}; transform-origin: 0 0; animation: fill .7s cubic-bezier(.2,.8,.2,1) .2s both"></span></span></a>''' for g, t, sub, p, h in m['pickup'])
    goals = ''.join(f'<a href="R8-Goals.dc.html" style="flex: 1 1 0; border-radius: {R_L}px; background: #FFFFFF; padding: 12px 10px; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">{mini_pool(p, f"{key}{i}", i)}<span style="font-size: 14px; font-weight: 600; line-height: 1.2">{n}</span><span style="font-size: 13px; color: {MUTED}">{p}%</span></a>' for i, (n, p) in enumerate(m['goals']))
    groups = ''.join(group(t, ks) for t, ks in m['groups'])
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 10px">
        <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600">{hub_icon(None, 18, EVG)}The next useful thing</span>
        <h2 class="d" style="font-size: 32px">{nt}</h2>
        <p style="font-size: 16px; line-height: 1.45; color: {INK}">{ntext}</p>
        <a href="{href}" style="margin-top: 6px; height: 52px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">{cta}</a>
      </section>
      <span style="font-size: 17px; font-weight: 600; margin-top: 2px">Pick up where you left off</span>
      <div style="display: flex; gap: 10px; margin-right: -20px; overflow: hidden">{pick}</div>
      <span style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 2px"><span style="font-size: 17px; font-weight: 600">Your goals</span><a href="R8-Goals.dc.html" style="min-height: 44px; display: flex; align-items: center; font-size: 14px; font-weight: 600; color: {EVG}">Goals studio</a></span>
      <div style="display: flex; gap: 10px; margin-top: -8px">{goals}</div>
      {groups}
      <a href="R7-Me.dc.html" style="min-height: 60px; border-radius: {R_L}px; background: {POOL}; padding: 0 16px; display: flex; align-items: center; gap: 12px; color: {EVG}">{icon('stones', 22, EVG)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Where you stand lives in Me</span><span style="font-size: 13px; color: {SEC}">Next check-in: 13 October</span></span>{icon('chev', 18, EVG)}</a>
      <button style="height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 15px; font-weight: 600">All 18 tools</button>
    </div>'''


def empty_biz():
    """Naledi has no business yet: the Hub says what it would do, and asks two minutes to set up."""
    prev = ''.join(f'<span style="display: flex; align-items: center; gap: 12px; min-height: 52px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="width: 40px; height: 40px; border-radius: {R_M}px; background: {EVG}; color: {LIME}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {MUTED}">{v}</span></span></span>'
                   for i, (n, g, v) in enumerate([('Quotes and invoices', 'letter', 'Get paid on time'), ('Price it right', 'tag', 'Charge enough to keep some'), ('Shop', 'shop', 'A catalogue and a link')]))
    return f'''<div class="pane" style="display: flex; flex-direction: column; gap: 16px; animation: [[ paneAnim ]] .32s cubic-bezier(.2,.8,.2,1) both">
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 22px 18px; display: flex; flex-direction: column; gap: 14px">
        <span style="width: 56px; height: 56px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8('shop', 28)}</span>
        <h2 class="d" style="font-size: 32px">A side business, or thinking of one?</h2>
        <p style="font-size: 16px; line-height: 1.45; color: {SEC}">Tell AWO a little about it and these tools appear here, with your currency and your numbers.</p>
        <div style="display: flex; flex-direction: column">{prev}</div>
        <a href="R7-Biz-Profile.dc.html" style="height: 52px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">Add my business, two minutes</a>
      </section>
      <span style="font-size: 14px; line-height: 1.45; color: {MUTED}; padding: 0 4px">Nothing is hidden meanwhile: every tool is still in "All 18 tools".</span>
    </div>'''


def mode_switch():
    btns = ''.join(f'<button role="tab" class="tabbtn" onClick="[[ tab{i} ]]" aria-selected="[[ tOn{i} ]]" style="position: relative; z-index: 1; flex: 1 1 0; height: 44px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600; color: [[ tFg{i} ]]">{ic8(g, 18)}{n}</button>'
                   for i, (n, g) in enumerate([('Me', 'stones'), ('My business', 'shop')]))
    return (f'<div role="tablist" aria-label="Hub mode" style="position: relative; display: flex; padding: 4px; border-radius: {R_M}px; background: #FFFFFF">'
            f'<span aria-hidden="true" style="position: absolute; top: 4px; bottom: 4px; left: [[ indL ]]px; right: [[ indR ]]px; border-radius: 8px; background: {EVG}; '
            f'transition: left .34s cubic-bezier(.2,.8,.2,1) [[ dl ]]s, right .34s cubic-bezier(.2,.8,.2,1) [[ dr ]]s"></span>{btns}</div>')


def hub(mkey):
    m = MEMBERS[mkey]
    me_pane = pane(m['me'], 'me', mkey + 'm')
    biz_pane = pane(m['biz'], 'biz', mkey + 'b') if m['biz'] else empty_biz()
    body = f'''  <div class="scr" style="gap: 16px">
    <header style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
      <h1 class="d" style="font-size: 44px">Hub</h1>
      <img class="face" src="{IMG[m['face']]}" alt="{m['name']}, {m['place']}" style="width: 44px; height: 44px">
    </header>
    <label for="hub-q" style="height: 52px; border-radius: {R_M}px; background: #FFFFFF; padding: 0 16px; display: flex; align-items: center; gap: 10px; color: {MUTED}">{icon('search', 20, INK)}<input id="hub-q" placeholder="What do you want to do?" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 16px; color: {INK}; outline: none"></label>
    {mode_switch()}
    <sc-if value="[[ p0 ]]" hint-placeholder-val="[[ {"true" if m['default'] == 0 else "false"} ]]">{me_pane}</sc-if>
    <sc-if value="[[ p1 ]]" hint-placeholder-val="[[ {"true" if m['default'] == 1 else "false"} ]]">{biz_pane}</sc-if>
  </div>
  {tabbar8('Hub')}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
    const t = st.t == null ? %(d)d : st.t, from = st.from == null ? t : st.from;
    const dir = t > from ? 1 : (t < from ? -1 : 0);
    v.indL = 4 + t * %(w)d; v.indR = 346 - %(w)d * (t + 1);
    v.dl = dir > 0 ? .08 : 0; v.dr = dir < 0 ? .08 : 0;
    v.paneAnim = dir > 0 ? 'inR' : (dir < 0 ? 'inL' : 'fadeIn');
    for (let i = 0; i < 2; i++) {
      v['tab' + i] = () => { if (i !== t) this.setState({ from: t, t: i }); };
      v['tOn' + i] = t === i; v['p' + i] = t === i; v['tFg' + i] = t === i ? '#FFFFFF' : '%(muted)s';
    }
    return v;
  }
}''' % dict(d=m['default'], w=MODE_W, muted=MUTED)
    h = 2100 if mkey == 'naledi' else 2080
    return with_css(phone('Hub', body, logic, h=h), PHONE_CSS + HUB_CSS)


def hub_naledi():
    return hub('naledi')


def hub_wanjiru():
    return hub('wanjiru')


# ---------------------------------------------------------------- the tool skeleton

BEATS = [('calc', 'Your numbers', 'Typed, or read from a photo or PDF that she checks line by line.'),
         ('pool', 'One plain result', 'One number and one sentence. Everything else is one tap deeper (rule D7).'),
         ('check', 'What it means', 'Governed text, marked "Reviewed by AWO". Never advice about her.'),
         ('moon', 'Learn this', 'The lesson behind it, and the Words it used.'),
         ('stones', 'Make it a goal or a step', 'Turn the result into a pool on Home, or this week\'s step.'),
         ('ripple', 'Share a milestone', 'A moment for her circle. It never carries an amount.')]
EXAMPLES = {
    'Payslip decoder': ['A photo of her payslip; she ticks six lines AI read', 'R 14 090 comes home, of R 18 500', 'R 1 388 of it is still hers: it goes to her pension', '"Your first payslip"; PAYE, UIF', 'Plan this R 14 090 in the pay-day plan', '"I can read my payslip now"'],
    'Price it right': ['Four costs for one woven basket, and the price now', 'Charge KSh 1 100 to keep 30%', 'A 20% markup is only a 17% margin', '"Pricing for profit"; markup, margin', 'Business stock: KSh 20 000 by March', '"First month in profit"'],
    'Fee eater': ['R 500 a month, for 20 years, and a yearly fee', 'A 2% fee takes about R 66 000', 'Fees come off every year, growth included', '"Fees, the quiet cost"; TER, compound', 'Start investing: a goal template', 'None: this tool has nothing to share'],
}
RULES = [('Deterministic and versioned', 'Every tool shows its version and the date of its figures ("Tax tables 2026/27, checked 1 March 2026"). Q-41 asks who keeps them current.'),
         ('AI reads or explains, nothing more', 'Reading a document, explaining a line, matching a word. Labelled "AI-assisted" and logged, never Ola (D-021, Q-32).'),
         ('Her numbers stay hers', 'Amounts never leave a tool unless she sends them herself, like an invoice to a customer. Milestones and buddies never see them.'),
         ('Education, not advice', 'Tools show what the numbers do. They never say which product, provider, loan or trade to choose (D-003).')]
DOC_PATH = [('camera', 'She adds a photo or PDF', 'With consent, each time'), ('eye', 'AI reads it', 'In South Africa; labelled'), ('check', 'She checks each line', 'Nothing counts until she does'),
            ('calc', 'The sum runs', 'Deterministic, versioned'), ('close', 'The original is deleted', 'Only her confirmed lines stay')]


def skeleton():
    beats = ''.join(f'''<div style="display: grid; grid-template-columns: 250px repeat(3, minmax(0, 1fr)); gap: 14px; padding: 14px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        <span style="display: flex; gap: 12px; align-items: flex-start"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {LIME if i < 2 else MIST}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span>
          <span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">{d}</span></span></span>
        {''.join(f'<span style="font-size: 14px; line-height: 1.45; color: {INK if i == 1 else SEC}; font-weight: {600 if i == 1 else 400}; padding-top: 2px">{EXAMPLES[k][i]}</span>' for k in EXAMPLES)}
      </div>''' for i, (g, t, d) in enumerate(BEATS))
    heads = ''.join(f'<span style="font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{hub_icon(None, 18, EVG)}{k}</span>' for k in EXAMPLES)
    rules = ''.join(f'<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.45; color: {SEC}">{d}</span></div>' for t, d in RULES)
    path = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center; position: relative">
        <span style="width: 52px; height: 52px; border-radius: 999px; background: {LIME if i == 2 else '#FFFFFF'}; box-shadow: inset 0 0 0 2px {EVG}; color: {EVG}; display: flex; align-items: center; justify-content: center; z-index: 1">{ic8(g, 24)}</span>
        <span style="font-size: 14px; font-weight: 600; line-height: 1.3">{t}</span><span style="font-size: 13px; color: {MUTED}">{d}</span></div>''' for i, (g, t, d) in enumerate(DOC_PATH))
    body = f'''<section class="card" style="gap: 4px">
      <div style="display: grid; grid-template-columns: 250px repeat(3, minmax(0, 1fr)); gap: 14px; padding-bottom: 10px"><span class="ktitle">The six beats</span>{heads}</div>
      {beats}
    </section>
    <div style="display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 24px; align-items: start">
      <section class="card" style="gap: 20px">
        <span class="ktitle">When a tool reads a document</span>
        <div style="position: relative; display: flex; gap: 8px">
          <span aria-hidden="true" style="position: absolute; left: 10%; right: 10%; top: 26px; height: 2px; background: {EVG}"></span>{path}</div>
        <span class="knote">The safe version of payslip, statement and contract reading (Q-37). Consent is asked for each upload, and "Your documents" in Me lists what is kept and when it goes. Processing in South Africa is a proposal until AWO's AI provider is chosen (Q-09).</span>
      </section>
      <section class="card" style="gap: 18px"><span class="ktitle">Rules for every tool</span>{rules}</section>
    </div>'''
    desc = ('Every Hub tool follows the same six beats, so learning one teaches them all. Each ends somewhere useful: a lesson, a goal, or a moment to share. '
            'Three tools shown beat by beat, with sample figures.')
    return with_css(board7('One skeleton for every tool', desc, body, static_logic(), 1600, 1400), HUB_CSS)


BOARDS = [('R8-Hub', hub_naledi), ('R8-Hub-Biz', hub_wanjiru), ('R8-Tool-Skeleton', skeleton)]
