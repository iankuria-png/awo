"""Round 9, batch 2: the Hub tools ranked 10 to 18 (doc 14), a savings-group record book, and "All tools".

Every tool follows the six-beat skeleton (R8-Tool-Skeleton): her numbers, one plain result, what it means (reviewed
by AWO), learn this, make it a goal or a step, and a milestone only where one makes sense. Tools work out her own
numbers the same way every time; none names, ranks or links a provider (D-003). Every fact is a dated sample (Q-41).

Sample members: Naledi (employed, Johannesburg), Amara (a nurse in London who sends money home to Harare) and
Wanjiru (a market stall in Nairobi)."""
import json

from lib9 import *  # noqa: F401,F403
from tools8 import tool_page


def tp(*a, **k):
    """tool_page with Round 9's shared CSS (segments, rows, sheets, toasts)."""
    k['css'] = CSS9 + k.get('css', '')
    return tool_page(*a, **k)
from biz8 import ksh_js

WARN_CHIP = f'<span class="chip" style="height: 24px; background: {WARN_BG}; color: {WARN_FG}">Ask about this</span>'
KNOW_CHIP = f'<span class="chip" style="height: 24px; background: {MIST}; color: {SEC}">Good to know</span>'


def js(o):
    return json.dumps(o, ensure_ascii=False)


def seg(hole, labels, aria):
    btns = ''.join(f'<button onClick="[[ {hole}{j} ]]" aria-pressed="[[ {hole}On{j} ]]" style="background: [[ {hole}Bg{j} ]]; color: [[ {hole}Fg{j} ]]">{t}</button>' for j, t in enumerate(labels))
    return f'<div role="group" aria-label="{aria}" class="seg9">{btns}</div>'


def seg_js(hole, n, cur):
    return ("    for (let j = 0; j < %d; j++) { v['%s' + j] = () => this.setState({ %s: j }); v['%sOn' + j] = %s === j; "
            "v['%sBg' + j] = %s === j ? '%s' : 'transparent'; v['%sFg' + j] = %s === j ? '#FFFFFF' : '%s'; }"
            % (n, hole, hole, hole, cur, hole, cur, EVG, hole, cur, INK))


def slider(id_, label, value_hole, min_, max_, step, cur, setter, pct):
    return (f'<span style="display: flex; justify-content: space-between; align-items: baseline"><label for="{id_}" style="font-size: 16px; font-weight: 600">{label}</label>'
            f'<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em; font-variant-numeric: tabular-nums">[[ {value_hole} ]]</span></span>'
            f'<input id="{id_}" class="rng8" type="range" min="{min_}" max="{max_}" step="{step}" value="[[ {cur} ]]" onInput="[[ {setter} ]]" style="--p: [[ {pct} ]]%">')


def stepper(label, hole, dec, inc, sub=''):
    btn = lambda h, lab, g: (f'<button onClick="[[ {h} ]]" aria-label="{lab}" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MIST}; '
                             f'display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 600; color: {EVG}">{g}</button>')
    subs = f'<span style="font-size: 12px; color: {MUTED}">{sub}</span>' if sub else ''
    return (f'<div style="display: flex; align-items: center; gap: 8px; min-height: 52px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 14px; color: {SEC}">{label}</span>{subs}</span>'
            f'{btn(dec, "Less", "−")}<span style="min-width: 76px; text-align: center; font-size: 17px; font-weight: 600; font-variant-numeric: tabular-nums">[[ {hole} ]]</span>{btn(inc, "More", "+")}</div>')


def toggle_row(i, label, sub=''):
    subs = f'<span style="font-size: 13px; color: {MUTED}">{sub}</span>' if sub else ''
    return (f'<div class="row9" style="padding-right: 0"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{label}</span>{subs}</span>{switch(i, label)}</div>')


def private_note(text):
    return (f'<span style="display: flex; gap: 8px; align-items: flex-start; font-size: 13px; line-height: 1.45; color: {SEC}; background: {MIST}; border-radius: {R_M}px; padding: 10px 12px">'
            f'{icon("lock", 16, EVG)}{text}</span>')


# ---------------------------------------------------------------- 10. Sending money home: the real cost

