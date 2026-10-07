# Ruling #90 — A partly derivable claim is partly assertable; the half that resists is a named debt, never a reason to skip the half that does not

**Filed:** 2026-10-07, at the point of filing, by the daily run's QA lane.
**Family:** assertion discipline — **twenty-eighth member**, and the first about
*how much of a claim* an instrument should take on when it cannot take all of it.
**Lane:** standing-queue **item 3**, raised 2026-09-13 at the weekly review, displaced
from the head **six** times, **24 days**. Reached the head today by the one-queue
rule's displacement clause and the 10-05 tiebreak (*among items past the
three-displacement threshold, the oldest goes first*) — it was the oldest past
threshold with an age on the board, and the rule chose the day's first job for the
**third consecutive run**.

---

## The rule

> **When a claim is only partly derivable from the files on disk, derive the part
> that is and assert it. Record the rest as a debt with its size.** Declining the
> whole claim because one half resists leaves the checkable half with no owner —
> and the checkable half is the one that will go stale, because it looks as settled
> as the half that genuinely cannot be computed.

Corollary, which is the shape this was found in: **when a count and a ratio quoting
that count sit in the same paragraph, they are two homes, not one.** A rule that says
*move the family's count* moves the number with the label on it and leaves the number
inside the sentence.

---

## What happened

Standing-queue item 3 asked for an assertion that computes the guidebook's `#1–#N`
range, §1's row count **and the shape of every row in both tables** from the files on
disk. It was specified on 2026-09-13 and displaced six times. It shipped today as
**standing assertion 30, `qa_register_shape`**, and it found three things, in
ascending order of interest.

### 1. The shape limb bit on first contact, outside every file the hand-run had covered

Twenty-one malformed rows have been repaired **by hand** in the three days before
today: five in §3 on 10-04, twelve in §1 on 10-05, three wrapped rows in the Edition
05 ledger plus the queue row that *specifies this check* on 10-06. The 10-06 run
generalised the scope in writing — *every hand-maintained markdown table the operation
keeps* — and ran the check over **seven files, 34 tables, 255 rows**.

The real scope is **715 files, 430 tables, 2,866 data rows.** The hand-run had covered
**7.9%** of the tables. The remaining 92% held **three** malformed rows, and all three
were outside the seven files:

- `content-drafts/recon/2026-08-17-ed05-egypt-baccalaureate.md:27` — three cells in a
  four-column table **since the document's first write, 51 days**, with the row's
  draft-blocking note sitting inside the *Status* cell and *What it carries*
  rendering blank. (Checked rather than assumed: the blocker behind it was
  superseded by the 09-16 re-verification, so this is shape only.)
- `content-drafts/verdicts/2026-09-08-zambia-free-education-act-verification.md:211`
  and `…/2026-09-09-sierra-leone-sleic-outcomes-verification.md:242` — **the same row
  in both**, two cells in a three-column EN/AR table, so the **AR column rendered
  blank** on the one table in each verdict whose entire purpose is to show both
  editions checked. Twenty-nine and twenty-eight days, through a pair verdict, a
  verification verdict and a confirmation read each.

**Two verdicts, two drafters, one row is a property of the template, not a slip** —
the identical diagnosis the 09-13 review made of the `annotation == sentence` defect.
The judgment in both was re-measured before the missing cell was written rather than
copied from the cell beside it: every file bearing either slug and carrying an
`approved:` line reads `false`, in both collections. What was wrong was that **a blank
cell and a cell saying *one sweep covers both* were recorded identically** — #83's
distinction between *wrong* and *unverifiable*, one surface over.

### 2. The four-count rule became a gate, and the proof harness corrected the tool

The 2026-09-20 rule — *a filing run moves §3's range, §3's heading, §1's count line,
and the ruling range quoted in `CLAUDE.md`* — is now **derived and asserted** rather
than remembered. Seven runs executed it correctly by hand; it still leaked twice in
its first three days (09-23 no §1 count, 09-25 no §3 row). That is the 2026-09-13
ruling exactly: *a hand-run assertion is a habit, not a gate.*

