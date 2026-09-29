# Ruling #75 — The durable fix for frozen prose about a moving count is not a fresher number; it is prose that carries no number

**Filed:** 2026-09-29, by the daily run testing the 2026-09-28 forward question.
**Family:** assertion discipline / enumeration. The first member about an artefact **no check had ever read**.

---

## The finding

The 2026-09-28 QA log named a surface nothing in this operation had ever looked at:

> Every check this operation owns reads an artefact that a machine produced. Not one reads the
> artefacts a human hand will apply. `git apply --check` proves a patch *applies*; nothing proves
> what it would then *assert*.

Asked deliberately the next morning, it failed on first contact, on a real staged patch, **one day
after that patch had been refreshed by a weekly review whose explicit job was to refresh it.**

`agents/patches/2026-09-20-issue-6-default-c-gate-register-comment.patch` adds a comment to
`.github/workflows/astro-pages.yml` answering *what gates the deploy?*. Applied to a scratch tree
on 09-29 it writes four claims, all wrong:

| claim | patch said | tree contained |
|---|---|---|
| standing assertions | 25 | 26 |
| of which gate the deploy | 22 | 23 |
| gated from `postbuild` | TEN | 11 |
| enumerated `postbuild` gates | 10 names | 11 — `qa_feed_direction` absent |

`git apply --check` returned **0** on it. It applied perfectly. It had applied perfectly on every
day it was wrong.

## The cadence was the defect, not the diligence

The 09-27 weekly review did everything its own rule asks: it re-read both open patches, found this
one stale by four assertions, regenerated it from a real diff, refreshed the counts, and re-verified
with `git apply --check`. It then wrote the standing rule *the weekly review re-reads every open
patch against current state.*

**It went stale again in one day**, because assertion 26 (`qa_feed_direction`) landed on Monday
09-28 and the next review is the following Sunday. A patch reconciled weekly against a count that
moves daily holds a wrong number **six days in seven**.

That is the **2026-09-20 cadence rule** arriving in the one directory the 09-20 fix did not reach:
*a document maintained on a slower clock than the work it describes is not out of date by accident
— it is out of date by design, and the fix is to move the cheapest part of the maintenance onto the
faster clock.* The guidebook's range moved to the point of filing and has been true since. The
patch queue was left on the weekly clock, and the 09-27 amendment's own question — *where else does
this number live? Grep for it; do not remember it* — was asked of `CLAUDE.md` and the patch queue's
two homes, and not of the patch **contents**.

## The ruling, in two parts

