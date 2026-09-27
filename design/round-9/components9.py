"""Round 9, batch 4: components the app still needed, and an empty-state set.

Two boards of live components, each shown working inside a phone-sized frame with the rule it follows: sheets,
dialogs (including "are you sure?" before a deletion) and toasts; a date picker, file upload, loading placeholders
and an amount in two currencies. Then empty states drawn from the five tab shapes: pool, moon, keystone, ripple,
stones. Every one says what to do next, never just "nothing here"."""
import calendar
import datetime
import json

from lib9 import *  # noqa: F401,F403

DAY_W = 44


def js(o):
    return json.dumps(o, ensure_ascii=False)


def frame(inner, h=560, bg=MIST, label=''):
    """A phone-width frame on a component board, clipping its own sheets and toasts."""
    return (f'<div role="group" aria-label="{label}" style="position: relative; width: 360px; height: {h}px; flex-shrink: 0; border-radius: 28px; background: {bg}; '
            f'box-shadow: 0 0 0 1px rgba(16,24,20,.1), 0 20px 50px rgba(16,24,20,.12); overflow: hidden">{inner}</div>')


def comp(title_text, rules, inner):
    rl = ''.join(f'<span style="display: flex; gap: 10px; font-size: 14px; line-height: 1.45; color: {SEC}"><span style="width: 6px; height: 6px; margin-top: 8px; flex-shrink: 0; border-radius: 999px; background: {EVG}"></span>{r}</span>' for r in rules)
    return (f'<section class="card" style="background: #FFFFFF; padding: 22px; display: flex; flex-direction: column; gap: 16px; width: 404px; box-sizing: border-box">'
            f'<span class="ktitle" style="font-size: 19px; font-weight: 600">{title_text}</span>{inner}<div style="display: flex; flex-direction: column; gap: 6px">{rl}</div></section>')


def btn(label, hole, kind='primary', h=48):
    styles = {'primary': f'background: {EVG}; color: #FFFFFF', 'quiet': f'background: #FFFFFF; color: {INK}; box-shadow: inset 0 0 0 1px #C9D3CE',
              'danger': f'background: {WARN_FG}; color: #FFFFFF', 'lime': f'background: {LIME}; color: {EVG}'}
    return f'<button onClick="[[ {hole} ]]" style="height: {h}px; width: 100%; border-radius: {R_M}px; {styles[kind]}; font-size: 15px; font-weight: 600">{label}</button>'


# ---------------------------------------------------------------- Sheets, dialogs, toasts

