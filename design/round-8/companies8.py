"""Round 8, batch 5: Companies explained, in Learn (night). The safe version of Q-36: editorial, never an invitation
to invest. Writes R8-Companies (the path, with AWO's proposed editorial rules), R8-Company-Brief (one listed company,
explained from its own results) and R8-Startup (how a sample startup raises money, and what happens to the founders' slice).

The brief uses a real company to test the format. Its figures come from Safaricom's results for the year to
31 March 2025. Whether AWO features real companies, and how, is still Q-36."""
import json

from lib8 import *  # noqa: F401,F403
from learn8 import PHONE_CSS, ola_pill, chip_dark, REVIEWED_D

EXTRA8.update({
    'phone': '<rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18.5h2"></path>',
    'cart': '<path d="M3 4h2.5l2.2 11h10.6l2-8H7"></path><circle cx="9.5" cy="19" r="1.4"></circle><circle cx="17" cy="19" r="1.4"></circle>',
    'rocket': '<path d="M12 3c3.5 2.2 5 6 4.4 10.5L12 17l-4.4-3.5C7 9 8.5 5.2 12 3z"></path><circle cx="12" cy="9.5" r="1.8"></circle><path d="M7.6 13.5 5 16l.5 3.5 3.5-1.2M16.4 13.5 19 16l-.5 3.5-3.5-1.2"></path>',
})
CO_CSS = """
.bul{display:flex;gap:12px;font-size:16px;line-height:1.5}
.bul::before{content:"";width:8px;height:8px;flex-shrink:0;margin-top:8px;border-radius:2px;background:#D8F36A}
@keyframes seg{from{stroke-dasharray:0 100}}
"""
SOURCE = "Safaricom results for the year to 31 March 2025"


def co_head(back, label, chip_bg=MINT, chip_fg=NIGHT, save=True):
    right = (f'<button onClick="[[ toggleSave ]]" aria-pressed="[[ saved ]]" aria-label="Save" style="width: 44px; height: 44px; border-radius: {R_M}px; background: [[ saveBg ]]; color: [[ saveFg ]]; display: flex; align-items: center; justify-content: center; transition: background-color .18s">{ic8("bookmark", 20)}</button>' if save else '')
    return (f'<header style="display: flex; align-items: center; gap: 10px">'
            f'<a href="{back}" aria-label="Back" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic("back", 20, MOON, 2.2)}</a>'
            f'<span class="chip" style="background: {chip_bg}; color: {chip_fg}">{ic8("building", 14, chip_fg, 2.2)}{label}</span><span style="flex-grow: 1"></span>{right}</header>')


SAVE_JS = """    const saved = !!st.saved;
    v.saved = saved; v.toggleSave = () => this.setState({ saved: !saved }); v.saveBg = saved ? '%s' : '%s'; v.saveFg = saved ? '%s' : '%s';""" % (LIME, RAISED, EVG, MOON)


def rules_card():
    rules = ['A company is chosen because it teaches something, never because it looks like a good buy.',
             'Every brief says what could go wrong.',
             'No share prices, no charts of returns, no buttons to buy and no links to trading platforms.',
             "Facts come from the company's own reports, with their date, and a second editor checks them.",
             'Nobody pays to appear. If that ever changed, it would be labelled and kept out of Learn.',
             "Companies don't see a brief before it's published."]
    items = ''.join(f'<span class="bul">{r}</span>' for r in rules)
    return (f'<section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 12px">'
            f'<span style="display: flex; justify-content: space-between; align-items: center; gap: 8px"><span style="font-size: 17px; font-weight: 600">How AWO chooses and writes these</span>{chip_dark("Proposal, Q-36")}</span>{items}</section>')


# ---------------------------------------------------------------- the path

SERIES = [('full', 'How a company makes money', '4 min', 'R7-Lesson.dc.html'), ('half', 'Revenue, profit and cash: not the same thing', '5 min', 'R7-Lesson.dc.html'),
          ('new', 'What an IPO is', '4 min', 'R7-Lesson.dc.html'), ('new', 'How a startup raises money', '5 min', 'R8-Startup.dc.html')]
WORDS = ['Revenue', 'Profit', 'Margin', 'IPO', 'Valuation', 'Dividend']


