"""Round 8 marketing: the store set, listing, feature graphic, device hero and ads, refreshed for the Round 8 IA
(Home, Learn, Hub, Community, Me). Built like Round 7's (marketing7.py): 2x captures of the Round 8 screens in a
device frame, Geist, the stepping-stones lockup and app icon A. Corners scale with the canvas (14 becomes 40 at 1080).
The hand appears only in someone's own words. Store copy and the app name are still open (Q-31); every number is a sample.

When a screen changes: recapture it with capture8.mjs (see the README), upload the JPEG and update CAPS8."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
sys.path.insert(0, os.path.join(HERE, '..', 'round-7'))

from lib8 import *  # noqa: F401,F403
from marketing import canvas_board, device  # noqa: E402
from brand7 import app_icon, lockup  # noqa: E402,F401
from marketing7 import H, K, hand_hole, DIVA_FULL  # noqa: E402

CAPS8 = {
    'me': '/_blob/d51d3a8058fa852b31242735ec0f598e', 'home': '/_blob/15e1b287ae69912d749ec1ac1a4fa54b',
    'hub': '/_blob/14deaff9ebe4844560d29ff6f9b9c11a', 'hubbiz': '/_blob/ab3ff800841d6554394cd40a7d70fdf2',
    'payslip': '/_blob/afd6970e81a744a4333f7678fb3550c3', 'words': '/_blob/d24306b25edd77ede9cf986edfb52966',
    'stories': '/_blob/07c7ba47d9a70195a0c56c8412fae4f3', 'feed': '/_blob/b8158f1c8fb98071263ff24a0126f700',
    'shop': '/_blob/676de7a88eccc68b8c8713758ef7edfb', 'goals': '/_blob/2b752de0ae8f5a0c28b6bd64c408b3be',
    'topic': '/_blob/c30b27d9abf177654bc9d4923020e790', 'podcast': '/_blob/0e9d94bb9ed94a97f7ea291b2e38448d',
    'company': '/_blob/51e9c77e8b33a99f0970e36525dd9d1f',
}
CAPTURES = [  # key, board, what to press first (a tab name, or buttons), js to run before the capture
    ('me', 'R7-Me', None, 'swap-tabbar'),  # Me is unchanged from Round 7; it gets the Round 8 tab bar
    ('home', 'R8-Home', None, None), ('hub', 'R8-Hub', None, None), ('hubbiz', 'R8-Hub-Biz', None, None),
    ('payslip', 'R8-Tool-Payslip', None, "(() => { const k = [...document.querySelector('.scr').children]; k[1].style.display = 'none'; k[2].style.display = 'none'; })()"),
    ('words', 'R8-Words-Decoder', None, None), ('stories', 'R8-Learn', 'Stories', None), ('feed', 'R8-Feed', None, None),
    ('shop', 'R8-Shop-Public', None, None), ('goals', 'R8-Goals', None, None), ('topic', 'R8-Topic-Shares', ['Next', 'Next', 'Next'], None),
    ('podcast', 'R8-Podcast', None, None), ('company', 'R8-Company-Brief', None, None),
]


def capture_specs():
    """The specs capture8.mjs reads: python3 marketing8.py specs > caps.json"""
    swap = ("(() => { const n = document.querySelector('nav.tab'); const t = document.createElement('div'); t.innerHTML = "
            + json.dumps(tabbar8('Me', links=False)) + '; n.replaceWith(t.firstElementChild); })()')
    out = []
    for key, board, press, js in CAPTURES:
        spec = {'key': key, 'board': board}
        if isinstance(press, str):
            spec['click'] = press
        elif press:
            spec['clicks'] = press
        if js:
            spec['js'] = swap if js == 'swap-tabbar' else js
        out.append(spec)
    return out


HF = "font-family: '[[ handFont ]]', cursive"
BAL = 'text-wrap: balance'  # no one-word last lines in headlines

STORE8 = [
    ('me', POOL, EVG, SEC, LIME, 'Know your DIVA score.', 'Where your money life stands, in plain words. For learning, never a credit score.', 'Me: your DIVA profile'),
    ('home', EVG, LIME, ON_EVG, LIME, 'Goals of every kind.', 'A car, moving out, a trip home. Each one gets its own pool.', 'Home'),
    ('hub', LIME, EVG, INK, '#FFFFFF', 'Tools that do the sums with you.', 'Payslips, pay-day, debts and prices, worked out with your own numbers.', 'Hub'),
    ('payslip', MIST, EVG, SEC, LIME, 'Every line of your payslip, explained.', "See what came off, and why. Nothing counts until you've checked it.", 'Payslip decoder'),
    ('words', NIGHT, MOON, NMUTED, LIME, 'Heard a word? Decode it.', 'ETFs, dividends, pips: in plain words, at three depths.', 'Words, in Learn'),
    ('feed', BLUSH, BLUSH_INK, BLUSH_2, LIME, 'Grow with women who get it.', 'Notes, letters and milestones, with your circles. No likes to chase.', 'Community'),
    ('stories', DEEP, MOON, NMUTED, LIME, 'Real stories. Real lessons.', 'Women who fell and rose, and the AWO Podcast.', 'Stories, in Learn'),
    ('shop', POOL, EVG, SEC, LIME, 'Your shop, in one link.', 'Show what you sell. Orders come straight to your WhatsApp.', 'Shop'),
]
FILES = {  # board: export file name
    **{f'R8-Store-{i + 1}': f'store-{i + 1}-{s[0]}.png' for i, s in enumerate(STORE8)},
    'R8-Feature-Graphic': 'feature-graphic-1024x500.png', 'R8-Hero-Device': 'device-hero.png',
    'R8-Ad-Diva': 'ad-square-diva.png', 'R8-Ad-Payslip': 'ad-square-payslip.png', 'R8-Ad-Goals': 'ad-square-goals.png', 'R8-Ad-Words': 'ad-square-words.png',
    'R8-Ad-Shop': 'ad-square-shop.png', 'R8-Ad-Explained': 'ad-square-explained.png', 'R8-Ad-Podcast': 'ad-story-podcast-1080x1920.png',
}


def shapes_row8(size, gap=12):
    """The five tab shapes, with the Hub's keystone in the centre."""
    items = [(EVG_D, LIME, 'pool'), (NIGHT, MOON, 'moon'), (LIME, EVG, 'hub'), (BLUSH, BLUSH_INK, 'ripple'), (POOL, EVG, 'stones')]
    return f'<span style="display: flex; gap: {gap}px">' + ''.join(
        f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {b}; display: flex; align-items: center; justify-content: center">'
        f'{hub_icon(None, round(size * .52), f, 2) if g == "hub" else icon(g, round(size * .5), f, 2)}</span>' for b, f, g in items) + '</span>'


