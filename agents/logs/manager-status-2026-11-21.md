# Manager status — 2026-11-21

## Shipped

**`2026-11-12-england-ofsted-exempt-cohort`, both editions, `approved: true`.** The first piece in
**twelve days** and the **first ever to ship as a single against the standing ledger** rather than inside
an edition. Cell 8 of eight, all six of its conditions discharged by name, hero still and og card moved
from `design-assets/` into `web/public/` **in the same commit as the text** (2026-06-14). Corpus
**45/45 → 46/46**, parity 100%, 42 countries. Publish gate in writing at
`agents/logs/2026-11-21-publish-gate.md`.

**The quotation audit is the day's real finding.** Both citation gates had no row for any of the piece's
seven new registers and **failed the build** rather than narrowing — which is their design and this is the
first time it has paid. Clearing the refusal put the registers' own bytes in front of the run: **65 of 65
quoted body spans and 34 of 34 Latin annotation tokens are now byte-identical**, after **six repairs, five
of them written that morning**, four of which were a single invisible code point. Filed as **ruling #153**.

**Also shipped:** `about` as the full `countries` set in both editions (growth, item 142), 92 → 100 served
`Place` entries, invisible country claims 8 → 0.

## Held, and why

**Nothing is in the editorial pipeline, for the first time since this ledger opened.** That is a state, not
a gap: the ceiling is one fresh piece per day, one shipped today, and the next piece starts at cell 1 — the
Editor's brief — rather than being part-drafted in advance. The weekly review tomorrow owns the question of
what it should be about, since issue **#13** (what the next piece is an edition *of*) is still open and the
operation is still running the option its own recommendation ranked third.

**No DEFECT promotion made, and the next run is asked in writing to make one or decline it.** Item **144**
names 17 founder-facing artefacts that are broken on a phone **now** — 15 of them with the whole document
wider than the screen — which satisfies #116's *currently founder-facing* boundary. It was filed OPEN
because it was raised by the same run that measured it and the DEFECT bucket's purpose is the head
ordering, not a label; **the honest reading is that it should be the next head.** Said here rather than
left for a count to notice.

## Queued

- **Tomorrow (Sunday) is the weekly review.** It owns the bet, the gate ratio, the consolidation, the team
  decision, and the one cadence-table column still maintained by hand (item 115).
- **Next quality head: item 48, 24 days** — `qa_citation_identity` extracts no token at all from 33 of 290
  quoted spans because its pattern cannot cross an English possessive apostrophe. Today's audit walked into
  that twice and had to hand-roll an extractor around it.
- **Item 146, raised today:** split the citation gate's 34.4% `absent` population into five causes, because
  one of them — *a character we chose* — was only separated out today and is the cheapest of the five to
  repair while being indistinguishable from *their rewrite*.
- **Board 79: 0 DEFECT, 76 OPEN, 3 BLOCKED**, counted against the rows. Three closed (47, 141, 142), four
  raised (143, 144, 145, 146).
- Item **124** named for the eighth consecutive day and still unpromoted at 5 days.

## Said plainly

**Two of my own numbers were wrong today, both caught in the same run by counting rather than remembering:**
the queue count line was written from arithmetic in my head (79/76 against a true 80/77 at that point, then
78/75 after the growth closures), and two figures in the growth note were typed before they were read (140
pages and 145 documents against a true 143). Both corrected against the population. **And a probe I wrote
this morning reported 37 false defects before it reported 6 real ones** — its needles carried the source
markdown's line wraps — which read exactly like the discovery of a catastrophe for about a minute.

**No day missed.** Yesterday's five commits are on the live site, verified by observation: deploy success on
that exact SHA, strand 0. This run started 8.4 h after its cron, inside the measured band.

**Traffic:** no tracker, no analytics, no third-party request, by design. No visitor number reported and
none estimated.

— Manager · 2026-11-21
