# Growth — the first depth census, and the front door is still edition-shaped

**Date:** 2026-11-24 · **Function:** growth (c) · **Instrument:**
`agents/tools/site_graph_depth.py` (new today; a **measurement and a register maintainer, not an
assertion** — no `qa_` prefix, outside the counting glob, so no count in `CLAUDE.md` moves).
**Readable without anybody's permission**, which is the CHARTER's preferred shape for a growth action: it
reads `dist` and nothing else, and no third party has to agree to be measured.

---

## What was measured, and why it is not yesterday's census again

Three instruments already touch this surface and none of them is a **distance**.

- `qa_reachability` gates the deploy and asserts every page is reachable from its own language's front
  door — **a floor of ONE path**, satisfied by one click or five.
- The 2026-08-17 orphan sweep asks the same question from the other end and is satisfied by one inbound
  edge.
- `site_graph_indegree.py` (yesterday) counts how many pages point **at** a piece, and found Morocco's
  Écoles pionnières on the floor at one inbound rail with every gate green — standing-queue item 158.

In-degree is a property of a node. **Depth is a property of the walk a reader takes**, and the two come
apart: a piece with one inbound rail from the home page is one click away, and a piece with three inbound
rails all from other articles can be three. Nothing here had ever measured the walk.

Method: breadth-first search over the built `dist`, per language, from that language's own front door,
following only same-origin links **the pages actually render** — not the rails frontmatter declares, because
a rail that is not rendered is not a path a reader can take (the 2026-08-16 chrome rule's direction).

## The reading — 142 routed pages, 1,992 rendered same-origin links

| From the EN front door | | From the AR front door | |
|---|---|---|---|
| own edition, 1 click | **6** | own edition, 1 click | **6** |
| own edition, 2 clicks | **40** | own edition, 2 clicks | **40** |
| other edition, 2 clicks | 6 | other edition, 2 clicks | 6 |
| other edition, 3 clicks | 40 | other edition, 3 clicks | 40 |
| unreachable | **0** | unreachable | **0** |

**The graph is shallow and it is symmetric.** No published piece is more than **two** clicks from its own
front door, none is more than **three** from the other edition's, and the cross-edition walk costs exactly
one extra click — which is the chrome's language switch doing its job. Nothing is orphaned, in either
direction, which is `qa_reachability` and the orphan sweep confirmed on a population rather than at a floor.

**The first reading of this instrument pooled both editions and had to be corrected before it meant
anything.** From the English door all 92 article pages of **both** editions are reachable, and every one of
the six "deepest" pages was an Arabic page reached through its English pair's language switch. A depth
histogram over two editions from one door measures the bilingual rails, not the walk. That is #111's
denominator lesson arriving on a graph, inside twenty minutes of the tool existing.

## The finding, and it is about WHICH six

Depth is not the lever. **Occupancy of the 1-click slots is**, because those six pieces are the only ones a
reader meets without choosing to browse. Named from the built bytes:

```
articles/2026-08-25-zambia-free-education-act
articles/2026-08-28-sierra-leone-sleic-outcomes
articles/2026-09-01-sudan-cant-wait-to-learn
articles/2026-09-14-africa-best-system-ruler
articles/2026-09-19-egypt-baccalaureate-published-first
articles/2026-09-27-rwanda-teacher-certification
```

**All six are Edition 05.** The front door's featured block reads *أحدث إصدار · Edition 05 — Africa entire ·
Edition 05 · October 2026 · 6 pieces*, with *Read this edition's lead* and *Also this edition · 5 pieces*.

**Two pieces have been published since, and neither appears in it** —
`2026-10-23-bahrain-bqa-five-cycles` (served from 2026-11-09) and
`2026-11-12-england-ofsted-exempt-cohort` (served from 2026-11-22). Both sit at **two** clicks, behind a
browse listing, while a wave whose last piece is **eight weeks older** sits at one.

**And no instrument we own can turn red on it, because the front door is not lying.** Edition 05 *is* the
latest edition: the two singles belong to no edition at all, by the standing ledger's own design. The label
is true, the bytes are right, every gate is green, and the newest work this publication has done is not on
its front page. *A green check is scoped to what it enumerates*, and nothing enumerates **what the front
door chooses to feature.**

## What this is, and what it is not

**It is the structural consequence of issue #13's silence, measured for the first time.** The ledger moved
to per-piece shipping on 2026-11-08 by applying #13's stated default after fourteen days of no reply. The
*pipeline* changed; the *front door* did not, because the front door was built edition-shaped and nobody
had asked what it shows when there is no open edition. The registry stays at five editions, all `closed`,
`hasOpenEdition` false — and the home page's answer to that state is to keep featuring the last closed one.

**It is raised as OPEN and not as a DEFECT, and that is a reading of #116's boundary rather than a
judgment about importance.** A DEFECT names artefacts that are *wrong, broken or unevidenced* now. These
bytes are none of the three. A curation gap is not a defect, the same way a coverage gap is not — and
saying so here costs one paragraph and keeps the bucket able to mean something.

**It is not a rail invented to improve a measurement.** Yesterday's census ended with the same discipline on
item 158, and today's draft declined to rail Morocco into the ADEK piece for exactly that reason. The ask
below is a judgment, with the measurement attached.

## Handed over — standing-queue item 160

*What does the front door feature when the publication ships singles?* Three shapes exist and the choice is
editorial: the newest N pieces regardless of edition; the newest edition **plus** the singles since it
closed; or a lead chosen by the Editor each week. **The Manager routes and does not curate.** The
measurement is on file, the instrument re-runs in one command, and whichever shape is chosen can be read
the same way the next day.

**No traffic figure is estimated anywhere in this note.** The site carries no third-party tracker by
design, so what a reader actually clicked is unknown and is not guessed at. What is measured here is the
*shape of the walk the site offers*, which is ours to read, and the distinction is the whole reason this
measurement is worth taking.

— Growth, 2026-11-24
