"""Round 9, batch 3: other sizes and channels.

Desktop and tablet layouts of the member app, the check-in on WhatsApp and on USSD, and one question rendered in
every channel. The point (doc 02): one question graph, many renderers. Each question is written once, with a short
label and five or fewer options, and every channel draws it in its own way. WhatsApp and USSD come late (D-009);
designing them now keeps the questions honest. The providers and journeys are open (Q-21)."""
import json

from lib9 import *  # noqa: F401,F403
from goals8 import MINE
from hub8 import mini_pool

MOBILE_BG = '#EFE7DE'   # a chat ground
OUT_BUBBLE = '#D9FDD3'  # her replies


def js(o):
    return json.dumps(o, ensure_ascii=False)


# ---------------------------------------------------------------- desktop and tablet navigation

NAV = [('Home', 'pool', 'R8-Home.dc.html'), ('Learn', 'moon', 'R8-Learn.dc.html'), ('Hub', 'hub', 'R8-Hub.dc.html'),
       ('Community', 'ripple', 'R8-Feed.dc.html'), ('Me', 'stones', 'R7-Me.dc.html')]


def glyph(g, size, col):
    return hub_icon(None, size, col) if g == 'hub' else icon(g, size, col)


def side_nav(active, dark=False):
    """The five areas down the side, each in its own colour when chosen; then search, notifications and help."""
    bg = DEEP if dark else '#FFFFFF'
    idle = NMUTED if dark else SEC
    line = NLINE if dark else LINE7
    items = ''
    for name, g, href in NAV:
        if name == active:
            pb, fg, _lc = ACTIVE8[name]
            items += (f'<a href="{href}" aria-current="page" style="height: 48px; border-radius: {R_M}px; background: {pb}; color: {fg}; display: flex; align-items: center; gap: 12px; padding: 0 14px; font-size: 15px; font-weight: 600">'
                      f'{glyph(g, 20, fg)}{name}</a>')
        else:
            items += f'<a href="{href}" style="height: 48px; border-radius: {R_M}px; color: {idle}; display: flex; align-items: center; gap: 12px; padding: 0 14px; font-size: 15px; font-weight: 500">{glyph(g, 20, idle)}{name}</a>'
    extra = ''.join(f'<a href="{href}" style="height: 44px; border-radius: {R_M}px; color: {idle}; display: flex; align-items: center; gap: 12px; padding: 0 14px; font-size: 14px; font-weight: 500">{ic8(g, 18, idle)}<span style="flex-grow: 1">{t}</span>{badge}</a>'
                    for g, t, href, badge in [('search', 'Search', 'R9-Search.dc.html', f'<span style="font-size: 12px; color: {idle}; border: 1px solid {line}; border-radius: 4px; padding: 1px 5px">Ctrl K</span>'),
                                              ('bell', 'Notifications', 'R9-Notifications.dc.html', f'<span style="min-width: 22px; height: 22px; border-radius: 999px; background: {LIME}; color: {EVG}; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center">3</span>'),
                                              ('question', 'Help', 'R9-Help.dc.html', '')])
    return f'''<nav aria-label="Main" style="position: absolute; left: 0; top: 0; bottom: 0; width: 248px; box-sizing: border-box; background: {bg}; border-right: 1px solid {line}; padding: 28px 16px 20px; display: flex; flex-direction: column; gap: 6px">
    <div style="padding: 0 10px 22px">{lockup(30, MOON if dark else EVG, LIME)}</div>
    {items}
    <span style="height: 1px; background: {line}; margin: 14px 4px"></span>
    {extra}
    <div style="flex-grow: 1"></div>
    <a href="R7-Settings.dc.html" style="display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: {R_M}px"><img class="face" src="{IMG['naledi']}" alt="" style="width: 40px; height: 40px"><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 14px; font-weight: 600">Naledi</span><span style="font-size: 12px; color: {idle}">Johannesburg</span></span></a>
  </nav>'''


def desk_top(date, heading, right=''):
    return f'''<header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px">
      <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {MUTED}">{date}</span><h1 class="d" style="font-size: 48px">{heading}</h1></div>
      <div style="display: flex; align-items: center; gap: 12px">{right}
        <a href="R9-Search.dc.html" style="width: 320px; height: 48px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 14px; font-size: 15px; color: {MUTED}">{icon('search', 18, INK)}<span style="flex-grow: 1">Search words, lessons, tools</span><span style="font-size: 12px; border: 1px solid {LINE}; border-radius: 4px; padding: 1px 5px">Ctrl K</span></a>
      </div></header>'''


# ---------------------------------------------------------------- Desktop: Home

