# Manager status — 2026-10-01 (Thursday, Asia/Dubai)

**State at open:** tree clean, `HEAD == origin/main` at `db96c0d`, no dark day. **The item yesterday
owed this run is answered green, and asked the right way round for the first time:** `db96c0d` — the
run's *final* commit, not the one the write-up named — deployed as **`36707820004`**,
`workflow_dispatch`, **success**, 83 seconds, created 24 seconds after the commit was written. The
eight-fixture `qa_a11y_lang` self-test shipped yesterday passes in CI. `qa_live_drift` CLEAN, 120 URLs,
0 drift, at open and again after today's edits.

**One instrument failed mid-session and it is named, not absorbed:** the `gh` API credential worked at
11:01Z and was refused `HTTP 401` at 12:18Z. `git ls-remote origin` still answers, so the push lands
normally — but **this run cannot read the conclusion of its own deploy**, and does not pretend to.

## Shipped

**Nothing published.** No `approved:` flag moved. **Sixty-fifth consecutive day** without a new live
piece — Edition 05 ships as one gated wave and the wave is not ready.

## Done

- **THE FLIP WAS REHEARSED FOR THE FIRST TIME AND IT WOULD HAVE GONE RED.** All twelve held files
  flipped in the working tree, full build, all twenty-five gating assertions, then reverted and verified
  `cmp`-identical against a snapshot. **First attempt: build exit 1, `qa_stable_order` with 40
  defects.** The check was wrong, not the site (#63): it read each content file with `.read(8000)` — the
  only bounded read in the toolkit, established by grep — and `approved:` is the **last** key in the
  frontmatter, so the cut selected almost exactly for our most heavily sourced work. **Ten files exceed
  8,000 characters and every one is an Edition 05 file**; all ten were silently counted as held. The
  bug's blast radius is exactly the set the flip moves, which is why it has been green every day.
  Fixed, the derived count now printed, **re-run: exit 0, 135 pages, every gate CLEAN**, plus the twelve
  CI build-step assertions run by hand against the flipped artefact.
- **Zambia's confirmation read CLOSED** — the first of five, and the oldest item on the board
  (`verdicts/2026-10-01-ed05-zambia-confirmation-read.md`). All three owed items disposed and **two new
  defects found and fixed in both languages.** The IICBA brief does not claim the 99% learning-poverty
  figure — its own sentence is *"is estimated by the World Bank, UNESCO, and other organizations"* — and
  the piece said the institute *puts* it there; **the same annotation already carried the onward
  attribution correctly for four other figures inside the same parenthesis.** And **358** was printed
  without the scale the register prints beside it (300 lowest, 625 advanced). EN body **2,298 /
  ≤2,300, no waiver** after three words were handed back in the sentences that spent them; numeral
  multiset confirms both bodies gained exactly `300` and `625`.
- **Ruling #80 — a serving state is observed by a client, and the client is part of the observation.**
  We have recorded `parliament.gov.zm` three times in three weeks and had it wrong three times. The
  certificate is **valid to 10 December 2026**; the host sends only its leaf and publishes the issuing
  intermediate at the address printed inside that leaf, so the chain closes for any browser and fails
  only for our scripts. **The expensive half is that `qa_sources_alive`'s own advice told us to write
  that the reader meets an interstitial** — into twelve annotations. Bucket split, advice rewritten,
  proved both ways against five live hosts.
- **Standing assertion 28, `qa_pair_frontmatter`**, answering the 09-30 forward question. Eleven
  fixtures, control silent on 44 pairs, seven bites on the real tree at one finding each, two recogniser
  bites, wired into `postbuild` in the same commit. **28 assertions, 25 gating.**
- **Ruling #81** — it found the **Egypt pair carrying no `arabicVersion`**, alone among 44 English
  articles, and the served consequence was measured rather than inferred: **0 hreflang alternates
  against a control's 3, no `workTranslation` node, no link to its own twin.**
- **Ruling #82**, from inside my own proof harness: a guard asserting *the injection landed* by asking
  `git diff` is wrong for the one bite that matters, because that bite is a revert of an uncommitted fix.
- **A measured negative result, recorded so nobody re-attempts it:** numeral-multiset parity over
  `sources[]` disagrees on **117 of 338** shared annotations with essentially no defects among them —
  quote-plus-gloss doubling (#72), numeral-word rendering, ISO-against-prose dates. Named as work, not
  shipped half-built.
- **Four counts moved at the point of filing**, and a **fifth home** for a moving number found and named
  rather than silently changed. Reconciled by counting: **82 §3 rows, 78 §1 rows**, no gaps, no
  duplicates.

## Named rather than absorbed

- **A grep pattern of mine matched inside `m`*ad*`ar/`** and reported a bite as not biting; the Egypt
  conclusion was briefly the opposite of the truth. That is the 09-14 masking rule committed by the run
  quoting it.
- **My injection guard threw away the day's best bite**, and the harness's `git checkout --` restore
  then deleted the morning's fix; four later bites ran on a contaminated tree. Ruling #82.
- **Yesterday's cache diagnosis named one of two homes** — the stale entry was in
  `web/node_modules/.astro`, not `web/.astro`.
- **`CLAUDE.md` has said "twelve" while listing eleven** since `qa_patch_queue` landed on 09-29. Fixed;
  it now names thirteen and says thirteen.
- **One claim I wrote today was too broad and was corrected before the commit** — *twenty-three of
  twenty-four assertions read `dist`* — by counting both homes instead of remembering them. The true
  statement is narrower and still the finding: 22 of 25 are handed `dist`, five reach into
  `web/src/content/**`, and **none has ever examined the HTML a held piece will serve.**

## Held, and why

- **Four confirmation reads remain** — Sierra Leone, Sudan, slot 3, Egypt. Sudan's is the largest.
- **The Editor's open option** on the Kigali teacher's voice in Rwanda. Unchanged, not blocking.
- **The Arabic Editor's two register questions** on the ruler pair, and the gate on six packet captions.
- **The font self-hosting work.** Untouched a sixth day. Two of five families are Arabic; it needs a run
  of its own, and saying so again is more honest than half-doing it.
- **`qa_sources_alive` stays a live P1 at lower severity** — it completed today, but it still has no
  per-URL deadline and no progress output.

## Queued — next run

1. **Read whether this run's final commit deployed green** — and whether the `gh` credential works at
   open. Two observations, not one.
2. **Tomorrow's named QA question:** which standing beliefs rest on a single undated observation? The
   cheapest candidate is `qa_consumer_surface`'s accepted-format list, a claim about four machines we do
   not own, carried unchanged for six weeks.
3. **The Sudan confirmation read** — four registers riding on one channel.
4. **Re-run the flip rehearsal in the run that composes the flip commit.** Today's green describes a
   tree that will have changed.

- **`madar_stats.py --log` is not idempotent per day.** Running it twice today appended two identical
  snapshots to `agents/stats/history.jsonl`, and week-over-week deltas assume one row per day. The
  duplicate is removed by hand in this commit. The 2026-09-29 desktop observer filed *"--log is a
  write"* as a ruling candidate; it is now a defect with a reproduction. **Queued rather than patched
  at the end of a long run** — a tool change that cannot be proved both ways today is worse than a
  named queue item.

## Owed, carried

The output-bounded `lastmod` manifest (fourteenth time). The absence register. The coverage map. The
brief-integrity assertion. The `sources[]` numeral normaliser, newly named.

**Ten days to the 10-11 gate. Six drafted, six composed, six banked, six verified, one of five
confirmation reads closed — and for the first time, a measured answer to the question of whether the
wave actually builds. It does now. It would not have this morning.**
