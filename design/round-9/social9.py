"""Round 9, batch 5 (second half): social. Two carousels (1080 by 1350), two more WhatsApp status cards (1080 by
1920), the AWO Podcast's cover art and episode tiles.

Rules: educational only; the DIVA score always says what it is; sample numbers are marked; a member's words appear
in her own hand, and nobody's amounts appear on anything she might share."""
import json

from lib9 import *  # noqa: F401,F403
from marketing7 import H, K  # noqa: E402
from kit7 import board7  # noqa: E402
from around9 import rules_card, label  # noqa: E402

BAL = 'text-wrap: balance'
CW, CH = 1080, 1350


def js(o):
    return json.dumps(o, ensure_ascii=False)


def slide(bg, inner, fg=INK):
    return f'<div style="position: relative; width: {CW}px; height: {CH}px; overflow: hidden; background: {bg}; color: {fg}; flex-shrink: 0">{inner}</div>'


def c_foot(col, accent, text, sub):
    return (f'<div style="position: absolute; left: 80px; right: 80px; bottom: 72px; display: flex; justify-content: space-between; align-items: flex-end">'
            f'<span style="font-size: 30px; line-height: 1.35; color: {sub}">{text}</span>{lockup(56, col, accent)}</div>')


def swipe(col):
    return (f'<span style="position: absolute; right: 80px; top: 88px; display: flex; align-items: center; gap: 12px; font-size: 30px; font-weight: 600; color: {col}">Swipe'
            f'<span style="display: flex; transform: scaleX(-1)">{ic("back", 34, col, 2.6)}</span></span>')


def sample_tag(col):
    return f'<span style="height: 52px; padding: 0 18px; border-radius: {R_M}px; border: 2px dashed {col}; color: {col}; display: inline-flex; align-items: center; font-size: 24px; font-weight: 600">Sample</span>'


# ---------------------------------------------------------------- Carousel 1: the DIVA score, explained