def desk_home():
    coming = [('Fri 30 Oct', 'Payday', 'Your step: R 150 to your safety net', 'pool', EVG, LIME), ('Thu 5 Nov', 'Kopano stokvel', "The pot goes to Mpho", 'people', POOL, EVG),
              ('Thu 12 Nov', 'A reminder', 'Check-in 5 is tomorrow', 'bell', MIST, EVG), ('Fri 13 Nov', 'Check-in 5', 'Three questions, then what changed', 'stones', POOL, EVG)]
    COMING = ''.join(f"""<div style="display: flex; flex-direction: column; gap: 8px; padding-right: 16px; {'border-left: 1px solid ' + LINE7 + '; padding-left: 16px;' if i else ''}">
          <span style="font-size: 13px; font-weight: 600; color: {MUTED}">{d}</span><span style="width: 40px; height: 40px; border-radius: 10px; background: {bg}; display: flex; align-items: center; justify-content: center">{icon(g, 20, fg) if g in ('pool', 'stones') else ic8(g, 20, fg)}</span>
          <span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">{sub}</span></div>""" for i, (d, t, sub, g, bg, fg) in enumerate(coming))
    PICK = ''.join(f"""<a href="{h}" style="min-height: 56px; display: flex; align-items: center; gap: 12px; {'border-top: 1px solid ' + LINE7 + ';' if i else ''}"><span style="width: 40px; height: 40px; border-radius: 10px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span>
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MUTED}">{sub}</span></span>{icon('chev', 16, MUTED)}</a>""" for i, (g, t, sub, h) in enumerate([('down', 'Debt plan', '2 of 3 debts added', 'R8-Tool-Debt.dc.html'), ('key', 'Moving-out goal', 'Add the first-month costs', 'R8-Goals.dc.html')]))
    goals = ''.join(f'''<a href="R8-Goals.dc.html" style="flex: 1 1 0; border-radius: {R_L}px; background: {EVG if i == 0 else "#FFFFFF"}; color: {"#FFFFFF" if i == 0 else INK}; padding: 14px; display: flex; gap: 12px; align-items: center">
        {mini_pool(round(have / want * 100), f"dh{i}", i)}<span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 13px; font-weight: 600; color: {ON_EVG if i == 0 else MUTED}">{n}</span><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.03em; color: {LIME if i == 0 else EVG}">{fmt_r(have, False)}</span><span style="font-size: 12px; color: {ON_EVG if i == 0 else MUTED}">of {fmt_r(want, False)}</span></span></a>''' for i, (n, have, want, _g) in enumerate(MINE))
    faces = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="position: relative; width: 56px; height: 56px"><span style="position: absolute; inset: 0; border-radius: 999px; box-shadow: inset 0 0 0 2.5px #F29BB5"></span><img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: 5px; top: 5px; width: 46px; height: 46px"></span><span style="font-size: 13px">{k.capitalize()}</span></span>' for k in ('wanjiru', 'amara', 'thandi', 'grace'))
    card = f'border-radius: {R_L}px; padding: 22px; display: flex; flex-direction: column; gap: 12px'
    inner = f'''  {side_nav('Home')}
  <main style="position: absolute; left: 248px; right: 0; top: 0; bottom: 0; padding: 36px 44px; box-sizing: border-box; display: flex; flex-direction: column; gap: 28px">
    {desk_top('Friday 25 September, payday', 'Hey Naledi')}
    <div style="display: grid; grid-template-columns: 1.25fr 1fr 1fr; gap: 24px; align-items: start">
      <div style="display: flex; flex-direction: column; gap: 24px">
        <section style="{card}; background: {EVG}; color: #FFFFFF">
          <span style="font-size: 14px; font-weight: 600; color: {ON_EVG}">This month's step</span>
          <span class="d" style="font-size: 36px; color: {LIME}">Raise your payday move to R 150</span>
          <span style="font-size: 15px; line-height: 1.45; color: {ON_EVG}">Payday is Friday 30 October. We'll remind you that morning.</span>
          <div style="display: flex; gap: 10px; margin-top: 4px"><a href="R9-Next-Step.dc.html" style="height: 48px; padding: 0 18px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Mark it done</a><a href="R9-Next-Step.dc.html" style="height: 48px; padding: 0 16px; border-radius: {R_M}px; background: rgba(255,255,255,.12); color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center">Change it</a></div>
        </section>
        <section style="display: flex; flex-direction: column; gap: 12px"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Your goals</span><a href="R8-Goals.dc.html" style="min-height: 44px; display: flex; align-items: center; font-size: 14px; font-weight: 600; color: {EVG}">Goals studio</a></span>
          <div style="display: flex; gap: 12px">{goals}</div></section>
      </div>
      <div style="display: flex; flex-direction: column; gap: 24px">
        <a href="R9-What-Changed.dc.html" style="{card}; background: {POOL}; color: {EVG}">
          <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 14px; font-weight: 600">Your DIVA profile</span>{sample_chip(EVG)}</span>
          <span style="display: flex; align-items: flex-end; justify-content: space-between"><span style="display: flex; flex-direction: column; gap: 4px"><span class="d" style="font-size: 40px; white-space: nowrap">Stage 2</span><span style="font-size: 15px; font-weight: 600">of 4 stages</span></span>
            <span role="img" aria-label="DIVA score 64 of 100" style="position: relative; width: 104px; height: 104px">{arc(104, 64, '#B7D5CE', EVG, sw=9)}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 4px"><span style="font-size: 30px; font-weight: 600; letter-spacing: -0.03em">64</span><span style="font-size: 12px">DIVA score</span></span></span></span>
          <span style="font-size: 15px; line-height: 1.45; color: {INK}">Version 4 is here: ready for surprises moved most. See what changed.</span>
        </a>
        <a href="R8-Tool-Payslip.dc.html" style="{card}; background: {LIME}; color: {EVG}">
          <span style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{hub_icon(None, 18, EVG)}From the Hub</span>
          <span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.2; color: {INK}">Pay-day was today. Decode your payslip: what came off, and why.</span>
          <span style="font-size: 14px; font-weight: 600">About two minutes</span>
        </a>
      </div>
      <div style="display: flex; flex-direction: column; gap: 24px">
        <section style="{card}; background: #FFFFFF"><span style="display: flex; justify-content: space-between"><span style="font-size: 17px; font-weight: 600">Wins this week</span>{sample_chip()}</span><div style="display: flex; justify-content: space-between">{faces}</div></section>
        <a href="R8-Post.dc.html" style="{card}; background: {BLUSH}; color: {BLUSH_INK}"><span style="font-size: 13px; font-weight: 600">This week's question, Safety net circle</span><span style="font-size: 20px; font-weight: 600; line-height: 1.25">Where do you keep your safety net?</span><span style="font-size: 14px">3 replies, including yours</span></a>
        <a href="R7-Lesson.dc.html" style="{card}; background: {NIGHT}; color: {MOON}"><span style="display: flex; align-items: center; gap: 10px">{moon(26, 'half', now=True)}<span style="font-size: 13px; color: {NMUTED}">Keep learning, lesson 3 of 6</span></span><span style="font-size: 20px; font-weight: 600; line-height: 1.25">Savings groups, in three minutes</span><span style="font-size: 14px; color: {NMUTED}">Told through Thandi's story</span></a>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 2.25fr 1fr; gap: 24px">
      <section style="{card}; background: #FFFFFF"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Coming up</span><span style="font-size: 13px; color: {MUTED}">The next 30 days</span></span>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; position: relative; margin-top: 6px">{COMING}</div></section>
      <section style="{card}; background: #FFFFFF"><span style="font-size: 17px; font-weight: 600">Pick up where you left off</span>{PICK}</section>
    </div>
  </main>'''
    return screen_board('Home, on a computer', 1440, 1000, MIST, inner, static_logic())