def foot(col, accent, text, sub_col):
    return (f'<div style="position: absolute; left: 80px; right: 80px; bottom: 80px; display: flex; justify-content: space-between; align-items: flex-end">'
            f'<span style="font-size: 30px; line-height: 1.35; color: {sub_col}">{text}</span>{lockup(64, col, accent)}</div>')


# ---------------------------------------------------------------- store screenshots

def store(i):
    key, bg, head, sub, accent, title, text, alt = STORE8[i]
    dark = bg in (NIGHT, DEEP)
    mark_col = {EVG: '#FFFFFF', NIGHT: MOON, DEEP: MOON}.get(bg, head)
    inner = f'''<div style="position: absolute; left: 90px; right: 90px; top: 96px; display: flex; flex-direction: column; gap: 30px">
  {lockup(52, mark_col, accent)}
  <h1 style="{H(116, head, BAL)}">{title}</h1>
  <p style="font-size: 40px; line-height: 1.3; color: {sub}; max-width: 860px">{text}</p>
</div>
<div style="position: absolute; left: 198px; top: 760px">{device(CAPS8[key], 660, 'The ' + alt + ' screen', dark=dark)}</div>'''
    return canvas_board(f'Store screenshot {i + 1}', 1080, 1920, bg, inner)


# ---------------------------------------------------------------- listing

SHORT = 'Get your DIVA score, learn money in plain words and do the sums with free tools.'
FULL = [('', 'AWO is a free money-learning app for women in Southern Africa and the diaspora.'),
        DIVA_FULL,
        ('Learn what matters.', 'Short paths on pay, debt, saving together, investing, crypto and forex, with scam checks built in. Decode any money word you hear. Real stories from women who fell and rose, and the AWO Podcast.'),
        ('Tools that do the sums with you.', 'Decode your payslip, plan pay-day with family support included, see your debt-free date, price your work and send invoices. Goals of every kind, each with its own pool.'),
        ('Grow together.', 'A feed of notes, letters and milestones, circles for your goals, and shops run by members. No likes to chase.'),
        ('', 'AWO is for education. It does not give personal financial advice or sell financial products.')]
