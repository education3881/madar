# Ruling #125 — a decline that names another instrument closes the question for everyone who does not go and look

**Filed** 2026-11-02, by the daily's QA lane, from the standing queue's own head — **item 26 at 15 days**,
the oldest row in OPEN, taken on the second consecutive morning the DEFECT bucket was empty.
**Family:** assertion discipline (**forty-sixth member**).
**Status:** BINDING.

---

## The rule, in one line

**A declined scope is a dated claim about a subject that moves — and when the decline names ANOTHER
INSTRUMENT as the owner of the question, it is a dated claim about that instrument's scope, which is the
harder shape, because a delegate looks like coverage.** A decline that says *nothing checks this* invites
somebody to check it. A decline that says *the instrument next door checks this* closes the question for
every reader who does not go and look. So: **a decline may not name a sibling without naming the limb,
and the run that writes it reads that limb first.**

## What was false

`qa_third_party_origins` is the one instrument whose entire subject is this publication's **privacy
posture** — the CHARTER's *no third-party trackers, ever*, which was a sentence with no number behind it
until 2026-09-18 and a measurement with no gate behind it until 2026-10-08. Its design is a classification
written before any code existed: **by who initiates the fetch, never by origin**, because this publication
points at 235 external origins on purpose and a check that counted those would report our own method as our
largest defect and be switched off inside a week. That design is right and is untouched.

Inside it, one of the three classes was declined. From **2026-10-08 to 2026-11-02** the header read:

> **DECLARATIONS** — markup that names a URL without fetching it, NOT asserted:
> `<link rel=alternate|canonical|author|license>`, `<meta property=og:image>`, `<meta name=twitter:image>`
> — *fetched by a scraper we hand the page to, not by the reader's browser; their format and origin are
> `qa_consumer_surface`'s subject, not this one*

**The format half is true. The origin half was false on the day it was written.**
`qa_consumer_surface` asserts that an `og:image` is a **raster** carrying **alt text** — that is the
2026-08-18 consumer-format rule, and it does that job well. It contains **no origin comparison at all**:
read for a netloc parse, a host set, or a literal origin, the whole file returns three hits, **all three in
prose comments and zero in code.** No other gate covers the class either. So **1,203 declarations across
135 served pages** were handed to a sibling that had never taken the question, and nothing re-read the
sentence for **25 days**.

## Why this class is worth asserting, and why `canonical` comes first

The decline's own wording ranked these by whether the reader's browser fetches them, and that ranking
buries the sharper risk. Split by what a foreign origin would actually **do**:

* `canonical`, `alternate`, `og:url` — **these name us.** A foreign origin here fetches nothing. It tells
  a crawler that **somebody else is the canonical home of our page**, which is worse than a fetch and
  cannot be undone by the reader declining to click. 665 alternates and 134 canonicals are served today.
* `og:image`, `og:image:secure_url`, `twitter:image`, `og:audio`, `og:video` — fetched by a **scraper we
  hand the page to.** The reader's browser does not fetch it; a machine acting on the reader's behalf does.
  That is the same hand-off the instrument exists to refuse, one actor further out — and 2026-08-18 already
  ruled on this surface in the other direction: *a promise in the metadata is a promise to a machine we do
  not own.*

## What shipped