# ---------------------------------------------------------------- Desktop: the DIVA profile

def desk_me():
    rows = ''.join(f'''<div style="display: grid; grid-template-columns: 210px 1fr 48px; gap: 18px; align-items: center; padding: 14px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">{n}</span><span style="font-size: 13px; color: {MUTED}">{d}</span></span>
        <span aria-hidden="true" style="position: relative; height: 12px; border-radius: 2px; background: {LINE7}; overflow: hidden"><span style="position: absolute; left: 0; top: 0; bottom: 0; width: {v4}%; background: {EVG}; transform-origin: 0 0; animation: fill .7s cubic-bezier(.2,.8,.2,1) {0.1 + i * 0.08:.2f}s both"></span><span style="position: absolute; top: 0; bottom: 0; left: {v3}%; width: 2px; background: {INK}; opacity: .5"></span></span>
        <span style="font-size: 22px; font-weight: 600; text-align: right; font-variant-numeric: tabular-nums">{v4}</span></div>''' for i, (n, d, v3, v4, _vd) in enumerate(AREAS9))
    vers = [(1, '13 Jul', 55), (2, '13 Aug', 59), (3, '13 Sep', 63), (4, '13 Oct', 64)]
    pts = ' '.join(f'{40 + k * 180},{150 - (v - 50) * 8}' for k, (_n, _d, v) in enumerate(vers))
    dots = ''.join(f'<circle cx="{40 + k * 180}" cy="{150 - (v - 50) * 8}" r="7" fill="{EVG if k == 3 else "#FFFFFF"}" stroke="{EVG}" stroke-width="2.5"></circle>' for k, (_n, _d, v) in enumerate(vers))
    labels = ''.join(f'<span style="position: absolute; left: {40 + k * 180 - 50}px; top: 178px; width: 100px; text-align: center; font-size: 13px; color: {SEC}"><b style="font-weight: 600; color: {INK}">{v}</b><br>{d}, v{n}</span>' for k, (n, d, v) in enumerate(vers))
    st_pts = [(42, 126, 34, 13), (139, 95, 37, 14), (235, 64, 37, 14), (330, 35, 31, 12)]
    dash = ' stroke-dasharray="8 8"'
    stones = ''.join(f'<ellipse cx="{x}" cy="{y + 9}" rx="{rx}" ry="{ry}" fill="{"#BFD9D2" if i < 2 else "none"}"></ellipse><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[EVG, LIME, "none", "none"][i]}" stroke="{EVG}" stroke-width="3"{dash if i > 1 else ""}></ellipse>' for i, (x, y, rx, ry) in enumerate(st_pts))
    card = f'border-radius: {R_L}px; padding: 26px; display: flex; flex-direction: column; gap: 14px'
    right = f'<a href="R7-Compare.dc.html" style="height: 48px; padding: 0 16px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1.5px {EVG}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Compare versions</a><a href="R7-Report.dc.html" style="height: 48px; padding: 0 16px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px">{ic("download", 18, "#FFFFFF")}The report (PDF)</a>'
    inner = f'''  {side_nav('Me')}
  <main style="position: absolute; left: 248px; right: 0; top: 0; bottom: 0; padding: 36px 44px; box-sizing: border-box; display: flex; flex-direction: column; gap: 28px">
    {desk_top('Version 4, 13 October 2026', 'Your DIVA profile', right)}
    <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 24px; align-items: start">
      <section style="{card}; background: {POOL}; color: {EVG}">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Where you stand</span>{sample_chip(EVG)}</span>
        <span style="display: flex; align-items: flex-end; justify-content: space-between"><span style="display: flex; align-items: baseline; gap: 10px; white-space: nowrap"><span class="d" style="font-size: 60px">Stage 2</span><span style="font-size: 18px; font-weight: 600">of 4</span></span>
          <span role="img" aria-label="DIVA score 64 of 100" style="position: relative; width: 132px; height: 132px">{arc(132, 64, '#B7D5CE', EVG, sw=11)}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 4px"><span style="font-size: 38px; font-weight: 600; letter-spacing: -0.03em">64</span><span style="font-size: 13px">DIVA score</span></span></span></span>
        <div role="img" aria-label="Four stepping stones. You are on stage 2." style="position: relative; height: 150px"><svg width="370" height="150" viewBox="0 0 370 150" aria-hidden="true" style="position: absolute; left: 0; top: 0">{stones}</svg><img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 119px; top: 44px; width: 40px; height: 40px; box-shadow: 0 0 0 3px {LIME}"></div>
        <span style="border-top: 1px solid rgba(15,74,54,.16); padding-top: 14px; display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 600; color: {INK}">What this means</span>{REVIEWED}</span>
        <p style="font-size: 16px; line-height: 1.55; color: {INK}">Everyday money is your strength: bills get paid and most spending is planned. The most room to grow is being ready for surprises, and it moved most this month.</p>
        <span style="font-size: 13px; color: {SEC}">Learning readiness, never a credit score. Worked out on AWO's servers, the same way for everyone.</span>
      </section>
      <div style="display: flex; flex-direction: column; gap: 24px">
        <section style="{card}; background: #FFFFFF; gap: 4px"><span style="display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 6px"><span style="font-size: 17px; font-weight: 600">Your four areas</span><span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}"><span style="width: 2px; height: 12px; background: {INK}; opacity: .5"></span>September</span></span>{rows}</section>
        <section style="{card}; background: #FFFFFF"><span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Your versions</span><span style="font-size: 13px; color: {MUTED}">Old versions never change</span></span>
          <div role="img" aria-label="DIVA score 55, 59, 63, then 64" style="position: relative; height: 220px"><svg width="620" height="170" viewBox="0 0 620 170" aria-hidden="true" style="display: block; overflow: visible"><polyline points="{pts}" fill="none" stroke="{EVG}" stroke-width="2.5"></polyline>{dots}</svg>{labels}</div></section>
      </div>
    </div>
  </main>'''
    return screen_board('Your DIVA profile, on a computer', 1440, 900, MIST, inner, static_logic())


