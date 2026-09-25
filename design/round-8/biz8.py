"""Round 8, batch 3: the business tools, for Wanjiru's Homeware (a market stall in Nairobi, in shillings).
Writes R8-Tool-Price, R8-Tool-Invoice, R8-Shop-Edit and R8-Shop-Public.

Shop is the safe version (Q-35): a catalogue and a link, orders go to her WhatsApp, and no payments pass through AWO."""
import json

from lib8 import *  # noqa: F401,F403
from tools8 import tool_page, beat, means, learn_this, make_goal, milestone, foot, result, SHARE_JS, TOOL_CSS, REVIEWED  # noqa: F401
from learn8 import PHONE_CSS

BACK = 'R8-Hub-Biz.dc.html'
STALL = IMG['wanjiru_stall']  # 1100 x 733


def ksh(n):
    return f'KSh{NB}' + f'{n:,}'.replace(',', NB)


def ksh_js():
    return "const K = (n) => 'KSh\\u00a0' + Math.round(n).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, '\\u00a0');"


def crop(x0, y0, s, w, h=None, radius=R_M, alt=''):
    """A real product, cut from Wanjiru's stall photo: region (x0, y0) of side s, shown at w by h."""
    h = h or w
    k = w / s
    return (f'<span role="img" aria-label="{alt}" style="position: relative; display: block; width: {w}px; height: {h}px; flex-shrink: 0; border-radius: {radius}px; overflow: hidden; background: {MIST}">'
            f'<img src="{STALL}" alt="" style="position: absolute; left: {-x0 * k:.0f}px; top: {-y0 * k:.0f}px; width: {1100 * k:.0f}px; max-width: none; filter: brightness(1.55) contrast(1.08) saturate(1.1)"></span>')


PRODUCTS = [('Woven basket, medium', 1100, (238, 130, 210), 'Sisal, dyed by hand. About 30 cm across.', True),
            ('Clay vase', 1450, (40, 188, 220), 'Fired clay, hand-painted. About 25 cm tall.', True),
            ('Carved figures, set of three', 2200, (8, 372, 230), 'Carved wood, each about 20 cm.', False)]


# ---------------------------------------------------------------- Price it right

COSTS = [('Sisal and dye', 360, 'For one basket'), ('Your time', 300, 'Two hours at KSh 150'), ('Stall and transport', 110, 'KSh 6 000 a month, over about 55 baskets')]