**1. The instrument was measuring the wrong property, and a green on the wrong property is worse
than no green.** `git apply --check` answers *will this land?*. Nothing answered *is what it lands
true?*. **Standing assertion 27, `qa_patch_queue.py`**, answers the second: it derives the register
from the three homes that actually hold it (`agents/tools/`, the workflow's build steps,
`web/package.json`'s `postbuild`), reads every numeric claim out of every file in the queue — for a
`.patch`, the **added** lines and the `Subject:`, because context lines are the tree quoted back
rather than a new claim — and fails the build when a staged claim disagrees. Wired to `postbuild`
in the commit that proved it, per the 2026-09-13 rule.

**2. And the part that generalises past this queue: the durable fix is prose that carries no
number.** The issue-6 comment has now been written three times in nine days — *seven / 21 / 19* on
09-20, *ten / 25 / 22* on 09-27, *twelve / 27 / 24* had today's run simply refreshed it again — and
each version was wrong within days. Refreshing a number resets a fuse; it does not remove one. The
re-staged patch therefore **states no count at all**. It explains the split, names the two homes,
notes that two `postbuild` gates are handed the repository root rather than `dist`, and points at
`qa_patch_queue.py` as the thing that derives the register on demand and gates it. It reads **0
numeric claims**, which is why it can never be a trap again.

> **A number that lives in three files should be asserted from them, never copied into a fourth —
> least of all into a file the run that finds the error cannot edit.**

## Why this defect class is the worst-shaped one the operation owns

A stale brief misinforms a reader who can check. A stale count in `CLAUDE.md` misinforms the next
run, which can correct it. **A stale patch injects its numbers at the moment a trusting hand applies
it, into the one path the autonomous identity is refused write access to.** The error is created by
the person fixing it, in a file its author cannot reach, on a day nobody is looking. A wrong
unapplied patch is not unapplied work. It is a trap with a delay fuse, and the identity that lights
it cannot put it out.

## Two limbs found while building the instrument, both worth keeping

**Limb A — a check whose population can legitimately be empty cannot use "found nothing" as its
failure signal; it needs a fixture.** Every other assertion here uses the 2026-08-16 silent-pass
guard: *a census that cannot find the numbers it exists to compare has failed, not passed.* This
tool's first draft did the same and **it failed the tree for passing** — within one run, because
part 2 of this very ruling makes an empty result the *goal*. A queue whose staged prose carries zero
claims is a queue that has been fixed. So the failure signal moved off the population and onto the
instrument: nine fixtures of sentences this queue has really carried, each with the extraction it
must produce, asserted before the tree is judged. It earned its keep immediately — it caught a
regression in the same edit that added it (see limb B).

**Limb B — a lookbehind that guards against one wrong read invites the engine to start one
character later.** Reading `22 of 25 gating`, the bare pattern `N gating` returned **25** — the
total, read as the ratio, which is the 2026-09-14 masking trap. Adding `(?<!of )` fixed that
sentence and the regex simply began at `5` instead, yielding **gating = 5**. Both wrong reads
produced a correct *failure* with a wrong *reason* inside it. Fixed with a token-start guard as
well, and both cases are now fixtures. **Generalised: a negative lookbehind constrains one starting
position, not the match — anchor the token, not the neighbourhood.**

## Proved both ways, per #35, and per #74 each injection asserted to have landed where its label says

Control: exit 0 on the real tree, all four queue files, after the patch and the README were
refreshed. Six bites and three controls, each asserting the injection landed on the **labelled**
population before the check ran:

1. a stale `TOTAL:` on an **added** line — fails, names `total` and `gating`
2. a `postbuild` list of the **right length naming the wrong set** — count reads `ok`, the by-name
   comparison reports `MISSING: qa_feed_direction` / `NOT WIRED: qa_live_drift`, fails
3. the **pattern list** corrupted — the fixture fails before any tree is read
4. the **tokenizer scar** (`qa_[a-z0-9_]+` → `qa_[a-z_]+`) — the guard fires on `qa_a11y_lang`'s
   absence, which is the 09-28 defect this run independently reproduced within the hour
5. a stale claim in **README.md**, a `.md` rather than a patch — fails
6. the **real 09-20 patch restored verbatim** — seven claims, six mismatches, two names missing
- **Control A:** the identical false claim on a patch **context** line yields **0 numeric claims**
  — the added-lines scoping is real. (That run exits 1 for a *different and correct* reason: adding
  a context line breaks the diff, so `applies: NO` fires. Read which assertion fired, not the exit
  code — #63.)
- **Control B:** a live claim wrapped in `~~strikethrough~~` is **exempt and printed**, so the
  README can keep an honest record of a superseded number without that record being read as a live
  claim. Tense is deliberately not parsed: a marker a writer sets is legible; a guess about *had
  been* versus *has* is an instrument that fails silently.
- **Control C:** an empty queue reports *clean by absence* and exits 0.

## The general form

*A green check is scoped to what it enumerates* — stated here for the first time about an artefact
**outside the machine entirely**. Every enumeration finding since 2026-08-09 has been about
something a build produced: a flag, a link, a page, a card, a date, a feed field. The 2026-08-23
rule reached the first artefact rendered for a human and still one we *render*. This is the first
about an artefact we **hand over**: work staged for someone else's hand, in a file we cannot write,
carrying our numbers into a place we cannot correct.

**Ask of anything staged for a hand you do not have: what does it assert, and who checks that?**