# ---------------------------------------------------------------- Tablet: Learn, list and lesson side by side

def tablet_learn():
    lessons = [('Why groups work', 'done'), ('Your share, your turn', 'done'), ('Savings groups, in three minutes', 'now'), ('When someone can’t pay', 'next'), ('Keeping the record', 'next'), ('From a group to a goal', 'next')]
    rows = ''
    for i, (t, s) in enumerate(lessons):
        lead = moon(26, 'full' if s == 'done' else ('half' if s == 'now' else 'new'), now=(s == 'now'))
        bg = RAISED if s == 'now' else 'transparent'
        sub = {'done': 'Done', 'now': 'In progress, card 2 of 5', 'next': '3 minutes'}[s]
        rows += f'<a href="R7-Lesson.dc.html" style="min-height: 64px; border-radius: {R_M}px; background: {bg}; padding: 0 14px; display: flex; align-items: center; gap: 14px">{lead}<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {NMUTED}">{sub}</span></span></a>'
    tabs = ''.join(f'<span style="flex: 1 1 0; height: 40px; border-radius: 8px; {"background: " + MINT + "; color: " + NIGHT + ";" if i == 0 else "color: " + NMUTED + ";"} font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 6px">{t}</span>' for i, t in enumerate(['Paths', 'Words', 'Stories']))
    cur = 'aria-current="page"'
    rail = ''.join(f'<a href="{href}" aria-label="{n}" {cur if n == "Learn" else ""} style="width: 56px; height: 56px; border-radius: {R_M}px; {"background: " + MINT + ";" if n == "Learn" else ""} display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; color: {NIGHT if n == "Learn" else NMUTED}; font-size: 12px; font-weight: 600">{glyph(g, 20, NIGHT if n == "Learn" else NMUTED)}</a>' for n, g, href in NAV)
    circle = ''
    import math
    for k in range(12):
        a = math.radians(k * 30 - 90)
        x, y = 170 + 130 * math.cos(a), 150 + 130 * math.sin(a)
        circle += f'<span style="position: absolute; left: {x - 15:.0f}px; top: {y - 15:.0f}px; width: 30px; height: 30px; border-radius: 999px; background: {RAISED}; box-shadow: inset 0 0 0 2px {NLINE}"></span>'
    inner = f'''  <nav aria-label="Main" style="position: absolute; left: 0; top: 0; bottom: 0; width: 88px; background: {DEEP}; border-right: 1px solid {NLINE}; display: flex; flex-direction: column; align-items: center; gap: 10px; padding-top: 28px">{mark(28, MOON, LIME)}<span style="height: 18px"></span>{rail}</nav>
  <section style="position: absolute; left: 88px; top: 0; bottom: 0; width: 392px; box-sizing: border-box; background: {DEEP}; padding: 32px 20px; display: flex; flex-direction: column; gap: 18px">
    <h1 class="d" style="font-size: 40px">Learn</h1>
    <div style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {NIGHT}">{tabs}</div>
    <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 17px; font-weight: 600">Saving together</span><span style="font-size: 13px; color: {NMUTED}">2 of 6 done</span></span>
    <div style="display: flex; flex-direction: column; gap: 4px">{rows}</div>
  </section>
  <section style="position: absolute; left: 480px; right: 0; top: 0; bottom: 0; padding: 32px 56px; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px">
    <div style="display: flex; gap: 6px">{''.join(f'<span style="flex: 1 1 0; height: 4px; border-radius: 2px; background: {MOON if i < 2 else NLINE}"></span>' for i in range(5))}</div>
    <header style="display: flex; justify-content: space-between; align-items: center"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Savings groups, in three minutes</span><span style="font-size: 13px; color: {NMUTED}">Lesson 3 of 6, card 2 of 5</span></span>
      <span style="display: flex; gap: 8px"><button aria-label="Save for offline" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; color: {MOON}; display: flex; align-items: center; justify-content: center">{ic8('download', 20)}</button><a href="R8-Learn.dc.html" aria-label="Close the lesson" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {RAISED}; display: flex; align-items: center; justify-content: center">{ic('close', 20, MOON, 2.2)}</a></span></header>
    <div style="display: flex; gap: 48px; align-items: center; flex-grow: 1">
      <div role="img" aria-label="Twelve members in a circle. The pot moves from one to the next each month." style="position: relative; width: 340px; height: 300px; flex-shrink: 0">{circle}
        <span style="position: absolute; left: 155px; top: 5px; width: 30px; height: 30px; border-radius: 999px; background: {LIME}; box-shadow: 0 0 22px rgba(216,243,106,.5)"></span>
        <span style="position: absolute; left: 100px; top: 116px; width: 140px; text-align: center; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 30px; font-weight: 600; letter-spacing: -0.03em; color: {LIME}">R 6 000</span><span style="font-size: 13px; color: {NMUTED}">in the pot this month</span></span></div>
      <div style="display: flex; flex-direction: column; gap: 16px; max-width: 320px">
        <h2 class="d" style="font-size: 36px">Each month, all twelve pay in R 500.</h2>
        <p style="font-size: 18px; line-height: 1.5; color: {NMUTED}">One member takes the whole pot home. Next month, it's someone else's turn.</p>
        <div style="display: flex; gap: 12px; align-items: flex-start; border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: {RAISED}; padding: 14px"><span style="flex-shrink: 0">{ola('tl', 44)}</span><span style="font-size: 15px; line-height: 1.45">Think of the pot moving around the circle.</span></div>
      </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; color: {NMUTED}">Tap the right side, or press the arrow keys</span>
      <span style="display: flex; gap: 10px"><a href="R7-Lesson.dc.html" style="height: 52px; padding: 0 20px; border-radius: {R_M}px; background: {RAISED}; color: {MOON}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Back</a><a href="R7-Lesson.dc.html" style="height: 52px; padding: 0 28px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center">Next</a></span></div>
  </section>'''
    return screen_board('Learn, on a tablet', 1280, 800, NIGHT, inner, static_logic(), dark=True, defs=ola_defs('tl'))


