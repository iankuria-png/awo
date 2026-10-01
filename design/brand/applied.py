"""The suggested brand system applied to the app: onboarding, the major screens, the Play Store set and marketing,
drawn natively in the brief's system (plum, terracotta and warm stone; Playfair Display and Montserrat) so it can be
compared with the app's own language on the Round 7 board (Q-49).

Each screen is written once (390 wide) and reused inside the store screenshots, the feature graphic and the website,
so they always match. Rules carried from the brief and the project: one terracotta focal point per view; terracotta
as type only when large or in white-on-terracotta buttons; small text on plum in warm stone, never sage; blush only
in Community; the DIVA score always says it is for learning; every number is a sample."""
from brand import (STONE, PLUM, TERRA, SAGE, BLUSH, WGREY, BODY, WHITE, SERIF, SANS, IMG, page_html, wordmark,  # noqa: F401
                   rule, scaled, frame)

GREY = '#6E6470'  # secondary text: 4.81:1 on warm stone, 5.65:1 on white
IMG = dict(IMG, phone_smile='/_blob/d52cdc4b08597f0ff8bc6e1c58f129dd', thandi='/_blob/f8021d36aaa6e41b5716f012f39438cb',
           grace='/_blob/876a6c76dcee466c2a8bb01c6c3a3d7d', amara='/_blob/1708e7afa42863658d9439e542a15a5c',
           naledi='/_blob/a1c6d27055f330029a50e20d5163113f', wanjiru='/_blob/18c9f6030b6eabb32eba39b3c6825506',
           lindiwe='/_blob/87835fd30cadd081b87b7e4942e8d0f0', together='/_blob/de99957f2ba63a4f30e2cf6bda586b39')
GRADE = 'filter: saturate(.74) sepia(.12) contrast(.97)'

P = {'home': '<path d="M4 11 12 4l8 7"></path><path d="M6 9.5V20h12V9.5"></path><path d="M10 20v-5h4v5"></path>',
     'learn': '<path d="M4 5.5c3-1.3 5.5-1.3 8 0v14c-2.5-1.3-5-1.3-8 0z"></path><path d="M20 5.5c-3-1.3-5.5-1.3-8 0v14c2.5-1.3 5-1.3 8 0z"></path>',
     'hub': '<rect x="4" y="4" width="7" height="7"></rect><rect x="13" y="4" width="7" height="7"></rect><rect x="4" y="13" width="7" height="7"></rect><rect x="13" y="13" width="7" height="7"></rect>',
     'people': '<circle cx="9" cy="8" r="3"></circle><path d="M3.5 19c.8-3.2 3-5 5.5-5s4.7 1.8 5.5 5"></path><circle cx="17" cy="9" r="2.4"></circle><path d="M15.5 14.3c2.4-.4 4.4 1.2 5 4.2"></path>',
     'me': '<circle cx="12" cy="8" r="4"></circle><path d="M4.5 20c1.2-4 4.2-6 7.5-6s6.3 2 7.5 6"></path>',
     'back': '<path d="m15 6-6 6 6 6"></path>', 'chev': '<path d="m9 6 6 6-6 6"></path>',
     'bell': '<path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"></path><path d="M10 20.5a2.2 2.2 0 0 0 4 0"></path>',
     'check': '<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 'play': '<path d="M8 5.5v13l10.5-6.5z"></path>',
     'calc': '<rect x="5" y="3" width="14" height="18" rx="1"></rect><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2M16 11v7"></path>',
     'doc': '<path d="M6.5 3h8l3 3v15h-11z"></path><path d="M9.5 10.5h5M9.5 14h5M9.5 17.5h3"></path>',
     'send': '<path d="M4 12 20 4l-6 16-3-7z"></path>', 'shield': '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"></path>',
     'chart': '<path d="M4 20V4M4 20h16"></path><path d="M8 16v-4M12 16V8M16 16v-6"></path>',
     'cal': '<rect x="4" y="5" width="16" height="15" rx="1"></rect><path d="M4 10h16M8 3v4M16 3v4"></path>',
     'heart': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"></path>',
     'bookmark': '<path d="M6.5 3.5h11v17L12 16.5l-5.5 4z"></path>', 'download': '<path d="M12 4v11M7 10.5l5 5 5-5"></path><path d="M5 20h14"></path>',
     'wallet': '<rect x="3.5" y="6" width="17" height="13" rx="1"></rect><path d="M3.5 9.5h17M15 14h2"></path>',
     'payslip': '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"></path><path d="M9 8h6M9 12h6"></path>',
     'search': '<circle cx="11" cy="11" r="6.5"></circle><path d="m20 20-4.2-4.2"></path>', 'lock': '<rect x="5" y="11" width="14" height="10" rx="1"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>'}


def ic(name, size=22, col=PLUM, sw=1.5):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; display: block">{P[name]}</svg>')


def status(col=BODY):
    return (f'<div style="position: absolute; left: 0; right: 0; top: 0; height: 44px; padding: 0 22px; display: flex; align-items: center; justify-content: space-between; font-size: 15px; font-weight: 600; color: {col}">'
            f'<span>9:41</span><span style="display: flex; gap: 6px; align-items: center"><span style="width: 18px; height: 10px; border: 1.5px solid {col}; border-radius: 2px; padding: 1px; display: flex"><span style="flex: .7; background: {col}"></span></span></span></div>')


TABS = [('Home', 'home'), ('Learn', 'learn'), ('Hub', 'hub'), ('Community', 'people'), ('Me', 'me')]


def tabbar(active, dark=False):
    bg, line, idle, on = (PLUM, 'rgba(245,235,227,.18)', '#D9CCD6', STONE) if dark else (WHITE, WGREY, GREY, PLUM)
    items = ''
    for n, g in TABS:
        a = n == active
        items += (f'<a href="#" {"aria-current=" + chr(34) + "page" + chr(34) if a else ""} style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; min-height: 52px; '
                  f'font-size: 12px; font-weight: {600 if a else 500}; color: {on if a else idle}; text-decoration: none; position: relative">'
                  f'{"<span style=" + chr(34) + "position: absolute; top: -9px; width: 28px; height: 2px; background: " + on + chr(34) + "></span>" if a else ""}{ic(g, 22, on if a else idle, 1.7 if a else 1.4)}{n}</a>')
    return (f'<nav aria-label="Main" style="position: absolute; left: 0; right: 0; bottom: 0; height: 84px; box-sizing: border-box; padding: 8px 8px 22px; background: {bg}; border-top: 1px solid {line}; '
            f'display: grid; grid-template-columns: repeat(5, minmax(0, 1fr))">{items}</nav>')


