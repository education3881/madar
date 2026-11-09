# Growth — 2026-11-09 · the archive stopped being an archive, and the hole was opened by our own ship

**Action:** `/editions/` and `/ar/editions/` now carry the pieces that belong to no edition, **derived
from the collection and never hand-listed**, and both pages' opening sentence has been corrected to
describe the publication that actually exists.

**Why this and not something else:** today's content function shipped the first single. The growth
action is the hole that ship opened, found while gating it, in a page a reader navigates by.

---

## What happened, in one paragraph

GitHub issue #13's stated default fell due on 2026-11-08 in silence, so from that date pieces ship as
**singles** against a standing per-piece ledger. A single carries **no `edition` number** — the schema
has always declared the field optional, and `/editions/` has always skipped a null. That is why option B
needed no code change, and it is also why, from the moment the first single shipped this morning, the
Editions page **stopped being an index of the published corpus.** The piece was reachable from both home
pages, both browse surfaces, both feeds and the sitemap — and from no edition.

**That is not an orphan.** The 2026-08-17 rule is satisfied several times over: inbound edges exist, and
the sitemap entry exists. It is the *next* thing, and it needed a different name to be seen at all: the
page whose own kicker reads **"The archive"** was serving an archive with a piece missing from it.

**And the page said so in words.** Its intro read *"Madār publishes in monthly editions. Each one
gathers the issue's pieces under a single editorial question, in both languages."* Every clause of that
was true on 2026-11-08 and the first was false on 2026-11-09. **A served sentence that describes the
publication's own shape expires when the shape changes, and nothing we own compares a sentence to a
shape** — which is #117's family (*a served artefact is read in the reader's present*) pointed at the
chrome instead of at an article body.

## What was built

The page already had the right furniture and it had been built for exactly this reason once before.
**"Standing pieces — Outside the editions"** was added on 2026-08-25 for VALENCE, the 540 KB instrument
that had been served for nine days with no inbound edge from anywhere. A section built to hold one
hand-written exception is now the derived home for a publishing mode.

- `const singles = all.filter((p) => p.data.edition == null).sort(byDateThenSlug)` on both language routes.
- Rendered in the standing block above VALENCE, each with its country and its date through the same formatter the edition blocks use — so the Arabic side keeps `countryAr()` and the `ar-EG` numerals, and the English side keeps the UTC pin that ruling #60 put there.
- **Derived, never hand-listed.** A list that must equal *the current set of pieces outside the editions* is the 2026-06-07 drift defect the sitemap taught us: correct the day it is written and silently wrong the next time a piece ships. The comment at the point of change says so, in both files.

## Measured, both ways, on the built pages

| | EN | AR |
|---|---|---|
| article links **above** the standing boundary (the five editions) | **44** | **44** |
| article links **inside** the standing block | **1** | **1** |
| total | **45** | **45** |
| VALENCE still linked | ✅ | ✅ |
| stale intro sentence still served | ✗ gone | ✗ gone |

45 is the corpus. **The control and the bite are the same measurement:** the 44 edition-held pieces are
untouched and in their editions, and the one edition-less piece appears exactly once and only in the
standing block. If the grouping had been loosened rather than extended, the 44 would have moved.

## What this is NOT, said plainly

**It is not a traffic claim.** The site carries no third-party tracker by design, so this operation
cannot say whether anybody reaches the new piece through this page, and it will not estimate. What can
be said without anyone's permission is structural and is what the CHARTER asks growth to prefer: **a
reader navigating this publication by its own archive could not reach today's piece this morning and can
this afternoon**, and the number of pieces the archive accounts for went from 44 of 45 to 45 of 45.

**It is not a decision about edition scope.** Issue #13 stays open. If a frame arrives, pieces after it
join an edition and this list shortens by itself — which is the point of deriving it.

## Forward

The standing block now has two populations in it with nothing distinguishing them: a published article
and a standalone interactive instrument, both under the heading *Outside the editions*. That reads fine
at one of each. At five singles and one instrument it will read as a miscellany, and the Arabic side
already carries a note on the VALENCE row explaining that its text is English — a per-row exception,
which is where a bucket set starts going wrong (#57/#70). **Named here so the next run can see it
coming, and deliberately not solved today at a population of two.**

— Growth · 2026-11-09
