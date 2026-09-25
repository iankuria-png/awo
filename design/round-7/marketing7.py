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
    'home': '/_blob/dea500386add2ea29edf312af1e533bd', 'me': '/_blob/98d12ef16b46f90e2fc1a134473e53bc',
    'learn': '/_blob/8bd5266de4987a831537092e31a8d092', 'vault': '/_blob/69e8bf7aa50a34e03d095eec025e1a74',
    'community': '/_blob/f45732525d9585201e36b728432660d6', 'ask': '/_blob/ce70f314055c11df2410b014a7b8bc49',
    'entry': '/_blob/1c34be39cae7eae7ebaa0e16cd349250', 'progress': '/_blob/cc1d7acdf4f9659cf52d325ec96d2659',
    'checkin': '/_blob/455aefd5bdabfa8a10b11eeff60b7eba',
}
HF = "font-family: '[[ handFont ]]', cursive"
K = 40  # the 14px corner, at 1080 wide


def H(size, col, extra=''):
    """A Geist display headline at marketing size."""
    return f'font-size: {size}px; font-weight: 600; letter-spacing: -0.05em; line-height: .95; color: {col}; {extra}'


STORE = [
    ('me', POOL, EVG, SEC, LIME, 'Know where you stand.', 'A clear picture of your money life, in plain words. Not a credit score.', 'Your DIVA profile'),
    ('home', EVG, LIME, ON_EVG, LIME, 'One small step a week.', 'Watch your safety net fill as you go.', 'Home'),
    ('learn', NIGHT, MOON, NMUTED, LIME, 'Learn money in three minutes.', "Short lessons told through real women's stories.", 'Learn'),
    ('vault', LIME, EVG, INK, '#FFFFFF', 'Money words, made clear.', 'Keep the words you learn, and practise them in two minutes.', 'The Vault'),
    ('community', BLUSH, BLUSH_INK, BLUSH_2, LIME, 'Grow with women who get it.', 'Circles, cheers and honest questions. First names only.', 'Community'),
    ('ask', DEEP, MOON, NMUTED, LIME, 'Ask anything. Get plain answers.', 'Ola explains and teaches. It never tells you what to buy.', 'Ask Ola'),
    ('progress', MIST, EVG, SEC, LIME, 'See how far you have come.', 'Check in every 30 days. Each check-in adds a version; old ones never change.', 'Your progress'),
]


def hand_hole(html):
    return html.replace('[[ handFont ]]', '{{ handFont }}')


def store(i):
    key, bg, head, sub, accent, title, text, alt = STORE[i]
    dark = bg in (NIGHT, DEEP)
    mark_col = {EVG: '#FFFFFF', NIGHT: MOON, DEEP: MOON}.get(bg, head)
    extra = ''
    if key == 'community':
        extra = (f'<div style="position: absolute; right: 70px; top: 1180px; z-index: 2; max-width: 360px; padding: 26px 32px; border-radius: {K}px {K // 3}px {K}px {K}px; '
                 f'background: {BLUSH_INK}; color: {BLUSH}; box-shadow: 0 24px 60px rgba(42,15,24,.3); transform: rotate(-3deg)">'
                 f'<span class="hand" style="font-size: 50px; {HF}">Takeaway on Friday. Cooked instead, and it was nicer.</span></div>')
    inner = f'''<div style="position: absolute; left: 90px; right: 90px; top: 96px; display: flex; flex-direction: column; gap: 30px">
  {lockup(52, mark_col, accent)}
  <h1 style="{H(124, head)}">{title}</h1>
  <p style="font-size: 40px; line-height: 1.3; color: {sub}; max-width: 860px">{text}</p>
</div>
<div style="position: absolute; left: 198px; top: 740px">{device(CAPS[key], 660, 'The ' + alt + ' screen', dark=dark)}</div>
{extra}'''
    return hand_hole(canvas_board(f'Store screenshot {i + 1}', 1080, 1920, bg, inner))


