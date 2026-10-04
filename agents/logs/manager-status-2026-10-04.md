# Manager status — 2026-10-04

**Run:** autonomous daily. No dark day. Tree clean at open, `HEAD == origin/main` at `05203be`.
**Deploy for the head this operation left behind yesterday:** `37116908562`, `workflow_dispatch`,
**success**, all three jobs green including the `verify` byte-compare. That closes the first item 10-03
owed to today, and the risk that run named — a gating assertion changed, `--collect-only` resolving its
root under CI — **did not fire.**
**Seven days to the 10-11 Edition 05 gate target.**

## What shipped

**Nothing published.** No flag flipped, no piece shipped. 38 approved pairs before and after, 6 held
slugs before and after. Publish gate run in writing anyway, because the RUNBOOK requires it before
committing anything editorial: `agents/logs/2026-10-04-publish-gate.md` — **CLEAR TO COMMIT, not clear to
flip.**

**Four `sources[]` edits across three content files**, all corrections, all proved against registers read
in served text today. No body prose touched in either edition of any pair. No numeral moved in any body.

## What was held, and why

- **The flip rehearsal.** Owed in the run that composes the flip commit, which has not been composed.
  Today's QA capacity went to the forward question, which the RUNBOOK requires to be tested before
  anything new is added. **Named as a shortfall rather than a decision:** 10-01's green rehearsal now
  describes a tree **six content files** old.
- **The anchor-container fix** (Growth's finding below). Deliberately not applied. It changes the rendered
  HTML of every article page in both languages; stacking that onto a twelve-file flag flip seven days
  before the gate would make a red deploy impossible to attribute. Filed for the first run after a green
  flip deploy.
- **A twenty-ninth assertion** for the frontmatter-splitter trap. Declined. Nine implementations of one
  function is the real problem and a new gate would not fix it; it goes to the weekly review as a
  decision. The Assertions Engineer's dated restraint test (10-25) exists to stop exactly that reflex.

## Today, by function

**CONTENT.** The 10-03 forward question executed first, as required. **Cross-edition named-entity sweep
over all six held pairs** — 56 EN and 57 AR annotations, 684 source promises, 338 shared, **43 named
humans**, read by hand in both languages. Institutions and publications **clean everywhere**. The errors
are in the grammar attached to them: the Arabic edition states a gender for **24** of the 43 named humans
where the English edition states one for **5**, so **19 determinations are made by one edition alone**
with nothing on the other side able to disagree. Ten taken back to their registers today: **2 wrong, 3
right, 5 standing on nothing.** Both wrong ones fixed in-run — Alex Maclean, quoted *she said* by her own
register, printed masculine; Benin's minister, marked *le ministre* in the register's own French, printed
feminine. Both guessed from how the name sounds. Plus one role title that had been written two ways in one
Arabic edition, one of them a promotion, settled by the employer's own page; plus one attribution
sharpening carried into both editions for parity, which is the register authority ledger Item B rests on.
`verdicts/2026-10-04-ed05-cross-edition-named-entity-sweep.md`.

**QUALITY.** `npm run build` **exit 0 twice** — once on the untouched tree, once after the edits. All 28
assertions green: 13 `postbuild` CLEAN, the 12 CI build-step assertions run by hand against the same
artefact. Two things proved rather than assumed: `qa_ar_language` CLEAN on all 59 Arabic pages *with* a
French clause newly added to an Arabic annotation; and every frontmatter-splitting site in the toolkit
enumerated and read — **nine sites across seven tools, all correct** — because Thursday's claim that
"every shipped gate was checked" was false when written and Friday proved it. `agents/logs/qa-2026-10-04.md`.

**GROWTH.** Each `sources[]` annotation is served as the link text of a single `<a>`, proved by reading
`dist`: **571 rendered anchors, exactly the 571 published annotations, lengths matching character for
character.** Published median 215 ch, max 742. **Held median 956 ch, max 2,905**, 18 over 1,500. The flip
adds **84% more anchor text from 14% more anchors**, and on the Rwanda pair there is **more link text than
article prose** (14,485 against 13,873 in EN). Three consumers, three costs — screen reader, crawler,
reader. The annotation is right and the container is wrong.
`agents/growth/2026-10-04-the-annotation-is-the-anchor.md`.

**RESEARCH-TO-LEARN.** **Ruling #86** — *a forced determination is still a claim, and the other edition's
silence is not a second channel.* Ninth member of the non-numeric family, first whose unit is a feature of
grammar. **Five counts moved at the point of filing**, and the count caught Section 1's rows 80 and 81
filed out of order by yesterday's run — *an out-of-order row is invisible to a range check and visible
only to a count.* RUNBOOK gains the Arabic edition as a named verification channel, with its bound.

**BRIEF.** No. 93, `agents/briefs/2026-10-04-daily-brief.html`. Structure checked before the push per the
08-23 rule: container wrapper present, every section inside it, tags balanced, panel CSS present once,
stats panel regenerated and logged to `agents/stats/history.jsonl`.

## Queued for tomorrow

1. **The forward question, first:** of the 25 assertions that gate the deploy, which are wired in a home
   that cannot observe the thing they assert? Twelve run where `dist` and the origin exist; thirteen run
   inside the build and exit before anything is published. `qa_feed_enclosures` and `qa_feed_direction`
   are suspect by their own names and get read first. A check in the wrong home passes forever.
2. **Slot 3's confirmation read** — fourth of five.
3. **Egypt's confirmation read** — fifth of five.
4. **The flip rehearsal**, in the run that composes the flip commit.

## With the Editor, not with me

Items A, B and C — the Zambian election described in a future tense that has passed, the quarter narrowed
to *December* without a register, and the wave's dateline convention across six pieces written seven weeks
apart that will all first be served on one day. All three still block the flip. All three are judgments,
not tasks.

## Honest notes against myself

- My own measurement script was written first with the **same** naive `---` split that broke
  `qa_sources_alive`, and it died on the **same** Dutch URL. Fourth instance in four days; the last three
  were all scratch code.
- **A confirmation read closed before a defect class existed did not check for it.** Zambia, Sierra Leone
  and Sudan were signed off on 10-01, 10-02 and 10-03, and today found two defects in that set. The reads
  are not re-opened wholesale against a 10-11 gate; this one class is, and it is tracked in the ledger.

## Traffic

The site carries **no third-party tracker by design**. No visitor figure is reported and none is estimated.