def price():
    rows = ''.join(f'<div style="min-height: 56px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {MUTED}">{d}</span></span><span style="font-size: 15px; font-weight: 600; font-variant-numeric: tabular-nums">{ksh(v)}</span></div>' for i, (n, v, d) in enumerate(COSTS))
    body = f'''    {beat("Your numbers", "calc")}
    <section class="card8" style="gap: 4px">
      <div style="display: flex; gap: 12px; align-items: center; padding-bottom: 10px">{crop(238, 130, 210, 56, alt='A woven basket')}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Woven basket, medium</span><span style="font-size: 13px; color: {MUTED}">You charge {ksh(925)} today</span></span></div>
      <div style="display: flex; flex-direction: column; border-top: 1px solid {LINE7}">{rows}</div>
      <div style="min-height: 52px; display: flex; align-items: center; justify-content: space-between; border-top: 2px solid {INK}; font-size: 16px; font-weight: 600"><span>What one basket costs you</span><span>{ksh(770)}</span></div>
    </section>
    <section class="card8">
      <span style="display: flex; justify-content: space-between; align-items: baseline"><label for="pr-m" style="font-size: 16px; font-weight: 600">How much of each sale to keep</label><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">[[ mTxt ]]</span></span>
      <input id="pr-m" class="rng8" type="range" min="15" max="50" step="5" value="[[ m ]]" onInput="[[ setM ]]" style="--p: [[ mP ]]%">
    </section>
    {result('Charge', 'price', 'priceSub', f'<div role="img" aria-label="[[ barLabel ]]" style="display: flex; height: 44px; margin-top: 8px; border-radius: {R_S}px; overflow: hidden"><span style="width: [[ costW ]]%; background: {EVG}; color: #FFFFFF; font-size: 13px; font-weight: 600; display: flex; align-items: center; padding-left: 10px; transition: width .45s cubic-bezier(.2,.8,.2,1)">Cost, [[ costTxt ]]</span><span style="flex-grow: 1; background: #FFFFFF; font-size: 13px; font-weight: 600; display: flex; align-items: center; padding-left: 10px">Yours</span></div>')}
    <section class="card8" style="gap: 14px">
      <span style="font-size: 16px; font-weight: 600">Markup is not margin</span>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 12px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px; color: {MUTED}">Markup today</span><span style="font-size: 28px; font-weight: 600; letter-spacing: -0.03em">20%</span><span style="font-size: 13px; line-height: 1.35; color: {SEC}">Added on top of {ksh(770)}</span></div>
        <div style="border-radius: {R_M}px; background: {WARN_BG}; color: {WARN_FG}; padding: 12px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px">Margin today</span><span style="font-size: 28px; font-weight: 600; letter-spacing: -0.03em">17%</span><span style="font-size: 13px; line-height: 1.35">What you keep of {ksh(925)}</span></div>
      </div>
    </section>
    <section class="card8" style="gap: 8px">
      <span style="font-size: 16px; font-weight: 600">Covering the stall</span>
      <p style="font-size: 16px; line-height: 1.45">At [[ price ]], the stall's {ksh(6000)} a month is covered after <b>[[ be ]] baskets</b>. At today's {ksh(925)}, it takes 23.</p>
      <span style="font-size: 13px; color: {MUTED}">Each basket's own costs are sisal, dye and your time: {ksh(660)}.</span>
    </section>
    {means("Markup is what you add to the cost. Margin is the part of the price you keep. A 20% markup keeps only 17%, which is why prices that feel fair can still leave nothing over.")}
    {learn_this('Pricing for profit', 5, ['Markup', 'Margin', 'Break-even'])}
    {make_goal('Business stock: KSh 20 000 by March', 'Sisal and clay for the December rush', 'R8-Goals.dc.html', 'shop', 'Make it')}
    {milestone("Wanjiru's first month in profit.", 'Side hustles circle', 'wanjiru')}
    {foot("Price it right, version 0.1. Your own costs; the tool never compares you with other sellers.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(K)s
    const m = st.m == null ? 30 : st.m, cost = 770, own = 660;
    const p = Math.ceil(cost / (1 - m / 100) / 10) * 10;
    return { %(share)s
      m, mTxt: m + '%%', mP: Math.round((m - 15) / 0.35), setM: (e) => this.setState({ m: +e.target.value }),
      price: K(p), priceSub: 'to keep ' + m + '%% of every sale: ' + K(p - cost) + ' a basket.', keep: K(p - cost),
      costW: Math.round(cost / p * 100), costTxt: K(cost), barLabel: 'Of ' + K(p) + ', ' + K(cost) + ' is cost and ' + K(p - cost) + ' is yours', be: Math.ceil(6000 / (p - own))
    };
  }
}''' % dict(K=ksh_js(), share=SHARE_JS)
    return tool_page('Price it right', body, logic, h=2230, mode='My business', back=BACK)


# ---------------------------------------------------------------- Quotes and invoices

ITEMS = [('Woven basket, medium', 6, 1100), ('Clay vase', 2, 1450), ('Delivery in Nairobi', 1, 300)]
OWED = [('Achieng', 'INV-019', 4300, 'Nine days late', True), ('Pendo', 'INV-021', 5000, 'Due in three days', False)]


