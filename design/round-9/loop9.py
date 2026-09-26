"""Round 9, batch 1: the 30-day loop as one flow, sharing to WhatsApp, help and one search.

The loop: a reminder on the lock screen (or in the notification centre), the check-in (Round 7's), the new version
and what changed, this month's one step, a milestone, and sharing it. Every screen here links to the next.
Rules the flow tests: no amounts on the lock screen or on anything shared; results never get a burst (showing up
does); a month that goes down is explained, not hidden; old versions never change."""
import json

from lib9 import *  # noqa: F401,F403
from marketing7 import H, K, hand_hole  # noqa: E402

BAL = 'text-wrap: balance'


def js(o):
    return json.dumps(o, ensure_ascii=False)


# ---------------------------------------------------------------- 1. The reminder, on the lock screen

def lock_reminder():
    act = lambda hole, label, primary=False: (
        f'<button onClick="[[ {hole} ]]" style="flex: 1 1 0; height: 44px; border-radius: {R_M}px; '
        f'background: {EVG if primary else "rgba(16,24,20,.08)"}; color: {"#FFFFFF" if primary else INK}; font-size: 14px; font-weight: 600">{label}</button>')
    inner = f'''  <img src="{IMG['naledi_cafe']}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 42% 30%">
  <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(11,15,14,.55), rgba(11,15,14,.2) 40%, rgba(11,15,14,.6))"></span>
  <div style="position: absolute; left: 24px; right: 24px; top: 64px; color: #FFFFFF; display: flex; flex-direction: column; align-items: center; gap: 2px">
    <span style="font-size: 16px; font-weight: 500">Tuesday 13 October</span>
    <span class="d" style="font-size: 96px">07:30</span>
  </div>
  <div style="position: absolute; left: 12px; right: 12px; bottom: 56px; display: flex; flex-direction: column; gap: 8px">
    <div style="border-radius: 22px; background: rgba(244,248,245,.94); color: {INK}; box-shadow: 0 10px 30px rgba(0,0,0,.2); overflow: hidden">
      <button onClick="[[ toggle ]]" aria-expanded="[[ open ]]" style="width: 100%; padding: 14px; display: flex; gap: 12px; align-items: flex-start; text-align: left">
        {app_badge(36)}
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 14px; font-weight: 600">AWO</span><span style="font-size: 12px; color: {MUTED}">now</span></span>
          <span style="font-size: 15px; font-weight: 600">Your check-in is ready</span>
          <span style="font-size: 14px; line-height: 1.35; color: {SEC}">Three questions, about two minutes. Your last one was on 13 September.</span></span>
        <span style="width: 24px; height: 24px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; transform: rotate([[ chevRot ]]deg); transition: transform .2s">{icon('chev', 16, MUTED)}</span>
      </button>
      <sc-if value="[[ open ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; gap: 6px; padding: 0 14px 14px; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">
        <a href="R7-Checkin.dc.html" style="flex: 1.3 1 0; height: 44px; border-radius: {R_M}px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center">Start</a>
        {act('later', 'Tonight')}{act('skip', 'Skip a month')}
      </div></sc-if>
    </div>
    <div style="border-radius: 22px; background: rgba(244,248,245,.94); color: {INK}; padding: 12px 14px; display: flex; gap: 12px; align-items: flex-start">
      <img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between"><span style="font-size: 14px; font-weight: 600">Wanjiru cheered your step</span><span style="font-size: 12px; color: {MUTED}">07:12</span></span>
        <span style="font-size: 14px; line-height: 1.35">Proud of you!</span></span>
    </div>
  </div>
  <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div class="toast" style="bottom: 250px">{icon('check', 18, LIME, 2.6)}<span>[[ toastText ]]</span></div></sc-if>
  <span style="position: absolute; left: 0; right: 0; bottom: 20px; text-align: center; font-size: 13px; color: rgba(255,255,255,.85)">Swipe up to open</span>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const open = st.open == null ? true : st.open;
    const say = (t) => this.setState({ toast: t, open: false });
    return {
      open, chevRot: open ? 90 : 0, toggle: () => this.setState({ open: !open }),
      later: () => say("We'll remind you at 19:00 tonight."),
      skip: () => say('Skipped. Your next reminder is on 12 November. Nothing is lost.'),
      toast: !!st.toast, toastText: st.toast || ''
    };
  }
}'''
    return free_page('Reminder, on the lock screen', inner, logic, h=844, bg=INK)


# ---------------------------------------------------------------- 2. The notification centre

NOTES = [  # key, when, kind (money or circles), area or face, title, text, time, href, unread, primary
    ('checkin', 'Today', 'money', 'Me', 'Your check-in is ready', 'Three questions, about two minutes. Your last one was on 13 September.', '07:30', 'R7-Checkin.dc.html', True, True),
    ('cheer', 'Today', 'circles', 'face:wanjiru', 'Wanjiru cheered your step', '"Proud of you!" on Build a starter safety net', '07:12', 'R8-Feed.dc.html', True, False),
    ('replies', 'This week', 'circles', 'Community', '3 replies to your question', 'In Safety net circle: "Where do you keep your safety net?"', 'Mon', 'R8-Post.dc.html', True, False),
    ('word', 'This week', 'money', 'Words', 'Word of the week: Dividend', "A share of a company's profit. Two minutes in Words.", 'Mon', 'R8-Words-Decoder.dc.html', False, False),
    ('podcast', 'This week', 'money', 'Learn', 'New on the AWO Podcast', 'Closing a shop, and opening a better one. With Amara.', 'Sun', 'R8-Podcast.dc.html', False, False),
    ('payday', 'Earlier', 'money', 'Hub', "October's pay-day plan is ready", "September's split, carried over. Check it before payday.", '25 Sep', 'R8-Tool-Payday.dc.html', False, False),
    ('method', 'Earlier', 'money', 'Help', 'How your DIVA score is worked out has changed', "Scoring v1.4 applies from your next check-in. Your past versions don't change.", '20 Sep', 'R9-Help.dc.html', False, False),
]
FILTERS = ['All', 'Your money', 'Circles']


