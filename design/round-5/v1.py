from lib import *

P = 'v1'


def row(lead, title, sub, last=False, chev=True):
    border = '' if last else f'border-bottom: 1px solid #EEF2EF; '
    c = icon('chev', 18, MUTED) if chev else ''
    return (f'<div style="{border}min-height: 64px; display: flex; align-items: center; gap: 12px">{lead}'
            f'<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">{title}</span>'
            f'<span style="font-size: 13px; color: {MUTED}">{sub}</span></span>{c}</div>')


def dot(bg, inner):
    return f'<span aria-hidden="true" style="width: 38px; height: 38px; flex-shrink: 0; border-radius: 999px; background: {bg}; display: flex; align-items: center; justify-content: center">{inner}</span>'


def home():
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr" style="gap: 16px">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 15px; font-weight: 500; color: {MUTED}">Hi Naledi</span><h2 class="d" style="font-size: 42px">It's payday.</h2></div>
      <img class="face" src="{IMG['naledi']}" alt="Naledi" style="width: 40px; height: 40px">
    </div>
    <section style="border-radius: 28px; background: {EVG}; color: #FFFFFF; padding: 20px; display: flex; flex-direction: column; gap: 14px">
      <div style="display: flex; align-items: center; gap: 18px">
        <div style="position: relative; width: 58px; height: 96px; flex-shrink: 0">
          {pool(58, 96, 'v1Pool', static=True, rimw=2.5)}
          <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="splash" style="left: 4px; top: 52px; width: 50px; height: 12px"></span></sc-if>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <span style="font-size: 14px; color: {ON_EVG}">Your safety net</span>
          <span class="d" style="font-size: 46px; color: {LIME}; font-variant-numeric: tabular-nums">{{{{ amountText }}}}</span>
          <span style="font-size: 14px; color: {ON_EVG}">of R 5 000</span>
        </div>
      </div>
      <div style="height: 1px; background: rgba(255,255,255,.16)"></div>
      <div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600">This week: pay yourself first.</span><span style="font-size: 14px; color: {ON_EVG}">Move R 100 in before anything else.</span></div>
      <sc-if value="{{{{ notMoved }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="pill" onClick="{{{{ doMove }}}}" style="height: 48px; background: {LIME}; color: {EVG}">I moved R 100</button></sc-if>
      <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="pill" onClick="{{{{ undoMove }}}}" aria-label="Done for this week. Tap to undo." style="height: 48px; background: transparent; color: {LIME}; box-shadow: inset 0 0 0 2px {LIME}">{icon('check', 20, LIME, 2.4)}Done for this week</button></sc-if>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">
      {row(dot(NIGHT, moon(18, 'half', dark='#3A4541')), 'Where to keep it', 'Lesson 3 of 6, 6 minutes')}
      {row(dot(LIME, icon('arch', 18, EVG)), 'Word of the week: Stokvel', 'Tap to learn it')}
      {row(f'<img class="face" src="{IMG["wanjiru"]}" alt="" style="width: 38px; height: 38px">', 'Wanjiru cheered your step', 'Safety net circle')}
      {row(dot(POOL, icon('stones', 18, EVG)), 'Your check-in is on 13 October', 'See what changed since August', last=True)}
    </section>
  </div>
  {tabbar('Home')}
</div>'''


def learn():
    return f'''<div class="ph dk" style="background: {NIGHT}; color: {MOON}">
  <div class="scr" style="gap: 16px">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <h2 class="d" style="font-size: 42px">Learn</h2>
      <button onClick="{{{{ doOla }}}}" style="height: 44px; padding: 0 14px 0 6px; border-radius: 999px; background: {RAISED}; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">
        <sc-if value="{{{{ olaIdle }}}}" hint-placeholder-val="{{{{ true }}}}">{ola(P, 30)}</sc-if>
        <sc-if value="{{{{ ola }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="jump" style="display: block">{ola(P, 30, happy=True)}</span></sc-if>Ask Ola</button>
    </div>
    <section style="border-radius: 28px; background: {DEEP}; padding: 20px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px; font-weight: 600">Safety nets</span><span style="font-size: 13px; color: {NMUTED}">Lesson 3 of 6</span></div>
      <div role="img" aria-label="Lessons 1 and 2 done, lesson 3 next, 3 more to come" style="display: flex; gap: 10px">{moon(22, 'full')}{moon(22, 'full')}{moon(22, 'half', now=True)}{moon(22, 'new')}{moon(22, 'new')}{moon(22, 'new')}</div>
      <div style="height: 1px; background: {NLINE}; margin: 4px 0"></div>
      <h3 class="d" style="font-size: 34px">Where to keep it</h3>
      <span style="font-size: 14px; color: {NMUTED}">6 minutes. One question at the end.</span>
      <button class="pill" style="margin-top: 4px; height: 48px; background: {LIME}; color: {INK}">Start the lesson</button>
    </section>
    <section style="border-radius: 20px; background: {RAISED}; padding: 0 16px; display: flex; flex-direction: column">
      <div style="border-bottom: 1px solid {NLINE}; min-height: 66px; display: flex; align-items: center; gap: 12px">
        <span style="position: relative; width: 40px; height: 40px; border-radius: 999px; overflow: hidden; flex-shrink: 0"><img class="face" src="{IMG['thandi']}" alt="" style="width: 40px; height: 40px"><span aria-hidden="true" style="position: absolute; left: -17px; top: 0; width: 40px; height: 40px; border-radius: 999px; background: rgba(11,15,14,.55)"></span></span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Stokvels, in three minutes</span><span style="font-size: 13px; color: {NMUTED}">Told through Thandi's story</span></span>{icon('chev', 18, NMUTED)}
      </div>
      <div style="min-height: 66px; display: flex; align-items: center; gap: 12px">
        <span style="width: 40px; display: flex; justify-content: center">{moon(26, 'new')}</span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">When business is slow</span><span style="font-size: 13px; color: {NMUTED}">New, 5 minutes</span></span>{icon('chev', 18, NMUTED)}
      </div>
    </section>
    <span style="font-size: 14px; color: {NMUTED}; padding: 0 4px">You showed up three evenings this week.</span>
  </div>
  {tabbar('Learn', dark=True)}