RULES8 = ['Icon 512 by 512, 32-bit PNG. Feature graphic 1024 by 500, with no transparency.',
          'Two to eight phone screenshots at 1080 by 1920 (9:16), 24-bit PNG.',
          'No ranking or promo words (best, top, new) and no install prompts on store graphics.',
          'Educational wording only. No company is named in ads. Numbers on screens are samples.',
          'The DIVA score always says what it is: readiness to learn, never a credit score.']
assert len(SHORT) <= 80, len(SHORT)


def listing():
    full_text = '\n\n'.join((h + ' ' + t).strip() for h, t in FULL)
    thumbs = ''.join(
        f'<div style="width: 118px; height: 212px; border-radius: 10px; background: {bg}; overflow: hidden; position: relative; flex-shrink: 0"><span style="position: absolute; left: 9px; top: 9px; right: 9px; {H(14, head)}">{title}</span>'
        f'<img src="{CAPS8[key]}" alt="" style="position: absolute; left: 16px; top: 70px; width: 86px; border-radius: 10px; box-shadow: 0 0 0 3px #0B0F0E, 0 0 0 4px #2E3A36"></div>'
        for key, bg, head, _s, _a, title, _t, _al in STORE8)
    feat_mini = (f'<div style="width: 512px; height: 250px; border-radius: 14px; background: {EVG}; position: relative; overflow: hidden; flex-shrink: 0">'
                 f'<div style="position: absolute; left: 28px; top: 28px; width: 250px; display: flex; flex-direction: column; gap: 12px">{lockup(22, "#FFFFFF", LIME)}<span style="{H(33, "#FFFFFF")}">Learn it. Plan it. Grow together.</span>{shapes_row8(24, 6)}</div>'
                 f'<div style="position: absolute; left: 300px; top: 22px; transform: rotate(-4deg)">{device(CAPS8["hub"], 110, "")}</div>'
                 f'<div style="position: absolute; left: 395px; top: 52px; transform: rotate(5deg)">{device(CAPS8["words"], 100, "", dark=True)}</div></div>')
    chips = ''.join(f'<span class="chip" style="height: 32px; font-size: 14px; background: {bg}; color: {fg}">{t}</span>' for t, bg, fg in [('Education', EVG, '#FFFFFF'), ('Free', '#FFFFFF', EVG), ('English at launch', '#FFFFFF', EVG)])
    full = ''.join(f'<p style="margin: 0">{"<strong style=" + chr(34) + "color: " + INK + chr(34) + ">" + h + "</strong> " if h else ""}{t}</p>' for h, t in FULL)
    rules = ''.join(f'<span style="display: flex; gap: 10px"><span style="color: {EVG}; display: flex; padding-top: 2px">{icon("check", 16, EVG, 2.6)}</span>{r}</span>' for r in RULES8)

    def counter(n, cap):
        return f'<span style="font-size: 13px; color: {MUTED}; font-variant-numeric: tabular-nums">{n} of {cap}</span>'
    inner = f'''<div style="position: absolute; inset: 64px; display: flex; gap: 56px">
  <div style="width: 540px; flex-shrink: 0; display: flex; flex-direction: column; gap: 20px">
    <div style="display: flex; align-items: center; gap: 22px">{app_icon(112)}<div style="display: flex; flex-direction: column; gap: 6px"><span style="{H(56, INK)}">AWO</span><span style="font-size: 19px; color: {SEC}">Money, understood.</span></div></div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap">{chips}</div>
    <div style="border-radius: 14px; background: #FFFFFF; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px">
      <span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">Short description</span>{counter(len(SHORT), 80)}</span>
      <span style="font-size: 18px; line-height: 1.4; font-weight: 500">{SHORT}</span></div>
    <div style="border-radius: 14px; background: #FFFFFF; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px">
      <span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">Full description</span>{counter(len(full_text), '4 000')}</span>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 15px; line-height: 1.5; color: {SEC}">{full}</div></div>
  </div>
  <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 18px; min-width: 0">
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Feature graphic</span>
    {feat_mini}
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Screenshots</span>
    <div style="display: flex; gap: 10px">{thumbs}</div>
    <div style="border-radius: 14px; background: #FFFFFF; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px; font-size: 15px; line-height: 1.45; color: {SEC}">
      <span style="font-size: 14px; font-weight: 600; color: {INK}">Store rules these drafts follow</span>{rules}
      <span style="font-size: 13px; color: {MUTED}">The copy is a sample until the name and store copy are settled (Q-31).</span></div>
  </div>
</div>'''
    return canvas_board('Store listing, Round 8 (our own layout)', 1720, 1080, MIST, inner)