**And the tool's own proof harness failed on one bite and changed the tool.** The
headerless-row injection **passed**, because a table header was governing to
end-of-file and the orphan row happened to be the same width as a table 140 lines
above it. A header's authority now ends at the next heading. All three candidate
scopes — end-of-file, end-of-h2, end-of-any-heading — are **equally silent on the real
tree**, so the strictest was free; it was simply never chosen, because nothing had
asked. *A control that passes tells you nothing about scope. Only a bite does.*

Two more things the measurement decided rather than the design:

- **Fenced code must be skipped.** `|| [ $? -eq 3 ]` in a bash fence in the
  operation's own patch queue is a shell or-operator. A shape check that does not
  know about ``` reports every piped shell command in its own documentation as a
  defect — 2026-09-14's input-side question, *where does the string I am looking
  for also legitimately appear?*
- **Continuation blocks inherit.** §1 and §3 are not tables; they are 11 and 9
  pipe-blocks separated by prose with one header between them. A checker demanding a
  header per block calls 18 of INDEX.md's 21 blocks headerless.

### 3. The finding that earned the ruling: the fifth home has two halves, and only the uncheckable half was honoured

The 10-04 amendment's limb one adds a **conditional fifth** count a filing run owes —
the register family's own running member count. Yesterday's run moved it,
TWENTY-SIX → TWENTY-SEVEN, and **recorded that the membership list it should be
reconciled against does not exist**: a derivation from this register's own labels
reached **24 of 27**, and the remaining three were filed as a debt owed to the 10-11
review rather than invented to balance the number. That was the right call and it is
not what this ruling criticises.

**What it criticises is what happened to the other half of the same sentence.** Three
sentences below the count line, in the same bullet, the family's quotable ratio read:

> *"**twenty-six of eighty-eight** rulings, nearly three in ten of everything the
> operation has written down"*

— against a true twenty-seven of eighty-nine. **The numerator is not derivable. The
denominator is exactly derivable: it is the register's own size.** And it was stale.

This has happened before and was *named* before. The **2026-10-04 consolidation found
this identical sentence five members stale** while the count line three sentences above
it was right, and repaired it — recording the reason nobody had caught it, which is
worth keeping: **the ratio held.** *A quarter* was true at 17/71 and true at 22/86, so
the sentence read correctly while both its numbers were wrong. It was then moved
correctly on **10-05** and missed again on **10-06**, by the run that was moving the
count line immediately above it.

So: a home named as a defect on Sunday, honoured on Monday, dropped on Tuesday, and
**asserted on Wednesday** — because the derivable half was finally separated from the
undrivable one instead of the pair being carried together as a debt.

---

## Why this is not #57, #70 or #75 restated

- **#57** says count against the population, never against yesterday's number. It
  assumes the population is countable. Here half of one is and half is not.
- **#70** says a bucket set is an enumeration and cannot report a distinction it
  cannot hold. It is about the *list* of homes. This is about **one home containing
  two numbers of different checkability**.
- **#75** says a number living in three files should be asserted from them, never
  copied into a fourth. It is the right instinct and it is why this tool exists — but
  taken strictly it says nothing about a number that can only be *half* asserted, and
  the practical reading on 10-06 was *this one cannot be derived, so record the debt*,
  which left a derivable number unowned for a day.

The new content is the **split**: ask of every claim you decline to assert, *which
part of this could I compute right now?* Assert that part. Carry the remainder with
its size. **A debt with a size is a debt; a debt with no size is a number nobody
maintains**, which is the defect the whole four-count family exists to stop.

---

## The instrument

`agents/tools/qa_register_shape.py` — standing assertion **30**, gated from
`web/package.json`'s `postbuild`, **27 of 30 gating** as derived by `qa_patch_queue`
from its three homes. Two limbs:

- **SHAPE** — every data row of every table in every hand-maintained markdown file
  carries its governing header's field count. Escaped pipes are not delimiters
  (`re.split(r'(?<!\\)\|', row)`, the correction the 10-06 run made to a
  specification that had been wrong for 23 days); fenced code is skipped; a wrapped
  row is its own named finding, because a wrapped row *terminates* its table.
- **REGISTER** — §3's ruling rows are counted and checked contiguous, §1's rows are
  counted, and the result is compared against **every home that quotes it**: §3's
  heading, the series-integrity line, §1's count line **in both its word and its
  numeral form**, `CLAUDE.md`'s non-negotiables, and now the **families list's
  ratio denominators**, scoped to §3 alone so that the dated consolidation blocks —
  which quote ratios that were true when written — stay as written.

**Why it is not in `qa_census`**, stated in the tool rather than left unexplained
(the 09-13 rule): the census cross-checks a printed number against a population it
derives independently from the content collection or `dist`. This tool's populations
are markdown rows and ruling numbers; a census row whose expected value is read from
the same file the tool reads is #57 with two names on it.

**Proved 25 ways, bite first (#74), on a copy of the tree in `/tmp` so a failed
experiment cannot leave a mutation behind** —
`agents/tools/proofs/prove_register_shape.sh`. Controls: the real tree silent on both
limbs and on each limb alone; a correctly **escaped** pipe silent; a shell pipe
**inside** a fence silent; a continuation block after prose silent. Bites: a cell
removed, a row wrapped, an orphan row under a later heading, the same shell pipe with
the fence removed, and each of the five range homes falsified one at a time —
including **§1's count word falsified while its numeral stayed right**, which a
numeral-only check reads as clean. Failure-to-check, all distinguished from clean by
exit code: `INDEX.md` absent, §3's heading renamed, §3 stripped of numbered rows, a
scope containing no tables, a nonexistent root (**exit 3**), no argument (**exit 2**).
Every injection asserts the file's hash changed before the check runs on it.

---

## How to apply it

1. **When you decline to assert a claim, say which half you could have.** "Not
   derivable" is almost never true of a whole sentence.
2. **A count and a ratio quoting it are two homes.** Grep for the number *and* for
   the denominator; do not remember either.
3. **Scope a check on hand-maintained prose to the live sections.** The operation's
   dated records quote numbers that were true when written, and asserting those turns
   its own history into a build failure.
4. **When a bite passes, suspect the scope before the tool.** The headerless-row bite
   passing is what found that a header was governing 140 lines further than it should.
5. **A proof harness is an artefact, and a fixture naming a moving number goes stale
   exactly like a staged patch does (#75).** This harness hardcoded `#89` and `85 rows`
   on its first write, and **all four range bites broke within the hour — because the
   thing they prove moved, by the ruling they prove.** The #74 guard caught it, printing
   *INJECTION DID NOT CHANGE THE FILE* four times rather than letting four
   non-injections read as four passes. That is the guard paying for itself on the day
   it was written, and the lesson is the same one the patch queue learned on 09-29:
   **the harness now derives the range, the count word, the count numeral and the ratio
   from the tree before it falsifies them.** A fixture that must be edited whenever the
   subject changes is a fixture that will be wrong whenever the subject changes.

**The debt this ruling does not discharge, with its size:** the assertion-discipline
family's **numerator** is still not derivable. #90 is appended to the membership list
in the same commit per limb 3, so the recoverable figure moves **24 of 27 → 25 of
28** and **the three members that are not recoverable are the same three as yesterday**
— #73, #74 and #75, which joined on 09-28 and 09-29 in the window before the
conditional-fifth-home rule existed. **Owed to the 2026-10-11 review, unchanged in kind
and unchanged in size**, which is the honest report: today's work made the denominator
assertable and did nothing whatever for the numerator.