def notifications():
    groups = []
    for g in ('Today', 'This week', 'Earlier'):
        idx = [i for i, n in enumerate(NOTES) if n[1] == g]
        rows = ''
        for i in idx:
            key, _w, kind, who, t, text, time, href, _u, prim = NOTES[i]
            lead = (f'<img class="face" src="{IMG[who[5:]]}" alt="" style="width: 40px; height: 40px">' if who.startswith('face:') else area_badge(who, 40))
            dot = f'<sc-if value="[[ un{i} ]]" hint-placeholder-val="[[ true ]]"><span aria-label="New" style="width: 10px; height: 10px; border-radius: 999px; background: {EVG}; flex-shrink: 0; margin-top: 6px"></span></sc-if>'
            if prim:
                rows += f'''<sc-if value="[[ show{i} ]]" hint-placeholder-val="[[ true ]]"><section style="border-radius: {R_L}px; background: {EVG}; color: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
            <span style="display: flex; gap: 12px; align-items: flex-start"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: {R_M}px; background: {POOL}; display: flex; align-items: center; justify-content: center">{icon('stones', 22, EVG)}</span>
              <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 12px; color: {ON_EVG}">{time}</span></span><span style="font-size: 14px; line-height: 1.4; color: {ON_EVG}">{text}</span></span></span>
            <span style="display: flex; gap: 8px"><a href="{href}" onClick="[[ read{i} ]]" style="flex: 1 1 0; height: 48px; border-radius: {R_M}px; background: {LIME}; color: {EVG}; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">Start the check-in</a>
              <button onClick="[[ read{i} ]]" style="height: 48px; padding: 0 14px; border-radius: {R_M}px; background: rgba(255,255,255,.12); color: #FFFFFF; font-size: 14px; font-weight: 600">Later</button></span>
          </section></sc-if>'''
            else:
                rows += f'''<sc-if value="[[ show{i} ]]" hint-placeholder-val="[[ true ]]"><a href="{href}" onClick="[[ read{i} ]]" style="padding: 12px 0; display: flex; gap: 12px; align-items: flex-start; border-top: 1px solid {LINE7}">
            {lead}<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 15px; font-weight: [[ fw{i} ]]">{t}</span><span style="font-size: 12px; color: {MUTED}; white-space: nowrap">{time}</span></span>
              <span style="font-size: 14px; line-height: 1.4; color: {SEC}">{text}</span></span>{dot}</a></sc-if>'''
        groups.append(f'<sc-if value="[[ g{g[:2]} ]]" hint-placeholder-val="[[ true ]]"><section style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px; font-weight: 600; color: {MUTED}; padding: 4px 0">{g}</span>{rows}</section></sc-if>')
    segs = ''.join(f'<button onClick="[[ f{j} ]]" aria-pressed="[[ fOn{j} ]]" style="background: [[ fBg{j} ]]; color: [[ fFg{j} ]]">{f}</button>' for j, f in enumerate(FILTERS))
    body = f'''    {head9('R8-Home.dc.html', 'Notifications', icon_btn('gear', 'Notification settings', href='R7-Settings.dc.html'))}
    <div role="group" aria-label="Show" class="seg9">{segs}</div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin: -6px 0 -8px"><span style="font-size: 14px; color: {SEC}">[[ newText ]]</span>
      <button onClick="[[ readAll ]]" aria-disabled="[[ noneNew ]]" style="min-height: 44px; padding: 0 2px; font-size: 14px; font-weight: 600; color: [[ readAllCol ]]">Mark all read</button></div>
    {''.join(groups)}
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 16px; display: flex; gap: 12px; align-items: center">{ic8('clock', 20, EVG)}
      <span style="flex-grow: 1; font-size: 14px; line-height: 1.4; color: {SEC}">Quiet hours, 21:00 to 07:00. Reminders wait until morning, and none show an amount on your lock screen.</span>
      <a href="R7-Settings.dc.html" style="min-height: 44px; display: flex; align-items: center; font-size: 14px; font-weight: 600; color: {EVG}">Change</a></section>'''
    kinds = [n[2] for n in NOTES]
    groups_of = [n[1][:2] for n in NOTES]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const f = st.f || 0, read = st.read || {};
    const kinds = %(kinds)s, gs = %(gs)s, unread0 = %(un)s;
    const vis = (i) => f === 0 || (f === 1 && kinds[i] === 'money') || (f === 2 && kinds[i] === 'circles');
    let n = 0;
    const v = { readAll: () => { const r = {}; kinds.forEach((_, i) => { r[i] = true; }); this.setState({ read: r }); } };
    kinds.forEach((_, i) => {
      const un = unread0[i] && !read[i];
      if (un && vis(i)) n++;
      v['show' + i] = vis(i); v['un' + i] = un; v['fw' + i] = un ? 600 : 500;
      v['read' + i] = () => this.setState({ read: Object.assign({}, read, { [i]: true }) });
    });
    ['To', 'Th', 'Ea'].forEach((g) => { v['g' + g] = kinds.some((_, i) => gs[i] === g && vis(i)); });
    v.newText = n ? n + (n === 1 ? ' new' : ' new') : "You're all caught up";
    v.noneNew = n === 0; v.readAllCol = n ? '%(evg)s' : '%(mut)s';
    for (let j = 0; j < 3; j++) { v['f' + j] = () => this.setState({ f: j }); v['fOn' + j] = f === j; v['fBg' + j] = f === j ? '#FFFFFF' : 'transparent'; v['fFg' + j] = f === j ? '%(ink)s' : '%(sec)s'; }
    return v;
  }
}''' % dict(kinds=js(kinds), gs=js(groups_of), un=js([n[8] for n in NOTES]), evg=EVG, mut=MUTED, ink=INK, sec=SEC)
    return page9('Notifications', body, logic, h=1270, tab='Home')


# ---------------------------------------------------------------- 3. The new version, and what changed

def what_changed():
    rows = ''
    for i, (name, dim, v3, v4, vd) in enumerate(AREAS9):
        rows += f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 0; {"border-top: 1px solid " + LINE7 + ";" if i else ""}">
          <span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{name}</span><span style="font-size: 12px; color: {MUTED}">{dim}</span></span>
            <span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 14px; color: {MUTED}; font-variant-numeric: tabular-nums">{v3} to <b style="color: {INK}; font-weight: 600">[[ n{i} ]]</b></span><span class="chip" style="height: 24px; min-width: 40px; justify-content: center; background: [[ dBg{i} ]]; color: [[ dFg{i} ]]">[[ d{i} ]]</span></span></span>
          <span aria-hidden="true" style="position: relative; height: 10px; border-radius: 2px; background: {LINE7}; overflow: hidden">
            <span style="position: absolute; left: 0; top: 0; bottom: 0; width: [[ w{i} ]]%; background: [[ barCol{i} ]]; transition: width .5s cubic-bezier(.2,.8,.2,1)"></span>
            <span style="position: absolute; top: -2px; bottom: -2px; left: {v3}%; width: 2px; background: {INK}; opacity: .55"></span>
          </span></div>'''
    months = ''.join(f'<button onClick="[[ m{j} ]]" aria-pressed="[[ mOn{j} ]]" style="background: [[ mBg{j} ]]; color: [[ mFg{j} ]]">{t}</button>' for j, t in enumerate(['A month that went up', 'A month that went down']))
    body = f'''    <header style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><a href="R7-Me.dc.html" aria-label="Close" style="width: 44px; height: 44px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('close', 20, INK, 2.2)}</a><span style="font-size: 15px; font-weight: 600; color: {SEC}">13 October, check-in 4</span>{sample_chip()}</header>
    <section style="border-radius: {R_L}px; background: {POOL}; color: {EVG}; padding: 20px 18px 18px; display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 15px; font-weight: 600">Version 4 of your DIVA profile</span>
      <span style="display: flex; align-items: flex-end; gap: 12px"><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; font-weight: 600">DIVA score</span><span class="d" style="font-size: 80px; font-variant-numeric: tabular-nums; animation: countUp .6s cubic-bezier(.2,.8,.2,1) .15s both">[[ score ]]</span></span>
        <span class="chip" style="height: 30px; margin-bottom: 12px; font-size: 14px; background: [[ scBg ]]; color: [[ scFg ]]">[[ scDelta ]]</span></span>
      <span style="font-size: 16px; line-height: 1.45; color: {INK}">[[ stageLine ]]</span>
      <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {SEC}; border-top: 1px solid rgba(15,74,54,.16); padding-top: 10px">{icon('lock', 14, SEC)}Version 3 is still there, exactly as it was. Versions never change.</span>
    </section>
    <section class="card8" style="gap: 10px">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 17px; font-weight: 600">What this means</span>{REVIEWED}</span>
      <p style="font-size: 16px; line-height: 1.5">[[ means ]]</p>
    </section>
    <section class="card8" style="gap: 0">
      <span style="display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 4px"><span style="font-size: 17px; font-weight: 600">What moved</span><span style="font-size: 13px; color: {MUTED}">September to October</span></span>
      {rows}
      <span style="display: flex; align-items: center; gap: 8px; font-size: 12px; color: {MUTED}; padding-top: 4px"><span style="width: 2px; height: 12px; background: {INK}; opacity: .55"></span>Where September was</span>
    </section>
    <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 14px 16px; display: flex; align-items: center; gap: 12px">{ic('shield', 22, EVG)}
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Evidence: building</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">3 of 4 check-ins included something you did, not only what you said. Kept apart from the score.</span></span></section>
    {primary("Choose this month's step", "R9-Next-Step.dc.html")}
    <a href="R7-Compare.dc.html" style="height: 48px; margin-top: -6px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1px #C9D3CE; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">Compare any two versions</a>
    <div style="border-top: 1px dashed #C9D3CE; padding-top: 14px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Design preview: the same screen after</span><div role="group" aria-label="Preview a month" class="seg9" style="background: #FFFFFF">{months}</div></div>'''
    up = [a[3] for a in AREAS9]
    down = [a[4] for a in AREAS9]
    v3 = [a[2] for a in AREAS9]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const m = st.m || 0, now = m ? %(down)s : %(up)s, was = %(v3)s;
    const score = m ? %(sd)d : %(s4)d, d = score - %(s3)d;
    const v = {
      score, scDelta: (d > 0 ? '+' : d < 0 ? '\\u2212' : '') + Math.abs(d) + ' since September',
      scBg: d >= 0 ? '%(lime)s' : '#DCE4DF', scFg: d >= 0 ? '%(evg)s' : '%(sec)s',
      stageLine: m ? 'Still stage 2 of 4. A month that goes down is part of it: nothing you learned is lost.' : 'Still stage 2 of 4. Stage 3 starts at 65.',
      means: m ? "Your safety net paid for the car repair. That's what it's for. Ready for surprises went from 48 to 40 while it refills; the rest held steady." : 'The number moved a little. The part you worked on moved most: ready for surprises went from 48 to 53, because your safety net grew.'
    };
    now.forEach((x, i) => {
      const dd = x - was[i];
      v['n' + i] = x; v['w' + i] = x;
      v['d' + i] = dd === 0 ? 'Same' : (dd > 0 ? '+' : '\\u2212') + Math.abs(dd);
      v['dBg' + i] = dd > 0 ? '%(lime)s' : '%(line)s'; v['dFg' + i] = dd > 0 ? '%(evg)s' : '%(sec)s';
      v['barCol' + i] = dd < 0 ? '#9FB0A8' : '%(evg)s';
    });
    for (let j = 0; j < 2; j++) { v['m' + j] = () => this.setState({ m: j }); v['mOn' + j] = m === j; v['mBg' + j] = m === j ? '%(evg)s' : 'transparent'; v['mFg' + j] = m === j ? '#FFFFFF' : '%(ink)s'; }
    return v;
  }
}''' % dict(up=js(up), down=js(down), v3=js(v3), sd=SCORE_DOWN, s4=SCORE_V4, s3=SCORE_V3, lime=LIME, evg=EVG, sec=SEC, ink=INK, line='#E4EAE6')
    return page9('What changed', body, logic, h=1420)


# ---------------------------------------------------------------- 4. This month's one step

STEPS9 = [('pool', LIME, 'Raise your payday move to R 150', 'R 50 more on payday. Your safety net refills faster after a surprise.', '5 min', 'Suggested'),
          ('moon', NIGHT, 'Learn where a safety net lives', 'A six-minute lesson: a separate pocket, a notice account, or a savings group.', '6 min', ''),
          ('doc', MIST, 'Name your next surprise', 'Write down one cost you can see coming this year, and roughly when.', '10 min', ''),
          ('check', POOL, "Keep September's step", 'R 100 on payday, the same as last month.', '5 min', '')]


def next_step():
    cards = ''
    for i, (g, bg, t, d, tm, tag) in enumerate(STEPS9):
        fg = MOON if bg == NIGHT else EVG
        glyph = icon(g, 22, fg) if g in ('pool', 'moon', 'check') else ic(g, 22, fg)
        tag_html = f'<span class="chip" style="height: 24px; background: {EVG}; color: #FFFFFF">{tag}</span>' if tag else ''
        cards += f'''<button onClick="[[ s{i} ]]" aria-pressed="[[ sOn{i} ]]" style="border-radius: {R_L}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ sBw{i} ]]px {EVG}; padding: 14px; display: flex; gap: 14px; align-items: flex-start; text-align: left; transition: box-shadow .18s">
          <span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: {R_M}px; background: {bg}; display: flex; align-items: center; justify-content: center">{glyph}</span>
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600">{t}</span><span style="font-size: 14px; line-height: 1.4; color: {MUTED}">{d}</span><span style="display: flex; gap: 6px; margin-top: 2px"><span class="chip" style="height: 24px; background: {MIST}; color: {SEC}">{tm}</span>{tag_html}</span></span>
          <span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; box-sizing: border-box; border-radius: 999px; border: 2px solid [[ sRc{i} ]]; display: flex; align-items: center; justify-content: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: [[ sRf{i} ]]"></span></span>
        </button>'''
    plan = [('This week', '[[ stepName ]]'), ('Next week', 'A lesson that goes with it'), ('Week 3', 'One small action, your size'), ('13 Nov', 'Check-in 5')]
    plan_html = ''.join(f'''<div style="display: flex; gap: 12px; align-items: flex-start">
          <span style="display: flex; flex-direction: column; align-items: center; align-self: stretch"><span style="width: 14px; height: 14px; border-radius: 999px; box-sizing: border-box; {f"background: {LIME}; border: 2px solid {EVG};" if i == 0 else f"border: 2px solid {EVG};" if i < 3 else f"border: 2px dashed {EVG};"}"></span>{'<span style="flex-grow: 1; width: 2px; background: #BFD9D2; margin: 2px 0"></span>' if i < 3 else ''}</span>
          <span style="display: flex; flex-direction: column; gap: 2px; padding-bottom: 10px; margin-top: -3px"><span style="font-size: 12px; color: {SEC}">{w}</span><span style="font-size: 15px; font-weight: 600">{t}</span></span></div>''' for i, (w, t) in enumerate(plan))
    body = f'''    {head9('R9-What-Changed.dc.html', "This month's step", sample_chip())}
    <sc-if value="[[ choosing ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 14px">
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 12px 14px; display: flex; align-items: center; gap: 12px"><span style="width: 32px; height: 32px; flex-shrink: 0; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon('check', 18, EVG, 2.8)}</span>
        <span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 13px; color: {MUTED}">September's step</span><span style="font-size: 15px; font-weight: 600">Build a starter safety net: you did it</span></span></section>
      {title('Pick one step for October.', 'Chosen for your focus, ready for surprises, from steps AWO has reviewed. One is enough.', 32)}
      <div role="radiogroup" aria-label="This month's step" style="display: flex; flex-direction: column; gap: 8px">{cards}</div>
      <section style="border-radius: {R_L}px; background: #FFFFFF; padding: 4px 6px 4px 16px; display: flex; align-items: center; gap: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Remind me on payday</span><span style="font-size: 13px; color: {MUTED}">Friday 30 October, 07:00</span></span>{switch(0, 'Remind me on payday')}</section>
      <section style="border-radius: {R_L}px; background: {POOL}; padding: 16px 16px 6px; display: flex; flex-direction: column; gap: 12px"><span style="font-size: 16px; font-weight: 600; color: {EVG}">Your next 30 days</span><div style="display: flex; flex-direction: column">{plan_html}</div></section>
      {primary('Start this step', hole='choose')}
    </div></sc-if>
    <sc-if value="[[ chosen ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; padding-top: 24px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
      <span style="width: 64px; height: 64px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 32, EVG, 2.8)}</span>
      {title("October's step is set.", None, 36)}
      <section class="card8"><span style="font-size: 13px; color: {MUTED}">Your step</span><span style="font-size: 18px; font-weight: 600">[[ stepName ]]</span><span style="font-size: 14px; color: {SEC}">[[ remindLine ]] It's on Home too.</span></section>
      <a href="R9-Milestone.dc.html" style="border-radius: {R_L}px; background: {BLUSH}; color: {BLUSH_INK}; padding: 16px; display: flex; align-items: center; gap: 14px">
        <span style="width: 56px; flex-shrink: 0">{stones_svg(4, 56, 40, new_last=True)}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 13px; font-weight: 600">A milestone</span><span style="font-size: 17px; font-weight: 600">Four check-ins in a row</span><span style="font-size: 13px">Share it, if you like. No amounts, ever.</span></span>{icon('chev', 18, BLUSH_INK)}</a>
      {primary('Back to Home', 'R8-Home.dc.html')}
      <button onClick="[[ change ]]" style="height: 48px; margin-top: -4px; border-radius: {R_M}px; font-size: 15px; font-weight: 600; color: {EVG}">Change the step</button>
    </div></sc-if>'''
    names = [s[2] for s in STEPS9]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const s = st.s == null ? 0 : st.s, names = %(names)s;
    const v = {
      stepName: names[s], choosing: !st.done, chosen: !!st.done,
      choose: () => this.setState({ done: true }), change: () => this.setState({ done: false })
    };
%(sw)s
    v.remindLine = v.sw0 ? "We'll remind you on payday, 30 October." : 'No reminder: you can add one on Home.';
    for (let i = 0; i < 4; i++) {
      v['s' + i] = () => this.setState({ s: i }); v['sOn' + i] = s === i; v['sBw' + i] = s === i ? 2 : 0;
      v['sRc' + i] = s === i ? '%(evg)s' : '#A9B6AF'; v['sRf' + i] = s === i ? '%(evg)s' : 'transparent';
    }
    return v;
  }
}''' % dict(names=js(names), evg=EVG, sw=switch_js(1, [True]))
    return page9("This month's step", body, logic, h=1290)