def remit():
    quote = lambda k, name: f'''<section class="card8" style="gap: 4px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 600">{name}</span><span style="font-size: 13px; color: {MUTED}">As you were quoted</span></span>
        {stepper('Fee', f'fee{k}', f'feeDn{k}', f'feeUp{k}')}
        {stepper('Rate', f'rate{k}', f'rateDn{k}', f'rateUp{k}', 'US$ for each £1')}
      </section>'''
    bars = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 6px">
        <span style="display: flex; justify-content: space-between; font-size: 14px"><span style="font-weight: 600">{n}</span><span style="font-variant-numeric: tabular-nums">[[ costTxt{k} ]] in all</span></span>
        <span aria-hidden="true" style="height: 14px; border-radius: 2px; background: {MIST}; display: flex; overflow: hidden"><span style="width: [[ feeW{k} ]]%; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span><span style="width: [[ fxW{k} ]]%; background: {WARN_FG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span>
        <span style="font-size: 13px; color: {MUTED}">[[ split{k} ]]</span></div>''' for k, n in enumerate(['Quote A', 'Quote B']))
    body = f'''    <div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG['amara']}" alt="" style="width: 36px; height: 36px"><span style="font-size: 14px; line-height: 1.4; color: {SEC}">Amara, a nurse in London, sends money to her mother in Harare.</span></div>
    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 14px">{slider('rm-send', 'You send', 'sendTxt', 50, 500, 10, 'send', 'setSend', 'sendP')}
      <span style="font-size: 13px; color: {MUTED}; margin-top: -6px">Type in two quotes you were given. AWO never names a provider.</span></section>
    {quote(0, 'Quote A')}
    {quote(1, 'Quote B')}
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; font-weight: 600">[[ bestName ]] gets more to your mother</span>
      <span class="d" style="font-size: 56px; font-variant-numeric: tabular-nums">[[ bestGot ]]</span>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ bestSub ]]</span>
    </section>
    <section class="card8" style="gap: 14px"><span style="font-size: 16px; font-weight: 600">What each one really costs</span>{bars}
      <span style="display: flex; gap: 14px; font-size: 13px"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {EVG}"></span>The fee</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: {WARN_FG}"></span>Hidden in the rate</span></span>
      <span style="font-size: 13px; color: {MUTED}">Measured against the mid-market rate, US$ 1,27 for £1: a sample from 26 September 2026.</span></section>
    {means("The real cost is the fee plus the gap between the rate you're offered and the mid-market rate. A transfer with no fee can still cost the most. Ask for the rate, not only the fee.")}
    {learn_this('The fee you don’t see', 3, ['Exchange rate', 'Mid-market rate'])}
    {make_goal('Plan it into pay-day', 'Money for home is a planned line, never a failure', 'R8-Tool-Payday.dc.html', 'calc', 'Plan it')}
    {foot("Sending money home, version 0.1. She types the quotes; AWO never names, ranks or links a provider. The mid-market rate is a dated sample (Q-41). No milestone: this stays private.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const send = st.send == null ? 200 : st.send, mid = 1.27;
    const fee = [st.f0 == null ? 3.99 : st.f0, st.f1 == null ? 0 : st.f1], rate = [st.r0 == null ? 1.25 : st.r0, st.r1 == null ? 1.21 : st.r1];
    const L = (n) => '\\u00a3' + n.toFixed(2).replace('.', ','), D = (n) => 'US$\\u00a0' + Math.round(n);
    const got = [0, 1].map((k) => Math.max(0, (send - fee[k]) * rate[k]));
    const cost = [0, 1].map((k) => send - got[k] / mid), fx = [0, 1].map((k) => cost[k] - fee[k]);
    const b = got[0] >= got[1] ? 0 : 1, o = 1 - b, max = Math.max(cost[0], cost[1], 1);
    const v = {
      send, sendTxt: '\\u00a3' + send, sendP: Math.round((send - 50) / 4.5), setSend: (e) => this.setState({ send: +e.target.value }),
      bestName: ['Quote A', 'Quote B'][b], bestGot: D(got[b]),
      bestSub: 'arrives, ' + D(got[b] - got[o]) + ' more than ' + ['Quote A', 'Quote B'][o] + '. It costs you ' + L(cost[b]) + ' in all' + (fee[b] === 0 ? ', though it has no fee.' : '.')
    };
    [0, 1].forEach((k) => {
      v['fee' + k] = fee[k] === 0 ? 'None' : L(fee[k]); v['rate' + k] = rate[k].toFixed(2).replace('.', ',');
      v['feeDn' + k] = () => this.setState({ ['f' + k]: Math.max(0, Math.round((fee[k] - 0.5) * 100) / 100) });
      v['feeUp' + k] = () => this.setState({ ['f' + k]: Math.round((fee[k] + 0.5) * 100) / 100 });
      v['rateDn' + k] = () => this.setState({ ['r' + k]: Math.round((rate[k] - 0.01) * 100) / 100 });
      v['rateUp' + k] = () => this.setState({ ['r' + k]: Math.min(mid, Math.round((rate[k] + 0.01) * 100) / 100) });
      v['costTxt' + k] = L(cost[k]); v['feeW' + k] = Math.round(fee[k] / max * 100); v['fxW' + k] = Math.round(Math.max(0, fx[k]) / max * 100);
      v['split' + k] = (fee[k] ? L(fee[k]) + ' fee, ' : 'No fee, ') + L(Math.max(0, fx[k])) + ' in the rate. ' + D(got[k]) + ' arrives.';
    });
    return v;
  }
}'''
    return tp('Sending money home', body, logic, h=2360)


# ---------------------------------------------------------------- 13. A loan's real cost, and explain my agreement

FLAGS = [('warn', 'Credit life insurance, R 45 a month', 'Insurance that pays the loan if you die or can’t work. It adds to the cost.', 'Can I use a policy I already have?'),
         ('warn', 'Initiation fee, R 1 150, added to the loan', 'Because it is added to what you borrow, you pay interest on it too.', 'Can I pay the fee up front instead?'),
         ('warn', 'Interest: 27,75% a year, linked to the repo rate', 'If the repo rate goes up, so does your instalment.', 'What would I pay each month if the rate rose by 1%?'),
         ('know', 'You may settle early', 'You can pay the loan off before 12 months, with notice.', 'How much notice, and is there a fee?'),
         ('know', 'Debit order on the 26th', 'The day after payday, so the money should be there.', '')]


def loan():
    terms = seg('tm', ['6 months', '12 months', '24 months'], 'Over how long')
    flags = ''
    for i, (kind, t, d, ask) in enumerate(FLAGS):
        chip = WARN_CHIP if kind == 'warn' else KNOW_CHIP
        ask_html = f'<span style="display: flex; gap: 8px; font-size: 14px; line-height: 1.4; color: {EVG}; font-weight: 600">{ic8("question", 16, EVG)}{ask}</span>' if ask else ''
        flags += f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="display: flex; justify-content: space-between; gap: 8px; align-items: flex-start"><span style="font-size: 15px; font-weight: 600">{t}</span>{chip}</span>
          <span style="font-size: 14px; line-height: 1.45; color: {SEC}">{d}</span>{ask_html}</div>'''
    real = f'''    <sc-if value="[[ tab0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: fadeIn .25s ease-out both">
    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 14px">{slider('ln-amt', 'You borrow', 'amtTxt', 2000, 20000, 500, 'amt', 'setAmt', 'amtP')}
      {terms}
      {slider('ln-rate', 'Interest a year', 'rateTxt', 10, 28, 0.25, 'rate', 'setRate', 'rateP')}
      <span style="font-size: 13px; line-height: 1.45; color: {MUTED}">Plus an initiation fee of R 1 150, added to the loan, and a service fee of R 69 a month. Sample fees (Q-41).</span></section>
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; font-weight: 600">You would pay back</span><span class="d" style="font-size: 56px; font-variant-numeric: tabular-nums">[[ total ]]</span>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ totalSub ]]</span>
      <div aria-hidden="true" style="display: flex; height: 14px; border-radius: 2px; overflow: hidden; margin-top: 6px"><span style="width: [[ wP ]]%; background: {EVG}"></span><span style="width: [[ wI ]]%; background: #3E7A63"></span><span style="width: [[ wF ]]%; background: {WARN_FG}"></span></div>
      <span style="display: flex; flex-wrap: wrap; gap: 12px; font-size: 13px; color: {INK}"><span>What you borrow [[ pTxt ]]</span><span>Interest [[ iTxt ]]</span><span>Fees [[ fTxt ]]</span></span>
    </section>
    <section class="card8" style="gap: 6px"><span style="font-size: 16px; font-weight: 600">[[ altHead ]]</span><span style="font-size: 15px; line-height: 1.45; color: {SEC}">[[ altText ]]</span></section>
    </div></sc-if>'''
    explain = f'''    <sc-if value="[[ tab1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: fadeIn .25s ease-out both">
    <section class="card8" style="gap: 12px">
      <span style="display: flex; gap: 12px; align-items: center"><span aria-hidden="true" style="width: 48px; height: 60px; flex-shrink: 0; border-radius: {R_S}px; background: {MIST}; box-shadow: inset 0 0 0 1px #C9D3CE; display: flex; align-items: center; justify-content: center">{ic8('letter', 22, EVG)}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; gap: 6px; align-items: center"><span style="font-size: 15px; font-weight: 600">Credit agreement, 4 pages</span>{AI_CHIP}</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">Read against AWO's reviewed list of lines to look for. The photos were deleted after reading.</span></span></span>
    </section>
    {beat("Lines worth asking about", "flag")}
    <section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px">{flags}</section>
    <button onClick="[[ copy ]]" style="height: 52px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('doc', 20, '#FFFFFF')}Copy my three questions</button>
    <span style="font-size: 14px; line-height: 1.5; color: {SEC}; background: #FFFFFF; border-radius: {R_M}px; padding: 12px 14px">AWO can't tell you whether to sign. These are the lines worth asking the lender about before you do.</span>
    </div></sc-if>'''
    body = f'''    {seg('pt', ['The real cost', 'Explain my agreement'], 'Part of the tool')}
{real}
{explain}
    {means("The real cost of a loan is everything you pay back, minus what you borrowed: interest, fees, and anything added to it, like insurance.")}
    {learn_this('What a loan really costs', 4, ['Interest', 'Initiation fee', 'Credit life insurance'])}
    {make_goal('Or save for it', '[[ saveLine ]]', 'R8-Goals.dc.html', 'pool', 'Open')}
    {foot("A loan's real cost, version 0.1. Worked out monthly on the whole amount, fees included. The agreement reading is AI-assisted and checked against a list AWO reviews; it never says whether to sign.")}
    <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div class="toast">{icon('check', 18, LIME, 2.6)}<span>Copied. Paste them into a message to the lender.</span></div></sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const amt = st.amt == null ? 8000 : st.amt, rate = st.rate == null ? 27.75 : st.rate, tm = st.tm == null ? 1 : st.tm, tab = st.pt || 0;
    const N = [6, 12, 24];
    const cost = (n) => { const P = amt + 1150, r = rate / 1200; const pay = P * r / (1 - Math.pow(1 + r, -n)); return { pay: pay + 69, total: (pay + 69) * n, interest: pay * n - P }; };
    const c = cost(N[tm]), fees = 1150 + 69 * N[tm], total = c.total;
    const alt = tm === 1 ? cost(6) : cost(12), an = tm === 1 ? 6 : 12;
    const v = {
      tab0: tab === 0, tab1: tab === 1, toast: !!st.toast, copy: () => this.setState({ toast: true }),
      amt, amtTxt: R(amt), amtP: Math.round((amt - 2000) / 180), setAmt: (e) => this.setState({ amt: +e.target.value }),
      rate, rateTxt: String(rate).replace('.', ',') + '%%', rateP: Math.round((rate - 10) / 0.18), setRate: (e) => this.setState({ rate: +e.target.value }),
      total: R(total), totalSub: R(c.pay) + ' a month for ' + N[tm] + ' months. The loan costs ' + R(total - amt) + ' on top of the ' + R(amt) + ' you borrow.',
      wP: Math.round(amt / total * 100), wI: Math.round(c.interest / total * 100), wF: Math.max(1, 100 - Math.round(amt / total * 100) - Math.round(c.interest / total * 100)),
      pTxt: R(amt), iTxt: R(c.interest), fTxt: R(fees),
      altHead: 'Over ' + an + ' months instead',
      altText: 'You would pay back ' + R(alt.total) + ', ' + (alt.total < total ? R(total - alt.total) + ' less' : R(alt.total - total) + ' more') + ' in all, and ' + R(alt.pay) + ' a month.',
      saveLine: 'At ' + R(Math.round(amt / 12 / 50) * 50) + ' a month, you would have ' + R(amt) + ' in about 12 months'
    };
%(seg1)s
%(seg2)s
    return v;
  }
}''' % dict(R=rands_js(), seg1=seg_js('tm', 3, 'tm'), seg2=seg_js('pt', 2, 'tab'))
    return tp("A loan's real cost", body, logic, h=2180)


