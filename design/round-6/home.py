"""R6-Home: Ian's structure. Hey Naledi, wins as stories, a bento (safety net, 30-day plan,
word of the week), a carousel shared by the community question and a member story, the small
week's step, keep learning, and your profile."""
from lib6 import *

UNSEEN = '#F29BB5'   # a deeper blush so the story ring reads on mist
SEEN = '#C9D3CE'

STORIES = [
    dict(name='Wanjiru', place='Nairobi, 2 hours ago', face='wanjiru', img='wanjiru_stall', pos='60% 35%',
         text='Seven evenings of notes. Now I know what the stall really earns.'),
    dict(name='Amara', place='London, yesterday', face='amara', img='amara_coat', pos='60% 40%',
         text='My safety net went down this month, and it did its job.'),
    dict(name='Thandi', place='Soweto, yesterday', face='thandi', img='thandi_window', pos='55% 40%',
         text='Three lessons in. I finally understand what my stokvel does for me.'),
    dict(name='Grace', place='Durban, 2 days ago', face='grace', img='grace_dancing', pos='40% 20%',
         text='Sixty-one, and I opened my first savings account this week.'),
]


def story_circles():
    out = [f'''<a href="R6-Community.dc.html" aria-label="Share a win of your own" style="display: flex; flex-direction: column; align-items: center; gap: 8px; width: 62px">
        <span style="width: 58px; height: 58px; box-sizing: border-box; border-radius: 999px; border: 2px dashed {EVG}; color: {EVG}; display: flex; align-items: center; justify-content: center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg></span>
        <span style="font-size: 12px; font-weight: 500">Your win</span></a>''']
    for i, s in enumerate(STORIES):
        out.append(f'''<button onClick="[[ open{i} ]]" aria-label="Open {s['name']}'s win" style="display: flex; flex-direction: column; align-items: center; gap: 8px; width: 62px">
        <span style="position: relative; width: 58px; height: 58px; display: block"><span aria-hidden="true" style="position: absolute; inset: 0; border-radius: 999px; border: 2.5px solid [[ ring{i} ]]; transition: border-color .28s"></span>
          <img class="face" src="{IMG[s['face']]}" alt="" style="position: absolute; left: 5px; top: 5px; width: 48px; height: 48px"></span>
        <span style="font-size: 12px; font-weight: 500">{s['name']}</span></button>''')
    return '<div style="display: flex; justify-content: space-between">' + ''.join(out) + '</div>'