# ---------------------------------------------------------------- 5. A milestone, and sharing it

def milestone_card(scale, name_hole=True):
    """The milestone as it will be shared: 9:16, drawn at 1080 wide and scaled."""
    w, h = 1080, 1920
    name = '<span style="font-size: 44px; font-weight: 600; color: #0F4A36">[[ cardName ]]</span>' if name_hole else ''
    return f'''<div aria-hidden="true" style="width: {round(w * scale)}px; height: {round(h * scale)}px; flex-shrink: 0; border-radius: {max(6, round(40 * scale))}px; overflow: hidden; position: relative; box-shadow: 0 16px 40px rgba(16,24,20,.18)">
      <div style="position: absolute; left: 0; top: 0; width: {w}px; height: {h}px; transform: scale({scale}); transform-origin: 0 0; background: {POOL}; font-family: 'Geist', ui-sans-serif, system-ui, sans-serif">
        <div style="position: absolute; left: 90px; top: 110px">{lockup(52, EVG, LIME)}</div>
        <div style="position: absolute; left: 120px; right: 120px; top: 480px">{stones_svg(4, 840, 360, new_last=True)}</div>
        <div style="position: absolute; left: 90px; right: 90px; top: 1000px; display: flex; flex-direction: column; gap: 36px">
          <span style="{H(132, EVG, BAL)}">Four <span style="white-space: nowrap">check-ins</span> in a row.</span>
          <span class="hand" style="font-size: 88px; color: {EVG}; {HF}">Four months, kept.</span>
          {name}
        </div>
        <span style="position: absolute; left: 90px; right: 90px; bottom: 100px; font-size: 34px; line-height: 1.35; color: {SEC}">On AWO, milestones never show amounts.</span>
      </div></div>'''