def stage_stones(w=920, h=460, here=2, total=4):
    """Four stones: the ones behind her in evergreen, where she stands in lime, the ones ahead dashed."""
    rx, ry = 96, 36
    out = ''
    for i in range(total):
        x = rx + 6 + i * (w - 2 * rx - 12) / (total - 1)
        y = h - ry - 30 - i * (h - 2 * ry - 60) / (total - 1)
        if i < here:
            fill = LIME if i == here - 1 else EVG
            out += (f'<ellipse cx="{x:.0f}" cy="{y + 18:.0f}" rx="{rx}" ry="{ry}" fill="#BFD9D2"></ellipse>'
                    f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{EVG}" stroke-width="6"></ellipse>')
        else:
            out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" fill="none" stroke="{EVG}" stroke-width="6" stroke-dasharray="16 14"></ellipse>'
        if i == here - 1:
            out += f'<text x="{x:.0f}" y="{y - 70:.0f}" text-anchor="middle" font-size="36" font-weight="600" fill="{EVG}" font-family="Geist, sans-serif">You are here</text>'
    return f'<svg role="img" aria-label="Four stones. You are on the second." width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; overflow: visible">{out}</svg>'


def diva_slides():
    s = []
    s.append((slide(POOL, f'''<div style="position: absolute; left: 80px; top: 80px">{lockup(48, EVG, LIME)}</div>{swipe(EVG)}
      <h2 style="position: absolute; left: 80px; right: 80px; top: 250px; margin: 0; {H(150, EVG, BAL)}">What is a DIVA score?</h2>
      <div role="img" aria-label="A sample DIVA score of 63" style="position: absolute; right: 80px; bottom: 90px; width: 440px; height: 440px">{arc(440, 63, '#BFD9D2', EVG, sw=36)}
        <span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px"><span style="{H(170, EVG)}">63</span><span style="font-size: 32px; color: {SEC}">DIVA score</span></span></div>
      <div style="position: absolute; left: 80px; bottom: 100px">{sample_tag(EVG)}</div>'''),
        'A sample DIVA score of 63 in a ring, under the question: What is a DIVA score?'))
    rows = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 14px; padding: 26px 0; {"border-top: 2px solid #D3E0DA;" if i else ""}">
        <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 44px; font-weight: 600; color: {EVG}">{n}</span><span style="font-size: 40px; font-weight: 600; color: {EVG}; font-variant-numeric: tabular-nums">{v3}</span></span>
        <span style="height: 18px; border-radius: 4px; background: #D3E0DA; overflow: hidden"><span style="display: block; height: 100%; width: {v3}%; background: {EVG}"></span></span>
        <span style="font-size: 28px; line-height: 1.35; color: {SEC}">{d}</span></div>'''
                   for i, ((n, _w, v3, _v4, _d), d) in enumerate(zip(AREAS9, ['Bills get paid; most spending is planned.', 'Could a surprise cost be covered?', 'Knowing some ways to save, borrow and grow money.', 'Goals with a date and an amount.'])))
    s.append((slide(MIST, f'''<h2 style="position: absolute; left: 80px; right: 80px; top: 90px; margin: 0; {H(96, EVG, BAL)}">It looks at four parts of your money life.</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 360px; display: flex; flex-direction: column">{rows}</div>
      <div style="position: absolute; left: 80px; bottom: 72px">{sample_tag(SEC)}</div>'''),
        'Four areas with sample bars: Everyday money 71, Ready for surprises 48, Knowing your options 60, Clear goals 69.'))
    s.append((slide(POOL, f'''<h2 style="position: absolute; left: 80px; right: 80px; top: 90px; margin: 0; {H(96, EVG, BAL)}">And shows where you stand, as a stage.</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 430px">{stage_stones()}</div>
      <span style="position: absolute; left: 80px; top: 960px; {H(120, EVG)}">Stage 2 of 4</span>
      <p style="position: absolute; left: 80px; right: 80px; top: 1100px; margin: 0; font-size: 34px; line-height: 1.35; color: {SEC}">Each stage says what usually helps next.</p>'''),
        'Four stepping stones rising. Stage 2 of 4.'))
    s.append((slide(EVG, f'''<h2 style="position: absolute; left: 80px; right: 80px; top: 180px; margin: 0; {H(170, LIME, BAL)}">It is not a credit score.</h2>
      <p style="position: absolute; left: 80px; right: 120px; top: 760px; margin: 0; font-size: 44px; line-height: 1.35; color: #FFFFFF">It is for learning. It says nothing about loans or whether you can borrow, and only you see it.</p>
      {c_foot('#FFFFFF', LIME, '', ON_EVG)}''', '#FFFFFF'),
        'It is not a credit score. It is for learning, says nothing about loans, and only you see it.'))
    pts = [(80, 300, 55, 'Jul'), (330, 230, 59, 'Aug'), (580, 160, 63, 'Sep'), (830, 140, 64, 'Oct')]
    line = ' '.join(f'{"M" if i == 0 else "L"}{x} {y}' for i, (x, y, _v, _m) in enumerate(pts))
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="{LIME if i == 3 else "#FFFFFF"}" stroke="{EVG}" stroke-width="6"></circle>'
                   f'<text x="{x}" y="{y - 40}" text-anchor="middle" font-size="40" font-weight="600" fill="{EVG}">{v}</text><text x="{x}" y="380" text-anchor="middle" font-size="30" fill="{SEC}">{m}</text>'
                   for i, (x, y, v, m) in enumerate(pts))
    s.append((slide(POOL, f'''<h2 style="position: absolute; left: 80px; right: 80px; top: 90px; margin: 0; {H(96, EVG, BAL)}">Check in every 30 days. Watch it change.</h2>
      <svg role="img" aria-label="Sample versions: 55 in July, 59 in August, 63 in September, 64 in October" width="920" height="400" viewBox="0 0 920 400" style="position: absolute; left: 80px; top: 420px; overflow: visible; font-family: Geist, sans-serif"><path d="{line}" fill="none" stroke="{EVG}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"></path>{dots}</svg>
      <p style="position: absolute; left: 80px; right: 80px; top: 880px; margin: 0; font-size: 36px; line-height: 1.35; color: {SEC}">Old versions never change, so you can see how far you have come.</p>
      {c_foot(EVG, LIME, 'Get yours, free,<br>on AWO.', EVG)}'''),
        'Sample versions rising from 55 in July to 64 in October. Old versions never change. Get yours, free, on AWO.'))
    return s


CAROUSELS = {
    'diva': dict(title='Carousel: the DIVA score, explained', slides=diva_slides, h=1240,
                 desc='Five slides at 1080 by 1350 for Instagram and Facebook: what the score is, what it looks at, the stage, what it is not, and how it changes.',
                 caption='What is a DIVA score? Five slides, one minute. It shows where your money life stands today, in plain words, and it changes as you do. Free on AWO. For learning, never a credit score.',
                 rules=['The fourth slide exists so nobody reads the score as a credit score.', 'Every number is a sample and says so on the slide.', 'The last slide carries the only call to action.']),
}


# ---------------------------------------------------------------- Carousel 2: before you sign for a loan

def loan_slides():
    s = []
    doc_lines = ''.join(f'<span style="height: 18px; width: {w}%; border-radius: 4px; background: {"#E9F7A8" if hl else "#E4EAE6"}; box-shadow: {"inset 0 0 0 3px " + EVG if hl else "none"}"></span>'
                        for w, hl in [(80, False), (92, False), (60, True), (88, False), (74, True), (90, False), (66, False), (84, True), (52, False), (78, True), (70, False)])
    s.append((slide(LIME, f'''<div style="position: absolute; left: 80px; top: 80px">{lockup(48, EVG, '#FFFFFF')}</div>{swipe(EVG)}
      <h2 style="position: absolute; left: 80px; right: 80px; top: 230px; margin: 0; {H(124, EVG, BAL)}">Before you sign for a loan, find these four lines.</h2>
      <div aria-hidden="true" style="position: absolute; left: 180px; right: 180px; top: 740px; height: 700px; border-radius: {K}px; background: #FFFFFF; padding: 60px 56px; box-sizing: border-box; display: flex; flex-direction: column; gap: 26px; transform: rotate(-3deg); box-shadow: 0 30px 70px rgba(15,74,54,.25)">
        <span style="height: 34px; width: 50%; border-radius: 6px; background: {EVG}"></span>{doc_lines}</div>'''),
        'A loan agreement with four lines highlighted, under the words: Before you sign for a loan, find these four lines.'))
    split = [('Borrowed', 8000, EVG, '#FFFFFF'), ('Interest', 1433, '#5E8C7A', '#FFFFFF'), ('Fees', 1978, WARN_FG, '#FFFFFF')]
    bar = ''.join(f'<span style="flex: {v} 1 0; background: {bg}"></span>' for _n, v, bg, _f in split)
    keys = ''.join(f'<span style="display: flex; align-items: center; gap: 14px; font-size: 32px; color: {INK}"><span style="width: 28px; height: 28px; border-radius: 6px; background: {bg}"></span>{n}<b style="margin-left: auto; font-weight: 600; font-variant-numeric: tabular-nums">R {v:,}</b></span>'.replace(',', ' ') for n, v, bg, _f in split)
    s.append((slide(MIST, f'''<span style="position: absolute; left: 80px; top: 90px; {H(56, SEC)}">1</span>
      <h2 style="position: absolute; left: 80px; right: 80px; top: 170px; margin: 0; {H(96, EVG, BAL)}">What you pay back, in all.</h2>
      <p style="position: absolute; left: 80px; right: 80px; top: 420px; margin: 0; font-size: 36px; line-height: 1.35; color: {SEC}">Not the monthly amount. The whole thing.</p>
      <div style="position: absolute; left: 80px; right: 80px; top: 580px; display: flex; flex-direction: column; gap: 26px">
        <span style="display: flex; align-items: baseline; gap: 20px"><span style="{H(150, EVG)}">R 11 411</span><span style="font-size: 32px; color: {SEC}">for R 8 000</span></span>
        <span style="display: flex; height: 48px; border-radius: 8px; overflow: hidden">{bar}</span>
        <div style="display: flex; flex-direction: column; gap: 14px">{keys}</div></div>
      <div style="position: absolute; left: 80px; bottom: 72px; display: flex; align-items: center; gap: 18px">{sample_tag(SEC)}<span style="font-size: 26px; color: {SEC}">R 8 000 over 12 months at 27.75%, with fees</span></div>'''),
        'Number 1: what you pay back in all. A sample: R 11 411 for R 8 000, split into borrowed, interest and fees.'))
    fee = lambda n, v, sub: (f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 30px 0; border-top: 2px solid #D3E0DA">'
                             f'<span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 44px; font-weight: 600; color: {EVG}">{n}</span><span style="font-size: 28px; color: {SEC}">{sub}</span></span>'
                             f'<span style="font-size: 48px; font-weight: 600; color: {EVG}; font-variant-numeric: tabular-nums">{v}</span></div>')
    s.append((slide(MIST, f'''<span style="position: absolute; left: 80px; top: 90px; {H(56, SEC)}">2</span>
      <h2 style="position: absolute; left: 80px; right: 80px; top: 170px; margin: 0; {H(96, EVG, BAL)}">The fees, and when they come.</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 460px; display: flex; flex-direction: column">
        {fee('Initiation fee', 'R 1 150', 'Once, often added to what you borrow')}{fee('Service fee', 'R 69', 'Every month')}{fee('Over a year', 'R 1 978', 'On top of the interest')}</div>
      <div style="position: absolute; left: 80px; bottom: 72px">{sample_tag(SEC)}</div>'''),
        'Number 2: the fees. Sample: an initiation fee of R 1 150 and R 69 a month, R 1 978 over a year.'))
    s.append((slide(MIST, f'''<span style="position: absolute; left: 80px; top: 90px; {H(56, SEC)}">3</span>
      <h2 style="position: absolute; left: 80px; right: 80px; top: 170px; margin: 0; {H(96, EVG, BAL)}">The rate, and whether it can change.</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 520px; display: grid; grid-template-columns: 1fr 1fr; gap: 28px">
        <div style="border-radius: {K}px; background: #FFFFFF; padding: 40px; display: flex; flex-direction: column; gap: 16px"><span style="font-size: 44px; font-weight: 600; color: {EVG}">Fixed</span><span style="font-size: 30px; line-height: 1.35; color: {SEC}">Stays the same for the whole loan.</span></div>
        <div style="border-radius: {K}px; background: #FFFFFF; padding: 40px; display: flex; flex-direction: column; gap: 16px"><span style="font-size: 44px; font-weight: 600; color: {EVG}">Linked</span><span style="font-size: 30px; line-height: 1.35; color: {SEC}">Moves with a rate like prime, so it can go up.</span></div>
      </div>
      <p style="position: absolute; left: 80px; right: 80px; top: 900px; margin: 0; font-size: 34px; line-height: 1.35; color: {SEC}">Look for the words "fixed", "variable" or "linked to".</p>'''),
        'Number 3: the rate, and whether it can change. Fixed stays the same; linked can go up.'))
    words = ''.join(f'<span style="height: 84px; padding: 0 32px; border-radius: {R_L * 2}px; background: #FFFFFF; box-shadow: inset 0 0 0 3px {EVG}; display: inline-flex; align-items: center; font-size: 40px; font-weight: 600; color: {EVG}">{w}</span>' for w in ['Default', 'Arrears', 'Collection costs', 'Early settlement'])
    s.append((slide(MIST, f'''<span style="position: absolute; left: 80px; top: 90px; {H(56, SEC)}">4</span>
      <h2 style="position: absolute; left: 80px; right: 80px; top: 170px; margin: 0; {H(96, EVG, BAL)}">What happens if you miss a payment.</h2>
      <p style="position: absolute; left: 80px; right: 80px; top: 450px; margin: 0; font-size: 36px; line-height: 1.35; color: {SEC}">Find these words, and read the line they are in.</p>
      <div style="position: absolute; left: 80px; right: 80px; top: 600px; display: flex; flex-wrap: wrap; gap: 20px">{words}</div>
      <div style="position: absolute; left: 80px; right: 80px; top: 900px; border-radius: {K}px; background: #FFFFFF; padding: 40px 44px; display: flex; flex-direction: column; gap: 16px">
        <span style="font-size: 28px; font-weight: 600; color: {SEC}">A line might read</span>
        <span style="font-size: 36px; line-height: 1.4; color: {INK}">"If an instalment is not paid on the due date, the account is in <b style="font-weight: 600; background: #E9F7A8; box-shadow: 0 0 0 4px #E9F7A8">arrears</b> and <b style="font-weight: 600; background: #E9F7A8; box-shadow: 0 0 0 4px #E9F7A8">collection costs</b> may be added."</span>
        <span style="font-size: 26px; color: {SEC}">Sample wording. Yours will differ.</span></div>'''),
        'Number 4: what happens if you miss a payment. Words to find: default, arrears, collection costs, early settlement.'))
    s.append((slide(EVG, f'''<h2 style="position: absolute; left: 80px; right: 80px; top: 150px; margin: 0; {H(124, '#FFFFFF', BAL)}">Not sure what a line means? Ask before you sign.</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 700px; border-radius: {K}px; background: {LIME}; padding: 44px; display: flex; gap: 30px; align-items: center">
        <span style="width: 110px; height: 110px; flex-shrink: 0; border-radius: {R_L * 2}px; background: {EVG}; display: flex; align-items: center; justify-content: center">{hub_icon(None, 60, LIME, 2)}</span>
        <span style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 44px; font-weight: 600; color: {EVG}">Explain my agreement</span><span style="font-size: 30px; color: {EVG}">In the Hub, on AWO. Free.</span></span></div>
      {c_foot('#FFFFFF', LIME, 'AWO explains. It never tells<br>you whether to sign.', ON_EVG)}''', '#FFFFFF'),
        'Not sure what a line means? Ask before you sign. Explain my agreement, in the Hub on AWO. AWO explains; it never tells you whether to sign.'))
    return s


CAROUSELS['loan'] = dict(title='Carousel: before you sign for a loan', slides=loan_slides, h=1270,
                         desc='Six slides that teach what to look for in any loan agreement, and point to the Hub\'s loan tool. No lender is named, and it never says whether to borrow.',
                         caption='Before you sign for a loan, find four lines: what you pay back in all, the fees, the rate and whether it can change, and what happens if you miss a payment. Save this for later.',
                         rules=['Teaches what to look for; never whether to borrow, or from whom.', 'The sample loan matches the Hub\'s loan tool (R 8 000, 12 months), so the numbers agree everywhere.', 'Fees are in wine, the colour for costs; never red.'])


def carousel(key):
    c = CAROUSELS[key]
    S = c['slides']()
    sc = .5
    tiles = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px"><div style="width: {CW * sc:.0f}px; height: {CH * sc:.0f}px; border-radius: {R_M}px; overflow: hidden; box-shadow: 0 14px 40px rgba(16,24,20,.14)">
        <div style="width: {CW}px; height: {CH}px; transform: scale({sc}); transform-origin: 0 0">{html}</div></div><span style="font-size: 14px; font-weight: 600; color: {SEC}">Slide {i + 1}</span></div>''' for i, (html, _alt) in enumerate(S))
    alts = ''.join(f'<span style="display: flex; gap: 12px; font-size: 15px; line-height: 1.45; color: {SEC}"><b style="width: 60px; flex-shrink: 0; color: {INK}; font-weight: 600">Slide {i + 1}</b>{alt}</span>' for i, (_h, alt) in enumerate(S))
    w = 112 + len(S) * CW * sc + (len(S) - 1) * 28
    body = f'''  <div style="display: flex; gap: 28px">{tiles}</div>
  <div style="display: grid; grid-template-columns: 1fr 1.4fr 1fr; gap: 24px; align-items: start">
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 20px 22px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 17px; font-weight: 600">The post's caption</span><p style="margin: 0; font-size: 16px; line-height: 1.5; color: {SEC}">{c['caption']}</p></section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 20px 22px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 17px; font-weight: 600">Alt text, for each slide</span>{alts}</section>
    {rules_card('Choices worth checking', c['rules'])}
  </div>'''
    return board7(c['title'], c['desc'], body, static_logic9(), round(w), c['h'], chip='Sample content')