def overlays():
    sheet_demo = frame(f'''<div style="padding: 24px 18px; display: flex; flex-direction: column; gap: 12px">
        <span style="font-size: 17px; font-weight: 600">Moving-out goal</span>
        <span style="font-size: 14px; color: {SEC}">R 1 900 of R 16 200</span>
        {btn('Change the amount', 'sheetOpen')}
      </div>
      <sc-if value="[[ sheet ]]" hint-placeholder-val="[[ true ]]"><div class="dim" onClick="[[ sheetClose ]]"></div>
        <div class="sheet" role="dialog" aria-label="Change the amount" style="padding: 10px 18px 22px; display: flex; flex-direction: column; gap: 14px">
          <span aria-hidden="true" style="align-self: center; width: 40px; height: 4px; border-radius: 2px; background: #C9D3CE"></span>
          <span style="font-size: 19px; font-weight: 600">How much do you need?</span>
          <span style="height: 56px; border-radius: {R_M}px; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; padding: 0 14px; font-size: 22px; font-weight: 600">[[ amt ]]</span>
          <div style="display: flex; gap: 6px">{''.join(f'<button onClick="[[ am{i} ]]" style="flex: 1 1 0; height: 44px; border-radius: 8px; background: {MIST}; font-size: 14px; font-weight: 600">{t}</button>' for i, t in enumerate(['R 12 000', 'R 16 200', 'R 20 000']))}</div>
          {btn('Save', 'sheetClose')}
        </div></sc-if>''', 360, label='A bottom sheet')
    dialog_demo = frame(f'''<div style="padding: 24px 18px; display: flex; flex-direction: column; gap: 12px">
        <span style="font-size: 17px; font-weight: 600">Moving-out goal</span>
        <span style="font-size: 14px; color: {SEC}">R 1 900 of R 16 200</span>
        {btn('Delete this goal', 'dlgOpen', 'quiet')}
        <sc-if value="[[ deleted ]]" hint-placeholder-val="[[ false ]]"><span style="font-size: 14px; color: {SEC}">Deleted. The R 1 900 is still in your account.</span></sc-if>
      </div>
      <sc-if value="[[ dlg ]]" hint-placeholder-val="[[ false ]]"><div class="dim"></div>
        <div role="alertdialog" aria-label="Delete the Moving-out goal?" style="position: absolute; z-index: 41; left: 20px; right: 20px; top: 70px; border-radius: 14px; background: #FFFFFF; padding: 22px 18px 18px; display: flex; flex-direction: column; gap: 12px; box-shadow: 0 20px 50px rgba(16,24,20,.25); animation: pop .3s cubic-bezier(.34,1.3,.64,1) both">
          <span style="font-size: 19px; font-weight: 600">Delete the Moving-out goal?</span>
          <span style="font-size: 15px; line-height: 1.45; color: {SEC}">The R 1 900 stays where it is; only the goal and its history go. You can't undo this.</span>
          {btn('Keep the goal', 'dlgClose')}
          {btn('Delete it', 'dlgDelete', 'danger')}
        </div></sc-if>''', 360, label='A dialog before deleting')
    toasts = [('Saved', 'check', LIME, ''), ('Goal deleted', 'check', LIME, 'Undo'), ("You're offline. We'll send it when you're back.", 'wifi-off', '#C9D3CE', ''), ("Couldn't save.", 'close', BLUSH, 'Try again')]
    tbtns = ''.join(f'<button onClick="[[ t{i} ]]" style="height: 44px; border-radius: 8px; background: #FFFFFF; box-shadow: 0 1px 2px rgba(16,24,20,.08); font-size: 14px; font-weight: 600">{n}</button>' for i, n in enumerate(['Saved', 'Undo', 'Offline', 'Error']))
    tvis = ''.join(f'''<sc-if value="[[ ts{i} ]]" hint-placeholder-val="[[ {"true" if i == 1 else "false"} ]]"><div role="status" class="toast" style="bottom: 18px; left: 14px; right: 14px; flex-direction: column; align-items: stretch; gap: 8px; padding-bottom: 10px">
          <span style="display: flex; align-items: center; gap: 10px">{icon(g, 18, c, 2.6) if g == 'check' else (ic8(g, 18, c) if g == 'wifi-off' else ic(g, 18, c, 2.4))}<span style="flex-grow: 1">{t}</span>{f'<button onClick="[[ tUndo ]]" style="min-height: 44px; margin: -12px 0; padding: 0 4px; color: {LIME}; font-size: 15px; font-weight: 600">{a}</button>' if a else ''}</span>
          {'<span aria-hidden="true" style="height: 3px; border-radius: 2px; background: rgba(255,255,255,.18); overflow: hidden"><span style="display: block; height: 100%; background: ' + LIME + '; transform-origin: 0 0; animation: drain 6s linear both"></span></span>' if i == 1 else ''}
        </div></sc-if>''' for i, (t, g, c, a) in enumerate(toasts))
    toast_demo = frame(f'''<div style="padding: 24px 18px; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 15px; font-weight: 600">Show a toast</span><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px">{tbtns}</div></div>{tvis}''', 300, label='Toasts')
    body = f'''  <div style="display: flex; gap: 28px; align-items: flex-start">
    {comp('A bottom sheet', ['For a short task or a choice, without leaving the screen.', 'A handle, a title, one main button. Tap outside or drag down to close.', 'Focus moves into the sheet and back to what opened it.'], sheet_demo)}
    {comp('Are you sure? (a dialog)', ['Only before something that can’t be undone.', 'The safe choice comes first and is the main button; the deletion is second, in wine.', 'Says exactly what goes and what stays.'], dialog_demo)}
    {comp('Toasts', ['One line, at the bottom, gone after six seconds.', 'Undo for anything that can be undone, with the time left shown.', 'Offline and errors say what happens next. Never red: wine on blush, or grey.'], toast_demo)}
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const t = st.t == null ? 1 : st.t, amts = ['R\u00a012\u00a0000', 'R\u00a016\u00a0200', 'R\u00a020\u00a0000'];
    const v = {
      sheet: st.sheet == null ? true : st.sheet, sheetOpen: () => this.setState({ sheet: true }), sheetClose: () => this.setState({ sheet: false }),
      amt: amts[st.am == null ? 1 : st.am],
      dlg: !!st.dlg, deleted: !!st.deleted, dlgOpen: () => this.setState({ dlg: true }), dlgClose: () => this.setState({ dlg: false }),
      dlgDelete: () => this.setState({ dlg: false, deleted: true }), tUndo: () => this.setState({ t: 0 })
    };
    [0, 1, 2].forEach((i) => { v['am' + i] = () => this.setState({ am: i }); });
    for (let i = 0; i < 4; i++) { v['t' + i] = () => this.setState({ t: i, n: (st.n || 0) + 1 }); v['ts' + i] = t === i; }
    return v;
  }
}'''
    css = '@keyframes drain{from{transform:scaleX(1)}to{transform:scaleX(0)}}.card{border-radius:14px}'
    return board7('Sheets, dialogs and toasts', 'The overlays the app needs, each working in a phone-width frame, with the rules it follows. Round 7 corners and colours; motion that answers a touch; reduce motion respected.', body, logic, 1400, 820, css=CSS9 + css)