</div>'''


def vault():
    words = [('Safety net', 'Saving'), ('Chama', 'Saving together'), ('Interest', 'Borrowing')]
    rows = ''.join(row(dot(MIST, icon('arch', 18, EVG)), w, c, last=(i == 2)) for i, (w, c) in enumerate(words))
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr" style="gap: 16px">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h2 class="d" style="font-size: 42px">Vault</h2><span style="font-size: 14px; color: {MUTED}; padding-bottom: 4px">12 words kept</span></div>
    <span style="height: 48px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 16px; font-size: 15px; color: {MUTED}">{icon('search', 20, MUTED)}Search money words</span>
    <div style="position: relative; height: 262px; perspective: 1400px; flex-shrink: 0">
      <div class="flipper" style="transform: {{{{ flipTf }}}}">
        <section class="face-f" aria-hidden="{{{{ flipped }}}}" style="border-radius: 28px; background: {LIME}; color: {EVG}; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px">
          <div style="display: flex; justify-content: space-between; align-items: flex-start"><span style="font-size: 13px; font-weight: 600">Word of the week</span>{icon('arch', 22, EVG)}</div>
          <span class="d" style="font-size: 50px">Stokvel</span>
          <span style="font-size: 14px">Say it: stok-fel</span>
          <span style="font-size: 15px; line-height: 1.45; color: {INK}">A savings group. Members pay in every month and take turns to receive the pot.</span>
          <button class="pill" tabindex="{{{{ frontTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; height: 44px; background: {EVG}; color: #FFFFFF">{icon('flip', 18, '#FFFFFF')}Flip for an example</button>
        </section>
        <section class="face-b" aria-hidden="{{{{ notFlipped }}}}" style="border-radius: 28px; background: {EVG}; color: #FFFFFF; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
          <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; font-weight: 600; color: {LIME}">For example</span><span class="chip" style="border: 1px dashed {ON_EVG}; color: {ON_EVG}">Sample</span></div>
          <span style="font-size: 17px; line-height: 1.45">Thandi and eleven neighbours each pay R 500 a month. Each month one of them takes home R 6 000. December is Thandi's turn.</span>
          <button class="pill" tabindex="{{{{ backTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; height: 44px; background: {LIME}; color: {EVG}">{icon('flip', 18, EVG)}Flip back</button>
        </section>
      </div>
    </div>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">{rows}</section>
  </div>
  {tabbar('Vault')}
</div>'''