def companies():
    series = ''.join(f'''<a href="{href}" style="min-height: 60px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + NLINE + ";" if i else ""}">
          {moon(24, p, now=(p == 'half'))}<span style="flex-grow: 1; font-size: 15px; font-weight: {600 if p == 'half' else 500}; line-height: 1.3">{t}</span><span style="flex-shrink: 0; white-space: nowrap; font-size: 13px; color: {NMUTED}">{m}</span></a>''' for i, (p, t, m, href) in enumerate(SERIES))
    words = ''.join(f'<a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {RAISED}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{icon("arch", 16, LIME)}{w}</a>' for w in WORDS)
    body = f'''  <div class="scr" style="gap: 18px">
    {co_head('R8-Learn.dc.html', 'Companies explained')}
    <div style="display: flex; flex-direction: column; gap: 10px">
      <h1 class="d" style="font-size: 44px">Companies explained</h1>
      <p style="font-size: 16px; line-height: 1.45; color: {NMUTED}">How companies make money, what an IPO is, and why most startups never make it. Education, never a tip.</p>
    </div>
    <section style="border-radius: {R_L}px; box-shadow: inset 0 0 0 1.5px {MINT}; padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start">
      <span style="color: {MINT}; padding-top: 2px">{ic('shield', 20, MINT)}</span>
      <span style="font-size: 15px; line-height: 1.45">AWO isn't paid to feature any company, and never tells you to buy a share.</span>
    </section>
    <span style="font-size: 17px; font-weight: 600; margin-top: 2px">Start here</span>
    <div style="border-radius: {R_L}px; background: {RAISED}; padding: 0 16px; display: flex; flex-direction: column; margin-top: -8px">{series}</div>
    <span style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 2px"><span style="font-size: 17px; font-weight: 600">Company briefs</span><span style="font-size: 13px; color: {NMUTED}">One company, five minutes</span></span>
    <a href="R8-Company-Brief.dc.html" style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 12px; margin-top: -8px; box-shadow: inset 0 0 0 1.5px {LIME}">
      <span style="display: flex; align-items: center; gap: 10px"><span style="width: 44px; height: 44px; border-radius: {R_M}px; background: {MINT}; color: {NIGHT}; display: flex; align-items: center; justify-content: center">{ic8('phone', 22)}</span>
        <span style="display: flex; gap: 6px; flex-wrap: wrap"><span class="chip" style="background: {RAISED}; color: {MOON}">Listed in Nairobi</span><span class="chip" style="background: {RAISED}; color: {MOON}">Five minutes</span></span></span>
      <span class="d" style="font-size: 26px">Safaricom: how a phone company became a money company</span>
      <span style="font-size: 15px; line-height: 1.45; color: {NMUTED}">M-Pesa now brings in more than calls do. What that means, and what could go wrong.</span>
      <span style="display: flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 600; color: {LIME}">Read the brief{icon('chev', 16, LIME)}</span>
    </a>
    <a href="R8-Startup.dc.html" style="border-radius: {R_L}px; background: {DEEP}; padding: 16px 18px; display: flex; align-items: center; gap: 12px">
      <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {IRIS}; color: {NIGHT}; display: flex; align-items: center; justify-content: center">{ic8('rocket', 22)}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 16px; font-weight: 600">A startup, from idea to Series A</span><span style="font-size: 13px; color: {NMUTED}">A sample startup in Lagos. Five steps</span></span>{icon('chev', 18, NMUTED)}</a>
    <div style="border-radius: {R_L}px; background: {RAISED}; padding: 12px 12px 12px 16px; display: flex; align-items: center; gap: 12px">
      <span style="color: {MINT}">{ic8('cart', 22, MINT)}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; color: {NMUTED}">Next brief, on Thursday</span><span style="font-size: 15px; font-weight: 600; line-height: 1.3">Shoprite, and living on thin margins</span></span>
      <button onClick="[[ remind ]]" aria-pressed="[[ reminded ]]" style="flex-shrink: 0; white-space: nowrap; height: 44px; padding: 0 12px; border-radius: {R_M}px; background: [[ remBg ]]; color: [[ remFg ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">[[ remLabel ]]</button>
    </div>
    <span style="font-size: 17px; font-weight: 600; margin-top: 2px">Words you'll meet</span>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: -8px">{words}</div>
    {rules_card()}
    {ola_pill(label='Ask Ola about a company', p='c')}
  </div>
  {tabbar8('Learn', dark=True)}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%s
    const r = !!st.reminded;
    v.reminded = r; v.remind = () => this.setState({ reminded: !r }); v.remLabel = r ? 'Reminder set' : 'Remind me';
    v.remBg = r ? '%s' : '%s'; v.remFg = r ? '%s' : '%s';
    return v;
  }
}''' % (SAVE_JS, LIME, DEEP, EVG, MOON)
    return with_css(phone('Companies explained', body, logic, h=2030, bg=NIGHT, dark=True, defs=ola_defs('c')), PHONE_CSS + HUB_CSS + CO_CSS)


