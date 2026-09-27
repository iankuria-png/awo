"""Round 9, batch 6: merchandise. A money-in-and-out notebook for traders (the Hub's notebook on paper), a
check-in fridge magnet and a printable year, stickers and enamel pins of the five shapes, a tote bag and ambassador
T-shirts with a name badge.

Rules: Africa in substance, never decoration (no patterns, maps or flag colours); nothing shows a member's
amounts except her own notebook, in her own hand; ambassadors show the app and never give advice (Q-48)."""
import calendar
import json
import re

from lib9 import *  # noqa: F401,F403
from marketing7 import H, K  # noqa: E402
from kit7 import board7  # noqa: E402
from around9 import rules_card, label, qr_svg, seg, seg_js, INK_PEN  # noqa: E402

BAL = 'text-wrap: balance'
MERCH_CSS = CSS9 + '.seg9 button{white-space:nowrap}'
PW, PH = 420, 597  # an A6 page (105 by 148 mm) at 4 px a millimetre
PAPER, RULE = '#FFFFFF', '#C9D6D0'
SHAPES = [('pool', 'Home', EVG_D, LIME, 'Your safety net, filling'), ('moon', 'Learn', NIGHT, MOON, 'Learning, a little at a time'),
          ('hub', 'Hub', LIME, EVG, 'Tools for your own sums'), ('ripple', 'Community', BLUSH, BLUSH_INK, 'Your circle'),
          ('stones', 'Me', POOL, EVG, 'Where you stand, and the next step')]


def js(o):
    return json.dumps(o, ensure_ascii=False)


def sty(html):
    """SVG presentation attributes can't hold a hole; move fill or stroke holes into style."""
    return re.sub(r'\b(fill|stroke)="(\[\[ \w+ \]\])"', r'style="\1: \2"', html)


def glyph(g, size, col, sw=2):
    return hub_icon(None, size, col, sw) if g == 'hub' else icon(g, size, col, sw)


def hw(text, size=20, col=INK_PEN, extra=''):
    """Her own handwriting on paper. Hidden when the board shows the blank template."""
    return f'<span class="hw hand" style="font-size: {size}px; line-height: 1; color: {col}; {HF}; {extra}">{text}</span>'


def page(inner, bg=PAPER, pad='26px 24px', right=False):
    gutter = 'linear-gradient(to right, rgba(16,24,20,.10), rgba(16,24,20,0) 7%)' if right else 'linear-gradient(to left, rgba(16,24,20,.10), rgba(16,24,20,0) 7%)'
    return (f'<div style="position: relative; width: {PW}px; height: {PH}px; box-sizing: border-box; padding: {pad}; background: {bg}; display: flex; flex-direction: column; gap: 12px; overflow: hidden">'
            f'<span aria-hidden="true" style="position: absolute; inset: 0; background: {gutter}; pointer-events: none"></span>{inner}</div>')


def spread(left, right):
    return f'<div style="display: flex; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 4px rgba(16,24,20,.12), 0 30px 60px rgba(16,24,20,.2)">{left}{right}</div>'


def printed(t, size=12, col=SEC, w=600):
    return f'<span style="font-size: {size}px; font-weight: {w}; color: {col}">{t}</span>'


# ================================================================ The money-in-and-out notebook

WEEK = [('Mon', 3400, 1000, 'slow morning'), ('Tue', 2900, 600, ''), ('Wed', 3800, 1700, 'bought wrapping paper'),
        ('Thu', 3100, 400, ''), ('Fri', 4900, 1100, 'blue bowls sold out'), ('Sat', 6800, 5000, 'restock, Gikomba'),
        ('Sun', 800, 200, 'rain')]


def n(v):
    return f'{v:,}'.replace(',', ' ')


def nb_cover():
    lines = [('Business', "Wanjiru's Homeware"), ('From', '5 Oct 2026'), ('To', '')]
    rows = ''.join(f'<div style="display: grid; grid-template-columns: 70px 1fr; align-items: end; gap: 8px; height: 32px"><span style="font-size: 12px; font-weight: 600; color: {SEC}; padding-bottom: 4px">{k}</span>'
                   f'<span style="border-bottom: 1.5px solid {RULE}; height: 100%; display: flex; align-items: flex-end; padding-bottom: 3px">{hw(v, 20) if v else ""}</span></div>' for k, v in lines)
    return page(f'''{lockup(22, '#FFFFFF', LIME)}
      <div style="flex-grow: 1"></div>
      <h3 style="margin: 0; {H(52, '#FFFFFF')}">Money in<br>and out</h3>
      <p style="margin: 0; font-size: 15px; line-height: 1.4; color: {ON_EVG}">A notebook for your business. A week to a spread, a month to a page.</p>
      <div style="border-radius: {R_M}px; background: #FFFFFF; padding: 10px 14px 12px; display: flex; flex-direction: column; gap: 2px">{rows}</div>
      <span style="font-size: 12px; color: {ON_EVG}">Keep it by the till. Write it the same evening.</span>''', EVG, '30px 28px')