# ---------------------------------------------------------------- 14. Is it worth it? (a business buy)

def worth():
    BARS = ''.join(f'<span aria-hidden="true" style="position: absolute; left: {round(k * 12.2)}px; width: 9px; top: [[ bt{k} ]]px; height: [[ bh{k} ]]px; border-radius: 2px; background: [[ bc{k} ]]; transition: top .35s cubic-bezier(.2,.8,.2,1), height .35s cubic-bezier(.2,.8,.2,1)"></span>' for k in range(26))
    body = f'''    <div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px"><span style="font-size: 14px; line-height: 1.4; color: {SEC}">Wanjiru wants a second-hand sewing machine, to make tote bags from her offcuts.</span></div>
    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 14px">
      {slider('w-cost', 'The machine costs', 'costTxt', 10000, 60000, 1000, 'cost', 'setCost', 'costP')}
      {slider('w-n', 'Extra bags a week', 'nTxt', 2, 20, 1, 'n', 'setN', 'nP')}
      <span style="display: flex; justify-content: space-between; font-size: 14px; color: {SEC}"><span>Sells for KSh 900; cloth and thread KSh 450</span><span>Repairs KSh 800 a month</span></span>
      {toggle_row(0, 'What if sales are half?', 'Plan for the slow weeks too')}
    </section>
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; font-weight: 600">It pays for itself in about</span><span class="d" style="font-size: 56px">[[ weeks ]]</span>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ weeksSub ]]</span>
    </section>
    <section class="card8" style="gap: 10px"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600">Money back, week by week</span><span style="font-size: 13px; color: {MUTED}">Half a year</span></span>
      <div role="img" aria-label="[[ chartLabel ]]" style="position: relative; height: 150px">
        <span aria-hidden="true" style="position: absolute; left: 0; right: 0; top: [[ zeroY ]]px; border-top: 1.5px dashed rgba(16,24,20,.35)"></span>
        {BARS}
      </div>
      <span style="display: flex; justify-content: space-between; font-size: 12px; color: {MUTED}"><span>Week 1</span><span>The day it has paid for itself</span><span>Week 26</span></span></section>
    {means("Payback is how long the machine takes to earn back what it cost. After that, what it earns is yours, as long as the extra sales are real. Try the slow weeks before you decide.")}
    {learn_this('Payback, in plain words', 3, ['Payback period', 'Profit margin'])}
    {make_goal('Save for the machine', 'A business goal, filled from your stall money', 'R8-Goals.dc.html', 'shop', 'Open')}
    {foot("Is it worth it?, version 0.1. Profit per bag is the price minus cloth and thread; repairs come off each month. A sample for design.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(K)s
    const cost = st.cost == null ? 28000 : st.cost, n0 = st.n == null ? 6 : st.n;
%(sw)s
    const n = v.sw0 ? n0 / 2 : n0, perWeek = n * 450 - 800 / 4.33;
    const w = perWeek > 0 ? Math.ceil(cost / perWeek) : 0;
    const lo = -cost, hi = Math.max(26 * perWeek - cost, cost * 0.4), span = hi - lo;
    const y = (m) => Math.round(144 - (m - lo) / span * 138);
    for (let k = 0; k < 26; k++) { const m = (k + 1) * perWeek - cost, a = y(m), z = y(0); v['bt' + k] = Math.min(a, z); v['bh' + k] = Math.max(2, Math.abs(a - z)); v['bc' + k] = m < 0 ? '#C9D3CE' : (k + 1 === w ? '%(lime)s' : '%(evg)s'); }
    Object.assign(v, {
      cost, costTxt: K(cost), costP: Math.round((cost - 10000) / 500), setCost: (e) => this.setState({ cost: +e.target.value }),
      n: n0, nTxt: String(n0), nP: Math.round((n0 - 2) / 0.18), setN: (e) => this.setState({ n: +e.target.value }),
      weeks: w > 0 ? w + ' weeks' : 'Not yet',
      weeksSub: w > 0 ? 'At ' + n + ' bags a week, it earns about ' + K(perWeek) + ' a week after repairs.' + (w > 26 ? ' That is longer than half a year.' : '') : 'At this many bags, repairs cost more than the bags earn.',
      zeroY: y(0),
      chartLabel: w > 0 ? 'The machine has paid for itself after about ' + w + ' weeks' : 'The machine does not pay for itself at this rate'
    });
    return v;
  }
}''' % dict(K=ksh_js(), lime=LIME, evg=EVG, sw=switch_js(1, [False]).replace('    for (let i', '    const v = {};\n    for (let i'))
    return tp('Is it worth it?', body, logic, h=1900, mode='My business', back='R8-Hub-Biz.dc.html')


# ---------------------------------------------------------------- 15. Two job offers