def community():
    def trio(a, b, c):
        return ('<span aria-hidden="true" style="display: flex; flex-shrink: 0">' + ''.join(
            f'<img class="face" src="{IMG[x]}" alt="" style="width: 30px; height: 30px; margin-left: {0 if i == 0 else -10}px; box-shadow: 0 0 0 2px #FFFFFF">'
            for i, x in enumerate((a, b, c))) + '</span>')
    circles = [(('thandi', 'grace', 'amara'), 'Safety net circle', '8 women'), (('wanjiru', 'zodwa', 'lindiwe'), 'Side hustles', '24 women'), (('grace', 'thandi', 'lindiwe'), 'Stokvel treasurers', '12 women')]
    rows = ''.join(row(trio(*f), t, s, last=(i == 2)) for i, (f, t, s) in enumerate(circles))
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr" style="gap: 14px">
    <h2 class="d" style="font-size: 42px">Community</h2>
    <section style="border-radius: 28px; background: {BLUSH}; color: {BLUSH_INK}; padding: 18px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; font-weight: 600; color: {BLUSH_2}">This week's question</span>{icon('ripple', 22, BLUSH_INK)}</div>
      <span class="d" style="font-size: 30px">What did you say no to this week?</span>
      <div style="display: flex; gap: 8px">
        <span style="flex-grow: 1; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; padding: 0 16px; font-size: 15px; color: {MUTED}">Share yours</span>
        <span aria-hidden="true" style="width: 44px; height: 44px; border-radius: 999px; background: {BLUSH_INK}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</span>
      </div>
    </section>
    <span style="font-size: 15px; font-weight: 600; padding: 2px 4px 0">Your circles</span>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 0 16px; display: flex; flex-direction: column">{rows}</section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; gap: 10px">
        <img class="face" src="{IMG['wanjiru']}" alt="" style="width: 36px; height: 36px">
        <span style="flex-grow: 1; font-size: 15px; font-weight: 600">Wanjiru <span style="font-weight: 400; color: {MUTED}">Nairobi</span></span>
        <button onClick="{{{{ doCheer }}}}" aria-pressed="{{{{ cheered }}}}" style="position: relative; height: 40px; padding: 0 14px; border-radius: 999px; background: {{{{ cheerBg }}}}; color: {{{{ cheerFg }}}}; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s">
          <sc-if value="{{{{ cheered }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span></sc-if>
          {icon('ripple', 18)}{{{{ cheerLabel }}}}<span style="font-weight: 500; opacity: .75">{{{{ cheerCount }}}}</span>
        </button>
      </div>
      <span style="font-size: 15px; line-height: 1.4">Seven evenings of notes. Now I know what the stall really earns.</span>
    </section>
  </div>
  {tabbar('Community')}
</div>'''


def me():
    st = stones(150, 34, [(16, 24, 14, 7), (54, 18, 16, 8), (96, 13, 16, 8), (134, 8, 13, 6.5)],
                [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='4 4')
    dims = [('Everyday money', 71), ('Ready for surprises', 48), ('Knowing your options', 60), ('Clear goals', 69)]
    rows = ''.join(
        f'<div style="{"" if i == 3 else "border-bottom: 1px solid #EEF2EF; "}padding: 12px 0; display: flex; flex-direction: column; gap: 8px">'
        f'<span style="display: flex; justify-content: space-between; font-size: 15px"><span style="font-weight: {600 if v == 48 else 500}">{n}</span><span style="font-weight: 600; font-variant-numeric: tabular-nums">{v}</span></span>'
        f'<span aria-hidden="true" style="height: 6px; border-radius: 3px; background: #E4ECE7; overflow: hidden"><span style="display: block; width: {v}%; height: 100%; border-radius: 3px; background: {EVG}"></span></span></div>'
        for i, (n, v) in enumerate(dims))
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr" style="gap: 14px">
    <div style="display: flex; align-items: center; gap: 12px">
      <img class="face" src="{IMG['naledi']}" alt="Naledi" style="width: 46px; height: 46px">
      <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><h2 class="d" style="font-size: 40px">Naledi</h2><span style="font-size: 13px; color: {MUTED}">Johannesburg, since August</span></div>
      <span aria-label="Settings" role="img" style="width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('gear', 20, INK)}</span>
    </div>
    <section style="border-radius: 28px; background: {POOL}; color: {EVG}; padding: 18px; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px"><span class="d" style="font-size: 34px">Stage 2 of 4</span><span role="img" aria-label="Stage 2 of 4, shown as stepping stones">{st}</span></div>
      <span style="font-size: 15px; line-height: 1.4; color: {INK}">Everyday money is a real strength. Most room to grow: being ready for surprises.</span>
      <div style="display: flex; gap: 8px; flex-wrap: wrap"><span class="chip" style="background: #FFFFFF; color: {EVG}">{icon('check', 14, EVG, 2.6)}Reviewed by AWO</span><span class="chip" style="background: rgba(255,255,255,.55); color: {SEC}">Evidence: early</span><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">Sample</span></div>
    </section>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 2px 16px; display: flex; flex-direction: column">{rows}</section>
    <span style="font-size: 13px; color: {MUTED}; padding: 0 4px">Version 3, 13 September. Next check-in on 13 October.</span>
  </div>
  {tabbar('Me')}
</div>'''


if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    logic = LOGIC % dict(poolH=96, cheerOn=BLUSH_INK, cheerOff=BLUSH, cheerOnFg=BLUSH, cheerOffFg=BLUSH_INK)
    html = board('Volume 1: Clean',
                 'Calm mist screens. Each screen gets one block in its area colour, the shapes stay small, and condensed type is saved for the one thing that matters.',
                 None, [home(), learn(), vault(), community(), me()], 2190, 1150, '#E4EAE6', logic, extra_defs=ola_defs(P))
    open(out, 'w').write(html)
    print('wrote', out, len(html))