def nb_week():
    head = (f'<div style="display: grid; grid-template-columns: 46px 1fr 1fr; gap: 8px; padding-bottom: 6px; border-bottom: 2px solid {EVG}">'
            f'{printed("Day")}{printed("Came in")}{printed("Went out")}</div>')
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 46px 1fr 1fr; gap: 8px; align-items: end; height: 50px; border-bottom: 1px solid {RULE}">
          {printed(d, 13, INK)}<span style="padding-bottom: 4px">{hw(n(a), 22)}</span><span style="padding-bottom: 4px">{hw(n(b), 22)}</span></div>''' for d, a, b, _t in WEEK)
    tot_in, tot_out = sum(w[1] for w in WEEK), sum(w[2] for w in WEEK)
    left = page(f'''<span style="display: flex; justify-content: space-between; align-items: flex-end; gap: 10px">{printed("Week of", 12)}<span style="flex-grow: 1; border-bottom: 1.5px solid {RULE}; padding: 0 0 3px 6px">{hw("5 Oct", 20)}</span>{printed("Money in", 12)}<span style="width: 58px; border-bottom: 1.5px solid {RULE}; padding: 0 0 3px 6px">{hw("KSh", 20)}</span></span>
      <div style="display: flex; flex-direction: column">{head}{rows}
        <div style="display: grid; grid-template-columns: 46px 1fr 1fr; gap: 8px; align-items: end; height: 48px; border-bottom: 2px solid {EVG}">{printed("Total", 13, EVG, 700)}<span style="padding-bottom: 4px">{hw(n(tot_in), 24)}</span><span style="padding-bottom: 4px">{hw(n(tot_out), 24)}</span></div></div>''')
    notes = ''.join(f'<div style="height: 30px; border-bottom: 1px solid {RULE}; display: flex; align-items: flex-end; padding-bottom: 3px">{hw(t, 19) if t else ""}</div>' for t in [d + ': ' + t for d, _a, _b, t in WEEK if t][:4])
    sum_row = lambda k, v, bold=False: (f'<div style="display: flex; justify-content: space-between; align-items: flex-end; height: 34px; border-bottom: 1px solid {RULE}">{printed(k, 13, INK if bold else SEC, 700 if bold else 600)}'
                                        f'<span style="padding-bottom: 3px">{hw(v, 24 if bold else 21)}</span></div>')
    right = page(f'''{printed("This week", 15, EVG, 700)}
      <div style="border-radius: {R_M}px; box-shadow: inset 0 0 0 1.5px {EVG}; padding: 4px 14px 10px">{sum_row("Came in", n(tot_in))}{sum_row("Went out", n(tot_out))}{sum_row("What's left", n(tot_in - tot_out), True)}{sum_row("I took for home", "3 000")}</div>
      {printed("What sold twice?", 13, INK)}<div style="height: 30px; border-bottom: 1px solid {RULE}; display: flex; align-items: flex-end; padding-bottom: 3px">{hw("blue bowls, small pots", 19)}</div>
      {printed("What happened", 13, INK)}{notes}
      <div style="flex-grow: 1"></div>
      <span style="display: flex; gap: 8px; align-items: flex-start; font-size: 12px; line-height: 1.4; color: {SEC}"><span style="flex-shrink: 0; display: flex">{icon("stones", 16, EVG)}</span>The stall's money and money for home, kept apart. From the lesson "Your stall's money, and yours".</span>''', right=True)
    return spread(left, right)


TICK = f'<span class="hw" style="position: absolute; left: 2px; top: -6px; font-size: 26px; color: {INK_PEN}">✓</span>'