def offers():
    rows = [('Pay before anything comes off', 'R 18 500 basic', 'R 21 000 cost to company'), ('Pension', 'You 7,5%, and your employer adds 7,5%', '7,5%, from inside the package'),
            ('Medical aid', 'Your employer pays half', 'None: you would pay your own'), ('Leave', '15 days', '18 days'), ('The commute', 'Two taxis, R 1 380 a month', 'One taxi, R 900 a month')]
    table = ''.join(f'''<div style="display: grid; grid-template-columns: 96px 1fr 1fr; gap: 10px; padding: 10px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        <span style="font-size: 13px; font-weight: 600; color: {MUTED}">{n}</span><span style="font-size: 14px; line-height: 1.35">{a}</span><span style="font-size: 14px; line-height: 1.35">{b}</span></div>''' for i, (n, a, b) in enumerate(rows))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 0; padding-top: 12px">
      <div style="display: grid; grid-template-columns: 96px 1fr 1fr; gap: 10px; padding-bottom: 8px"><span></span><span style="font-size: 15px; font-weight: 600">Offer A</span><span style="font-size: 15px; font-weight: 600">Offer B</span></div>
      {table}
    </section>
    <section class="card8" style="gap: 2px; padding: 6px 6px 6px 16px">{toggle_row(0, 'Count the medical aid you would pay', 'About R 2 100 a month for Offer B (sample)')}<div style="border-top: 1px solid {LINE7}">{toggle_row(1, 'Count the commute', 'Taxi fares, both ways')}</div></section>
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="font-size: 14px; font-weight: 600">In your hand each month</span>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px">Offer A</span><span class="d" style="font-size: 34px; font-variant-numeric: tabular-nums">[[ handA ]]</span></span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px">Offer B</span><span class="d" style="font-size: 34px; font-variant-numeric: tabular-nums">[[ handB ]]</span></span></div>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ handLine ]]</span>
      <span style="font-size: 15px; line-height: 1.4; color: {INK}; border-top: 1px solid rgba(15,74,54,.2); padding-top: 10px"><b style="font-weight: 600">Into your pension:</b> R 2 775 a month with Offer A, R 1 575 with Offer B. That money is yours too, for later.</span>
    </section>
    {means("Cost to company counts everything the job costs the employer, including things you never see in your account, like pension and allowances. Compare what reaches you, and what goes in for later, separately.")}
    {learn_this('Cost to company, explained', 3, ['CTC', 'Take-home pay', 'Gross pay'])}
    {make_goal('Questions to ask HR', 'Medical aid, pension, leave and probation, before you choose', 'R7-Lesson.dc.html', 'list', 'See them')}
    {foot("Two job offers, version 0.1. Take-home is worked out with sample 2026/27 tax tables (Q-41). Only she can weigh the rest: the work, the people, and where each job leads.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const v = {};
%(sw)s
    const a = 14090 - (v.sw1 ? 1380 : 0), b = 16010 - (v.sw0 ? 2100 : 0) - (v.sw1 ? 900 : 0), d = b - a;
    v.handA = R(a); v.handB = R(b);
    v.handLine = d === 0 ? 'Both leave the same in your hand.' : 'Offer ' + (d > 0 ? 'B' : 'A') + ' leaves ' + R(Math.abs(d)) + ' more each month, counting what you chose above.';
    return v;
  }
}''' % dict(R=rands_js(), sw=switch_js(2, [True, True]))
    return tp('Two job offers', body, logic, h=1960)


# ---------------------------------------------------------------- 16. Business setup checklist

SETUP9 = {
    'Kenya': [('Register your business name', 'With the Business Registration Service, on eCitizen. About KSh 950.', 1),
              ('Your KRA PIN', 'A sole trader uses her own PIN. You have one.', 1),
              ('A single business permit', 'From Nairobi County. The fee depends on the trade and the area.', 0),
              ('A separate money line', 'A business account or a mobile-money till, so stall money and home money stay apart.', 0),
              ('Keep records', 'Money in and out, every day. Your notebook in AWO counts.', 1),
              ('Turnover tax', 'On sales between KSh 1 million and KSh 25 million a year. Not yet at your size.', 2),
              ('VAT', 'Only once sales pass KSh 5 million a year.', 2)],
    'South Africa': [('Choose how to trade', 'As a sole proprietor under your own name, or register a company with CIPC.', 0),
                     ('Tell SARS', 'A sole proprietor adds her business profit to her own tax return.', 0),
                     ('A separate account', 'So business money and home money stay apart.', 0),
                     ('Keep records', 'Money in and out, every day. Your notebook in AWO counts.', 1),
                     ('Turnover tax', 'A simpler tax for businesses under R 1 million a year. Optional.', 2),
                     ('VAT', 'Required once sales pass R 2,3 million a year (from 1 April 2026).', 2),
                     ('Local licences', 'Some trades, like food, need a municipal licence.', 0)],
}


def setup():
    panes = ''
    for ci, (country, steps) in enumerate(SETUP9.items()):
        rows = ''
        for i, (t, d, s) in enumerate(steps):
            k = f'{ci}_{i}'
            if s == 2:
                mark = f'<span class="chip" style="height: 24px; background: {MIST}; color: {SEC}">Later</span>'
                rows += f'''<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-top: 1px solid {LINE7}"><span style="width: 44px; height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="width: 24px; height: 24px; border-radius: {R_S}px; box-shadow: inset 0 0 0 2px #C9D3CE"></span></span>
              <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; padding-top: 10px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 15px; font-weight: 600; color: {MUTED}">{t}</span>{mark}</span><span style="font-size: 14px; line-height: 1.4; color: {MUTED}">{d}</span></span></div>'''
            else:
                rows += f'''<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><button role="checkbox" aria-checked="[[ ok{k} ]]" onClick="[[ tick{k} ]]" aria-label="{t}: done" style="width: 44px; height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="width: 24px; height: 24px; border-radius: {R_S}px; background: [[ okBg{k} ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center; transition: background-color .18s">{icon("check", 16, "#FFFFFF", 3)}</span></button>
              <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; padding-top: 10px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">{d}</span></span></div>'''
        panes += f'<sc-if value="[[ c{ci} ]]" hint-placeholder-val="[[ {"true" if ci == 0 else "false"} ]]"><section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px; animation: fadeIn .25s ease-out both">{rows}</section></sc-if>'
    body = f'''    <div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px"><span style="font-size: 14px; line-height: 1.4; color: {SEC}">Wanjiru's stall, in Nairobi. The steps follow the country her business is in.</span></div>
    {beat("Your numbers", "calc")}
    {seg('cn', ['Kenya', 'South Africa'], 'Country')}
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; font-weight: 600">Steps done</span><span class="d" style="font-size: 56px">[[ doneTxt ]]</span>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ nextTxt ]]</span>
      <span aria-hidden="true" style="height: 8px; border-radius: 2px; background: rgba(15,74,54,.18); overflow: hidden; margin-top: 4px"><span style="display: block; height: 100%; width: [[ doneP ]]%; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span>
    </section>
    {panes}
    <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}">{ic8('clock', 16, MUTED)}Each fact was last checked on 26 September 2026 (sample, Q-41).</span>
    {means("Registering protects your business name and makes it easier to open a business account, get paid by companies, and apply for support. Each step says what it costs and where to do it.")}
    {learn_this('Registering a small business', 4, ['KRA PIN', 'Turnover tax', 'VAT'])}
    {make_goal('Keep the notebook going', 'Records make every step after this easier', 'R7-Biz-Home.dc.html', 'list', 'Open')}
    {foot("Business setup checklist, version 0.1. General guidance, not tax advice: for her own case, an accountant or the tax office can confirm. Facts are dated samples (Q-41).")}'''
    counts = [len([s for s in st if s[2] != 2]) for st in SETUP9.values()]
    init = [[s[2] == 1 for s in st] for st in SETUP9.values()]
    names = [[s[0] for s in st] for st in SETUP9.values()]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const cn = st.cn || 0, ok = st.ok || %(init)s, names = %(names)s, counts = %(counts)s;
    const v = { c0: cn === 0, c1: cn === 1 };
    ok.forEach((list, c) => list.forEach((on, i) => {
      v['ok' + c + '_' + i] = on; v['okBg' + c + '_' + i] = on ? '%(evg)s' : '#FFFFFF';
      v['tick' + c + '_' + i] = () => { const n = ok.map((l) => l.slice()); n[c][i] = !on; this.setState({ ok: n }); };
    }));
    const mine = ok[cn], nm = names[cn], later = %(later)s[cn];
    const done = mine.filter((on, i) => on && !later[i]).length, next = nm.find((_, i) => !mine[i] && !later[i]);
    v.doneTxt = done + ' of ' + counts[cn]; v.doneP = Math.round(done / counts[cn] * 100);
    v.nextTxt = next ? 'Next: ' + next.charAt(0).toLowerCase() + next.slice(1) + '.' : 'Every step you need now is done.';
