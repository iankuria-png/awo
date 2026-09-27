"""Round 9, batch 5 (first half): around the app. Three emails, print (an A5 flyer and a workshop deck) and the app
in real places (a market stall, a commute, the printed report on a kitchen table, the reminder on a lock screen).

Rules these follow: no amounts, DIVA score or stage in an email or on paper that leaves the room (Q-47); one main
action each; every piece says what AWO is not; the QR code is real but only says it is a sample."""
import json

from lib9 import *  # noqa: F401,F403
from marketing7 import H, K, PHOTO_TOGETHER  # noqa: E402
from kit7 import board7  # noqa: E402

BAL = 'text-wrap: balance'
INK_PEN = '#1D3A8F'  # a blue ballpoint: only ever her own writing on paper

# The flyer's QR code (version 4, level M). It encodes "AWO sample QR code. The real link is still to come.",
# so a test scan says what it is and goes nowhere. Replace it when the real link exists (Q-31).
QR = ['1fc79f37f', '1043e8541', '1757adf5d', '17507015d', '1758aca5d', '105c74941', '1fd55557f', '001d24800', '17c3e947c',
      '189e058cd', '036024888', '11177091f', '0c5504495', '09bd70a46', '007c00116', '190093d2e', '0fef8e4b0', '073c9e849',
      '11c2f814a', '1d27efda5', '14e632593', '1c1726340', '11dab55ee', '1185e5c2f', '1145a87f8', '001052115', '1fc6f5756',
      '105871d1e', '1751e45f9', '175bf3bb7', '175ecdf48', '1041958d4', '1fda8a722']

CAP = {'bizhome': '/_blob/98c49bde66d116bc51f599dc9dcecbe3', 'podcast': '/_blob/2cdb905380728d20af96f186b3c4906f',
       'report': '/_blob/0c8c27441959f830b270811d10eea389', 'me': '/_blob/d5c4a5e69456dcdc10e834e90f32445a',
       'lock': '/_blob/6f3a4c5dce73ec89bb40a3ed8158b154', 'entry': '/_blob/1c34be39cae7eae7ebaa0e16cd349250',
       'words': '/_blob/d24306b25edd77ede9cf986edfb52966'}


def js(o):
    return json.dumps(o, ensure_ascii=False)


def qr_svg(size, fg=INK, bg='#FFFFFF', label='QR code. A sample: it says so when scanned.'):
    n, q = len(QR), 4
    d = ''.join(f'M{x + q} {y + q}h1v1h-1z' for y, row in enumerate(QR) for x, bit in enumerate(bin(int(row, 16))[2:].zfill(n)) if bit == '1')
    t = n + 2 * q
    return (f'<svg role="img" aria-label="{label}" width="{size}" height="{size}" viewBox="0 0 {t} {t}" shape-rendering="crispEdges" style="display: block; flex-shrink: 0">'
            f'<rect width="{t}" height="{t}" fill="{bg}"></rect><path d="{d}" fill="{fg}"></path></svg>')


def seg(hole, labels, aria, w=None):
    btns = ''.join(f'<button onClick="[[ {hole}{j} ]]" aria-pressed="[[ {hole}On{j} ]]" style="background: [[ {hole}Bg{j} ]]; color: [[ {hole}Fg{j} ]]; padding: 0 12px">{t}</button>' for j, t in enumerate(labels))
    return f'<div role="group" aria-label="{aria}" class="seg9" style="{f"width: {w}px" if w else ""}">{btns}</div>'


def seg_js(hole, n, cur):
    return ("    for (let j = 0; j < %d; j++) { v['%s' + j] = () => this.setState({ %s: j }); v['%sOn' + j] = %s === j; "
            "v['%sBg' + j] = %s === j ? '%s' : 'transparent'; v['%sFg' + j] = %s === j ? '#FFFFFF' : '%s'; }"
            % (n, hole, hole, hole, cur, hole, cur, EVG, hole, cur, INK))


def label(text):
    return f'<span style="font-size: 15px; font-weight: 600; color: {SEC}">{text}</span>'


def rules_card(title_text, items, bg='#FFFFFF'):
    rl = ''.join(f'<span style="display: flex; gap: 10px; font-size: 15px; line-height: 1.45; color: {SEC}"><span style="width: 6px; height: 6px; margin-top: 8px; flex-shrink: 0; border-radius: 999px; background: {EVG}"></span><span>{r}</span></span>' for r in items)
    return (f'<section style="border-radius: {R_L}px; background: {bg}; padding: 20px 22px; display: flex; flex-direction: column; gap: 10px">'
            f'<span style="font-size: 17px; font-weight: 600">{title_text}</span>{rl}</section>')


# ================================================================ Emails

def pal(dark):
    if dark:
        return dict(bg=DEEP, card=RAISED, ink=MOON, sub=NMUTED, line=NLINE, btn=LIME, btnfg=EVG, link=MINT, around=NIGHT)
    return dict(bg='#FFFFFF', card=MIST, ink=INK, sub=SEC, line=LINE7, btn=EVG, btnfg='#FFFFFF', link=EVG, around=MIST)