def nb_month():
    weeks = [('5 Oct', 25700, 10000), ('12 Oct', 21400, 7300), ('19 Oct', 23900, 12600), ('26 Oct', 18200, 5100)]
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 64px 1fr 1fr 1fr; gap: 6px; align-items: end; height: 44px; border-bottom: 1px solid {RULE}">
          <span style="padding-bottom: 4px">{hw(d, 18)}</span><span style="padding-bottom: 4px">{hw(n(a), 20)}</span><span style="padding-bottom: 4px">{hw(n(b), 20)}</span><span style="padding-bottom: 4px">{hw(n(a - b), 20)}</span></div>''' for d, a, b in weeks)
    ti, to = sum(w[1] for w in weeks), sum(w[2] for w in weeks)
    tick = lambda t, on: (f'<span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {INK}"><span style="position: relative; width: 20px; height: 20px; border-radius: 4px; box-shadow: inset 0 0 0 1.5px {SEC}">'
                          f'{TICK if on else ""}</span>{t}</span>')
    left = page(f'''<span style="display: flex; align-items: flex-end; gap: 10px">{printed("Month", 12)}<span style="flex-grow: 1; border-bottom: 1.5px solid {RULE}; padding: 0 0 3px 6px">{hw("October", 22)}</span></span>
      <div style="display: flex; flex-direction: column"><div style="display: grid; grid-template-columns: 64px 1fr 1fr 1fr; gap: 6px; padding-bottom: 6px; border-bottom: 2px solid {EVG}">{printed("Week")}{printed("Came in")}{printed("Went out")}{printed("Left")}</div>{rows}
        <div style="display: grid; grid-template-columns: 64px 1fr 1fr 1fr; gap: 6px; align-items: end; height: 46px; border-bottom: 2px solid {EVG}">{printed("Month", 13, EVG, 700)}<span style="padding-bottom: 4px">{hw(n(ti), 21)}</span><span style="padding-bottom: 4px">{hw(n(to), 21)}</span><span style="padding-bottom: 4px">{hw(n(ti - to), 21)}</span></div></div>
      {printed("Did the stall pay me this month?", 13, INK)}<span style="display: flex; gap: 20px">{tick("Yes", True)}{tick("Not yet", False)}</span>
      {printed("One thing to try next month", 13, INK)}<div style="height: 30px; border-bottom: 1px solid {RULE}; display: flex; align-items: flex-end; padding-bottom: 3px">{hw("own wallet for the stall", 19)}</div>''')
    mx = max(w[1] for w in weeks)
    bars = ''.join(f'''<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px; height: 100%; justify-content: flex-end">
          <div style="width: 100%; display: flex; gap: 4px; align-items: flex-end; height: 100%; box-sizing: border-box; padding: 0 4px">
            <span class="hw" style="flex: 1 1 0; height: {a / mx * 100:.0f}%; background: repeating-linear-gradient(135deg, {INK_PEN} 0 2px, transparent 2px 7px); box-shadow: inset 0 0 0 2px {INK_PEN}; border-radius: 2px"></span>
            <span class="hw" style="flex: 1 1 0; height: {b / mx * 100:.0f}%; box-shadow: inset 0 0 0 2px {INK_PEN}; border-radius: 2px"></span></div>
          {printed(str(i + 1), 12)}</div>''' for i, (_d, a, b) in enumerate(weeks + [('', 0, 0)]))
    grid = ''.join(f'<span style="position: absolute; left: 0; right: 0; bottom: {k * 20}%; border-top: 1px dashed {RULE}"></span>' for k in range(1, 5))
    right = page(f'''{printed("Colour in your weeks", 15, EVG, 700)}
      <span style="font-size: 12px; line-height: 1.4; color: {SEC}">One bar for what came in, shaded; one for what went out, empty. Week by week, the shape tells you before the total does.</span>
      <div style="position: relative; flex-grow: 1; display: flex; gap: 6px; padding-top: 10px; border-bottom: 2px solid {EVG}">{grid}{bars}</div>
      <span style="display: flex; gap: 16px; font-size: 12px; color: {SEC}"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 14px; height: 14px; background: repeating-linear-gradient(135deg, {SEC} 0 2px, transparent 2px 5px); box-shadow: inset 0 0 0 1.5px {SEC}"></span>Came in</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 14px; height: 14px; box-shadow: inset 0 0 0 1.5px {SEC}"></span>Went out</span></span>''', right=True)
    return spread(left, right)


def nb_back():
    return page(f'''<h3 style="margin: 0; {H(34, '#FFFFFF')}">Keep it in the app too, if you like.</h3>
      <p style="margin: 0; font-size: 14px; line-height: 1.45; color: {ON_EVG}">The notebook in AWO's Hub has the same pages. It adds up for you, works offline and stays private.</p>
      <span style="align-self: flex-start; border-radius: {R_M}px; background: #FFFFFF; padding: 8px">{qr_svg(120)}</span>
      <div style="flex-grow: 1"></div>
      <span style="font-size: 12px; line-height: 1.5; color: {ON_EVG}">AWO is for learning. It never lends money and never asks for your PIN.<br>26 weeks and 6 month pages. A6, lays flat, takes pencil and pen.</span>
      {lockup(20, '#FFFFFF', LIME)}''', EVG, '30px 28px')


def notebook():
    views = [('Cover', nb_cover()), ('A week', nb_week()), ('The month', nb_month()), ('Back', nb_back())]
    shown = ''.join(f'<sc-if value="[[ pg{i} ]]" hint-placeholder-val="[[ {"true" if i == 1 else "false"} ]]"><div style="display: flex; justify-content: center; animation: dimIn .25s both">{v}</div></sc-if>' for i, (_n, v) in enumerate(views))
    body = f'''  <div style="display: flex; gap: 40px; align-items: flex-start">
    <div style="width: 900px; flex-shrink: 0; display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap">{seg('nv', [v[0] for v in views], 'Which pages')}
        <span style="display: flex; align-items: center; gap: 4px; font-size: 15px; font-weight: 600">Filled in by Wanjiru{switch(0, 'Filled in by Wanjiru')}</span></div>
      <div style="--hw: [[ hwO ]]; min-height: 620px; display: flex; align-items: flex-start; justify-content: center">{shown}</div>
    </div>
    <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px">
      {rules_card("Made for a trader's day", ["A6, so it fits an apron pocket or the tote's inside pocket. Lays flat on a table.", "One week to a spread: what came in and went out each day, the week's sums, and what sold twice.", 'The currency is written once a week, so the same book works in shillings, rand, pula or kwacha.', 'A month page to colour in: the shape shows a slow month before the total does.'])}
      {rules_card('Paper and the app, the same pages', ['The columns match the notebook in the Hub, so moving to the phone later changes nothing she has learned.', "The back cover's QR code is a sample; it says so when scanned.", 'Switch off "filled in" for the blank pages, ready to print.'])}
      {rules_card('Choices worth checking', ['Given at workshops, or sold at cost? Printed where? (Q-48)', "The sample week matches Wanjiru's notebook in the app: KSh 25 700 in, KSh 10 000 out."])}
    </div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const nv = st.nv == null ? 1 : st.nv;
    const v = {};