def milestone_share():
    targets = [('circles', 'ripple', 'My circles'), ('status', 'whatsapp', 'WhatsApp status'), ('chat', 'whatsapp', 'WhatsApp chat'), ('save', 'download', 'Save image')]
    tbtn = ''.join(f'''<button onClick="[[ t_{k} ]]" style="flex: 1 1 0; min-height: 84px; border-radius: {R_M}px; background: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; font-size: 13px; font-weight: 600; line-height: 1.2; text-align: center; padding: 8px 4px">
        <span style="width: 40px; height: 40px; border-radius: 999px; background: {BLUSH if k == "circles" else (EVG if k in ("status", "chat") else MIST)}; color: {BLUSH_INK if k == "circles" else ("#FFFFFF" if k in ("status", "chat") else EVG)}; display: flex; align-items: center; justify-content: center">{icon(g, 20) if g == "ripple" else ic8(g, 20)}</span>{lbl}</button>''' for k, g, lbl in targets)
    inner = f'''  <div class="scr" style="bottom: 0; padding-bottom: 24px; gap: 16px">
    {head9('R9-Next-Step.dc.html', 'A milestone', sample_chip())}
    <div style="display: flex; gap: 16px; align-items: flex-start">
      {milestone_card(0.16)}
      <div style="display: flex; flex-direction: column; gap: 8px; padding-top: 6px">
        <span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.15">Four check-ins in a row</span>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}">You showed up four months running. That's the milestone: not the score.</span>
      </div>
    </div>
    <section class="card8" style="gap: 2px; padding: 6px 6px 6px 16px">
      <div class="row9"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Show my first name</span><span style="font-size: 13px; color: {MUTED}">Naledi</span></span>{switch(0, 'Show my first name')}</div>
      <div class="row9" style="border-top: 1px solid {LINE7}; padding-right: 10px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Amounts, score and stage</span><span style="font-size: 13px; color: {MUTED}">Never on anything you share</span></span>{icon('lock', 20, MUTED)}</div>
    </section>
    <span style="font-size: 15px; font-weight: 600; margin-bottom: -6px">Share it</span>
    <div style="display: flex; gap: 6px">{tbtn}</div>
    <a href="R8-Home.dc.html" style="height: 48px; border-radius: {R_M}px; font-size: 15px; font-weight: 600; color: {EVG}; display: flex; align-items: center; justify-content: center">Not now</a>
  </div>
  <sc-if value="[[ sheet ]]" hint-placeholder-val="[[ false ]]"><div class="dim" onClick="[[ close ]]"></div>
    <div class="sheet" role="dialog" aria-label="Post to WhatsApp status" style="padding: 10px 20px 28px; display: flex; flex-direction: column; gap: 14px">
      <span aria-hidden="true" style="align-self: center; width: 40px; height: 4px; border-radius: 2px; background: #C9D3CE"></span>
      <span style="font-size: 20px; font-weight: 600">Post to your WhatsApp status?</span>
      <div style="display: flex; gap: 14px; align-items: center">{milestone_card(0.12)}<span style="font-size: 14px; line-height: 1.5; color: {SEC}">WhatsApp opens with this image. You choose who sees it there; AWO never sees who views it.</span></div>
      {primary('Open WhatsApp', hole='post')}
      <button onClick="[[ close ]]" style="height: 48px; margin-top: -6px; border-radius: {R_M}px; font-size: 15px; font-weight: 600">Cancel</button>
    </div></sc-if>
  <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div class="toast" style="bottom: 32px">{icon('check', 18, LIME, 2.6)}<span>[[ toastText ]]</span></div></sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const say = (t) => this.setState({ toast: t, sheet: false });
    const v = {
      sheet: !!st.sheet, toast: !!st.toast, toastText: st.toast || '',
      t_circles: () => say('Shared with Safety net circle. They can cheer it.'),
      t_status: () => this.setState({ sheet: true, toast: '' }),
      t_chat: () => say('WhatsApp opened. Pick a chat to send it to.'),
      t_save: () => say('Saved to your photos.'),
      post: () => say('WhatsApp opened with your card.'), close: () => this.setState({ sheet: false })
    };
%(sw)s
    v.cardName = v.sw0 ? 'Naledi' : '';
    return v;
  }
}''' % dict(sw=switch_js(1, [True]))
    return hand_hole(free_page('A milestone', inner, logic, h=900))


# ---------------------------------------------------------------- 6. WhatsApp status cards (1080 by 1920)

def status_milestone():
    inner = f'''<div style="position: absolute; left: 90px; top: 110px">{lockup(52, EVG, LIME)}</div>
<div style="position: absolute; left: 120px; right: 120px; top: 480px">{stones_svg(4, 840, 360, new_last=True)}</div>
<div style="position: absolute; left: 90px; right: 90px; top: 1000px; display: flex; flex-direction: column; gap: 36px">
  <h1 style="margin: 0; {H(132, EVG, BAL)}">Four <span style="white-space: nowrap">check-ins</span> in a row.</h1>
  <span class="hand" style="font-size: 88px; color: {EVG}; {HF}">Four months, kept.</span>
  <span style="font-size: 44px; font-weight: 600; color: {EVG}">Naledi</span>
</div>
<span style="position: absolute; left: 90px; right: 90px; bottom: 100px; font-size: 34px; line-height: 1.35; color: {SEC}">On AWO, milestones never show amounts.</span>'''
    return hand_hole(canvas_board('Status card: a milestone', 1080, 1920, POOL, inner))


def status_word():
    inner = f'''<div style="position: absolute; left: 90px; top: 110px">{lockup(52, MOON, LIME)}</div>
<div style="position: absolute; left: 150px; right: 150px; top: 300px; height: 960px; border-radius: 390px 390px {K}px {K}px; background: {LIME}; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 300px 70px 0; box-sizing: border-box; gap: 26px">
  <span style="font-size: 40px; font-weight: 600; color: {EVG}">Word of the week</span>
  <span style="{H(168, EVG)}">Dividend</span>
  <span style="font-size: 38px; color: {EVG}">Say it: div-i-dend</span>
  <p style="margin: 0; font-size: 44px; line-height: 1.3; color: {INK}; {BAL}">A share of a company's profit, paid to the people who own its shares.</p>
</div>
<div style="position: absolute; left: 90px; right: 90px; top: 1360px; display: flex; flex-direction: column; gap: 18px">
  <span style="font-size: 44px; line-height: 1.3; color: {MOON}; {BAL}">Not every company pays one. A dividend can shrink, or stop.</span>
  <span style="font-size: 34px; color: {NMUTED}">Decode any money word in Words, on AWO.</span>
</div>'''
    return canvas_board('Status card: word of the week', 1080, 1920, NIGHT, inner)