# ---------------------------------------------------------------- Two more WhatsApp status cards

def status_question():
    inner = f'''<div style="position: absolute; left: 90px; top: 110px">{lockup(52, BLUSH_INK, '#FFFFFF')}</div>
<svg width="900" height="900" viewBox="0 0 900 900" aria-hidden="true" style="position: absolute; left: 90px; top: 250px">
  <circle cx="450" cy="450" r="90" fill="{BLUSH_INK}"></circle><circle cx="450" cy="450" r="250" fill="none" stroke="{BLUSH_INK}" stroke-width="10"></circle><circle cx="450" cy="450" r="420" fill="none" stroke="{BLUSH_INK}" stroke-width="10" stroke-opacity=".35"></circle></svg>
<div style="position: absolute; left: 90px; right: 90px; top: 1180px; display: flex; flex-direction: column; gap: 30px">
  <span style="font-size: 40px; font-weight: 600; color: {BLUSH_2}">This week's question in the circles</span>
  <h1 style="margin: 0; {H(116, BLUSH_INK, BAL)}">What's one money habit your mother taught you?</h1>
</div>
<span style="position: absolute; left: 90px; right: 90px; bottom: 100px; font-size: 34px; line-height: 1.35; color: {BLUSH_2}">Answer in your circle on AWO. First names only.</span>'''
    return canvas_board('Status card: this week\'s question', 1080, 1920, BLUSH, inner)


