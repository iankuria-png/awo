"""Round 7 marketing (T-076, D-033): built from 2x captures of the Round 7 screens, in Geist, with the
stepping-stones lockup and app icon A. Corners scale with the canvas: 14 at phone width (390) becomes
40 on a 1080 canvas. The hand appears only for a member's own words.

When a screen changes: recapture it (plan-caps.json in the scratchpad recipe), upload it, update CAPS."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from marketing import canvas_board, device  # noqa: E402
from brand7 import app_icon, lockup  # noqa: E402
from screens7 import mark, IMG as IMG7  # noqa: E402,F401

CAPS = {
    'home': '/_blob/1fa941cd9884f3e7fea1cd149714b9b1', 'me': '/_blob/a7f8f6fb1c6620cef498333d9227ca99',
    'learn': '/_blob/8bd5266de4987a831537092e31a8d092', 'vault': '/_blob/881e12c7cdfaa26b1436a7214d97fcd1',
    'community': '/_blob/aeb8d7a97b251926e044f716c8b216b2', 'ask': '/_blob/ce70f314055c11df2410b014a7b8bc49',
    'entry': '/_blob/1c34be39cae7eae7ebaa0e16cd349250', 'progress': '/_blob/72bf6db1e05d62b0926afc1377fbd8fa',
    'checkin': '/_blob/455aefd5bdabfa8a10b11eeff60b7eba',
}
HF = "font-family: '[[ handFont ]]', cursive"
K = 40  # the 14px corner, at 1080 wide


def H(size, col, extra=''):
    """A Geist display headline at marketing size."""
    return f'font-size: {size}px; font-weight: 600; letter-spacing: -0.05em; line-height: .95; color: {col}; {extra}'


STORE = [
    ('me', POOL, EVG, SEC, LIME, 'Know your DIVA score.', 'Where your money life stands, in plain words. For learning, never a credit score.', 'Your DIVA profile'),
    ('home', EVG, LIME, ON_EVG, LIME, 'One small step a week.', 'One clear thing to do each week, sized to your life.', 'Home'),
    ('learn', NIGHT, MOON, NMUTED, LIME, 'Learn money in three minutes.', "Short lessons told through real women's stories.", 'Learn'),
    ('vault', LIME, EVG, INK, '#FFFFFF', 'Money words, made clear.', 'Keep the words you learn, and practise them in two minutes.', 'The Vault'),
    ('community', BLUSH, BLUSH_INK, BLUSH_2, LIME, 'Grow with women who get it.', 'Circles, cheers and honest questions. First names only.', 'Community'),
    ('ask', DEEP, MOON, NMUTED, LIME, 'Ask anything. Get plain answers.', 'Ola explains and teaches. It never tells you what to buy.', 'Ask Ola'),
    ('progress', MIST, EVG, SEC, LIME, 'See how far you have come.', 'Check in every 30 days and your DIVA score updates. Old versions never change.', 'Your progress'),
    ('checkin', POOL, EVG, SEC, LIME, 'Watch your safety net fill.', 'Three questions every 30 days update your DIVA score. Honest answers, never shared.', 'The 30-day check-in'),
]
BAL = 'text-wrap: balance'  # no one-word last lines in headlines
# The DIVA score in marketing: always with what it is for, and never next to credit, loans or eligibility.
FEATURE_HEAD = 'Know your DIVA score. Grow from there.'
DIVA_FULL = ('Know your DIVA score.', 'A short check gives you your DIVA score: where your money life stands today across four areas, in plain words, '
             'and the one step that would help most. It shows readiness to learn and act, and it is not a credit score. '
             'Each 30-day check-in adds a new version; old ones never change.')
PHOTO_TOGETHER = '/_blob/de99957f2ba63a4f30e2cf6bda586b39'  # two women laughing (nappy.co), used on Round 3's store screenshot


def hand_hole(html):
    return html.replace('[[ handFont ]]', '{{ handFont }}')


def store(i):
    key, bg, head, sub, accent, title, text, alt = STORE[i]
    dark = bg in (NIGHT, DEEP)
    mark_col = {EVG: '#FFFFFF', NIGHT: MOON, DEEP: MOON}.get(bg, head)
    extra = pre = ''
    dev_left, dev_w = 198, 660
    if key == 'community':
        dev_left, dev_w = 470, 560
        pre = f'<img src="{PHOTO_TOGETHER}" alt="Two women laughing together" style="position: absolute; left: 60px; top: 820px; width: 450px; height: 720px; object-fit: cover; object-position: 30% 40%; border-radius: {K}px">'
        extra = (f'<div style="position: absolute; left: 50px; top: 1440px; z-index: 2; max-width: 360px; padding: 26px 32px; border-radius: {K}px {K // 3}px {K}px {K}px; '
                 f'background: {BLUSH_INK}; color: {BLUSH}; box-shadow: 0 24px 60px rgba(42,15,24,.3); transform: rotate(-3deg)">'
                 f'<span class="hand" style="font-size: 50px; {HF}">Takeaway on Friday. Cooked instead, and it was nicer.</span></div>')
    inner = f'''<div style="position: absolute; left: 90px; right: 90px; top: 96px; display: flex; flex-direction: column; gap: 30px">
  {lockup(52, mark_col, accent)}
  <h1 style="{H(124, head, BAL)}">{title}</h1>
  <p style="font-size: 40px; line-height: 1.3; color: {sub}; max-width: 860px; text-wrap: balance">{text}</p>
</div>
{pre}
<div style="position: absolute; left: {dev_left}px; top: 740px">{device(CAPS[key], dev_w, 'The ' + alt + ' screen', dark=dark)}</div>
{extra}'''
    return hand_hole(canvas_board(f'Store screenshot {i + 1}', 1080, 1920, bg, inner))


def shapes_row(size, gap=12):
    items = [(EVG_D, LIME, 'pool'), (NIGHT, MOON, 'moon'), (LIME, EVG, 'arch'), (BLUSH, BLUSH_INK, 'ripple'), (POOL, EVG, 'stones')]
    return f'<span style="display: flex; gap: {gap}px">' + ''.join(
        f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {b}; display: flex; align-items: center; justify-content: center">{icon(ic, round(size * .5), f, 2)}</span>' for b, f, ic in items) + '</span>'


def feature():
    inner = f'''<div style="position: absolute; left: 60px; top: 56px; width: 500px; display: flex; flex-direction: column; gap: 20px">
  {lockup(40, '#FFFFFF', LIME)}
  <h1 style="{H(66, '#FFFFFF', BAL)}">{FEATURE_HEAD}</h1>
  <p style="font-size: 20px; line-height: 1.4; color: {ON_EVG}">Free money learning for women, at home and abroad.</p>
  {shapes_row(44, 10)}
</div>
<div style="position: absolute; left: 640px; top: 46px; transform: rotate(-4deg)">{device(CAPS['home'], 250, 'The Home screen')}</div>
<div style="position: absolute; left: 820px; top: 110px; transform: rotate(5deg)">{device(CAPS['learn'], 230, 'The Learn screen', dark=True)}</div>'''
    return canvas_board('Feature graphic', 1024, 500, EVG, inner)


def icon512():
    inner = app_icon(512, 'square').replace(f'border-radius: {round(512 * .22)}px', 'border-radius: 0')
    return canvas_board('App icon A (512)', 512, 512, EVG, inner)


def hero():
    chips = ''.join(f'<span style="height: 40px; padding: 0 16px; border-radius: 8px; background: {bg}; color: {fg}; display: inline-flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600">{lead}{t}</span>'
                    for t, bg, fg, lead in [('Free', EVG, '#FFFFFF', ''), ('Education, not advice', '#FFFFFF', EVG, ''), ('Data stays in South Africa', '#FFFFFF', EVG, icon('lock', 16, EVG))])
    inner = f'''<div style="position: absolute; left: 80px; top: 110px; width: 540px; display: flex; flex-direction: column; gap: 28px">
  {lockup(44, EVG, LIME)}
  <h1 style="{H(112, INK)}">Money, understood.</h1>
  <p style="font-size: 24px; line-height: 1.45; color: {SEC}">Your DIVA score, money learning and insight for women building their financial lives, at home and abroad.</p>
  <div style="display: flex; gap: 10px; flex-wrap: wrap">{chips}</div>
</div>
<img src="{IMG['naledi_table']}" alt="A woman working at her dining table with a laptop" style="position: absolute; left: 680px; top: 60px; width: 620px; height: 780px; object-fit: cover; object-position: 38% 50%; border-radius: 24px">
<div style="position: absolute; left: 1200px; top: 140px">{device(CAPS['home'], 300, 'The Home screen')}</div>
<div style="position: absolute; left: 640px; top: 620px; border-radius: 24px; background: #FFFFFF; padding: 20px 24px; display: flex; align-items: center; gap: 16px; box-shadow: 0 20px 50px rgba(11,15,14,.16)">
  <span style="width: 44px; height: 44px; border-radius: 10px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 24, EVG, 2.8)}</span>
  <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600">Check-in done</span><span style="font-size: 15px; color: {MUTED}">Your DIVA score has a new version</span></span></div>'''
    return canvas_board('Device hero', 1600, 900, MIST, inner)


SHORT = 'Get your DIVA score, learn money in plain words and grow with women who get it.'
FULL = [('', 'AWO is a free money-learning app for women in Southern Africa and the diaspora.'),
        DIVA_FULL,
        ('Learn a little every day.', 'Three-minute lessons, a Vault of money words, and Ola, a guide who explains without judging.'),
        ('Take one step at a time.', 'One clear step each week, and a safety net that fills as you go.'),
        ('Grow together.', 'Share wins, ask questions and find your circle, from stokvels to side hustles.'),
        ('', 'AWO is for education. It does not give personal financial advice.')]
assert len(SHORT) <= 80, len(SHORT)
RULES = ['Icon 512 by 512, 32-bit PNG. Feature graphic 1024 by 500, with no transparency.',
         'Two to eight phone screenshots at 1080 by 1920 (9:16), 24-bit PNG.',
         'No ranking or promo words (best, top, new) and no install prompts on store graphics.',
         'Educational wording only. Numbers on screens are samples.',
         'The DIVA score always says what it is: readiness to learn, never a credit score.']


def listing():
    full_text = '\n\n'.join((h + ' ' + t).strip() for h, t in FULL)
    thumbs = ''.join(
        f'<div style="width: 118px; height: 212px; border-radius: 10px; background: {bg}; overflow: hidden; position: relative; flex-shrink: 0"><span style="position: absolute; left: 9px; top: 9px; right: 9px; {H(14, head)}">{title}</span>'
        f'<img src="{CAPS[key]}" alt="" style="position: absolute; left: 16px; top: 64px; width: 86px; border-radius: 10px; box-shadow: 0 0 0 3px #0B0F0E, 0 0 0 4px #2E3A36"></div>'
        for key, bg, head, _s, _a, title, _t, _al in STORE)
    feat_mini = f'''<div style="width: 512px; height: 250px; border-radius: 14px; background: {EVG}; position: relative; overflow: hidden; flex-shrink: 0"><div style="position: absolute; left: 28px; top: 28px; width: 260px; display: flex; flex-direction: column; gap: 12px">{lockup(22, '#FFFFFF', LIME)}<span style="{H(34, '#FFFFFF', BAL)}">{FEATURE_HEAD}</span>{shapes_row(24, 6)}</div><div style="position: absolute; left: 318px; top: 24px; transform: rotate(-4deg)">{device(CAPS['home'], 130, '')}</div></div>'''
    chips = ''.join(f'<span class="chip" style="height: 32px; font-size: 14px; background: {bg}; color: {fg}">{t}</span>' for t, bg, fg in [('Education', EVG, '#FFFFFF'), ('Free', '#FFFFFF', EVG), ('English at launch', '#FFFFFF', EVG)])
    strong = lambda h: f'<strong style="color: {INK}">{h}</strong> ' if h else ''
    full = ''.join(f'<p style="margin: 0">{strong(h)}{t}</p>' for h, t in FULL)
    rules = ''.join(f'<span style="display: flex; gap: 10px"><span style="color: {EVG}; display: flex; padding-top: 2px">{icon("check", 16, EVG, 2.6)}</span>{r}</span>' for r in RULES)
    counter = lambda n, cap: f'<span style="font-size: 13px; color: {MUTED}; font-variant-numeric: tabular-nums">{n} of {cap}</span>'
    inner = f'''<div style="position: absolute; inset: 64px; display: flex; gap: 56px">
  <div style="width: 520px; flex-shrink: 0; display: flex; flex-direction: column; gap: 20px">
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
      <span style="font-size: 14px; font-weight: 600; color: {INK}">Store rules these drafts follow</span>{rules}</div>
  </div>
</div>'''
    return canvas_board('Store listing (our own layout)', 1720, 1000, MIST, inner)


def ad_diva():
    """The DIVA score as a sample result: the score, the stage on the stones, a strength and a focus."""
    pts = [(56, 150, 46, 17), (186, 110, 52, 19), (318, 70, 52, 19), (440, 32, 42, 16)]
    dash = ' stroke-dasharray="8 8"'
    stones = ''.join(
        f'<ellipse cx="{x}" cy="{y + 9}" rx="{rx}" ry="{ry}" fill="{"#BFD9D2" if i < 2 else "none"}"></ellipse>'
        f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{[EVG, LIME, "none", "none"][i]}" stroke="{EVG}" stroke-width="3.5"{dash if i > 1 else ""}></ellipse>'
        for i, (x, y, rx, ry) in enumerate(pts))
    tile = lambda bg, k, v: (f'<div style="flex: 1; border-radius: {K // 2}px; background: {bg}; padding: 22px 26px; display: flex; flex-direction: column; gap: 8px">'
                             f'<span style="font-size: 24px; color: {SEC}">{k}</span><span style="font-size: 32px; font-weight: 600; color: {EVG}">{v}</span></div>')
    inner = f'''<h1 style="position: absolute; left: 80px; right: 80px; top: 70px; margin: 0; {H(112, EVG, BAL)}">What's your DIVA score?</h1>
<div style="position: absolute; left: 80px; right: 80px; top: 330px; height: 500px; box-sizing: border-box; border-radius: {K}px; background: #FFFFFF; padding: 40px 44px; display: flex; flex-direction: column; gap: 30px; box-shadow: 0 24px 60px rgba(15,74,54,.12)">
  <span style="position: absolute; right: 36px; top: 250px; height: 44px; padding: 0 16px; border-radius: 10px; border: 2px dashed {EVG}; color: {EVG}; display: inline-flex; align-items: center; font-size: 22px; font-weight: 600">Sample</span>
  <div style="display: flex; gap: 44px; align-items: center">
    <div role="img" aria-label="DIVA score 63 of 100" style="position: relative; width: 250px; height: 250px; flex-shrink: 0">{arc(250, 63, '#D3E8E4', EVG, sw=22)}
      <span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; padding-top: 6px"><span style="{H(96, EVG)}">63</span><span style="font-size: 22px; color: {SEC}">DIVA score</span></span></div>
    <div style="display: flex; flex-direction: column; gap: 18px">
      <span style="{H(76, EVG)}">Stage 2 of 4</span>
      <svg role="img" aria-label="Four stepping stones. You are on stage 2." width="490" height="180" viewBox="0 0 490 180" style="display: block; overflow: visible">{stones}</svg>
    </div>
  </div>
  <div style="display: flex; gap: 16px">{tile(MIST, 'Your strength', 'Everyday money')}{tile(LIME, 'Your focus', 'Ready for surprises')}</div>
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 70px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 30px; line-height: 1.35; color: {EVG}">Readiness to learn,<br>never a credit score.</span>{lockup(64, EVG, LIME)}</div>'''
    return canvas_board('Square ad, the DIVA score', 1080, 1080, POOL, inner)


def ad_photo():
    inner = f'''<div style="position: absolute; left: 80px; top: 90px; width: 500px; display: flex; flex-direction: column; gap: 28px">
  <h1 style="{H(108, BLUSH_INK)}">Talk money. Grow together.</h1>
  <p style="font-size: 36px; line-height: 1.3; color: {BLUSH_2}">Circles of women on the same step. First names only.</p>
</div>
<img src="{IMG7['phone_smile']}" alt="A woman laughing on a phone call" style="position: absolute; left: 620px; top: 90px; width: 380px; height: 740px; object-fit: cover; object-position: 50% 20%; border-radius: {K}px">
<div style="position: absolute; left: 540px; top: 700px; height: 96px; padding: 0 30px 0 18px; border-radius: 24px; background: #FFFFFF; display: flex; align-items: center; gap: 16px; box-shadow: 0 20px 50px rgba(42,15,24,.2); font-size: 32px; font-weight: 600; color: {INK}"><span style="width: 60px; height: 60px; border-radius: 14px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 32, EVG, 2.8)}</span>Lesson done</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 80px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 30px; line-height: 1.35; color: {BLUSH_INK}">Your free DIVA score<br>and money learning.</span>{lockup(64, BLUSH_INK, '#FFFFFF')}</div>'''
    return canvas_board('Square ad, photo-led', 1080, 1080, BLUSH, inner)


def ad_pool():
    p = pool(300, 760, 'adPool', water=POOL, wave=LIME, vessel=EVG_D, rim=LIME, rimw=6, static=True, hole='adY', label='adLabel')
    p = p.replace('{{ adY }}', str(round(760 * (1 - 0.36)))).replace('{{ adLabel }}', 'A safety net pool, just over a third full')
    inner = f'''<div style="position: absolute; left: 90px; top: 160px">{p}</div>
<div style="position: absolute; left: 470px; right: 80px; top: 160px; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(168, LIME)}">R 100 at a time.</h1>
  <p style="font-size: 42px; line-height: 1.3; color: #FFFFFF">Build a safety net that fits your life.</p>
</div>
<div style="position: absolute; left: 470px; right: 80px; bottom: 90px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 28px; line-height: 1.35; color: {ON_EVG}">Your free DIVA score<br>and money learning.</span>{lockup(64, '#FFFFFF', LIME)}</div>'''
    return canvas_board('Square ad, the pool', 1080, 1080, EVG, inner)


def ad_word():
    inner = f'''<div style="position: absolute; left: 190px; right: 190px; top: 80px; height: 700px; border-radius: 350px 350px {K}px {K}px; background: {LIME}; box-shadow: inset 0 0 0 4px {EVG}; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 200px 60px 0; box-sizing: border-box; gap: 18px">
  <span style="font-size: 32px; font-weight: 600; color: {EVG}">Word of the week</span>
  <span style="{H(150, EVG)}">Stokvel</span>
  <span style="font-size: 32px; color: {EVG}">Say it: stok-fel</span>
  <p style="font-size: 36px; line-height: 1.3; color: {INK}; max-width: 560px">A savings group that takes turns with the pot.</p>
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 80px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 34px; font-weight: 600; color: {EVG}">Learn a money word a week.</span>{lockup(64, EVG, LIME)}</div>'''
    return canvas_board('Square ad, word of the week', 1080, 1080, MIST, inner)


def ad_story():
    inner = f'''<img src="{IMG['amara_coat']}" alt="Amara outdoors in a winter coat" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1180px; object-fit: cover; object-position: 60% 35%">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 840px; border-radius: {K}px {K}px 0 0; background: {EVG}; padding: 90px 90px 110px; box-sizing: border-box; display: flex; flex-direction: column; gap: 30px">
  <span class="hand" style="font-size: 92px; color: #FFFFFF; {HF}">My safety net went down this month. It did its job.</span>
  <span style="font-size: 32px; color: {ON_EVG}">Amara, a nurse in London. Sample story, in her own words.</span>
  <div style="flex-grow: 1"></div>
  <div style="display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 34px; line-height: 1.35; color: #FFFFFF">Money, understood,<br>with women who get it.</span>{lockup(72, '#FFFFFF', LIME)}</div>
</div>'''
    return hand_hole(canvas_board('Story ad', 1080, 1920, EVG, inner))


BOARDS = ([(f'R7-Store-{i + 1}', (lambda i=i: store(i))) for i in range(len(STORE))]
          + [('R7-Listing', listing), ('R7-Feature-Graphic', feature), ('R7-App-Icon', icon512), ('R7-Hero-Device', hero),
             ('R7-Ad-Diva', ad_diva), ('R7-Ad-Photo', ad_photo), ('R7-Ad-Pool', ad_pool), ('R7-Ad-Word', ad_word), ('R7-Ad-Story', ad_story)])