%(seg)s
    return v;
  }
}''' % dict(init=js(init), names=js(names), counts=js(counts), later=js([[s[2] == 2 for s in st] for st in SETUP9.values()]), evg=EVG, seg=seg_js('cn', 2, 'cn'))
    return tp('Business setup checklist', body, logic, h=2060, mode='My business', back='R8-Hub-Biz.dc.html')


# ---------------------------------------------------------------- 17. What I own and owe

OWN = [('Safety net pool', 1800), ('Moving-out pool', 1900), ('A trip home pool', 2600), ('Paid into Kopano stokvel', 4500)]
OWE = [('Personal loan', 18000), ('Store card', 6200), ('Clothing account', 2400), ('Aunt Lindiwe, no interest', 1500)]


def owe():
    def items(lst, key, col):
        return ''.join(f'''<button role="checkbox" aria-checked="[[ {key}{i} ]]" onClick="[[ {key}T{i} ]]" style="width: 100%; min-height: 52px; display: flex; align-items: center; gap: 12px; text-align: left; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: {R_S}px; background: [[ {key}Bg{i} ]]; box-shadow: inset 0 0 0 2px {col}; display: flex; align-items: center; justify-content: center">{icon("check", 14, "#FFFFFF", 3)}</span>
          <span style="flex-grow: 1; font-size: 15px">{n}</span><span style="font-size: 15px; font-weight: 600; font-variant-numeric: tabular-nums; opacity: [[ {key}Op{i} ]]">{fmt_r(v, False)}</span></button>''' for i, (n, v) in enumerate(lst))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 2px"><span style="display: flex; justify-content: space-between"><span style="font-size: 16px; font-weight: 600">What you own</span><span style="font-size: 16px; font-weight: 600; color: {EVG}">[[ ownTxt ]]</span></span>{items(OWN, 'o', EVG)}
      <div style="border-top: 1px solid {LINE7}; margin: 0 -10px 0 0">{toggle_row(0, 'Your pension, R 42 000', 'Locked away until you retire')}</div></section>
    <section class="card8" style="gap: 2px"><span style="display: flex; justify-content: space-between"><span style="font-size: 16px; font-weight: 600">What you owe</span><span style="font-size: 16px; font-weight: 600; color: {WARN_FG}">[[ oweTxt ]]</span></span>{items(OWE, 'w', WARN_FG)}</section>
    {private_note("Only you see this. It's never used for your DIVA score and never shared. Sample policy.")}
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 14px; font-weight: 600">[[ netHead ]]</span><span class="d" style="font-size: 56px; font-variant-numeric: tabular-nums">[[ netTxt ]]</span>
      <div aria-hidden="true" style="display: flex; flex-direction: column; gap: 6px; margin-top: 4px">
        <span style="display: flex; align-items: center; gap: 8px"><span style="width: 44px; font-size: 12px">Own</span><span style="height: 12px; width: [[ ownW ]]%; border-radius: 2px; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span>
        <span style="display: flex; align-items: center; gap: 8px"><span style="width: 44px; font-size: 12px">Owe</span><span style="height: 12px; width: [[ oweW ]]%; border-radius: 2px; background: {WARN_FG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span></div>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ netSub ]]</span>
    </section>
    {means("What you own minus what you owe is your net worth. It moves slowly. Below zero is common early on, or while you pay debt down, and every payment moves it up.")}
    {learn_this('Net worth, without the jargon', 3, ['Asset', 'Liability', 'Net worth'])}
    {make_goal('See when it turns', 'Your debt plan shows the month you owe less than you own', 'R8-Tool-Debt.dc.html', 'down', 'Open')}
    {foot("What I own and owe, version 0.1. Pools come from her goals; debts from her debt plan; the rest she typed. Worth a look every three months. There is no milestone: this stays private.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const own = %(own)s, owe = %(owe)s, o = st.o || own.map(() => true), w = st.w || owe.map(() => true);
    const v = {};
%(sw)s
    const O = own.reduce((s, x, i) => s + (o[i] ? x : 0), 0) + (v.sw0 ? 42000 : 0), W = owe.reduce((s, x, i) => s + (w[i] ? x : 0), 0), net = O - W, big = Math.max(O, W, 1);
    own.forEach((_, i) => { v['o' + i] = o[i]; v['oBg' + i] = o[i] ? '%(evg)s' : '#FFFFFF'; v['oOp' + i] = o[i] ? 1 : .4; v['oT' + i] = () => { const n = o.slice(); n[i] = !o[i]; this.setState({ o: n }); }; });
    owe.forEach((_, i) => { v['w' + i] = w[i]; v['wBg' + i] = w[i] ? '%(wine)s' : '#FFFFFF'; v['wOp' + i] = w[i] ? 1 : .4; v['wT' + i] = () => { const n = w.slice(); n[i] = !w[i]; this.setState({ w: n }); }; });
    Object.assign(v, {
      ownTxt: R(O), oweTxt: R(W), ownW: Math.round(O / big * 100), oweW: Math.round(W / big * 100),
      netHead: net >= 0 ? 'You own more than you owe, by' : 'You owe more than you own, by', netTxt: R(Math.abs(net)),
      netSub: v.sw0 ? 'Counting your pension. Without it, the gap is ' + R(Math.abs(net - 42000)) + (net - 42000 < 0 ? ' the other way.' : '.') : 'Without your pension. It is common while paying debt down, and it closes with every payment.'
    });
    return v;
  }
}''' % dict(R=rands_js(), own=js([x[1] for x in OWN]), owe=js([x[1] for x in OWE]), evg=EVG, wine=WARN_FG, sw=switch_js(1, [False]))
    return tp('What I own and owe', body, logic, h=2140)


# ---------------------------------------------------------------- 18. Retirement pulse