%s
%s
    for (let i = 0; i < 4; i++) v['pg' + i] = nv === i;
    v.hwO = v.sw0 ? 1 : 0;
    return v;
  }
}''' % (seg_js('nv', 4, 'nv'), switch_js(1, [True]))
    return board7('Money in and out: a notebook for traders', 'The Hub\'s business notebook on paper, for the stall, the salon or the spaza: a week to a spread, a month to a page, in her own hand. Flip through it, or switch to the blank pages.',
                  body, logic, 1760, 940, css=MERCH_CSS + '.hw{opacity:var(--hw);transition:opacity .25s}')


# ================================================================ The check-in magnet and a printed year

def mini_month(y, m):
    cal = calendar.Calendar(0).monthdayscalendar(y, m)
    cells = ''
    for wk in cal:
        for d in wk:
            if not d:
                cells += '<span></span>'
                continue
            if d == 13:
                cells += (f'<span style="position: relative; height: 19px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; color: {EVG}">'
                          f'<svg width="28" height="17" viewBox="0 0 28 17" aria-hidden="true" style="position: absolute"><ellipse cx="14" cy="8.5" rx="13" ry="7.5" fill="{LIME}" stroke="{EVG}" stroke-width="1.5"></ellipse></svg><span style="position: relative">{d}</span></span>')
            elif d == 5:
                cells += f'<span style="height: 19px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 12px; color: {INK}">{d}<span style="width: 5px; height: 5px; border-radius: 9px; background: {BLUSH_2}; margin-top: -1px"></span></span>'
            else:
                cells += f'<span style="height: 19px; display: flex; align-items: center; justify-content: center; font-size: 12px; color: {SEC}">{d}</span>'
    heads = ''.join(f'<span style="font-size: 12px; font-weight: 600; color: {MUTED}; text-align: center">{d}</span>' for d in 'MTWTFSS')
    return (f'<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 14px; font-weight: 700; color: {EVG}">{calendar.month_name[m]} {y}</span>'
            f'<div style="display: grid; grid-template-columns: repeat(7, 1fr); row-gap: 0">{heads}{cells}</div></div>')


def magnet_stones():
    """Twelve stones, January to December, rising in three rows; the same magnet works any year."""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    xs = [50, 140, 230, 320]
    pos = [(xs[k], 330 - k * 10) for k in range(4)] + [(xs[3 - k], 215 - k * 10) for k in range(4)] + [(xs[k], 100 - k * 10) for k in range(4)]
    out = ''
    for i, ((x, y), mo) in enumerate(zip(pos, months)):
        out += f'''<button onClick="[[ tk{i} ]]" aria-pressed="[[ tkOn{i} ]]" aria-label="{mo}: mark this check-in done" style="position: absolute; left: {x - 36}px; top: {y - 22}px; width: 72px; height: 44px; display: flex; align-items: center; justify-content: center">
          <svg width="68" height="34" viewBox="0 0 68 34" aria-hidden="true" style="position: absolute"><ellipse cx="34" cy="20" rx="31" ry="12" fill="#BFD9D2"></ellipse><ellipse cx="34" cy="16" rx="31" ry="12" fill="#FFFFFF" stroke="{EVG}" stroke-width="2"></ellipse></svg>
          <span style="position: relative; font-size: 13px; font-weight: 700; color: {EVG}">{mo}</span>
          <sc-if value="[[ tkOn{i} ]]" hint-placeholder-val="[[ {"true" if 6 <= i <= 9 else "false"} ]]"><span class="hand" style="position: absolute; left: 22px; top: -16px; font-size: 40px; color: {INK_PEN}; {HF}; animation: pop .3s both">✓</span></sc-if>
        </button>'''
    path = ' '.join(f'{"M" if i == 0 else "L"}{x} {y}' for i, (x, y) in enumerate(pos))
    return f'<svg width="370" height="380" aria-hidden="true" style="position: absolute; left: 0; top: 0"><path d="{path}" fill="none" stroke="{EVG}" stroke-opacity=".25" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"></path></svg>' + out


def calendar_board():
    fridge = f'''<div style="position: relative; width: 640px; height: 820px; flex-shrink: 0; border-radius: {R_L}px; overflow: hidden; background: linear-gradient(100deg, #E6EAE8, #F4F6F5 45%, #E3E7E5); box-shadow: inset 0 0 0 1px rgba(16,24,20,.08)">
      <span aria-hidden="true" style="position: absolute; right: 36px; top: 120px; width: 22px; height: 420px; border-radius: 11px; background: linear-gradient(to right, #C6CCC9, #EEF1EF, #B9C0BC); box-shadow: 0 8px 18px rgba(16,24,20,.18)"></span>
      <div role="group" aria-label="A fridge magnet with twelve check-in stones" style="position: absolute; left: 90px; top: 110px; width: 420px; height: 580px; border-radius: {R_L}px; background: {POOL}; box-shadow: 0 2px 3px rgba(16,24,20,.2), 0 18px 34px rgba(16,24,20,.22); padding: 26px 26px 22px; box-sizing: border-box; transform: rotate(-2deg)">
        <span style="display: flex; justify-content: space-between; align-items: center">{lockup(20, EVG, LIME)}<span style="font-size: 12px; font-weight: 600; color: {EVG}">Tick a stone each month</span></span>
        <h3 style="margin: 16px 0 0; {H(40, EVG)}">My check-in day</h3>
        <span style="display: flex; align-items: flex-end; gap: 8px; margin-top: 6px"><span style="flex-grow: 1; border-bottom: 2px solid {EVG}; padding-bottom: 2px">{"<span class='hand' style='font-size: 30px; color: " + INK_PEN + "; " + HF + "'>the 13th</span>"}</span></span>
        <div style="position: relative; height: 380px; margin-top: 8px">{magnet_stones()}</div>
        <span style="position: absolute; left: 26px; right: 26px; bottom: 20px; font-size: 13px; line-height: 1.4; color: {EVG}">Three questions, about two minutes. Skipping a month is fine.</span>
      </div>
    </div>'''
    months = [(2026, 11), (2026, 12)] + [(2027, m) for m in range(1, 11)]
    grid = ''.join(mini_month(y, m) for y, m in months)
    year = f'''<div style="width: 940px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px">{label('Print my year, from Me, then Reminders (A4 landscape)')}
      <div style="width: 940px; height: 666px; box-sizing: border-box; background: #FFFFFF; padding: 24px 34px 20px; display: flex; flex-direction: column; gap: 18px; box-shadow: 0 2px 4px rgba(16,24,20,.1), 0 24px 60px rgba(16,24,20,.16)">
        <span style="display: flex; justify-content: space-between; align-items: flex-end"><span style="display: flex; flex-direction: column; gap: 4px"><span style="{H(34, EVG)}">Naledi's next 12 check-ins</span><span style="font-size: 13px; color: {SEC}">November 2026 to October 2027</span></span>{lockup(22, EVG, LIME)}</span>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px 40px">{grid}</div>
        <div style="flex-grow: 1"></div>
        <span style="display: flex; justify-content: space-between; gap: 20px; font-size: 12px; line-height: 1.45; color: {SEC}; border-top: 1px solid {LINE7}; padding-top: 10px">
          <span style="display: flex; gap: 18px; align-items: center"><span style="display: flex; align-items: center; gap: 6px"><svg width="22" height="12" viewBox="0 0 22 12" aria-hidden="true"><ellipse cx="11" cy="6" rx="10" ry="5" fill="{LIME}" stroke="{EVG}" stroke-width="1.5"></ellipse></svg>Check-in day</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 6px; height: 6px; border-radius: 9px; background: {BLUSH_2}"></span>Kopano stokvel pot</span></span>
          <span>Printed from AWO on 13 October 2026. Dates only, never amounts. Sample.</span></span>
      </div></div>'''
    body = f'''  <div style="display: flex; gap: 40px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 12px">{label('A fridge magnet, 90 by 120 mm (tap a stone to tick it)')}{fridge}</div>
    <div style="display: flex; flex-direction: column; gap: 20px">{year}
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px">
        {rules_card('The magnet', ['The same magnet for everyone: she writes her own day with a marker.', 'Twelve stones, ticked by hand. Nothing to charge, pair or sync.', 'Skipping is fine, and the magnet says so.'])}
        {rules_card('The printed year', ['Made from her own dates in the app: check-ins, and the dates she added, like her stokvel.', 'Dates only; no amounts, score or stage, because it hangs where everyone can see it.', 'Weeks start on Monday, like the date picker.'])}
      </div>
    </div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const done = st.done || [false, false, false, false, false, false, true, true, true, true, false, false];
    const v = {};
    for (let i = 0; i < 12; i++) { v['tkOn' + i] = !!done[i]; v['tk' + i] = () => { const d = done.slice(); d[i] = !d[i]; this.setState({ done: d }); }; }
    return v;
  }
}'''
    return board7('The check-in, on the fridge', 'A magnet to tick each month\'s check-in by hand, and a year she can print from the app with her own dates on it. For the kitchen, where money talk already happens.', body, logic, 1760, 1170, css=MERCH_CSS)


# ================================================================ Stickers and pins

def sticker(inner, w, h, radius, rot=0, bg='#FFFFFF'):
    return (f'<div style="width: {w}px; height: {h}px; border-radius: {radius}; background: {bg}; box-shadow: 0 0 0 7px #FFFFFF, 0 3px 8px 6px rgba(16,24,20,.12); display: flex; align-items: center; justify-content: center; '
            f'transform: rotate({rot}deg); flex-shrink: 0">{inner}</div>')


def stickers_pins():
    shapes = ''.join(sticker(glyph(g, 50, fg, 2.2), 88, 88, '999px', 0, bg) for g, _n, bg, fg, _d in SHAPES)
    words = [('<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em; color: #FFFFFF">Money, understood.</span>', 250, 64, '12px', -3, EVG),
             (f'<span style="display: flex; align-items: center; gap: 10px; font-size: 22px; font-weight: 600; color: {EVG}">{icon("stones", 26, EVG, 2.2)}I checked in</span>', 210, 64, '12px', 2, POOL),
             (f'<span style="font-size: 22px; font-weight: 600; color: {EVG}">Ask me about AWO</span>', 236, 64, '12px', -1, LIME),
             (f'<span style="display: flex; flex-direction: column; align-items: center; gap: 2px"><span style="font-size: 13px; font-weight: 600; color: {EVG}">Word of the week</span><span style="font-size: 30px; font-weight: 600; letter-spacing: -0.03em; color: {EVG}">Stokvel</span></span>', 190, 130, '95px 95px 12px 12px', 3, LIME),
             (lockup(34, '#FFFFFF', LIME), 190, 90, '14px', -2, EVG)]
    wd = ''.join(sticker(i, w, h, r, rot, bg) for i, w, h, r, rot, bg in words)
    sheet = f'''<div style="width: 600px; height: 640px; flex-shrink: 0; box-sizing: border-box; border-radius: 10px; background: #EEF1EF; box-shadow: 0 2px 4px rgba(16,24,20,.12), 0 24px 60px rgba(16,24,20,.16); padding: 44px 40px; display: flex; flex-direction: column; gap: 44px; position: relative">
      <div style="display: flex; justify-content: space-between; padding: 0 6px">{shapes}</div>
      <div style="display: flex; flex-wrap: wrap; gap: 34px 30px; justify-content: center; align-items: center">{wd}</div>
      <span style="position: absolute; left: 40px; bottom: 18px; font-size: 13px; color: {SEC}">Kiss-cut sheet, 150 by 160 mm. Matt vinyl, weatherproof, for phones, laptops and water bottles.</span>
    </div>'''
    finishes = {0: ('#DDE2DF', '#9AA39F', '#F7F9F8'), 1: ('#3A403D', '#1B1F1D', '#6B726E')}
    pins = ''.join(f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 10px">
          <span style="position: relative; width: 104px; height: 104px; border-radius: 999px; background: linear-gradient(135deg, [[ rimA ]], [[ rimB ]] 60%, [[ rimC ]]); box-shadow: 0 6px 12px rgba(0,0,0,.35); display: flex; align-items: center; justify-content: center">
            <span style="width: 90px; height: 90px; border-radius: 999px; background: {bg}; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 2px 3px rgba(0,0,0,.25)">{glyph(g, 50, fg, 2.6)}</span>
            <span aria-hidden="true" style="position: absolute; left: 18px; top: 12px; width: 34px; height: 14px; border-radius: 999px; background: rgba(255,255,255,.35); transform: rotate(-30deg)"></span></span>
          <span style="font-size: 13px; font-weight: 600; color: {MOON}">{name}</span></div>''' for g, name, bg, fg, _d in SHAPES)
    legend = ''.join(f'<span style="display: flex; gap: 10px; align-items: baseline; font-size: 14px; line-height: 1.4; color: {ON_EVG}"><b style="width: 92px; flex-shrink: 0; color: #FFFFFF; font-weight: 600">{name}</b>{d}</span>' for _g, name, _bg, _fg, d in SHAPES)
    card = f'''<div style="width: 560px; flex-shrink: 0; border-radius: {R_L}px; background: {EVG}; padding: 36px 36px 30px; box-sizing: border-box; display: flex; flex-direction: column; gap: 26px; box-shadow: 0 24px 60px rgba(16,24,20,.2)">
      <span style="display: flex; justify-content: space-between; align-items: center">{lockup(24, '#FFFFFF', LIME)}<span style="font-size: 13px; color: {ON_EVG}">Enamel pins, 25 mm</span></span>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 26px 10px; justify-items: center">{pins}</div>
      <div style="display: flex; flex-direction: column; gap: 8px">{legend}</div>
    </div>'''
    body = f'''  <div style="display: flex; gap: 40px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 12px">{label('A sticker sheet')}{sheet}</div>
    <div style="display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; justify-content: space-between; align-items: center">{label('Pins on their card')}{seg('fin', ['Silver', 'Black nickel'], 'Pin finish')}</div>{card}</div>
    <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px; padding-top: 32px">
      {rules_card('The five shapes, off the screen', ['Each shape is a part of AWO, in its own colour: they already mean something to members, so a pin says which part you love.', 'No patterns, maps or flag colours. Africa is in who wears them and what they say.', '"I checked in" and "Ask me about AWO" are the only word stickers that talk about AWO; none shows a number.'])}
      {rules_card('Choices worth checking', ['Who gets them: members at a workshop, after a milestone, or ambassadors only (Q-48)?', "Silver or black nickel; gold reads as luxury, so it isn't offered."])}
    </div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const fin = st.fin || 0;
    const v = {};
%s
    const F = %s;
    v.rimA = F[fin][0]; v.rimB = F[fin][1]; v.rimC = F[fin][2];
    return v;
  }
}''' % (seg_js('fin', 2, 'fin'), js([list(finishes[0]), list(finishes[1])]))
    return board7('Stickers and pins: the five shapes', 'The tab shapes as die-cut stickers and enamel pins, each in its area\'s colour, with a few word stickers for laptops and water bottles.', body, logic, 1760, 990, css=MERCH_CSS)


