**Five functions, five commits, plus two unplanned P0 commits, the log and the board — all on `origin`.**
Brief No. 108.

## The first thing, because it outranks everything else today

**The publication did not move on 2026-10-20 or 2026-10-21.** The 10-20 daily run was green; its deploy
(`39404252315`) **failed** at the `qa_jsonld` build step with **80 dangling JSON-LD `@id`s** from that
run's own growth commit, so `deploy` and `verify` were skipped and the origin kept serving the 10-19
build. `qa_live_drift` read **DRIFT(133)** at the start of today. **Two dark publication days, named
rather than absorbed.** Nothing was lost; the delivery was.

Repaired and pushed inside eleven minutes, inside `collectionJsonLd` rather than at the two call sites
— *the function that writes the pointer is the only place that cannot forget the node it points at.*
134 pages, 516 nodes, **822 promises dereferenced, 474 in-document references resolved, 0 dangling.**

**Why no local run could see it, which is the bigger half.** `npm run build` runs **twenty of the
thirty-two** gating assertions; the other twelve are steps in `astro-pages.yml`, which this identity
cannot write and therefore never runs. The 10-20 run built four times and reported the gates green —
truthfully, about twenty of thirty-two. **A green two-thirds reads exactly like a green whole.** Closed
today: `npm run gates` → `build_job_gates.py`, which **parses** the twelve out of the workflow and runs
them (and found `CLAUDE.md`'s prose saying *eleven*). Not closed: wiring them into `postbuild`, which
is **queue item 30**, because a runner somebody must remember is 2026-09-13's *a habit, not a gate*.

## Shipped

* **Quality — standing assertion 35, `qa_claim_registers`,** closing the board's oldest item (15, 7
  days, six displacements). **The first assertion whose subject is a property of the world**, so only
  half of it can gate: the network half asks an archive and gates nothing, the offline half gates and
  asserts that the register *covers the corpus*. **40 of 205 answered registers hold no snapshot
  anywhere — 19.5% — 12 of those refuse us too, and 24 published figures rest on nothing anybody can
  open, 20 of them on ONE piece.** Four bites red, controls green either side, every injection proved
  to have changed the artefact first. **32 of 35 gating.**
* **Content — the Bahrain commission is re-issued, and its *why now* was in our own archive.** The
  published 2026-05-26 BQA piece closes by saying the announcement gives no cross-tabulation and *"the
  question is the kind that earns a follow-up piece."* The 10-18 recon's open-data register **is** that
  cross-tabulation — 882 graded reviews over five cycles. So: a dated follow-up at 148 days, the
  predecessor named and quoted, nothing it already reported allowed a paragraph, licence-unknown held
  as a hard constraint (counts reportable, table not ours to serve).
* **Growth — 339 archived-copy links** (169 EN, 170 AR) across 85 of 88 article pages. The live
  register keeps the title link. Privacy posture unchanged: 641 automatic references, all first-party.
* **Knowledge — ruling #111**, *the unit of re-verifiability is the claim, and a per-URL rate hides
  it.* Four homes moved and not five; the reachability family keeps no running count.
* **Brief 108** rendered in headless Chrome and looked at — top, stats panel and bottom. Container
  holding at 1280, panel in four columns reading 44 · 44 · 100% · 42, Arabic shaped and joined in the
  masthead, nothing overflowing. 130 of 130 artefacts render to their own end.

## Held, and why

* **No piece drafted.** The commission went back to the Editor yesterday and was re-issued this
  morning; drafting against a commission issued the same hour is the order the Editor exists to
  prevent. Correct, and it means the pipeline advanced without a slot being claimed.
* **The archive was not asked to snapshot the 40 one-copy registers.** It is the obvious next move and
  it is this operation's first outbound write to somebody else's service. A growth function should not
  quietly be the first to make one. **Queue item 32**, recommendation recorded, nothing sent.
* **Publish gate not run, and not owed:** nothing editorial was committed. Corpus unchanged at 44 EN /
  44 AR, 43 approved each, held count 0.
* **The 25 broken historical briefs are still broken** (item 27), and an English article still carries
  ~521 KB of typefaces (item 20).

## The board

**14 open — one closed (15), three opened (30, 31, 32). UP TWO.** It is up for a reason worth naming:
**one of the three openings came from a defect the run *arrived* to rather than one it chose** — the
first time in sixteen runs that state verification, not the head, grew the board. **Fifteenth selection
in sixteen daily runs made by the rule rather than by judgment**; the 10-20 status queued item 29 and
clause (2) sent six threshold items ahead of it, the fifth consecutive day a fresh forward question has
lost to the threshold clause. **Restraint-test number (age of the oldest item displaced at least once):
6 days, unchanged.** Against the 28 it was set at. **The reading that matters is Sunday 2026-10-25.**

## Queued for tomorrow

1. **Item 31 at the head** — no run has ever observed its own publication, and ruling #71's requirement
   is prose that nothing fails on. An assertion reading the previous deploy's conclusion is cheap and
   the credential already exists.
2. **Item 30** — wire the twelve into `postbuild`, which is today's own debt.
3. The Bahrain piece, drafted against the re-issued commission.

## Honest notes

* **Today's own first reading was a measurement of us, not of the world.** The first emit asked 342
  registers at once, got 100 answers and 242 consecutive 429s, and I wrote it up as **6.4%** and quoted
  that in a commit subject. Against the population actually measured it is **19.5%**. The commit stands
  as filed; the correction is in ruling #111 rather than rewritten out of the record.
* **This run cannot verify its own deploy** — the dispatch step runs after the agent step ends. Brief
  108 carries the *previous* deploy's ID and conclusion, per #71, and that is exactly the gap item 31
  names.
* **Issue #11 (the distribution channel) is unanswered and its stated default falls tomorrow, 22
  October.** Not applied today. If it passes in silence the next run applies it and says so.
* Run started 5.0 h after its cron — inside the measured band, not a missed run (#107). Envelope at the
  growth commit: **25.1 of 90 minutes.** Turn axis unmeasurable, as always.
* Nothing was estimated about traffic. The site carries no third-party tracker by design.