# ---------------------------------------------------------------- feature graphic and device hero

def feature():
    inner = f'''<div style="position: absolute; left: 60px; top: 56px; width: 470px; display: flex; flex-direction: column; gap: 20px">
  {lockup(40, '#FFFFFF', LIME)}
  <h1 style="{H(64, '#FFFFFF', BAL)}">Learn it. Plan it. Grow together.</h1>
  <p style="font-size: 20px; line-height: 1.4; color: {ON_EVG}">Your DIVA score, money learning and tools for women, at home and abroad.</p>
  {shapes_row8(44, 10)}
</div>
<div style="position: absolute; left: 610px; top: 40px; transform: rotate(-4deg)">{device(CAPS8['hub'], 240, 'The Hub screen')}</div>
<div style="position: absolute; left: 800px; top: 100px; transform: rotate(5deg)">{device(CAPS8['words'], 220, 'The Words screen', dark=True)}</div>'''
    return canvas_board('Feature graphic, Round 8', 1024, 500, EVG, inner)


def hero():
    chips = ''.join(f'<span style="height: 40px; padding: 0 16px; border-radius: 8px; background: {bg}; color: {fg}; display: inline-flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600">{lead}{t}</span>'
                    for t, bg, fg, lead in [('Free', EVG, '#FFFFFF', ''), ('Education, not advice', '#FFFFFF', EVG, ''), ('Data stays in South Africa', '#FFFFFF', EVG, icon('lock', 16, EVG))])
    inner = f'''<div style="position: absolute; left: 80px; top: 110px; width: 560px; display: flex; flex-direction: column; gap: 28px">
  {lockup(44, EVG, LIME)}
  <h1 style="{H(112, INK, BAL)}">Money, understood.</h1>
  <p style="font-size: 24px; line-height: 1.45; color: {SEC}">Your DIVA score, money learning, tools that do the sums with you, and women who get it. At home and abroad.</p>
  <div style="display: flex; gap: 10px; flex-wrap: wrap">{chips}</div>
  {shapes_row8(48, 12)}
</div>
<img src="{IMG['naledi_table']}" alt="A woman working at her dining table with a laptop" style="position: absolute; left: 700px; top: 60px; width: 600px; height: 780px; object-fit: cover; object-position: 38% 50%; border-radius: 24px">
<div style="position: absolute; left: 1210px; top: 120px">{device(CAPS8['hub'], 300, 'The Hub screen')}</div>
<div style="position: absolute; left: 640px; top: 640px; border-radius: 24px; background: #FFFFFF; padding: 20px 26px 20px 20px; display: flex; align-items: center; gap: 16px; box-shadow: 0 20px 50px rgba(11,15,14,.16)">
  <span style="width: 52px; height: 52px; border-radius: 12px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{hub_icon(None, 28, EVG)}</span>
  <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600">Payslip decoded</span><span style="font-size: 15px; color: {MUTED}">R 14 090 comes home. Here's where R 4 410 went.</span></span></div>'''
    return canvas_board('Device hero, Round 8', 1600, 900, MIST, inner)


# ---------------------------------------------------------------- ads

def ad_diva():
    chips = ''.join(f'<span style="height: 64px; padding: 0 24px; border-radius: 16px; background: #FFFFFF; color: {EVG}; display: inline-flex; align-items: center; font-size: 30px; font-weight: 600">{t}</span>' for t in ('Not a credit score', 'Updates every 30 days'))
    inner = f'''<div style="position: absolute; left: 80px; top: 90px; width: 470px; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(104, EVG, BAL)}">What's your DIVA score?</h1>
  <p style="font-size: 34px; line-height: 1.3; color: {SEC}">A short check shows where your money life stands, in plain words.</p>
  <div style="display: flex; gap: 12px; flex-wrap: wrap">{chips}</div>
</div>
<div style="position: absolute; left: 600px; top: 60px">{device(CAPS8['me'], 400, 'The Me screen, with a sample DIVA profile')}</div>
<div style="position: absolute; left: 80px; bottom: 80px">{lockup(64, EVG, LIME)}</div>'''
    return canvas_board('Square ad, the DIVA score', 1080, 1080, POOL, inner)