# ---------------------------------------------------------------- a company brief

# Group service revenue, year to 31 March 2025 (KSh billion): M-Pesa 161.1, voice 82.0, mobile data 78.5,
# fixed and wholesale 16.8, the rest 33.0 (messaging, incoming calls, Ethiopia and other). Total 371.4.
SPLIT = [('M-Pesa', 43, LIME, NIGHT, 'Small fees on sending money, paying shops and borrowing through the app: KSh 161 billion in the year, up 15%.'),
         ('Calls', 22, MINT, NIGHT, 'Voice calls, the business it started with. Still KSh 82 billion, but barely growing: up 2%.'),
         ('Mobile data', 21, IRIS, NIGHT, 'Internet on phones: KSh 79 billion, and growing fastest, up 17%.'),
         ('Home and business internet', 5, BLUSH, BLUSH_INK, 'Fibre to homes and connections for companies: KSh 17 billion.'),
         ('Everything else', 9, '#8E9A95', NIGHT, 'Text messages, calls in from other networks, and its newer business in Ethiopia.')]
NUMBERS = [('35.8 million', 'M-Pesa customers used it in the last month of the year. Each payment earns a small fee.'),
           ('KSh 371 billion', 'earned from services in the year. About KSh 1 billion a day.'),
           ('Over KSh 20 billion', 'lost in Ethiopia before interest and tax, while it builds a network there.')]
RISKS = [('Rules on M-Pesa', 'Most of its growth comes from M-Pesa, so a change in the rules or taxes on mobile-money fees matters a lot.'),
         ('A big bet in Ethiopia', 'It is spending heavily to grow there. The birr lost value against the shilling, which made the losses bigger.'),
         ('Others want the same payments', "Other mobile-money services and banks' own apps compete for every payment.")]