# ---------------------------------------------------------------- Dates, files, loading, two currencies

RATES = {'R': 1.0, '£': 23.05, 'US$': 18.10, 'KSh': 0.14, 'P': 1.33}
CUR_NAMES = {'R': 'South African rand', '£': 'British pound', 'US$': 'US dollar', 'KSh': 'Kenyan shilling', 'P': 'Botswana pula'}


def inputs():
    # October 2026, weeks starting on Monday
    cal = calendar.Calendar(firstweekday=0)
    days = list(cal.itermonthdates(2026, 10))
    marks = {datetime.date(2026, 10, 30): 'pay', datetime.date(2026, 10, 13): 'check', datetime.date(2026, 10, 5): 'pot'}
    cells = ''
    for i, d in enumerate(days):
        other = d.month != 10
        mk = marks.get(d)
        dot = {'pay': LIME, 'check': POOL, 'pot': BLUSH}.get(mk, 'transparent')
        if other:
            cells += f'<span style="height: 44px; display: flex; align-items: center; justify-content: center; font-size: 14px; color: #B3BDB8">{d.day}</span>'
        else:
            cells += (f'<button onClick="[[ d{d.day} ]]" aria-pressed="[[ dOn{d.day} ]]" aria-label="{d.strftime("%A")} {d.day} October" style="height: 44px; border-radius: 10px; background: [[ dBg{d.day} ]]; color: [[ dFg{d.day} ]]; '
                      f'font-size: 15px; font-weight: {600 if mk else 500}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; {"box-shadow: inset 0 0 0 1.5px " + EVG + ";" if d.day == 13 else ""}">{d.day}'
                      f'<span style="width: 6px; height: 6px; border-radius: 999px; background: {dot}"></span></button>')
    heads = ''.join(f'<span style="height: 28px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: {MUTED}">{h}</span>' for h in ['M', 'T', 'W', 'T', 'F', 'S', 'S'])
    quick = ''.join(f'<button onClick="[[ q{i} ]]" style="height: 40px; padding: 0 12px; border-radius: 8px; background: {MIST}; font-size: 13px; font-weight: 600; white-space: nowrap">{t}</button>' for i, t in enumerate(['Payday', 'End of the month', 'Check-in day']))
    date_demo = frame(f'''<div style="padding: 20px 16px; display: flex; flex-direction: column; gap: 12px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 17px; font-weight: 600">October 2026</span><span style="display: flex; gap: 4px">{icon_btn('back', 'September', hole='noop', bg=MIST)}<span style="transform: scaleX(-1)">{icon_btn('back', 'November', hole='noop', bg=MIST)}</span></span></span>
        <div style="display: flex; gap: 6px">{quick}</div>
        <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px">{heads}{cells}</div>
        <span style="display: flex; gap: 12px; font-size: 12px; color: {SEC}"><span style="display: flex; align-items: center; gap: 5px"><span style="width: 8px; height: 8px; border-radius: 999px; background: {LIME}"></span>Payday</span><span style="display: flex; align-items: center; gap: 5px"><span style="width: 8px; height: 8px; border-radius: 999px; background: {POOL}; box-shadow: inset 0 0 0 1px {EVG}"></span>Check-in</span><span style="display: flex; align-items: center; gap: 5px"><span style="width: 8px; height: 8px; border-radius: 999px; background: {BLUSH}"></span>Stokvel pot</span></span>
        <span style="font-size: 15px; font-weight: 600">[[ dateLine ]]</span>
      </div>''', 560, label='A date picker')
    fstates = ['Empty', 'Reading', 'Done', 'Failed']
    fseg = ''.join(f'<button onClick="[[ f{i} ]]" aria-pressed="[[ fOn{i} ]]" style="background: [[ fBg{i} ]]; color: [[ fFg{i} ]]">{t}</button>' for i, t in enumerate(fstates))
    thumb = (f'<span aria-hidden="true" style="width: 56px; height: 72px; flex-shrink: 0; border-radius: {R_S}px; background: #FFFFFF; box-shadow: inset 0 0 0 1px #C9D3CE; padding: 8px 7px; box-sizing: border-box; display: flex; flex-direction: column; gap: 5px">'
             f'<span style="height: 5px; width: 70%; border-radius: 2px; background: #9FB0A8"></span><span style="height: 4px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 4px; border-radius: 2px; background: #C9D3CE"></span><span style="height: 5px; width: 60%; border-radius: 2px; background: {EVG}"></span></span>')
    file_demo = frame(f'''<div style="padding: 20px 16px; display: flex; flex-direction: column; gap: 14px">
        <div role="group" aria-label="Show a state" class="seg9">{fseg}</div>
        <sc-if value="[[ fs0 ]]" hint-placeholder-val="[[ false ]]"><div style="border-radius: 14px; border: 2px dashed #A9B6AF; padding: 22px 16px; display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; animation: fadeIn .25s both">
          <span style="width: 56px; height: 56px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic8('camera', 26, EVG)}</span>
          <span style="font-size: 16px; font-weight: 600">Add a photo of your payslip</span><span style="font-size: 14px; line-height: 1.4; color: {SEC}">Or a PDF. Flat, in good light, all four corners showing.</span>
          <span style="display: flex; gap: 8px; width: 100%">{btn('Take a photo', 'f1')}{btn('Choose a file', 'f1', 'quiet')}</span></div></sc-if>
        <sc-if value="[[ fs1 ]]" hint-placeholder-val="[[ false ]]"><div style="border-radius: 14px; background: #FFFFFF; padding: 16px; display: flex; gap: 12px; align-items: center; animation: fadeIn .25s both">{thumb}
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 8px"><span style="display: flex; justify-content: space-between; font-size: 14px"><span style="font-weight: 600">Reading your payslip</span><span>64%</span></span>
            <span style="height: 6px; border-radius: 2px; background: {MIST}; overflow: hidden"><span style="display: block; height: 100%; width: 64%; background: {EVG}"></span></span><span style="font-size: 13px; color: {MUTED}">In South Africa. About 10 seconds.</span></span></div></sc-if>
        <sc-if value="[[ fs2 ]]" hint-placeholder-val="[[ true ]]"><div style="border-radius: 14px; background: #FFFFFF; padding: 16px; display: flex; gap: 12px; align-items: center; animation: fadeIn .25s both">{thumb}
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><span style="display: flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 600">{icon('check', 16, EVG, 2.8)}Read: 6 lines</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">The photo is deleted once you've checked the lines.</span></span></div></sc-if>
        <sc-if value="[[ fs3 ]]" hint-placeholder-val="[[ false ]]"><div style="border-radius: 14px; background: {WARN_BG}; color: {WARN_FG}; padding: 16px; display: flex; flex-direction: column; gap: 10px; animation: fadeIn .25s both">
          <span style="font-size: 15px; font-weight: 600">It's too blurry to read</span><span style="font-size: 14px; line-height: 1.45">Try again in brighter light, or type the lines in yourself.</span>
          <span style="display: flex; gap: 8px">{btn('Try again', 'f0')}{btn('Type them in', 'f2', 'quiet')}</span></div></sc-if>
      </div>''', 380, label='File upload')
    skel = ''.join('<div style="display: flex; gap: 12px; align-items: center"><span class="sk" style="width: 44px; height: 44px; border-radius: 10px; flex-shrink: 0"></span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 8px"><span class="sk" style="height: 12px; width: 70%"></span><span class="sk" style="height: 10px; width: 45%"></span></span></div>' for _ in range(3))
    real = ''.join(f'<div style="display: flex; gap: 12px; align-items: center"><span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 10px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic8(g, 20)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{t}</span><span style="font-size: 13px; color: {MUTED}">{s}</span></span></div>'
                   for g, bg, fg, t, s in [('doc', POOL, EVG, 'Payslip decoder', 'Every line, in plain words'), ('down', LIME, EVG, 'Debt payoff', 'Your debt-free date'), ('home', WARN_BG, WARN_FG, 'Sending money home', 'The real cost')])
    load_demo = frame(f'''<div style="padding: 20px 16px; display: flex; flex-direction: column; gap: 16px">
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Loading on slow data</span>{switch(0, 'Show it loading')}</span>
        <sc-if value="[[ sw0 ]]" hint-placeholder-val="[[ true ]]"><div style="display: flex; flex-direction: column; gap: 16px">{skel}</div></sc-if>
        <sc-if value="[[ notLoading ]]" hint-placeholder-val="[[ false ]]"><div style="display: flex; flex-direction: column; gap: 16px; animation: fadeIn .3s both">{real}</div></sc-if>
      </div>''', 300, label='Loading placeholders')
    curs = list(RATES.keys())
    cbtn = lambda side: ''.join(f'<button onClick="[[ {side}{i} ]]" aria-pressed="[[ {side}On{i} ]]" style="height: 40px; min-width: 44px; padding: 0 10px; border-radius: 8px; background: [[ {side}Bg{i} ]]; color: [[ {side}Fg{i} ]]; font-size: 14px; font-weight: 600">{c}</button>' for i, c in enumerate(curs))
    cur_demo = frame(f'''<div style="padding: 20px 16px; display: flex; flex-direction: column; gap: 12px">
        <span style="font-size: 13px; font-weight: 600; color: {MUTED}">You have</span>
        <label style="height: 60px; border-radius: {R_M}px; background: #FFFFFF; box-shadow: inset 0 0 0 2px {EVG}; display: flex; align-items: center; gap: 8px; padding: 0 14px"><span style="font-size: 24px; font-weight: 600">[[ fromSym ]]</span><span style="{SR}">Amount</span>
          <input value="[[ amount ]]" onInput="[[ typeAmt ]]" inputmode="decimal" style="flex-grow: 1; min-width: 0; height: 44px; border: 0; outline: none; background: transparent; font-size: 24px; font-weight: 600"></label>
        <div role="group" aria-label="In" style="display: flex; gap: 4px; flex-wrap: wrap">{cbtn('fr')}</div>
        <button onClick="[[ swap ]]" aria-label="Swap currencies" style="align-self: center; width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; transform: rotate(90deg)">{ic8('swap', 20, EVG)}</button>
        <span style="font-size: 13px; font-weight: 600; color: {MUTED}">That's about</span>
        <span style="height: 60px; border-radius: {R_M}px; background: {POOL}; display: flex; align-items: center; padding: 0 14px; font-size: 24px; font-weight: 600; color: {EVG}">[[ result ]]</span>
        <div role="group" aria-label="In" style="display: flex; gap: 4px; flex-wrap: wrap">{cbtn('to')}</div>
        <span style="font-size: 12px; line-height: 1.45; color: {MUTED}">For planning only. Sample rates from 26 Sep 2026; the rate a provider gives you will be lower.</span>
      </div>''', 500, label='An amount in two currencies')
    body = f'''  <div style="display: grid; grid-template-columns: repeat(4, auto); gap: 28px; align-items: start">
    {comp('A date picker', ['Weeks start on Monday. Her own dates are marked: payday, check-in, the stokvel pot.', 'Quick picks for the dates she uses most.', 'Every day is a 44-pixel target, and today has an outline.'], date_demo)}
    {comp('File upload', ['Four states: empty, reading, done, failed.', 'Says where it is read and when it is deleted.', 'A failure offers another way, typing it in.'], file_demo)}
    {comp('An amount in two currencies', ['For members at home and abroad: rand, pound, dollar, shilling, pula.', 'The rate and its date are always shown, and called a sample.', 'Never says where to change money.'], cur_demo)}
    {comp('Loading placeholders', ['The shape of what is coming, so the page doesn’t jump.', 'A slow shimmer; still with reduce motion on.', 'Shown only after half a second, so fast loads don’t flash.'], load_demo)}
  </div>'''
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const day = st.day == null ? 30 : st.day, fs = st.fs == null ? 2 : st.fs;
    const rates = %(rates)s, curs = %(curs)s, fr = st.fr == null ? 1 : st.fr, to = st.to == null ? 0 : st.to, amount = st.amount == null ? '200' : st.amount;
    const n = parseFloat(String(amount).replace(',', '.')) || 0, conv = n * rates[curs[fr]] / rates[curs[to]];
    const fmt = (x) => (x >= 100 ? Math.round(x).toString() : x.toFixed(2).replace('.', ',')).replace(/\\B(?=(\\d{3})+(?!\\d))/g, '\\u00a0');
    const names = %(names)s;
    const dname = (d) => ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][(d + 2) %% 7];
    const v = {
      dateLine: dname(day) + ' ' + day + ' October' + (day === 30 ? ', payday' : day === 13 ? ', check-in day' : day === 5 ? ', the stokvel pot' : ''),
      q0: () => this.setState({ day: 30 }), q1: () => this.setState({ day: 31 }), q2: () => this.setState({ day: 13 }), noop: () => {},
      fs0: fs === 0, fs1: fs === 1, fs2: fs === 2, fs3: fs === 3,
      amount, fromSym: curs[fr], typeAmt: (e) => this.setState({ amount: e.target.value }), result: curs[to] + '\\u00a0' + fmt(conv),
      swap: () => this.setState({ fr: to, to: fr })
    };
    for (let d = 1; d <= 31; d++) { v['d' + d] = () => this.setState({ day: d }); v['dOn' + d] = day === d; v['dBg' + d] = day === d ? '%(evg)s' : 'transparent'; v['dFg' + d] = day === d ? '#FFFFFF' : '%(ink)s'; }
    for (let i = 0; i < 4; i++) { v['f' + i] = () => this.setState({ fs: i }); v['fOn' + i] = fs === i; v['fBg' + i] = fs === i ? '#FFFFFF' : 'transparent'; v['fFg' + i] = fs === i ? '%(ink)s' : '%(sec)s'; }
    curs.forEach((c, i) => {
      v['fr' + i] = () => this.setState({ fr: i }); v['frOn' + i] = fr === i; v['frBg' + i] = fr === i ? '%(evg)s' : '#FFFFFF'; v['frFg' + i] = fr === i ? '#FFFFFF' : '%(ink)s';
      v['to' + i] = () => this.setState({ to: i }); v['toOn' + i] = to === i; v['toBg' + i] = to === i ? '%(evg)s' : '#FFFFFF'; v['toFg' + i] = to === i ? '#FFFFFF' : '%(ink)s';
    });
