"""R6-Components and R6-Widgets: the Round 6 parts, laid out as a kit. Tap them."""
from lib6 import *
from areas import dot

KIT_CSS = """
.card{border-radius:28px;background:#FFFFFF;padding:24px;display:flex;flex-direction:column;gap:16px;box-sizing:border-box}
.ktitle{font-size:18px;font-weight:600}
.knote{font-size:13px;line-height:1.4;color:#56625C}
.press{transition:transform 90ms cubic-bezier(.2,.8,.2,1)}
.press:active{transform:scale(.96)}
.sk{background:linear-gradient(90deg,#E4ECE7 0,#F3F7F5 40%,#E4ECE7 80%);background-size:300% 100%;animation:shimmer 1.4s linear infinite;border-radius:8px}
@keyframes shimmer{from{background-position:100% 0}to{background-position:0 0}}
"""


def kit_board(title, desc, body, logic, w, h, defs='', css='', chip='Sample content. Try tapping.'):
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
<style>{BASE_CSS}{EXTRA_CSS}{KIT_CSS}{css}
body{{background:#E4EAE6}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; box-sizing: border-box; padding: 56px; background: #E4EAE6; color: {INK}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif; display: flex; flex-direction: column; gap: 32px">
  <svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs>{defs}</defs></svg>
  <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
    <div style="display: flex; flex-direction: column; gap: 12px"><h1 class="d" style="font-size: 64px">{title}</h1><p style="max-width: 1000px; font-size: 19px; line-height: 1.45; color: {SEC}">{desc}</p></div>
    <span style="flex-shrink: 0; font-size: 14px; font-weight: 500; color: {SEC}; padding: 7px 14px; border: 1px dashed {SEC}; border-radius: 999px">{chip}</span>
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


def components():
    tabs = ''.join(
        f'<button onClick="[[ tab{i} ]]" aria-pressed="[[ tabOn{i} ]]" class="ti" style="color: [[ tabLc{i} ]]; font-weight: [[ tabW{i} ]]; font-size: 12px"><span class="tp" style="background: [[ tabBg{i} ]]; color: [[ tabFg{i} ]]; transition: background-color .18s">{icon(ic)}</span>{n}</button>'
        for i, (n, ic) in enumerate(AREAS))
    filt = ''.join(f'<button onClick="[[ f{i} ]]" aria-pressed="[[ fOn{i} ]]" class="press" style="height: 44px; padding: 0 16px; border-radius: 999px; background: [[ fBg{i} ]]; color: [[ fFg{i} ]]; box-shadow: inset 0 0 0 1px [[ fBd{i} ]]; font-size: 14px; font-weight: 600">{n}</button>' for i, n in enumerate(['All', 'Saving', 'Borrowing', 'Business']))
    seg = ''.join(f'<button onClick="[[ s{i} ]]" aria-pressed="[[ sOn{i} ]]" style="flex: 1 1 0; height: 40px; border-radius: 999px; background: [[ sBg{i} ]]; color: [[ sFg{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{n}</button>' for i, n in enumerate(['Week', 'Month', 'Year']))
    switches = ''.join(f'''<div style="min-height: 52px; display: flex; align-items: center; gap: 12px; {'border-bottom: 1px solid #EEF2EF;' if i == 0 else ''}">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span class="knote">{d}</span></span>
          <button role="switch" aria-checked="[[ sw{i} ]]" aria-label="{t}" onClick="[[ toggle{i} ]]" style="width: 60px; height: 44px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="width: 52px; height: 32px; border-radius: 999px; background: [[ swBg{i} ]]; position: relative; transition: background-color .18s"><span style="position: absolute; top: 3px; left: 3px; width: 26px; height: 26px; border-radius: 999px; background: #FFFFFF; box-shadow: 0 1px 3px rgba(16,24,20,.25); transform: translateX([[ swX{i} ]]px); transition: transform .18s cubic-bezier(.2,.8,.2,1)"></span></span></button>
        </div>''' for i, (t, d) in enumerate([('Check-in reminders', 'The day before, at 18:00'), ('Circle cheers', 'When someone cheers your step')]))
    radios = ''.join(f'''<button onClick="[[ r{i} ]]" aria-pressed="[[ rOn{i} ]]" style="min-height: 56px; padding: 10px 16px; border-radius: 18px; background: {MIST}; box-shadow: inset 0 0 0 [[ rBw{i} ]]px {EVG}; display: flex; align-items: center; gap: 12px; text-align: left; font-size: 15px; font-weight: 500">
          <span style="flex-grow: 1">{o}</span><span aria-hidden="true" style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 99px; border: 2px solid [[ rC{i} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 10px; height: 10px; border-radius: 99px; background: [[ rF{i} ]]"></span></span></button>''' for i, o in enumerate(["I'd cover it from savings", "I'd borrow from family or friends"]))
    st4 = stones(150, 34, [(16, 24, 14, 7), (54, 18, 16, 8), (96, 13, 16, 8), (134, 8, 13, 6.5)], [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='4 4')
    col1 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">Buttons</span>
        <button class="pill press" style="height: 56px; background: {EVG}; color: #FFFFFF">Start my check-in</button>
        <button class="pill press" style="height: 52px; background: transparent; box-shadow: inset 0 0 0 1px #C9D3CE">Just look around</button>
        <div style="display: flex; align-items: center; gap: 12px"><button class="press" style="height: 44px; padding: 0 8px; font-size: 15px; font-weight: 600; color: {EVG}">Remind me tomorrow</button><button class="press" aria-label="Send" style="width: 44px; height: 44px; border-radius: 999px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center">{icon('send', 18, EVG)}</button><button disabled style="height: 44px; padding: 0 18px; border-radius: 999px; background: #DCE4DF; color: {MUTED}; font-size: 15px; font-weight: 600">Continue</button></div>
        <div style="border-radius: 20px; background: {NIGHT}; padding: 16px; display: flex; flex-direction: column; gap: 10px"><button class="pill press" style="height: 52px; background: {LIME}; color: {INK}">Start the lesson</button><button class="pill press" style="height: 48px; background: transparent; color: {MOON}; box-shadow: inset 0 0 0 1px {NLINE}">Save for later</button></div>
        <span class="knote">One main button per screen: evergreen on light, lime on dark. Press gives a 90 ms squeeze.</span>
      </section>
      <section class="card">
        <span class="ktitle">Tab bar: the shapes teach the areas</span>
        <nav aria-label="Demo tab bar" style="height: 64px; border-radius: 20px; background: {MIST}; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); align-items: center; color: {MUTED}">{tabs}</nav>
        <span class="knote">Home is the pool, Learn the moon, Vault the arch, Community the ripple, Me the stones. The active pill takes the area's colour.</span>
      </section>
      <section class="card">
        <span class="ktitle">Labels that say where things come from</span>
        <div style="display: flex; flex-wrap: wrap; gap: 8px">{sample_chip()}<span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">AI-assisted</span><span class="chip" style="background: {EVG}; color: #FFFFFF">{icon('check', 14, '#FFFFFF', 2.6)}Reviewed by AWO</span><span class="chip" style="background: {MIST}; color: {SEC}">Evidence: early</span><span class="chip" style="background: {BLUSH}; color: {BLUSH_INK}">Member story</span><span class="chip" style="background: {POOL}; color: {EVG}">{icon('lock', 14, EVG)}Stored in South Africa</span></div>
        <span class="knote">"Reviewed by AWO" only appears on content from the governed library. Everything in these rounds is marked Sample.</span>
      </section>
    </div>'''
    col2 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">Inputs and choices</span>
        <label style="height: 48px; border-radius: 999px; background: {MIST}; display: flex; align-items: center; gap: 10px; padding: 0 16px; color: {MUTED}">{icon('search', 20, MUTED)}<input placeholder="Search money words" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; background: transparent; font-size: 15px; color: {INK}"></label>
        <div role="group" aria-label="Filter" style="display: flex; flex-wrap: wrap; gap: 8px">{filt}</div>
        <div role="group" aria-label="Period" style="display: flex; gap: 4px; padding: 4px; border-radius: 999px; background: {MIST}">{seg}</div>
        <div style="display: flex; flex-direction: column; gap: 8px">{radios}</div>
        <div style="display: flex; flex-direction: column">{switches}</div>
      </section>
      <section class="card">
        <span class="ktitle">Feedback</span>
        <div style="position: relative; height: 56px">
          <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div role="status" style="position: absolute; inset: 0; border-radius: 999px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 8px 0 16px; font-size: 15px; animation: rise .28s cubic-bezier(.2,.8,.2,1) both"><span style="width: 26px; height: 26px; border-radius: 99px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 14, EVG, 3)}</span><span style="flex-grow: 1">Saved. Your check-in is in.</span><button onClick="[[ hideToast ]]" style="height: 44px; padding: 0 12px; font-weight: 600; color: {LIME}">Undo</button></div></sc-if>
          <sc-if value="[[ noToast ]]" hint-placeholder-val="[[ true ]]"><button class="pill press" onClick="[[ showToast ]]" style="height: 56px; background: {MIST}">Show a confirmation</button></sc-if>
        </div>
        <div style="border-radius: 999px; background: {INK}; color: {MOON}; padding: 10px 16px; display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 500"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M2 8.8a15 15 0 0 1 4.2-2.6M9.8 5.2A15 15 0 0 1 22 8.8M8.5 16.4a5 5 0 0 1 7 0M12 20h.01M3 3l18 18"></path></svg>You're offline. Your lesson is saved on this phone.</div>
        <div style="display: flex; flex-direction: column; gap: 10px" aria-label="Loading" role="img"><div style="display: flex; gap: 12px; align-items: center"><span class="sk" style="width: 38px; height: 38px; border-radius: 99px"></span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span class="sk" style="height: 12px; width: 70%"></span><span class="sk" style="height: 10px; width: 45%"></span></span></div><div style="display: flex; gap: 12px; align-items: center"><span class="sk" style="width: 38px; height: 38px; border-radius: 99px"></span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span class="sk" style="height: 12px; width: 60%"></span><span class="sk" style="height: 10px; width: 35%"></span></span></div></div>
        <div style="border-radius: 20px; background: {MIST}; padding: 16px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 15px; font-weight: 600">Nothing here yet, and that's fine.</span><span class="knote">Empty states say what comes first, never what's missing.</span></div>
      </section>
    </div>'''
    col3 = f'''<div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card">
        <span class="ktitle">The shapes, working</span>
        <div style="display: flex; gap: 20px; align-items: center">
          <div style="position: relative; width: 64px; height: 120px; flex-shrink: 0">{pool(64, 120, 'kPool', rimw=2.5)}<sc-if value="[[ moved ]]" hint-placeholder-val="[[ false ]]"><span class="splash" style="left: 6px; top: [[ splashY ]]px; width: 52px; height: 12px"></span></sc-if></div>
          <div style="display: flex; flex-direction: column; gap: 8px"><span class="d" style="font-size: 40px; color: {EVG}; font-variant-numeric: tabular-nums">[[ amountText ]]</span><span class="knote">of R 5 000. The pool only ever means money she's building.</span><button class="press" onClick="[[ move ]]" style="align-self: flex-start; height: 44px; padding: 0 16px; border-radius: 999px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">[[ moveLabel ]]</button></div>
        </div>
        <div style="height: 1px; background: #EEF2EF"></div>
        <div style="display: flex; align-items: center; gap: 16px"><div style="border-radius: 16px; background: {NIGHT}; padding: 10px 12px; display: flex; gap: 8px" role="img" aria-label="Lesson 3 of 6">{moon(22, 'full')}{moon(22, 'full')}{moon(22, 'half', now=True)}{moon(22, 'new')}{moon(22, 'new')}{moon(22, 'new')}</div><span class="knote">Moons wax as lessons go on.</span></div>
        <div style="display: flex; align-items: center; gap: 16px"><span role="img" aria-label="Stage 2 of 4">{st4}</span><span class="knote">Stones: where she stands.</span></div>
        <div style="display: flex; align-items: center; gap: 16px"><div role="img" aria-label="Readiness 63" style="position: relative; width: 96px; height: 90px">{arc(96, 63, '#DCE4DF', EVG, sw=8)}<span class="d" style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 30px; padding-top: 4px">63</span></div><span class="knote">One readiness arc, never rings. Not a credit score.</span></div>
      </section>
      <section class="card">
        <span class="ktitle">People</span>
        <div style="display: flex; gap: 14px; align-items: flex-start">
          <span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="position: relative; width: 58px; height: 58px"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid #F29BB5"></span><img class="face" src="{IMG['wanjiru']}" alt="" style="position: absolute; left: 5px; top: 5px; width: 48px; height: 48px"></span><span style="font-size: 12px">New win</span></span>
          <span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="position: relative; width: 58px; height: 58px"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid #C9D3CE"></span><img class="face" src="{IMG['amara']}" alt="" style="position: absolute; left: 5px; top: 5px; width: 48px; height: 48px"></span><span style="font-size: 12px">Seen</span></span>
          <span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="width: 58px; height: 58px; box-sizing: border-box; border-radius: 999px; border: 2px dashed {EVG}; color: {EVG}; display: flex; align-items: center; justify-content: center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg></span><span style="font-size: 12px">Your win</span></span>
        </div>
        <div style="display: flex; gap: 8px; align-items: flex-start"><img class="face" src="{IMG['thandi']}" alt="" style="width: 30px; height: 30px"><span style="padding: 9px 13px; border-radius: 6px 16px 16px 16px; background: {BLUSH}; color: {BLUSH_INK}; font-size: 14px; line-height: 1.4"><strong>Thandi</strong> A second pair of work shoes. The first pair is fine.</span></div>
        <div style="display: flex; align-items: center; gap: 12px"><img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px"><span style="flex-grow: 1; font-size: 15px; font-weight: 600">Wanjiru</span>
          <button onClick="[[ doCheer ]]" aria-pressed="[[ cheered ]]" class="press" style="position: relative; height: 44px; padding: 0 14px; border-radius: 999px; background: [[ cheerBg ]]; color: [[ cheerFg ]]; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s"><sc-if value="[[ cheered ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span></sc-if>{icon('ripple', 18)}[[ cheerLabel ]]<span style="font-weight: 500; opacity: .75">[[ cheerCount ]]</span></button></div>
        <span class="knote">Blush is only for people: faces, their words, cheers.</span>
      </section>
      <section class="card">
        <span class="ktitle">Rows and steps</span>
        <div style="display: flex; align-items: center; gap: 12px">{dot(LIME, icon('arch', 18, EVG))}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Word of the week: Stokvel</span><span class="knote">Tap to learn it</span></span>{icon('chev', 18, MUTED)}</div>
        <div style="display: flex; align-items: center; gap: 12px"><span style="position: relative; width: 44px; height: 44px"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="18" fill="none" stroke="#E4ECE7" stroke-width="5"></circle><circle cx="22" cy="22" r="18" fill="none" stroke="{EVG}" stroke-width="5" stroke-linecap="round" pathLength="100" style="stroke-dasharray: [[ stepDash ]] 100; transform: rotate(-90deg); transform-origin: center; transition: stroke-dasharray .6s cubic-bezier(.2,.8,.2,1)"></circle></svg><span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700">[[ stepCount ]]</span></span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span class="knote">This week's step</span><span style="font-size: 15px; font-weight: 600">Build a starter safety net</span></span><button onClick="[[ stepToggle ]]" aria-label="Mark the next part done" class="press" style="width: 44px; height: 44px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 18, EVG, 2.6)}</button></div>
      </section>
    </div>'''
    body = f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; align-items: start">{col1}{col2}{col3}</div>'
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const tab = st.tab || 0, f = st.f || 0, s = st.s || 0, r = st.r == null ? 1 : st.r;
    const sw = st.sw || [true, false];
    const moved = !!st.moved, cheered = !!st.cheered, toast = !!st.toast, step = !!st.step;
    const amount = moved ? 1900 : 1800;
    const act = %(act)s;
    const v = {
      moved, amountText: 'R ' + String(amount).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' '),
      waterY: Math.round(120 * (1 - amount / 5000)), splashY: Math.round(120 * (1 - amount / 5000)) - 6,
      poolLabel: 'Safety net R ' + amount + ' of R 5 000',
      move: () => this.setState({ moved: !moved }), moveLabel: moved ? 'Undo' : 'I moved R 100',
      cheered, doCheer: () => this.setState({ cheered: !cheered }), cheerLabel: cheered ? 'Cheered' : 'Cheer', cheerCount: cheered ? 25 : 24,
      cheerBg: cheered ? '%(bi)s' : '%(b)s', cheerFg: cheered ? '%(b)s' : '%(bi)s',
      toast, noToast: !toast, showToast: () => this.setState({ toast: true }), hideToast: () => this.setState({ toast: false }),
      stepDash: step ? 100 : 50, stepCount: step ? '2/2' : '1/2', stepToggle: () => this.setState({ step: !step })
    };
    for (let i = 0; i < 5; i++) {
      v['tab' + i] = () => this.setState({ tab: i }); v['tabOn' + i] = tab === i;
      v['tabBg' + i] = tab === i ? act[i][0] : 'transparent'; v['tabFg' + i] = tab === i ? act[i][1] : '%(mut)s';
      v['tabLc' + i] = tab === i ? act[i][2] : '%(mut)s'; v['tabW' + i] = tab === i ? 600 : 400;
    }
    for (let i = 0; i < 4; i++) {
      v['f' + i] = () => this.setState({ f: i }); v['fOn' + i] = f === i;
      v['fBg' + i] = f === i ? '%(evg)s' : '#FFFFFF'; v['fFg' + i] = f === i ? '#FFFFFF' : '%(ink)s'; v['fBd' + i] = f === i ? '%(evg)s' : '#DCE4DF';
    }
    for (let i = 0; i < 3; i++) {
      v['s' + i] = () => this.setState({ s: i }); v['sOn' + i] = s === i;
      v['sBg' + i] = s === i ? '#FFFFFF' : 'transparent'; v['sFg' + i] = s === i ? '%(ink)s' : '%(mut)s';
    }
    for (let i = 0; i < 2; i++) {
      v['r' + i] = () => this.setState({ r: i }); v['rOn' + i] = r === i; v['rBw' + i] = r === i ? 2 : 0;
      v['rC' + i] = r === i ? '%(evg)s' : '#A9B6AF'; v['rF' + i] = r === i ? '%(evg)s' : 'transparent';
      v['sw' + i] = !!sw[i]; v['swBg' + i] = sw[i] ? '%(evg)s' : '#C9D3CE'; v['swX' + i] = sw[i] ? 20 : 0;
      v['toggle' + i] = () => { const n = sw.slice(); n[i] = !n[i]; this.setState({ sw: n }); };
    }
    return v;
  }
}''' % dict(act=[list(ACTIVE[n]) for n, _ in AREAS], bi=BLUSH_INK, b=BLUSH, evg=EVG, ink=INK, mut=MUTED)
    return kit_board('Components', 'Everything the Round 6 screens are built from, at Volume 1. Each part has one job, and the ones that move, move for a reason.', body, logic, 1440, 1300)


def widgets():
    # Lock screen: a real photo, the time as the photo's own caption, three widget sizes and two notifications.
    ring = f'''<span style="position: relative; width: 64px; height: 64px; border-radius: 999px; background: rgba(16,24,20,.45); display: flex; align-items: center; justify-content: center"><svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true" style="position: absolute; inset: 0"><circle cx="32" cy="32" r="26" fill="none" stroke="rgba(255,255,255,.3)" stroke-width="5"></circle><circle cx="32" cy="32" r="26" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" pathLength="100" style="stroke-dasharray: 40 100; transform: rotate(-90deg); transform-origin: center"></circle></svg><span style="display: flex; flex-direction: column; align-items: center; line-height: 1"><span class="d" style="font-size: 22px">12</span><span style="font-size: 12px">of 30</span></span></span>'''
    notif = lambda lead, title, text, when: f'''<div style="border-radius: 22px; background: rgba(244,248,245,.9); color: {INK}; padding: 12px 14px; display: flex; gap: 12px; align-items: flex-start">{lead}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">{title}</span><span style="font-size: 12px; color: {MUTED}">{when}</span></span><span style="font-size: 14px; line-height: 1.35">{text}</span></span></div>'''
    appicon = f'<span aria-hidden="true" style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 10px; background: {EVG}; display: flex; align-items: center; justify-content: center"><span class="d" style="font-size: 16px; color: {LIME}">awo</span></span>'
    lock = f'''<div class="ph" style="background: {INK}">
      <img src="{IMG['naledi_cafe']}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 42% 30%">
      <span aria-hidden="true" style="position: absolute; inset: 0; background: rgba(11,15,14,.35)"></span>
      <div style="position: absolute; left: 24px; right: 24px; top: 70px; color: #FFFFFF; display: flex; flex-direction: column; align-items: center; gap: 4px">
        <span style="font-size: 16px; font-weight: 500">Friday 25 September</span>
        <span class="d" style="font-size: 96px; font-stretch: 90%">07:30</span>
        <div style="display: flex; gap: 12px; margin-top: 12px; align-items: center">{ring}
          <span style="height: 64px; padding: 0 14px; border-radius: 20px; background: rgba(16,24,20,.45); display: flex; flex-direction: column; justify-content: center; gap: 2px"><span style="font-size: 12px; opacity: .85">Next lesson, 3 minutes</span><span style="font-size: 15px; font-weight: 600">Savings groups</span></span></div>
        <span style="font-size: 14px; margin-top: 6px">Check-in on 13 October</span>
      </div>
      <div style="position: absolute; left: 12px; right: 12px; bottom: 40px; display: flex; flex-direction: column; gap: 8px">
        {notif(f'<img class="face" src="{IMG["wanjiru"]}" alt="" style="width: 36px; height: 36px">', 'Wanjiru cheered you', 'Your step this week: done. Proud of you!', 'now')}
        {notif(appicon, 'AWO', "It's payday. Your one step is waiting, and it takes a minute.", '07:00')}
      </div>
    </div>'''
    tile = lambda w, h, bg, fg, inner: f'<div style="width: {w}px; height: {h}px; box-sizing: border-box; border-radius: 26px; background: {bg}; color: {fg}; padding: 14px; display: flex; flex-direction: column; gap: 6px; overflow: hidden; position: relative">{inner}</div>'
    small_pool = tile(164, 164, EVG, '#FFFFFF', f'<span style="font-size: 12px; color: {ON_EVG}">Safety net</span><div style="display: flex; align-items: flex-end; gap: 12px; flex-grow: 1">{pool(40, 90, "wPool", rimw=2, static=True, hole="wY", label="wLabel")}<span style="display: flex; flex-direction: column"><span class="d" style="font-size: 26px; color: {LIME}">R 1 800</span><span style="font-size: 12px; color: {ON_EVG}">of R 5 000</span></span></div>')
    small_word = tile(164, 164, LIME, EVG, f'<span style="display: flex; justify-content: space-between"><span style="font-size: 12px; font-weight: 600">Word of the week</span>{icon("arch", 18, EVG)}</span><span class="d" style="font-size: 32px; margin-top: auto">Stokvel</span><span style="font-size: 12px; color: {INK}">A savings group that takes turns</span>')
    medium = tile(344, 164, '#FFFFFF', INK, f'''<span style="font-size: 12px; color: {MUTED}">This week's step</span><span class="d" style="font-size: 28px">Build a starter safety net</span>
        <div style="margin-top: auto; display: flex; gap: 8px"><span style="flex-grow: 1; height: 40px; border-radius: 12px; background: {MIST}; display: flex; align-items: center; gap: 8px; padding: 0 10px; font-size: 13px"><span style="width: 18px; height: 18px; border-radius: 99px; background: {EVG}; display: flex; align-items: center; justify-content: center">{icon("check", 11, "#FFFFFF", 3)}</span>Lesson</span><span style="flex-grow: 1; height: 40px; border-radius: 12px; background: {MIST}; display: flex; align-items: center; gap: 8px; padding: 0 10px; font-size: 13px"><span style="width: 18px; height: 18px; box-sizing: border-box; border-radius: 99px; border: 2px solid #A9B6AF"></span>Your amount</span></div>''')
    faces = ''.join(f'<span style="position: relative; width: 46px; height: 46px"><span style="position: absolute; inset: 0; border-radius: 999px; border: 2px solid #F29BB5"></span><img class="face" src="{IMG[k]}" alt="" style="position: absolute; left: 4px; top: 4px; width: 38px; height: 38px"></span>' for k in ('wanjiru', 'amara', 'thandi', 'grace'))
    large = tile(344, 344, MIST, INK, f'''<span style="display: flex; justify-content: space-between; align-items: center"><span class="d" style="font-size: 26px">Hey Naledi</span><span style="font-size: 12px; color: {MUTED}">Payday</span></span>
        <span style="font-size: 12px; font-weight: 600">Wins this week</span><div style="display: flex; gap: 8px">{faces}</div>
        <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 6px; flex-grow: 1">
          <div style="border-radius: 18px; background: {EVG}; color: #FFFFFF; padding: 12px; display: flex; flex-direction: column; justify-content: space-between"><span style="font-size: 12px; color: {ON_EVG}">Safety net</span><span class="d" style="font-size: 26px; color: {LIME}">R 1 800</span></div>
          <div style="border-radius: 18px; background: {NIGHT}; color: {MOON}; padding: 12px; display: flex; flex-direction: column; justify-content: space-between">{moon(22, 'half', dark='#3A4541')}<span style="font-size: 13px; font-weight: 600">Savings groups, 3 min</span></div>
        </div>''')
    home_phone = f'''<div class="ph" style="background: {POOL}">
      <div style="position: absolute; left: 21px; top: 72px; display: grid; grid-template-columns: repeat(2, 164px); gap: 16px">{small_pool}{small_word}<div style="grid-column: span 2">{medium}</div><div style="grid-column: span 2">{large}</div></div>
    </div>'''
    specimens = f'''<div style="display: flex; flex-direction: column; gap: 20px; flex-grow: 1">
      <section class="card"><span class="ktitle">Sizes</span><span class="knote">Small (2 by 2): one number or one word. Medium (4 by 2): this week's step. Large (4 by 4): a pocket Home. Each widget wears the colour of the area it opens.</span></section>
      <section class="card"><span class="ktitle">Lock screen</span><span class="knote">A ring for the 30-day plan, the next lesson and the check-in date. No amounts on the lock screen: anyone can see it.</span></section>
      <section class="card"><span class="ktitle">Notifications</span><span class="knote">A person first, then a single step. Never guilt, never a streak. At most one a day, and quiet hours are on by default.</span>
        {notif(dot(BLUSH, icon('ripple', 18, BLUSH_INK), 36), 'Circle', 'Grace left a voice note for the safety net circle.', '2h')}
        {notif(dot(POOL, icon('stones', 18, EVG), 36), 'Your check-in', 'Two minutes whenever you are ready. Last month stays exactly as it was.', 'Tue')}
      </section>
    </div>'''
    body = f'<div style="display: flex; gap: 40px; align-items: flex-start"><div style="display: flex; flex-direction: column; gap: 14px"><span style="font-size: 16px; font-weight: 600">Lock screen</span>{lock}</div><div style="display: flex; flex-direction: column; gap: 14px"><span style="font-size: 16px; font-weight: 600">Home screen</span>{home_phone}</div>{specimens}</div>'
    logic = '''class Component extends DCLogic {
  renderVals() { return { wY: Math.round(90 * (1 - 1800 / 5000)), wLabel: 'Safety net R 1 800 of R 5 000' }; }
}'''
    return kit_board('Widgets and notifications', 'AWO outside the app: one glance, one step, and no amounts where others can see them.', body, logic, 1760, 1110, chip='Sample content')


if __name__ == '__main__':
    out = sys.argv[1]
    write(os.path.join(out, 'R6-Components.dc.html'), components())
    write(os.path.join(out, 'R6-Widgets.dc.html'), widgets())