def brief():
    seg_btns = ''.join(f'''<button onClick="[[ sg{i} ]]" aria-pressed="[[ sgOn{i} ]]" style="min-height: 44px; padding: 0 10px 0 8px; border-radius: 8px; background: [[ sgBg{i} ]]; display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: {MOON}; transition: background-color .18s">
          <span style="width: 12px; height: 12px; border-radius: 2px; background: {c}"></span>{n}, {p}</button>''' for i, (n, p, c, _f, _t) in enumerate(SPLIT))
    bar = ''.join(f'<span style="height: 40px; flex: {p} 1 0; min-width: 8px; background: {c}; opacity: [[ sgOp{i} ]]; transform-origin: 0 0; animation: barIn .6s cubic-bezier(.2,.8,.2,1) {0.15 + i * 0.07:.2f}s both; transition: opacity .2s"></span>' for i, (_n, p, c, _f, _t) in enumerate(SPLIT))
    numbers = ''.join(f'<div style="padding: 14px 0; display: flex; flex-direction: column; gap: 4px; {"border-top: 1px solid " + NLINE + ";" if i else ""}"><span style="font-size: 26px; font-weight: 600; letter-spacing: -0.03em; color: {LIME}">{n}</span><span style="font-size: 15px; line-height: 1.45; color: #DDE3E0">{t}</span></div>' for i, (n, t) in enumerate(NUMBERS))
    risks = ''.join(f'<div style="display: flex; flex-direction: column; gap: 4px; padding: 12px 0; {"border-top: 1px solid rgba(255,199,214,.2);" if i else ""}"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 15px; line-height: 1.45; opacity: .9">{d}</span></div>' for i, (t, d) in enumerate(RISKS))
    words = ''.join(f'<a href="R8-Words-Decoder.dc.html" style="height: 44px; padding: 0 14px; border-radius: {R_M}px; background: {RAISED}; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{icon("arch", 16, LIME)}{w}</a>' for w in ['Revenue', 'Market share', 'Dividend', 'Listed company'])
    body = f'''  <div class="scr" style="gap: 18px">
    {co_head('R8-Companies.dc.html', 'Company brief')}
    <div style="display: flex; gap: 6px; flex-wrap: wrap"><span class="chip" style="background: {RAISED}; color: {MOON}">Listed in Nairobi</span><span class="chip" style="background: {RAISED}; color: {MOON}">Five minutes</span>{chip_dark('Sample editorial')}</div>
    <h1 class="d" style="font-size: 38px">Safaricom: how a phone company became a money company</h1>
    <span style="font-size: 13px; line-height: 1.45; color: {NMUTED}">By AWO's editors, from {SOURCE}.</span>
    <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="font-size: 17px; font-weight: 600">In one minute</span>
      <span class="bul">Safaricom is Kenya's biggest mobile network. Its shares are listed on the Nairobi Securities Exchange.</span>
      <span class="bul">It started by selling calls. Now M-Pesa brings in about twice as much as calls do.</span>
      <span class="bul">M-Pesa earns small fees on millions of payments. Small fees, times millions, add up.</span>
    </section>
    <section style="display: flex; flex-direction: column; gap: 12px">
      <span style="font-size: 17px; font-weight: 600">How it makes money</span>
      <span style="font-size: 15px; line-height: 1.45; color: {NMUTED}">Of every KSh 100 it earned from services:</span>
      <div aria-hidden="true" style="display: flex; gap: 3px; border-radius: {R_S}px; overflow: hidden">{bar}</div>
      <div role="group" aria-label="Where the money comes from: tap a part" style="display: flex; flex-wrap: wrap; gap: 4px; margin-left: -8px">{seg_btns}</div>
      <p style="min-height: 72px; border-radius: {R_M}px; background: {DEEP}; padding: 12px 14px; font-size: 15px; line-height: 1.5">[[ sgText ]]</p>
    </section>
    <section style="display: flex; flex-direction: column; gap: 4px">
      <span style="font-size: 17px; font-weight: 600; margin-bottom: 4px">The numbers, in plain words</span>{numbers}
    </section>
    <section style="border-radius: {R_L}px; background: {NWARN_BG}; color: {NWARN_FG}; padding: 16px 18px 6px; display: flex; flex-direction: column">
      <span style="display: flex; align-items: center; gap: 8px; font-size: 17px; font-weight: 600; padding-bottom: 4px">{ALERT}What could go wrong</span>{risks}
    </section>
    <section style="border-radius: {R_L}px; box-shadow: inset 0 0 0 1.5px {MINT}; padding: 16px 18px; display: flex; flex-direction: column; gap: 8px">
      <span style="font-size: 15px; font-weight: 600; color: {MINT}">Why AWO chose it</span>
      <span style="font-size: 16px; line-height: 1.5">It shows how tiny fees on millions of payments add up, and how a company can change what it is. Not because it's a good or a bad buy.</span>
    </section>
    <section style="display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 17px; font-weight: 600">Learn more</span>
      <a href="R8-Topic-Shares.dc.html" style="min-height: 56px; border-radius: {R_M}px; background: {RAISED}; padding: 0 14px; display: flex; align-items: center; gap: 12px">{moon(22, 'half')}<span style="flex-grow: 1; font-size: 15px; font-weight: 600">Shares and dividends</span>{icon('chev', 16, NMUTED)}</a>
      <a href="R7-Lesson.dc.html" style="min-height: 56px; border-radius: {R_M}px; background: {RAISED}; padding: 0 14px; display: flex; align-items: center; gap: 12px">{moon(22, 'new')}<span style="flex-grow: 1; font-size: 15px; font-weight: 600">What an IPO is</span>{icon('chev', 16, NMUTED)}</a>
      <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px">{words}</div>
    </section>
    <section style="border-top: 1px solid {NLINE}; padding-top: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; gap: 8px; flex-wrap: wrap">{REVIEWED_D}{chip_dark('Sample editorial, Q-36')}</span>
      <p style="font-size: 14px; line-height: 1.5; color: {NMUTED}">Education, not a recommendation. AWO isn't paid to feature Safaricom and has no link to it. There's no button to buy its shares, on purpose. Source: {SOURCE}.</p>
      {ola_pill(label='Ask Ola about this brief', p='b')}
    </section>
  </div>
  {tabbar8('Learn', dark=True)}'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%s
    const T = %s, sg = st.sg == null ? 0 : st.sg;
    v.sgText = T[sg];
    for (let i = 0; i < T.length; i++) {
      v['sg' + i] = () => this.setState({ sg: i }); v['sgOn' + i] = sg === i;
      v['sgBg' + i] = sg === i ? '%s' : 'transparent'; v['sgOp' + i] = sg === i ? 1 : .45;
    }
    return v;
  }
}''' % (SAVE_JS, json.dumps([nbs(t) for _n, _p, _c, _f, t in SPLIT], ensure_ascii=False), RAISED)
    css = PHONE_CSS + HUB_CSS + CO_CSS + '@keyframes barIn{from{transform:scaleX(0)}to{transform:scaleX(1)}}'
    return with_css(phone('A company brief', body, logic, h=2560, bg=NIGHT, dark=True, defs=ola_defs('b')), css)


