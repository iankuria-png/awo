from lib import *

P = 'v2'


def home():
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <div style="display: flex; flex-direction: column; gap: 8px">
        <span style="font-size: 15px; font-weight: 500; color: {MUTED}">Hi Naledi</span>
        <h2 class="d" style="font-size: 54px">It's payday.</h2>
      </div>
      <img class="face" src="{IMG['naledi']}" alt="Naledi" style="width: 44px; height: 44px">
    </div>
    <section style="border-radius: 28px; background: {EVG}; color: #FFFFFF; padding: 20px; display: flex; flex-direction: column; gap: 16px">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 12px">
        <div style="display: flex; flex-direction: column; gap: 8px; padding-bottom: 8px">
          <span style="font-size: 15px; color: {ON_EVG}">Your safety net</span>
          <span class="d" style="font-size: 62px; color: {LIME}; font-variant-numeric: tabular-nums">{{{{ amountText }}}}</span>
          <span style="font-size: 15px; color: {ON_EVG}">of R 5 000</span>
        </div>
        <div style="position: relative; width: 96px; height: 158px; flex-shrink: 0">
          {pool(96, 158, 'v2Pool')}
          <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}">
            <span class="drop" style="left: 26px; top: 64px"></span><span class="drop" style="left: 44px; top: 54px; animation-delay: .12s"></span><span class="drop" style="left: 62px; top: 66px; animation-delay: .24s"></span>
            <span class="splash" style="left: 14px; top: 92px; width: 68px; height: 16px"></span>
          </sc-if>
        </div>
      </div>
      <div style="height: 1px; background: rgba(255,255,255,.16)"></div>
      <div style="display: flex; flex-direction: column; gap: 4px">
        <span style="font-size: 17px; font-weight: 600">This week: pay yourself first.</span>
        <span style="font-size: 15px; line-height: 1.4; color: {ON_EVG}">Move R 100 in before anything else.</span>
      </div>
      <sc-if value="{{{{ notMoved }}}}" hint-placeholder-val="{{{{ true }}}}">
        <button class="pill" onClick="{{{{ doMove }}}}" style="background: {LIME}; color: {EVG}">I moved R 100</button>
      </sc-if>
      <sc-if value="{{{{ moved }}}}" hint-placeholder-val="{{{{ false }}}}">
        <button class="pill" onClick="{{{{ undoMove }}}}" aria-label="Done for this week. Tap to undo." style="background: transparent; color: {LIME}; box-shadow: inset 0 0 0 2px {LIME}; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">{icon('check', 20, LIME, 2.4)}Done for this week</button>
      </sc-if>
    </section>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">
      <section style="height: 150px; box-sizing: border-box; border-radius: 24px; background: {NIGHT}; color: {MOON}; padding: 16px; display: flex; flex-direction: column; justify-content: space-between">
        {moon(40, 'half', now=True)}
        <div style="display: flex; flex-direction: column; gap: 6px"><span class="d" style="font-size: 26px; line-height: .95">Where to keep it</span><span style="font-size: 13px; color: {NMUTED}">Lesson 3, 6 min</span></div>
      </section>
      <section style="height: 150px; box-sizing: border-box; border-radius: 24px; background: {LIME}; color: {EVG}; padding: 16px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
        <span aria-hidden="true" style="width: 32px; height: 40px; box-sizing: border-box; border-radius: 16px 16px 4px 4px; border: 3px solid {EVG}"></span>
        <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; font-weight: 600">Word of the week</span><span class="d" style="font-size: 36px">Stokvel</span></div>
      </section>
    </div>
    <section style="border-radius: 24px; background: {BLUSH}; color: {BLUSH_INK}; padding: 14px 16px; display: flex; align-items: center; gap: 14px">
      <span style="position: relative; width: 44px; height: 44px; flex-shrink: 0">
        <span aria-hidden="true" style="position: absolute; inset: -7px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .22"></span>
        <span aria-hidden="true" style="position: absolute; inset: -14px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .1"></span>
        <img class="face" src="{IMG['wanjiru']}" alt="" style="position: relative; width: 44px; height: 44px">
      </span>
      <span style="font-size: 15px; line-height: 1.35"><strong style="font-weight: 600">Wanjiru</strong> cheered your step</span>
    </section>
  </div>
  {tabbar('Home')}