def btn(label, kind='primary', h=52, extra=''):
    k = {'primary': f'background: {PLUM}; color: {STONE}', 'accent': f'background: {TERRA}; color: {WHITE}', 'light': f'background: {STONE}; color: {PLUM}',
         'quiet': f'background: transparent; color: {PLUM}; box-shadow: inset 0 0 0 1.5px {PLUM}', 'quiet-dark': f'background: transparent; color: {STONE}; box-shadow: inset 0 0 0 1.5px {STONE}'}[kind]
    return f'<a href="#" style="height: {h}px; flex-shrink: 0; border-radius: 4px; {k}; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 16px; font-weight: 600; text-decoration: none; {extra}">{label}</a>'


def card(inner, bg=WHITE, pad='18px 18px', gap=8, extra=''):
    return f'<div style="background: {bg}; border-radius: 4px; padding: {pad}; display: flex; flex-direction: column; gap: {gap}px; {extra}">{inner}</div>'


def small(t, col=GREY, w=500, size=13):
    return f'<span style="font-size: {size}px; font-weight: {w}; color: {col}; line-height: 1.4">{t}</span>'


def h(t, size=30, col=PLUM, extra=''):
    return f'<h1 style="margin: 0; {SERIF}; font-weight: 500; font-size: {size}px; line-height: 1.12; letter-spacing: -0.01em; color: {col}; {extra}">{t}</h1>'


def sample(col=GREY):
    return f'<span style="height: 26px; padding: 0 9px; border: 1px dashed {col}; border-radius: 3px; display: inline-flex; align-items: center; font-size: 12px; font-weight: 600; color: {col}">Sample</span>'


def reviewed(col=PLUM):
    return f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 12px; font-weight: 600; color: {col}">{ic("check", 14, col, 2)}Reviewed by AWO</span>'


def screen(bg, inner, h=844):
    return f'<div style="position: relative; width: 390px; height: {h}px; overflow: hidden; background: {bg}; color: {BODY}; {SANS}">{inner}</div>'


def scroll(inner, top=44, bottom=84, gap=14, pad='8px 20px 20px'):
    return f'<div style="position: absolute; left: 0; right: 0; top: {top}px; bottom: {bottom}px; padding: {pad}; box-sizing: border-box; display: flex; flex-direction: column; gap: {gap}px; overflow: hidden">{inner}</div>'


def stones(n_done, current, w=300, hgt=96, dark=True):
    """Four stones rising: those behind her filled, where she stands in terracotta, the ones ahead dashed."""
    rx, ry = 30, 11
    out = ''
    for i in range(4):
        x = rx + 4 + i * (w - 2 * rx - 8) / 3
        y = hgt - ry - 8 - i * (hgt - 2 * ry - 16) / 3
        fill_done = STONE if dark else PLUM
        line = STONE if dark else PLUM
        if i < current:
            out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" fill="{fill_done}"></ellipse>'
        elif i == current:
            out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" fill="{TERRA}"></ellipse>'
        else:
            out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" fill="none" stroke="{line}" stroke-width="1.5" stroke-dasharray="4 4"></ellipse>'
    return f'<svg width="{w}" height="{hgt}" viewBox="0 0 {w} {hgt}" aria-hidden="true" style="display: block">{out}</svg>'


def bar(pct, col=PLUM, track=WGREY, hgt=6):
    return f'<span style="display: block; height: {hgt}px; background: {track}"><span style="display: block; height: 100%; width: {pct}%; background: {col}"></span></span>'


# ================================================================ Onboarding

def welcome():
    inner = f'''<img src="{IMG['phone_smile']}" alt="A woman laughing on a phone call" style="position: absolute; left: 0; top: 0; width: 390px; height: 480px; object-fit: cover; object-position: 50% 22%; {GRADE}">
  <span aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 268px; height: 214px; background: linear-gradient(to bottom, rgba(74,45,78,0), {PLUM})"></span>
  {status(WHITE)}
  <div style="position: absolute; left: 0; right: 0; top: 478px; bottom: 0; background: {PLUM}; padding: 18px 24px 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
    {wordmark(22, STONE)}
    {h('Money, understood.', 38, STONE)}
    {rule(56)}
    <p style="margin: 0; font-size: 15px; line-height: 1.55; color: {STONE}">Learn where you stand, what it means and what to do next. Free, in plain words.</p>
    <div style="flex-grow: 1"></div>
    {btn('Join free', 'light')}
    <a href="#" style="min-height: 44px; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 600; color: {STONE}; text-decoration: underline; text-underline-offset: 4px">I have an account</a>
  </div>'''
    return screen(PLUM, inner)


def signin():
    inner = f'''{status()}{scroll(f"""
    <a href="#" aria-label="Back" style="width: 44px; height: 44px; margin-left: -10px; display: flex; align-items: center; justify-content: center">{ic('back', 24)}</a>
    {h('Your number is your <span style="color: ' + TERRA + '">key</span>.', 34)}
    <p style="margin: 0; font-size: 15px; line-height: 1.55; color: {BODY}">We text you a code. There is no password to remember.</p>
    <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px">
      {small('Mobile number', PLUM, 600)}
      <div style="display: flex; gap: 8px">
        <span style="height: 54px; padding: 0 14px; background: {WHITE}; border-radius: 4px; box-shadow: inset 0 0 0 1px {WGREY}; display: flex; align-items: center; font-size: 17px; font-weight: 600">+27</span>
        <span style="flex-grow: 1; height: 54px; padding: 0 16px; background: {WHITE}; border-radius: 4px; box-shadow: inset 0 0 0 1.5px {PLUM}; display: flex; align-items: center; font-size: 18px; letter-spacing: .02em">82 123 4567</span></div>
      {small('We will text a 6-digit code to +27 82 123 4567.', GREY)}
    </div>
    {btn('Send me a code')}
    <span style="display: flex; align-items: center; gap: 12px; font-size: 13px; color: {GREY}"><span style="flex-grow: 1; height: 1px; background: {WGREY}"></span>or<span style="flex-grow: 1; height: 1px; background: {WGREY}"></span></span>
    {btn('Continue with Google', 'quiet')}
    {btn('Continue with Apple', 'quiet')}
    <div style="flex-grow: 1"></div>
    <p style="margin: 0; font-size: 13px; line-height: 1.5; color: {GREY}; text-align: center">By continuing you agree to the Terms and Privacy Policy. Your data is stored in South Africa.</p>""", bottom=0, gap=14)}'''
    return screen(STONE, inner)