def ad_payslip():
    chips = ''.join(f'<span style="height: 64px; padding: 0 24px; border-radius: 16px; background: #FFFFFF; color: {EVG}; display: inline-flex; align-items: center; font-size: 30px; font-weight: 600">{t}</span>' for t in ('PAYE', 'UIF', 'Pension'))
    inner = f'''<div style="position: absolute; left: 80px; top: 90px; width: 470px; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(104, EVG, BAL)}">What came off your payslip?</h1>
  <p style="font-size: 34px; line-height: 1.3; color: {SEC}">Every line, in plain words. Nothing counts until you check it.</p>
  <div style="display: flex; gap: 12px; flex-wrap: wrap">{chips}</div>
</div>
<div style="position: absolute; left: 600px; top: 60px">{device(CAPS8['payslip'], 400, 'The payslip decoder')}</div>
<div style="position: absolute; left: 80px; bottom: 80px">{lockup(64, EVG, LIME)}</div>'''
    return canvas_board('Square ad, payslip', 1080, 1080, POOL, inner)


def ad_goals():
    pools, ph = '', 380
    for k, (name, pct) in enumerate([('Safety net', 36), ('Moving out', 12), ('A trip home', 40)]):
        p = pool(200, ph, f'agp{k}', water=POOL, wave=LIME, vessel=EVG_D, rim=LIME, rimw=5, static=True, hole=f'agY{k}', label=f'agL{k}')
        p = p.replace('{{ agY' + str(k) + ' }}', str(round(ph * (1 - pct / 100)))).replace('{{ agL' + str(k) + ' }}', f'{name}, {pct}% full')
        pools += f'<div style="display: flex; flex-direction: column; align-items: center; gap: 18px">{p}<span style="font-size: 32px; font-weight: 600; color: #FFFFFF">{name}</span></div>'
    inner = f'''<div style="position: absolute; left: 80px; right: 80px; top: 80px; display: flex; flex-direction: column; gap: 24px">
  <h1 style="{H(120, LIME, BAL)}">Goals of every kind.</h1>
  <p style="font-size: 36px; line-height: 1.3; color: #FFFFFF">One pool each, filled at your pace.</p>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 424px; display: flex; justify-content: space-between">{pools}</div>
{foot('#FFFFFF', LIME, 'A free DIVA score, lessons<br>and tools for women.', ON_EVG)}'''
    return canvas_board('Square ad, goals', 1080, 1080, EVG, inner)


def ad_words():
    inner = f'''<div style="position: absolute; left: 190px; right: 190px; top: 80px; height: 700px; border-radius: 350px 350px {K}px {K}px; background: {LIME}; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 190px 60px 0; box-sizing: border-box; gap: 18px">
  <span style="font-size: 32px; font-weight: 600; color: {EVG}">Heard it at work?</span>
  <span style="{H(170, EVG)}">ETF</span>
  <span style="font-size: 32px; color: {EVG}">Exchange-traded fund</span>
  <p style="font-size: 36px; line-height: 1.3; color: {INK}; max-width: 560px">One thing you can buy that holds many shares at once, like a basket.</p>
</div>
{foot(MOON, LIME, 'Decode any money word<br>in Words, on AWO.', NMUTED)}'''
    return canvas_board('Square ad, words', 1080, 1080, NIGHT, inner)