</div>'''


def learn():
    return f'''<div class="ph dk" style="background: {NIGHT}; color: {MOON}">
  <div class="scr">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <h2 class="d" style="font-size: 56px">Learn</h2>
      <span style="height: 40px; padding: 0 14px 0 6px; border-radius: 999px; background: {RAISED}; display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600">{ola(P, 28)}Ask Ola</span>
    </div>
    <section style="position: relative; border-radius: 28px; background: {DEEP}; padding: 20px; display: flex; flex-direction: column; gap: 10px; overflow: hidden">
      <div style="position: relative; height: 176px">
        <div aria-hidden="true" style="position: absolute; right: 6px; top: 2px; filter: drop-shadow(0 0 28px rgba(134,227,196,.28))">{moon(168, 'half', craters=True, dark=RAISED)}</div>
        <button onClick="{{{{ doOla }}}}" aria-label="Say hello to Ola" style="position: absolute; left: 4px; bottom: -2px; width: 84px; height: 84px">
          <sc-if value="{{{{ olaIdle }}}}" hint-placeholder-val="{{{{ true }}}}"><span style="display: block; animation: bob 3.2s ease-in-out infinite">{ola(P, 84, look=8)}</span></sc-if>
          <sc-if value="{{{{ ola }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="jump" style="display: block">{ola(P, 84, happy=True)}</span></sc-if>
        </button>
        <sc-if value="{{{{ ola }}}}" hint-placeholder-val="{{{{ false }}}}">
          <span style="position: absolute; left: 92px; bottom: 58px; padding: 8px 12px; border-radius: 16px 16px 16px 4px; background: {MOON}; color: {NIGHT}; font-size: 14px; font-weight: 500; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">Ready when you are.</span>
        </sc-if>
      </div>
      <h3 class="d" style="font-size: 40px">Where to keep it</h3>
      <span style="font-size: 15px; color: {NMUTED}">Lesson 3 of 6 in Safety nets. 6 minutes.</span>
      <button class="pill" style="margin-top: 6px; background: {LIME}; color: {INK}">Start the lesson</button>
    </section>
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 4px 0">
      <span style="font-size: 14px; font-weight: 600">Safety nets</span>
      <div role="img" aria-label="Lessons 1 and 2 done, lesson 3 next, 3 more to come" style="display: flex; gap: 10px">{moon(20, 'full')}{moon(20, 'full')}{moon(20, 'half', now=True)}{moon(20, 'new')}{moon(20, 'new')}{moon(20, 'new')}</div>
    </div>
    <div style="display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 12px">
      <section style="border-radius: 24px; background: {RAISED}; padding: 14px; display: flex; flex-direction: column; gap: 10px">
        <span style="position: relative; width: 52px; height: 52px; border-radius: 999px; overflow: hidden; display: block">
          <img class="face" src="{IMG['thandi']}" alt="" style="width: 52px; height: 52px">
          <span aria-hidden="true" style="position: absolute; left: -22px; top: 0; width: 52px; height: 52px; border-radius: 999px; background: rgba(11,15,14,.55)"></span>
        </span>
        <span class="d" style="font-size: 21px; line-height: .98">Stokvels, in three minutes</span>
        <span style="font-size: 13px; color: {NMUTED}">Told through Thandi's story</span>
      </section>
      <section style="border-radius: 24px; background: {RAISED}; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px">
        {moon(28, 'cres')}
        <span style="font-size: 15px; line-height: 1.35">You showed up three evenings this week.</span>
      </section>
    </div>
  </div>
  {tabbar('Learn', dark=True)}