def story_overlays():
    out = []
    n = len(STORIES)
    for i, s in enumerate(STORIES):
        segs = ''.join(
            f'<span style="flex-grow: 1; height: 3px; border-radius: 2px; background: rgba(255,255,255,.35); overflow: hidden">'
            + ('<span style="display: block; height: 100%; background: #FFFFFF"></span>' if j < i else
               '<span style="display: block; height: 100%; background: #FFFFFF; transform-origin: left; animation: fill 5s linear both"></span>' if j == i else '')
            + '</span>' for j in range(n))
        out.append(f'''<sc-if value="[[ st{i} ]]" hint-placeholder-val="[[ false ]]">
    <div style="position: absolute; inset: 0; z-index: 20; background: rgba(11,15,14,.78)">
    <div role="dialog" aria-label="{s['name']}'s win" style="position: absolute; left: 0; right: 0; top: 0; height: 844px; overflow: hidden; background: #000000; color: #FFFFFF; animation: storyIn .28s cubic-bezier(.2,.8,.2,1) both">
      <img src="{IMG[s['img']]}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {s['pos']}">
      <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(rgba(0,0,0,.45) 0, rgba(0,0,0,0) 22%, rgba(0,0,0,0) 45%, rgba(0,0,0,.78) 100%)"></span>
      <div style="position: absolute; left: 14px; right: 14px; top: 48px; display: flex; gap: 4px">{segs}</div>
      <div style="position: absolute; left: 16px; right: 10px; top: 62px; display: flex; align-items: center; gap: 10px">
        <img class="face" src="{IMG[s['face']]}" alt="" style="width: 36px; height: 36px; box-shadow: 0 0 0 2px #FFFFFF">
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">{s['name']}</span><span style="font-size: 13px; opacity: .85">{s['place']}</span></span>
        <button onClick="[[ closeStory ]]" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button>
      </div>
      <button onClick="[[ prevStory ]]" aria-label="Previous win" style="position: absolute; left: 0; top: 120px; width: 40%; bottom: 220px"></button>
      <button onClick="[[ nextStory ]]" aria-label="Next win" style="position: absolute; right: 0; top: 120px; width: 60%; bottom: 220px"></button>
      <div style="position: absolute; left: 20px; right: 20px; bottom: 40px; display: flex; flex-direction: column; gap: 16px">
        <span class="chip" style="align-self: flex-start; background: {BLUSH}; color: {BLUSH_INK}">{icon('ripple', 14, BLUSH_INK)}Win this week</span>
        <p class="d" style="font-size: 36px; line-height: .95">{s['text']}</p>
        <div style="display: flex; align-items: center; gap: 10px">
          <button onClick="[[ cheer{i} ]]" aria-pressed="[[ cheered{i} ]]" style="position: relative; height: 48px; padding: 0 20px; border-radius: 999px; background: [[ cheerBg{i} ]]; color: [[ cheerFg{i} ]]; display: flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 600; transition: background-color .18s, color .18s">
            <sc-if value="[[ cheered{i} ]]" hint-placeholder-val="[[ false ]]"><span class="rp" style="inset: 0; color: {BLUSH}"></span></sc-if>{icon('ripple', 18)}[[ cheerLabel{i} ]]</button>
          <span class="chip" style="border: 1px dashed rgba(255,255,255,.7); color: #FFFFFF">Sample</span>
        </div>
      </div>
    </div>
    </div>
  </sc-if>''')
    return '\n  '.join(out)


def bento():
    dots = ''.join(
        f'<span style="width: 8px; height: 8px; border-radius: 99px; background: {EVG if d < 11 else ("#FFFFFF" if d == 11 else "#DCE4DF")};'
        f'{" box-shadow: 0 0 0 2px " + EVG + ";" if d == 11 else ""}"></span>' for d in range(30))
    return f'''<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: 156px 156px; gap: 12px">
      <section class="tile" style="grid-row: span 2; background: {EVG}; color: #FFFFFF; gap: 10px">
        <span class="lbl" style="color: {ON_EVG}">Safety net goal</span>
        <div style="flex-grow: 1; display: flex; align-items: center">{pool(64, 150, 'hPool', rimw=2.5, hole='waterY', label='poolLabel')}</div>
        <span class="d" style="font-size: 40px; color: {LIME}; font-variant-numeric: tabular-nums">R 1 800</span>
        <span class="cap" style="color: {ON_EVG}">of R 5 000. You're over a third of the way.</span>
      </section>
      <section class="tile" style="background: #FFFFFF">
        <span class="lbl" style="color: {MUTED}">30-day plan</span>
        <div style="display: flex; align-items: baseline; gap: 6px"><span class="d" style="font-size: 44px">12</span><span class="cap" style="color: {MUTED}">of 30 days</span></div>
        <div role="img" aria-label="Day 12 of 30" style="margin-top: auto; display: grid; grid-template-columns: repeat(10, 8px); gap: 5px">{dots}</div>
      </section>
      <a href="R6-Vault.dc.html" class="tile" style="background: {LIME}; color: {EVG}">
        <span style="display: flex; justify-content: space-between; align-items: center"><span class="lbl">Word of the week</span>{icon('arch', 20, EVG)}</span>
        <span class="d" style="font-size: 36px; margin-top: 4px">Stokvel</span>
        <span class="cap" style="margin-top: auto; color: {INK}">Say it: stok-fel. Tap to learn it.</span>
      </a>
    </div>'''