%(sw)s
    v.notLoading = !v.sw0;
    return v;
  }
}''' % dict(rates=js(RATES), curs=js(list(RATES.keys())), names=js(CUR_NAMES), evg=EVG, ink=INK, sec=SEC, sw=switch_js(1, [True]))
    css = '.card{border-radius:14px}'
    return board7('Dates, files, loading, two currencies', 'The inputs the Round 9 screens use, each working, with the rules it follows.', body, logic, 1840, 1000, css=CSS9 + TOOL_CSS + css)


# ---------------------------------------------------------------- Empty states from the five shapes

def ill(kind):
    """An illustration from one of the five shapes, 200 by 150, calm and slow."""
    if kind == 'pool':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><rect x="72" y="30" width="56" height="110" rx="28" fill="#FFFFFF" stroke="{EVG}" stroke-width="3"></rect>
          <path d="M75 128q12-5 25 0t25 0" fill="none" stroke="{EVG}" stroke-width="3" stroke-linecap="round"></path>
          <path d="M100 4c-6 9-9 14-9 18a9 9 0 0 0 18 0c0-4-3-9-9-18z" fill="{LIME}" stroke="{EVG}" stroke-width="2.5" class="float9"></path></svg>'''
    if kind == 'moon':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><rect x="0" y="0" width="200" height="150" rx="14" fill="{NIGHT}"></rect>
          <circle cx="100" cy="66" r="34" fill="none" stroke="{MOON}" stroke-width="3" stroke-dasharray="6 7"></circle>
          <path d="M100 108v22M90 122l10 10 10-10" fill="none" stroke="{LIME}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="float9"></path></svg>'''
    if kind == 'hub':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><g transform="translate(40 20) scale(5)" fill="none" stroke="{EVG}" stroke-width=".6" stroke-linejoin="round">
          <path d="M2.00 20.50A10 10 0 0 1 9.75 10.76L11.25 15.15A5.4 5.4 0 0 0 6.60 20.50z" fill="{LIME}"></path><path d="M22.00 20.50A10 10 0 0 0 14.25 10.76L12.75 15.15A5.4 5.4 0 0 1 17.40 20.50z" fill="{LIME}"></path>
          <path d="M8.65 2.16L15.35 2.16L12.75 11.15L11.25 11.15z" fill="#FFFFFF" stroke-dasharray="1 1" class="float9"></path></g></svg>'''
    if kind == 'ripple':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><circle cx="100" cy="75" r="12" fill="{BLUSH_INK}"></circle>
          <circle cx="100" cy="75" r="34" fill="none" stroke="{BLUSH_INK}" stroke-width="3" class="ring9"></circle><circle cx="100" cy="75" r="60" fill="none" stroke="{BLUSH_INK}" stroke-width="3" stroke-opacity=".35"></circle></svg>'''
    if kind == 'stones':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><ellipse cx="40" cy="120" rx="26" ry="10" fill="{EVG}"></ellipse>
          <ellipse cx="88" cy="94" rx="26" ry="10" fill="none" stroke="{EVG}" stroke-width="3" stroke-dasharray="6 6"></ellipse><ellipse cx="136" cy="66" rx="26" ry="10" fill="none" stroke="{EVG}" stroke-width="3" stroke-dasharray="6 6"></ellipse>
          <ellipse cx="176" cy="38" rx="20" ry="8" fill="none" stroke="{EVG}" stroke-width="3" stroke-dasharray="6 6"></ellipse><circle cx="40" cy="96" r="11" fill="{LIME}" stroke="{EVG}" stroke-width="2.5" class="float9"></circle></svg>'''
    if kind == 'arch':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><path d="M58 140V70a42 42 0 0 1 84 0v70" fill="{MINT}" stroke="{NIGHT}" stroke-width="3"></path><path d="M44 140h112" stroke="{NIGHT}" stroke-width="3" stroke-linecap="round"></path>
          <circle cx="112" cy="82" r="18" fill="#FFFFFF" stroke="{NIGHT}" stroke-width="3"></circle><path d="M125 95l14 14" stroke="{NIGHT}" stroke-width="4" stroke-linecap="round"></path><path d="M106 82h12" stroke="{NIGHT}" stroke-width="3" stroke-linecap="round"></path></svg>'''
    if kind == 'bell':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><circle cx="100" cy="75" r="60" fill="{POOL}"></circle><g transform="translate(64 38) scale(3)" fill="none" stroke="{EVG}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{EXTRA_ICONS['bell']}</g>
          <circle cx="140" cy="44" r="16" fill="{LIME}" stroke="{EVG}" stroke-width="2.5"></circle><path d="M133 44l5 5 9-10" fill="none" stroke="{EVG}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>'''
    if kind == 'offline':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><rect x="0" y="0" width="200" height="150" rx="14" fill="{NIGHT}"></rect><path d="M118 52a26 26 0 1 1-34-24 20 20 0 0 0 34 24z" fill="{MOON}"></path>
          <g transform="translate(118 78) scale(2)" fill="none" stroke="{LIME}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{EXTRA8['wifi-off']}</g></svg>'''
    if kind == 'group':
        import math
        seats = ''.join(f'<circle cx="{100 + 52 * math.cos(math.radians(k * 36 - 90)):.1f}" cy="{75 + 52 * math.sin(math.radians(k * 36 - 90)):.1f}" r="9" fill="#FFFFFF" stroke="{EVG}" stroke-width="2.5" stroke-dasharray="4 4"></circle>' for k in range(10))
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true">{seats}<circle cx="100" cy="75" r="18" fill="{LIME}" stroke="{EVG}" stroke-width="2.5" class="float9"></circle></svg>'''
    if kind == 'error':
        return f'''<svg width="200" height="150" viewBox="0 0 200 150" aria-hidden="true"><ellipse cx="60" cy="118" rx="28" ry="11" fill="{EVG}"></ellipse><ellipse cx="112" cy="90" rx="28" ry="11" fill="{EVG}" transform="rotate(-12 112 90)" class="wobble9"></ellipse>
          <ellipse cx="160" cy="60" rx="24" ry="9" fill="none" stroke="{EVG}" stroke-width="3" stroke-dasharray="6 6"></ellipse></svg>'''