# ---------------------------------------------------------------- how a startup raises money

OWNERS = [('Founders', LIME), ('Friends and family', MINT), ('Seed investors', IRIS), ('Series A investors', BLUSH)]
STAKES = [[100, 0, 0, 0], [90, 10, 0, 0], [72, 8, 20, 0], [54, 6, 15, 25], [54, 6, 15, 25]]
STEPS = [('Two founders, one idea', 'Adaeze and Kemi start a delivery company in Lagos. They own all of it, half each. It is worth very little so far: an idea and two laptops.', 'Worth, on paper: almost nothing yet'),
         ('Friends and family', 'An aunt and two friends put in ₦ 5 million for 10% of the company. That says the whole company is worth ₦ 50 million, on paper.', 'Worth, on paper: ₦ 50 million'),
         ('A seed round', 'Seed investors pay ₦ 150 million for new shares: 20% of the company. Everyone who owned a slice now owns a smaller one. That is dilution.', 'Worth, on paper: ₦ 750 million'),
         ('A Series A', 'Bigger investors pay ₦ 1.5 billion for 25%. The founders now own 54% together, of a company valued at ₦ 6 billion. Owning less of something bigger.', 'Worth, on paper: ₦ 6 billion'),
         ('Most never get here', 'Most startups never raise another round, and many close. A valuation is not money in the bank: if the company closes, every share is worth nothing. The owners only get cash if it is sold, or listed.', 'Worth, on paper: only if it lasts')]


def donut():
    """Four slices on one ring (pathLength 100), each slice's length and offset bound to the step."""
    rings = ''.join(f'<circle cx="60" cy="60" r="46" pathLength="100" fill="none" stroke="{c}" stroke-width="20" style="stroke-dasharray: [[ dl{i} ]] 100; stroke-dashoffset: [[ do{i} ]]; transition: stroke-dasharray .6s cubic-bezier(.2,.8,.2,1), stroke-dashoffset .6s cubic-bezier(.2,.8,.2,1)"></circle>' for i, (_n, c) in enumerate(OWNERS))
    return (f'<svg width="150" height="150" viewBox="0 0 120 120" aria-hidden="true" style="display: block; transform: rotate(-90deg)">'
            f'<circle cx="60" cy="60" r="46" fill="none" stroke="{RAISED}" stroke-width="20"></circle>{rings}</svg>')