class Mail:
    """Blocks for one email, at desktop width (600) or on a phone (m)."""

    def __init__(self, dark=False, m=False):
        self.P, self.m = pal(dark), m
        self.pad = 22 if m else 40

    def head(self):
        return (f'<div style="background: {EVG}; padding: {16 if self.m else 22}px {self.pad}px; display: flex; align-items: center; justify-content: space-between">'
                f'{lockup(22 if self.m else 26, "#FFFFFF", LIME)}<span style="font-size: 12px; font-weight: 600; color: #FFFFFF; padding: 4px 8px; border: 1px dashed rgba(255,255,255,.7); border-radius: {R_S}px">Sample</span></div>')

    def body(self, *blocks, gap=24):
        return f'<div style="padding: {self.pad - 8}px {self.pad}px {self.pad}px; display: flex; flex-direction: column; gap: {gap}px">{"".join(blocks)}</div>'

    def h1(self, t):
        return f'<h2 style="margin: 0; font-size: {28 if self.m else 36}px; font-weight: 600; letter-spacing: -0.03em; line-height: 1.08; color: {self.P["ink"]}; {BAL}">{t}</h2>'

    def h2(self, t):
        return f'<span style="font-size: {17 if self.m else 18}px; font-weight: 600; color: {self.P["ink"]}">{t}</span>'

    def p(self, t, sub=True, size=None):
        return f'<p style="margin: 0; font-size: {size or (16 if self.m else 17)}px; line-height: 1.5; color: {self.P["sub"] if sub else self.P["ink"]}">{t}</p>'

    def btn(self, t, href='#'):
        w = 'width: 100%;' if self.m else 'align-self: flex-start; padding: 0 28px;'
        return (f'<a href="{href}" style="{w} height: 52px; box-sizing: border-box; border-radius: {R_M}px; background: {self.P["btn"]}; color: {self.P["btnfg"]}; '
                f'display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">{t}</a>')

    def links(self, *items):
        return (f'<span style="display: flex; flex-wrap: wrap; gap: 4px 22px">' + ''.join(
            f'<a href="#" style="min-height: 44px; display: inline-flex; align-items: center; font-size: 15px; font-weight: 600; color: {self.P["link"]}; text-decoration: underline; text-underline-offset: 3px">{t}</a>' for t in items) + '</span>')

    def card(self, inner, bg=None, gap=10, outline=False):
        ring = f' box-shadow: inset 0 0 0 1.5px {self.P["line"]};' if outline else ''
        return f'<div style="border-radius: {R_L}px; background: {bg or self.P["card"]};{ring} padding: {16 if self.m else 22}px; display: flex; flex-direction: column; gap: {gap}px">{inner}</div>'

    def item(self, area, t, sub):
        return (f'<div style="display: flex; gap: 14px; align-items: flex-start">{area_badge(area, 40)}<span style="display: flex; flex-direction: column; gap: 2px">'
                f'<span style="font-size: 16px; font-weight: 600; color: {self.P["ink"]}">{t}</span><span style="font-size: 14px; line-height: 1.45; color: {self.P["sub"]}">{sub}</span></span></div>')

    def rule(self):
        return f'<span style="height: 1px; background: {self.P["line"]}"></span>'

    def foot(self, why, *extra):
        lines = ''.join(f'<p style="margin: 0">{t}</p>' for t in (why,) + extra)
        return (f'<div style="border-top: 1px solid {self.P["line"]}; padding: 20px {self.pad}px 28px; display: flex; flex-direction: column; gap: 10px; font-size: 13px; line-height: 1.5; color: {self.P["sub"]}">'
                f'{lines}{self.links("Choose your emails", "Unsubscribe")}'
                f'<p style="margin: 0">AWO gives education, not financial advice. Your data is stored in South Africa. AWO\'s postal address goes here.</p></div>')

    def stones(self, done, total=4, w=None):
        """Stones for check-ins: done ones filled, the next one dashed."""
        w = w or (300 if self.m else 360)
        h = round(w * .3)
        rx = w / (total * 3.2)
        out = ''
        for i in range(total):
            x = rx + 4 + i * (w - 2 * rx - 8) / (total - 1)
            y = h - rx * .6 - 6 - i * (h - rx * 1.2 - 12) / (total - 1)
            ry = rx * .4
            if i < done:
                fill = LIME if (i == done - 1 and done == total) else (MOON if self.P['bg'] == DEEP else EVG)
                out += f'<ellipse cx="{x:.0f}" cy="{y + 5:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="{"#2E3A36" if self.P["bg"] == DEEP else "#BFD9D2"}"></ellipse><ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="{fill}" stroke="{EVG}" stroke-width="2"></ellipse>'
            else:
                out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="none" stroke="{self.P["link"]}" stroke-width="2.5" stroke-dasharray="6 6"></ellipse>'
        return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; overflow: visible">{out}</svg>'

    def wrap(self, *parts):
        return f'<div style="background: {self.P["bg"]}; color: {self.P["ink"]}; font-family: \'Geist\', -apple-system, \'Segoe UI\', Roboto, Arial, sans-serif">{"".join(parts)}</div>'


def email_welcome(dark=False, m=False, halfway=False):
    E = Mail(dark, m)
    if halfway:
        lead = [E.h1('Welcome, Naledi.'),
                E.p("You're halfway through your first check. About four more minutes, and your answers so far are saved."),
                E.btn('Finish my check'),
                E.p('At the end you get your DIVA score: where your money life stands today, in plain words, and the one step that would help most. It is for learning, never a credit score.', size=15)]
    else:
        lead = [E.h1('Welcome, Naledi. Your first step is ready.'),
                E.p('Your DIVA profile is in the app, where only you can see it. It shows where your money life stands today, and one step that would help most.'),
                E.btn('Open AWO'),
                E.p('It is for learning, never a credit score, and it says nothing about loans.', size=15)]
    tries = E.card(E.h2('Three things to try this week')
                   + E.item('Learn', 'A three-minute lesson', 'What a safety net is for, told through Thandi\'s story.')
                   + E.item('Words', 'The word of the week: stokvel', 'Say it, keep it, and see it in a real sentence.')
                   + E.item('Community', 'Say hello in your circle', 'Women on the same step as you. First names only.'), gap=16)
    isnt = E.card(E.h2('What AWO is, and what it isn\'t')
                  + E.p('AWO teaches. It never tells you what to buy, where to bank or whether to borrow.', size=15)
                  + E.p('We never sell your data, and it is stored in South Africa.', size=15), bg=E.P['bg'], outline=True)
    scam = (f'<div style="display: flex; gap: 12px; align-items: flex-start; border-radius: {R_L}px; background: {BLUSH if not dark else "#3A1E27"}; padding: 16px 18px">'
            f'{ic("shield", 22, BLUSH_INK if not dark else BLUSH, 2)}<span style="font-size: 15px; line-height: 1.45; color: {BLUSH_INK if not dark else BLUSH}"><b style="font-weight: 600">AWO will never ask</b> for your PIN, a password or a payment, by email, SMS or WhatsApp. If someone does, it isn\'t us.</span></div>')
    return E.wrap(E.head(), E.body(*lead, tries, isnt, scam),
                  E.foot('You are getting this because you joined AWO on 13 July 2026.'))


def email_reminder(dark=False, m=False):
    E = Mail(dark, m)
    step = E.card(f'<span style="font-size: 14px; font-weight: 600; color: {E.P["sub"]}">Last month\'s step</span>'
                  + E.h2('Move a little into your safety net on payday')
                  + E.p('Did it happen? You\'ll say in the check-in. Either answer is fine; it helps pick this month\'s step.', size=15))
    nxt = E.card(E.h2('What happens next')
                 + E.item('Me', 'A new version of your DIVA profile', 'Version 4. September\'s stays as it was.')
                 + E.item('Home', 'What changed, and why', 'In plain words, even in a month that goes down.'), bg=E.P['bg'], gap=16, outline=True)
    return E.wrap(E.head(), E.body(
        E.stones(3),
        E.h1('Naledi, it\'s check-in day.'),
        E.p('Three questions about the last 30 days. About two minutes.'),
        E.btn('Start my check-in'),
        E.links('Remind me tonight', 'Skip this month'),
        E.p('Skipping is fine: nothing is lost, and next month picks up where you are.', size=15),
        step, nxt),
        E.foot('You get this on your check-in day, at 07:30, because you chose email reminders.', 'Change the day or time in the app, in Me, then Reminders.'))


def email_summary(dark=False, m=False):
    E = Mail(dark, m)
    tile = lambda n, t, bg, fg: (f'<div style="border-radius: {R_L}px; background: {bg}; padding: 16px; display: flex; flex-direction: column; gap: 4px">'
                                 f'<span style="font-size: {30 if m else 36}px; font-weight: 600; letter-spacing: -0.03em; color: {fg}">{n}</span><span style="font-size: 14px; line-height: 1.35; color: {fg}">{t}</span></div>')
    card_bg = E.P['card']
    tiles = (f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">'
             + tile('5', 'lessons finished', NIGHT, MOON) + tile('3', 'words saved', MINT, NIGHT) + tile('2', 'steps done', POOL, EVG) + tile('7', 'cheers from your circle', BLUSH, BLUSH_INK) + '</div>')
    words = ''.join(f'<span style="height: 36px; padding: 0 14px; border-radius: 8px; background: {card_bg}; display: inline-flex; align-items: center; font-size: 15px; font-weight: 600; color: {E.P["ink"]}">{w}</span>' for w in ['Dividend', 'Stokvel', 'Compound interest'])
    version = E.card(f'<span style="display: flex; gap: 12px; align-items: center">{area_badge("Me", 40)}<span style="font-size: 17px; font-weight: 600; color: {E.P["ink"]}">Your DIVA profile has a new version</span></span>'
                     + E.p('Version 4, from your check-in on 13 October. The score and what moved are in the app, where only you see them.', size=15)
                     + E.btn('See what changed'))
    return E.wrap(E.head(), E.body(
        E.h1('Your October on AWO'),
        E.p('Here is what you did this month. The numbers about your money stay in the app.'),
        E.card(f'<span style="display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap">{E.stones(4, w=240 if m else 280)}'
               f'<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600; color: {E.P["ink"]}">Four check-ins in a row</span><span style="font-size: 14px; color: {E.P["sub"]}">July to October</span></span></span>', bg=POOL if not dark else RAISED),
        tiles, version,
        f'<div style="display: flex; flex-direction: column; gap: 10px">{E.h2("Words you saved")}<span style="display: flex; flex-wrap: wrap; gap: 8px">{words}</span></div>',
        E.rule(),
        f'<div style="display: flex; flex-direction: column; gap: 8px">{E.h2("Coming up in November")}{E.p("Your step: keep the payday move going. Check-in 5 is on Friday 13 November.", size=15)}</div>'),
        E.foot('You get a summary on the 1st of each month, only for a month you used AWO. A quiet month gets no email.'))