def doc_face(kind):
    """One side of the document: the quote, or the invoice it became."""
    is_inv = kind == 'invoice'
    lines = ''.join(f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) 36px 88px; gap: 8px; min-height: 36px; align-items: center; font-size: 14px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span>{n}</span><span style="color: {MUTED}; text-align: right">{"" if q == 1 else "×" + str(q)}</span><span style="text-align: right; font-weight: 600; font-variant-numeric: tabular-nums">{ksh(q * p)}</span></div>' for i, (n, q, p) in enumerate(ITEMS))
    total = sum(q * p for _n, q, p in ITEMS)
    label, num, dates = ('Invoice', 'INV-022', 'Due 9 Oct 2026') if is_inv else ('Quote', 'Q-014', 'Valid until 9 Oct 2026')
    status = (f'<span class="chip" style="background: {WARN_BG}; color: {WARN_FG}">Unpaid</span>' if is_inv else f'<span class="chip" style="background: {MIST}; color: {SEC}">Draft</span>')
    cls, hidden = ('face-b', '[[ notInv ]]') if is_inv else ('face-f', '[[ inv ]]')
    return f'''<section class="{cls}" aria-hidden="{hidden}" style="border-radius: {R_L}px; background: #FFFFFF; padding: 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; box-shadow: 0 1px 0 #DCE4DF">
          <div style="display: flex; justify-content: space-between; align-items: flex-start">
            <span style="display: flex; align-items: center; gap: 10px"><span style="width: 40px; height: 40px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">WH</span><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Wanjiru's Homeware</span><span style="font-size: 12px; color: {MUTED}">Market stall, Nairobi</span></span></span>
            <span style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px"><span class="d" style="font-size: 26px">{label}</span><span style="font-size: 13px; color: {MUTED}">{num}</span></span>
          </div>
          <div style="display: flex; justify-content: space-between; gap: 8px; font-size: 13px; color: {SEC}"><span>For <b style="color: {INK}; font-weight: 600">Achieng Otieno</b>, Kilimani</span><span>{dates}</span></div>
          <div style="border-top: 1px solid {INK}; padding-top: 2px">{lines}</div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; border-top: 2px solid {INK}; padding-top: 10px"><span style="font-size: 15px; font-weight: 600">Total</span><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.02em">{ksh(total)}</span></div>
          <div style="display: flex; justify-content: space-between; align-items: center; gap: 8px"><span style="font-size: 12px; line-height: 1.4; color: {MUTED}">No VAT: not registered. Pay by M-Pesa till 123 456 (sample).</span>{status}</div>
        </section>'''