# ================================================================ The tote bag

TOTE_COLS = [('Evergreen', EVG, LIME, '#FFFFFF'), ('Night', NIGHT, LIME, MOON), ('Mist', '#DDE6E1', EVG, EVG)]


def tote():
    tex = ('<filter id="cotton"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3"></feTurbulence>'
           '<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .16 0"></feColorMatrix><feComposite in2="SourceGraphic" operator="in"></feComposite></filter>')
    bag = f'''<svg width="520" height="720" viewBox="0 0 520 720" role="img" aria-label="A tote bag" style="display: block; overflow: visible">
      <defs>{tex}<linearGradient id="fold" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".12"></stop><stop offset=".08" stop-color="#000" stop-opacity="0"></stop><stop offset=".92" stop-color="#000" stop-opacity="0"></stop><stop offset="1" stop-color="#000" stop-opacity=".14"></stop></linearGradient></defs>
      <path d="M150 190 C150 40 230 20 230 20 M370 190 C370 40 290 20 290 20" fill="none" style="stroke: [[ bagCol ]]" stroke-width="26" stroke-linecap="round"></path>
      <path d="M150 190 C150 40 230 20 230 20 M370 190 C370 40 290 20 290 20" fill="none" stroke="#000" stroke-opacity=".15" stroke-width="26" stroke-linecap="round" filter="url(#cotton)"></path>
      <path d="M40 180 L480 180 L470 700 L50 700 Z" style="fill: [[ bagCol ]]"></path>
      <path d="M40 180 L480 180 L470 700 L50 700 Z" fill="url(#fold)"></path>
      <path d="M40 180 L480 180 L470 700 L50 700 Z" fill="#000" filter="url(#cotton)"></path>
      <path d="M40 196 L480 196" stroke="#000" stroke-opacity=".12" stroke-width="2" stroke-dasharray="6 5"></path>
    </svg>'''
    stones_print = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" style="fill: {f}; stroke: [[ inkCol ]]" stroke-width="5"{d}></ellipse>'
                           for x, y, rx, ry, f, d in [(80, 210, 62, 24, '[[ inkCol ]]', ''), (200, 150, 66, 25, '[[ inkCol ]]', ''), (320, 88, 62, 24, '[[ accCol ]]', ''), (430, 34, 54, 21, 'none', ' stroke-dasharray="14 12"')])
    design_a = f'''<sc-if value="[[ dA ]]" hint-placeholder-val="[[ true ]]"><div style="position: absolute; left: 90px; top: 290px; width: 340px; display: flex; flex-direction: column; gap: 26px">
        <svg width="340" height="160" viewBox="0 0 500 240" aria-hidden="true" style="overflow: visible">{stones_print}</svg>
        <span style="font-size: 46px; font-weight: 600; letter-spacing: -0.05em; line-height: .95; color: [[ inkCol ]]">One step<br>at a time.</span></div></sc-if>'''
    row = ''.join(f'<span style="width: 58px; height: 58px; border-radius: 999px; box-shadow: inset 0 0 0 4px [[ inkCol ]]; display: flex; align-items: center; justify-content: center">{glyph(g, 30, "currentColor", 2.4)}</span>' for g, *_ in SHAPES)
    design_b = f'''<sc-if value="[[ dB ]]" hint-placeholder-val="[[ false ]]"><div style="position: absolute; left: 90px; top: 330px; width: 340px; display: flex; flex-direction: column; gap: 30px; color: [[ inkCol ]]">
        <span style="display: flex; gap: 12px">{row}</span>
        <span style="font-size: 50px; font-weight: 600; letter-spacing: -0.05em; line-height: .95">Money,<br>understood.</span></div></sc-if>'''
    scene = f'''<div style="position: relative; width: 760px; height: 820px; flex-shrink: 0; border-radius: {R_L}px; background: #D9DFDB; overflow: hidden">
      <div style="position: absolute; left: 120px; top: 50px; filter: drop-shadow(0 24px 30px rgba(16,24,20,.28))">{bag}</div>
      <div style="position: absolute; left: 120px; top: 50px; width: 520px; height: 720px">{design_a}{design_b}
        <span style="position: absolute; right: 70px; bottom: 50px; opacity: .9">{sty(lockup(22, '[[ inkCol ]]', '[[ accCol ]]'))}</span></div>
    </div>'''
    body = f'''  <div style="display: flex; gap: 40px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 16px">
      <div style="display: flex; gap: 20px; align-items: center">{seg('tc', [c[0] for c in TOTE_COLS], 'Bag colour')}{seg('td', ['One step at a time', 'Five shapes'], 'Print')}</div>{scene}</div>
    <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px; padding-top: 58px">
      {rules_card('Made to be used', ['Heavy cotton, 38 by 42 cm, long handles for the shoulder: big enough for the market or a laptop.', 'An inside pocket that fits the A6 notebook and a phone.', 'Printed in one or two colours, so it can be made by a local screen printer.'])}
      {rules_card('What it says', ['"One step at a time" is the stones, the Me shape: the whole product in one line.', 'The five shapes read as a set without a word; the lockup is small, on the corner.', 'No natural-canvas cream: evergreen, night or mist, like the app.'])}
      {rules_card('Choices worth checking', ['Given at workshops, or sold at cost, and made where (Q-48)?'])}
    </div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const tc = st.tc || 0, td = st.td || 0;
    const C = %s;
    const v = { bagCol: C[tc][1], accCol: C[tc][2], inkCol: C[tc][3], dA: td === 0, dB: td === 1 };
%s
%s
    return v;
  }
}''' % (js([list(c) for c in TOTE_COLS]), seg_js('tc', 3, 'tc'), seg_js('td', 2, 'td'))
    return board7('A tote bag', 'For the market, the commute and the workshop: a heavy cotton tote in the app\'s colours, with the stones or the five shapes. Try the colours and the two prints.', body, logic, 1760, 1150, css=MERCH_CSS)