EMAILS = {
    'welcome': dict(fn=email_welcome, title='Welcome email', h=1660, subject='Welcome to AWO, Naledi', pre='Your DIVA profile is ready, and so is your first step.',
                    when='13 Jul, 18:42', states=['She finished the first check', 'She stopped halfway'],
                    pre_alt="You're halfway through your first check. Your answers are saved.",
                    desc='Sent once, a few minutes after she joins. One main button. It says what AWO is and isn\'t, and warns about scams before anyone else can.',
                    notes=[('When it goes', ['A few minutes after she joins, once.', 'If she stops halfway through the first check, the welcome asks her to finish it instead (switch above).', 'Never before she has said yes to emails at sign-up.']),
                           ('Rules it follows', ['No DIVA score, stage or amounts in any email: an inbox is often shared, or read over a shoulder (Q-47).', 'One main button; everything else is a quiet link.', 'Says what AWO isn\'t, in the first email she gets.', 'The scam line: AWO never asks for a PIN, password or payment.'])]),
    'reminder': dict(fn=email_reminder, title='Check-in reminder email', h=1640, subject="It's check-in day, Naledi", pre='Three questions, about two minutes. Skipping is fine too.',
                     when='13 Oct, 07:30',
                     desc='For members who chose email reminders. The same three choices as the lock screen: start, tonight, or skip a month, with nothing lost.',
                     notes=[('When it goes', ['On her check-in day, at the time she chose, only if she hasn\'t checked in yet.', 'One email per check-in; a push reminder on the phone is the default, email is her choice (sample).', 'Never on a day she skipped.']),
                            ('Rules it follows', ['Last month\'s step, without its amount.', '"Did it happen? Either answer is fine": no guilt, ever.', 'What happens next: a new version, and the old one never changes.'])]),
    'summary': dict(fn=email_summary, title='Monthly summary email', h=1830, subject='Your October on AWO', pre='Four check-ins in a row, five lessons and three new words.',
                    when='1 Nov, 09:00',
                    desc='On the 1st of the month, for the month before. It counts what she did (lessons, words, steps, cheers), never money, and sends her to the app for the rest.',
                    notes=[('When it goes', ['The 1st of each month, for the month before.', 'Only for a month she used AWO. A quiet month gets no email, never a "we miss you".']),
                           ('Rules it follows', ['Counts what she did; never an amount, the score or the stage.', 'The streak is about showing up, like the milestone card.', 'One main button: what changed, in the app.'])]),
}


def inbox_preview(subject, pre, when):
    other = lambda: (f'<div style="display: flex; gap: 12px; padding: 14px 0; border-top: 1px solid {LINE7}; opacity: .55">'
                     f'<span style="width: 40px; height: 40px; border-radius: 999px; background: #DCE4DF; flex-shrink: 0"></span>'
                     f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 8px; padding-top: 4px"><span style="width: 45%; height: 10px; border-radius: 3px; background: #C9D3CE"></span>'
                     f'<span style="width: 80%; height: 10px; border-radius: 3px; background: #DCE4DF"></span></span></div>')
    return (f'<section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px 20px 6px; display: flex; flex-direction: column">'
            f'<span style="font-size: 17px; font-weight: 600; padding-bottom: 10px">In her inbox, on a phone</span>'
            f'<div style="display: flex; gap: 12px; padding: 14px 0; border-top: 1px solid {LINE7}">{app_badge(40)}'
            f'<span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 16px; font-weight: 700">AWO</span><span style="font-size: 13px; font-weight: 600; color: {EVG}">{when.split(", ")[1]}</span></span>'
            f'<span style="font-size: 15px; font-weight: 600">[[ subj ]]</span>'
            f'<span style="font-size: 14px; line-height: 1.4; color: {SEC}; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden">[[ pre ]]</span></span></div>'
            f'{other()}{other()}</section>')


def email_board(key):
    e = EMAILS[key]
    fn, states = e['fn'], e.get('states')
    n = len(states) if states else 1
    desk = ''.join(f'<sc-if value="[[ d{s} ]]" hint-placeholder-val="[[ {"true" if s == 0 else "false"} ]]">{fn(False, False, s == 1) if states else fn(False, False)}</sc-if>' for s in range(n))
    subj_html = '[[ subj ]]'
    desktop = f'''<div style="width: 680px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px">{label('On a computer')}
      <div style="border-radius: {R_L}px; background: #FFFFFF; box-shadow: 0 0 0 1px rgba(16,24,20,.08), 0 24px 60px rgba(16,24,20,.12); overflow: hidden">
        <div style="padding: 20px 28px; border-bottom: 1px solid {LINE7}; display: flex; flex-direction: column; gap: 14px">
          <span style="font-size: 22px; font-weight: 600; letter-spacing: -0.01em">{subj_html}</span>
          <span style="display: flex; align-items: center; gap: 12px">{app_badge(40)}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">AWO</span><span style="font-size: 13px; color: {MUTED}">To Naledi</span></span><span style="font-size: 13px; color: {MUTED}">{e['when']}</span></span>
        </div>
        <div style="background: {MIST}; padding: 28px 40px"><div style="width: 600px; border-radius: {R_L}px; overflow: hidden; box-shadow: 0 0 0 1px rgba(16,24,20,.06)">{desk}</div></div>
      </div></div>'''
    def phone_chrome(dark):
        fg, line = (MOON, NLINE) if dark else (INK, LINE7)
        batt = (f'<span style="width: 24px; height: 12px; box-sizing: border-box; border-radius: 3px; border: 1.5px solid {fg}; padding: 1.5px; display: flex">'
                f'<span style="width: 70%; border-radius: 1px; background: {fg}"></span></span>')
        return (f'<div style="position: sticky; top: 0; z-index: 2; background: {NIGHT if dark else "#FFFFFF"}; color: {fg}; padding: 16px 20px 12px; border-bottom: 1px solid {line}; display: flex; flex-direction: column; gap: 6px">'
                f'<span style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 600"><span>{e["when"].split(", ")[1]}</span>{batt}</span>'
                f'<span style="display: flex; align-items: center; gap: 2px; margin-left: -8px; min-height: 36px; font-size: 16px; color: {MINT if dark else EVG}">{ic("back", 22, MINT if dark else EVG, 2.2)}Inbox</span>'
                f'<span style="font-size: 18px; font-weight: 600; line-height: 1.25">{subj_html}</span></div>')
    phones = ''.join(f'''<sc-if value="[[ p{k}{s} ]]" hint-placeholder-val="[[ {"true" if (k, s) == ("l", 0) else "false"} ]]"><div style="position: absolute; inset: 0; overflow-y: auto; background: {NIGHT if k == "d" else "#FFFFFF"}">{phone_chrome(k == "d")}{(fn(k == "d", True, s == 1) if states else fn(k == "d", True))}</div></sc-if>''' for k in 'ld' for s in range(n))
    phone = f'''<div style="width: 390px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px">{label('On a phone, in a mail app')}
      {seg('md', ['Light mail app', 'Dark mail app'], 'Mail app colours')}
      <div role="region" aria-label="The email on a phone. Scroll inside." tabindex="0" style="position: relative; width: 390px; height: 800px; border-radius: 40px; overflow: hidden; box-shadow: 0 0 0 10px #0B0F0E, 0 30px 70px rgba(16,24,20,.25); margin: 10px 0 0">{phones}</div>
      <span style="font-size: 14px; line-height: 1.45; color: {SEC}">Scroll inside the phone. In a dark mail app the green band stays, the page goes night and the button turns lime, so nothing is inverted by the app.</span></div>'''
    state_seg = f'<div style="display: flex; flex-direction: column; gap: 8px">{label("Which welcome")}{seg("ws", states, "Which welcome")}</div>' if states else ''
    notes = ''.join(rules_card(t, items) for t, items in e['notes'])
    plain = (f'<section style="border-radius: {R_L}px; background: #FFFFFF; padding: 16px 20px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 17px; font-weight: 600">Subject and preview text</span>'
             f'<span style="font-size: 15px; line-height: 1.45; color: {SEC}">Subject: [[ subjN ]] characters, so it fits a phone\'s inbox. Preview: [[ preN ]] characters. Both name no amount.</span>'
             f'<span style="font-size: 15px; line-height: 1.45; color: {SEC}">Every email also goes as plain text, and reads well in Geist or the phone\'s own font. Images are never needed to understand it.</span></section>')
    right = f'''<div style="width: 540px; flex-shrink: 0; display: flex; flex-direction: column; gap: 16px">{state_seg}{inbox_preview(e['subject'], e['pre'], e['when'])}{plain}{notes}</div>'''
    body = f'  <div style="display: flex; gap: 44px; align-items: flex-start">{desktop}{phone}{right}</div>'
    pre_alt = e.get('pre_alt', e['pre'])
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const md = st.md || 0, ws = st.ws || 0;
    const v = {};