def pension():
    bars = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px">
        <span style="font-size: 12px; font-weight: 600; font-variant-numeric: tabular-nums">[[ bv{i} ]]</span>
        <div style="height: 150px; width: 100%; display: flex; align-items: flex-end; justify-content: center"><span style="width: 56%; height: [[ bh{i} ]]%; border-radius: 4px 4px 2px 2px; background: {EVG if i == 3 else "#8DBFAE"}; transition: height .45s cubic-bezier(.2,.8,.2,1)"></span></div>
        <span style="font-size: 12px; color: {MUTED}">[[ ba{i} ]]</span></div>''' for i in range(4))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 14px">
      <span style="display: flex; justify-content: space-between; font-size: 15px"><span style="color: {SEC}">You are 31. In your fund now</span><span style="font-weight: 600">R 42 000</span></span>
      <span style="display: flex; justify-content: space-between; font-size: 15px"><span style="color: {SEC}">Going in each month</span><span style="font-weight: 600">[[ inTxt ]]</span></span>
      {slider('p-add', 'Add more yourself', 'addTxt', 0, 5, 1, 'add', 'setAdd', 'addP')}
      <span style="font-size: 15px; font-weight: 600; margin-bottom: -6px">Retire at</span>{seg('ag', ['60', '63', '65'], 'Retire at')}
      <span style="font-size: 15px; font-weight: 600; margin-bottom: -6px">Growth above inflation</span>{seg('gr', ['Lower, 2%', 'Middle, 4%', 'Higher, 6%'], 'Growth')}
    </section>
    {beat("One plain result", "pool")}
    <section style="border-radius: {R_L}px; background: {LIME}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; font-weight: 600">It might pay about, each month</span><span class="d" style="font-size: 56px; font-variant-numeric: tabular-nums">[[ month ]]</span>
      <span style="font-size: 16px; line-height: 1.4; color: {INK}">[[ monthSub ]]</span>
    </section>
    <section class="card8" style="gap: 10px"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600">Your fund, in today's money</span><span style="font-size: 13px; color: {MUTED}">An illustration</span></span>
      <div role="img" aria-label="[[ chartLabel ]]" style="display: flex; gap: 10px">{bars}</div></section>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 14px 16px; font-size: 14px; line-height: 1.5">Since September 2024, part of what goes in lands in a savings pot you can reach once a year. Every withdrawal lowers this number. A dated sample fact (Q-41).</section>
    {means("Small changes early make a big difference later, because growth builds on growth. This is an illustration, not a promise: returns go up and down, and some years go down.")}
    {learn_this('Your pension, in plain words', 4, ['Two-pot system', 'Annuity', 'Compound growth'])}
    {make_goal('Add 1% on your next raise', 'A step: you won’t miss what you never had', 'R8-Tool-Payday.dc.html', 'grow', 'Plan it')}
    {foot("Retirement pulse, version 0.1. Assumes steady growth above inflation, no withdrawals, pay that keeps up with inflation, and a fund spread over 25 years. AWO never names a fund.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(R)s
    const add = st.add == null ? 0 : st.add, ag = st.ag == null ? 2 : st.ag, gr = st.gr == null ? 1 : st.gr;
    const age = [60, 63, 65][ag], g = [0.02, 0.04, 0.06][gr], pay = 2775 + 18500 * add / 100;
    const r = Math.pow(1 + g, 1 / 12) - 1;
    const fund = (yrs) => { const n = yrs * 12, f = Math.pow(1 + r, n); return 42000 * f + pay * (f - 1) / r; };
    const pot = fund(age - 31), month = pot / 300;
    const M = (n) => n >= 1e6 ? 'R\\u00a0' + (n / 1e6).toFixed(1).replace('.', ',') + '\\u00a0m' : R(Math.round(n / 1000) * 1000);
    const v = {
      add, addTxt: add ? '+' + add + '%%' : 'Nothing more', addP: add * 20, setAdd: (e) => this.setState({ add: +e.target.value }),
      inTxt: R(pay), month: R(Math.round(month / 100) * 100),
      monthSub: 'from a fund of about ' + M(pot) + ' at ' + age + ', in today\\u2019s money. About ' + Math.round(month / 14090 * 100) + '%% of what reaches you each month now.',
      chartLabel: 'Your fund grows to about ' + M(pot) + ' by ' + age
    };
    const ages = [40, 50, age - 5, age];
    ages.forEach((a, i) => { const f = fund(a - 31); v['bv' + i] = M(f); v['bh' + i] = Math.max(3, Math.round(f / pot * 100)); v['ba' + i] = 'At ' + a; });
%(s1)s
%(s2)s
    return v;
  }
}''' % dict(R=rands_js(), s1=seg_js('ag', 3, 'ag'), s2=seg_js('gr', 3, 'gr'))
    return tp('Retirement pulse', body, logic, h=2140)


# ---------------------------------------------------------------- The savings-group record book (Q-45)

MEMBERS9 = [('Naledi', 'naledi', 1, '1 Oct'), ('Thandi', 'thandi', 1, '1 Oct'), ('Grace', 'grace', 1, '1 Oct'), ('Lindiwe', 'lindiwe', 1, '2 Oct'),
            ('Mpho', None, 1, '2 Oct'), ('Zodwa', 'zodwa', 1, '2 Oct'), ('Palesa', None, 1, '3 Oct'), ('Kagiso', None, 1, '3 Oct'),
            ('Zanele', None, 0, ''), ('Lerato', None, 0, '')]
ORDER9 = ['Thandi', 'Grace', 'Naledi', 'Lindiwe', 'Palesa', 'Zodwa', 'Kagiso', 'Zanele', 'Lerato', 'Mpho']
MONTHS9 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
RULES_G = [('Each month', 'R 500 each, by the 3rd.'), ('Late', 'R 50 into the pot if it is after the 5th.'), ('The pot', "Paid out on the 5th, in the order below."),
           ('Leaving', "Tell the group a month ahead. You get back what you paid in, less any turn you've had."), ('December', 'A braai together, paid for separately.')]


def avatar(name, face, size=40):
    if face:
        return f'<img class="face" src="{IMG[face]}" alt="" style="width: {size}px; height: {size}px">'
    return (f'<span aria-hidden="true" style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: 999px; background: {POOL}; color: {EVG}; '
            f'display: flex; align-items: center; justify-content: center; font-size: {round(size * .4)}px; font-weight: 600">{name[0]}</span>')