# ================================================================ Ambassador T-shirts and a name badge

TEE_COLS = [('Evergreen', EVG, '#FFFFFF', LIME), ('Night', NIGHT, MOON, LIME), ('Lime', LIME, EVG, '#FFFFFF')]


def tee_svg(back=False):
    neck = 'Q250 52 330 28' if back else 'Q250 92 330 28'
    return f'''<svg width="500" height="560" viewBox="0 0 500 560" role="img" aria-label="A T-shirt, {'back' if back else 'front'}" style="display: block; overflow: visible">
      <path d="M170 28 {neck} L420 62 L492 168 L418 206 L398 176 L398 548 L102 548 L102 176 L82 206 L8 168 L80 62 Z" style="fill: [[ teeCol ]]"></path>
      <path d="M170 28 {neck} L420 62 L492 168 L418 206 L398 176 L398 548 L102 548 L102 176 L82 206 L8 168 L80 62 Z" fill="url(#teeShade)"></path>
      <path d="M170 28 {neck}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="10"></path>
    </svg>'''


SHIRT_RULES = rules_card('What the shirt may say', ['"Ask me about AWO", never "Ask me about your money": an ambassador shows the app; she doesn\'t advise.',
                                                   "The badge says the same in her words: what she can do, and what she can't.",
                                                   'No slogans about getting rich, and nothing a stranger could read as a lender.'])