%s
%s
    for (let s = 0; s < %d; s++) { v['d' + s] = ws === s; v['pl' + s] = md === 0 && ws === s; v['pd' + s] = md === 1 && ws === s; }
    v.subj = %s;
    v.pre = ws === 1 ? %s : %s;
    v.subjN = v.subj.length; v.preN = v.pre.length;
    return v;
  }
}''' % (seg_js('md', 2, 'md'), seg_js('ws', n, 'ws') if states else '', n, js(e['subject']), js(pre_alt), js(e['pre']))
    return board7(e['title'], e['desc'], body, logic, 1800, e['h'], css=CSS9 + MAIL_CSS)


MAIL_CSS = """
.seg9 button{white-space:nowrap}
[role=region]:focus-visible{outline:3px solid #0F4A36;outline-offset:14px}
"""


# ================================================================ Print: the A5 flyer

AUDIENCES = [
    dict(key='church', tab='Church groups', photo=IMG['grace_dancing'], pos='50% 18%', alt='An older woman dancing at a street celebration',
         head='Learn money together, after the service.', sub='A free money-learning app for women, and a workshop for your fellowship.',
         fill=[('Group', 'Women\'s fellowship'), ('When', 'Sun 8 Nov, after the service'), ('Where', 'The church hall'), ('Ask for', 'Grace')]),
    dict(key='campus', tab='Campuses', photo=IMG['adaeze'], pos='50% 30%', alt='A young woman smiling at her laptop',
         head='Learn money before the first payslip.', sub='Bursaries, payslips, debt and saving, in plain words. Free.',
         fill=[('Group', 'Money over lunch'), ('When', 'Wed 11 Nov, 13:00'), ('Where', 'Library seminar room 2'), ('Ask for', 'Naledi')]),
    dict(key='stokvel', tab='Stokvel meetings', photo=PHOTO_TOGETHER, pos='50% 40%', alt='Four women laughing together on a street',
         head='Your stokvel saves together. Now learn together.', sub='Keep your group\'s book, learn the money words and check in every 30 days.',
         fill=[('Group', 'Kopano stokvel'), ('When', 'Sat 7 Nov, 14:00'), ('Where', 'Thandi\'s house'), ('Ask for', 'Thandi')]),
]
A5W, A5H = 560, 794  # A5 (148 by 210 mm) at 96 dpi


def flyer_front(a):
    return f'''<div class="sheet5" style="width: {A5W}px; height: {A5H}px; background: #FFFFFF; position: relative; overflow: hidden; display: flex; flex-direction: column">
      <div style="padding: 34px 34px 0; display: flex; flex-direction: column; gap: 14px">
        <span style="display: flex; justify-content: space-between; align-items: center">{lockup(24, EVG, LIME)}<span style="font-size: 12px; font-weight: 600; color: {SEC}; padding: 3px 7px; border: 1px dashed {SEC}; border-radius: {R_S}px">Sample</span></span>
        <h2 style="margin: 0; {H(46, EVG, BAL)}; line-height: 1">{a['head']}</h2>
        <p style="margin: 0; font-size: 16px; line-height: 1.4; color: {SEC}">{a['sub']}</p>
      </div>
      <img src="{a['photo']}" alt="{a['alt']}" style="margin: 20px 34px 0; width: calc(100% - 68px); height: 250px; object-fit: cover; object-position: {a['pos']}; border-radius: {R_L}px; display: block">
      <div style="flex-grow: 1"></div>
      <div style="margin: 0 34px 26px; border-radius: {R_L}px; background: {POOL}; padding: 14px; display: flex; gap: 16px; align-items: center">
        <span style="border-radius: {R_M}px; background: #FFFFFF; padding: 6px">{qr_svg(112, INK)}</span>
        <span style="display: flex; flex-direction: column; gap: 6px; color: {EVG}"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.15">Scan to get your DIVA score</span><span style="font-size: 13px; line-height: 1.4">Free, about six minutes. For learning, never a credit score.</span></span>
      </div>
      <div style="background: {EVG}; color: #FFFFFF; padding: 12px 34px; font-size: 12px; line-height: 1.4; display: flex; justify-content: space-between; gap: 12px"><span>Education, not financial advice.</span><span>Your data stays in South Africa.</span></div>
    </div>'''


def flyer_back(a):
    steps = [('Where am I?', 'Answer a short check. You get your DIVA score and where you stand, in plain words.'),
             ('What does it mean?', 'Three-minute lessons, money words and real women\'s stories. Even offline.'),
             ('What next?', 'One small step, then a check-in every 30 days to see what changed.')]
    st = ''.join(f'''<div style="display: flex; gap: 14px; align-items: flex-start">
          <svg width="44" height="30" viewBox="0 0 44 30" aria-hidden="true" style="flex-shrink: 0; margin-top: 2px"><ellipse cx="22" cy="19" rx="19" ry="8" fill="#BFD9D2"></ellipse><ellipse cx="22" cy="15" rx="19" ry="8" fill="{[EVG, EVG, LIME][i]}" stroke="{EVG}" stroke-width="2"></ellipse></svg>
          <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600; color: {EVG}">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">{d}</span></span></div>''' for i, (t, d) in enumerate(steps))
    isnt = ''.join(f'<span style="display: flex; gap: 8px; align-items: center; font-size: 14px; color: {INK}">{ic("close", 14, WARN_FG, 2.6)}{t}</span>' for t in ['Not a bank, and not a loan', 'Never tells you what to buy', 'Never sells your data', 'Never asks for your PIN'])
    fill = ''.join(f'''<div style="display: grid; grid-template-columns: 76px 1fr; align-items: end; gap: 10px; height: 34px">
          <span style="font-size: 13px; font-weight: 600; color: {SEC}; padding-bottom: 5px">{k}</span>
          <span style="border-bottom: 1.5px solid #9AA8A1; height: 100%; display: flex; align-items: flex-end; padding-bottom: 2px"><span class="hand" style="font-size: 21px; line-height: 1; color: {INK_PEN}; {HF}">{v}</span></span></div>''' for k, v in a['fill'])
    return f'''<div class="sheet5" style="width: {A5W}px; height: {A5H}px; background: #FFFFFF; position: relative; overflow: hidden; padding: 34px; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px">
      <h2 style="margin: 0; {H(34, EVG)}">How AWO works</h2>
      <div style="display: flex; flex-direction: column; gap: 16px">{st}</div>
      <div style="border-radius: {R_L}px; background: {MIST}; padding: 16px 18px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px 12px">{isnt}</div>
      <div style="border-radius: {R_L}px; box-shadow: inset 0 0 0 1.5px {EVG}; padding: 16px 18px; display: flex; flex-direction: column; gap: 4px">
        <span style="font-size: 17px; font-weight: 600; color: {EVG}">Our AWO session</span>
        <span style="font-size: 12px; color: {SEC}">For the organiser to fill in by hand.</span>{fill}
      </div>
      <div style="flex-grow: 1"></div>
      <span style="display: flex; justify-content: space-between; align-items: flex-end; font-size: 12px; line-height: 1.4; color: {SEC}"><span>AWO gives education, not financial advice.<br>Sample flyer. The real link and store name are still open.</span>{app_icon(40)}</span>
    </div>'''


def flyer():
    fronts = ''.join(f'<sc-if value="[[ au{i} ]]" hint-placeholder-val="[[ {"true" if i == 2 else "false"} ]]">{flyer_front(a)}</sc-if>' for i, a in enumerate(AUDIENCES))
    backs = ''.join(f'<sc-if value="[[ au{i} ]]" hint-placeholder-val="[[ {"true" if i == 2 else "false"} ]]">{flyer_back(a)}</sc-if>' for i, a in enumerate(AUDIENCES))
    sheet = lambda lab, inner: (f'<div style="display: flex; flex-direction: column; gap: 12px">{label(lab)}'
                                f'<div style="filter: [[ copyFilter ]]; box-shadow: 0 1px 2px rgba(16,24,20,.1), 0 24px 60px rgba(16,24,20,.16); transition: filter .3s">{inner}</div></div>')
    spec = rules_card('Print it', ['A5, 148 by 210 mm, with 3 mm bleed. 170 gsm matt, or any office paper.',
                                   'Reads on a photocopier: try the black-and-white switch. Meaning never rests on colour.',
                                   'The QR code is at least 25 mm wide, with a white quiet zone, on a plain ground.',
                                   'The back has lines for the organiser to write the group, time, place and who to ask.'])
    rules = rules_card('What it says, and never says', ['The DIVA score, always with what it is: for learning, never a credit score.',
                                                        'What AWO isn\'t, on the back: not a bank or a loan; never sells data or asks for a PIN.',
                                                        'No prizes, no "earn", no promises about money.',
                                                        'No logos of churches, universities or real groups; the organiser writes her own.'])
    qr_note = rules_card('The QR code', ['Real and scannable. Today it only says "AWO sample QR code. The real link is still to come."',
                                          'Each audience gets its own link, so AWO can count sign-ups from a flyer without tracking anyone (to confirm).'])
    body = f'''  <div style="display: flex; gap: 40px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap">{seg('aud', [a['tab'] for a in AUDIENCES], 'Who the flyer is for')}
        <span style="display: flex; align-items: center; gap: 4px; font-size: 15px; font-weight: 600">Photocopied, in black and white{switch(0, 'Photocopied, in black and white')}</span></div>
      <div style="display: flex; gap: 36px">{sheet('Front', fronts)}{sheet('Back', backs)}</div>
    </div>
    <div style="width: 440px; flex-shrink: 0; display: flex; flex-direction: column; gap: 16px">{spec}{rules}{qr_note}</div>
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const aud = st.aud == null ? 2 : st.aud;
    const v = {};