def question():
    opts = [('Savings set aside for it', False), ('Cut back for a month or two', True), ('Borrow from family or a friend', False), ('A loan or credit card', False), ("I'm not sure", False)]
    rows = ''.join(f'''<a href="#" style="min-height: 56px; padding: 12px 16px; background: {WHITE}; border-radius: 4px; box-shadow: inset 0 0 0 {1.5 if on else 1}px {PLUM if on else WGREY}; display: flex; align-items: center; gap: 14px; text-decoration: none; color: {BODY}">
        <span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 999px; box-shadow: inset 0 0 0 1.5px {PLUM}; display: flex; align-items: center; justify-content: center">{"<span style='width: 12px; height: 12px; border-radius: 999px; background: " + PLUM + "'></span>" if on else ""}</span>
        <span style="font-size: 16px; font-weight: {600 if on else 500}">{t}</span></a>''' for t, on in opts)
    inner = f'''{status()}{scroll(f"""
    <div style="display: flex; align-items: center; gap: 12px"><a href="#" aria-label="Back" style="width: 44px; height: 44px; margin-left: -10px; display: flex; align-items: center; justify-content: center">{ic('back', 24)}</a>
      <span style="flex-grow: 1">{bar(33, TERRA, WGREY, 4)}</span>{small('4 of 12', GREY, 600)}</div>
    {small('Ready for surprises', PLUM, 600)}
    {h('If a R 2 000 surprise came this month, how would you cover it?', 28)}
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 4px">{rows}</div>
    <div style="flex-grow: 1"></div>
    <span style="display: flex; gap: 10px; align-items: flex-start; font-size: 13px; line-height: 1.5; color: {GREY}">{ic('lock', 16, GREY)}Honest answers make your profile more useful. Nothing here is shared.</span>
    {btn('Continue')}""", bottom=0, gap=14)}'''
    return screen(STONE, inner)


def reveal():
    inner = f'''{status(STONE)}{scroll(f"""
    {small('Your DIVA profile', STONE, 600, 14)}
    {h('Stage 2 of 4', 46, STONE)}
    {stones(1, 1, 320, 96)}
    <div style="display: flex; align-items: flex-end; gap: 16px; padding: 16px 0; border-top: 1px solid rgba(245,235,227,.25); border-bottom: 1px solid rgba(245,235,227,.25)">
      <span style="{SERIF}; font-size: 64px; line-height: .9; color: {STONE}">63</span>
      <span style="display: flex; flex-direction: column; gap: 3px; padding-bottom: 4px"><span style="font-size: 15px; font-weight: 600; color: {STONE}">DIVA score</span><span style="font-size: 13px; color: {STONE}">For learning, never a credit score.</span></span>
      <span style="margin-left: auto; padding-bottom: 6px">{sample(STONE)}</span></div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">
      {card(small('Your strength', STONE, 600) + '<span style="' + SERIF + '; font-size: 20px; line-height: 1.2; color: ' + STONE + '">Everyday money</span>', 'rgba(245,235,227,.08)')}
      {card(small('Your focus', STONE, 600) + '<span style="' + SERIF + '; font-size: 20px; line-height: 1.2; color: ' + STONE + '">Ready for surprises</span>', 'rgba(245,235,227,.08)')}</div>
    <p style="margin: 0; font-size: 15px; line-height: 1.6; color: {STONE}">Your everyday money habits are a real strength. A small cushion for surprises is the next thing to learn about.</p>
    {reviewed(STONE)}
    <div style="flex-grow: 1"></div>
    {btn('See your first step', 'light')}""", bottom=0, gap=16, pad='16px 24px 28px')}'''
    return screen(PLUM, inner)


def first_step():
    chips = ''.join(f'<span style="flex: 1; height: 48px; border-radius: 4px; background: {PLUM if on else WHITE}; color: {STONE if on else BODY}; box-shadow: inset 0 0 0 1px {PLUM if on else WGREY}; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">{t}</span>'
                    for t, on in [('R 50', False), ('R 100', True), ('R 200', False)])
    inner = f'''{status()}{scroll(f"""
    {small('Your first step', PLUM, 600, 14)}
    {h('Start a starter <span style="color: ' + TERRA + '">safety net</span>.', 34)}
    <p style="margin: 0; font-size: 15px; line-height: 1.6; color: {BODY}">Move a little into a separate pocket on payday, so a surprise doesn't knock your plans off course.</p>
    {card(small('How much feels right on payday?', PLUM, 600, 14) + '<div style="display: flex; gap: 8px">' + chips + '</div>' + small('You can change this any time.', GREY), gap=12)}
    {card('<span style="display: flex; align-items: center; gap: 12px">' + ic('bell', 22) + '<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Remind me on payday</span>' + small('The 25th, at 09:00') + '</span><span style="width: 48px; height: 28px; border-radius: 999px; background: ' + PLUM + '; position: relative"><span style="position: absolute; right: 3px; top: 3px; width: 22px; height: 22px; border-radius: 999px; background: ' + STONE + '"></span></span></span>')}
    {card(small('Why this step', PLUM, 600, 14) + '<span style="font-size: 14px; line-height: 1.55; color: ' + BODY + '">It matches your focus: being ready for surprises. Most people start small; what matters is the habit.</span>' + reviewed(), gap=8)}
    <div style="flex-grow: 1"></div>
    {btn('Start this step')}""", bottom=0, gap=14)}'''
    return screen(STONE, inner)


# ================================================================ The major screens