# ---------------------------------------------------------------- The check-in on WhatsApp

Q1_OPTS = ['Nothing yet', 'Up to R 500', 'R 500 to R 1 000', 'R 1 000 to R 2 000', 'More than R 2 000']


def whatsapp():
    def awo(text, time, extra='', step=None):
        return (f'<div style="align-self: flex-start; max-width: 300px; display: flex; flex-direction: column; gap: 4px; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">'
                f'<div style="border-radius: 2px 10px 10px 10px; background: #FFFFFF; padding: 8px 10px 6px; box-shadow: 0 1px 1px rgba(0,0,0,.08); display: flex; flex-direction: column; gap: 2px">'
                f'<span style="font-size: 15px; line-height: 1.4">{text}</span><span style="align-self: flex-end; font-size: 12px; color: {MUTED}">{time}</span></div>{extra}</div>')

    def her(hole, time):
        return (f'<div style="align-self: flex-end; max-width: 260px; border-radius: 10px 2px 10px 10px; background: {OUT_BUBBLE}; padding: 8px 10px 6px; box-shadow: 0 1px 1px rgba(0,0,0,.08); display: flex; flex-direction: column; gap: 2px; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">'
                f'<span style="font-size: 15px; line-height: 1.4">[[ {hole} ]]</span><span style="align-self: flex-end; font-size: 12px; color: {MUTED}">{time}</span></div>')

    def buttons(pairs):
        return ''.join(f'<button onClick="[[ {h} ]]" style="height: 44px; border-radius: 10px; background: #FFFFFF; box-shadow: 0 1px 1px rgba(0,0,0,.08); color: #027EB5; font-size: 15px; font-weight: 500">{t}</button>' for h, t in pairs)

    opts = ''.join(f'''<button onClick="[[ pick{i} ]]" style="width: 100%; min-height: 52px; display: flex; align-items: center; justify-content: space-between; gap: 10px; text-align: left; font-size: 16px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">{o}
        <span aria-hidden="true" style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 999px; border: 2px solid [[ rc{i} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: [[ rf{i} ]]"></span></span></button>''' for i, o in enumerate(Q1_OPTS))
    chat = f'''
      <span style="align-self: center; font-size: 12px; background: #FFFFFF; color: {SEC}; border-radius: 6px; padding: 4px 10px">Today</span>
      {awo("Hi Naledi, it's check-in day. Three questions, about two minutes. Only you and AWO see your answers.", '07:30', '<div style="display: flex; flex-direction: column; gap: 4px">' + buttons([('start', 'Start'), ('later', 'Tonight'), ('skip', 'Skip a month')]) + '</div>')}
      <sc-if value="[[ saidLater ]]" hint-placeholder-val="[[ false ]]">{her('laterText', '07:31')}{awo("Okay. I'll ask again at 19:00.", '07:31')}</sc-if>
      <sc-if value="[[ s1 ]]" hint-placeholder-val="[[ false ]]">{her('startText', '07:31')}{awo('<b style="font-weight: 600">1 of 3.</b> Since 13 September, how much did you put aside for your safety net?', '07:31', '<button onClick="[[ openList ]]" style="height: 44px; border-radius: 10px; background: #FFFFFF; box-shadow: 0 1px 1px rgba(0,0,0,.08); color: #027EB5; font-size: 15px; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 8px">' + ic8('list', 18, '#027EB5') + 'Choose an amount</button>')}</sc-if>
      <sc-if value="[[ s2 ]]" hint-placeholder-val="[[ false ]]">{her('q1Text', '07:32')}{awo("<b style='font-weight: 600'>2 of 3.</b> Did you try this month's step: R 100 into a separate pocket on payday?", '07:32', '<div style="display: flex; flex-direction: column; gap: 4px">' + buttons([('a0', 'Yes'), ('a1', 'Partly'), ('a2', 'Not this time')]) + '</div>')}</sc-if>
      <sc-if value="[[ s3 ]]" hint-placeholder-val="[[ false ]]">{her('q2Text', '07:32')}{awo('<b style="font-weight: 600">3 of 3.</b> How did money feel this month?', '07:33', '<div style="display: flex; flex-direction: column; gap: 4px">' + buttons([('b0', 'Calm'), ('b1', 'Tight'), ('b2', 'Hard')]) + '</div>')}</sc-if>
      <sc-if value="[[ s4 ]]" hint-placeholder-val="[[ false ]]">{her('q3Text', '07:33')}{awo("Thank you, Naledi. That's check-in 4 done. Your new version and what changed are in the app.", '07:33', '<a href="R9-What-Changed.dc.html" style="height: 44px; border-radius: 10px; background: #FFFFFF; box-shadow: 0 1px 1px rgba(0,0,0,.08); color: #027EB5; font-size: 15px; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 8px">' + ic8('share', 16, '#027EB5') + 'See what changed</a>')}{awo('Reply HELP for help, or STOP to end check-ins here. You can delete this chat at any time.', '07:33')}</sc-if>'''
    inner = f'''  <header style="position: absolute; left: 0; right: 0; top: 0; height: 100px; box-sizing: border-box; padding: 44px 10px 0; background: #FFFFFF; border-bottom: 1px solid {LINE7}; display: flex; align-items: center; gap: 8px">
    <span style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('back', 22, INK, 2.2)}</span>{app_badge(38)}
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 16px; font-weight: 600">AWO</span><span style="font-size: 12px; color: {MUTED}">Business account</span></span>
    <span class="chip" style="border: 1px dashed {MUTED}; color: {MUTED}; margin-right: 6px">WhatsApp, a sample</span>
  </header>
  <div style="position: absolute; left: 0; right: 0; top: 100px; bottom: 64px; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: flex-end; gap: 8px; overflow: hidden">{chat}
  </div>
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 64px; box-sizing: border-box; padding: 8px 10px 12px; display: flex; gap: 8px; align-items: center">
    <span style="flex-grow: 1; height: 44px; border-radius: 22px; background: #FFFFFF; display: flex; align-items: center; padding: 0 16px; font-size: 16px; color: {MUTED}">Message</span>
    <span style="width: 44px; height: 44px; border-radius: 999px; background: #1DAA61; display: flex; align-items: center; justify-content: center">{ic8('mic', 20, '#FFFFFF')}</span>
  </div>
  <sc-if value="[[ list ]]" hint-placeholder-val="[[ false ]]"><div class="dim" onClick="[[ closeList ]]"></div>
    <div class="sheet" role="dialog" aria-label="Choose an amount" style="padding: 10px 20px 24px; display: flex; flex-direction: column; gap: 6px">
      <span aria-hidden="true" style="align-self: center; width: 40px; height: 4px; border-radius: 2px; background: #C9D3CE"></span>
      <span style="font-size: 17px; font-weight: 600; text-align: center; padding: 6px 0">Choose an amount</span>
      <div style="display: flex; flex-direction: column">{opts}</div>
      <button onClick="[[ sendList ]]" style="height: 48px; margin-top: 8px; border-radius: 24px; background: #1DAA61; color: #FFFFFF; font-size: 16px; font-weight: 600">Send</button>
    </div></sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const s = st.s || 0, q1 = st.q1 == null ? 3 : st.q1, opts = %(opts)s;
    const v = {
      s1: s >= 1, s2: s >= 2, s3: s >= 3, s4: s >= 4, list: !!st.list, saidLater: !!st.later && s === 0,
      startText: 'Start', laterText: 'Tonight', q1Text: opts[q1], q2Text: ['Yes', 'Partly', 'Not this time'][st.a || 0], q3Text: ['Calm', 'Tight', 'Hard'][st.b == null ? 1 : st.b],
      start: () => { if (s === 0) this.setState({ s: 1, later: false }); }, later: () => this.setState({ later: true }), skip: () => this.setState({ later: true }),
      openList: () => { if (s === 1) this.setState({ list: true }); }, closeList: () => this.setState({ list: false }),
      sendList: () => this.setState({ list: false, s: 2 })
    };
    opts.forEach((_, i) => { v['pick' + i] = () => this.setState({ q1: i }); v['rc' + i] = q1 === i ? '#1DAA61' : '#A9B6AF'; v['rf' + i] = q1 === i ? '#1DAA61' : 'transparent'; });
    [0, 1, 2].forEach((i) => { v['a' + i] = () => { if (s === 2) this.setState({ a: i, s: 3 }); }; v['b' + i] = () => { if (s === 3) this.setState({ b: i, s: 4 }); }; });
    return v;
  }
}''' % dict(opts=js(Q1_OPTS))
    return free_page('The check-in, on WhatsApp', inner, logic, h=844, bg=MOBILE_BG)