def status_quiz():
    opt = lambda k, t, sub, on: (f'<div style="border-radius: {K}px; background: {LIME if on else RAISED}; color: {EVG if on else MOON}; padding: 40px 44px; display: flex; gap: 30px; align-items: center">'
                                 f'<span style="width: 90px; height: 90px; flex-shrink: 0; border-radius: 999px; background: {EVG if on else DEEP}; color: {LIME if on else MOON}; display: flex; align-items: center; justify-content: center; font-size: 44px; font-weight: 600">{k}</span>'
                                 f'<span style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 46px; font-weight: 600">{t}</span><span style="font-size: 32px; opacity: .8">{sub}</span></span></div>')
    inner = f'''<div style="position: absolute; left: 90px; top: 110px">{lockup(52, MOON, LIME)}</div>
<div style="position: absolute; left: 90px; right: 90px; top: 280px; display: flex; flex-direction: column; gap: 34px">
  <span style="font-size: 40px; font-weight: 600; color: {LIME}">A two-second quiz</span>
  <h1 style="margin: 0; {H(116, MOON, BAL)}">Same loan of R 8 000. Which costs more in all?</h1>
</div>
<div style="position: absolute; left: 90px; right: 90px; top: 900px; display: flex; flex-direction: column; gap: 26px">
  {opt('A', '12 months', 'R 951 a month', False)}
  {opt('B', '24 months', 'R 570 a month', True)}
</div>
<div style="position: absolute; left: 90px; right: 90px; top: 1440px; display: flex; flex-direction: column; gap: 18px">
  <span style="font-size: 44px; line-height: 1.3; color: {MOON}; {BAL}">B, by R 2 271. Smaller payments, more months of interest and fees.</span>
  <span style="font-size: 32px; line-height: 1.35; color: {NMUTED}">Sample numbers, from the loan tool in AWO's Hub. Do your own sums there.</span>
</div>'''
    return canvas_board('Status card: a quick quiz', 1080, 1920, NIGHT, inner)