EMPTY = [
    ('pool', 'Home, no goals yet', 'A goal is a pool you fill at your own pace', 'A car, moving out, a trip home. Start with any amount.', 'Make a goal', 'R8-Goals.dc.html', MIST),
    ('moon', 'Learn, nothing saved', 'Nothing saved for offline yet', 'Save a lesson or a story and it reads without data.', 'Browse the paths', 'R8-Learn.dc.html', MIST),
    ('hub', 'Hub, no tools used', 'Your first tool takes two minutes', 'Start with your payslip: what came off, and why.', 'Decode my payslip', 'R8-Tool-Payslip.dc.html', MIST),
    ('ripple', 'Community, a quiet circle', 'Your circle is quiet today', 'Ask the first question, or share a small win.', 'Ask the circle', 'R8-Compose.dc.html', BLUSH),
    ('stones', 'Me, before the first check-in', 'Your first check-in is on 13 October', 'Each one adds a stone, and a new version of your profile.', 'Set a reminder', 'R7-Auth-Notify.dc.html', POOL),
    ('arch', 'Search, nothing found', 'No words match "staking" yet', 'Try another spelling, or ask Ola to explain it.', 'Suggest it for Words', 'R9-Search.dc.html', MIST),
    ('bell', 'Notifications, all read', "You're all caught up", 'New replies, cheers and reminders will show here.', 'Notification settings', 'R7-Settings.dc.html', MIST),
    ('offline', 'Offline', "You're offline", 'Saved lessons, your tools and your notebook still work. We’ll send anything new when you’re back.', 'See what works offline', 'R9-Help.dc.html', MIST),
    ('group', 'Savings group book, a new group', "Add your group's members", "First names only. AWO never holds or moves the group's money.", 'Add a member', 'R9-Group-Book.dc.html', MIST),
    ('error', 'An error', 'Something went wrong on our side', 'Your answers are safe. Try again in a minute. Reference AWO-5102.', 'Try again', 'R8-Home.dc.html', MIST),
]