def home():
    face = f'<img src="{IMG["naledi"]}" alt="" style="width: 44px; height: 44px; border-radius: 999px; object-fit: cover">'
    inner = f'''{status()}{scroll(f"""
    <header style="display: flex; align-items: center; gap: 12px">{face}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px">{small('Tuesday 1 October')}<span style="{SERIF}; font-size: 24px; color: {PLUM}">Good morning, Naledi</span></span>
      <a href="#" aria-label="Notifications" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; position: relative">{ic('bell', 24)}<span style="position: absolute; right: 9px; top: 9px; width: 8px; height: 8px; border-radius: 9px; background: {PLUM}"></span></a></header>
    {card(small("This week's step", STONE, 600) + h('Move R 100 into your safety net', 25, STONE) + '<span style="display: flex; align-items: center; gap: 12px; margin-top: 6px"><span style="flex-grow: 1">' + bar(50, TERRA, 'rgba(245,235,227,.25)', 3) + '</span>' + small('1 of 2 done', STONE, 600) + '</span>' + btn('Mark it done', 'light', 46, 'margin-top: 6px'), PLUM, '20px 18px', 10)}
    <div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 10px">
      {card(small('Safety net', PLUM, 600) + '<span style="' + SERIF + '; font-size: 30px; line-height: 1; color: ' + PLUM + '">R 3 100</span>' + small('of R 5 000') + bar(62), pad='16px', gap=8)}
      {card(small('Next check-in', PLUM, 600) + '<span style="' + SERIF + '; font-size: 30px; line-height: 1; color: ' + PLUM + '">12 days</span>' + small('13 October, three questions') + bar(60, PLUM), pad='16px', gap=8)}</div>
    {card('<span style="display: flex; justify-content: space-between; align-items: center">' + small('Word of the week', PLUM, 600) + small('Say it: stok-fel') + '</span><span style="' + SERIF + '; font-size: 28px; color: ' + PLUM + '">Stokvel</span><span style="font-size: 14px; line-height: 1.5">A savings group that takes turns with the pot.</span>', pad='16px')}
    {card(small('Your circle asked', BODY, 700) + '<span style="font-size: 17px; font-weight: 700; line-height: 1.35; color: ' + BODY + '">What’s one money habit your mother taught you?</span>' + small('12 answers. First names only.', BODY), BLUSH, '16px')}
    <span style="display: flex; justify-content: flex-end">{sample()}</span>""", gap=12)}{tabbar('Home')}'''
    return screen(STONE, inner, 980)