def status_story():
    inner = f'''<img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her stall" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1060px; object-fit: cover; object-position: 60% 30%">
<div style="position: absolute; left: 90px; top: 100px; display: flex; gap: 12px"><span style="height: 60px; padding: 0 24px; border-radius: 14px; background: {LIME}; color: {EVG}; display: inline-flex; align-items: center; font-size: 30px; font-weight: 600">Rise story</span><span style="height: 60px; padding: 0 24px; border-radius: 14px; background: {BLUSH}; color: {BLUSH_INK}; display: inline-flex; align-items: center; font-size: 30px; font-weight: 600">Member story</span></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 960px; border-radius: {K}px {K}px 0 0; background: {NIGHT}; padding: 90px 90px 100px; box-sizing: border-box; display: flex; flex-direction: column; gap: 34px">
  <h1 style="margin: 0; {H(104, MOON, BAL)}">My first stall closed in four months.</h1>
  <span class="hand" style="font-size: 92px; color: {LIME}; {HF}">Then I started again.</span>
  <span style="font-size: 32px; color: {NMUTED}">Wanjiru, Nairobi. A sample story, in her own words.</span>
  <div style="flex-grow: 1"></div>
  <div style="display: flex; justify-content: space-between; align-items: flex-end"><span style="font-size: 32px; line-height: 1.35; color: {MOON}">Read or listen in AWO,<br>even offline.</span>{lockup(64, MOON, LIME)}</div>
</div>'''
    return hand_hole(canvas_board('Status card: a Rise story', 1080, 1920, NIGHT, inner))


# ---------------------------------------------------------------- 7. One search

INDEX = [  # area, title, sub, href, extra words to match
    ('Words', 'Dividend', "A share of a company's profit, paid to shareholders", 'R8-Words-Decoder.dc.html', 'shares investing word of the week'),
    ('Words', 'Stokvel', 'A savings group that takes turns with the pot', 'R8-Words-Decoder.dc.html', 'chama savings group rotating'),
    ('Words', 'UIF', 'Unemployment insurance: 1% of your pay', 'R8-Words-Decoder.dc.html', 'payslip deduction'),
    ('Words', 'Debit order', 'A payment your bank sends every month for you', 'R8-Words-Decoder.dc.html', 'statement bank'),
    ('Learn', 'Savings groups, in three minutes', "A lesson, through Thandi's story", 'R7-Lesson.dc.html', 'stokvel chama saving together'),
    ('Learn', 'Shares and dividends', 'A topic: step through the bakery', 'R8-Topic-Shares.dc.html', 'dividend investing shares'),
    ('Learn', 'Fees, the quiet cost', 'A lesson in the Investing path, 3 minutes', 'R8-Topic-Shares.dc.html', 'fee investing'),
    ('Hub', 'Payslip decoder', 'Every line of your payslip, in plain words', 'R8-Tool-Payslip.dc.html', 'paye uif pension salary pay'),
    ('Hub', 'Pay-day plan', 'Every rand a job, family included', 'R8-Tool-Payday.dc.html', 'payday budget pay'),
    ('Hub', 'Debt payoff', 'Your debt-free date', 'R8-Tool-Debt.dc.html', 'loan store card'),
    ('Hub', 'Fee eater', 'What a fee costs over 20 years', 'R8-Tool-Fees.dc.html', 'investing fee'),
    ('Community', 'Where do you keep your safety net?', 'A question in Safety net circle, 3 replies', 'R8-Post.dc.html', 'saving emergency'),
    ('Community', 'Do I pay tax on dividends?', 'A question in Investing circle, 5 replies', 'R8-Post.dc.html', 'dividend tax shares investing'),
    ('Community', 'Our stokvel pays out in December', 'A note from Thandi in Saving together', 'R8-Feed.dc.html', 'stokvel chama'),
    ('Help', 'What is the DIVA score?', 'A number from 0 to 100: readiness to learn and act', 'R9-Help.dc.html', 'diva score profile'),
    ('Help', 'Who can see my answers?', 'Only you. Here is what AWO can and cannot see', 'R9-Help.dc.html', 'privacy data'),
    ('Me', 'Your DIVA profile', 'Stage, score, and what it means', 'R7-Me.dc.html', 'diva score stage'),
]
AREA_ORDER = ['Words', 'Learn', 'Hub', 'Community', 'Help', 'Me']
SFILTERS = ['All', 'Learn', 'Words', 'Hub', 'Community', 'Help']