def group_book():
    faces = dict((n, f) for n, f, _s, _d in MEMBERS9)
    mrows = ''.join(f'''<div style="min-height: 60px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">{avatar(n, f)}
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{n}{" (you)" if n == "Naledi" else ""}</span><span style="font-size: 13px; color: [[ mc{i} ]]">[[ ms{i} ]]</span></span>
          <sc-if value="[[ un{i} ]]" hint-placeholder-val="[[ {"false" if s else "true"} ]]"><button onClick="[[ mark{i} ]]" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">Mark paid</button></sc-if>
          <sc-if value="[[ pd{i} ]]" hint-placeholder-val="[[ {"true" if s else "false"} ]]"><span aria-label="Paid" style="width: 32px; height: 32px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon("check", 18, EVG, 2.8)}</span></sc-if></div>''' for i, (n, f, s, _d) in enumerate(MEMBERS9))
    orows = ''.join(f'''<div style="min-height: 56px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="width: 40px; font-size: 13px; font-weight: 600; color: {MUTED}">{MONTHS9[i]}</span>{avatar(n, faces[n], 32)}
          <span style="flex-grow: 1; font-size: 15px; font-weight: {600 if i == 9 else 500}">{n}{" (you)" if n == "Naledi" else ""}</span>
          {f'<span class="chip" style="height: 26px; background: {LIME}; color: {EVG}">5 Oct, next</span>' if i == 9 else f'<span style="font-size: 13px; color: {MUTED}">Received</span>'}</div>''' for i, n in enumerate(ORDER9))
    rrows = ''.join(f'<div style="padding: 12px 0; display: flex; flex-direction: column; gap: 3px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="font-size: 13px; font-weight: 600; color: {MUTED}">{t}</span><span style="font-size: 15px; line-height: 1.45">{d}</span></div>' for i, (t, d) in enumerate(RULES_G))
    how = ''.join(f'<button onClick="[[ how{j} ]]" aria-pressed="[[ howOn{j} ]]" style="background: [[ howBg{j} ]]; color: [[ howFg{j} ]]">{t}</button>' for j, t in enumerate(['Cash', 'Bank', 'Mobile money']))
    body = f'''    <header style="display: flex; align-items: center; gap: 10px">{back('R8-Hub.dc.html', 'Back to the Hub')}
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; color: {MUTED}">{hub_icon(None, 14, MUTED)}Hub, saving together</span><span style="font-size: 18px; font-weight: 600">Kopano stokvel</span></span>{sample_chip()}</header>
    <section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 16px 18px; display: flex; flex-direction: column; gap: 6px">
      <span style="font-size: 13px; color: {ON_EVG}">10 members, R 500 each on the 1st, the pot on the 5th</span>
      <span class="d" style="font-size: 40px; color: {LIME}">Mpho's turn</span>
      <span style="font-size: 15px; color: {ON_EVG}">R 5 000 on 5 October, once everyone has paid.</span>
    </section>
    <section style="border-radius: {R_L}px; background: {WARN_BG}; color: {WARN_FG}; padding: 12px 14px; display: flex; gap: 10px; align-items: flex-start; font-size: 14px; line-height: 1.45">{ic('shield', 20, WARN_FG)}<span><b style="font-weight: 600">AWO never holds, moves or promises your group's money.</b> This book is your group's own record. Sample (Q-45).</span></section>
    {seg('sv', ['October', 'Payout order', 'Rules'], 'Show')}
    <sc-if value="[[ tb0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 12px; animation: fadeIn .25s ease-out both">
      <section class="card8" style="gap: 8px"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 16px; font-weight: 600">[[ paidTxt ]]</span><span style="font-size: 14px; color: {SEC}; font-variant-numeric: tabular-nums">[[ potTxt ]]</span></span>
        <span aria-hidden="true" style="height: 8px; border-radius: 2px; background: {MIST}; overflow: hidden"><span style="display: block; height: 100%; width: [[ paidP ]]%; background: {EVG}; transition: width .4s cubic-bezier(.2,.8,.2,1)"></span></span></section>
      <section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px">{mrows}</section>
      <sc-if value="[[ someUnpaid ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ remind ]]" style="height: 52px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1.5px {EVG}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('whatsapp', 20, EVG)}Remind the ones still to pay</button></sc-if>
      <button onClick="[[ share ]]" style="height: 52px; border-radius: {R_M}px; font-size: 15px; font-weight: 600; color: {EVG}; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('share', 18, EVG)}Share October's record with the group</button>
    </div></sc-if>
    <sc-if value="[[ tb1 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px">{orows}</section>
      <span style="font-size: 14px; line-height: 1.45; color: {SEC}">Swapping turns needs both members to agree. Record the swap here after they do.</span>
    </div></sc-if>
    <sc-if value="[[ tb2 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s ease-out both">
      <section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px">{rrows}</section>
      <span style="font-size: 14px; line-height: 1.45; color: {SEC}">Your group's rules, in your group's words. AWO doesn't set them or enforce them.</span>
    </div></sc-if>
    {learn_this('Savings groups, in three minutes', 3, ['Stokvel', 'Chama'])}
    {foot("Savings group book, version 0.1. First names only. Only members the keeper adds can see the record. What a group may keep here waits on Q-45.")}'''
    overlays = f'''  <sc-if value="[[ sheet ]]" hint-placeholder-val="[[ false ]]"><div class="dim" onClick="[[ close ]]"></div>
    <div class="sheet" role="dialog" aria-label="Record a payment" style="padding: 10px 20px 28px; display: flex; flex-direction: column; gap: 14px">
      <span aria-hidden="true" style="align-self: center; width: 40px; height: 4px; border-radius: 2px; background: #C9D3CE"></span>
      <span style="font-size: 20px; font-weight: 600">[[ sheetTitle ]]</span>
      <span style="font-size: 15px; color: {SEC}">R 500 for October, on [[ today ]]</span>
      <span style="font-size: 15px; font-weight: 600; margin-bottom: -6px">How</span><div role="group" aria-label="How they paid" class="seg9">{how}</div>
      {primary('Save to the record', hole='save')}
      <button onClick="[[ close ]]" style="height: 48px; margin-top: -6px; border-radius: {R_M}px; font-size: 15px; font-weight: 600">Cancel</button>
    </div></sc-if>
  <sc-if value="[[ wa ]]" hint-placeholder-val="[[ false ]]"><div class="dim" onClick="[[ close ]]"></div>
    <div class="sheet" role="dialog" aria-label="A reminder to send" style="padding: 10px 20px 28px; display: flex; flex-direction: column; gap: 14px">
      <span aria-hidden="true" style="align-self: center; width: 40px; height: 4px; border-radius: 2px; background: #C9D3CE"></span>
      <span style="font-size: 20px; font-weight: 600">A reminder, ready to send</span>
      <span style="border-radius: 10px 10px 10px 2px; background: #E7F6DF; padding: 12px 14px; font-size: 15px; line-height: 1.5">Hi [[ waNames ]], a friendly reminder that October's R 500 for Kopano is due. The pot goes to Mpho on the 5th. Thank you! Naledi</span>
      <span style="font-size: 13px; color: {MUTED}">WhatsApp opens with this message. You can change it before you send.</span>
      {primary('Open WhatsApp', hole='sendWa')}
      <button onClick="[[ close ]]" style="height: 48px; margin-top: -6px; border-radius: {R_M}px; font-size: 15px; font-weight: 600">Cancel</button>
    </div></sc-if>
  <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div class="toast">{icon('check', 18, LIME, 2.6)}<span>[[ toastText ]]</span></div></sc-if>'''
    names = [m[0] for m in MEMBERS9]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const names = %(names)s, dates = %(dates)s, paid = st.paid || %(paid)s, tb = st.sv || 0, how = st.how || 0;
    const n = paid.filter(Boolean).length, un = names.filter((_, i) => !paid[i]);
    const v = {
      tb0: tb === 0, tb1: tb === 1, tb2: tb === 2,
      paidTxt: n + ' of 10 paid', potTxt: 'R\\u00a0' + (n * 500).toLocaleString('en-ZA').replace(/,/g, '\\u00a0') + ' of R\\u00a05\\u00a0000', paidP: n * 10,
      someUnpaid: un.length > 0, sheet: st.sheet != null, wa: !!st.wa, toast: !!st.toast, toastText: st.toast || '',
      sheetTitle: st.sheet != null ? names[st.sheet] + ' paid' : '', today: '4 Oct',
      waNames: un.join(' and '),
      remind: () => this.setState({ wa: true, toast: '' }), sendWa: () => this.setState({ wa: false, toast: 'WhatsApp opened with your reminder.' }),
      share: () => this.setState({ toast: "October's record is ready to share: first names, amounts and dates." }),
      close: () => this.setState({ sheet: null, wa: false }),
      save: () => { const p = paid.slice(); p[st.sheet] = true; this.setState({ paid: p, sheet: null, toast: names[st.sheet] + ' marked paid on 4 Oct.' }); }
    };
    names.forEach((nm, i) => {
      v['un' + i] = !paid[i]; v['pd' + i] = !!paid[i];
      v['ms' + i] = paid[i] ? 'Paid ' + (dates[i] || '4 Oct') : 'Not yet'; v['mc' + i] = paid[i] ? '%(mut)s' : '%(wine)s';
      v['mark' + i] = () => this.setState({ sheet: i, toast: '' });
    });