def learn():
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 0; height: 330px; background: {PLUM}"></div>{status(STONE)}{scroll(f"""
    <header style="display: flex; align-items: center; justify-content: space-between">{h('Learn', 34, STONE)}<a href="#" aria-label="Search" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('search', 24, STONE)}</a></header>
    <div role="tablist" style="display: flex; gap: 22px; border-bottom: 1px solid rgba(245,235,227,.25)">{''.join(f'<span role="tab" style="padding: 10px 0; font-size: 15px; font-weight: {700 if i == 0 else 500}; color: {STONE}; box-shadow: {"inset 0 -2px 0 " + STONE if i == 0 else "none"}">{t}</span>' for i, t in enumerate(['Paths', 'Words', 'Stories']))}</div>
    <div style="display: flex; flex-direction: column; gap: 8px; padding: 6px 0 10px">{small('Continue your path', STONE, 600)}{h('Your safety net, explained', 26, STONE)}<span style="display: flex; align-items: center; gap: 10px"><span style="flex-grow: 1">{bar(60, STONE, 'rgba(245,235,227,.25)', 3)}</span>{small('Lesson 3 of 5', STONE, 600)}</span>{btn('Continue: what a safety net is for', 'accent', 50, 'margin-top: 6px')}</div>
    <div style="display: flex; flex-direction: column; gap: 10px; padding-top: 18px">{small('Words you saved', PLUM, 600)}
      <span style="display: flex; gap: 8px; flex-wrap: wrap">{''.join(f'<span style="height: 40px; padding: 0 14px; background: {WHITE}; border-radius: 4px; box-shadow: inset 0 0 0 1px {WGREY}; display: inline-flex; align-items: center; {SERIF}; font-size: 17px; color: {PLUM}">{w}</span>' for w in ['Stokvel', 'Dividend', 'Compound interest'])}</span></div>
    <div style="position: relative; height: 170px; border-radius: 4px; overflow: hidden"><img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her stall" style="width: 100%; height: 100%; object-fit: cover; object-position: 60% 30%; {GRADE}"><span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(74,45,78,.92), rgba(74,45,78,0) 70%)"></span>
      <span style="position: absolute; left: 16px; right: 16px; bottom: 14px; display: flex; flex-direction: column; gap: 4px">{small('A Rise story', STONE, 600)}<span style="{SERIF}; font-size: 20px; line-height: 1.2; color: {STONE}">My first stall closed in four months.</span></span></div>
    {card('<span style="display: flex; align-items: center; gap: 14px"><span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 999px; box-shadow: inset 0 0 0 1.5px ' + PLUM + '; display: flex; align-items: center; justify-content: center">' + ic('play', 18) + '</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">The AWO Podcast, episode 12</span>' + small('Closing a shop, and opening a better one. 32 min') + '</span></span>', pad='12px 16px')}""", gap=12)}{tabbar('Learn')}'''
    return screen(STONE, inner)


def lesson():
    inner = f'''{status()}{scroll(f"""
    <div style="display: flex; align-items: center; gap: 12px"><a href="#" aria-label="Back" style="width: 44px; height: 44px; margin-left: -10px; display: flex; align-items: center; justify-content: center">{ic('back', 24)}</a><span style="flex-grow: 1">{bar(60, PLUM, WGREY, 3)}</span>{small('3 of 5', GREY, 600)}</div>
    {small('Your safety net, explained', GREY, 600)}
    {h('What a safety net is for', 32)}
    <span style="display: flex; gap: 12px; align-items: center">{small('3 minutes')}{reviewed()}</span>
    <p style="margin: 0; font-size: 17px; line-height: 1.7; color: {BODY}">A safety net is money you don't plan to spend. It is there for the car repair, the school trip, the month the hours are cut.</p>
    <blockquote style="margin: 4px 0; padding: 4px 0 4px 18px; border-left: 3px solid {TERRA}; {SERIF}; font-style: italic; font-size: 22px; line-height: 1.4; color: {PLUM}">“My safety net went down this month. It did its job.”</blockquote>
    {small('Amara, a nurse in London. Sample story.')}
    <p style="margin: 0; font-size: 17px; line-height: 1.7; color: {BODY}">Using it isn't failing. Refilling it, a little at a time, is the habit that matters.</p>
    {card(small('The idea to keep', PLUM, 700) + '<span style="font-size: 16px; line-height: 1.55">Keep it apart from everyday money, so it stays a safety net and not a spending pot.</span>', pad='16px')}
    <div style="flex-grow: 1"></div>
    <div style="display: flex; gap: 10px">{btn(ic('bookmark', 20) + 'Save', 'quiet', 52, 'flex: 0 0 120px')}{btn('Next: where to keep it', 'primary', 52, 'flex: 1')}</div>""", bottom=0, gap=12)}'''
    return screen(STONE, inner)


def hub():
    groups = [('Know your pay', [('payslip', 'Payslip decoder', 'Every line, in plain words'), ('cal', 'Pay-day plan', 'Where your pay goes first')]),
              ('Borrow with care', [('calc', "A loan's real cost", 'The total you would repay'), ('doc', 'Explain my agreement', 'Lines worth asking about')]),
              ('Send and grow', [('send', 'Sending money home', 'What arrives, and what it costs'), ('chart', 'Retirement pulse', 'What your fund might pay')])]
    g = ''.join(f'''<div style="display: flex; flex-direction: column">{small(t, PLUM, 700)}<div style="margin-top: 8px; background: {WHITE}; border-radius: 4px">''' + ''.join(
        f'''<a href="#" style="min-height: 60px; padding: 10px 16px; display: flex; align-items: center; gap: 14px; text-decoration: none; color: {BODY}; {"border-top: 1px solid " + WGREY + ";" if k else ""}">{ic(i, 22)}
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{n}</span>{small(d)}</span>{ic('chev', 18, GREY)}</a>''' for k, (i, n, d) in enumerate(items)) + '</div></div>' for t, items in groups)
    inner = f'''{status()}{scroll(f"""
    {h('Hub', 34)}
    <p style="margin: 0; font-size: 15px; line-height: 1.5; color: {BODY}">Tools for your own sums. Your numbers stay on your phone.</p>
    <div role="group" style="display: flex; background: {WHITE}; border-radius: 4px; padding: 4px; box-shadow: inset 0 0 0 1px {WGREY}"><span style="flex: 1; height: 40px; border-radius: 3px; background: {PLUM}; color: {STONE}; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600">Me</span><span style="flex: 1; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; color: {PLUM}">My business</span></div>
    {card('<span style="display: flex; justify-content: space-between; align-items: center">' + small('New in the Hub', STONE, 600) + rule(40) + '</span>' + h('Sending money home: what really arrives', 22, STONE) + small('Compare two quotes, fee and rate together.', STONE), PLUM, '16px 18px', 8)}
    {g}""", gap=14)}{tabbar('Hub')}'''
    return screen(STONE, inner)


def loan_tool():
    parts = [('Borrowed', 8000, PLUM), ('Interest', 1433, SAGE), ('Fees', 1978, TERRA)]
    tot = sum(p[1] for p in parts)
    seg = ''.join(f'<span style="flex: {v} 1 0; background: {c}"></span>' for _n, v, c in parts)
    keys = ''.join(f'<span style="display: flex; align-items: center; gap: 10px; font-size: 14px"><span style="width: 12px; height: 12px; background: {c}"></span><span style="flex-grow: 1">{n}</span><b style="font-weight: 600">R {v:,}</b></span>'.replace(',', ' ') for n, v, c in parts)
    field = lambda k, v: f'<span style="display: flex; justify-content: space-between; align-items: center; min-height: 48px; border-bottom: 1px solid {WGREY}"><span style="font-size: 14px; color: {GREY}">{k}</span><span style="font-size: 17px; font-weight: 600">{v}</span></span>'
    inner = f'''{status()}{scroll(f"""
    <div style="display: flex; align-items: center; justify-content: space-between"><a href="#" aria-label="Back" style="width: 44px; height: 44px; margin-left: -10px; display: flex; align-items: center; justify-content: center">{ic('back', 24)}</a>{sample()}</div>
    {h("A loan's real cost", 30)}
    {card(field('You borrow', 'R 8 000') + field('Over', '12 months') + field('Interest rate', '27.75% a year') + field('Fees', 'R 1 150, then R 69 a month'), pad='4px 16px 8px', gap=0)}
    {card(small('You would pay back', PLUM, 700) + '<span style="' + SERIF + '; font-size: 46px; line-height: 1; color: ' + PLUM + '">R 11 411</span>' + small('R 951 a month for 12 months. R 3 411 on top of what you borrow.', BODY) + '<span style="display: flex; height: 14px; margin-top: 6px">' + seg + '</span><div style="display: flex; flex-direction: column; gap: 6px; margin-top: 4px">' + keys + '</div>', pad='18px', gap=8)}
    <a href="#" style="min-height: 56px; padding: 0 16px; background: {WHITE}; border-radius: 4px; display: flex; align-items: center; gap: 12px; text-decoration: none; color: {BODY}">{ic('doc', 22)}<span style="flex-grow: 1; font-size: 15px; font-weight: 600">Explain my agreement</span>{ic('chev', 18, GREY)}</a>
    <span style="font-size: 13px; line-height: 1.5; color: {GREY}">AWO explains. It never says whether to borrow, or from whom.</span>""", gap=12)}{tabbar('Hub')}'''
    return screen(STONE, inner)


def community():
    faces = ''.join(f'<img src="{IMG[k]}" alt="" style="width: 34px; height: 34px; border-radius: 999px; object-fit: cover; box-shadow: 0 0 0 2px {WHITE}; margin-left: {"-8px" if i else "0"}">' for i, k in enumerate(['thandi', 'grace', 'amara', 'lindiwe']))
    inner = f'''{status()}{scroll(f"""
    {h('Community', 34)}
    {card('<span style="display: flex; align-items: center; gap: 12px"><span style="display: flex">' + faces + '</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Safety net circle</span>' + small('8 women on the same step') + '</span>' + ic('chev', 18, GREY) + '</span>', pad='14px 16px')}
    {card(small("This week's question", BODY, 700) + '<span style="' + SERIF + '; font-size: 24px; line-height: 1.25; color: ' + BODY + '">What’s one money habit your mother taught you?</span>' + btn('Answer in your circle', 'primary', 46, 'margin-top: 6px'), BLUSH, '18px', 10)}
    {card('<span style="display: flex; align-items: center; gap: 10px"><img src="' + IMG['thandi'] + '" alt="" style="width: 40px; height: 40px; border-radius: 999px; object-fit: cover"><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Thandi</span>' + small('Safety net circle, 2 hours ago') + '</span></span><span style="' + SERIF + '; font-size: 21px; line-height: 1.3; color: ' + PLUM + '">Filled my safety net, a little at a time.</span><span style="display: flex; gap: 8px; margin-top: 4px">' + ''.join('<span style="height: 44px; padding: 0 14px; border-radius: 4px; box-shadow: inset 0 0 0 1px ' + WGREY + '; display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; color: ' + PLUM + '">' + t + '</span>' for t in ['Cheer', 'Same here', 'Taught me']) + '</span>', pad='16px', gap=10)}
    {card('<span style="display: flex; align-items: center; gap: 10px"><img src="' + IMG['wanjiru'] + '" alt="" style="width: 40px; height: 40px; border-radius: 999px; object-fit: cover"><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Wanjiru</span>' + small('Side hustles, yesterday') + '</span></span><span style="font-size: 15px; line-height: 1.5">Does anyone keep the stall’s money in its own wallet? How did you start?</span>' + small('9 replies'), pad='16px', gap=10)}
    <span style="font-size: 13px; line-height: 1.5; color: {GREY}">First names only. Nobody sees your numbers.</span>""", gap=12)}{tabbar('Community')}'''
    return screen(STONE, inner)


def me():
    areas = [('Everyday money', 71, False), ('Ready for surprises', 48, True), ('Knowing your options', 60, False), ('Clear goals', 69, False)]
    ar = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 10px 0; {"border-top: 1px solid " + WGREY + ";" if i else ""}">
        <span style="display: flex; justify-content: space-between; font-size: 14px; font-weight: {700 if f else 500}"><span>{n}{" (your focus)" if f else ""}</span><span>{v}</span></span>{bar(v, TERRA if f else PLUM)}</div>''' for i, (n, v, f) in enumerate(areas))
    pts = [(10, 46), (100, 32), (190, 16)]
    spark = (f'<svg width="200" height="56" viewBox="0 0 200 56" aria-hidden="true"><path d="M10 46L100 32L190 16" fill="none" stroke="{PLUM}" stroke-width="1.6"></path>'
             + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{PLUM if x == 190 else WHITE}" stroke="{PLUM}" stroke-width="1.6"></circle>' for x, y in pts) + '</svg>')
    inner = f'''{status()}{scroll(f"""
    <header style="display: flex; align-items: center; gap: 12px"><img src="{IMG['naledi']}" alt="" style="width: 48px; height: 48px; border-radius: 999px; object-fit: cover"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px">{h('Naledi', 24)}{small('Johannesburg')}</span>{sample()}</header>
    {card(small('Your DIVA profile', STONE, 600) + '<span style="display: flex; align-items: flex-end; justify-content: space-between">' + h('Stage 2 of 4', 34, STONE) + '<span style="display: flex; flex-direction: column; align-items: flex-end"><span style="' + SERIF + '; font-size: 40px; line-height: 1; color: ' + STONE + '">63</span>' + small('DIVA score', STONE, 600) + '</span></span>' + stones(1, 1, 310, 70) + small('For learning, never a credit score. Version 3, 13 September.', STONE), PLUM, '18px', 10)}
    {card(small('Your four areas', PLUM, 700) + ar, pad='14px 16px', gap=2)}
    {card('<span style="display: flex; align-items: center; justify-content: space-between">' + small('Your versions', PLUM, 700) + small('55, 59, 63') + '</span>' + spark, pad='14px 16px')}
    <div style="display: flex; gap: 10px">{btn('Compare', 'quiet', 48, 'flex: 1')}{btn(ic('download', 18, PLUM) + 'Report', 'quiet', 48, 'flex: 1')}</div>""", gap=12)}{tabbar('Me')}'''
    return screen(STONE, inner)


def what_changed():
    rows = [('Everyday money', 71, 71), ('Ready for surprises', 48, 53), ('Knowing your options', 60, 60), ('Clear goals', 69, 70)]
    rw = ''.join(f'''<div style="display: flex; align-items: center; gap: 12px; min-height: 52px; {"border-top: 1px solid " + WGREY + ";" if i else ""}">
        <span style="flex-grow: 1; font-size: 15px; font-weight: {700 if b - a >= 5 else 500}">{n}</span><span style="font-size: 14px; color: {GREY}">{a}</span>{ic('chev', 14, GREY)}
        <span style="{SERIF}; font-size: 22px; color: {TERRA if b - a >= 5 else PLUM}; min-width: 30px; text-align: right">{b}</span></div>''' for i, (n, a, b) in enumerate(rows))
    inner = f'''<div style="position: absolute; left: 0; right: 0; top: 0; height: 300px; background: {PLUM}"></div>{status(STONE)}{scroll(f"""
    {small('Check-in 4, 13 October', STONE, 600)}
    {h('Version 4 is ready.', 36, STONE)}
    <div style="display: flex; align-items: flex-end; gap: 14px; padding: 6px 0 18px"><span style="{SERIF}; font-size: 60px; line-height: .9; color: {STONE}">64</span><span style="display: flex; flex-direction: column; gap: 3px; padding-bottom: 4px"><span style="font-size: 15px; font-weight: 600; color: {STONE}">DIVA score, up 1</span><span style="font-size: 13px; color: {STONE}">September's version stays as it was.</span></span></div>
    {card(small('What moved', PLUM, 700) + rw, pad='14px 16px', gap=0)}
    {card(small('Why', PLUM, 700) + '<span style="font-size: 15px; line-height: 1.55">You kept the payday move going, so you are more ready for surprises. That area moved by five.</span>' + reviewed(), pad='14px 16px')}
    <div style="flex-grow: 1"></div>
    {btn("See this month's step")}""", bottom=0, gap=12)}'''
    return screen(STONE, inner)


SCREENS = [('BA-Welcome', 'Welcome', welcome, 844), ('BA-Signin', 'Sign in', signin, 844), ('BA-Question', 'The first check: a question', question, 844),
           ('BA-Reveal', 'Your DIVA profile, revealed', reveal, 844), ('BA-First-Step', 'Your first step', first_step, 844),
           ('BA-Home', 'Home', home, 900), ('BA-Learn', 'Learn', learn, 844), ('BA-Lesson', 'A lesson', lesson, 844), ('BA-Hub', 'Hub', hub, 844),
           ('BA-Loan', "A loan's real cost", loan_tool, 844), ('BA-Community', 'Community', community, 844), ('BA-Me', 'Me: your DIVA profile', me, 844),
           ('BA-What-Changed', 'What changed', what_changed, 844)]
FN = {n: fn for n, _t, fn, _h in SCREENS}
TITLES_SHORT = {n: t for n, t, _fn, _h in SCREENS}


def picture(html):
    """A screen used as an image: its links become plain text, so nothing in a marketing picture is a target."""
    return html.replace('<a href="#"', '<span').replace('</a>', '</span>')


def phone_board(name, title, fn, hgt):
    return page_html(title, 390, hgt, STONE, fn())


# ================================================================ Marketing

def device(name, w, dark=False):
    """A phone with one of the screens inside, cropped to 844, at width w."""
    sc = w / 390
    bez = round(12 * sc)
    return (f'<div style="width: {w + 2 * bez}px; height: {round(844 * sc) + 2 * bez}px; box-sizing: border-box; padding: {bez}px; border-radius: {round(52 * sc)}px; background: #1E1620; '
            f'box-shadow: {"0 0 0 2px rgba(245,235,227,.18)," if dark else ""} 0 40px 90px rgba(42,31,46,.32)">'
            f'<div role="img" aria-label="The {TITLES_SHORT[name]} screen" style="width: {w}px; height: {round(844 * sc)}px; border-radius: {round(42 * sc)}px; overflow: hidden"><div aria-hidden="true" style="width: 390px; height: 844px; overflow: hidden; transform: scale({sc:.4f}); transform-origin: 0 0">{picture(FN[name]())}</div></div></div>')


STORE = [('BA-Me', STONE, 'Know your <span style="color: ' + TERRA + '">DIVA score</span>.', 'Where your money life stands today, in plain words. For learning, never a credit score.'),
         ('BA-Home', PLUM, 'One step at a time.', 'One clear step each week, sized to your life.'),
         ('BA-Lesson', STONE, 'Learn money in <span style="color: ' + TERRA + '">three minutes</span>.', "Short lessons told through real women's stories."),
         ('BA-Loan', PLUM, 'Do the sums before you sign.', 'Tools that show the real cost. AWO never tells you what to choose.'),
         ('BA-Community', STONE, 'Grow with women who <span style="color: ' + TERRA + '">get it</span>.', 'Circles on the same step. First names only.'),
         ('BA-What-Changed', PLUM, 'Check in every 30 days.', 'Three questions, then what changed and why. Old versions never change.')]


def store_inner(i):
    name, bg, head, sub = STORE[i]
    dark = bg == PLUM
    fg = STONE if dark else PLUM
    acc = '' if not dark else f'<span style="display: block; margin-top: 30px">{rule(120)}</span>'
    return frame(bg, f'''<div style="position: absolute; left: 90px; top: 96px">{wordmark(40, fg)}</div>
      <h2 style="position: absolute; left: 90px; right: 90px; top: 220px; margin: 0; {SERIF}; font-weight: 500; font-size: 108px; line-height: 1.04; letter-spacing: -0.01em; color: {fg}">{head}</h2>
      <div style="position: absolute; left: 90px; right: 120px; top: 600px">{acc if dark else ''}<p style="margin: {"24px" if dark else "0"} 0 0; font-size: 38px; line-height: 1.4; color: {STONE if dark else BODY}">{sub}</p></div>
      <div style="position: absolute; left: 179px; top: 760px">{device(name, 680, dark)}</div>''', 1080, 1920, fg)


def store(i):
    return page_html(f'Store screenshot {i + 1}', 1080, 1920, STORE[i][1], store_inner(i))


def app_icon(size, mask='square'):
    r = {'square': round(size * .22), 'circle': size // 2, 'none': 0}[mask]
    art = (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">'
           f'<ellipse cx="28" cy="70" rx="15" ry="6.5" fill="{STONE}"></ellipse><ellipse cx="52" cy="53" rx="16" ry="7" fill="{STONE}"></ellipse>'
           f'<ellipse cx="75" cy="35" rx="14" ry="6.5" fill="none" stroke="{TERRA}" stroke-width="3" stroke-dasharray="4 4"></ellipse></svg>')
    return f'<span role="img" aria-label="AWO app icon" style="width: {size}px; height: {size}px; border-radius: {r}px; background: {PLUM}; display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0">{art}</span>'


def feature_inner():
    return f'''<div style="position: relative; width: 1024px; height: 500px; overflow: hidden; background: {PLUM}; {SANS}">
  <div style="position: absolute; left: 56px; top: 54px; width: 480px; display: flex; flex-direction: column; gap: 18px">
    {wordmark(30, STONE)}
    <h2 style="margin: 0; {SERIF}; font-weight: 500; font-size: 52px; line-height: 1.08; color: {STONE}">Financial intelligence for African women.</h2>
    {rule(80)}
    <p style="margin: 0; font-size: 19px; line-height: 1.45; color: {STONE}">Your DIVA score, money in plain words, and tools for your own sums. Free.</p></div>
  <div style="position: absolute; left: 600px; top: 40px">{device('BA-Home', 190, True)}</div>
  <div style="position: absolute; left: 800px; top: 90px">{device('BA-Me', 190, True)}</div></div>'''


def feature():
    return page_html('Feature graphic', 1024, 500, PLUM, feature_inner())


SHORT = 'Get your DIVA score, learn money in plain words and grow with women who get it.'


def listing():
    thumbs = ''.join(scaled(store_inner(i), 1080, 1920, .15) for i in range(6))
    icons = ''.join(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 8px">{app_icon(s, m)}<span style="font-size: 13px; color: {GREY}">{t}</span></span>' for s, m, t in [(120, 'square', 'Rounded square'), (120, 'circle', 'Circle mask'), (72, 'square', '72 px'), (48, 'square', '48 px')])
    chips = ''.join(f'<span style="height: 34px; padding: 0 12px; border-radius: 4px; box-shadow: inset 0 0 0 1px {WGREY}; background: {WHITE}; display: inline-flex; align-items: center; font-size: 14px; font-weight: 600; color: {PLUM}">{t}</span>' for t in ['Education', 'Free', 'Data stays in South Africa'])
    inner = f'''<div style="position: absolute; inset: 64px; display: flex; gap: 56px">
  <div style="width: 560px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px">
    <div style="display: flex; align-items: center; gap: 22px">{app_icon(112)}<div style="display: flex; flex-direction: column; gap: 6px"><span style="{SERIF}; font-size: 52px; line-height: 1; color: {PLUM}">AWO</span><span style="font-size: 18px; color: {BODY}">Money, understood.</span></div></div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap">{chips}</div>
    <section style="background: {WHITE}; border-radius: 4px; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px"><span style="display: flex; justify-content: space-between">{small('Short description', PLUM, 700, 14)}{small(str(len(SHORT)) + ' of 80')}</span><span style="font-size: 18px; line-height: 1.45; font-weight: 500">{SHORT}</span></section>
    <section style="background: {WHITE}; border-radius: 4px; padding: 18px 20px; display: flex; flex-direction: column; gap: 14px">{small('The app icon: the stepping stones, in the new palette', PLUM, 700, 14)}<div style="display: flex; gap: 22px; align-items: flex-end">{icons}</div>
      <span style="font-size: 14px; line-height: 1.5; color: {BODY}">Two stones she has stood on, in warm stone, and the next one dashed in terracotta, on plum. The stepping-stones icon (D-031), recoloured; the brief has no icon.</span></section>
  </div>
  <div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 16px">
    {small('Feature graphic, 1024 by 500', PLUM, 700, 15)}{scaled(feature_inner(), 1024, 500, .6)}
    {small('Phone screenshots, 1080 by 1920', PLUM, 700, 15)}<div style="display: flex; gap: 12px">{thumbs}</div>
    <span style="font-size: 14px; line-height: 1.5; color: {BODY}">Educational wording only. No ranking or promo words, no install prompts. Store name and copy are still open (Q-31). Every number on a screen is a sample.</span>
  </div></div>'''
    return page_html('Store listing in the new brand', 1720, 900, STONE, inner)


def landing():
    trust = ''.join(f'<span style="display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 500; color: {BODY}; white-space: nowrap">{ic(g, 22)}{t}</span>' for g, t in [('check', 'Free to use'), ('learn', 'Education, not advice'), ('lock', 'Your data stays in South Africa')])
    nav = ''.join(f'<a href="#" style="min-height: 44px; display: flex; align-items: center; font-size: 16px; font-weight: 500; color: {BODY}; text-decoration: none">{t}</a>' for t in ['How it works', 'Learn', 'Community', 'Sign in'])
    inner = f'''<header style="position: absolute; left: 80px; right: 80px; top: 36px; height: 56px; display: flex; align-items: center; gap: 36px">{wordmark(30, PLUM)}<span style="flex-grow: 1"></span>{nav}{btn('Get the app', 'primary', 48, 'padding: 0 22px')}</header>
<div style="position: absolute; left: 80px; top: 200px; width: 620px; display: flex; flex-direction: column; gap: 26px">
  <h1 style="margin: 0; {SERIF}; font-weight: 500; font-size: 76px; line-height: 1.05; letter-spacing: -0.01em; color: {PLUM}">Financial intelligence for African women.</h1>
  {rule(96)}
  <p style="margin: 0; font-size: 21px; line-height: 1.6; color: {BODY}; max-width: 560px">Know where your money life stands, understand what it means, and take one clear step at a time. Free, in plain words, at home or abroad.</p>
  <div style="display: flex; gap: 14px; align-items: center">{btn('Get your DIVA score', 'primary', 56, 'padding: 0 28px')}<a href="#" style="min-height: 48px; display: flex; align-items: center; font-size: 17px; font-weight: 600; color: {PLUM}; text-decoration: underline; text-underline-offset: 4px">How it works</a></div>
  <div style="display: flex; gap: 26px; margin-top: 14px; width: 720px">{trust}</div>
</div>
<div style="position: absolute; left: 790px; top: 150px; width: 470px; height: 640px; overflow: hidden"><img src="{IMG['naledi_table']}" alt="A woman working at her dining table" style="width: 100%; height: 100%; object-fit: cover; object-position: 30% 50%; {GRADE}"></div>
<div style="position: absolute; left: 1120px; top: 230px">{device('BA-Home', 250)}</div>
<span style="position: absolute; left: 80px; bottom: 40px; font-size: 14px; color: {GREY}">AWO gives education, not financial advice. The DIVA score is for learning, never a credit score. Sample page.</span>'''
    return page_html('Website hero in the new brand', 1440, 900, STONE, inner)


def ad_score():
    inner = f'''<h2 style="position: absolute; left: 90px; right: 90px; top: 90px; margin: 0; {SERIF}; font-weight: 500; font-size: 104px; line-height: 1.05; color: {PLUM}">What's your <span style="color: {TERRA}">DIVA score</span>?</h2>
<div style="position: absolute; left: 90px; right: 90px; top: 430px; background: {WHITE}; border-radius: 4px; padding: 48px; display: flex; gap: 48px; align-items: center">
  <span style="display: flex; flex-direction: column; gap: 14px"><span style="{SERIF}; font-size: 200px; line-height: 1; color: {PLUM}">63</span><span style="font-size: 26px; font-weight: 600; color: {PLUM}">DIVA score</span></span>
  <span style="display: flex; flex-direction: column; gap: 16px"><span style="{SERIF}; font-size: 54px; color: {PLUM}">Stage 2 of 4</span>{stones(1, 1, 420, 120, False)}<span style="font-size: 22px; color: {GREY}">Sample</span></span></div>
<div style="position: absolute; left: 90px; right: 90px; bottom: 80px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 30px; line-height: 1.35; color: {BODY}">For learning,<br>never a credit score.</span>{wordmark(46, PLUM)}</div>'''
    return page_html('Square ad: the DIVA score', 1080, 1080, STONE, inner)


def ad_photo():
    inner = f'''<img src="{IMG['together']}" alt="Four women laughing together" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; {GRADE}">
<span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(74,45,78,.96) 0, rgba(74,45,78,.82) 42%, rgba(74,45,78,0) 72%)"></span>
<div style="position: absolute; left: 90px; right: 90px; bottom: 90px; display: flex; flex-direction: column; gap: 28px">
  <h2 style="margin: 0; {SERIF}; font-weight: 500; font-size: 96px; line-height: 1.06; color: {STONE}">Money talk, among women who get it.</h2>
  {rule(120)}
  <span style="display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 30px; line-height: 1.35; color: {STONE}">Free money learning, at home<br>and abroad.</span>{wordmark(46, STONE)}</span></div>'''
    return page_html('Square ad: photo-led', 1080, 1080, PLUM, inner)


BOARDS = ([(n, (lambda n=n, t=t, fn=fn, hh=hh: phone_board(n, t, fn, hh))) for n, t, fn, hh in SCREENS]
          + [(f'BA-Store-{i + 1}', (lambda i=i: store(i))) for i in range(6)]
          + [('BA-Feature', feature), ('BA-Listing', listing), ('BA-Landing', landing), ('BA-Ad-Score', ad_score), ('BA-Ad-Photo', ad_photo)])
TITLES = dict({n: t for n, t, _f, _h in SCREENS}, **{f'BA-Store-{i + 1}': f'Store screenshot {i + 1}' for i in range(6)},
              **{'BA-Feature': 'Feature graphic, 1024 by 500', 'BA-Listing': 'Store listing and app icon', 'BA-Landing': 'Website hero',
                 'BA-Ad-Score': 'Square ad: the DIVA score', 'BA-Ad-Photo': 'Square ad: photo-led'})
ROWS = [('bst4', 'Applied to the app (Q-49): onboarding, from welcome to the first step', ['BA-Welcome', 'BA-Signin', 'BA-Question', 'BA-Reveal', 'BA-First-Step']),
        ('bst5', 'Applied to the app: the major screens', ['BA-Home', 'BA-Learn', 'BA-Lesson', 'BA-Hub', 'BA-Loan', 'BA-Community', 'BA-Me', 'BA-What-Changed']),
        ('bst6', 'Applied to the Play Store: six screenshots, the feature graphic, the listing and the icon', [f'BA-Store-{i + 1}' for i in range(6)] + ['BA-Feature', 'BA-Listing']),
        ('bst7', 'Applied to marketing: the website and two ads', ['BA-Landing', 'BA-Ad-Score', 'BA-Ad-Photo'])]
