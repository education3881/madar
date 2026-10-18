# Ruling #106 — a check's assumptions about its subject are dated

**Filed** 2026-10-18, at the weekly review, by the consolidation that found them.
**Family** assertion discipline — the **thirty-fifth** member, and the first whose subject is a check's
own decision **not** to assert something.
**Instrument** `agents/tools/qa_register_shape.py`, standing assertion 30, built 2026-10-07.

---

## The rule, in one line

**An exemption, a scope and a pattern are each a claim about the subject as it stood on the day the check
was written — and the subject keeps moving.** Nothing re-reads the reason beside a check's blind spot when
the thing that justified it stops being true, so a check decays into silence while continuing to pass; the
only defence is that **a check reports how many claims it actually read**, because zero is the one number
an exemption, a mis-scope and a stale pattern all produce.

## What happened

`qa_register_shape` exists to assert the ruling range from §3's own rows rather than let it be copied
between four files. It does that, it has done it correctly every day since 10-07, and it has twice failed
the build on a filing run's own edits. **All three of its claims about the document it reads were false
this morning, and the register's prose is what moved under it — every edit that falsified them was itself
correct.**

### Limb 1 — the exemption outlived its reason

The tool's own comment declines to assert the fifth home's **numerator**, and gives a real reason:

> the NUMERATOR of that count is not derivable — the 10-06 reconciliation got 24 of 27 members from this
> register's own labels and recorded the remaining three as a debt rather than inventing them, so asserting
> it would be asserting a number nobody can check.

That was true on 10-07. **It stopped being true on 10-11**, when ruling #95 established that the three were
never missing and the repair wrote the assertion-discipline family an explicit **MEMBERSHIP OF RECORD** — a
list beside the count, which is exactly the artefact whose absence made the numerator undecidable. The
reason expired; the exemption did not. Nobody re-read the comment, because a comment is read by whoever
edits the file and nobody had cause to edit it.

Two stale numerators followed inside six days, both found by hand here:

* **The assertion-discipline family declared three different sizes of itself in one screen.** Its count word
  read **THIRTY-FOUR**, its membership list enumerated **33**, and the list's own dated header read
  **thirty-one**. #103 moved the count on 10-17 and did not append to the list three lines below it — limb 3
  of the 10-04 second amendment (*when a count moves, the membership list moves with it*), failed in the one
  place that had been given a list six days earlier so that limb 3 would have something to attach to.
* **The operating-cost family's count line read *two* against a population of three.** #105 was filed this
  morning; its own series-integrity note says *"the conditional fifth being the operating-cost family's own
  member count, which this ruling takes to three"* — and the count line itself still read two. **The fifth
  home has two addresses**, a narrative paragraph and a count line, and the filing run moved the paragraph
  that claims the move.

### Limb 2 — the scope was a parser, and the structure moved under it

`families_block()` returns the families list by walking forward from a cue and breaking at *"the first
non-bullet prose"*. When it was written the list was nine bullets and nothing else. Sub-paragraphs have
since been written **beneath** the bullets — the three movements of assertion discipline, the membership of
record, the non-numeric family's member notes — and an indented continuation line is non-bullet prose, so
the loop breaks at the first one. **Measured: it returned five of the nine top-level bullets**, and the four
it never reached were the four that carry the membership declarations. A parser that stops at the first
thing it does not recognise does not report a failure; it reports a **prefix** as the whole.

### Limb 3 — the pattern moved, and the check went silent

The limb that *was* asserted reads ratio denominators of the form `"twenty-six of eighty-eight rulings"`.
**The families list contains no such claim any more.** The only match left in scope is the literal
`N of M rulings` in the preamble sentence about the gate ratio, which `words_to_int` correctly refuses — so
the limb ran, read **zero** live claims, and printed clean. The prose had moved to *"standing at
THIRTY-FIVE"* and *"THIRTEEN members, enumerated here in full"*; the check was still looking for the older
form. **A check whose pattern its subject has stopped using is indistinguishable from a check whose subject
is correct** — the 2026-08-16 silent-pass trap, stated in this repository's own words as *a ruling that
finds nothing to check has failed, not passed*, and arriving here inside the instrument built to end the
hand-maintenance of this very register.

## Why it is one ruling and not three