def ad_shop():
    from biz8 import crop, PRODUCTS, ksh
    name, price, (x0, y0, side), _d, _stock = PRODUCTS[0]
    tile = (f'<div style="border-radius: {K}px; background: #FFFFFF; padding: 18px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 18px 44px rgba(107,43,64,.14)">'
            f'<span style="position: relative; display: block">{crop(x0, y0, side, 384, 212, 24, name)}'
            f'<span style="position: absolute; right: 12px; top: 12px; height: 40px; padding: 0 14px; border-radius: 12px; background: #FFFFFF; border: 2px dashed {BLUSH_INK}; color: {BLUSH_INK}; display: inline-flex; align-items: center; font-size: 20px; font-weight: 600">Sample</span></span>'
            f'<span style="display: flex; flex-direction: column; gap: 4px; padding: 0 4px"><span style="font-size: 26px; font-weight: 600; color: {INK}">{name}</span>'
            f'<span style="font-size: 24px; color: {SEC}; font-variant-numeric: tabular-nums">{ksh(price)}</span></span>'
            f'<span style="height: 64px; border-radius: 16px; background: {EVG}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; gap: 12px; font-size: 24px; font-weight: 600">{ic8("whatsapp", 26, "#FFFFFF")}Order on WhatsApp</span></div>')
    inner = f'''<h1 style="position: absolute; left: 80px; right: 80px; top: 80px; margin: 0; {H(104, BLUSH_INK, BAL)}">Shop local, from women on AWO.</h1>
<img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her stall" style="position: absolute; left: 80px; top: 330px; width: 460px; height: 540px; object-fit: cover; object-position: 55% 36%; border-radius: {K}px">
<div style="position: absolute; left: 580px; right: 80px; top: 330px; height: 540px; display: flex; flex-direction: column; justify-content: space-between">
  <p style="margin: 0; font-size: 30px; line-height: 1.35; color: {BLUSH_2}">A catalogue and a link. Orders go straight to her WhatsApp.</p>
  {tile}
</div>
{foot(BLUSH_INK, '#FFFFFF', 'Wanjiru, a market stall<br>in Nairobi.', BLUSH_2)}'''
    return canvas_board('Square ad, shop local', 1080, 1080, BLUSH, inner)


def ad_explained():
    inner = f'''<div style="position: absolute; left: 80px; top: 90px; width: 500px; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(100, MOON)}">Shares, explained.<br>Never sold.</h1>
  <p style="font-size: 34px; line-height: 1.3; color: {NMUTED}">Investing, crypto and forex in plain words. AWO never tells you what to buy.</p>
</div>
<div style="position: absolute; left: 600px; top: 60px">{device(CAPS8['topic'], 400, 'The Shares and dividends topic', dark=True)}</div>
<div style="position: absolute; left: 80px; bottom: 80px">{lockup(64, MOON, LIME)}</div>'''
    return canvas_board('Square ad, explained', 1080, 1080, DEEP, inner)


def ad_podcast():
    inner = f'''<img src="{IMG['amara_coat']}" alt="Amara, the episode's guest" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1100px; object-fit: cover; object-position: 55% 25%">
<span style="position: absolute; left: 80px; top: 80px; height: 64px; padding: 0 26px; border-radius: 16px; background: {LIME}; color: {EVG}; display: inline-flex; align-items: center; font-size: 30px; font-weight: 600">The AWO Podcast</span>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 900px; border-radius: {K}px {K}px 0 0; background: {NIGHT}; padding: 90px 90px 100px; box-sizing: border-box; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(96, MOON, BAL)}">Closing a shop, and opening a better one.</h1>
  <span class="hand" style="font-size: 72px; color: {LIME}; {HF}">Every month open cost more. So I stopped.</span>
  <span style="font-size: 30px; color: {NMUTED}">Episode 12, with Amara. A sample guest, in her own words.</span>
  <div style="flex-grow: 1"></div>
  <div style="display: flex; justify-content: space-between; align-items: flex-end">
    <span style="display: flex; align-items: center; gap: 22px"><span style="width: 96px; height: 96px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('play', 40, INK)}</span><span style="font-size: 30px; line-height: 1.35; color: {MOON}">Listen in Learn,<br>even offline.</span></span>
    {lockup(72, MOON, LIME)}
  </div>
</div>'''
    return hand_hole(canvas_board('Story ad, the podcast', 1080, 1920, NIGHT, inner))


BOARDS = ([(f'R8-Store-{i + 1}', (lambda i=i: store(i))) for i in range(len(STORE8))]
          + [('R8-Listing', listing), ('R8-Feature-Graphic', feature), ('R8-Hero-Device', hero),
             ('R8-Ad-Diva', ad_diva), ('R8-Ad-Payslip', ad_payslip), ('R8-Ad-Goals', ad_goals), ('R8-Ad-Words', ad_words),
             ('R8-Ad-Shop', ad_shop), ('R8-Ad-Explained', ad_explained), ('R8-Ad-Podcast', ad_podcast)])


if __name__ == '__main__' and sys.argv[1:] == ['specs']:
    print(json.dumps(capture_specs(), indent=1))