# ---------------------------------------------------------------- The check-in on USSD

USSD = [('*120*2926#', 'AWO check-in\n1. Start (3 questions)\n2. Remind me tonight\n3. Skip this month\n0. Help'),
        ('1', '1/3 Since 13 Sep, how much did you put aside for your safety net?\n1. Nothing yet\n2. Up to R500\n3. R500-R1000\n4. R1000-R2000\n5. More'),
        ('4', "2/3 Did you try this month's step: R100 on payday?\n1. Yes\n2. Partly\n3. Not this time"),
        ('1', '3/3 How did money feel this month?\n1. Calm\n2. Tight\n3. Hard'),
        ('2', "Done, Naledi. Check-in 4 is saved. See what changed in the AWO app. We'll SMS your step. No amounts by SMS."),
        ('SMS', "AWO: Check-in 4 done. October's step: raise your payday move by R50. Open the app to see what changed. Reply STOP to end SMS.")]


def lcd(text, w=236, h=236, font=15):
    lines = text.replace('\n', '<br>')
    return (f'<div style="width: {w}px; height: {h}px; box-sizing: border-box; border-radius: 6px; background: #C9D6C2; box-shadow: inset 0 0 0 2px #9FB09A, inset 0 2px 8px rgba(0,0,0,.18); '
            f'padding: 12px 12px; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: {font}px; line-height: 1.35; color: #1B2419; overflow: hidden">{lines}</div>')