def carousel():
    trio = ''.join(f'<img class="face" src="{IMG[x]}" alt="" style="width: 28px; height: 28px; margin-left: {0 if k == 0 else -9}px; box-shadow: 0 0 0 2px {BLUSH}">' for k, x in enumerate(('thandi', 'grace', 'wanjiru')))
    return f'''<section aria-label="From the community" style="display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; justify-content: space-between">
        <span style="font-size: 15px; font-weight: 600">From the community</span>
        <div style="display: flex; align-items: center">
          <button onClick="[[ prevSlide ]]" aria-label="Previous card" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; color: [[ prevCol ]]"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"></path></svg></button>
          <span aria-hidden="true" style="display: flex; gap: 5px"><span style="width: [[ d0w ]]px; height: 6px; border-radius: 99px; background: [[ d0c ]]; transition: width .28s, background-color .28s"></span><span style="width: [[ d1w ]]px; height: 6px; border-radius: 99px; background: [[ d1c ]]; transition: width .28s, background-color .28s"></span></span>
          <button onClick="[[ nextSlide ]]" aria-label="Next card" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; color: [[ nextCol ]]"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"></path></svg></button>
        </div>
      </div>
      <div style="overflow: hidden; margin-right: -20px">
        <div style="display: flex; gap: 12px; transform: translateX([[ trackX ]]px); transition: transform .45s cubic-bezier(.2,.8,.2,1)">
          <article class="tile" style="width: 300px; height: 244px; flex-shrink: 0; background: {BLUSH}; color: {BLUSH_INK}; padding: 18px; gap: 10px">
            <span style="display: flex; justify-content: space-between; align-items: center"><span class="lbl" style="color: {BLUSH_2}">This week's question</span>{icon('ripple', 20, BLUSH_INK)}</span>
            <span class="d" style="font-size: 32px">What did you say no to this week?</span>
            <div style="margin-top: auto; display: flex; align-items: center; gap: 10px"><span style="display: flex">{trio}</span><span class="cap" style="flex-grow: 1">38 women answered</span>
              <a href="R6-Community.dc.html" style="height: 44px; padding: 0 16px; border-radius: 999px; background: {BLUSH_INK}; color: {BLUSH}; font-size: 14px; font-weight: 600; display: flex; align-items: center">Answer</a></div>
          </article>
          <article class="tile" style="width: 300px; height: 244px; flex-shrink: 0; padding: 0; color: #FFFFFF; background: {INK}">
            <img src="{IMG['adaeze']}" alt="Adaeze smiling at her laptop in her studio" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%">
            <span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(rgba(0,0,0,0) 30%, rgba(0,0,0,.8) 100%)"></span>
            <div style="position: absolute; left: 16px; right: 16px; bottom: 16px; display: flex; flex-direction: column; gap: 8px">
              <span style="display: flex; gap: 6px"><span class="chip" style="background: {BLUSH}; color: {BLUSH_INK}">Member story</span><span class="chip" style="border: 1px dashed rgba(255,255,255,.7); color: #FFFFFF">Sample</span></span>
              <span class="d" style="font-size: 27px">Adaeze paid off her store card in five months.</span>
              <span class="cap" style="opacity: .9">The one habit that helped, in three minutes.</span>
            </div>
          </article>
        </div>
      </div>
    </section>'''


