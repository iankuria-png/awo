"""Round 7 components, written natively: controls (R7-Components) and data and feedback (R7-Data).
Everything is live. Corners are 6, 10, 14 and a circle; Geist does all the type."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round-6'))
from lib6 import *  # noqa: E402,F401,F403
from screens7 import ic, switch, switch_js, mark, R_S, R_M, R_L, LINE7  # noqa: E402

KIT7_CSS = f"""
.card{{border-radius:{R_L}px;background:#FFFFFF;padding:24px;display:flex;flex-direction:column;gap:16px;box-sizing:border-box}}
.ktitle{{font-size:18px;font-weight:600}}
.knote{{font-size:13px;line-height:1.45;color:#56625C}}
.press{{transition:transform 90ms cubic-bezier(.2,.8,.2,1)}}
.press:active{{transform:scale(.96)}}
.btn{{height:52px;width:100%;border-radius:{R_M}px;font-size:16px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px}}
.sk{{background:linear-gradient(90deg,#E4ECE7 0,#F3F7F5 40%,#E4ECE7 80%);background-size:300% 100%;animation:shimmer 1.4s linear infinite;border-radius:{R_S}px}}
.skd{{background:linear-gradient(90deg,#1C2421 0,#2A3531 40%,#1C2421 80%);background-size:300% 100%;animation:shimmer 1.4s linear infinite;border-radius:{R_S}px}}
@keyframes shimmer{{from{{background-position:100% 0}}to{{background-position:0 0}}}}
.rng{{-webkit-appearance:none;appearance:none;width:100%;height:44px;background:transparent;margin:0}}
.rng::-webkit-slider-runnable-track{{height:8px;border-radius:2px;background:linear-gradient(to right,{EVG} 0,{EVG} var(--p),#DCE4DF var(--p))}}
.rng::-webkit-slider-thumb{{-webkit-appearance:none;width:30px;height:30px;margin-top:-11px;border-radius:{R_S}px;background:{LIME};box-shadow:0 0 0 3px {EVG}}}
.rng::-moz-range-track{{height:8px;border-radius:2px;background:#DCE4DF}}
.rng::-moz-range-progress{{height:8px;border-radius:2px;background:{EVG}}}
.rng::-moz-range-thumb{{width:28px;height:28px;border:0;border-radius:{R_S}px;background:{LIME};box-shadow:0 0 0 3px {EVG}}}
.rng:focus-visible{{outline:2px solid {EVG};outline-offset:4px}}
"""


def board7(title, desc, body, logic, w, h, css='', chip='Sample content. Try tapping.'):
    """A canvas board in Round 7 style (not a phone)."""
    body = holes(body)
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
<style>{BASE_CSS}{EXTRA_CSS}{KIT7_CSS}{css}
body{{background:#E4EAE6}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; box-sizing: border-box; padding: 56px; background: #E4EAE6; color: {INK}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif; display: flex; flex-direction: column; gap: 32px">
  <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
    <div style="display: flex; flex-direction: column; gap: 12px"><h1 class="d" style="font-size: 64px">{title}</h1><p style="max-width: 980px; font-size: 19px; line-height: 1.45; color: {SEC}">{desc}</p></div>
    <span style="flex-shrink: 0; font-size: 14px; font-weight: 500; color: {SEC}; padding: 7px 12px; border: 1px dashed {SEC}; border-radius: {R_S}px">{chip}</span>
  </header>
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
{logic}
</script>
</body>
</html>
'''


def chip7(text, bg=None, fg=INK, dashed=None, lead=''):
    style = f'background: {bg}; color: {fg}' if bg else f'border: 1px dashed {dashed}; color: {dashed}'
    return f'<span class="chip" style="{style}">{lead}{text}</span>'


ALERT = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0"><circle cx="12" cy="12" r="9"></circle><path d="M12 7.5v5M12 16h.01"></path></svg>')

PROVENANCE = (chip7('Sample', dashed=MUTED) + chip7('AI-assisted', dashed=EVG)
              + chip7('Reviewed by AWO', EVG, '#FFFFFF', lead=icon('check', 14, '#FFFFFF', 2.6))
              + chip7('Evidence: early', MIST, SEC) + chip7('Member story', BLUSH, BLUSH_INK)
              + chip7('Stored in South Africa', POOL, EVG, lead=icon('lock', 14, EVG)))


# ---------------------------------------------------------------- Controls

def controls():
    tabs = ''.join(
        f'<button onClick="[[ tab{i} ]]" aria-pressed="[[ tabOn{i} ]]" class="ti" style="color: [[ tabLc{i} ]]; font-weight: [[ tabW{i} ]]; font-size: 12px"><span class="tp" style="background: [[ tabBg{i} ]]; color: [[ tabFg{i} ]]; transition: background-color .18s">{icon(icn)}</span>{n}</button>'
        for i, (n, icn) in enumerate(AREAS))
    filt = ''.join(f'<button onClick="[[ f{i} ]]" aria-pressed="[[ fOn{i} ]]" class="press" style="height: 44px; padding: 0 16px; border-radius: {R_M}px; background: [[ fBg{i} ]]; color: [[ fFg{i} ]]; box-shadow: inset 0 0 0 1px [[ fBd{i} ]]; font-size: 14px; font-weight: 600">{n}</button>'
                   for i, n in enumerate(['All', 'Saving', 'Borrowing', 'Business']))
    seg = ''.join(f'<button onClick="[[ s{i} ]]" aria-pressed="[[ sOn{i} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: [[ sBg{i} ]]; color: [[ sFg{i} ]]; box-shadow: [[ sSh{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{n}</button>'
                  for i, n in enumerate(['Week', 'Month', 'Year']))
    radios = ''.join(f'''<button onClick="[[ r{i} ]]" aria-pressed="[[ rOn{i} ]]" style="min-height: 56px; padding: 0 16px; border-radius: {R_M}px; background: {MIST}; box-shadow: inset 0 0 0 [[ rBw{i} ]]px {EVG}; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; font-weight: 500">
          <span style="flex-grow: 1">{o}</span><span aria-hidden="true" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 999px; border: 2px solid [[ rC{i} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: [[ rF{i} ]]"></span></span></button>'''
                     for i, o in enumerate(["I'd cover it from savings", "I'd borrow from family or friends"]))
    checks = ''.join(f'''<button role="checkbox" aria-checked="[[ c{i} ]]" onClick="[[ tc{i} ]]" style="min-height: 44px; display: flex; align-items: center; gap: 12px; font-size: 15px; font-weight: 500; text-align: left">
          <span aria-hidden="true" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: {R_S}px; background: [[ cBg{i} ]]; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; justify-content: center"><sc-if value="[[ c{i} ]]" hint-placeholder-val="[[ {'true' if i == 0 else 'false'} ]]">{icon('check', 16, '#FFFFFF', 3)}</sc-if></span>{t}</button>'''
                     for i, t in enumerate(['Lessons I finish', 'My check-in dates']))
    sw = [('Check-in reminders', 'The day before, at 18:00'), ('Circle cheers', 'When someone cheers your step'), ('Quiet hours', '21:00 to 07:00, on by default')]
    switches = ''.join(f'''<div style="min-height: 56px; display: flex; align-items: center; gap: 12px; {f'border-bottom: 1px solid {LINE7};' if i < 2 else ''}">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span class="knote">{d}</span></span>{switch(i, t)}</div>''' for i, (t, d) in enumerate(sw))
    st4 = stones(150, 34, [(16, 24, 14, 7), (54, 18, 16, 8), (96, 13, 16, 8), (134, 8, 13, 6.5)], [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='4 4')
    rings = ''.join(f'''<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="position: relative; width: 58px; height: 58px"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid {c}"></span><img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: 5px; top: 5px; width: 48px; height: 48px"></span><span style="font-size: 12px">{t}</span></span>'''
                    for k, c, t in [('wanjiru', '#F29BB5', 'New win'), ('amara', '#C9D3CE', 'Seen')])
    rings += f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="width: 58px; height: 58px; box-sizing: border-box; border-radius: 999px; border: 2px dashed {EVG}; color: {EVG}; display: flex; align-items: center; justify-content: center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg></span><span style="font-size: 12px">Your win</span></span>'
    stack = ''.join(f'<img class="face" src="{IMG[k]}" alt="" style="width: 32px; height: 32px; margin-left: {0 if j == 0 else -9}px; box-shadow: 0 0 0 2px #FFFFFF">' for j, k in enumerate(('thandi', 'grace', 'zodwa', 'lindiwe')))
    col1 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">Buttons</span>
        <button class="btn press" style="height: 56px; background: {EVG}; color: #FFFFFF">Start my check-in</button>
        <button class="btn press" style="box-shadow: inset 0 0 0 1px #C9D3CE">Just look around</button>
        <div style="display: flex; align-items: center; gap: 10px"><button class="press" style="height: 44px; padding: 0 6px; font-size: 15px; font-weight: 600; color: {EVG}">Remind me tomorrow</button><button class="press" aria-label="Send" style="width: 44px; height: 44px; border-radius: {R_M}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('send', 18, EVG)}</button><button aria-disabled="true" style="height: 44px; padding: 0 18px; border-radius: {R_M}px; background: #DCE4DF; color: {MUTED}; font-size: 15px; font-weight: 600">Continue</button></div>
        <div style="border-radius: {R_L}px; background: {NIGHT}; padding: 16px; display: flex; flex-direction: column; gap: 10px"><button class="btn press" style="background: {LIME}; color: {INK}">Start the lesson</button><button class="btn press" style="height: 48px; color: {MOON}; box-shadow: inset 0 0 0 1px {NLINE}">Save for later</button></div>
        <span class="knote">One main button per screen: evergreen on light, lime on dark. Buttons have 10px corners, not pills. A press squeezes to 96% in 90 ms.</span>
      </section>
      <section class="card">
        <span class="ktitle">Tab bar: the shapes teach the areas</span>
        <nav aria-label="Demo tab bar" style="height: 68px; border-radius: {R_L}px; background: {MIST}; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); align-items: center; color: {MUTED}">{tabs}</nav>
        <span class="knote">Home is the pool, Learn the moon, Vault the arch, Community the ripple, Me the stones. The active tab takes its area's colour.</span>
      </section>
      <section class="card">
        <span class="ktitle">The top of a screen</span>
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 12px; display: flex; align-items: center; justify-content: space-between"><span style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('back', 20, INK, 2.2)}</span><span style="font-size: 17px; font-weight: 600">Your buddy</span>{sample_chip()}</div>
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 12px; display: flex; align-items: center; justify-content: space-between"><span class="d" style="font-size: 40px">Vault</span><span style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('search', 20, INK)}</span></div>
        <span class="knote">The five areas open with a big title. Screens inside them get a back button and a small centred title.</span>
      </section>
    </div>'''
    col2 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">Inputs</span>
        <label style="height: 48px; border-radius: {R_M}px; background: {MIST}; display: flex; align-items: center; gap: 10px; padding: 0 14px; color: {MUTED}">{icon('search', 20, MUTED)}<input placeholder="Search money words" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 15px; color: {INK}"></label>
        <div style="display: flex; flex-direction: column; gap: 6px"><label for="k7-inc" style="font-size: 13px; font-weight: 600">Monthly income</label><input id="k7-inc" value="R 12 500" style="height: 52px; box-sizing: border-box; border: 0; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 0 14px; font-size: 16px"><span class="knote">Only you see this.</span></div>
        <div style="display: flex; flex-direction: column; gap: 6px"><label for="k7-save" style="font-size: 13px; font-weight: 600">Put aside each month</label><input id="k7-save" value="five hundred" aria-invalid="true" aria-describedby="k7-err" style="height: 52px; box-sizing: border-box; border: 0; border-radius: {R_M}px; box-shadow: inset 0 0 0 2px {BLUSH_2}; padding: 0 14px; font-size: 16px"><span id="k7-err" style="display: flex; align-items: center; gap: 6px; font-size: 13px; color: {BLUSH_2}; font-weight: 500">{ALERT}Enter an amount in numbers, like 500.</span></div>
      </section>
      <section class="card">
        <span class="ktitle">Choices</span>
        <div role="group" aria-label="Filter" style="display: flex; flex-wrap: wrap; gap: 8px">{filt}</div>
        <div role="group" aria-label="Period" style="display: flex; gap: 4px; padding: 4px; border-radius: {R_M}px; background: {MIST}">{seg}</div>
        <div role="radiogroup" aria-label="A surprise cost" style="display: flex; flex-direction: column; gap: 8px">{radios}</div>
        <div role="group" aria-label="Share with my buddy" style="display: flex; flex-direction: column">{checks}</div>
        <span class="knote">Radios are circles; checkboxes are squares with 6px corners.</span>
      </section>
      <section class="card">
        <span class="ktitle">Switches</span>
        <div style="display: flex; flex-direction: column">{switches}</div>
        <span class="knote">A 10px track and a 6px thumb, inside a 44px target.</span>
      </section>
    </div>'''
    col3 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">The shapes, working</span>
        <div style="display: flex; gap: 20px; align-items: center">
          <div style="position: relative; width: 64px; height: 120px; flex-shrink: 0">{pool(64, 120, 'kPool', rimw=2.5)}<sc-if value="[[ moved ]]" hint-placeholder-val="[[ false ]]"><span class="splash" style="left: 6px; top: [[ splashY ]]px; width: 52px; height: 12px"></span></sc-if></div>
          <div style="display: flex; flex-direction: column; gap: 8px"><span class="d" style="font-size: 40px; color: {EVG}; font-variant-numeric: tabular-nums">[[ amountText ]]</span><span class="knote">of R 5 000. The pool only ever means money she's building.</span><button class="press" onClick="[[ move ]]" style="align-self: flex-start; height: 44px; padding: 0 16px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">[[ moveLabel ]]</button></div>
        </div>
        <div style="height: 1px; background: {LINE7}"></div>
        <div style="display: flex; align-items: center; gap: 16px"><div style="border-radius: {R_M}px; background: {NIGHT}; padding: 10px 12px; display: flex; gap: 8px" role="img" aria-label="Lesson 3 of 6">{moon(22, 'full')}{moon(22, 'full')}{moon(22, 'half', now=True)}{moon(22, 'new')}{moon(22, 'new')}{moon(22, 'new')}</div><span class="knote">Moons wax as lessons go on.</span></div>
        <div style="display: flex; align-items: center; gap: 16px"><span role="img" aria-label="Stage 2 of 4">{st4}</span><span class="knote">Stones: where she stands.</span></div>
        <div style="display: flex; align-items: center; gap: 16px"><div role="img" aria-label="DIVA score 63" style="position: relative; width: 90px; height: 90px">{arc(90, 63, '#DCE4DF', EVG, sw=8)}<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 600; letter-spacing: -0.03em; padding-top: 2px">63</span></div><span class="knote">The DIVA score: one arc, never rings. Not a credit score.</span></div>
      </section>
      <section class="card">
        <span class="ktitle">Labels that say where things come from</span>
        <div style="display: flex; flex-wrap: wrap; gap: 8px">{PROVENANCE}</div>
        <span class="knote">Labels have 6px corners. "Reviewed by AWO" only appears on content from the governed library.</span>
      </section>
      <section class="card">
        <span class="ktitle">People</span>
        <div style="display: flex; gap: 14px; align-items: flex-start">{rings}<span style="margin-left: auto; display: flex; flex-direction: column; align-items: flex-end; gap: 6px"><span style="display: flex">{stack}</span><span style="font-size: 12px; color: {MUTED}">38 answered</span></span></div>
        <div style="display: flex; gap: 10px; align-items: flex-start"><img class="face" src="{IMG['thandi']}" alt="" style="width: 32px; height: 32px"><span style="padding: 10px 14px; border-radius: {R_S}px {R_L}px {R_L}px {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; font-size: 14px; line-height: 1.4">A second pair of work shoes. The first pair is fine.</span></div>
        <div style="display: flex; align-items: center; gap: 10px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 32px; height: 32px"><span style="flex-grow: 1; font-size: 14px; font-weight: 600">Wanjiru</span><button onClick="[[ doCheer ]]" aria-pressed="[[ cheered ]]" style="position: relative; height: 44px; padding: 0 14px; border-radius: {R_M}px; background: [[ cheerBg ]]; color: [[ cheerFg ]]; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s"><sc-if value="[[ cheered ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; border-radius: {R_M}px; color: {BLUSH_INK}"></span></sc-if>{icon('ripple', 18)}[[ cheerLabel ]]</button></div>
        <span class="knote">Circles are for people. Blush is only for people: faces, their words, cheers.</span>
      </section>
    </div>'''
    body = f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; align-items: start">{col1}{col2}{col3}</div>'
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const tab = st.tab == null ? 0 : st.tab, f = st.f || 0, s = st.s == null ? 1 : st.s, r = st.r == null ? 1 : st.r;
    const amt = st.amt == null ? 1800 : st.amt, moved = !!st.moved, cheered = !!st.cheered;
    const act = %(act)s;
    const v = {
      amountText: 'R ' + String(amt).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' '),
      waterY: Math.round(116 - (amt / 5000) * 112), poolLabel: 'R ' + amt + ' of R 5 000', splashY: Math.round(116 - (amt / 5000) * 112) - 6,
      moved, move: () => this.setState({ amt: amt >= 4900 ? 1800 : amt + 100, moved: false }, () => this.setState({ moved: true })),
      moveLabel: amt >= 4900 ? 'Start again' : 'I moved R 100',
      cheered, doCheer: () => this.setState({ cheered: !cheered }), cheerLabel: cheered ? 'Cheered' : 'Cheer',
      cheerBg: cheered ? '%(bi)s' : '%(b)s', cheerFg: cheered ? '%(b)s' : '%(bi)s'
    };
    for (let i = 0; i < 5; i++) {
      const on = tab === i;
      v['tab' + i] = () => this.setState({ tab: i }); v['tabOn' + i] = on;
      v['tabBg' + i] = on ? act[i][0] : 'transparent'; v['tabFg' + i] = on ? act[i][1] : '%(mut)s';
      v['tabLc' + i] = on ? act[i][2] : '%(mut)s'; v['tabW' + i] = on ? 600 : 400;
    }
    for (let i = 0; i < 4; i++) {
      v['f' + i] = () => this.setState({ f: i }); v['fOn' + i] = f === i;
      v['fBg' + i] = f === i ? '%(evg)s' : '#FFFFFF'; v['fFg' + i] = f === i ? '#FFFFFF' : '%(ink)s'; v['fBd' + i] = f === i ? '%(evg)s' : '#C9D3CE';
    }
    for (let i = 0; i < 3; i++) {
      v['s' + i] = () => this.setState({ s: i }); v['sOn' + i] = s === i;
      v['sBg' + i] = s === i ? '#FFFFFF' : 'transparent'; v['sFg' + i] = s === i ? '%(ink)s' : '%(mut)s';
      v['sSh' + i] = s === i ? '0 1px 3px rgba(16,24,20,.12)' : 'none';
    }
    for (let i = 0; i < 2; i++) {
      v['r' + i] = () => this.setState({ r: i }); v['rOn' + i] = r === i; v['rBw' + i] = r === i ? 2 : 0;
      v['rC' + i] = r === i ? '%(evg)s' : '#A9B6AF'; v['rF' + i] = r === i ? '%(evg)s' : 'transparent';
      const c = st['c' + i] == null ? i === 0 : st['c' + i];
      v['c' + i] = c; v['tc' + i] = () => this.setState({ ['c' + i]: !c }); v['cBg' + i] = c ? '%(evg)s' : '#FFFFFF';
    }
%(sw)s
    return v;
  }
}''' % dict(act=[[ACTIVE[n][0], ACTIVE[n][1], NIGHT if n == 'Learn' else ACTIVE[n][2]] for n, _ in AREAS], bi=BLUSH_INK, b=BLUSH, mut=MUTED, evg=EVG, ink=INK, sw=switch_js(3, [True, True, True]))
    return board7('Components', 'The controls every Round 7 screen is built from: Geist for all type, corners of 6, 10 and 14, and circles only for people, dots and the shapes. Everything here works.', body, logic, 1440, 1420)


# ---------------------------------------------------------------- Data and feedback

def spark(points, w, h, col, dot_last=True):
    lo, hi = min(points), max(points)
    xs = [round(4 + i * (w - 8) / (len(points) - 1), 1) for i in range(len(points))]
    ys = [round(h - 4 - (p - lo) / (hi - lo or 1) * (h - 8), 1) for p in points]
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in zip(xs, ys))
    end = f'<circle cx="{xs[-1]}" cy="{ys[-1]}" r="4" fill="{col}"></circle>' if dot_last else ''
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display: block; overflow: visible"><path d="{d}" fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"></path>{end}</svg>'


def data():
    week = ''.join(f'<span style="width: 14px; height: {h}px; border-radius: 2px; background: {EVG if on else "#DCE4DF"}"></span>' for h, on in [(26, 1), (26, 1), (26, 0), (26, 1), (26, 1), (26, 0), (26, 0)])
    stats = f'''<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">
      <section class="card" style="flex-direction: row; align-items: flex-end; justify-content: space-between; padding: 22px 24px"><span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {SEC}">Safety net</span><span class="d" style="font-size: 48px; color: {EVG}">R 3 100</span><span style="font-size: 13px; color: {SEC}"><b style="color: {EVG}">+R 500</b> this month</span></span>{spark([1600, 1900, 2100, 2600, 3100], 120, 44, EVG)}</section>
      <section class="card" style="flex-direction: row; align-items: flex-end; justify-content: space-between; padding: 22px 24px"><span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {SEC}">Learning days</span><span class="d" style="font-size: 48px">4</span><span style="font-size: 13px; color: {SEC}">this week, one more than last</span></span><span role="img" aria-label="4 of 7 days" style="display: flex; gap: 4px">{week}</span></section>
      <section class="card" style="flex-direction: row; align-items: flex-end; justify-content: space-between; padding: 22px 24px; background: {LIME}"><span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {EVG}">Lessons done</span><span class="d" style="font-size: 48px; color: {EVG}">9</span><span style="font-size: 13px; color: {EVG}"><b>+2</b> this week</span></span>{spark([3, 4, 5, 7, 9], 120, 44, EVG)}</section>
    </div>'''
    bars = ''.join(f'''<button onClick="[[ m{i} ]]" aria-pressed="[[ mOn{i} ]]" aria-label="Month {i + 1}" style="flex: 1 1 0; height: 196px; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 8px">
          <span style="width: 100%; max-width: 34px; height: [[ bh{i} ]]px; border-radius: 4px 4px 2px 2px; background: [[ bc{i} ]]; transition: height .4s cubic-bezier(.2,.8,.2,1), background-color .18s"></span>
          <span style="font-size: 12px; color: [[ bl{i} ]]; font-weight: [[ bw{i} ]]">{i + 1}</span></button>''' for i in range(12))
    calc = f'''<section class="card" style="gap: 14px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span class="ktitle">What if I put aside a little each month?</span>{chip7('Calculator', MIST, SEC)}</span>
        <span style="display: flex; align-items: baseline; gap: 12px"><span style="font-size: 15px; color: {SEC}">Each month</span><span class="d" style="font-size: 44px; color: {EVG}; font-variant-numeric: tabular-nums">[[ perText ]]</span></span>
        <label for="k7-per" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Amount each month</label>
        <input id="k7-per" class="rng" style="--p: [[ perPct ]]%" type="range" min="100" max="2000" step="50" value="[[ per ]]" onInput="[[ slide ]]" aria-valuetext="[[ perText ]] a month">
        <div role="group" aria-label="Months. Tap one to see its total." style="display: flex; gap: 8px; align-items: flex-end; border-bottom: 1px solid {LINE7}; padding-bottom: 4px">{bars}</div>
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; color: {SEC}">[[ afterText ]]</span><span class="d" style="font-size: 32px; color: {EVG}; font-variant-numeric: tabular-nums">[[ totalText ]]</span></div>
        <span class="knote">Simple arithmetic with no interest. Not a forecast. Tap a month to see its total.</span>
      </section>'''
    st4 = stones(120, 30, [(14, 22, 12, 6), (46, 16, 13, 6.5), (80, 11, 13, 6.5), (110, 6, 10, 5)], [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='3 3')
    story = ''.join(f'<span style="flex: 1 1 0; height: 4px; border-radius: 2px; background: {c}"></span>' for c in [MOON, MOON, 'rgba(242,241,236,.35)', 'rgba(242,241,236,.35)'])
    five = [
        (f'<span style="width: 100%; display: flex; flex-direction: column; gap: 8px"><span style="display: flex; justify-content: space-between; font-size: 13px"><span style="font-weight: 600">This week’s step</span><span style="color: {MUTED}">1 of 2</span></span><span style="height: 8px; border-radius: 2px; background: #DCE4DF; overflow: hidden"><span style="display: block; width: 50%; height: 100%; background: {EVG}; transform-origin: left; animation: fill .8s cubic-bezier(.2,.8,.2,1) .2s both"></span></span></span>', 'A bar for steps', MIST),
        (f'<span role="img" aria-label="Day 12 of 30" style="position: relative; width: 76px; height: 76px">{arc(76, 40, "#DCE4DF", EVG, sw=7)}<span style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1.1"><span style="font-size: 22px; font-weight: 600">12</span><span style="font-size: 12px; color: {MUTED}">of 30</span></span></span>', 'An arc for the 30 days', MIST),
        (f'<span role="img" aria-label="R 1 800 of R 5 000" style="display: flex; align-items: center; gap: 12px"><span style="width: 40px; height: 76px">{pool(40, 76, "dPool", rimw=2, static=True, hole="dY", label="dLabel")}</span><span style="font-size: 20px; font-weight: 600; color: {EVG}">R 1 800</span></span>', 'A pool for money goals', MIST),
        (f'<span role="img" aria-label="Stage 2 of 4">{st4}</span>', 'Stones for her stage', MIST),
        (f'<span role="img" aria-label="Lesson 3 of 6" style="display: flex; gap: 6px">{moon(20, "full")}{moon(20, "full")}{moon(20, "half", now=True)}{moon(20, "new")}{moon(20, "new")}</span>', 'Moons for lessons', NIGHT),
        (f'<span aria-hidden="true" style="width: 100%; display: flex; gap: 4px">{story}</span>', 'Story bars inside a lesson', NIGHT),
    ]
    tiles = ''.join(f'<div style="border-radius: {R_M}px; background: {bg}; color: {MOON if bg == NIGHT else INK}; padding: 16px; min-height: 132px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; align-items: flex-start; gap: 12px"><span style="min-height: 76px; width: 100%; display: flex; align-items: center">{vis}</span><span style="font-size: 13px; font-weight: 600">{cap}</span></div>' for vis, cap, bg in five)
    progress_card = f'''<section class="card">
        <span class="ktitle">Progress, six ways</span>
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px">{tiles}</div>
        <span class="knote">Each kind of progress has its own shape, so it's never confused with another. None of them is a streak.</span>
      </section>'''
    appmark = f'<span aria-hidden="true" style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {EVG}; display: flex; align-items: center; justify-content: center">{mark(26, "#FFFFFF", LIME)}</span>'
    notes = f'''<section class="card">
        <span class="ktitle">Notices</span>
        <div style="border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; min-height: 56px; padding: 6px 6px 6px 12px; box-sizing: border-box; display: flex; align-items: center; gap: 12px"><span style="width: 30px; height: 30px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 16, EVG, 3)}</span><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Saved to your Vault</span><button style="height: 44px; padding: 0 14px; border-radius: {R_S}px; background: rgba(255,255,255,.14); font-size: 14px; font-weight: 600">View</button></div>
        <div style="border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #DCE4DF; padding: 12px; display: flex; align-items: center; gap: 12px"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {POOL}; color: {EVG}; display: flex; align-items: center; justify-content: center">{icon('stones', 20)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Your check-in is in 3 days</span><span class="knote">Three questions, about two minutes.</span></span></div>
        <div style="border-radius: {R_M}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 12px; display: flex; align-items: center; gap: 12px"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {BLUSH_2}; color: #FFFFFF; display: flex; align-items: center; justify-content: center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4 2.5 20h19z"></path><path d="M12 10v4.5M12 17.5h.01"></path></svg></span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">A common scam sign</span><span style="font-size: 13px; line-height: 1.4">This message asks for a fee before paying out a prize.</span></span></div>
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 12px; display: flex; align-items: center; gap: 12px">{appmark}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Lesson 3 is ready</span><span class="knote">Where to keep a safety net, six minutes.</span></span><span style="font-size: 12px; color: {MUTED}; align-self: flex-start">now</span></div>
        <div style="position: relative; height: 56px">
          <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div role="status" style="position: absolute; inset: 0; border-radius: {R_M}px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 6px 0 14px; font-size: 15px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both"><span style="width: 26px; height: 26px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 14, EVG, 3)}</span><span style="flex-grow: 1">Saved. Your check-in is in.</span><button onClick="[[ hideToast ]]" style="height: 44px; padding: 0 12px; font-weight: 600; color: {LIME}">Undo</button></div></sc-if>
          <sc-if value="[[ noToast ]]" hint-placeholder-val="[[ true ]]"><button class="btn press" onClick="[[ showToast ]]" style="height: 56px; background: {MIST}">Show a confirmation</button></sc-if>
        </div>
        <span class="knote">A person or a plain fact first, then one thing to do. Never guilt and never a streak.</span>
      </section>'''
    states = f'''<section class="card">
        <span class="ktitle">Waiting, empty, offline, failed</span>
        <div role="img" aria-label="Loading" style="border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #DCE4DF; padding: 14px; display: flex; flex-direction: column; gap: 12px"><div style="display: flex; gap: 12px; align-items: center"><span class="sk" style="width: 40px; height: 40px; border-radius: {R_M}px"></span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span class="sk" style="height: 12px; width: 70%"></span><span class="sk" style="height: 10px; width: 45%"></span></span></div><span class="sk" style="height: 64px; border-radius: {R_M}px"></span></div>
        <div role="img" aria-label="Ola is thinking" style="border-radius: {R_M}px; background: {NIGHT}; padding: 14px; display: flex; flex-direction: column; gap: 10px"><span style="display: flex; gap: 6px; align-items: center">{''.join(f'<span style="width: 8px; height: 8px; border-radius: 999px; background: {MINT}; animation: pulse 1.2s ease-in-out {d}s infinite"></span>' for d in (0, .2, .4))}<span style="font-size: 13px; color: {NMUTED}; margin-left: 4px">Ola is thinking</span></span><span class="skd" style="height: 12px; width: 80%"></span><span class="skd" style="height: 12px; width: 55%"></span></div>
        <div style="border-radius: {R_M}px; background: {INK}; color: {MOON}; padding: 12px 14px; display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 500"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M2 8.8a15 15 0 0 1 4.2-2.6M9.8 5.2A15 15 0 0 1 22 8.8M8.5 16.4a5 5 0 0 1 7 0M12 20h.01M3 3l18 18"></path></svg>You're offline. Your lesson is saved on this phone.</div>
        <div style="border-radius: {R_M}px; background: {MIST}; padding: 14px 16px; display: flex; align-items: center; gap: 12px"><span style="color: {EVG}; display: flex">{icon('arch', 26)}</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Nothing kept yet, and that's fine.</span><span class="knote">Tap the bookmark on any word to keep it here.</span></span></div>
        <div style="border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #DCE4DF; padding: 14px 16px; display: flex; align-items: center; gap: 12px; min-height: 72px; box-sizing: border-box">
          <sc-if value="[[ failed ]]" hint-placeholder-val="[[ true ]]"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">That didn't load.</span><span class="knote">Your answers are safe on this phone.</span></span><button onClick="[[ retry ]]" style="height: 44px; padding: 0 16px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">Try again</button></sc-if>
          <sc-if value="[[ loading ]]" hint-placeholder-val="[[ false ]]"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span class="sk" style="height: 12px; width: 60%"></span><span class="sk" style="height: 10px; width: 40%"></span></span></sc-if>
          <sc-if value="[[ loaded ]]" hint-placeholder-val="[[ false ]]"><span style="width: 30px; height: 30px; border-radius: {R_S}px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 16, EVG, 3)}</span><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Loaded. Lesson 3 is ready.</span><button onClick="[[ reset ]]" style="height: 44px; padding: 0 12px; font-size: 14px; font-weight: 600; color: {EVG}">Reset</button></sc-if>
        </div>
        <span class="knote">Skeletons keep the page's shape on slow data. Empty states say what comes first, never what's missing.</span>
      </section>'''
    body = f'''{stats}
    <div style="display: grid; grid-template-columns: 1.1fr .9fr; gap: 24px; align-items: start">{calc}{progress_card}</div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; align-items: start">{notes}{states}</div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const per = st.per == null ? 500 : st.per, mon = st.mon == null ? 11 : st.mon;
    const fmt = (n) => 'R ' + String(n).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' ');
    const toast = !!st.toast, phase = st.phase || 0;
    const v = {
      per, perText: fmt(per), perPct: Math.round((per - 100) / 19), slide: (e) => this.setState({ per: Number(e.target.value) }),
      afterText: 'After ' + (mon + 1) + (mon === 0 ? ' month' : ' months'), totalText: fmt(per * (mon + 1)),
      dY: Math.round(76 * (1 - 1800 / 5000)), dLabel: 'R 1 800 of R 5 000',
      toast, noToast: !toast, showToast: () => this.setState({ toast: true }), hideToast: () => this.setState({ toast: false }),
      failed: phase === 0, loading: phase === 1, loaded: phase === 2,
      retry: () => { this.setState({ phase: 1 }); setTimeout(() => this.setState({ phase: 2 }), 1200); },
      reset: () => this.setState({ phase: 0 })
    };
    for (let i = 0; i < 12; i++) {
      v['m' + i] = () => this.setState({ mon: i }); v['mOn' + i] = mon === i;
      v['bh' + i] = Math.max(4, Math.round(per * (i + 1) / 24000 * 170));
      v['bc' + i] = mon === i ? '%(evg)s' : '#BFD9D2'; v['bl' + i] = mon === i ? '%(ink)s' : '%(mut)s'; v['bw' + i] = mon === i ? 600 : 400;
    }
    return v;
  }
}''' % dict(evg=EVG, ink=INK, mut=MUTED)
    return board7('Data and feedback', 'Numbers always come with plain words. Charts use one colour, thin marks and labels right on them. The calculator is live.', body, logic, 1440, 1560)


BOARDS = [('R7-Components', controls), ('R7-Data', data)]
