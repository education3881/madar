# Manager status — 2026-09-18

## State at the start of the run, verified from git and the origin

`HEAD == origin/main == 5e1be85`, tree clean, no dark day, no missed run. **And the site
was a day stale.** The 09-17 deploy (`35209579023`, dispatched by the daily workflow's own
publish step) **failed**, so the live origin was still serving the 09-16 build. Everything
yesterday produced was on `main` and unread. Named at the top of the brief with the day
count, per the 2026-09-14 rule.

## What shipped

Nothing to a reader. **No `approved` flips; corpus unchanged at 38 EN / 38 AR.** What
landed in the repository:

- **`qa_lastmod` repaired and strengthened.** The check modelled two of the resolver's
  three branches and failed the deploy on a truthful date. Ceiling is now derived per URL;
  proved five ways, including an isolating bite where the old version prints PASS and the
  new one prints DEFECT on the same file.
- **Standing assertion 18, `qa_arabic_joining.py`**, landed and gated in `postbuild`.
  **16 of 18 assertions now gate the deploy.**
- **Ruling #56** — *a convenience answer is not the index* — with two origin cases from
  today and an amendment on the unsound oracle.
- **Four Editor decisions** (`content-drafts/verdicts/2026-09-18-ed05-editor-decisions.md`)
  closing both items routed out of the 09-17 verification verdict and the Egypt
  draft-blocker.
- **Growth: the third-party surface audit**, the first time the privacy posture has been
  measured rather than asserted.

## What was held and why

- **The Edition 05 wave.** Unchanged and correct. Three confirmation reads owed, reciprocal
  rails owed at the flip, the Arabic Editor's two register questions from 09-15 still
  unanswered, and `qa_sources_alive` still un-schedulable. Today removed the last
  *editorial* obstruction; the remaining ones are operational and can be given run numbers.
- **Self-hosting the five font families.** Recommended, licensed, shaped, and deliberately
  not done. A change that re-renders every page in both editions does not belong in the
  push that repairs a broken deploy.
- **The Egypt draft.** Unblocked today, not drafted today. One piece per day, and today's
  capacity went to the P0.

## What is queued

1. **Confirm the deploy this run triggers went green**, against the live origin and not
   against our own build. First action of the next run, before anything else.
2. **Egypt drafts** — row 5, spine set, two naming traps recorded in advance.
3. **Rwanda re-verification** — row 6, unclaimed since 09-16.
4. **The three confirmation reads**, one per run, interleaved.
5. **The forward question**: `verify` already holds both sides of a per-URL byte
   comparison and discards them. Ask whether it can emit a hash manifest — that is the
   only honest route to a lastmod bounded from below.

## Judgement calls I made, recorded because nobody was asked

- **Fixed the deploy before testing the forward question**, though the standing rule says
  the named surface is tested "before adding anything new." Repairing a red deploy is not
  adding something new, and a red deploy is not a tomorrow problem.
- **Refused the one-line fix** for `qa_lastmod` (widen the ceiling to include
  `web/public`). It would have worked today and re-opened a closed leak.
- **Departed from my own recorded view on Egypt.** I had written that the spine should be
  the absent enrolment figure. As Editor I ruled otherwise: the absence is a limit, not a
  thesis, and the edition's posture is positive by the founder's frame. The Manager's view
  for the record is not the Editor's ruling, and this is the first time the two have
  differed in writing. Both are on file.
- **Shipped assertion 18 in the same run as the P0.** Arguable. The oracle, the control and
  the bites were all in hand from the experiment the forward question required, and the
  09-13 rule forbids leaving a proved assertion ungated. Splitting it would have meant
  proving it twice.

## Nothing is owed by the founder

No open founder decision. Issue #6 remains open as a record and needs no reply — its
recommendation was implemented, and today is the first day that implementation has been
observed failing and recovering.

— Manager · 2026-09-18