%s
%s
    for (let i = 0; i < 3; i++) v['au' + i] = aud === i;
    v.copyFilter = v.sw0 ? 'grayscale(1) contrast(1.15)' : 'none';
    return v;
  }
}''' % (seg_js('aud', 3, 'aud'), switch_js(1, [False]))
    html = board7('A5 flyer, front and back', 'For churches, campuses and stokvel meetings: one flyer, three openings. The back explains the loop in three questions and leaves room for the organiser\'s own handwriting.', body, logic, 1760, 1180, css=CSS9 + MAIL_CSS)
    return html


# ================================================================ Print: the workshop deck

SW, SHH = 1280, 720


def slide_wrap(bg, inner, fg=INK):
    return f'<div style="position: relative; width: {SW}px; height: {SHH}px; overflow: hidden; background: {bg}; color: {fg}">{inner}</div>'


def slide_foot(col, accent, left='AWO workshop'):
    return (f'<div style="position: absolute; left: 64px; right: 64px; bottom: 40px; display: flex; justify-content: space-between; align-items: center; font-size: 18px; color: {col}">'
            f'<span>{left}</span>{lockup(28, col, accent)}</div>')


def slides():
    s = []
    s.append(('Title', slide_wrap(EVG, f'''<div style="position: absolute; left: 80px; top: 80px">{lockup(40, "#FFFFFF", LIME)}</div>
      <h2 style="position: absolute; left: 80px; right: 380px; top: 210px; margin: 0; {H(112, '#FFFFFF')}">Money, understood.</h2>
      <p style="position: absolute; left: 80px; top: 470px; margin: 0; font-size: 32px; color: {ON_EVG}">A 45-minute workshop</p>
      <p style="position: absolute; left: 80px; bottom: 80px; margin: 0; font-size: 26px; color: #FFFFFF">With <span style="border-bottom: 2px dashed {LIME}; padding: 0 4px">your name here</span></p>
      <div style="position: absolute; right: 60px; top: 150px">{stones_svg(3, 330, 330, new_last=True, dark=True)}</div>''', '#FFFFFF'),
        'Welcome everyone. Say what the next 45 minutes hold: three questions, one story, one thing to try. Nobody will be asked to share an amount.'))
    qs = [('Where am I?', 'A short check gives your DIVA score'), ('What does it mean?', 'Plain words, and a real story'), ('What next?', 'One small step for this month')]
    cols = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 18px">
        <svg width="150" height="60" viewBox="0 0 150 60" aria-hidden="true"><ellipse cx="75" cy="38" rx="68" ry="20" fill="#BFD9D2"></ellipse><ellipse cx="75" cy="30" rx="68" ry="20" fill="{[EVG, EVG, LIME][i]}" stroke="{EVG}" stroke-width="3"></ellipse></svg>
        <span style="{H(46, EVG)}">{q}</span><span style="font-size: 26px; line-height: 1.35; color: {SEC}">{d}</span></div>''' for i, (q, d) in enumerate(qs))
    s.append(('Today', slide_wrap(POOL, f'''<h2 style="position: absolute; left: 80px; top: 70px; margin: 0; {H(72, EVG)}">Today, three questions</h2>
      <div style="position: absolute; left: 80px; right: 80px; top: 230px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px">{cols}</div>{slide_foot(EVG, LIME)}'''),
        'These are the same three questions the app asks. Point to the stones: each one is a step she has stood on, and the lime one is next.'))
    s.append(('Big idea', slide_wrap(NIGHT, f'''<h2 style="position: absolute; left: 80px; right: 520px; top: 110px; margin: 0; {H(80, MOON, BAL)}">A safety net is money you don't plan to spend.</h2>
      <p style="position: absolute; left: 80px; right: 560px; top: 420px; margin: 0; font-size: 28px; line-height: 1.4; color: {NMUTED}">It is there for the car repair, the school trip, the month the hours are cut.</p>
      <div style="position: absolute; right: 150px; top: 120px; width: 220px; height: 460px; border-radius: 110px; box-shadow: inset 0 0 0 6px {LIME}; overflow: hidden"><span style="position: absolute; left: 0; right: 0; bottom: 0; height: 38%; background: {LIME}"></span></div>{slide_foot(NMUTED, LIME)}''', MOON),
        'Ask: what would a surprise cost look like in your life? Let people answer in general terms. Then show the pool: it fills a little at a time.'))
    s.append(('A word', slide_wrap(MIST, f'''<div style="position: absolute; left: 330px; right: 330px; top: 60px; height: 560px; border-radius: 310px 310px {R_L * 2}px {R_L * 2}px; background: {LIME}; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 170px 50px 0; box-sizing: border-box; gap: 12px">
        <span style="font-size: 24px; font-weight: 600; color: {EVG}">A money word</span><span style="{H(104, EVG)}">Stokvel</span><span style="font-size: 24px; color: {EVG}">Say it: stok-fel</span>
        <p style="margin: 0; font-size: 28px; line-height: 1.3; color: {INK}">A savings group that takes turns with the pot.</p></div>{slide_foot(EVG, LIME)}'''),
        'Ask who is in a stokvel, chama or savings club. Let two people say how theirs works. Every group\'s rules are its own.'))
    s.append(('Talk', slide_wrap(BLUSH, f'''<span style="position: absolute; left: 80px; top: 80px; height: 48px; padding: 0 18px; border-radius: {R_M}px; background: {BLUSH_INK}; color: {BLUSH}; display: inline-flex; align-items: center; font-size: 22px; font-weight: 600">Talk in pairs, 5 minutes</span>
      <h2 style="position: absolute; left: 80px; right: 120px; top: 190px; margin: 0; {H(84, BLUSH_INK, BAL)}">What's one money habit you learned at home?</h2>
      <p style="position: absolute; left: 80px; top: 500px; margin: 0; font-size: 28px; color: {BLUSH_2}">Nobody needs to share an amount.</p>{slide_foot(BLUSH_INK, "#FFFFFF")}''', BLUSH_INK),
        'Time five minutes. Walk the room. Ask two pairs to share one habit each with everyone, only if they want to.'))
    s.append(('A story', slide_wrap(NIGHT, f'''<img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her stall" style="position: absolute; left: 0; top: 0; width: 560px; height: 720px; object-fit: cover; object-position: 60% 30%">
      <div style="position: absolute; left: 630px; right: 70px; top: 110px; display: flex; flex-direction: column; gap: 26px">
        <span class="hand" style="font-size: 58px; line-height: 1.15; color: {LIME}; {HF}">The notebook tells me before I panic.</span>
        <span style="font-size: 24px; line-height: 1.4; color: {NMUTED}">Wanjiru, a market trader in Nairobi. A sample story, in her own words.</span></div>{slide_foot(NMUTED, LIME, '').replace('left: 64px', 'left: 630px')}''', MOON),
        'Read the quote aloud. Wanjiru\'s full story is in the app, in Learn. Ask: what would you write in a notebook like hers?'))
    s.append(('Try it', slide_wrap(POOL, f'''<h2 style="position: absolute; left: 80px; right: 560px; top: 90px; margin: 0; {H(76, EVG, BAL)}">Get your DIVA score, now.</h2>
      <p style="position: absolute; left: 80px; right: 600px; top: 300px; margin: 0; font-size: 28px; line-height: 1.4; color: {SEC}">About six minutes. For learning, never a credit score. Only you see it.</p>
      <div style="position: absolute; left: 80px; bottom: 90px; border-radius: {R_L}px; background: #FFFFFF; padding: 12px">{qr_svg(170)}</div>
      <div style="position: absolute; right: 120px; top: 40px">{device(CAP['entry'], 300, 'The AWO welcome screen: Join for free')}</div>''', EVG),
        'Give everyone ten minutes. Help anyone without data to use the venue Wi-Fi. Walk the room, but never look at anyone\'s answers.'))
    s.append(('Close', slide_wrap(EVG, f'''<h2 style="position: absolute; left: 80px; right: 480px; top: 110px; margin: 0; {H(96, '#FFFFFF', BAL)}">One step this month. That's all.</h2>
      <p style="position: absolute; left: 80px; right: 520px; top: 380px; margin: 0; font-size: 26px; line-height: 1.45; color: {ON_EVG}">AWO gives education, not financial advice. It never tells you what to buy, and never asks for your PIN.</p>
      <div style="position: absolute; right: 90px; top: 110px; display: flex; flex-direction: column; align-items: center; gap: 14px"><span style="border-radius: {R_L}px; background: #FFFFFF; padding: 12px">{qr_svg(260)}</span><span style="font-size: 22px; color: #FFFFFF">Scan to start</span></div>{slide_foot(ON_EVG, LIME)}''', '#FFFFFF'),
        'Thank people. Say when the next session is. Remind them that AWO never asks for a PIN, and to be careful of anyone who does.'))
    return s