**Limb 2 of `qa_third_party_origins`**, written inside the tool that already parsed and classified these
URLs and merely never asserted them — so the count is derived from the instrument's own enumeration rather
than from a second script that would then be free to disagree with it (#57).

**Measured before anything was asserted (#93):** 1,203 declarations, **0 naming an origin we do not own.**
The floor therefore sits exactly at today's reality rather than above it, which is the condition that makes
the assertion free. *This is the general lesson about kind-C declines read from the other end: a floor is
unaffordable only while the count is non-zero, and nobody had ever taken this count.*

**`author`, `license` and `me` are exempt BY REL, counted and printed, never asserted.** A licence link is
*supposed* to name creativecommons.org. **Zero exist in the corpus today**, and the exemption is written in
advance precisely so the first legitimate one reds nothing — because a gate that reds on correct work gets
"fixed" by deleting the limb, which is item 68's lesson arriving before the defect does.

**The old reason is written out in the header rather than deleted**, following the only precedent in the
register — `qa_artefact_render`'s own *"why the do-not-assert reason above no longer holds, limb by limb."*
A decline that is quietly removed teaches the next run nothing, and the next run is the one that will write
the next decline.

## Proved both ways

| | Injection | Expected | Got |
|---|---|---|---|
| Control 1 | none — the real 135-page `dist` | green | exit 0, 1,203 declarations, 0 foreign |
| Bite 1 | `og:image` → `cdn.example-cdn.net` | red | exit 1 |
| Bite 2 | `canonical` → `medium.com` | red | exit 1 |
| Bite 3 | `alternate hreflang=ar` → `scraper.example.org` | red | exit 1, host and page named |
| Control 2 | `link rel=license` → creativecommons.org | **green** | exit 0, host printed as exempt |
| Control 3 | restore | green | exit 0 |

**And bite 3 did not bite on its first run.** A `sed` delimiter collided with a comma in the expression,
the file was never modified, and the check **exited 0 and printed CLEAN — indistinguishable from a passing
control.** It was caught only by the guard the 2026-09-14 rule requires: the harness compares the injected
file against the original and refuses to read the verdict until the injection is proved to have changed the
artefact. Fourth time this operation has been handed that lesson by its own harness (09-14, #112's fifth
bite, #124's bite 4, today) and **the first time the guard caught it rather than a human noticing
afterwards** — which is what a rule becoming a mechanism looks like.

## The population behind the rule, because item 26 asked for a set and not an instance

**76 declining statements across 21 of the 41 instruments**, of which **20 are genuine declines** — a
measurement taken and deliberately not asserted, with a stated reason. The useful partition is **by the
kind of reason**, because the kind is what tells you what would falsify it:

| Kind | What the reason claims | N | Status 2026-11-02 |
|---|---|---|---|
| **A — delegated to a named sibling** | another instrument owns this | 1 | **FALSE — this ruling** |
| **B — blocked on a permission** | the right home needs a write nobody here holds | 3 | True · issue **#7**, 43 days |
| **C — a #93 floor above today's reality** | a floor here reds every build | 7 | True today; **expires by arithmetic** |
| **D — an oracle or capability limit** | no available instrument can represent this | 6 | True |
| **E — a missing artefact** | there is nothing to check it against | 3 | 1 was FALSE (#106); 2 stand |

**Two of the five kinds have now produced a falsified reason, and item 26 found both** — kind E on
2026-10-18 (`qa_register_shape` declined the fifth home's numerator *because no membership list existed*;
#95 wrote one on 10-11 and nothing re-read the comment) and kind A today. The 10-25 three-item sample's hit
(`qa_live_drift`'s *strictly stronger*) is a sixth decline of its own shape: a claim about a **job** rather
than about an instrument, still open behind kind B's permission.

**Kind C is the one to watch and it is the subject of the successor row (item 71).** Seven declines are
#93 floors, each true only while its own count is non-zero — 408, 42, 7, 91, 129, 15 of 21, median 8%
today. **The day any one reads zero, the decline is stale and the assertion is free**, exactly as the
declarations class became free once somebody counted it; and the one that reaches zero is the one nobody
will look at, because a measurement that has stopped finding anything is the least interesting line in the
output.

## Binding

1. **A decline may not name a sibling instrument without naming the sibling's LIMB**, and the run that
   writes the decline reads that limb before writing the sentence. *Owner, limb, date* — a bare tool name
   is not a delegation, it is a hope.
2. **Every decline carries the date it was written**, so a reader can price it. Of the 20 on the board,
   most do; the ones that do not gain it at the next consolidation.
3. **A decline is re-read when the instrument it names changes, and by the weekly review otherwise** —
   this is kind A's trigger, and it is the one kind whose falsifier is somebody else's commit rather than
   the calendar.
4. **When a decline is overturned, the old reason is written out beside the new limb, never deleted.**

*General form, and it is #57 pointed one desk further out: a count in prose is maintained by nobody, and a
**scope** in prose is maintained by nobody either — but a scope that names a neighbour is worse than one
that names nothing, because it reads as coverage to everybody except the person who opens the neighbour.*

**Related:** #93 (what a check may print and not assert) · #106 (a decline whose artefact arrived and
nothing re-read it) · #75 (derive a number, never copy it) · #57 (count against the population) ·
#35 (prove both ways) · 2026-09-14 (an injection that does not change the artefact) · 2026-08-18 (a promise
in the metadata is a promise to a machine we do not own) · #116 (the queue head that reached this row).