# ---------------------------------------------------------------- The AWO Podcast: cover and episode tiles

def moon_art(size, col):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true" style="display: block">'
            f'<path d="M86 64A40 40 0 1 1 36 14a31 31 0 0 0 50 50z" fill="{col}"></path></svg>')


def cover(size=1000):
    k = size / 1000
    return (f'<div role="img" aria-label="The AWO Podcast cover: a lime moon on night, with the title" style="position: relative; width: {size}px; height: {size}px; overflow: hidden; background: {NIGHT}; flex-shrink: 0">'
            f'<div style="position: absolute; right: {-90 * k:.0f}px; top: {-70 * k:.0f}px">{moon_art(round(620 * k), LIME)}</div>'
            f'<div style="position: absolute; left: {70 * k:.0f}px; top: {70 * k:.0f}px">{mark(round(70 * k), MOON, LIME)}</div>'
            f'<span style="position: absolute; left: {66 * k:.0f}px; right: {60 * k:.0f}px; bottom: {150 * k:.0f}px; font-size: {205 * k:.1f}px; font-weight: 600; letter-spacing: -0.055em; line-height: .86; color: {MOON}">The AWO<br>Podcast</span>'
            f'<span style="position: absolute; left: {72 * k:.0f}px; bottom: {72 * k:.0f}px; font-size: {34 * k:.1f}px; color: {NMUTED}">Money stories from women who\'ve lived them</span></div>')