def workshop():
    S = slides()
    main = ''.join(f'<sc-if value="[[ sl{i} ]]" hint-placeholder-val="[[ {"true" if i == 0 else "false"} ]]">{html}</sc-if>' for i, (_n, html, _t) in enumerate(S))
    thumbs = ''.join(f'''<button onClick="[[ go{i} ]]" aria-pressed="[[ slOn{i} ]]" aria-label="Slide {i + 1}: {n}" style="display: flex; flex-direction: column; gap: 6px; align-items: flex-start">
          <span style="display: block; width: 144px; height: 81px; overflow: hidden; border-radius: {R_S}px; box-shadow: 0 0 0 [[ thW{i} ]]px {EVG}; transition: box-shadow .18s"><span style="display: block; width: {SW}px; height: {SHH}px; transform: scale(.1125); transform-origin: 0 0; pointer-events: none">{html}</span></span>
          <span style="font-size: 13px; font-weight: 600; color: [[ thC{i} ]]">{i + 1}. {n}</span></button>''' for i, (n, html, _t) in enumerate(S))
    notes = js([t for _n, _h, t in S])
    names = js([n for n, _h, _t in S])
    nav = lambda hole, lab, g: (f'<button onClick="[[ {hole} ]]" aria-label="{lab}" style="width: 48px; height: 48px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; display: flex; align-items: center; justify-content: center">{g}</button>')
    right = f'''<div style="width: 400px; flex-shrink: 0; display: flex; flex-direction: column; gap: 16px">
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 20px 22px; display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 17px; font-weight: 600">Speaker notes</span><span style="font-size: 14px; color: {MUTED}; font-variant-numeric: tabular-nums">[[ pos ]]</span></span>
        <span style="font-size: 20px; font-weight: 600; color: {EVG}">[[ slName ]]</span>
        <p aria-live="polite" style="margin: 0; font-size: 16px; line-height: 1.55; color: {SEC}; min-height: 130px">[[ note ]]</p>
        <span style="display: flex; gap: 8px">{nav('prev', 'Previous slide', ic('back', 20, INK, 2.2))}{nav('next', 'Next slide', f'<span style="display: flex; transform: scaleX(-1)">{ic("back", 20, INK, 2.2)}</span>')}</span>
      </section>
      {rules_card('Rules for whoever presents', ['Nobody shares an amount out loud, and nobody is asked to.', "Never name a bank, product or provider as the one to choose. Point to the Hub's tools instead.", 'Text no smaller than 24 pixels on a 1280 slide, so the back of a hall can read it.', 'One idea a slide. The notes carry the rest.'])}
      {rules_card('The template', ['Eight layouts: title, agenda, a big idea, a money word, talk in pairs, a story, try it, close.', 'Each area keeps its colour: night for Learn, blush for Community, lime for a word.', "The hand appears only in a member's own words."])}
    </div>'''
    body = f'''  <div style="display: flex; gap: 32px; align-items: flex-start">
    <div style="display: flex; flex-direction: column; gap: 20px">
      <div role="region" aria-label="The current slide" style="width: {SW}px; height: {SHH}px; border-radius: {R_M}px; overflow: hidden; box-shadow: 0 24px 60px rgba(16,24,20,.18)">{main}</div>
      <div style="display: flex; gap: 0; justify-content: space-between">{thumbs}</div>
    </div>{right}
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const n = %d, i = st.i || 0, notes = %s, names = %s;
    const v = { note: notes[i], slName: names[i], pos: (i + 1) + ' of ' + n,
      prev: () => this.setState({ i: Math.max(0, i - 1) }), next: () => this.setState({ i: Math.min(n - 1, i + 1) }) };
    for (let k = 0; k < n; k++) { v['sl' + k] = k === i; v['slOn' + k] = k === i; v['go' + k] = () => this.setState({ i: k });
      v['thW' + k] = k === i ? 3 : 0; v['thC' + k] = k === i ? '%s' : '%s'; }
    return v;
  }
}''' % (len(S), notes, names, EVG, MUTED)
    return board7('Workshop slides', 'A template for AWO workshops in halls, churches, campuses and stokvel meetings: eight layouts on the loop\'s three questions, with speaker notes. Use the arrows or pick a slide.', body, logic, 1860, 1150, css=CSS9)