</div>'''


def vault():
    arch = 'border-radius: 175px 175px 28px 28px'
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <h2 class="d" style="font-size: 56px">Vault</h2>
      <span style="font-size: 15px; color: {MUTED}; padding-bottom: 4px">12 words kept</span>
    </div>
    <span style="height: 48px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; gap: 10px; padding: 0 16px; font-size: 15px; color: {MUTED}">{icon('search', 20, MUTED)}Search money words</span>
    <div style="position: relative; height: 330px; perspective: 1400px; flex-shrink: 0">
      <div class="flipper" style="transform: {{{{ flipTf }}}}">
        <section class="face-f" aria-hidden="{{{{ flipped }}}}" style="{arch}; background: {LIME}; color: {EVG}; padding: 84px 26px 22px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 10px">
          <span style="font-size: 13px; font-weight: 600">Word of the week</span>
          <span class="d" style="font-size: 68px">Stokvel</span>
          <span style="font-size: 14px">Say it: stok-fel</span>
          <span style="font-size: 16px; line-height: 1.45; color: {INK}">A savings group. Members pay in every month and take turns to receive the pot.</span>
          <button class="pill" tabindex="{{{{ frontTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; height: 48px; background: {EVG}; color: #FFFFFF">{icon('flip', 18, '#FFFFFF')}Flip for an example</button>
        </section>
        <section class="face-b" aria-hidden="{{{{ notFlipped }}}}" style="{arch}; background: {EVG}; color: #FFFFFF; padding: 84px 26px 22px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px">
          <span style="font-size: 13px; font-weight: 600; color: {LIME}">For example</span>
          <span style="font-size: 18px; line-height: 1.45">Thandi and eleven neighbours each pay R 500 a month. Each month one of them takes home R 6 000. December is Thandi's turn.</span>
          <span class="chip" style="border: 1px dashed {ON_EVG}; color: {ON_EVG}">Sample</span>
          <button class="pill" tabindex="{{{{ backTab }}}}" onClick="{{{{ doFlip }}}}" style="margin-top: auto; height: 48px; background: {LIME}; color: {EVG}">{icon('flip', 18, EVG)}Flip back</button>
        </section>
      </div>
    </div>
    <span style="font-size: 15px; font-weight: 600; padding: 4px 4px 0">Kept lately</span>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px">
      <span style="height: 128px; box-sizing: border-box; border-radius: 56px 56px 18px 18px; background: #FFFFFF; padding: 40px 10px 14px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; text-align: center; gap: 4px"><span class="d" style="font-size: 22px">Safety net</span><span style="font-size: 12px; color: {MUTED}">Saving</span></span>
      <span style="height: 128px; box-sizing: border-box; border-radius: 56px 56px 18px 18px; background: {POOL}; color: {EVG}; padding: 40px 10px 14px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; text-align: center; gap: 4px"><span class="d" style="font-size: 22px">Chama</span><span style="font-size: 12px; color: {SEC}">Saving together</span></span>
      <span style="height: 128px; box-sizing: border-box; border-radius: 56px 56px 18px 18px; background: #FFFFFF; padding: 40px 10px 14px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; text-align: center; gap: 4px"><span class="d" style="font-size: 22px">Interest</span><span style="font-size: 12px; color: {MUTED}">Borrowing</span></span>
    </div>
  </div>
  {tabbar('Vault')}
</div>'''