def podcast_cover():
    sizes = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 10px; align-items: flex-start"><div style="border-radius: {max(4, round(s * .06))}px; overflow: hidden; box-shadow: 0 8px 20px rgba(16,24,20,.18)">
        <div style="width: {s}px; height: {s}px; overflow: hidden"><div style="width: 1000px; height: 1000px; transform: scale({s / 1000}); transform-origin: 0 0">{cover()}</div></div></div><span style="font-size: 14px; color: {SEC}">{s} px{n}</span></div>'''
                    for s, n in [(300, ', a show page'), (160, ', a search result'), (88, ', a list'), (55, ', the smallest, in a car')])
    inner = f'''<div style="position: absolute; left: 56px; top: 56px; border-radius: {R_L}px; overflow: hidden; box-shadow: 0 30px 70px rgba(16,24,20,.25)">{cover(1000)}</div>
<div style="position: absolute; left: 1112px; right: 56px; top: 56px; bottom: 56px; display: flex; flex-direction: column; gap: 22px">
  <h1 style="margin: 0; {H(56, INK)}">The AWO Podcast: cover art</h1>
  <p style="margin: 0; font-size: 18px; line-height: 1.45; color: {SEC}">Learn's moon, in lime on night, and the name set big enough to read at the size of a thumbnail.</p>
  {label('At the sizes people see it')}
  <div style="display: grid; grid-template-columns: auto auto; justify-content: start; gap: 22px 28px; align-items: end">{sizes}</div>
  {rules_card('Made to the rules', ['3000 by 3000 pixels, RGB, JPEG or PNG, as podcast apps ask; drawn here at 1000.', 'At 55 pixels the moon and "AWO" still read; the line under the name is allowed to go.', "No faces on the show's cover. Guests go on the episode tiles."])}