def invoice():
    tabs = ''.join(f'<button role="tab" onClick="[[ tb{j} ]]" aria-selected="[[ tbOn{j} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ tbBg{j} ]]; color: [[ tbFg{j} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{t}</button>' for j, t in enumerate(['Quotes', 'Invoices', 'Who owes me']))
    owed = ''
    for i, (n, num, amt, when, late) in enumerate(OWED):
        owed += f'''<div style="padding: 12px 0; display: flex; flex-direction: column; gap: 10px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <div style="display: flex; align-items: center; gap: 12px"><span style="width: 40px; height: 40px; border-radius: 999px; background: {BLUSH if late else MIST}; color: {BLUSH_INK if late else EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">{n[0]}</span>
            <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}, {num}</span><span style="font-size: 13px; color: {WARN_FG if late else MUTED}">{when}</span></span>
            <span style="font-size: 16px; font-weight: 600; font-variant-numeric: tabular-nums">[[ amt{i} ]]</span></div>
          <div style="display: flex; gap: 8px; padding-left: 52px">
            <sc-if value="[[ unpaid{i} ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ remind{i} ]]" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">A polite reminder</button><button onClick="[[ paid{i} ]]" style="height: 44px; padding: 0 12px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 14px; font-weight: 600">Mark paid</button></sc-if>
            <sc-if value="[[ isPaid{i} ]]" hint-placeholder-val="[[ false ]]"><span class="chip" style="background: {EVG}; color: #FFFFFF; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 14, '#FFFFFF', 2.6)}Paid</span></sc-if>
          </div></div>'''
    inv_list = ''.join(f'<div style="min-height: 56px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {MUTED}">{num}</span></span><span style="font-size: 15px; font-weight: 600">{ksh(a)}</span><span class="chip" style="background: {bg}; color: {fg}">{s}</span></div>'
                       for i, (n, num, a, s, bg, fg) in enumerate([('Achieng', 'INV-019', 4300, 'Late', WARN_BG, WARN_FG), ('Mama Njeri', 'INV-020', 3300, 'Paid', EVG, '#FFFFFF'), ('Pendo', 'INV-021', 5000, 'Unpaid', MIST, SEC)]))
    body = f'''    <div role="tablist" aria-label="Quotes and invoices" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: #FFFFFF">{tabs}</div>
    <sc-if value="[[ t0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 14px; animation: fadeIn .25s ease-out both">
      {beat("Your numbers", "calc")}
      <div style="position: relative; height: 350px; perspective: 1600px">
        <div class="flipper" style="transform: [[ flipTf ]]">{doc_face('quote')}{doc_face('invoice')}</div>
      </div>
      <sc-if value="[[ notInv ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 8px">
        <button onClick="[[ convert ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{icon('flip', 18, '#FFFFFF')}Achieng said yes: make it an invoice</button>
        <span style="font-size: 13px; color: {MUTED}; text-align: center">One tap. The items, prices and customer carry over.</span></div></sc-if>
      <sc-if value="[[ inv ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 8px; animation: rise .3s cubic-bezier(.2,.8,.2,1) .35s both">
        <sc-if value="[[ notSent ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; gap: 8px"><button onClick="[[ send ]]" style="flex: 1.4 1 0; height: 56px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('whatsapp', 20, '#FFFFFF')}Send by WhatsApp</button><button onClick="[[ send ]]" style="flex: 1 1 0; height: 56px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; background: #FFFFFF; font-size: 15px; font-weight: 600">Email a PDF</button></div></sc-if>
        <sc-if value="[[ sent ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="flex-direction: row; align-items: center; gap: 12px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 20, EVG, 2.8)}</span><span style="font-size: 15px; line-height: 1.4">Sent to Achieng. It sits in Who owes me until it's paid.</span></section></sc-if>
      </div></sc-if>
    </div></sc-if>
    <sc-if value="[[ t1 ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="gap: 4px; animation: fadeIn .25s ease-out both">
      <sc-if value="[[ inv ]]" hint-placeholder-val="[[ false ]]"><div style="min-height: 56px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid {LINE7}"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Achieng</span><span style="font-size: 13px; color: {MUTED}">INV-022, new</span></span><span style="font-size: 15px; font-weight: 600">{ksh(9800)}</span><span class="chip" style="background: {MIST}; color: {SEC}">Unpaid</span></div></sc-if>
      {inv_list}</section></sc-if>
    <sc-if value="[[ t2 ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: fadeIn .25s ease-out both">
      {result('Owed to you', 'owed', 'owedSub')}
      <section class="card8" style="gap: 0; padding-top: 4px; padding-bottom: 4px">{owed}</section>
      <sc-if value="[[ reminding ]]" hint-placeholder-val="[[ false ]]"><section class="card8" style="box-shadow: inset 0 0 0 2px {EVG}; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
        <span style="font-size: 16px; font-weight: 600">Your reminder to Achieng</span>
        <p style="border-radius: {R_M}px {R_M}px {R_M}px {R_S}px; background: {MIST}; padding: 12px 14px; font-size: 15px; line-height: 1.5">Hi Achieng, a gentle reminder about invoice INV-019 for {ksh(4300)}, due on 16 September. My M-Pesa till is 123 456. Thank you! Wanjiru</p>
        <span style="font-size: 13px; color: {MUTED}">Written for you. Change anything before you send it.</span>
        <sc-if value="[[ notReminded ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ sendReminder ]]" style="height: 52px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('whatsapp', 20, '#FFFFFF')}Send by WhatsApp</button></sc-if>
        <sc-if value="[[ reminded ]]" hint-placeholder-val="[[ false ]]"><span style="height: 52px; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600">{icon('check', 20, EVG, 2.8)}Reminder sent.</span></sc-if>
      </section></sc-if>
      {means("Most late payments are forgotten, not refused. A friendly reminder on the day after it's due gets most invoices paid.")}
      {learn_this('Getting paid on time', 4, ['Invoice', 'Quote', 'Payment terms'])}
      {make_goal("A month's float: KSh 30 000", 'So a late payer never stops the stall', 'R8-Goals.dc.html', 'pool', 'Open')}
      {milestone("Wanjiru's customers all paid this month.", 'Side hustles circle', 'wanjiru')}
    </div></sc-if>
    {foot("Quotes and invoices, version 0.1. Templates to be reviewed per country. A VAT line appears only if she's registered (in Kenya, at KSh 5 million a year). AWO never handles the payment.")}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(K)s
    const t = st.t == null ? 0 : st.t, inv = !!st.inv, sent = !!st.sent, paid = st.paid || [false, false];
    const AMT = [4300, 5000];
    let owed = AMT.reduce((a, x, i) => a + (paid[i] ? 0 : x), 0) + (sent ? 9800 : 0);
    const n = paid.filter((p) => !p).length + (sent ? 1 : 0);
    const v = { %(share)s
      t0: t === 0, t1: t === 1, t2: t === 2, inv, notInv: !inv, sent, notSent: !sent,
      flipTf: inv ? 'rotateY(180deg)' : 'rotateY(0deg)',
      convert: () => this.setState({ inv: true }), send: () => this.setState({ sent: true }),
      owed: K(owed), owedSub: owed ? 'on ' + n + (n === 1 ? ' invoice' : ' invoices') + (paid[0] ? '.' : ". Achieng's first one is nine days late.") : 'Everyone has paid. Nicely run.',
      reminding: !!st.reminding, reminded: !!st.reminded, notReminded: !st.reminded, sendReminder: () => this.setState({ reminded: true })
    };
    for (let j = 0; j < 3; j++) { v['tb' + j] = () => this.setState({ t: j }); v['tbOn' + j] = t === j; v['tbBg' + j] = t === j ? '%(evg)s' : 'transparent'; v['tbFg' + j] = t === j ? '#FFFFFF' : '%(ink)s'; }
    for (let i = 0; i < 2; i++) {
      v['amt' + i] = K(AMT[i]); v['unpaid' + i] = !paid[i]; v['isPaid' + i] = paid[i];
      v['paid' + i] = () => { const p = paid.slice(); p[i] = true; this.setState({ paid: p }); };
      v['remind' + i] = () => this.setState({ reminding: true, reminded: false });
    }
    return v;
  }
}''' % dict(K=ksh_js(), share=SHARE_JS, evg=EVG, ink=INK)
    return tool_page('Quotes and invoices', body, logic, h=1900, mode='My business', back=BACK)


