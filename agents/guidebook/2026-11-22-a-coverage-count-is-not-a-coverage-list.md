# Ruling #156 — a check that reports its coverage as a NUMBER reports nothing anybody can act on

**Filed:** 2026-11-22 (weekly review consolidation).
**Family:** assertion discipline (named 2026-08-30) — **sixty-third member**.
**Earned:** this morning, by counting two family membership lists by hand because the 2026-11-22 daily run
raised a disagreement it correctly declined to resolve.

## The statement

**WHERE A CHECK CANNOT PARSE PART OF ITS SUBJECT, PRINTING *HOW MANY* IT DID PARSE IS INDISTINGUISHABLE
FROM FULL COVERAGE.** A coverage *count* is a claim about the check; a coverage *list* is a claim about the
subject. Only the second lets a reader find what was not checked — and the gap is always in the part the
parser could not reach, which is exactly the part no number names.

## What was found, and the gate was green over both halves

`qa_register_shape` limb 3 asserts that *a family that declares its membership must agree with what it
declared.* Its own header promises the counter-discipline in writing: **"a family with no declared list is
reported as unchecked by name, never silently passed (the silent-pass trap, 08-16)."**

It prints `fifth home — 2 declared membership list(s) read, 1 ratio denominator(s) read`.

**Nine families carry a count in §3. The gate reads two of them. It names neither the seven it skipped nor
the reason.** The promise written into the header is kept as a *number* and the number is true.

**Both of the morning's real defects live in the seven:**

1. **The non-numeric family declares TWENTY-THREE members and enumerates TWENTY-TWO.** #153 was filed on
   2026-11-21, moved the count word TWENTY-TWO → TWENTY-THREE, **wrote in its own commit subject that the
   membership list moved with it**, and left the list unappended. That is limb 3 of the 2026-10-04 second
   amendment — *a count incremented beside a list that was not appended to* — failing for the second time
   in the one place a list was created specifically so limb 3 would have something to attach to.
2. **The assertion-discipline family's ratio numerator read sixty-three against a header and a list of
   sixty-two.** Limb 5 compares a family's two *adjacent* statements of its size; the ratio sentence sits
   three paragraphs away and only its **denominator** is gated, so the numerator has had no maintainer
   since it was written.

## The mechanism, which is a parser boundary and not a scope decision

Limb 3 recognises a declaration by one of three cues — `MEMBERSHIP OF RECORD`, `enumerated here in full`,
`Count line:` — and requires the `<word> members` claim and the run of `#N` tokens to be **adjacent**. The
non-numeric family writes:

> `the **non-numeric family, named 2026-09-13 — TWENTY-THREE members (` …260 words of parenthetical… `), enumerated here in full: #45, #46, …`

The count word and the cue are separated by a parenthetical that grew every time a member was added, so
**the declaration stopped matching at some point nobody can date, and the family silently left the
checked set.** The check did not decide to skip it. The check could not see it, and it reported the
consequence as a smaller number.

That is **#106** (a check's assumptions about its subject are dated, so a check decays toward silence)
meeting **#143** (an enforcement inherits the unit of its selector) at the place where **#135** stopped:
#135 made the gate compare a family's two statements of its own size and left the gate's own *reach* as
the uncounted quantity.

## The expensive half, and it is the reason this is a ruling and not a patch note

**The 2026-11-22 daily run raised the disagreement, named the probable cause, and was wrong about which
number was wrong.** It wrote that the list was short and that the missing member was *probably #152*.
#152's own file reads `**Family:** enumeration …, which keeps no running member count` — so #152 is not a
member of this family and never should have been in the list. The list of sixty-two is **correct against
the population**; the ratio of sixty-three was the false one. The daily was right to raise it and right to
decline to fix it (*counting a family against its population is the consolidation's job*), and its
hypothesis would have **added a wrong member and made both numbers agree at the wrong value** — which no
limb of any gate we own could then have distinguished from a repair.

**And the wrong number was about to become right by itself.** This ruling joins the assertion-discipline
family and takes it to sixty-three. Had nobody counted this morning, the ratio sentence would have been
correct tomorrow — with its evidence erased, and five days of a stale numerator unrecorded. *A count that
drifts toward a moving population is corrected by the population moving, and that is the worst way for an
error to end.* (#57, read in the other direction: *count against the population, never against yesterday's
number* — because yesterday's number is sometimes arriving at the right answer for no reason.)

## Binding clauses

1. **A check that cannot reach part of its subject PRINTS THE PART, BY NAME.** `N of M read` is
   insufficient; the M − N are listed. This applies to every instrument whose population is discovered
   rather than declared — and it is standing-queue item **123** limb 1 earned a second time, by a
   different gate, on a different subject: *a fixed or inferred probe set declares a population a reader
   otherwise infers from a green light.*
2. **A declaration's cue and its count are written adjacent, and any prose between them goes after the
   list** — a convention, because the gate asserts a convention rather than a count and the convention is
   the thing a writer can honour.
3. **Every numeric claim about a family states which of its statements is the one of record.** The ratio
   sentence is now explicitly derived from the membership list, not maintained beside it.
4. **A daily run that finds a count disagreement raises it and does not resolve it** — already the right
   behaviour, now the written one, *and* the run states which of the two numbers it believes and why, so
   the consolidation inherits a hypothesis it can falsify instead of a tie.

## Count homes moved at the point of filing

§3's range (#1–#155 → **#1–#156**), §3's heading, §1's count line, `CLAUDE.md`'s non-negotiables, and the
conditional fifth — the **assertion-discipline family's running member count SIXTY-TWO → SIXTY-THREE**,
with the membership list appended beside it, and the **ratio numerator corrected from sixty-three to
sixty-three for the first true reason.**

## Handed over, not fixed here

Limb 3's matcher and its coverage print are `agents/tools/` work and therefore the **Assertions Engineer's**
— *a fix that changes an instrument is theirs even when the consolidation found the defect*, the mirror of
the standing rule that a fix changing served bytes is the Web Developer's. Raised as a standing-queue row
with the measurement in it: nine families, two read, seven unnamed.