</div>'''
    return screen_board('The AWO Podcast: cover art', 1760, 1112, '#E4EAE6', inner, static_logic9())


EPISODES = [(12, 'Closing a shop, and opening a better one', 'Amara, Accra', IMG['amara_coat'], '55% 25%'),
            (13, 'A stall, a notebook and a slow month', 'Wanjiru, Nairobi', IMG['wanjiru_stall'], '62% 30%'),
            (14, 'My first payslip, line by line', 'Naledi, Johannesburg', IMG['naledi_cafe'], '30% 35%'),
            (15, 'Four debts, paid off one at a time', 'Thandi, Durban', IMG['thandi_window'], '50% 30%')]


def ep_tile(n, t, who, src, pos):
    return f'''<div style="position: relative; width: 1080px; height: 1080px; overflow: hidden; background: {NIGHT}; color: {MOON}; flex-shrink: 0">
  <img src="{src}" alt="{who.split(',')[0]}, this episode's guest" style="position: absolute; left: 80px; top: 80px; width: 520px; height: 560px; object-fit: cover; object-position: {pos}; border-radius: 260px 260px {K}px {K}px">
  <div style="position: absolute; right: 80px; top: 80px; display: flex; flex-direction: column; align-items: flex-end; gap: 24px">{moon_art(150, LIME)}<span style="height: 64px; padding: 0 26px; border-radius: {R_L}px; background: {LIME}; color: {EVG}; display: inline-flex; align-items: center; font-size: 32px; font-weight: 600">Episode {n}</span></div>
  <h2 style="position: absolute; left: 80px; right: 80px; top: 690px; margin: 0; {H(82, MOON, BAL)}">{t}</h2>
  <span style="position: absolute; left: 80px; bottom: 76px; font-size: 30px; color: {NMUTED}">{who}. A sample guest.</span>
  <span style="position: absolute; right: 80px; bottom: 70px">{lockup(40, MOON, LIME)}</span>