def search():
    groups = ''
    for a in AREA_ORDER:
        rows = ''
        for i, (area, t, sub, href, _k) in enumerate(INDEX):
            if area != a:
                continue
            rows += f'''<sc-if value="[[ r{i} ]]" hint-placeholder-val="[[ true ]]"><a href="{href}" style="min-height: 60px; padding: 8px 0; display: flex; align-items: center; gap: 12px; border-top: 1px solid {LINE7}">{area_badge(area, 36)}
            <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; line-height: 1.35; color: {MUTED}">{sub}</span></span>{icon('chev', 16, MUTED)}</a></sc-if>'''
        label = {'Words': 'Words, in Learn', 'Learn': 'Lessons and topics', 'Hub': 'Hub tools', 'Community': 'Community', 'Help': 'Help', 'Me': 'Me'}[a]
        groups += f'<sc-if value="[[ g{a} ]]" hint-placeholder-val="[[ true ]]"><section style="display: flex; flex-direction: column"><span style="font-size: 13px; font-weight: 600; color: {MUTED}; padding: 10px 0 6px">{label}</span>{rows}</section></sc-if>'
    fchips = ''.join(f'<button onClick="[[ sf{j} ]]" aria-pressed="[[ sfOn{j} ]]" style="height: 40px; flex-shrink: 0; padding: 0 14px; border-radius: 8px; background: [[ sfBg{j} ]]; color: [[ sfFg{j} ]]; font-size: 14px; font-weight: 600; white-space: nowrap">{f} <span style="opacity: .7">[[ sfN{j} ]]</span></button>' for j, f in enumerate(SFILTERS))
    tries = ''.join(f'<button onClick="[[ try{j} ]]" style="height: 40px; padding: 0 14px; border-radius: 8px; background: #FFFFFF; font-size: 14px; font-weight: 600; color: {EVG}">{w}</button>' for j, w in enumerate(['Dividend', 'Payslip', 'Stokvel', 'DIVA score']))
    recent = ''.join(f'''<sc-if value="[[ rec{j} ]]" hint-placeholder-val="[[ true ]]"><div style="min-height: 48px; display: flex; align-items: center; gap: 12px; border-top: 1px solid {LINE7}">{ic8('clock', 18, MUTED)}<button onClick="[[ use{j} ]]" style="flex-grow: 1; min-height: 44px; text-align: left; font-size: 15px">{w}</button>
        <button onClick="[[ del{j} ]]" aria-label="Remove {w}" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ic('close', 16, MUTED)}</button></div></sc-if>''' for j, w in enumerate(['car goal', 'uif', 'school fees']))
    body = f'''    <header style="display: flex; align-items: center; gap: 10px">
      <label style="flex-grow: 1; height: 48px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; gap: 10px; padding: 0 12px">{icon('search', 20, EVG)}<span style="{SR}">Search AWO</span>
        <input value="[[ q ]]" onInput="[[ type ]]" placeholder="Words, lessons, tools, circles" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; outline: none; background: transparent; font-size: 16px"></label>
      <sc-if value="[[ hasQ ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ clear ]]" style="height: 48px; padding: 0 4px; font-size: 15px; font-weight: 600; color: {EVG}">Clear</button></sc-if>
      <sc-if value="[[ noQ ]]" hint-placeholder-val="[[ true ]]"><a href="R8-Home.dc.html" style="height: 48px; padding: 0 4px; display: flex; align-items: center; font-size: 15px; font-weight: 600; color: {EVG}">Cancel</a></sc-if>
    </header>
    <sc-if value="[[ noQ ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 18px">
      <section style="display: flex; flex-direction: column"><span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Recent</span><button onClick="[[ clearRecent ]]" style="min-height: 44px; font-size: 14px; font-weight: 600; color: {EVG}">Clear all</button></span>{recent}
        <sc-if value="[[ noRecent ]]" hint-placeholder-val="[[ false ]]"><span style="font-size: 14px; color: {MUTED}; padding: 8px 0">No recent searches.</span></sc-if></section>
      <section style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 15px; font-weight: 600">Try</span><div style="display: flex; flex-wrap: wrap; gap: 8px">{tries}</div></section>
      <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}">{icon('lock', 14, MUTED)}Recent searches stay on this phone.</span>
    </div></sc-if>
    <sc-if value="[[ hasQ ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 6px">
      <div role="group" aria-label="Show results from" class="hscroll" style="display: flex; gap: 6px; margin: 0 -20px; padding: 0 20px 4px; overflow-x: auto; scrollbar-width: none">{fchips}</div>
      {groups}
      <sc-if value="[[ none ]]" hint-placeholder-val="[[ false ]]"><section style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding: 28px 12px; animation: rise .3s cubic-bezier(.2,.8,.2,1) both">
        <span style="width: 64px; height: 64px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('search', 28, MUTED)}</span>
        <span style="font-size: 18px; font-weight: 600">Nothing for "[[ q ]]" yet</span>
        <span style="font-size: 15px; line-height: 1.45; color: {SEC}">Check the spelling, or ask Ola to explain it in plain words.</span>
        <a href="R7-Ask.dc.html" style="height: 48px; padding: 0 18px; border-radius: {R_M}px; background: {NIGHT}; color: {MOON}; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600">Ask Ola <span class="chip" style="height: 22px; border: 1px dashed {MINT}; color: {MINT}">AI-assisted</span></a>
        <button onClick="[[ suggest ]]" style="min-height: 44px; font-size: 14px; font-weight: 600; color: {EVG}">Suggest it for Words</button>
      </section></sc-if>
    </div></sc-if>
    <sc-if value="[[ toast ]]" hint-placeholder-val="[[ false ]]"><div class="toast" style="bottom: 24px">{icon('check', 18, LIME, 2.6)}<span>[[ toastText ]]</span></div></sc-if>'''
    idx = [[a, t.lower() + ' ' + s.lower() + ' ' + k] for a, t, s, _h, k in INDEX]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const q = st.q == null ? 'dividend' : st.q, f = st.f || 0, idx = %(idx)s, areas = %(areas)s, filt = %(filt)s;
    const rec = st.rec || [true, true, true], words = ['car goal', 'uif', 'school fees'], tries = ['Dividend', 'Payslip', 'Stokvel', 'DIVA score'];
    const terms = q.trim().toLowerCase().split(/\\s+/).filter(Boolean);
    const hit = idx.map((e) => terms.length > 0 && terms.every((t) => e[1].indexOf(t) >= 0));
    const inF = (a) => f === 0 || filt[f] === a || (filt[f] === 'Learn' && a === 'Learn');
    const v = {
      q, hasQ: terms.length > 0, noQ: terms.length === 0, type: (e) => this.setState({ q: e.target.value }), clear: () => this.setState({ q: '', f: 0 }),
      clearRecent: () => this.setState({ rec: [false, false, false] }), noRecent: !rec.some(Boolean),
      suggest: () => this.setState({ toast: 'Thanks. The Words team reads every suggestion.' }), toast: !!st.toast, toastText: st.toast || ''
    };
    idx.forEach((e, i) => { v['r' + i] = hit[i] && inF(e[0]); });
    areas.forEach((a) => { v['g' + a] = idx.some((e, i) => e[0] === a && v['r' + i]); });
    v.none = terms.length > 0 && !idx.some((e, i) => v['r' + i]);
    filt.forEach((fl, j) => {
      const n = idx.filter((e, i) => hit[i] && (j === 0 || e[0] === fl)).length;
      v['sf' + j] = () => this.setState({ f: j }); v['sfOn' + j] = f === j; v['sfN' + j] = n;
      v['sfBg' + j] = f === j ? '%(evg)s' : '#FFFFFF'; v['sfFg' + j] = f === j ? '#FFFFFF' : '%(ink)s';
    });
    words.forEach((w, j) => { v['rec' + j] = rec[j]; v['use' + j] = () => this.setState({ q: w }); v['del' + j] = () => { const r = rec.slice(); r[j] = false; this.setState({ rec: r }); }; });
    tries.forEach((w, j) => { v['try' + j] = () => this.setState({ q: w, f: 0 }); });
    return v;
  }
}''' % dict(idx=js(idx), areas=js(AREA_ORDER), filt=js(SFILTERS), evg=EVG, ink=INK)
    return page9('Search', body, logic, h=1000)


# ---------------------------------------------------------------- 8. Help and support

TOPICS = [('stones', POOL, 'Your DIVA score'), ('clock', MIST, 'Check-ins and versions'), ('shield', MIST, 'Privacy and your data'),
          ('lock', MIST, 'Account and PIN'), ('hub', LIME, 'Hub tools'), ('ripple', BLUSH, 'Community and safety')]
QS = [
    [('What is the DIVA score?', "A number from 0 to 100 that shows your readiness to learn and act with money, across four areas. It's worked out on AWO's servers, the same way for everyone. It isn't a credit score and says nothing about loans."),
     ('Why did my DIVA score go down?', 'Something in your answers changed, often for a good reason, like using your safety net. What changed shows which area moved and why. Your past versions stay exactly as they were.')],
    [('When is my next check-in?', "Every 30 days from your last one. Yours is on 13 November, and we remind you the day before."),
     ('Can I change an answer?', "Not in a version that's done: versions never change. Your next check-in makes a new one.")],
    [('Who can see my answers?', 'Only you. People at AWO never see your amounts. If a support person needs your details to help you, they must give a reason, and it shows in your own history.'),
     ('Where is my data kept?', 'In South Africa. You can download it, or delete your account, in Me, under Settings.')],
    [('I lost my phone. What now?', 'Sign in on a new phone with your number and the code we send. Your PIN keeps AWO private if someone else has your old phone.'),
     ('I forgot my PIN', 'Sign in again with your number and the code, then choose a new PIN.')],
    [("Is a tool's answer advice?", 'No. A tool works out your own numbers the same way every time and explains them. It never picks a product or a provider for you.'),
     ('Why does a tool show a date?', 'Tax tables and fees change. Each tool shows when its figures were last checked.')],
    [('How do I report a post?', 'Tap the three dots on any post, then Report. A person at AWO looks at every report.'),
     ('Is it safe to share?', 'Use your first name. Milestones never show amounts. Never share your PIN or ID number, even with someone who says they are from AWO.')],
]


def help_centre():
    tiles = ''.join(f'''<button onClick="[[ tp{i} ]]" aria-pressed="[[ tpOn{i} ]]" style="min-height: 76px; border-radius: {R_L}px; background: #FFFFFF; box-shadow: inset 0 0 0 [[ tpBw{i} ]]px {EVG}; padding: 12px; display: flex; flex-direction: column; align-items: flex-start; justify-content: space-between; gap: 8px; text-align: left; transition: box-shadow .18s">
        <span style="width: 32px; height: 32px; border-radius: {R_M}px; background: {bg}; display: flex; align-items: center; justify-content: center">{hub_icon(None, 18, EVG) if g == "hub" else (icon(g, 18, BLUSH_INK if g == "ripple" else EVG) if g in ("stones", "ripple", "lock") else ic8(g, 18, EVG))}</span>
        <span style="font-size: 14px; font-weight: 600; line-height: 1.25">{t}</span></button>''' for i, (g, bg, t) in enumerate(TOPICS))
    qrows = ''
    for ti, qs in enumerate(QS):
        for qi, (q, a) in enumerate(qs):
            k = ti * 2 + qi
            qrows += f'''<sc-if value="[[ qs{k} ]]" hint-placeholder-val="[[ {"true" if ti == 0 else "false"} ]]"><div style="border-top: 1px solid {LINE7}">
          <button onClick="[[ qa{k} ]]" aria-expanded="[[ qo{k} ]]" style="width: 100%; min-height: 56px; display: flex; align-items: center; justify-content: space-between; gap: 10px; text-align: left; font-size: 15px; font-weight: 600">{q}<span style="flex-shrink: 0; transform: rotate([[ qr{k} ]]deg); transition: transform .2s">{icon('chev', 16, MUTED)}</span></button>
          <sc-if value="[[ qo{k} ]]" hint-placeholder-val="[[ false ]]"><p style="font-size: 15px; line-height: 1.5; color: {SEC}; padding-bottom: 14px; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">{a}</p></sc-if></div></sc-if>'''
    contact = ''.join(f'''<a href="{href}" style="min-height: 60px; display: flex; align-items: center; gap: 12px; {"border-top: 1px solid " + LINE7 + ";" if i else ""}"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: {R_M}px; background: {MIST}; color: {EVG}; display: flex; align-items: center; justify-content: center">{ic8(g, 18)}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MUTED}">{d}</span></span>{icon('chev', 16, MUTED)}</a>''' for i, (g, t, d, href) in enumerate([
        ('note', 'Chat with a person', 'Weekdays, 08:00 to 17:00 (sample hours)', 'R9-Help.dc.html'),
        ('whatsapp', 'WhatsApp us', 'Replies in the same hours', 'R9-Help.dc.html'),
        ('flag', 'Report a problem', 'Something broken, or a number that looks wrong', 'R9-Help-Report.dc.html')]))
    body = f'''    {head9('R7-Me.dc.html', 'Help')}
    <a href="R9-Search.dc.html" style="height: 48px; border-radius: {R_M}px; background: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 14px; font-size: 16px; color: {MUTED}">{icon('search', 20, MUTED)}Search help and everything else</a>
    <section style="border-radius: {R_L}px; background: {NIGHT}; color: {MOON}; padding: 18px; display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 13px; font-weight: 600; color: {MINT}">Asked most</span>
      <span style="font-size: 22px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.2">Is AWO giving me advice?</span>
      <span style="font-size: 15px; line-height: 1.5; color: #DDE3E0">No. AWO teaches and explains. It never tells you what to buy, where to borrow, or which provider to use, and it never holds or moves your money.</span>
    </section>
    <span style="font-size: 15px; font-weight: 600; margin-bottom: -6px">Topics</span>
    <div role="group" aria-label="Help topics" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{tiles}</div>
    <section class="card8" style="gap: 0; padding-top: 10px; padding-bottom: 4px"><span style="font-size: 16px; font-weight: 600; padding-bottom: 8px">[[ topicName ]]</span>{qrows}</section>
    <section class="card8" style="gap: 0; padding-top: 12px; padding-bottom: 4px"><span style="font-size: 16px; font-weight: 600; padding-bottom: 4px">Still stuck? Talk to a person</span>{contact}</section>
    <section style="border-radius: {R_L}px; background: {WARN_BG}; color: {WARN_FG}; padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start; font-size: 14px; line-height: 1.45">{ic('shield', 20, WARN_FG)}<span><b style="font-weight: 600">AWO will never ask for your PIN, your bank password or money.</b> Not by phone, SMS, WhatsApp or email. If someone does, report it here.</span></section>
    {foot("Help articles are reviewed by AWO. Last reviewed 20 September 2026. Sample content.")}'''
    names = [t for _g, _b, t in TOPICS]
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const tp = st.tp || 0, qo = st.qo == null ? 0 : st.qo, names = %(names)s;
    const v = { topicName: names[tp] };
    for (let i = 0; i < 6; i++) { v['tp' + i] = () => this.setState({ tp: i, qo: i * 2 }); v['tpOn' + i] = tp === i; v['tpBw' + i] = tp === i ? 2 : 0; }
    for (let k = 0; k < 12; k++) {
      v['qs' + k] = Math.floor(k / 2) === tp; v['qo' + k] = qo === k; v['qr' + k] = qo === k ? 90 : 0;
      v['qa' + k] = () => this.setState({ qo: qo === k ? -1 : k });
    }
    return v;
  }
}''' % dict(names=js(names))
    return page9('Help', body, logic, h=1480, tab='Me')


