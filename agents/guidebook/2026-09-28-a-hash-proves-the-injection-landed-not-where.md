# Ruling #74 — a hash proves the injection landed, not that it landed where the label says: an injection is located, not merely counted

**Filed:** 2026-09-28, QA lane, caught inside the proof of standing assertion 26.
**Family:** assertion discipline.
**Immediate ancestor:** #66 (inject the defect that shipped) and the 2026-09-14 trap (assert that the
injection changed the file before running the check on it).

## What happened, in one paragraph

Five bites were injected into the *fixed* Arabic and English feeds to prove `qa_feed_direction` fires.
Each was hash-proved to have landed per the 09-14 trap, each fired exit 1, and the run was about to
record five for five. Two of the five were labelled *"dir attribute stripped from one AR item
description"* and *"…from one EN item description"*. Both were implemented as
`text.replace('&lt;div dir="rtl" lang="ar"&gt;', …, 1)` — **replace the first occurrence in the
document.** The same fix had just given the *channel* description that identical wrapper, and the channel
block precedes the first item. So both injections hit the channel description, not an item, and the
check named the channel description — **correctly**. The check was right; the label was wrong.

The hash changed. The experiment was still not the experiment claimed.

## The ruling

> **A hash proves the file changed. It does not prove the file changed where you said it did.** An
> injection is specified by a **location**, and the proof asserts the located target changed *and* that
> the regions the label excludes did not. `replace(..., 1)` is not a location; it is a bet on document
> order, and it is exactly the bet a fix that adds a new occurrence upstream will silently win against
> you.

The corrected procedure, executed the same run:

1. **Find the target block first** — the `<item>` whose `<link>` carries the slug — and mutate inside
   that block only.
2. **Assert the block changed** (`broken != target`), not merely the file.
3. **Assert the excluded region did not change** — the channel block is compared byte-for-byte before
   and after.
4. **Assert the check names the injected target** — the reported field must contain the slug injected,
   not merely some field.

Re-run that way, both bites named `2026-07-28-england-report-cards-first-term/description`, on the side
injected, with the channel untouched. Seven proofs, all located.

## Why this is worth a number rather than a note

Because of what the unlocated version would have banked. As first written, those two bites were the
**only** test that the check enumerates *item* descriptions at all — everything else in the proof set
targeted a title or the channel. Had the assertion been accidentally scoped to channel fields only, the
five-way proof would have been green, the QA log would have recorded *proved five ways*, and 76 item
descriptions would have been enumerated by nothing. **A mislabelled bite does not merely mis-describe
the test; it silently removes a population from the proof set** — and the artefact of the mistake is a
log entry claiming coverage that was never measured.

This is the 09-14 trap's other half. That one said: *a bite that fails to change the artefact reads
exactly like a passing control.* This one says: **a bite that changes the wrong part of the artefact
reads exactly like a passing bite** — worse, because it produces a red, and a red is what we are looking
for, so nothing prompts a second look.

## General form

> Every claim in a proof is a claim, including the label. When a bite fires, read **what the check
> named** against **what you intended to break**, and treat a mismatch as a failed experiment rather
> than as a passing one. The cheapest instrument is to make the check print the *identity* of the thing
> it faults — a slug, a URL, a field path — so the two can be compared at a glance. A check that reports
> only a count cannot participate in its own proof.

That last sentence is the design rule this ruling leaves behind, and `qa_feed_direction` was written to
it: every defect line names the feed, the slug, the field and the first character that moves.

## Cross-references

- **#66** — inject the defect that shipped, not the bite you wrote. The defect this ruling is about is
  not in the check or in the injection's effect; it is in the **description** of the injection.
- **#35** — prove an assertion both ways, and prove the bite as carefully as the control. "As carefully"
  now includes *located*.
- **#65** — an assertion has two outputs, the verdict and the record. Here the verdict was right and the
  *record the proof wrote* was wrong, which is that ruling aimed at the proof procedure rather than at
  the tool.
- **#57** — a section that claims no count cannot be caught claiming a wrong one. Sibling on the input
  side: a bite that claims no location cannot be caught claiming a wrong one.