def community():
    # Eight women around the circle (centre 262,104 inside the tile; radius 72)
    import math
    faces = ['naledi', 'wanjiru', 'amara', 'thandi', 'grace', 'lindiwe', 'zodwa', None]
    ring = []
    for i, f in enumerate(faces):
        a = -math.pi / 2 + i * 2 * math.pi / 8
        x, y = 256 + 70 * math.cos(a) - 19, 104 + 70 * math.sin(a) - 19
        if f:
            ring.append(f'<img class="face" src="{IMG[f]}" alt="" style="position: absolute; left: {x:.0f}px; top: {y:.0f}px; width: 38px; height: 38px; box-shadow: 0 0 0 3px {BLUSH}">')
        else:
            ring.append(f'<span aria-hidden="true" style="position: absolute; left: {x:.0f}px; top: {y:.0f}px; width: 38px; height: 38px; border-radius: 999px; background: {BLUSH_INK}; color: {BLUSH}; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 0 3px {BLUSH}">P</span>')
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr">
    <h2 class="d" style="font-size: 54px">Community</h2>
    <section style="position: relative; height: 206px; flex-shrink: 0; border-radius: 28px; background: {BLUSH}; color: {BLUSH_INK}; overflow: hidden">
      <span aria-hidden="true" style="position: absolute; left: 216px; top: 64px; width: 80px; height: 80px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .18"></span>
      <span aria-hidden="true" style="position: absolute; left: 166px; top: 14px; width: 180px; height: 180px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .12"></span>
      <span aria-hidden="true" style="position: absolute; left: 116px; top: -36px; width: 280px; height: 280px; border-radius: 999px; border: 2px solid {BLUSH_INK}; opacity: .07"></span>
      <span aria-hidden="true" style="position: absolute; left: 248px; top: 96px; width: 16px; height: 16px; border-radius: 999px; background: {BLUSH_INK}"></span>
      {''.join(ring)}
      <div style="position: absolute; left: 20px; top: 22px; bottom: 20px; width: 150px; display: flex; flex-direction: column; justify-content: space-between">
        <span class="d" style="font-size: 32px">Safety net circle</span>
        <span style="font-size: 14px; line-height: 1.4; color: {BLUSH_2}">8 women, one small step a week</span>
      </div>
    </section>
    <section style="border-radius: 24px; background: #FFFFFF; padding: 16px; display: flex; flex-direction: column; gap: 12px">
      <span style="font-size: 13px; font-weight: 600; color: #9C2F52">This week's question</span>
      <span class="d" style="font-size: 30px">What did you say no to this week?</span>
      <div style="display: flex; gap: 8px">
        <span style="flex-grow: 1; height: 44px; border-radius: 999px; border: 1px solid {LINE}; display: flex; align-items: center; padding: 0 16px; font-size: 15px; color: {MUTED}">Share yours</span>
        <span aria-hidden="true" style="width: 44px; height: 44px; border-radius: 999px; background: {BLUSH_INK}; color: {BLUSH}; display: flex; align-items: center; justify-content: center">{icon('send', 18, BLUSH)}</span>
      </div>
    </section>
    <section style="border-radius: 24px; background: #FFFFFF; overflow: hidden; display: flex; flex-direction: column">
      <img src="{IMG['wanjiru_stall']}" alt="Wanjiru at her homeware stall in Nairobi" style="display: block; width: 100%; height: 96px; object-fit: cover; object-position: 60% 32%">
      <div style="padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px">
          <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600">Wanjiru</span><span style="font-size: 13px; color: {MUTED}">Nairobi</span></span>
          <button onClick="{{{{ doCheer }}}}" aria-pressed="{{{{ cheered }}}}" style="position: relative; height: 40px; padding: 0 14px; border-radius: 999px; background: {{{{ cheerBg }}}}; color: {{{{ cheerFg }}}}; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: background-color .18s, color .18s">
            <sc-if value="{{{{ cheered }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="rp" style="inset: 0; color: {BLUSH_INK}"></span><span class="rp" style="inset: 0; color: {BLUSH_INK}; animation-delay: .18s"></span></sc-if>
            {icon('ripple', 18)}{{{{ cheerLabel }}}}<span style="font-weight: 500; opacity: .75">{{{{ cheerCount }}}}</span>
          </button>
        </div>
        <span style="font-size: 15px; line-height: 1.4">Seven evenings of notes. Now I know what the stall really earns.</span>
      </div>
    </section>
  </div>
  {tabbar('Community')}