def step_row():
    return f'''<section style="border-radius: 20px; background: #FFFFFF; padding: 6px 16px; display: flex; flex-direction: column">
      <div style="min-height: 64px; display: flex; align-items: center; gap: 12px">
        <span style="position: relative; width: 44px; height: 44px; flex-shrink: 0">
          <svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="18" fill="none" stroke="#E4ECE7" stroke-width="5"></circle>
            <circle cx="22" cy="22" r="18" fill="none" stroke="{EVG}" stroke-width="5" stroke-linecap="round" pathLength="100" style="stroke-dasharray: [[ stepDash ]] 100; transform: rotate(-90deg); transform-origin: center; transition: stroke-dasharray .6s cubic-bezier(.2,.8,.2,1)"></circle></svg>
          <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700">[[ stepCount ]]</span>
        </span>
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span class="cap" style="color: {MUTED}">This week's step</span><span style="font-size: 15px; font-weight: 600">Build a starter safety net</span></span>
        <button onClick="[[ toggleStep ]]" aria-expanded="[[ open ]]" aria-label="Show this week's step" style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 999px; background: {LIME}; color: {EVG}; display: flex; align-items: center; justify-content: center"><span style="display: flex; transform: rotate([[ chevRot ]]deg); transition: transform .28s cubic-bezier(.2,.8,.2,1)">{icon('chev', 20, EVG, 2.4)}</span></button>
      </div>
      <sc-if value="[[ open ]]" hint-placeholder-val="[[ false ]]">
        <div style="border-top: 1px solid #EEF2EF; padding: 8px 0 6px; display: flex; flex-direction: column; animation: rise .28s cubic-bezier(.2,.8,.2,1) both">
          <div style="min-height: 44px; display: flex; align-items: center; gap: 12px; font-size: 15px"><span aria-hidden="true" style="width: 24px; height: 24px; border-radius: 99px; background: {EVG}; display: flex; align-items: center; justify-content: center">{icon('check', 14, '#FFFFFF', 3)}</span>Lesson: where to keep it</div>
          <div style="min-height: 44px; display: flex; align-items: center; gap: 12px; font-size: 15px">
            <sc-if value="[[ chosen ]]" hint-placeholder-val="[[ false ]]"><span aria-hidden="true" style="width: 24px; height: 24px; border-radius: 99px; background: {EVG}; display: flex; align-items: center; justify-content: center; animation: pop .45s cubic-bezier(.34,1.56,.64,1) both">{icon('check', 14, '#FFFFFF', 3)}</span></sc-if>
            <sc-if value="[[ notChosen ]]" hint-placeholder-val="[[ true ]]"><span aria-hidden="true" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 99px; border: 2px solid #A9B6AF"></span></sc-if>
            <span style="flex-grow: 1">[[ amountLine ]]</span>
            <sc-if value="[[ notChosen ]]" hint-placeholder-val="[[ true ]]"><button onClick="[[ choose ]]" style="height: 44px; padding: 0 16px; border-radius: 999px; background: {EVG}; color: #FFFFFF; font-size: 14px; font-weight: 600">R 100 a week</button></sc-if>
          </div>
        </div>
      </sc-if>
    </section>'''


def learning_tile():
    return f'''<a href="R4-M4-Lesson.dc.html" class="tile" style="background: {NIGHT}; color: {MOON}; flex-direction: row; align-items: center; gap: 14px; padding: 16px">
      <span style="width: 52px; height: 52px; border-radius: 999px; background: {RAISED}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{moon(30, 'half', dark='#3A4541')}</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><span class="lbl" style="color: {NMUTED}">Keep learning</span><span class="d" style="font-size: 24px">Savings groups, in three minutes</span><span class="cap" style="color: {NMUTED}">Lesson 3 of 6, through Thandi's story</span></span>
      <span aria-hidden="true" style="width: 48px; height: 48px; border-radius: 999px; background: {LIME}; color: {INK}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon('play', 18, INK)}</span>
    </a>'''


def profile_tile():
    st = stones(118, 30, [(14, 22, 12, 6), (46, 17, 14, 7), (82, 12, 14, 7), (110, 7, 10, 5)],
                [EVG, LIME, 'none', 'none'], [EVG, EVG, EVG, EVG], dash='4 4')
    return f'''<a href="R6-Me.dc.html" class="tile" style="background: {POOL}; color: {EVG}; padding: 16px 16px 18px; gap: 10px">
      <span style="display: flex; align-items: center; justify-content: space-between"><span class="lbl">Your profile</span>{icon('chev', 18, EVG)}</span>
      <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><span class="d" style="font-size: 34px">Stage 2 of 4</span><span role="img" aria-label="Stage 2 of 4 as stepping stones">{st}</span></div>
      <span class="cap" style="color: {INK}">Readiness 63. Everyday money is your strength; the most room to grow is being ready for surprises.</span>
    </a>'''