# ================================================================ In real places

def place(title_text, where, who, scene, asks, control, logic_extra, w=1760, h=1000, scene_w=1080, chip='Composite: a stock photo and a live screen'):
    rows = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 4px; padding: 14px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="font-size: 16px; font-weight: 600">{a}</span><span style="font-size: 15px; line-height: 1.45; color: {SEC}">{b}</span></div>''' for i, (a, b) in enumerate(asks))
    inner = f'''<div style="position: absolute; left: 0; top: 0; width: {scene_w}px; height: {h}px; overflow: hidden">{scene}</div>
<div style="position: absolute; left: {scene_w}px; right: 0; top: 0; bottom: 0; padding: 56px 52px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px; background: #E4EAE6">
  <span style="display: flex; justify-content: space-between; align-items: center; gap: 12px"><span style="font-size: 15px; font-weight: 600; color: {SEC}">{where}</span>{sample_chip(SEC, chip)}</span>
  <h1 style="margin: 0; {H(52, INK, BAL)}">{title_text}</h1>
  <p style="margin: 0; font-size: 18px; line-height: 1.45; color: {SEC}">{who}</p>
  {control}
  <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 6px 22px; display: flex; flex-direction: column">
    <span style="font-size: 13px; font-weight: 600; color: {MUTED}; padding-top: 14px">What this place asks, and how the design answers</span>{rows}</section>
</div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const v = {};
%s
    return v;
  }
}''' % logic_extra
    return screen_board(title_text, w, h, '#E4EAE6', inner, logic)


def control_row(i, text):
    return f'<span style="display: flex; align-items: center; justify-content: space-between; gap: 12px; border-radius: {R_L}px; background: #FFFFFF; padding: 6px 8px 6px 20px; font-size: 16px; font-weight: 600">{text}{switch(i, text)}</span>'


def floating_phone(src, w, alt, x, y, rot=0, overlay='', dark=False):
    h = round(w * 1688 / 780)
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; transform: rotate({rot}deg); width: {w + 24}px; height: {h + 24}px; box-sizing: border-box; padding: 12px; border-radius: {round(w * .14)}px; background: #0B0F0E; '
            f'box-shadow: 0 {"0 0 2px #2E3A36, 0" if dark else ""} 40px 90px rgba(11,15,14,.4)">'
            f'<div style="position: relative; width: {w}px; height: {h}px; border-radius: {round(w * .115)}px; overflow: hidden"><img src="{src}" alt="{alt}" style="width: 100%; height: 100%; display: block">{overlay}</div></div>')


def place_stall():
    glare = (f'<span aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(120% 80% at 80% 10%, rgba(255,255,255,.85), rgba(255,255,255,.35) 55%, rgba(255,255,255,.15)); '
             f'opacity: [[ glare ]]; transition: opacity .4s"></span>')
    scene = f'''<img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her homeware stall, looking at her stock" style="position: absolute; left: -440px; top: 0; width: 1500px; height: 1000px; object-fit: cover; object-position: 40% 30%; filter: brightness([[ sunB ]]); transition: filter .4s">
  {floating_phone(CAP['bizhome'], 330, "Wanjiru's business Home: this week's step and her notebook", 690, 120, -4, glare)}
  <div style="position: absolute; left: 560px; top: 800px; border-radius: {R_L}px; background: #FFFFFF; padding: 14px 18px; display: flex; align-items: center; gap: 12px; box-shadow: 0 20px 50px rgba(11,15,14,.3); transform: rotate(-2deg)">
    <span style="width: 44px; height: 44px; border-radius: {R_M}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{ic8('plus', 24, EVG, 2.6)}</span>
    <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 18px; font-weight: 600">KSh 350 in, cash</span><span style="font-size: 14px; color: {MUTED}">Saved on your phone. Sends when there's signal.</span></span></div>'''
    asks = [('Bright sun washes a screen out.', 'Amounts and buttons carry 7:1 contrast and weight 600; nothing she needs is in light grey. Turn the sun on to test it.'),
            ('One hand is holding change.', 'Adding a sale is one tap from Home, in reach of the thumb, and the keypad opens on the amount.'),
            ('Signal comes and goes, and data costs money.', 'The notebook works offline, saves on the phone and sends later, and says so.'),
            ('Customers can see her screen.', 'An eye in the header hides every amount until she taps it (proposed).')]
    return place('At a market stall', 'Nairobi, midday', 'Wanjiru keeps the stall\'s notebook between customers: money in, money out, every evening.',
                 scene, asks, control_row(0, 'In full sun'),
                 switch_js(1, [False]) + "\n    v.glare = v.sw0 ? 1 : 0; v.sunB = v.sw0 ? 1.18 : 1;")


