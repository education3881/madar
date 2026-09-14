# Manager status — 2026-09-14 (run 2, the first cloud run)

## What shipped

**Nothing to readers.** No flag flipped, corpus unchanged at 38 EN / 38 AR. One reader-visible byte
of the *site* changes: the browse pages' accent colour, which is a defect fix.

- **Content.** Edition 05 slot 3 composed in Arabic and gated the same day — Arabic Editor **PASS**,
  held. Four of six pieces now exist in both languages. Two English-side register corrections made
  in the same run, both produced by the crossing itself.
- **Quality.** `qa_css_tokens.py` — the thirteenth standing assertion, wired into CI in the commit
  that proves it, proved four ways. It exists because the question it answers was written down on
  09-09 and skipped for three runs; asked today it found an undefined custom property on 76 pages,
  six hours old.
- **Growth.** Wave packet's fourth caption written; a stale caption on a *different* piece found and
  fixed; a flip-day checklist added so the find becomes a procedure.
- **Research.** Ruling #50 — a correction has a blast radius. Series #1–#50.
- **Brief.** No. 73, the day's second. No. 72 preserved at `2026-09-14-daily-brief-run1.html`.

## What was held, and why

- **The wave.** All four Edition 05 pairs stay `approved: false`. Slot 3 has an Arabic gate and
  nothing more: the Editor's five-test pair verdict and the Verifier's verdict are both still owed,
  and neither is implied by today's PASS. The four pieces are mutually rail-bound and flip
  atomically or not at all.
- **The three confirmation reads** (Zambia, Sierra Leone, Sudan) remain owed at the gate. They did
  not move today; the run spent its content capacity on the Arabic composition, which was the
  ledger's named next step.
- **`show_full_output`** stays on in the daily workflow. The file says to remove it "once the
  cutover is confirmed," and one green run is not confirmation.

## The thing that needs the founder, once

**Today's commit is on `main` and not on the origin.** The push succeeded and started no deploy: a
push made with the Actions token does not trigger workflows, and this run cannot dispatch one
(`actions: read`). Confirmed against production — the live stylesheet still serves the undefined
`--color-accent` on all 76 browse pages, which is the defect this run found and fixed. One **Run
workflow** on *Deploy Astro site to Pages*, or any push of his own, publishes it.

This is the steady state from today, not a one-off, and it is the cutover's unfinished half: the
operation can now work without him and still cannot publish without him. Issue #6 carries it, with
the recommendation changed to *give the run a PAT* and a default of *open a PR instead of pushing*
from 2026-09-20, because a default has to be something the operation can apply by itself.

## Named plainly

Four dispatches of the new daily workflow failed this morning before this one ran. The readable
failure — readable only because the third commit enabled full output — was that the
`CLAUDE_CODE_OAUTH_TOKEN` secret contained **a line break at character 80**. Nothing in this
repository could have fixed it, and two of the three commits chasing it were hypotheses about the
one file we could see. The five automatic failure issues are closed with the cause written on each.

Three consecutive runs (09-10, 09-11, 09-14 run 1) wrote no QA log and therefore named no forward
question, which has been a required written output since 08-23. Resumed today, and the lapse is
recorded in the log rather than papered over.

## Queued

1. **Editor's five-test pair verdict on slot 3** (EN+AR together) — the next run's content work.
2. **Verifier's verdict** on the same pair, one per run, in banking order. Ceiling clear; this
   edition's verification backlog is zero.
3. **Egypt re-verification**, then Rwanda — both in the pipeline since scope closed at six on 09-13.
4. **Three confirmation reads**, interleaved one per run, never batched.
5. **Tomorrow's forward question, before anything new:** nothing this operation owns has ever
   checked that a page *renders*. Thirteen assertions, all structural, zero pixels.
6. **Sunday's consolidation** owes the canonical ruling table a merge: it still ends at #48 while
   #49 and #50 live as register rows.

Gate target for the wave is unchanged — on the origin by **2026-10-11**, outer bound 11-15, and the
ruler piece must be live before PASEC 2024 publishes in the last quarter of 2026. Four pieces
drafted of six, with three pipelines and three confirmation reads still to run. The arithmetic still
has no slack, and the order of sacrifice is still the one stated on 09-13: **the date gives, the
verdicts do not.**

— Manager · 2026-09-14
