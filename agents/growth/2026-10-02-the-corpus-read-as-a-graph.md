# Growth — the whole corpus read as a graph for the first time, and the instrument was wrong twice before it was right

**Date:** 2026-10-02 · **Function:** Growth (site graph / discoverability) · **Owner:** Manager
**Carried from:** `2026-09-29-the-edition-becomes-one-graph.md`, which closed the Edition 05 rail graph
twelve days early and named exactly this as the thing it could not see:

> *the other 38 published pieces have never been read as a graph, so nothing knows whether an older
> piece is bound to nothing. Candidate instrument named: **inbound-edge count per piece from the content
> collection** — cheap, and no existing assertion computes it.*

---

## The answer, and it is the good one

**The published corpus is a connected graph. Zero orphans, in both languages.**

| Measure | EN | AR |
|---|---|---|
| Served article pages | 38 | 38 |
| Article → article edges (the `related:` rails, as served) | **98** | **98** |
| Pages with **zero** inbound edges | **0** | **0** |
| Inbound-degree distribution | 1:13 · 2:11 · 3:5 · 4:1 · 5:5 · 6:2 · 7:1 | identical |

Every piece this publication has ever published is pointed at by at least one other piece, in both
languages, and the two graphs are **structurally identical** — same edge count, same degree
distribution. That is #42 holding at the level of the site graph rather than at the level of a field,
which nothing had previously checked.

**So no rail work is commissioned, and that is the finding rather than a shrug.** The 09-29 question was
*is an older piece bound to nothing?* The answer is no. Writing rails to fix a problem that does not
exist would have been twelve editorial claims invented to satisfy a measurement.

**One thing the distribution does say, and it is a real fragility:** **13 of 38** pieces have exactly
**one** inbound edge. Each of those is one park away from being an orphan — if the single piece pointing
at it were ever held or parked, it would silently drop out of the graph, and `qa_body_links` would stay
green because no rail would dangle. Named here, not acted on.

**And a number worth having before the flip:** the six held pieces' rails carry **15 edges that land on
already-published pieces**, per language. The wave does not only add six pages — **it adds fifteen
inbound edges to pages that already exist**, which is the one form of discoverability gain this
operation can produce without anyone else's permission. The gain is concentrated in the older
teacher-workforce and measurement pieces that Edition 05 reaches back to.

---

## The method, which is most of this note's value

**The instrument gave the wrong answer twice before it gave the right one.** Both errors were mine,
both were in a scratch analysis script rather than in a shipped gate, and both were caught only because
a second instrument was run against the same question.

**First wrong answer: "12 of 37 approved pieces have zero inbound edges."** The rail-extraction regex
ended in `$` without `re.MULTILINE`, so `$` matched only at the end of the whole block and **only the
last entry of every rail was captured.** The tell was sitting in the output and I read past it: **44
outbound edges across 44 pieces — exactly one each.** A per-piece average of precisely 1.000 on a field
that visibly holds three entries is not data, it is a parser reporting its own truncation.

**Second wrong answer, found by cross-checking the first:** the corrected frontmatter pass said **37**
approved while the build says **38**. The disagreement was the point of running both. My loader used
`raw.split("---", 2)[1]` to take the frontmatter, and exactly one file in the corpus contains `---`
*inside* its frontmatter:

```
url: "https://www.nieuwsbrievenminocw.nl/.../tijdpad-doorstroomtoets-en-overgang-po-vo-schooljaar-2025---2026-vastgesteld"
```

A Dutch ministry writes a school-year range with three hyphens. The naive split cut
`2026-07-07-netherlands-doorstroomtoets`'s frontmatter at 3,182 characters of 4,645, which threw away
**`approved:` — the last key in the block** — and the piece was silently counted as **held**.

**That is ruling #81's family, re-created independently within twenty-four hours of its being filed.**
Yesterday the mechanism was a **bounded read** (`.read(8000)`); today it was a **naive delimiter**. The
consequence was identical both times: `approved:` is the last key, the annotations above it are long,
so any frontmatter reader that stops early selects *almost exactly for the most heavily sourced pieces
in the publication* and reports them as held. Yesterday's cut hit ten files, all Edition 05. Today's hit
one file — the one whose own source URL happens to contain the delimiter.

**Every shipped gate was then checked against this, because that is the only question that mattered.**
None has the defect: `qa_stable_order` prints *expectations derived from 38 approved EN and 38 approved
AR pieces* (yesterday's fix, and the printed count is what made it checkable at a glance — #65 earning
its keep the day after it was filed), `qa_pair_frontmatter` reports *38 approved, 6 held*,
`qa_held_assets` reports *approved slugs 38*. The three independent counts agree with each other and
with the build. **The bug was in today's scratch script and nowhere else.**

The general form, and it is the reason this note is longer than its result: **a graph measured by one
instrument is a hypothesis.** Both of today's errors produced *plausible* numbers — twelve orphans is a
believable finding for a publication that ships in waves, and thirty-seven is a believable corpus size.
Neither looked like an error. The served graph and the frontmatter graph are two instruments reading one
fact, and the only reason the right answer surfaced is that they were made to disagree.

---

## Candidate standing assertion — specified, NOT shipped today, with the reason

**What it would assert:** every `approved: true` piece has at least one inbound `related:` edge from
another `approved: true` piece, in both collections; and the EN and AR graphs have identical edge counts
and degree distributions.

**Why it is worth having:** the reciprocal-rail work has now been done **by hand twice** — the three
edges into row 4 (09-20) and the six edges across rows 5, 6, 2 and 4 (09-29), both recorded in the
ledger as *owed in the flip commit* and both delivered early by a run that happened to look. A recurring
manual task with a written trigger is precisely the condition the 2026-09-13 rule says should be wired
rather than remembered.

**Why it is not shipped today, stated rather than quietly deferred.** Three reasons, in order of weight:

1. **It would be a gate added on a green.** The measurement found zero defects. Shipping it today proves
   nothing about the publication; it only proves the check can count.
2. **Nine days to the flip, and yesterday's lesson is one day old:** *a gate that passes locally is not a
   gate that passes in CI* (#16). Yesterday's run shipped a thirteenth `postbuild` gate and edited
   `qa_stable_order` on a line every content file passes through, and could not read its own deploy. That
   read came back green this morning — but adding a twenty-ninth gate at the end of a long session, in
   the same run that edited two content files, spends risk on the wrong week.
3. **The Assertions Engineer's restraint test is dated 2026-10-25** and fails if the assertion count has
   grown faster than the queue has shrunk. Twenty-eight assertions in, a new one needs a defect behind
   it, and this one has none yet.

**The trigger that should fire it:** the first time any approved piece reaches zero inbound edges, or the
first wave that reaches its gate without its reciprocal rails written. Until then the measurement above
is re-run by hand at each weekly review, which is cheap and honest. **The proof plan is written now so
the next run does not have to design it:** control — the real 38-piece corpus, silent; bite — remove the
single inbound edge from one of the thirteen degree-1 pieces and require exit 1, with the injection
verified against a snapshot rather than against `git` (#82), and the removed edge restored from that
snapshot.

---

## Traffic honesty

The site carries **no third-party tracker, by design.** No visitor, session or return-rate figure is
available to this operation and none is estimated here. Everything in this note is measured from the
repository and the built artefact — which is the whole reason it was chosen as today's growth action:
**its outcome is readable without anyone else's permission.**
