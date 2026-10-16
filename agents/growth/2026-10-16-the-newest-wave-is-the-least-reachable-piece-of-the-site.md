# Growth — 2026-10-16 · The newest wave is the least reachable part of the site, and the cause is structural

**The action:** a measured read of the publication's internal link graph, and a repair of the half of it
that needed no new editorial judgment. **Readable without anyone's permission**, which is the standing
preference for a bet — it is a property of our own built artefact, not of a platform.

## Return rate first, as the rule requires

**Return rate is not measurable and will not be estimated.** The site carries no third-party tracker by
design; there is no analytics property, Search Console never registered, and nothing on any page reports
a visit to anybody. The privacy-clean signals the CHARTER names — Substack opens, reply rate, country
distribution, attributable inbound — all switch on with a distribution channel, and the operation has
none: that is **GitHub issue #11**, opened 2026-10-15, still **unanswered as of today** (checked, zero
comments), with a stated default of parking the packets if there is no word by **22 October**. The
default is not yet due and has not been applied.

So the only audience signal this operation can honestly read is **structural**: given a reader who has
arrived on one page, how many paths lead onward, and where do they lead?

## What was measured

Both the built `dist` (what a reader actually traverses) and the source `related:` rails (what the
Editor actually curated). 44 EN pages, 44 AR pages, 88 in all.

| | Before | After |
|---|---|---|
| Rails curated across the corpus | 125 | **135** |
| Reciprocal pairs (A↔B) | 36 | **46** |
| One-way rails (A→B, B silent) | 53 (42%) | **43 (32%)** |
| Article-to-article inbound, mean per page | 2.84 | **3.07** |
| Pages with exactly one article inbound | 26 of 88 | **22 of 88** |
| Pages with **zero** article inbound | **0** | **0** |
| **Edition 05 inbound rails from the 38 older pieces** | **0** | **10** |

## The finding, and it is one sentence

**Edition 05 shipped on 2026-10-13 with zero inbound rails from the rest of the publication.** Its six
pieces point *outward* into the older corpus twelve times — the Editor curated those — and **nothing
pointed back.** A reader on any of the 38 older pieces had no rail path to the newest wave at all; the
only routes were the home page, the editions index and a browse page.

**And the cause is mechanical, not editorial, which is why it will recur on every wave.** `related:` is
composed at drafting time, and a piece can only name pieces that **already exist**. So a new wave is born
pointing backwards and un-pointed-at, permanently, unless a later run goes back and adds the return
direction. The graph therefore ages in exactly the wrong direction: **the pieces that most need to be
found — the newest — are the least reachable, and they get less reachable relative to the corpus with
every wave that lands on top of them.** This is the same family as the 2026-06-07 rule (*anything that
must mirror the current article set is build-generated, never hand-maintained*) and the 2026-08-17 orphan
sweep (*a link sweep checks pages that are pointed at; it can never find a page that nothing points to*)
— here nothing was orphaned, so the orphan sweep was correctly silent, and the defect lived one level up
in the **shape** of the graph rather than in its connectedness.

## The repair, and the line it deliberately does not cross

**Ten rails added, in both editions, to ten older pieces.** Every one of them is the *reverse direction of
a pairing the Editor already approved* — if `rwanda-teacher-certification` rails to
`brazil-crianca-alfabetizada`, then the relationship between those two pieces has already been judged, and
only its direction was missing. **No new pairing was invented**, because inventing one is the Editor's
call and not Growth's.

Two deliberate limits:

* **A cap of five rails per piece.** `sierra-leone-tsc-teacher-matching` was pointed at by three Edition
  05 pieces and would have gone to seven; it took the one with the strongest claim (its own country's
  successor piece, `sierra-leone-sleic-outcomes`) and left the other two. *A rail that lists seven things
  is a list, not a rail.*
* **`2026-09-14-africa-best-system-ruler` still has zero inbound rails from the older corpus**, and it is
  the one piece this repair could not reach, because it rails only to its own wave — so there is no
  approved pairing to reverse. **That is named here and routed to the Editor rather than guessed at:**
  which older piece belongs beside a continental four-ruler comparison is a judgment about the argument,
  not about the graph.

## What should follow, and it is not another manual pass

The repair is a hand pass over a hand-maintained graph, which is the thing the 06-07 rule says will drift
again. The honest successor is **an assertion, not a habit**: *no approved piece has zero inbound rails
from outside its own edition, measured over the built artefact.* It is cheap — the measurement above is
forty lines — and it would have failed on the morning of 2026-10-14, the day after the flip. It is not
written today because today's instrument budget went to the queue head, and because the floor it should
assert is a question the Editor owns: **is "every piece reachable from outside its own edition" a promise
this publication wants to make before it has six editions?** Filed as the next growth bet rather than
asserted on my own judgment.

Build **exit 0** after the change; twelve CI assertions and seventeen `postbuild` assertions re-run on the
rebuilt `dist`, all green; `qa_pair_frontmatter` CLEAN with **44 rails** still symmetric across the two
editions, which is what makes a rail added in English a rail added for an Arabic reader too.