def startup():
    legend = ''.join(f'<span style="display: flex; align-items: center; gap: 10px; font-size: 14px; line-height: 1.3; opacity: [[ lgOp{i} ]]; transition: opacity .3s"><span style="width: 12px; height: 12px; flex-shrink: 0; border-radius: 2px; background: {c}"></span><span style="flex-grow: 1">{n}</span><span style="font-weight: 600; font-variant-numeric: tabular-nums">[[ pc{i} ]]%</span></span>' for i, (n, c) in enumerate(OWNERS))
    defs = ''.join(f'<div style="border-radius: {R_M}px; background: {DEEP}; padding: 14px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600; color: {LIME}">{w}</span><span style="font-size: 15px; line-height: 1.45">{d}</span></div>'
                   for w, d in [('Valuation', 'What investors agree a company is worth. Not money in the bank.'), ('Dilution', 'Owning a smaller slice when new shares are sold.'), ('A round', 'A time a startup sells new shares: friends and family, seed, then Series A, B and on.')])
    body = f'''  <div class="scr" style="gap: 18px">
    {co_head('R8-Companies.dc.html', 'Companies explained', save=False)}
    <div style="display: flex; flex-direction: column; gap: 10px">
      <h1 class="d" style="font-size: 40px">How a startup raises money</h1>
      <p style="font-size: 16px; line-height: 1.45; color: {NMUTED}">Follow a sample startup from two founders to a Series A, and watch the slice they own.</p>
    </div>
    <section style="border-radius: {R_L}px; background: {DEEP}; padding: 18px 16px 16px; display: flex; flex-direction: column; gap: 14px">
      <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 13px; font-weight: 600; color: {MINT}">[[ stepLabel ]]</span>{chip_dark('Sample startup')}</div>
      <h2 class="d" style="font-size: 28px">[[ stepTitle ]]</h2>
      <div style="display: flex; align-items: center; gap: 14px">
        <div role="img" aria-label="[[ pieLabel ]]" style="position: relative; flex-shrink: 0">{donut()}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center"><span style="font-size: 26px; font-weight: 600; letter-spacing: -0.03em">[[ pc0 ]]%</span><span style="font-size: 12px; color: {NMUTED}">founders</span></span></div>
        <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 10px">{legend}</div>
      </div>
      <span style="font-size: 14px; font-weight: 600; color: {LIME}">[[ worth ]]</span>
      <p style="font-size: 16px; line-height: 1.5; min-height: 96px">[[ stepText ]]</p>
      <div style="display: flex; gap: 8px">
        <button onClick="[[ prev ]]" aria-disabled="[[ atStart ]]" style="flex: 1 1 0; height: 48px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px {NLINE}; font-size: 15px; font-weight: 600; opacity: [[ prevOp ]]">Back</button>
        <button onClick="[[ next ]]" style="flex: 1.6 1 0; height: 48px; border-radius: {R_M}px; background: {LIME}; color: {INK}; font-size: 15px; font-weight: 600">[[ nextLabel ]]</button>
      </div>
    </section>
    <span style="font-size: 17px; font-weight: 600">Three words</span>
    <div style="display: flex; flex-direction: column; gap: 8px; margin-top: -8px">{defs}</div>
    <section style="border-radius: {R_L}px; background: {NWARN_BG}; color: {NWARN_FG}; padding: 16px 18px; display: flex; gap: 12px; align-items: flex-start">
      <span style="padding-top: 2px">{ALERT}</span>
      <span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 16px; font-weight: 600">Why AWO never connects you with a startup</span><span style="font-size: 15px; line-height: 1.5">Putting money into a startup is risky: most who do lose it, and a share is hard to sell. AWO teaches how it works. It never lists deals, or introduces members to founders or investors.</span></span>
    </section>
    <section style="border-top: 1px solid {NLINE}; padding-top: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; gap: 8px; flex-wrap: wrap">{REVIEWED_D}{chip_dark('Sample figures')}</span>
      <p style="font-size: 14px; line-height: 1.5; color: {NMUTED}">Adaeze and Kemi's company is a sample, made up to teach the idea. Real rounds differ in size and terms.</p>
      {ola_pill(label='Ask Ola about startups', p='s')}
    </section>
  </div>
  {tabbar8('Learn', dark=True)}'''
    steps = json.dumps([[nbs(a), nbs(b), nbs(c)] for a, b, c in STEPS], ensure_ascii=False)
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const S = %s, P = %s, N = %s;
    const s = st.s || 0, p = P[s];
    const v = {
      stepLabel: 'Step ' + (s + 1) + ' of ' + S.length, stepTitle: S[s][0], stepText: S[s][1], worth: S[s][2],
      next: () => this.setState({ s: s === S.length - 1 ? 0 : s + 1 }), prev: () => this.setState({ s: Math.max(0, s - 1) }),
      nextLabel: s === S.length - 1 ? 'Start again' : 'Next', atStart: s === 0 ? 'true' : 'false', prevOp: s === 0 ? .45 : 1,
      pieLabel: N.map((n, i) => n + ' ' + p[i] + '%%').join(', ')
    };
    let off = 0;
    for (let i = 0; i < 4; i++) { v['pc' + i] = p[i]; v['dl' + i] = p[i]; v['do' + i] = -off; off += p[i]; v['lgOp' + i] = p[i] ? 1 : .35; }
    return v;
  }
}''' % (steps, json.dumps(STAKES), json.dumps([n for n, _c in OWNERS]))
    return with_css(phone('How a startup raises money', body, logic, h=1780, bg=NIGHT, dark=True, defs=ola_defs('s')), PHONE_CSS + HUB_CSS + CO_CSS)


BOARDS = [('R8-Companies', companies), ('R8-Company-Brief', brief), ('R8-Startup', startup)]