def build():
    body = f'''  <div class="scr" style="bottom: 84px; gap: 18px">
    <header style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px">
      <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {MUTED}">Friday 25 September, payday</span><h1 class="d" style="font-size: 50px">Hey Naledi</h1></div>
      <a href="R6-Me.dc.html" aria-label="Your profile"><img class="face" src="{IMG['naledi']}" alt="" style="width: 44px; height: 44px"></a>
    </header>
    <section aria-label="Wins this week" style="display: flex; flex-direction: column; gap: 12px">
      <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">Wins this week</span>{sample_chip()}</span>
      {story_circles()}
    </section>
    {bento()}
    {carousel()}
    {step_row()}
    {learning_tile()}
    {profile_tile()}
  </div>
  {tabbar6('Home')}
  {story_overlays()}'''
    n = len(STORIES)
    logic = '''class Component extends DCLogic {
  renderVals() {
    const st = this.state || {};
    const story = st.story == null ? -1 : st.story;
    const seen = st.seen || [false, false, false, false];
    const cheers = st.cheers || [false, false, false, false];
    const slide = st.slide || 0;
    const open = !!st.open, chosen = !!st.chosen;
    const N = %(n)d;
    const go = (i) => { const s = seen.slice(); if (i >= 0) s[i] = true; this.setState({ story: i, seen: s }); };
    const v = {
      closeStory: () => this.setState({ story: -1 }),
      prevStory: () => go(story > 0 ? story - 1 : -1),
      nextStory: () => go(story < N - 1 ? story + 1 : -1),
      trackX: slide === 0 ? 0 : -312,
      d0w: slide === 0 ? 18 : 6, d1w: slide === 1 ? 18 : 6,
      d0c: slide === 0 ? '%(evg)s' : '#C9D3CE', d1c: slide === 1 ? '%(evg)s' : '#C9D3CE',
      prevCol: slide === 0 ? '#A9B6AF' : '%(ink)s', nextCol: slide === 1 ? '#A9B6AF' : '%(ink)s',
      prevSlide: () => this.setState({ slide: 0 }),
      nextSlide: () => this.setState({ slide: 1 }),
      open, chosen, notChosen: !chosen,
      toggleStep: () => this.setState({ open: !open }),
      choose: () => this.setState({ chosen: true }),
      chevRot: open ? 90 : 0,
      stepDash: chosen ? 100 : 50, stepCount: chosen ? '2/2' : '1/2',
      amountLine: chosen ? 'R 100 a week, from today' : 'Choose your amount',
      waterY: Math.round(150 * (1 - 1800 / 5000)),
      poolLabel: 'Safety net: R 1 800 of R 5 000'
    };
    for (let i = 0; i < N; i++) {
      v['open' + i] = () => go(i);
      v['st' + i] = story === i;
      v['ring' + i] = seen[i] ? '%(seen)s' : '%(unseen)s';
      v['cheered' + i] = !!cheers[i];
      v['cheer' + i] = () => { const c = cheers.slice(); c[i] = !c[i]; this.setState({ cheers: c }); };
      v['cheerLabel' + i] = cheers[i] ? 'Cheered' : 'Cheer';
      v['cheerBg' + i] = cheers[i] ? '#FFFFFF' : '%(blush)s';
      v['cheerFg' + i] = cheers[i] ? '%(blush2)s' : '%(blushInk)s';
    }
    return v;
  }
}''' % dict(n=n, evg=EVG, ink=INK, seen=SEEN, unseen=UNSEEN, blush=BLUSH, blush2=BLUSH_2, blushInk=BLUSH_INK)
    return phone('Home', body, logic, h=HOME_H)


HOME_H = 1580

if __name__ == '__main__':
    write(sys.argv[1], build())