</div>'''


def me():
    st = stones(300, 78, [(34, 58, 30, 14), (112, 44, 34, 15), (196, 30, 34, 15), (272, 18, 26, 12)],
                [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='5 5')
    # Readiness over time (sample): Aug 55, 1 Sep 59, 13 Sep 63; domain 40..80, plot y 60 (low) .. 14 (high)
    pts = [(24, 55, 'Aug'), (160, 59, '1 Sep'), (296, 63, '13 Sep')]
    y = lambda v: 60 - (v - 40) / 40 * 46
    line = ' '.join(f'{x},{y(v):.1f}' for x, v, _ in pts)
    marks = ''.join(f'<circle cx="{x}" cy="{y(v):.1f}" r="{5 if i < 2 else 6}" fill="{EVG}" stroke="#FFFFFF" stroke-width="2"></circle>' for i, (x, v, _) in enumerate(pts))
    labels = ''.join(
        f'<span style="position: absolute; left: {x - 20}px; top: {y(v) - 26:.0f}px; width: 40px; text-align: center; font-size: 13px; font-weight: {700 if i == 2 else 500}; color: {INK if i == 2 else SEC}">{v}</span>'
        f'<span style="position: absolute; left: {x - 24}px; top: 70px; width: 48px; text-align: center; font-size: 12px; color: {MUTED}">{d}</span>'
        for i, (x, v, d) in enumerate(pts))
    dims = [('Everyday money', 71, False), ('Ready for surprises', 48, True), ('Knowing your options', 60, False), ('Clear goals', 69, False)]
    def tile(n, v, low):
        ring = f'box-shadow: inset 0 0 0 2px {EVG}; ' if low else ''
        tag = ''
        return (f'<div style="height: 88px; box-sizing: border-box; border-radius: 20px; background: #FFFFFF; {ring}padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between">'
                f'<span style="display: flex; align-items: baseline; justify-content: space-between; gap: 6px"><span class="d" style="font-size: 34px">{v}</span>{tag}</span>'
                f'<span style="font-size: 13px; line-height: 1.2; color: {SEC}">{n}</span>'
                f'<span aria-hidden="true" style="height: 6px; border-radius: 3px; background: #E4ECE7; overflow: hidden"><span style="display: block; width: {v}%; height: 100%; border-radius: 3px; background: {EVG}"></span></span></div>')
    tiles = ''.join(tile(n, v, low) for n, v, low in dims)
    return f'''<div class="ph" style="background: {MIST}">
  <div class="scr">
    <div style="display: flex; align-items: center; gap: 14px">
      <img class="face" src="{IMG['naledi']}" alt="Naledi" style="width: 52px; height: 52px">
      <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><h2 class="d" style="font-size: 48px">Naledi</h2><span style="font-size: 13px; color: {MUTED}">Johannesburg, since August</span></div>
      <span aria-label="Settings" role="img" style="width: 44px; height: 44px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('gear', 20, INK)}</span>
    </div>
    <section style="position: relative; border-radius: 28px; background: {POOL}; color: {EVG}; padding: 18px 18px 16px; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 10px"><span class="d" style="font-size: 44px">Stage 2 of 4</span><span class="chip" style="border: 1px dashed {EVG}; color: {EVG}">Sample</span></div>
      <span style="font-size: 15px; line-height: 1.4; color: {INK}">Everyday money is a real strength. Most room to grow: being ready for surprises.</span>
      <div style="position: relative; height: 80px" role="img" aria-label="Stage 2 of 4, shown as four stepping stones">
        {st}
        <img class="face" src="{IMG['naledi']}" alt="" style="position: absolute; left: 94px; top: 6px; width: 36px; height: 36px; box-shadow: 0 0 0 3px {LIME}">
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap"><span class="chip" style="background: #FFFFFF; color: {EVG}">{icon('check', 14, EVG, 2.6)}Reviewed by AWO</span><span class="chip" style="background: rgba(255,255,255,.55); color: {SEC}">Evidence: early</span></div>
    </section>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{tiles}</div>
    <section style="border-radius: 20px; background: #FFFFFF; padding: 12px 14px 10px; display: flex; flex-direction: column; gap: 4px">
      <span style="font-size: 14px; font-weight: 600">Readiness over time</span>
      <div style="position: relative; height: 88px" role="img" aria-label="Overall readiness: 55 in August, 59 on 1 September, 63 on 13 September">
        <svg width="322" height="88" viewBox="0 0 322 88" aria-hidden="true" style="display: block; overflow: visible"><path d="M0 64H322" stroke="#E4ECE7" stroke-width="1"></path><polyline points="{line}" fill="none" stroke="{EVG}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>{marks}</svg>
        {labels}
      </div>
    </section>
  </div>
  {tabbar('Me')}
</div>'''


if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    logic = LOGIC % dict(poolH=158, cheerOn=BLUSH_INK, cheerOff=BLUSH, cheerOnFg=BLUSH, cheerOffFg=BLUSH_INK)
    html = board('Volume 2: Bold',
                 'Bento tiles that wear the colour of the area they open. Big condensed type for the one thing that matters, the shapes as heroes, bigger photos. One ambient motion per screen.',
                 None, [home(), learn(), vault(), community(), me()], 2190, 1150, '#E4EAE6', logic, extra_defs=ola_defs(P))
    open(out, 'w').write(html)
    print('wrote', out, len(html))