KINDS = ["Something doesn't work", 'A number looks wrong', "I can't find something", 'Someone in Community', 'Something else']


def help_report():
    kinds = ''.join(f'<button onClick="[[ k{i} ]]" aria-pressed="[[ kOn{i} ]]" style="min-height: 44px; padding: 0 14px; border-radius: 8px; background: [[ kBg{i} ]]; color: [[ kFg{i} ]]; font-size: 14px; font-weight: 600; transition: background-color .18s">{k}</button>' for i, k in enumerate(KINDS))
    shot = f'''<div aria-hidden="true" style="width: 72px; height: 132px; flex-shrink: 0; border-radius: 10px; background: {MIST}; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 10px 8px; box-sizing: border-box; display: flex; flex-direction: column; gap: 6px">
        <span style="height: 8px; width: 60%; border-radius: 2px; background: {INK}; opacity: .7"></span>
        <span style="height: 26px; border-radius: 4px; background: {LIME}; display: flex; align-items: center; padding: 0 5px"><span style="height: 8px; width: 70%; border-radius: 2px; background: [[ blurCol ]]; filter: blur([[ blurPx ]]px)"></span></span>
        <span style="height: 6px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 6px; width: 80%; border-radius: 2px; background: #C9D3CE"></span>
        <span style="height: 8px; width: 50%; border-radius: 2px; background: [[ blurCol ]]; filter: blur([[ blurPx ]]px)"></span></div>'''
    body = f'''    {head9('R9-Help.dc.html', 'Report a problem')}
    <sc-if value="[[ writing ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px">
      <section style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 16px; font-weight: 600">What happened?</span><div role="radiogroup" aria-label="What happened" style="display: flex; flex-wrap: wrap; gap: 6px">{kinds}</div></section>
      <label style="display: flex; flex-direction: column; gap: 8px"><span style="display: flex; justify-content: space-between"><span style="font-size: 16px; font-weight: 600">Tell us in your own words</span><span style="font-size: 13px; color: {MUTED}">[[ count ]] of 500</span></span>
        <textarea value="[[ text ]]" onInput="[[ typing ]]" maxlength="500" rows="4" placeholder="What were you trying to do? What did you see?" style="border: 0; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 12px 14px; font: inherit; font-size: 16px; line-height: 1.45; resize: none; color: {INK}"></textarea></label>
      <section class="card8" style="gap: 12px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 16px; font-weight: 600">A screenshot</span><span style="font-size: 13px; color: {MUTED}">Optional</span></span>
        <sc-if value="[[ noShot ]]" hint-placeholder-val="[[ false ]]"><button onClick="[[ attach ]]" style="height: 56px; border-radius: {R_M}px; box-shadow: inset 0 0 0 1.5px #C9D3CE; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600; color: {EVG}">{ic8('image', 20, EVG)}Add a screenshot</button></sc-if>
        <sc-if value="[[ hasShot ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; gap: 14px; align-items: flex-start; animation: rise .25s cubic-bezier(.2,.8,.2,1) both">{shot}
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; line-height: 1.4; color: {SEC}">Screenshot from 13 Oct, 08:14</span>
            <span style="display: flex; align-items: center; justify-content: space-between; gap: 6px; margin-right: -8px"><span style="font-size: 15px; font-weight: 600">Hide amounts in it</span>{switch(0, 'Hide amounts in the screenshot')}</span>
            <button onClick="[[ unattach ]]" style="align-self: flex-start; min-height: 44px; font-size: 14px; font-weight: 600; color: {WARN_FG}">Remove</button></span></div></sc-if>
      </section>
      <section class="card8" style="gap: 6px; padding-right: 10px"><span style="display: flex; align-items: center; justify-content: space-between; gap: 8px"><span style="font-size: 16px; font-weight: 600">Include phone details</span>{switch(1, 'Include phone details')}</span>
        <span style="font-size: 13px; line-height: 1.45; color: {MUTED}">Your phone model, Android version and AWO version. Never your answers or amounts.</span></section>
      <sc-if value="[[ canSend ]]" hint-placeholder-val="[[ false ]]">{primary('Send to AWO', hole='send')}</sc-if>
      <sc-if value="[[ cantSend ]]" hint-placeholder-val="[[ true ]]">{disabled('Send to AWO')}</sc-if>
      <span style="font-size: 13px; color: {MUTED}; text-align: center; margin-top: -6px">[[ hint ]]</span>
    </div></sc-if>
    <sc-if value="[[ sent ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; padding-top: 40px; animation: rise .35s cubic-bezier(.2,.8,.2,1) both">
      <span style="width: 64px; height: 64px; border-radius: 999px; background: {LIME}; display: flex; align-items: center; justify-content: center; animation: pop .5s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 32, EVG, 2.8)}</span>
      {title('Sent. Thank you.', 'A person at AWO reads every report and replies within two working days (sample). The reply comes to Notifications.', 36)}
      <section class="card8" style="gap: 6px"><span style="font-size: 13px; color: {MUTED}">Your reference</span><span style="font-size: 22px; font-weight: 600; letter-spacing: 0.02em">AWO-2419</span><span style="font-size: 14px; color: {SEC}">[[ kindName ]]</span></section>
      {primary('Back to Help', 'R9-Help.dc.html')}
      <a href="R9-Notifications.dc.html" style="height: 48px; margin-top: -6px; border-radius: {R_M}px; font-size: 15px; font-weight: 600; color: {EVG}; display: flex; align-items: center; justify-content: center">Go to Notifications</a>
    </div></sc-if>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const k = st.k == null ? 1 : st.k, text = st.text == null ? 'My DIVA score says 64 but Me still shows 63.' : st.text, shot = st.shot == null ? true : st.shot;
    const kinds = %(kinds)s;
    const v = {
      writing: !st.sent, sent: !!st.sent, text, count: text.length, typing: (e) => this.setState({ text: e.target.value }),
      noShot: !shot, hasShot: shot, attach: () => this.setState({ shot: true }), unattach: () => this.setState({ shot: false }),
      canSend: k >= 0 && text.trim().length > 0, cantSend: !(k >= 0 && text.trim().length > 0),
      hint: k < 0 ? 'Choose what happened first.' : (text.trim() ? 'A person reads it. No bots.' : 'Add a few words so we can help.'),
      send: () => this.setState({ sent: true }), kindName: k >= 0 ? kinds[k] : ''
    };
%(sw)s
    v.blurPx = v.sw0 ? 3 : 0; v.blurCol = v.sw0 ? '#8A9690' : '%(ink)s';
    for (let i = 0; i < 5; i++) { v['k' + i] = () => this.setState({ k: i }); v['kOn' + i] = k === i; v['kBg' + i] = k === i ? '%(evg)s' : '#FFFFFF'; v['kFg' + i] = k === i ? '#FFFFFF' : '%(ink)s'; }
    return v;
  }
}''' % dict(kinds=js(KINDS), evg=EVG, ink=INK, sw=switch_js(2, [True, True]))
    return page9('Report a problem', body, logic, h=1080)