# ---------------------------------------------------------------- Shop: the editor

RULES = ['Sell what you make or stock yourself.', 'No money products: no loans, "investments", savings schemes or crypto.', 'No recruiting: no "join my team" or pay-to-join.',
         'Buyers pay you directly. AWO doesn\'t handle payments or deliveries.']


def shop_edit():
    prods = ''.join(f'''<div style="min-height: 76px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        {crop(*box, 56, alt=n)}
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0"><span style="font-size: 15px; font-weight: 600">{n}</span><span style="font-size: 14px; color: {SEC}">{ksh(p)}</span><span style="font-size: 12px; color: [[ stkFg{i} ]]">[[ stk{i} ]]</span></span>
        {switch(i, 'In stock: ' + n)}</div>''' for i, (n, p, box, _d, _s) in enumerate(PRODUCTS))
    rules = ''.join(f'<span style="display: flex; gap: 10px; font-size: 14px; line-height: 1.45"><span aria-hidden="true" style="width: 6px; height: 6px; flex-shrink: 0; margin-top: 8px; border-radius: 999px; background: {EVG}"></span>{r}</span>' for r in RULES)
    body = f'''    <section style="border-radius: {R_L}px; background: #FFFFFF; overflow: hidden">
      <div style="position: relative; height: 120px; overflow: hidden"><img src="{STALL}" alt="Wanjiru's stall" style="width: 100%; height: 100%; object-fit: cover; object-position: 30% 40%"></div>
      <div style="padding: 0 16px 16px; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: flex-end; gap: 12px; margin-top: -28px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 64px; height: 64px; box-shadow: 0 0 0 4px #FFFFFF"><span class="chip" style="margin-bottom: 4px; background: [[ liveBg ]]; color: [[ liveFg ]]">[[ liveTxt ]]</span></div>
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">Wanjiru's Homeware</span><span style="font-size: 14px; color: {MUTED}">Handmade baskets, vases and carvings. Market stall, Nairobi.</span></span>
        <div style="display: flex; gap: 8px; align-items: center"><span style="flex-grow: 1; min-height: 44px; border-radius: {R_M}px; background: {MIST}; padding: 0 12px; display: flex; align-items: center; font-size: 14px; color: {SEC}">awo.africa/s/wanjiru</span><button aria-label="Share your shop link" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic8('share', 20, '#FFFFFF')}</button></div>
        <span style="font-size: 12px; color: {MUTED}">A sample link. The web address is not decided.</span>
      </div>
    </section>
    <section class="card8" style="gap: 4px">
      <span style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px"><span style="font-size: 16px; font-weight: 600">Products</span><span style="font-size: 13px; color: {MUTED}">In stock</span></span>
      <div>{prods}</div>
      <button style="margin-top: 8px; height: 52px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1.5px #C9D3CE; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('camera', 20, EVG)}Add a product: start with a photo</button>
    </section>
    <section class="card8" style="gap: 0; padding-top: 6px; padding-bottom: 6px">
      <div style="min-height: 60px; display: flex; align-items: center; gap: 12px"><span style="width: 36px; height: 36px; border-radius: {R_M}px; background: {MIST}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8('whatsapp', 20)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Orders come to your WhatsApp</span><span style="font-size: 13px; color: {MUTED}">+254 712 345 678</span></span></div>
      <div style="min-height: 60px; display: flex; align-items: center; gap: 12px; border-top: 1px solid {LINE7}"><span style="width: 36px; height: 36px; border-radius: {R_M}px; background: {MIST}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8('home', 20)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Pick-up or delivery</span><span style="font-size: 13px; color: {MUTED}">At the stall, or in Nairobi for {ksh(300)}</span></span></div>
      <div style="min-height: 60px; display: flex; align-items: center; gap: 12px; border-top: 1px solid {LINE7}"><span style="width: 36px; height: 36px; border-radius: {R_M}px; background: {BLUSH}; color: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('ripple', 20)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Show it in Community</span><span style="font-size: 13px; color: {MUTED}">As a "Shop local" card in the feed</span></span>{switch(3, 'Show my shop in Community')}</div>
    </section>
    <section class="card8" style="box-shadow: inset 0 0 0 2px {EVG}">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 600">Seller rules</span>{sample_chip()}</span>
      {rules}
      <button role="checkbox" aria-checked="[[ agreed ]]" onClick="[[ agree ]]" style="min-height: 52px; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; font-weight: 600"><span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: {R_S}px; background: [[ agreeBg ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center">{icon('check', 16, '#FFFFFF', 3)}</span>I'll sell by these rules</button>
      <sc-if value="[[ canPublish ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ publish ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600">Publish my shop</button></sc-if>
      <sc-if value="[[ cantPublish ]]" hint-placeholder-val="[[ true ]]"><span style="height: 56px; border-radius: {R_M}px; background: #DCE4DF; color: {MUTED}; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center">[[ pubLabel ]]</span></sc-if>
      <span style="font-size: 13px; line-height: 1.45; color: {MUTED}">Members can report a shop; a person at AWO reviews every report. Rules, payments and seller terms are still open (Q-35).</span>
    </section>
    <a href="R8-Shop-Public.dc.html" style="height: 52px; border-radius: {R_M}px; background: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('eye', 20, EVG)}See it as a buyer</a>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%(sw)s
    for (let i = 0; i < 3; i++) { v['stk' + i] = v['sw' + i] ? 'In stock' : 'Sold out: still shown, marked sold out'; v['stkFg' + i] = v['sw' + i] ? '%(muted)s' : '%(wine)s'; }
    const agreed = !!st.agreed, live = !!st.live;
    v.agreed = agreed; v.agreeBg = agreed ? '%(evg)s' : '#FFFFFF'; v.agree = () => this.setState({ agreed: !agreed });
    v.canPublish = agreed && !live; v.cantPublish = !agreed || live; v.pubLabel = live ? 'Your shop is live' : 'Publish my shop';
    v.publish = () => this.setState({ live: true });
    v.liveTxt = live ? 'Live' : 'Draft'; v.liveBg = live ? '%(lime)s' : '%(mist)s'; v.liveFg = live ? '%(evg)s' : '%(sec)s';
    return v;
  }
}''' % dict(sw=switch_js(4, [True, True, False, True]), muted=MUTED, wine=WARN_FG, evg=EVG, lime=LIME, mist=MIST, sec=SEC)
    html = tool_page('Your shop', body, logic, h=2020, mode='My business', back=BACK)
    return html