def place_commute():
    ug = (f'<sc-if value="[[ sw0 ]]" hint-placeholder-val="[[ false ]]"><span style="position: absolute; left: 14px; right: 14px; bottom: 96px; border-radius: {R_M}px; background: {MOON}; color: {INK}; padding: 10px 12px; display: flex; gap: 10px; align-items: center; font-size: 13px; line-height: 1.35; box-shadow: 0 10px 30px rgba(0,0,0,.4); animation: toastIn .3s both">'
          f'{ic8("wifi-off", 18, EVG)}<span>No signal. Words you saved, and lessons you downloaded, still work.</span></span></sc-if>')
    scene = f'''<img src="{IMG['amara_coat']}" alt="Amara outdoors in a winter coat, on her way to work" style="position: absolute; left: -260px; top: 0; width: 1500px; height: 1000px; object-fit: cover; object-position: 50% 30%; filter: brightness([[ ugB ]]); transition: filter .4s">
  {floating_phone(CAP['words'], 320, 'Words: decoding ETF, with where you live set to the UK', 90, 150, 3, ug, dark=True)}'''
    asks = [('No signal between stations.', 'Saved words and downloaded lessons work offline. Episodes save at home on Wi-Fi, and the player says how big each one is.'),
            ('Standing, one hand on a rail.', 'The level switch (new to this, the basics, go deeper) is one tap, low enough for the thumb.'),
            ('She lives in London, not Johannesburg.', 'Where you live changes the example: in the UK, an ETF is often held in an ISA.'),
            ('People all around her.', 'Nothing about her own money shows in Learn or Words.')]
    return place('On a commute', 'London, 07:40', 'Amara, a nurse, has 40 minutes each way on the Underground. Her pension statement said "ETF", so she looks it up.',
                 scene, asks, control_row(0, 'Underground, no signal'),
                 switch_js(1, [False]) + "\n    v.ugB = v.sw0 ? .72 : 1;")


def place_table():
    grain = ('<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.45" numOctaves="3" seed="7"></feTurbulence>'
             '<feColorMatrix values="0 0 0 0 .36  0 0 0 0 .24  0 0 0 0 .15  0 0 0 .28 0"></feColorMatrix></filter>')
    circle = f'<path d="M0 26C2 8 40 -2 74 4S126 30 110 44 36 58 10 46C0 41 -1 34 2 28" fill="none" stroke="{INK_PEN}" stroke-width="3" stroke-linecap="round"></path>'
    scene = f'''<div style="position: absolute; inset: 0; background: #A77B55"></div>
  <svg width="1080" height="1000" aria-hidden="true" style="position: absolute; inset: 0"><defs>{grain}</defs><rect width="1080" height="1000" filter="url(#grain)"></rect></svg>
  <div style="position: absolute; left: 80px; top: 70px; width: 600px; height: 849px; transform: rotate(-5deg); box-shadow: 0 2px 3px rgba(40,24,10,.25), 0 30px 60px rgba(40,24,10,.35); filter: [[ copyF ]]; transition: filter .3s">
    <img src="{CAP['report']}" alt="Naledi's printed one-page DIVA report, September" style="width: 100%; height: 100%; display: block">
    <svg width="130" height="64" viewBox="-6 -4 128 66" aria-hidden="true" style="position: absolute; left: 480px; top: 362px; overflow: visible">{circle}</svg>
    <span class="hand" style="position: absolute; left: 64px; top: 728px; width: 420px; transform: rotate(-2deg); font-size: 26px; line-height: 1.15; color: {INK_PEN}; {HF}">ask Mum about the burial society</span>
  </div>
  <div style="position: absolute; left: 610px; top: 560px; transform: rotate(38deg); width: 300px; height: 14px; border-radius: 7px; background: linear-gradient(to right, #1D2B6B 0 88%, #C9D3CE 88% 94%, #6A7470 94%); box-shadow: 0 8px 14px rgba(40,24,10,.35)"></div>
  <div style="position: absolute; left: 770px; top: 70px; width: 200px; height: 200px; border-radius: 999px; background: #F2F1EC; box-shadow: 0 16px 40px rgba(40,24,10,.4); display: flex; align-items: center; justify-content: center"><span style="width: 150px; height: 150px; border-radius: 999px; background: radial-gradient(circle at 40% 40%, #6B4A35, #3A2518)"></span></div>
  {floating_phone(CAP['me'], 250, 'Her DIVA profile on the phone', 760, 380, 8)}'''
    asks = [('Printed for a family meeting, or for a counsellor.', 'One A4 page: where she stands, what it means in plain words, the date and version at the top.'),
            ('Printed in black and white.', 'Labels carry the meaning, never colour alone. Switch to photocopied to test it.'),
            ('Left on a table others use.', 'The page says what the score is on the page itself: learning readiness, never a credit score. Printing amounts asks first (proposed).'),
            ('She writes on it.', 'Wide margins; the next version will add a "My notes" box (proposed). Old versions never change, so her notes stay true to the page.')]
    return (place('The report on a kitchen table', 'Johannesburg, Sunday afternoon', 'Naledi printed September\'s report to talk about it with her mother. She circled the area she is working on.',
                           scene, asks, control_row(0, 'Photocopied, in black and white'),
                           switch_js(1, [False]) + "\n    v.copyF = v.sw0 ? 'grayscale(1) contrast(1.2)' : 'none';", chip='A drawn table, with the real report'))


def place_lock():
    s = .9
    scr_x, scr_y, scr_w, scr_h = 1020 * s, 276 * s, 362 * s, 754 * s
    left, top = 540 - 1201 * s, 520 - 653 * s
    scene = f'''<img src="{IMG['hero_photo']}" alt="Two hands holding a phone" style="position: absolute; left: {left:.0f}px; top: {top:.0f}px; width: {2400 * s:.0f}px; height: {1600 * s:.0f}px; display: block">
  <span aria-hidden="true" style="position: absolute; inset: 0; background: rgba(11,15,14,[[ nightA ]]); transition: background-color .4s; pointer-events: none"></span>
  <div style="position: absolute; left: {left + scr_x:.0f}px; top: {top + scr_y:.0f}px; width: {scr_w:.0f}px; height: {scr_h:.0f}px; border-radius: {40 * s:.0f}px; overflow: hidden; background: #0B0F0E">
    <img src="{CAP['lock']}" alt="The lock screen: Your check-in is ready, with Start, Tonight and Skip a month" style="width: 100%; height: auto; display: block; filter: brightness([[ nightB ]]); transition: filter .4s">
  </div>'''
    asks = [('Anyone nearby can read it.', 'No amount, score or stage, ever: only what it is and how long it takes.'),
            ('It is a glance, not a read.', 'Four words say what it is ("Your check-in is ready"), then how long it takes.'),
            ('A busy morning.', 'Tonight and Skip a month work from the notification itself. Nothing is lost by skipping.'),
            ('Every app asks for attention.', 'One reminder a check-in, and one the evening before only if she asks for it.')]
    return place('The reminder on a lock screen', 'Johannesburg, 07:30', 'Naledi\'s fourth check-in is due. The reminder arrives before work, and stays until she does it or skips.',
                 scene, asks, control_row(0, 'In a dark room'),
                 switch_js(1, [False]) + "\n    v.nightA = v.sw0 ? .62 : 0; v.nightB = v.sw0 ? .92 : 1;")


BOARDS = [('R9-Email-Welcome', lambda: email_board('welcome')), ('R9-Email-Reminder', lambda: email_board('reminder')),
          ('R9-Email-Summary', lambda: email_board('summary')), ('R9-Flyer-A5', flyer), ('R9-Workshop-Slides', workshop),
          ('R9-Place-Stall', place_stall), ('R9-Place-Commute', place_commute), ('R9-Place-Table', place_table), ('R9-Place-Lock', place_lock)]