def shapes_row(size, gap=12):
    items = [(EVG_D, LIME, 'pool'), (NIGHT, MOON, 'moon'), (LIME, EVG, 'arch'), (BLUSH, BLUSH_INK, 'ripple'), (POOL, EVG, 'stones')]
    return f'<span style="display: flex; gap: {gap}px">' + ''.join(
        f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {b}; display: flex; align-items: center; justify-content: center">{icon(ic, round(size * .5), f, 2)}</span>' for b, f, ic in items) + '</span>'


def feature():
    inner = f'''<div style="position: absolute; left: 60px; top: 56px; width: 500px; display: flex; flex-direction: column; gap: 20px">
  {lockup(40, '#FFFFFF', LIME)}
  <h1 style="{H(66, '#FFFFFF')}">Know where you stand. Grow from there.</h1>
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
  <p style="font-size: 24px; line-height: 1.45; color: {SEC}">Free money learning and insight for women building their financial lives, at home and abroad.</p>
  <div style="display: flex; gap: 10px; flex-wrap: wrap">{chips}</div>
</div>
<img src="{IMG['naledi_table']}" alt="A woman working at her dining table with a laptop" style="position: absolute; left: 680px; top: 60px; width: 620px; height: 780px; object-fit: cover; object-position: 38% 50%; border-radius: 24px">
<div style="position: absolute; left: 1200px; top: 140px">{device(CAPS['home'], 300, 'The Home screen')}</div>
<div style="position: absolute; left: 640px; top: 620px; border-radius: 24px; background: #FFFFFF; padding: 20px 24px; display: flex; align-items: center; gap: 16px; box-shadow: 0 20px 50px rgba(11,15,14,.16)">
  <span style="width: 44px; height: 44px; border-radius: 10px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 24, EVG, 2.8)}</span>
  <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600">Check-in done</span><span style="font-size: 15px; color: {MUTED}">Your profile has a new version</span></span></div>'''
    return canvas_board('Device hero', 1600, 900, MIST, inner)


def listing():
    thumbs = ''.join(
        f'<div style="width: 150px; height: 272px; border-radius: 12px; background: {bg}; overflow: hidden; position: relative; flex-shrink: 0"><span style="position: absolute; left: 12px; top: 12px; right: 12px; {H(19, head)}">{title}</span>'
        f'<img src="{CAPS[key]}" alt="" style="position: absolute; left: 20px; top: 82px; width: 110px; border-radius: 12px; box-shadow: 0 0 0 4px #0B0F0E, 0 0 0 5px #2E3A36"></div>'
        for key, bg, head, _s, _a, title, _t, _al in STORE)
    feat_mini = f'''<div style="width: 512px; height: 250px; border-radius: 14px; background: {EVG}; position: relative; overflow: hidden; flex-shrink: 0"><div style="position: absolute; left: 28px; top: 28px; width: 260px; display: flex; flex-direction: column; gap: 12px">{lockup(22, '#FFFFFF', LIME)}<span style="{H(34, '#FFFFFF')}">Know where you stand. Grow from there.</span>{shapes_row(24, 6)}</div><div style="position: absolute; left: 318px; top: 24px; transform: rotate(-4deg)">{device(CAPS['home'], 130, '')}</div></div>'''
    chips = ''.join(f'<span class="chip" style="height: 32px; font-size: 14px; background: {bg}; color: {fg}">{t}</span>' for t, bg, fg in [('Free', EVG, '#FFFFFF'), ('Education', '#FFFFFF', EVG), ('English at launch', '#FFFFFF', EVG)])
    inner = f'''<div style="position: absolute; inset: 64px; display: flex; gap: 64px">
  <div style="width: 480px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px">
    <div style="display: flex; align-items: center; gap: 22px">{app_icon(128)}<div style="display: flex; flex-direction: column; gap: 6px"><span style="{H(64, INK)}">AWO</span><span style="font-size: 20px; color: {SEC}">Money, understood.</span></div></div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap">{chips}</div>
    <p style="font-size: 22px; line-height: 1.4; font-weight: 600">Money learning and insight for African women, at home and abroad.</p>
    <div style="display: flex; flex-direction: column; gap: 14px; font-size: 17px; line-height: 1.5; color: {SEC}">
      <span><strong style="color: {INK}">Know where you stand.</strong> A DIVA profile in plain words, with a new version after every check-in.</span>
      <span><strong style="color: {INK}">One small step a week,</strong> and a safety net that fills as you go.</span>
      <span><strong style="color: {INK}">Three-minute lessons,</strong> a vault of money words and circles of women who get it.</span>
      <span><strong style="color: {INK}">Ask Ola</strong> to explain a result, a word or an offer. It teaches; it never tells you what to buy.</span>
    </div>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 15px; color: {SEC}">{icon('lock', 18, EVG)}Your data is stored in South Africa.</span>
  </div>
  <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 24px; min-width: 0">
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Feature graphic</span>
    {feat_mini}
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Screenshots</span>
    <div style="display: flex; gap: 12px">{thumbs}</div>
  </div>
</div>'''
    return canvas_board('Store listing (our own layout)', 1720, 820, MIST, inner)


def ad_photo():
    inner = f'''<div style="position: absolute; left: 80px; top: 90px; width: 500px; display: flex; flex-direction: column; gap: 28px">
  <h1 style="{H(108, BLUSH_INK)}">Talk money. Grow together.</h1>
  <p style="font-size: 36px; line-height: 1.3; color: {BLUSH_2}">Circles of women on the same step. First names only.</p>
</div>
<img src="{IMG7['phone_smile']}" alt="A woman laughing on a phone call" style="position: absolute; left: 620px; top: 90px; width: 380px; height: 740px; object-fit: cover; object-position: 50% 20%; border-radius: {K}px">
<div style="position: absolute; left: 540px; top: 700px; height: 96px; padding: 0 30px 0 18px; border-radius: 24px; background: #FFFFFF; display: flex; align-items: center; gap: 16px; box-shadow: 0 20px 50px rgba(42,15,24,.2); font-size: 32px; font-weight: 600; color: {INK}"><span style="width: 60px; height: 60px; border-radius: 14px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 32, EVG, 2.8)}</span>Lesson done</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 80px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 30px; line-height: 1.35; color: {BLUSH_INK}">Free money learning<br>for women.</span>{lockup(64, BLUSH_INK, '#FFFFFF')}</div>'''
    return canvas_board('Square ad, photo-led', 1080, 1080, BLUSH, inner)


def ad_pool():
    p = pool(300, 760, 'adPool', water=POOL, wave=LIME, vessel=EVG_D, rim=LIME, rimw=6, static=True, hole='adY', label='adLabel')
    p = p.replace('{{ adY }}', str(round(760 * (1 - 0.36)))).replace('{{ adLabel }}', 'A safety net pool, just over a third full')
    inner = f'''<div style="position: absolute; left: 90px; top: 160px">{p}</div>
<div style="position: absolute; left: 470px; right: 80px; top: 160px; display: flex; flex-direction: column; gap: 30px">
  <h1 style="{H(168, LIME)}">R 100 at a time.</h1>
  <p style="font-size: 42px; line-height: 1.3; color: #FFFFFF">Build a safety net that fits your life.</p>
</div>
<div style="position: absolute; left: 470px; right: 80px; bottom: 90px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 28px; line-height: 1.35; color: {ON_EVG}">Free money learning<br>for women.</span>{lockup(64, '#FFFFFF', LIME)}</div>'''
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
             ('R7-Ad-Photo', ad_photo), ('R7-Ad-Pool', ad_pool), ('R7-Ad-Word', ad_word), ('R7-Ad-Story', ad_story)])