%(seg1)s
    for (let j = 0; j < 3; j++) { v['how' + j] = () => this.setState({ how: j }); v['howOn' + j] = how === j; v['howBg' + j] = how === j ? '#FFFFFF' : 'transparent'; v['howFg' + j] = how === j ? '%(ink)s' : '%(sec)s'; }
    return v;
  }
}''' % dict(names=js(names), dates=js([m[3] for m in MEMBERS9]), paid=js([bool(m[2]) for m in MEMBERS9]), mut=MUTED, wine=WARN_FG, ink=INK, sec=SEC, seg1=seg_js('sv', 3, 'tb'))
    inner = f'  <div class="scr" style="gap: 16px">\n{body}\n  </div>\n{overlays}\n  {tabbar8("Hub")}'
    return free_page('Savings group book', inner, logic, h=1720)


# ---------------------------------------------------------------- All tools

ALL = [  # group, key, name, icon, value, href, ai, modes (m = Me, b = My business), new in Round 9
    ('Understand', 'Payslip decoder', 'doc', 'Every line, in plain words', 'R8-Tool-Payslip.dc.html', True, 'm', False),
    ('Understand', 'Statement insights', 'list', 'Debit orders and fees, from one statement', 'R8-Tool-Statement.dc.html', True, 'mb', False),
    ('Understand', 'Explain my agreement', 'letter', 'A loan or contract, line by line', 'R9-Tool-Loan.dc.html', True, 'mb', True),
    ('Plan', 'Pay-day plan', 'calc', 'Every rand a job, family included', 'R8-Tool-Payday.dc.html', False, 'm', False),
    ('Plan', 'Pay yourself', 'calc', 'Business money and home money, apart', 'R8-Tool-Payday.dc.html', False, 'b', False),
    ('Plan', 'Debt payoff', 'down', 'Your debt-free date', 'R8-Tool-Debt.dc.html', False, 'mb', False),
    ('Plan', 'Goals studio', 'pool', 'A car, moving out, investing', 'R8-Goals.dc.html', False, 'mb', False),
    ('Plan', 'Savings group book', 'people', 'Who has paid, and whose turn', 'R9-Group-Book.dc.html', False, 'mb', True),
    ('Plan', 'What I own and owe', 'scale', 'A private snapshot', 'R9-Tool-Owe.dc.html', False, 'mb', True),
    ('Grow', 'Fee eater', 'grow', 'What fees cost over 20 years', 'R8-Tool-Fees.dc.html', False, 'mb', False),
    ('Grow', 'Two job offers', 'swap', 'The whole package, side by side', 'R9-Tool-Offers.dc.html', False, 'm', True),
    ('Grow', 'Retirement pulse', 'clock', 'What your pension might pay', 'R9-Tool-Pension.dc.html', False, 'm', True),
    ('Grow', 'Is it worth it?', 'grow', 'When a new machine pays for itself', 'R9-Tool-Worth.dc.html', False, 'b', True),
    ('Grow', 'Business setup checklist', 'list', 'Registration, tax, a business account', 'R9-Tool-Setup.dc.html', False, 'b', True),
    ('Run my business', 'Quotes and invoices', 'letter', 'A quote becomes an invoice in one tap', 'R8-Tool-Invoice.dc.html', False, 'b', False),
    ('Run my business', 'Money in and out', 'list', 'Your notebook, and a profit page each month', 'R7-Biz-Home.dc.html', False, 'b', False),
    ('Run my business', 'Shop', 'shop', 'A catalogue and a link; orders by WhatsApp', 'R8-Shop-Edit.dc.html', False, 'b', False),
    ('Run my business', 'Price it right', 'tag', 'Cost, margin, and how many to break even', 'R8-Tool-Price.dc.html', False, 'b', False),
    ('Stay safe', 'Check an offer', 'shield', "AWO's red-flag list, with the offer in hand", 'R7-Offer.dc.html', True, 'mb', False),
    ('Stay safe', "A loan's real cost", 'calc', 'The total you would repay', 'R9-Tool-Loan.dc.html', False, 'mb', True),
    ('Stay safe', 'Sending money home', 'home', 'The fee and the rate: the real cost', 'R9-Tool-Remit.dc.html', False, 'mb', True),
]
GROUPS_ALL = ['Understand', 'Plan', 'Grow', 'Run my business', 'Stay safe']


def all_tools():
    from hub8 import GROUP_STYLE, GROUP_NOTE
    secs = ''
    for g in GROUPS_ALL:
        bg, fg = GROUP_STYLE[g]
        rows = ''
        for i, (grp, name, glyph, value, href, ai, modes, new) in enumerate(ALL):
            if grp != g:
                continue
            chips = (f'<span class="chip" style="height: 22px; padding: 0 7px; background: {LIME}; color: {EVG}">New</span>' if new else '') + \
                    (f'<span class="chip" style="height: 22px; padding: 0 7px; border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span>' if ai else '')
            rows += f'''<sc-if value="[[ t{i} ]]" hint-placeholder-val="[[ true ]]"><a href="{href}" style="min-height: 68px; display: flex; align-items: center; gap: 12px; border-top: 1px solid {LINE7}">
            <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic8(glyph, 22)}</span>
            <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0"><span style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap"><span style="font-size: 16px; font-weight: 600">{name}</span>{chips}</span><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{value}</span></span>{icon("chev", 18, MUTED)}</a></sc-if>'''
        key = g.split()[0]
        secs += f'''<sc-if value="[[ g{key} ]]" hint-placeholder-val="[[ true ]]"><section style="display: flex; flex-direction: column; gap: 8px">
        <span style="display: flex; justify-content: space-between; align-items: baseline; padding: 0 2px"><span style="font-size: 17px; font-weight: 600">{g}</span><span style="font-size: 13px; color: {MUTED}">{GROUP_NOTE[g]}</span></span>
        <div style="border-radius: {R_L}px; background: #FFFFFF; padding: 0 14px; margin-top: -1px; overflow: hidden"><div style="margin-top: -1px">{rows}</div></div></section></sc-if>'''
    body = f'''    {head9('R8-Hub.dc.html', 'All tools')}
    <p style="font-size: 15px; line-height: 1.45; color: {SEC}">Every tool, grouped by the job it does. Each works out your own numbers the same way every time, and none picks a product for you.</p>
    {seg('md', ['Everything', 'Me', 'My business'], 'Show tools for')}
    <span style="font-size: 14px; color: {SEC}; margin-bottom: -6px">[[ countTxt ]]</span>
    {secs}'''
    modes = [x[6] for x in ALL]
    groups = [x[0].split()[0] for x in ALL]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const md = st.md || 0, modes = %(modes)s, groups = %(groups)s;
    const vis = (i) => md === 0 || (md === 1 && modes[i].indexOf('m') >= 0) || (md === 2 && modes[i].indexOf('b') >= 0);
    const v = {};
    modes.forEach((_, i) => { v['t' + i] = vis(i); });
    ['Understand', 'Plan', 'Grow', 'Run', 'Stay'].forEach((g) => { v['g' + g] = groups.some((x, i) => x === g && vis(i)); });
    const n = modes.filter((_, i) => vis(i)).length;
    v.countTxt = n + ' tools' + (md === 0 ? '' : md === 1 ? ' for your own money' : ' for your business');
%(seg)s
    return v;
  }
}''' % dict(modes=js(modes), groups=js(groups), seg=seg_js('md', 3, 'md'))
    return page9('All tools', body, logic, h=2080, tab='Hub')


BOARDS = [('R9-Hub-All', all_tools), ('R9-Tool-Remit', remit), ('R9-Tool-Loan', loan), ('R9-Tool-Offers', offers), ('R9-Tool-Pension', pension),
          ('R9-Tool-Owe', owe), ('R9-Group-Book', group_book), ('R9-Tool-Worth', worth), ('R9-Tool-Setup', setup)]