def ussd():
    keys = [('1', ''), ('2', 'abc'), ('3', 'def'), ('4', 'ghi'), ('5', 'jkl'), ('6', 'mno'), ('7', 'pqrs'), ('8', 'tuv'), ('9', 'wxyz'), ('*', ''), ('0', ''), ('#', '')]
    keypad = ''.join(f'<button onClick="[[ k{i} ]]" aria-label="{k}" style="height: 44px; border-radius: 8px; background: #2A2F2C; color: #F2F1EC; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1"><span style="font-size: 18px; font-weight: 600">{k}</span><span style="font-size: 12px; color: #9AA39F">{sub}</span></button>' for i, (k, sub) in enumerate(keys))
    screens = [s for s in USSD[:5]]
    lcds = ''
    for i, (typed, text) in enumerate(screens):
        plain = text.replace('\n', ' ')
        lcds += f'''<div style="display: flex; flex-direction: column; gap: 8px">
        <span style="font-size: 13px; font-weight: 600; color: {SEC}">{"She dials " + typed if i == 0 else "She replies " + typed}</span>
        {lcd(text, 232, 220, 14)}
        <span style="font-size: 12px; color: {MUTED}">{len(plain)} of 160 characters</span></div>'''
    sms = USSD[5][1]
    body = f'''  <div style="display: flex; gap: 48px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 12px; align-items: center">
      <div style="width: 300px; box-sizing: border-box; border-radius: 42px; background: #151816; padding: 30px 30px 24px; box-shadow: 0 30px 70px rgba(11,15,14,.3), inset 0 0 0 2px #2E3A36; display: flex; flex-direction: column; gap: 16px">
        <span style="align-self: center; width: 60px; height: 6px; border-radius: 3px; background: #2E3A36"></span>
        <div role="region" aria-live="polite" aria-label="The phone's screen">
          <div style="width: 240px; height: 250px; box-sizing: border-box; border-radius: 6px; background: #C9D6C2; box-shadow: inset 0 0 0 2px #9FB09A, inset 0 2px 8px rgba(0,0,0,.18); padding: 12px; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 15px; line-height: 1.35; color: #1B2419; display: flex; flex-direction: column; justify-content: space-between">
            <span style="white-space: pre-line">[[ screen ]]</span>
            <span style="display: flex; justify-content: space-between; border-top: 1px solid #9FB09A; padding-top: 6px"><span>[[ typed ]]<span style="animation: caret 1s steps(1) infinite">_</span></span><span>[[ hint ]]</span></span></div></div>
        <div style="display: flex; justify-content: space-between"><button onClick="[[ send ]]" style="height: 44px; padding: 0 16px; border-radius: 8px; background: #2A2F2C; color: {LIME}; font-size: 15px; font-weight: 600">Send</button><button onClick="[[ reset ]]" style="height: 44px; padding: 0 16px; border-radius: 8px; background: #2A2F2C; color: #F2F1EC; font-size: 15px; font-weight: 600">Cancel</button></div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px">{keypad}</div>
      </div>
      <span style="font-size: 14px; color: {SEC}; text-align: center; max-width: 280px">Press 1 to start, then answer with numbers and Send. Cancel starts again.</span>
    </div>
    <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; gap: 18px; flex-wrap: wrap">{lcds}</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px">
        <section class="card" style="background: #FFFFFF; padding: 20px 22px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 17px; font-weight: 600">Then, by SMS</span>{lcd(sms, 360, 120, 14)}<span style="font-size: 13px; color: {MUTED}">{len(sms)} of 160 characters. No amounts, no score: anyone can read an SMS.</span></section>
        <section class="card" style="background: #FFFFFF; padding: 20px 22px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 17px; font-weight: 600">Why it's shaped like this</span>
          <span style="font-size: 15px; line-height: 1.5; color: {SEC}">Each screen fits 160 characters. Answers are single numbers. A session ends after about two minutes, so there are three questions and nothing else. The same questions, with the same values, as the app and WhatsApp.</span>
          <span style="font-size: 13px; color: {MUTED}">The short code and timings are samples; the provider is open (Q-21).</span></section>
      </div>
    </div>
  </div>'''
    flow = [s[1] for s in USSD[:5]]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const step = st.step || 0, typed = st.typed || '', flow = %(flow)s, keys = %(keys)s;
    const valid = [['1', '2', '3', '0'], ['1', '2', '3', '4', '5'], ['1', '2', '3'], ['1', '2', '3'], []][step];
    const v = {
      screen: flow[step], typed, hint: step === 4 ? 'Done' : (typed ? 'Send' : 'Reply'),
      send: () => { if (valid.indexOf(typed) >= 0) this.setState({ step: step === 0 && typed !== '1' ? 0 : step + 1, typed: '' }); },
      reset: () => this.setState({ step: 0, typed: '' })
    };
    keys.forEach((k, i) => { v['k' + i] = () => this.setState({ typed: step < 4 ? k : '' }); });
    return v;
  }
}''' % dict(flow=js(flow), keys=js([k for k, _s in keys]))
    css = '@keyframes caret{50%{opacity:0}}'
    return board7('The check-in on USSD, for any phone', 'No data and no smartphone needed: she dials a short code and answers with numbers. The same three questions as the app and WhatsApp, with the same values. Try it on the phone.', body, logic, 1800, 880, css=css, chip='Sample code and timings (Q-21). Try the keypad.')


# ---------------------------------------------------------------- One question, every channel

def one_question():
    DOT = f'<span style="width: 8px; height: 8px; border-radius: 999px; background: {EVG}"></span>'
    spec = [('Question', 'safety_net.put_aside, version 3'), ('Asks', 'Since your last check-in, how much did you put aside for your safety net?'),
            ('Short label', 'Put aside (20 characters at most)'), ('Answers', 'Five bands: nothing; up to R 500; R 500 to R 1 000; R 1 000 to R 2 000; more. Stored as the band, never as a guess'),
            ('Feeds', 'Ready for surprises, in the DIVA score, worked out on AWO\'s servers'), ('Rules', 'Five or fewer options. One question per screen. Plain words. The same answer means the same thing everywhere')]
    spec_html = ''.join(f'<div style="padding: 12px 0; display: flex; flex-direction: column; gap: 3px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="font-size: 13px; font-weight: 600; color: {MUTED}">{k}</span><span style="font-size: 15px; line-height: 1.45">{v}</span></div>' for i, (k, v) in enumerate(spec))
    chips = ''.join(f'<span style="flex: 1 1 0; height: 40px; border-radius: 8px; background: {EVG if i == 3 else "#FFFFFF"}; color: {"#FFFFFF" if i == 3 else INK}; font-size: 13px; font-weight: 600; display: flex; align-items: center; justify-content: center">{t}</span>' for i, t in enumerate(['Nothing', 'R 500', 'R 1 000', 'R 2 000']))
    app = f'''<div style="width: 300px; border-radius: 28px; background: {MIST}; box-shadow: 0 0 0 6px {INK}; padding: 22px 18px; display: flex; flex-direction: column; gap: 14px">
      <span class="lbl" style="color: {EVG}">Question 1 of 3</span><span class="d" style="font-size: 24px">Since 13 Sep, how much did you put aside for your safety net?</span>
      <span class="d" style="font-size: 44px; color: {EVG}">R 1 800</span>
      <span aria-hidden="true" style="height: 8px; border-radius: 2px; background: linear-gradient(to right, {EVG} 36%, #DCE4DF 36%); position: relative"><span style="position: absolute; left: 34%; top: -11px; width: 30px; height: 30px; border-radius: 6px; background: {LIME}; box-shadow: 0 0 0 3px {EVG}"></span></span>
      <div style="display: flex; gap: 4px; margin-top: 8px">{chips}</div></div>'''
    web = f'''<div style="width: 360px; border-radius: 14px; background: #FFFFFF; box-shadow: 0 0 0 1px {LINE}, 0 18px 40px rgba(16,24,20,.12); padding: 24px; display: flex; flex-direction: column; gap: 14px">
      <span style="font-size: 13px; font-weight: 600; color: {EVG}">1 of 3</span><span style="font-size: 20px; font-weight: 600; line-height: 1.3">Since 13 September, how much did you put aside for your safety net?</span>
      {''.join(f'<span style="min-height: 44px; border-radius: 8px; box-shadow: inset 0 0 0 {2 if i == 3 else 1}px {EVG if i == 3 else LINE}; padding: 0 14px; display: flex; align-items: center; gap: 12px; font-size: 15px"><span style="width: 18px; height: 18px; box-sizing: border-box; border-radius: 999px; border: 2px solid {EVG if i == 3 else "#A9B6AF"}; display: flex; align-items: center; justify-content: center">{DOT if i == 3 else ""}</span>{o}</span>' for i, o in enumerate(Q1_OPTS))}
      <span style="font-size: 13px; color: {MUTED}">Use the arrow keys, then Enter.</span></div>'''
    wa = f'''<div style="width: 300px; border-radius: 18px; background: {MOBILE_BG}; padding: 14px; display: flex; flex-direction: column; gap: 8px">
      <div style="border-radius: 2px 10px 10px 10px; background: #FFFFFF; padding: 8px 10px; font-size: 15px; line-height: 1.4"><b style="font-weight: 600">1 of 3.</b> Since 13 September, how much did you put aside for your safety net?</div>
      <div style="border-radius: 12px; background: #FFFFFF; padding: 8px 14px; display: flex; flex-direction: column">{''.join(f'<span style="min-height: 40px; display: flex; align-items: center; justify-content: space-between; font-size: 14px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">{o}<span style="width: 16px; height: 16px; box-sizing: border-box; border-radius: 999px; border: 2px solid {"#1DAA61" if i == 3 else "#A9B6AF"}; background: {"#1DAA61" if i == 3 else "transparent"}"></span></span>' for i, o in enumerate(Q1_OPTS))}</div></div>'''
    us = lcd(USSD[1][1], 260, 230, 14)
    col = lambda name, sub, inner, href='': (f'<div style="display: flex; flex-direction: column; gap: 14px; align-items: flex-start"><span style="display: flex; flex-direction: column; gap: 3px"><span style="font-size: 20px; font-weight: 600">{name}</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}; max-width: 320px">{sub}</span></span>{inner}'
                                             + (f'<a href="{href}" style="min-height: 44px; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; color: {EVG}">Open it{icon("chev", 14, EVG)}</a>' if href else '') + '</div>')
    body = f'''  <div style="display: grid; grid-template-columns: 380px 1fr; gap: 44px; align-items: start">
    <section class="card" style="background: #FFFFFF; padding: 22px 26px; display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 600; padding-bottom: 6px">Written once</span>{spec_html}</section>
    <div style="display: grid; grid-template-columns: repeat(4, auto); gap: 36px; align-items: start">
      {col('The app', 'A slider and four quick amounts. The band is worked out from the amount.', app, 'R7-Checkin.dc.html')}
      {col('The web', 'The five bands as a list. Works with the keyboard alone.', web)}
      {col('WhatsApp', 'A list message: five options, one tap.', wa, 'R9-WhatsApp-Checkin.dc.html')}
      {col('USSD', 'Numbers only, 160 characters a screen.', us, 'R9-USSD.dc.html')}
    </div>
  </div>'''
    return board7('One question, every channel', 'The same question, with the same five answers, drawn four ways. The question graph is written once, with a short label and five or fewer options, so a check-in on WhatsApp or USSD means exactly what it means in the app.', body, static_logic(), 2080, 1060, chip='Sample question. Tap to open a channel.')


BOARDS = [('R9-Desktop-Home', desk_home), ('R9-Desktop-Me', desk_me), ('R9-Tablet-Learn', tablet_learn),
          ('R9-WhatsApp-Checkin', whatsapp), ('R9-USSD', ussd), ('R9-One-Question', one_question)]