def tshirts():
    defs = ('<svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs><linearGradient id="teeShade" x1="0" x2="1">'
            '<stop offset="0" stop-color="#000" stop-opacity=".16"></stop><stop offset=".22" stop-color="#000" stop-opacity="0"></stop><stop offset=".78" stop-color="#000" stop-opacity="0"></stop><stop offset="1" stop-color="#000" stop-opacity=".16"></stop></linearGradient></defs></svg>')
    front = f'''<div style="position: relative; width: 500px; height: 560px; filter: drop-shadow(0 20px 26px rgba(16,24,20,.25))">{tee_svg()}
      <span style="position: absolute; left: 282px; top: 150px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px">{sty(mark(40, '[[ inkCol ]]', '[[ accCol ]]'))}<span style="font-size: 20px; font-weight: 600; letter-spacing: -0.05em; color: [[ inkCol ]]">awo</span></span></div>'''
    back = f'''<div style="position: relative; width: 500px; height: 560px; filter: drop-shadow(0 20px 26px rgba(16,24,20,.25))">{tee_svg(True)}
      <div style="position: absolute; left: 140px; right: 140px; top: 130px; display: flex; flex-direction: column; gap: 18px; color: [[ inkCol ]]">
        <span style="font-size: 50px; font-weight: 600; letter-spacing: -0.05em; line-height: .95">Ask me about AWO</span>
        <span style="font-size: 17px; line-height: 1.35">Free money learning for women, at home and abroad.</span>
        <span style="display: flex; align-items: center; gap: 8px; margin-top: 30px">{sty(mark(28, '[[ inkCol ]]', '[[ accCol ]]'))}<span style="font-size: 15px; font-weight: 600">AWO ambassador</span></span></div></div>'''
    badge = f'''<div style="width: 300px; flex-shrink: 0; display: flex; flex-direction: column; align-items: center">
      <span aria-hidden="true" style="width: 18px; height: 70px; background: {EVG}; border-radius: 3px 3px 0 0"></span>
      <div style="width: 300px; border-radius: {R_L}px; background: #FFFFFF; box-shadow: 0 2px 3px rgba(16,24,20,.15), 0 20px 40px rgba(16,24,20,.18); overflow: hidden">
        <div style="background: {EVG}; padding: 16px 20px; display: flex; justify-content: space-between; align-items: center">{lockup(20, '#FFFFFF', LIME)}<span style="font-size: 12px; font-weight: 600; color: {ON_EVG}">Ambassador</span></div>
        <div style="padding: 18px 20px 20px; display: flex; flex-direction: column; gap: 12px">
          <span style="display: flex; gap: 12px; align-items: center"><img class="face" src="{IMG['thandi']}" alt="Thandi" style="width: 56px; height: 56px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.02em">Thandi</span><span style="font-size: 13px; color: {SEC}">Durban</span></span></span>
          <span style="display: flex; flex-direction: column; gap: 6px; font-size: 14px; line-height: 1.4">
            <span style="display: flex; gap: 8px">{icon('check', 16, EVG, 2.6)}I can show you the app and run a workshop.</span>
            <span style="display: flex; gap: 8px">{ic('close', 16, WARN_FG, 2.6)}I can't give financial advice, and I never ask for your PIN or money.</span></span>
        </div></div></div>'''
    body = f'''  {defs}<div style="display: flex; gap: 36px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 16px">
      <div style="display: flex; gap: 20px; align-items: center">{seg('tt', [c[0] for c in TEE_COLS], 'T-shirt colour')}</div>
      <div style="display: flex; gap: 24px; border-radius: {R_L}px; background: #D9DFDB; padding: 40px 30px 30px">
        <div style="display: flex; flex-direction: column; gap: 10px; align-items: center">{front}<span style="font-size: 14px; font-weight: 600; color: {SEC}">Front: the mark, small</span></div>
        <div style="display: flex; flex-direction: column; gap: 10px; align-items: center">{back}<span style="font-size: 14px; font-weight: 600; color: {SEC}">Back: an invitation</span></div>
      </div></div>
    <div style="display: flex; flex-direction: column; gap: 12px; padding-top: 58px">{label('And a name badge')}{badge}</div>
    <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px; padding-top: 58px">
      {SHIRT_RULES}
      {rules_card('Made to be worn', ['A fitted cut and a straight cut, XS to 4XL.', 'One-colour prints, so a local printer can make small runs.', 'Evergreen by default; night for evening events; lime for a crowd.'])}
      {rules_card('Choices worth checking', ['Is there an ambassador programme, and what may ambassadors say and hand out (Q-48)?'])}
    </div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const tt = st.tt || 0;
    const C = %s;
    const v = { teeCol: C[tt][1], inkCol: C[tt][2], accCol: C[tt][3] };
%s
    return v;
  }
}''' % (js([list(c) for c in TEE_COLS]), seg_js('tt', 3, 'tt'))
    return board7('Ambassador T-shirts', 'For the women who run AWO workshops and share the app: a shirt that invites questions, and a badge that says what an ambassador can and can\'t do.', body, logic, 1860, 1010, css=MERCH_CSS)


BOARDS = [('R9-Notebook', notebook), ('R9-Checkin-Magnet', calendar_board), ('R9-Stickers-Pins', stickers_pins), ('R9-Tote', tote), ('R9-Tshirts', tshirts)]