</div>'''


def podcast_tiles():
    sc = .4
    tiles = ''.join(f'<div style="width: {1080 * sc:.0f}px; height: {1080 * sc:.0f}px; border-radius: {R_M}px; overflow: hidden; box-shadow: 0 14px 40px rgba(16,24,20,.18)"><div style="width: 1080px; height: 1080px; transform: scale({sc}); transform-origin: 0 0">{ep_tile(*e)}</div></div>' for e in EPISODES)
    rows = ''.join(f'''<div style="display: flex; gap: 14px; align-items: center; padding: 12px 0; {"border-top: 1px solid " + NLINE + ";" if i else ""}">
        <div style="width: 64px; height: 64px; flex-shrink: 0; border-radius: 8px; overflow: hidden"><div style="width: 1080px; height: 1080px; transform: scale({64 / 1080:.5f}); transform-origin: 0 0">{ep_tile(*e)}</div></div>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 13px; color: {NMUTED}">Episode {e[0]}, {e[2].split(",")[0]}</span><span style="font-size: 16px; font-weight: 600; line-height: 1.3; color: {MOON}">{e[1]}</span></span>
        <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon("play", 18, INK)}</span></div>''' for i, e in enumerate(reversed(EPISODES)))
    body = f'''  <div style="display: flex; gap: 28px">{tiles}</div>
  <div style="display: flex; gap: 28px; align-items: flex-start">
    <section style="width: 432px; flex-shrink: 0; border-radius: {R_L}px; background: {DEEP}; padding: 14px 20px; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 600; color: {NMUTED}; padding: 6px 0 4px">In a list, at 64 pixels</span>{rows}</section>
    {rules_card('How the tiles work', ["1080 by 1080, for the feed, WhatsApp and the episode page. The show's cover stays the same; the tile changes.", 'The guest sits in an arch, the same shape for every guest; her own photo, with her consent.', 'The title does the work: one line of what happened, in her words where possible.'])}
    {rules_card('Choices worth checking', ['Guests are samples. Real guests sign a release that says where their story and photo appear (to confirm).', 'No amounts in titles, even when the story has them.', 'Episode numbers are real sequence, not decoration: listeners use them to find their place.'])}
  </div>'''
    w = 112 + 4 * 432 + 3 * 28
    return board7('The AWO Podcast: episode tiles', 'One tile per episode, each with its guest, for the feed, WhatsApp and the podcast apps. The list shows how they read at 64 pixels.', body, static_logic9(), w, 1150, chip='Sample content')


BOARDS = [('R9-Carousel-Diva', lambda: carousel('diva')), ('R9-Carousel-Loan', lambda: carousel('loan')),
          ('R9-Status-Question', status_question), ('R9-Status-Quiz', status_quiz),
          ('R9-Podcast-Cover', podcast_cover), ('R9-Podcast-Tiles', podcast_tiles)]
