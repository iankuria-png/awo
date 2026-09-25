"""Round 6 marketing, built from captures of the Round 6 screens (not from older mock-ups).
Recapture with render4.mjs (plan-shots.json) whenever a screen changes, then re-upload."""
from lib6 import *

CAPS = {
    'home': '/_blob/8deffe6fa15d00879d7ef7fe64afa829', 'me': '/_blob/2024fdeb6f77457201ed88d05715f7d3',
    'learn': '/_blob/f6fe6a3e5f9d71f1d94e190140008434', 'vault': '/_blob/f0c6a25d441f689449537f296cf32f97',
    'community': '/_blob/cee149f6c4b2dcb313c07307e85aad28', 'ask': '/_blob/5cd594e87a207ebd029f5199dc879bd3',
    'welcome': '/_blob/c6e54f6c0b375527f4431beadcf33ac5',
}


def canvas_board(title, w, h, bg, inner, fg=INK):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{BASE_CSS}{EXTRA_CSS}
body{{background:{bg}}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {bg}; color: {fg}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
{static_logic()}
</script>
</body>
</html>
'''


def device(src, w, alt, shadow=True, dark=False):
    h = round(w * 1688 / 780)
    sh = 'box-shadow: 0 40px 90px rgba(11,15,14,.28);' if shadow else ''
    if dark:
        sh = 'box-shadow: 0 0 0 2px #2E3A36, 0 40px 90px rgba(0,0,0,.5);'
    return (f'<div style="width: {w + 24}px; height: {h + 24}px; box-sizing: border-box; padding: 12px; border-radius: {round(w * .14)}px; background: #0B0F0E; {sh}">'
            f'<img src="{src}" alt="{alt}" style="width: {w}px; height: {h}px; border-radius: {round(w * .115)}px; display: block"></div>')


def wordmark(size, col):
    return f'<span class="d" style="font-size: {size}px; color: {col}">awo</span>'


STORE = [
    ('me', POOL, EVG, SEC, 'Know where you stand.', 'A clear picture of your money life, in plain words. Not a credit score.', 'Your DIVA profile'),
    ('home', EVG, LIME, ON_EVG, 'One small step a week.', 'Watch your safety net fill as you go.', 'Home'),
    ('learn', NIGHT, MOON, NMUTED, 'Learn money in three minutes.', "Short lessons told through real women's stories.", 'Learn'),
    ('vault', LIME, EVG, INK, 'Money words, made clear.', 'Keep the words you learn. Flip any of them for a real example.', 'The Vault'),
    ('community', BLUSH, BLUSH_INK, BLUSH_2, 'Grow with women who get it.', 'Cheers, circles and honest questions. First names only.', 'Community'),
    ('ask', DEEP, MOON, NMUTED, 'Ask anything. Get plain answers.', 'Ola explains and teaches. It never tells you what to buy.', 'Ask Ola'),
]


def store(i):
    key, bg, head, sub, title, text, alt = STORE[i]
    inner = f'''<div style="position: absolute; left: 90px; right: 90px; top: 96px; display: flex; flex-direction: column; gap: 28px">
  {wordmark(52, head)}
  <h1 class="d" style="font-size: 132px; color: {head}">{title}</h1>
  <p style="font-size: 40px; line-height: 1.3; color: {sub}; max-width: 860px">{text}</p>
</div>
<div style="position: absolute; left: 198px; top: 720px">{device(CAPS[key], 660, 'The ' + alt + ' screen', dark=bg in (NIGHT, DEEP))}</div>'''
    return canvas_board(f'Store screenshot {i + 1}', 1080, 1920, bg, inner)


def shapes_strip(size=96):
    items = [(EVG_D, LIME, 'pool'), (NIGHT, MOON, 'moon'), (LIME, EVG, 'arch'), (BLUSH, BLUSH_INK, 'ripple'), (POOL, EVG, 'stones')]
    return ''.join(f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {b}; display: flex; align-items: center; justify-content: center">{icon(ic, round(size * .5), f, 2)}</span>' for b, f, ic in items)


def feature():
    ys = [250, 190, 140, 104, 84]
    shapes = ''.join(
        f'<span style="position: absolute; left: {560 + k * 92}px; top: {ys[k]}px; width: 112px; height: 112px; border-radius: 999px; background: {b}; display: flex; align-items: center; justify-content: center; box-shadow: 0 16px 30px rgba(0,0,0,.18)">{icon(ic, 54, f, 2)}</span>'
        for k, (b, f, ic) in enumerate([(EVG_D, LIME, 'pool'), (NIGHT, MOON, 'moon'), (LIME, EVG, 'arch'), (BLUSH, BLUSH_INK, 'ripple'), (POOL, EVG, 'stones')]))
    inner = f'''<div style="position: absolute; left: 64px; top: 60px; width: 470px; display: flex; flex-direction: column; gap: 18px">
  {wordmark(64, LIME)}
  <h1 class="d" style="font-size: 72px; color: #FFFFFF">Know where you stand. Grow from there.</h1>
  <p style="font-size: 20px; line-height: 1.4; color: {ON_EVG}">Free money learning for women, at home and abroad.</p>
</div>
<svg width="1024" height="500" viewBox="0 0 1024 500" aria-hidden="true" style="position: absolute; inset: 0"><path d="M600 360C700 330 800 250 1010 150" fill="none" stroke="{LIME}" stroke-opacity=".3" stroke-width="2" stroke-dasharray="4 8"></path></svg>
{shapes}'''
    return canvas_board('Feature graphic', 1024, 500, EVG, inner)


def icon_mark(size, kind):
    r = round(size * .22)
    if kind == 'stones':
        s = size / 100
        art = (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">'
               f'<ellipse cx="28" cy="72" rx="15" ry="6.5" fill="{EVG_D}"></ellipse><ellipse cx="28" cy="69" rx="15" ry="6.5" fill="{LIME}"></ellipse>'
               f'<ellipse cx="52" cy="55" rx="16" ry="7" fill="{EVG_D}"></ellipse><ellipse cx="52" cy="52" rx="16" ry="7" fill="{LIME}"></ellipse>'
               f'<ellipse cx="75" cy="36" rx="14" ry="6.5" fill="none" stroke="{LIME}" stroke-width="3" stroke-dasharray="4 4"></ellipse></svg>')
    else:
        art = f'<span class="d" style="font-size: {round(size * .44)}px; color: {LIME}; margin-top: -{round(size * .04)}px">awo</span>'
    return f'<span style="width: {size}px; height: {size}px; border-radius: {r}px; background: {EVG}; display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0">{art}</span>'


def icons_board():
    def cand(kind, name, note):
        circle = f'<span style="width: 120px; height: 120px; border-radius: 999px; overflow: hidden; display: flex; align-items: center; justify-content: center; background: {EVG}">{icon_mark(120, kind).replace("border-radius: 26px", "border-radius: 0")}</span>'
        return f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; align-items: flex-end; gap: 28px">{icon_mark(300, kind)}<div style="display: flex; flex-direction: column; gap: 18px; align-items: center">{circle}{icon_mark(64, kind)}{icon_mark(40, kind)}</div></div>
      <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 22px; font-weight: 600">{name}</span><span style="font-size: 16px; line-height: 1.45; color: {SEC}; max-width: 480px">{note}</span></div>
    </div>'''
    inner = f'''<div style="position: absolute; inset: 56px; display: flex; gap: 96px">
  {cand('stones', 'A: stepping stones', 'The Me shape: where you stand, and the next step. Reads at 40px and in a circle mask. No letters to localise.')}
  {cand('word', 'B: the wordmark', 'Lowercase awo in the condensed display face. Strong at large sizes; the letters blur below 48px. Wordmark itself is still open (Q-25).')}
</div>'''
    return canvas_board('App icon candidates', 1280, 640, MIST, inner)


def hero():
    inner = f'''<div style="position: absolute; left: 80px; top: 120px; width: 520px; display: flex; flex-direction: column; gap: 26px">
  {wordmark(48, EVG)}
  <h1 class="d" style="font-size: 116px">Money, understood.</h1>
  <p style="font-size: 24px; line-height: 1.45; color: {SEC}">Free money learning and insight for women building their financial lives, at home and abroad.</p>
  <div style="display: flex; gap: 10px"><span class="chip" style="height: 36px; padding: 0 16px; font-size: 15px; background: {EVG}; color: #FFFFFF">Free</span><span class="chip" style="height: 36px; padding: 0 16px; font-size: 15px; background: #FFFFFF; color: {EVG}">Education, not advice</span><span class="chip" style="height: 36px; padding: 0 16px; font-size: 15px; background: #FFFFFF; color: {EVG}">{icon('lock', 16, EVG)}Data stays in South Africa</span></div>
</div>
<img src="{IMG['naledi_table']}" alt="A woman working at her dining table with a laptop" style="position: absolute; left: 660px; top: 60px; width: 640px; height: 780px; object-fit: cover; object-position: 38% 50%; border-radius: 40px">
<div style="position: absolute; left: 1196px; top: 150px">{device(CAPS['home'], 300, 'The Home screen')}</div>'''
    return canvas_board('Device hero', 1600, 900, MIST, inner)


def listing():
    thumbs = ''.join(
        f'<div style="width: 160px; height: 290px; border-radius: 22px; background: {bg}; overflow: hidden; position: relative; flex-shrink: 0"><span class="d" style="position: absolute; left: 14px; top: 14px; right: 14px; font-size: 20px; color: {head}">{title}</span>'
        f'<img src="{CAPS[key]}" alt="" style="position: absolute; left: 22px; top: 86px; width: 116px; border-radius: 14px; box-shadow: 0 0 0 4px #0B0F0E, 0 0 0 5px #2E3A36"></div>'
        for key, bg, head, _s, title, _t, _a in STORE)
    feat_mini = f'''<div style="width: 512px; height: 250px; border-radius: 22px; background: {EVG}; position: relative; overflow: hidden; flex-shrink: 0"><div style="position: absolute; left: 28px; top: 28px; width: 250px; display: flex; flex-direction: column; gap: 10px">{wordmark(30, LIME)}<span class="d" style="font-size: 34px; color: #FFFFFF">Know where you stand. Grow from there.</span></div><div style="position: absolute; right: 24px; top: 70px; display: flex; gap: 8px">{shapes_strip(40)}</div></div>'''
    inner = f'''<div style="position: absolute; inset: 64px; display: flex; gap: 64px">
  <div style="width: 480px; flex-shrink: 0; display: flex; flex-direction: column; gap: 22px">
    <div style="display: flex; align-items: center; gap: 22px">{icon_mark(128, 'stones')}<div style="display: flex; flex-direction: column; gap: 6px"><span class="d" style="font-size: 64px">AWO</span><span style="font-size: 20px; color: {SEC}">Money, understood.</span></div></div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap"><span class="chip" style="height: 32px; font-size: 14px; background: {EVG}; color: #FFFFFF">Free</span><span class="chip" style="height: 32px; font-size: 14px; background: #FFFFFF; color: {EVG}">Education</span><span class="chip" style="height: 32px; font-size: 14px; background: #FFFFFF; color: {EVG}">English at launch</span></div>
    <p style="font-size: 22px; line-height: 1.4; font-weight: 600">Money learning and insight for African women, at home and abroad.</p>
    <div style="display: flex; flex-direction: column; gap: 14px; font-size: 17px; line-height: 1.5; color: {SEC}">
      <span><strong style="color: {INK}">Know where you stand.</strong> A DIVA profile in plain words, with a new version after every check-in.</span>
      <span><strong style="color: {INK}">One small step a week,</strong> and a safety net that fills as you go.</span>
      <span><strong style="color: {INK}">Three-minute lessons,</strong> a vault of money words and circles of women who get it.</span>
      <span><strong style="color: {INK}">Ask Ola</strong> to explain a result, a word or an offer. It teaches; it never tells you what to buy.</span>
    </div>
    <span style="display: flex; align-items: center; gap: 8px; font-size: 15px; color: {SEC}">{icon('lock', 18, EVG)}Your data is stored in South Africa.</span>
  </div>
  <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 28px; min-width: 0">
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Feature graphic</span>
    {feat_mini}
    <span style="font-size: 15px; font-weight: 600; color: {MUTED}">Screenshots</span>
    <div style="display: flex; gap: 14px">{thumbs}</div>
  </div>
</div>'''
    return canvas_board('Store listing (our own layout)', 1720, 820, MIST, inner)


def ad_word():
    inner = f'''<div style="position: absolute; inset: 80px; display: flex; flex-direction: column; gap: 22px; color: {EVG}">
  <div style="display: flex; justify-content: space-between; align-items: flex-start"><span style="font-size: 34px; font-weight: 600">Word of the week</span>{icon('arch', 120, EVG, 1.6)}</div>
  <span class="d" style="font-size: 300px; line-height: .82; margin-top: 10px">Stokvel</span>
  <span style="font-size: 34px">Say it: stok-fel</span>
  <p style="font-size: 44px; line-height: 1.3; color: {INK}; max-width: 860px">A savings group. Members pay in every month and take turns to receive the pot.</p>
  <div style="flex-grow: 1"></div>
  <div style="display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 32px; font-weight: 600">Learn a money word a week.</span>{wordmark(76, EVG)}</div>
</div>'''
    return canvas_board('Square ad, word of the week', 1080, 1080, LIME, inner)


def ad_pool():
    inner = f'''<div style="position: absolute; left: 90px; top: 150px">{pool(300, 780, 'adPool', water=POOL, wave=LIME, vessel=EVG_D, rim=LIME, rimw=6, static=True, hole='adY', label='adLabel').replace('{{ adY }}', str(round(780 * (1 - 0.36)))).replace('{{ adLabel }}', 'A safety net pool, just over a third full')}</div>
<div style="position: absolute; left: 470px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
  <h1 class="d" style="font-size: 170px; color: {LIME}">R 100 at a time.</h1>
  <p style="font-size: 42px; line-height: 1.3; color: #FFFFFF">Build a safety net that fits your life.</p>
</div>
<div style="position: absolute; left: 470px; right: 80px; bottom: 90px; display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 26px; line-height: 1.35; color: {ON_EVG}">Free money learning<br>for women.</span>{wordmark(80, LIME)}</div>'''
    return canvas_board('Square ad, the pool', 1080, 1080, EVG, inner)


def ad_story():
    inner = f'''<img src="{IMG['amara_coat']}" alt="Amara outdoors in a winter coat" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1180px; object-fit: cover; object-position: 60% 35%">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 820px; border-radius: 64px 64px 0 0; background: {EVG}; padding: 90px 90px 110px; box-sizing: border-box; display: flex; flex-direction: column; gap: 30px">
  <span class="d" style="font-size: 104px; color: #FFFFFF">“My safety net went down this month. It did its job.”</span>
  <span style="font-size: 32px; color: {ON_EVG}">Amara, a nurse in London. Sample story.</span>
  <div style="flex-grow: 1"></div>
  <div style="display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 32px; line-height: 1.35; color: #FFFFFF">Money, understood,<br>with women who get it.</span>{wordmark(92, LIME)}</div>
</div>'''
    return canvas_board('Story ad', 1080, 1920, EVG, inner)


if __name__ == '__main__':
    out = sys.argv[1]
    for i in range(len(STORE)):
        write(os.path.join(out, f'R6-Store-{i + 1}.dc.html'), store(i))
    for name, fn in [('R6-Listing', listing), ('R6-Feature-Graphic', feature), ('R6-App-Icon', icons_board), ('R6-Hero-Device', hero),
                     ('R6-Ad-Word', ad_word), ('R6-Ad-Pool', ad_pool), ('R6-Ad-Story', ad_story)]:
        write(os.path.join(out, name + '.dc.html'), fn())