def empty_states():
    cards = ''
    for kind, where, head, sub, cta, href, bg in EMPTY:
        cards += f'''<div style="display: flex; flex-direction: column; gap: 10px">
      <span style="font-size: 14px; font-weight: 600; color: {SEC}">{where}</span>
      <div style="width: 320px; height: 400px; box-sizing: border-box; border-radius: 22px; background: {bg}; box-shadow: 0 0 0 1px rgba(16,24,20,.08); padding: 28px 22px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; text-align: center">
        {ill(kind)}
        <span style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; line-height: 1.25; color: {BLUSH_INK if bg == BLUSH else INK}">{head}</span>
        <span style="font-size: 15px; line-height: 1.45; color: {BLUSH_2 if bg == BLUSH else SEC}">{sub}</span>
        <a href="{href}" style="margin-top: 4px; height: 48px; padding: 0 18px; border-radius: {R_M}px; background: {BLUSH_INK if bg == BLUSH else EVG}; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center">{cta}</a>
      </div></div>'''
    body = f'''  <div style="display: grid; grid-template-columns: repeat(5, 320px); gap: 32px 28px">{cards}</div>'''
    css = ('@keyframes float9{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}.float9{animation:float9 3.6s ease-in-out infinite;transform-box:fill-box}'
           '@keyframes ring9{0%{transform:scale(.8);opacity:.9}100%{transform:scale(1.25);opacity:0}}.ring9{transform-origin:100px 75px;animation:ring9 3.2s ease-out infinite}'
           '@keyframes wobble9{0%,100%{transform:rotate(-12deg)}50%{transform:rotate(-6deg)}}.wobble9{transform-box:fill-box;transform-origin:center;animation:wobble9 4s ease-in-out infinite}')
    return board7('Empty states, from the five shapes', 'When there is nothing yet, the area’s own shape says so, and one button says what to do next. The pool waits for its first drop, the stones for the next step. Calm, slow motion; none with reduce motion on.', body, static_logic(), 1880, 1200, css=css, chip='Sample copy. Tap a button to go there.')


BOARDS = [('R9-Comp-Overlays', overlays), ('R9-Comp-Inputs', inputs), ('R9-Empty-States', empty_states)]