# ---------------------------------------------------------------- Shop: the public page

def shop_public():
    cards = ''.join(f'''<button onClick="[[ pick{i} ]]" style="border-radius: {R_L}px; background: #FFFFFF; overflow: hidden; display: flex; flex-direction: column; text-align: left; position: relative">
        {crop(*box, 169, 150, 0, alt=n)}
        {"" if s else f'<span class="chip" style="position: absolute; left: 10px; top: 10px; background: {INK}; color: #FFFFFF">Sold out</span>'}
        <span style="padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 14px; font-weight: 600; line-height: 1.3">{n}</span><span style="font-size: 15px; font-weight: 600; color: {EVG}">{ksh(p)}</span></span></button>''' for i, (n, p, box, _d, s) in enumerate(PRODUCTS))
    sheets = ''.join(f'''<sc-if value="[[ sh{i} ]]" hint-placeholder-val="[[ false ]]">
      <div style="position: absolute; inset: 0; z-index: 20; background: rgba(11,15,14,.5); animation: fadeIn .2s ease-out both">
        <div role="dialog" aria-label="{n}" style="position: absolute; left: 0; right: 0; bottom: 0; border-radius: {R_L}px {R_L}px 0 0; background: #FFFFFF; padding: 16px 20px 28px; display: flex; flex-direction: column; gap: 14px; animation: sheetUp .3s cubic-bezier(.2,.8,.2,1) both">
          <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 18px; font-weight: 600">{n}</span><button onClick="[[ closeSheet ]]" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</button></div>
          {crop(max(0, box[0] - 70), max(0, box[1] - 30), box[2] + 140, 350, 220, R_M, alt=n)}
          <span style="font-size: 15px; line-height: 1.45; color: {SEC}">{d}</span>
          <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em">[[ lineTotal ]]</span>
            <span style="display: flex; align-items: center; gap: 6px"><button onClick="[[ qDown ]]" aria-label="One fewer" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MIST}; font-size: 22px">−</button><span style="min-width: 32px; text-align: center; font-size: 18px; font-weight: 600">[[ q ]]</span><button onClick="[[ qUp ]]" aria-label="One more" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MIST}; font-size: 22px">+</button></span></div>
          <sc-if value="[[ notDrafted ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ order ]]" style="height: 56px; width: 100%; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 16px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px">{ic8('whatsapp', 20, '#FFFFFF')}Order on WhatsApp</button></sc-if>
          <sc-if value="[[ drafted ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 8px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both"><span style="font-size: 13px; color: {MUTED}">Opens WhatsApp with this message. Nothing is sent until you press send there.</span><p style="border-radius: {R_M}px {R_M}px {R_S}px {R_M}px; background: #DDF3D0; padding: 12px 14px; font-size: 15px; line-height: 1.45">[[ message ]]</p></div></sc-if>
        </div>
      </div>
    </sc-if>''' for i, (n, _p, box, d, _s) in enumerate(PRODUCTS))
    body = f'''  <div class="scr" style="bottom: 0; padding-top: 16px; gap: 16px">
    <div style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; color: {MUTED}"><span style="display: flex; align-items: center; gap: 6px">{icon('stones', 16, EVG)}A shop on AWO</span>{sample_chip()}</div>
    <section style="border-radius: {R_L}px; background: #FFFFFF; overflow: hidden">
      <div style="height: 150px; overflow: hidden"><img src="{STALL}" alt="Wanjiru at her stall" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%"></div>
      <div style="padding: 0 16px 16px; display: flex; flex-direction: column; gap: 8px">
        <img class="face" src="{IMG['wanjiru']}" alt="" style="width: 64px; height: 64px; margin-top: -30px; box-shadow: 0 0 0 4px #FFFFFF">
        <span class="d" style="font-size: 32px">Wanjiru's Homeware</span>
        <span style="font-size: 15px; line-height: 1.45; color: {SEC}">Handmade baskets, vases and carvings. Pick up at the stall, or delivery in Nairobi for {ksh(300)}.</span>
      </div>
    </section>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">{cards}</div>
    <section style="border-radius: {R_L}px; background: {MIST}; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 14px; line-height: 1.5; color: {SEC}">AWO lists this shop for its member. Payment and delivery are between you and Wanjiru.</span>
      <button onClick="[[ report ]]" style="align-self: flex-start; min-height: 44px; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: {WARN_FG}">{ic8('flag', 18, WARN_FG)}[[ reportLabel ]]</button>
    </section>
  </div>
  {sheets}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    %(K)s
    const P = %(prods)s;
    const sh = st.sh == null ? -1 : st.sh, q = st.q || 1, drafted = !!st.drafted;
    const v = {
      q, qDown: () => this.setState({ q: Math.max(1, q - 1) }), qUp: () => this.setState({ q: q + 1 }),
      closeSheet: () => this.setState({ sh: -1 }), drafted, notDrafted: !drafted, order: () => this.setState({ drafted: true }),
      lineTotal: sh >= 0 ? K(P[sh][1] * q) : '',
      message: sh >= 0 ? 'Hi Wanjiru, I\\'d like ' + q + ' × ' + P[sh][0] + ' (' + K(P[sh][1] * q) + ') from your shop on AWO. Pick-up or delivery? Thank you!' : '',
      report: () => this.setState({ reported: true }), reportLabel: st.reported ? 'Reported. A person at AWO will look at it.' : 'Report this shop'
    };
    for (let i = 0; i < 3; i++) { v['sh' + i] = sh === i; v['pick' + i] = () => this.setState({ sh: i, q: 1, drafted: false }); }
    return v;
  }
}''' % dict(K=ksh_js(), prods=json.dumps([[n, p] for n, p, _b, _d, _s in PRODUCTS], ensure_ascii=False))
    return with_css(phone("Wanjiru's Homeware", body, logic, h=1140), PHONE_CSS + TOOL_CSS)


BOARDS = [('R8-Tool-Price', price), ('R8-Tool-Invoice', invoice), ('R8-Shop-Edit', shop_edit), ('R8-Shop-Public', shop_public)]