Because the three share a mechanism and a remedy. An exemption, a scope rule and a match pattern are all
**dated assumptions about the subject**, written at the moment of greatest knowledge about it and never
revisited; and all three failed in the same direction — **toward silence**, which is the direction that
reads as health. The remedy is not vigilance. It is that the check **says what it read**: one line of
output, *N declared membership lists, M ratio denominators*, turns all three failures into a visible zero.
This is #52 (*an assertion names the artefact it read*) moved one level inward — from the artefact to the
**claims inside it** — and it is the second time in two days that the operation has found a rule true of one
axis and taken as true of both (#105, *a constant is not a measurement*).

## What was done

1. **`families_block()` now treats an indented line as a continuation**, and returns nine bullets.
2. **The numerator is asserted**, narrowly: a family that *declares* its membership — one of three cues the
   operation writes on purpose — must agree with the list it declared. A family that declares no list is
   **printed as unchecked by name**, never silently passed.
3. **Zero of both forms is a finding.** The fifth home is not permitted to be entirely unread.
4. **The check prints its claim counts on every run**, clean or not.
5. Both stale counts repaired by counting tokens: assertion discipline to **thirty-five** with #103 and
   #106 appended to the list, operating cost to **three** with #94, #96, #105 named in the count line.

## Proof — both ways, bite first (#35)

Run on copies under `/tmp/rsproof`, never on the repository. Every injection was asserted to have **changed
the file** before the check ran on it (2026-09-14, trap 1): a bite that does not alter the artefact reads
exactly like a passing control.

| # | Injection into a copy of `INDEX.md` | exit | What it said |
|---|---|---|---|
| 1 | **control** — the repaired file, unmodified | **0** | `fifth home — 3 declared membership list(s) read, 0 ratio denominator(s) read` |
| 2 | `thirty-five members` → `thirty-four members` | **1** | `declared count says 'thirty-four members' (34) and the list beside it enumerates 35` |
| 3 | `#103` struck from the membership list | **1** | `says 'thirty-five members' (35) … enumerates 34` |
| 4 | `THREE members — #94, #96, #105` → `#94, #96` | **1** | `says 'THREE members' (3) … enumerates 2: #94 #96` |
| 5 | the membership list given a `#999` | **1** | **two** findings: 35 against 36 enumerated, **and** `names #999 and the register ends at #106` |
| 6 | all three cues removed, no ratio present | **1** | `0 declared … 0 ratio` + `the fifth home is entirely unchecked, which is a check with nothing to check rather than a clean one` |
| 7 | `thirty-five` → `thirtyfive` | **1** | `'thirtyfive' is not a number word this check can read` |

**Limb 2 measured rather than injected**, because the defect was the shipped code: the pre-10-18
`families_block` returns **5 of the 9** top-level bullets against the current file, and **0** of the three
membership cues appear inside that prefix — so the limb added today would have read nothing had the scope
not been fixed first. **Limb 3 likewise:** the only `X of Y rulings` string left in the families list is the
preamble's literal `N of M rulings`, which `words_to_int` refuses, so `ratios_seen` is **0** on the control
— printed, not asserted, because zero ratios beside three declarations is the prose having moved on, not a
defect.

## And the check caught the same defect in itself, twice, within one run of being written

Both found by the **claim-count line** and by nothing else, which is the only reason they are in this file
rather than in next week's:

* The dash class was written `[:—–-]` inside a **raw** string, where `—` is not an escape — a
  backslash, a `u` and four digits, and no em dash. The operating-cost declaration is introduced by an em
  dash, so it was not read.
* The cue was required to sit **before** the count. The non-numeric family writes the count first
  (*THIRTEEN members, enumerated here in full: …*), so it was not read either.

Each time the check read **2 of the 3** declarations on disk and exited **0**. A count-of-claims line turned
both into a visible number in the first second; without it, a tool filed this morning as the remedy for
silent decay would have shipped two-thirds awake and passed every day until a hand counted again.

## Kin

* **#105** (2026-10-18) — *a constant is not a measurement*. Yesterday's instance of a sentence that retires
  a question. This one is a *comment* that retires a question, inside a tool, where even fewer people read.
* **#92** — *a predicate that falls back cannot fail*. There the silence came from the API; here from the
  document.
* **#95** — *a shortfall indicts the method before the population*. The method that under-recovered on 10-06
  is the thing this exemption was written to respect. It was right to respect it and wrong to keep doing so.
* **#57** — *count against the population, never against yesterday's number*. Both stale counts agreed with
  the arithmetic that produced them.
* **The enumeration family** — *a green check is scoped to what it enumerates*. Limb 2 is that rule pointed
  at the enumerator's own parser rather than at its subject.

## The forward question this leaves

Every one of our thirty-two instruments carries dated assumptions of this shape, and **the only ones we
have ever re-read are the ones that failed.** Which other check's stated reason for not asserting something
has quietly become false? The population is enumerable — every `# ...not derivable / cannot / is out of
scope` comment in `agents/tools/**` — and nothing has ever read them as a set. Entered on the standing
queue rather than carried in this file.
