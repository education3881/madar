# The related rail only points backwards in time — measured, and three edges turned round

**2026-11-02 · growth function · [WD] work routed by the Manager.** Raises standing-queue **item 72**.
No founder decision, no credential, no third party: the outcome is readable in this repository.

## The question nobody had asked

The `related:` rail is **the publication's only reader-facing path from one piece to another.** The
browse pages group by country and theme, the editions index groups by wave, the feeds are
reverse-chronological — but the rail is the only thing that says *this piece and that piece are about the
same question.* `qa_body_links` asserts that every rail slug **resolves**; `qa_reachability` asserts every
page is reachable from its own front door. **Neither has ever asked which direction the rail points.**

## What the graph actually looks like

Measured over all 44 approved EN pieces and all 44 AR, from frontmatter:

| | Before | After |
|---|---|---|
| Directed edges inside the corpus | 135 | **138** |
| Reciprocated | 92 | **98** |
| One-way | 43 | **40** |
| Pieces with zero inbound rail | **0 of 44** | 0 of 44 |
| Pieces with zero outbound rail | **0 of 44** | 0 of 44 |
| Dangling targets | **0** | 0 |

Connectivity is **clean**, and both editions are byte-identical in their rails — the parity the
Arabic edition is supposed to have, confirmed rather than assumed. So this is not an orphan finding.

**The finding is in the 43 one-way edges, and it is a clock rather than a mistake: 34 of 43 point from a
newer piece to an older one.** Five point forward, four join pieces published the same day.

That asymmetry is not carelessness and could not have been avoided one piece at a time. **A rail is
curated when a piece is written, and at that moment the only pieces that exist are the older ones.** Every
follow-up this publication has ever written could point back at what it follows up; not one of them could
point forward, because the thing doing the pointing did not exist yet. So the rail is **structurally
retrospective**, and nothing ever goes back.

## Why that costs a reader something real

**Sixteen published pieces are pointed back at by a newer piece and offer no forward path of their own.**
The worst of them:

| Piece | Later pieces that point back at it | Forward paths it offers |
|---|---|---|
| `2026-06-20-oman-school-performance-ratings` | **5** | 0 |
| `2026-06-17-korea-aidt-reversal` | **4** | 0 |
| `2026-06-08-sierra-leone-tsc-teacher-matching` | 3 | 0 |
| `2026-06-25-brazil-crianca-alfabetizada` | 3 | 0 |
| `2026-05-25-bo-teacher-chalk` | 2 | 0 |
| `2026-06-10-rak-iqra-arabic-diglossia` | 2 | 0 |

**And the direction of the loss is the opposite of harmless.** The older piece is the one with the longer
accumulated exposure — more inbound rails, more time in the feeds, more time in whatever indexing happens
to a site with no tracker on it. **It is the likelier landing page**, and it is precisely the page from
which the publication's own later work on the same question is invisible. A reader who arrives at Oman's
school ratings has five later Madār pieces about published school performance and no route to any of them.

This is the **2026-08-17 orphan rule's own shape, one level in**: that rule found a page nothing pointed
at, and this finds a page nothing points *onward* from. *A link sweep checks pages that are pointed at; it
can never find a page that nothing points to* — and it cannot find a page whose pointers all point into
the past either.

## What was changed today, and why only three

**Three forward rails added, each in both editions — 6 files.** Every one is a pair where the later piece
is about the **same instrument**, so the relation was already the Editor's judgment in one direction and
turning it round asserts nothing new:

| From (older) | To (newer) | Why the pair is symmetric |
|---|---|---|
| Oman school performance ratings | England report cards, first term | both are a regulator publishing school-level verdicts |
| Korea AIDT reversal | Philippines MTB-MLE reversal | both are a government withdrawing a flagship policy |
| Sierra Leone TSC teacher matching | Rwanda teacher certification | both are a teacher workforce counted against its own register |

**The other 31 were deliberately not touched, and the reason is not time.** A rail entry is an *editorial*
claim that two pieces are about one question — the schema calls it *editor-curated* — and a one-way edge
is not evidence that the reverse edge is warranted. Chile's SIMCE return and Australia's NAPLAN reset both
point at Oman, and both are national **assessments** where Oman is school-level **inspection**: close
enough for a later piece to cite as context, not necessarily close enough to put on the older piece's rail
as onward reading. **Reciprocating all 34 mechanically would convert an editorial judgment into a graph
operation**, which is the thing this rail exists not to be. So the class is raised for the Editor as item
72 rather than swept.

Verified after the change: `npm run build` **exit 0**, all 38 gating assertions green, `qa_body_links`
PASS (every rail slug resolves), `qa_pair_frontmatter` clean on 44 pairs, and the EN and AR rails still
identical piece for piece.

## No traffic figure

The site carries **no third-party tracker by design**, so there is no visitor number here and none is
estimated. What is measurable without anyone's permission is the graph itself, and that is what is
reported: 138 edges, 98 reciprocated, 40 one-way, 34 of those pointing into the past.

## The honest limit of today's action

Three edges of thirty-four is **not** a fix of the class, and the rail's asymmetry will regrow by itself:
every piece published from now on adds backward edges and no forward ones. **A defect that regenerates
with each unit of normal work is not closed by a sweep, it is closed by a step in the workflow** — which
is why item 72's real ask is one line in the commission template, not a one-off reciprocity pass. The
Bahrain draft verdicted this morning declares three `related:` entries, all three backward, and the pieces
it will be a follow-up to will be unreachable from it on the day it ships unless somebody adds the
forward edge at that moment.