# ---------------------------------------------------------------- 9. The loop, end to end (a board)

FLOW_CAPS = {'lock': '/_blob/6f3a4c5dce73ec89bb40a3ed8158b154', 'notif': '/_blob/b12c402f4009ed243b64ab5a49c11d9f',
             'checkin': '/_blob/aa2747e542df2f651c25c477e83783ea', 'changed': '/_blob/f1905e3eeb50a9fb548749ee3b762d48',
             'step': '/_blob/317ba27e4e8ed38f22e19fb880234f05', 'milestone': '/_blob/7ab3cc538d480b78a791833bfa636160',
             'status': '/_blob/42aff4b6ffed97962036c3ef27f7b4fd', 'home': '/_blob/be682d2143b220d853c02461273a8261'}
FLOW = [  # cap, when, title, board, she sees, AWO does
    ('lock', 'Day 30, 07:30', 'The reminder', 'R9-Lock-Reminder', 'A reminder on her lock screen, with no amounts. Start, tonight, or skip a month.', 'Sends one push, after quiet hours end.'),
    ('notif', 'If she missed it', 'Notifications', 'R9-Notifications', 'The check-in stays on top until she does it. The bell on Home shows what is new.', 'Keeps reminders, replies and changes in one place.'),
    ('checkin', 'About two minutes', 'The check-in', 'R7-Checkin', 'Three questions: what she put aside, the step, how money felt.', 'Keeps her answers private. Nothing is shared.'),
    ('changed', 'Straight after', 'What changed', 'R9-What-Changed', 'Version 4: her DIVA score, what moved and why, in plain words.', 'Scores on the server and makes a new version. Version 3 never changes.'),
    ('step', 'Next', 'One step', 'R9-Next-Step', 'One reviewed step for October, and a reminder on payday.', 'Offers steps from the reviewed library for her focus. AI never picks.'),
    ('milestone', 'When there is one', 'A milestone', 'R9-Milestone', 'Four check-ins in a row: showing up, not the score.', 'Keeps amounts, the score and the stage off the card.'),
    ('status', 'If she wants', 'Shared', 'R9-Status-Milestone', 'The card, on her WhatsApp status or in her circle.', 'Makes the image on her phone. Never sees who views it.'),
    ('home', 'The next 30 days', 'Home', 'R8-Home', 'Her step and the next check-in on Home. Day 60 starts it again.', 'Reminds her on payday, then the day before check-in 5.'),
]
GAPS = [('The check-in ended on Me, where nothing said what had changed.', 'What changed, and a month that went down explained too'),
        ('There was a first step, but no step for each month after it.', "This month's step, from reviewed steps"),
        ('A reminder disappeared once it was swiped away.', 'The notification centre, with a bell on Home'),
        ('Milestones stayed inside the app.', 'Sharing, with the privacy rules built into the card'),
        ('Missing a month had no kind way out.', '"Skip a month" on the reminder: nothing is lost'),
        ('Help and search had no home.', 'Help, one search, and reporting a problem')]
RULES9 = ['No amounts on the lock screen, or on anything she shares.', 'Results never get a burst. Showing up does.',
          'Old versions never change. A check-in makes a new one.', 'Steps come from the reviewed library. AI never picks one.',
          'A month that goes down is explained, never hidden.']


def loop_flow():
    cols = ''
    for i, (cap, when, t, board, she, awo) in enumerate(FLOW):
        tall = 'height: 434px' if cap != 'status' else 'height: 356px'
        arrow = '' if i == len(FLOW) - 1 else f'<span aria-hidden="true" style="position: absolute; right: -22px; top: 250px; width: 20px; height: 20px; color: {EVG}">{icon("chev", 20, EVG, 2.4)}</span>'
        cols += f"""<div style="position: relative; width: 236px; flex-shrink: 0; display: flex; flex-direction: column; gap: 12px">
        <span style="font-size: 14px; font-weight: 600; color: {EVG}">{when}</span>
        <a href="{board}.dc.html" style="display: block; width: 200px; {tall}; border-radius: 22px; overflow: hidden; box-shadow: 0 0 0 5px {INK}, 0 18px 40px rgba(16,24,20,.18); margin: 5px 0 6px 5px"><img src="{FLOW_CAPS[cap]}" alt="The {t} screen" style="width: 200px; display: block"></a>{arrow}
        <a href="{board}.dc.html" style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; display: flex; align-items: center; gap: 6px; min-height: 44px">{t}{icon('chev', 16, MUTED)}</a>
        <span style="font-size: 15px; line-height: 1.45"><b style="font-weight: 600">She sees.</b> {she}</span>
        <span style="font-size: 14px; line-height: 1.45; color: {SEC}"><b style="font-weight: 600; color: {EVG}">AWO does.</b> {awo}</span>
      </div>"""
    gaps = ''.join(f"""<div style="display: grid; grid-template-columns: 1fr 24px 1fr; gap: 12px; align-items: start; padding: 12px 0; {'border-top: 1px solid ' + LINE7 + ';' if i else ''}">
        <span style="font-size: 15px; line-height: 1.45; color: {SEC}">{g}</span>{icon('send', 20, EVG)}<span style="font-size: 15px; line-height: 1.45; font-weight: 600">{f}</span></div>""" for i, (g, f) in enumerate(GAPS))
    rules = ''.join(f'<span style="display: flex; gap: 10px; font-size: 15px; line-height: 1.45"><span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 6px; background: {LIME}; display: flex; align-items: center; justify-content: center">{icon("check", 14, EVG, 2.8)}</span>{r}</span>' for r in RULES9)
    body = f"""  <div style="display: flex; gap: 40px; align-items: flex-start">{cols}</div>
  <div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 24px">
    <section class="card" style="background: #FFFFFF; padding: 22px 26px; display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 600; padding-bottom: 6px">Gaps this flow found, and what closes them</span>{gaps}</section>
    <div style="display: flex; flex-direction: column; gap: 24px">
      <section class="card" style="background: #FFFFFF; padding: 22px 26px; display: flex; flex-direction: column; gap: 12px"><span style="font-size: 20px; font-weight: 600">The rules it keeps</span>{rules}</section>
      <section class="card" style="background: {BLUSH}; color: {BLUSH_INK}; padding: 20px 24px; display: flex; flex-direction: column; gap: 8px"><span style="font-size: 17px; font-weight: 600">Still AWO's call (Q-46)</span><span style="font-size: 15px; line-height: 1.5">What may a member share outside AWO? Proposed: milestones about showing up and learning, never amounts, the DIVA score or the stage.</span></section>
    </div>
  </div>"""
    return board7('The 30-day loop, end to end', 'Naledi\'s fourth check-in, from the reminder to the next 30 days. Each screen already existed or is new in Round 9; seen in order, the gaps show. Tap a screen or its name to open it.', body, static_logic(), 2360, 1500, chip='Sample content. Tap to open a screen.')


BOARDS = [('R9-Lock-Reminder', lock_reminder), ('R9-Notifications', notifications), ('R9-What-Changed', what_changed),
          ('R9-Next-Step', next_step), ('R9-Milestone', milestone_share), ('R9-Status-Milestone', status_milestone),
          ('R9-Status-Word', status_word), ('R9-Status-Story', status_story), ('R9-Search', search),
          ('R9-Help', help_centre), ('R9-Help-Report', help_report), ('R9-Loop-Flow', loop_flow)]
