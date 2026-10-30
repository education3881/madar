# A collision needs no oracle — where a per-artefact judgment needs one, look between the artefacts

**Ruling #121.** Filed 2026-10-30 from the standing queue's own head — **item 51**, raised 2026-10-28 by
the brief function, **2 days**, the only row in the DEFECT bucket and **the youngest head this board has
ever handed out**. Family: **assertion discipline** (#16, #35, #36, #37, #52, #57, #70, #75, #83, #85,
#88, #89, #90, #92, #93, #95, #103, #106, #108, #109, #113, #114, #115, #118 — the full list of record is
in §2 of the guidebook index), which keeps a running member count — so **five counts moved**, and this is
its **forty-second** member.

**The fifth home was CORRECTED rather than incremented, and the correction is this family's own subject.**
The count word in §2 read **thirty-six** while the membership list three lines below it read **forty**,
reconciled against the population at the 2026-10-25 review. The ordinal narrative never re-read that
reconciliation: #118 was filed on 10-27 as *the thirty-sixth member* — **a slot #108 already held** — so
the series continued from a number the population had left behind two days earlier, and the membership
list was not appended to at all, which is limb 3 of the 10-04 second amendment declined. #118 is the
**forty-first**, #121 is the **forty-second**, both corrected on the face today, and the list moved with
the number. *An ordinal series is a running count, and a reconciliation that moves the population does not
move the series unless somebody re-reads it* — #57 inside the one family that exists to hold #57, which is
the fourth time this register has produced that shape in four weeks.

---

## What the item asked for, and the half it declared editorial

Item 51 was raised by the brief function on the morning #119 was filed. It had found that **ten of the
briefs disagreed with themselves about their own date or their own number** in the `<head>` — the half of
the artefact that reaches a browser tab, a link preview and a search engine, and the half no human has
ever looked at. Those ten were repaired by hand the same day, because a brief's date and number are
derivable from its filename and its own masthead. The row carried forward what was left:

> `2026-10-19`, `2026-10-26` and `2026-10-27` describe, in the text a search engine and a link preview
> read, **a finding from an earlier day** … Not rewritten by the run that found them, because only the
> run that wrote a brief knows what it meant to say — the repair is to read each brief's own Today
> section and write a description from it, which is one morning's work and is **editorial rather than
> mechanical**.

Both halves of that are right about the *repair*. The error is in what it implies about the **check**: it
specified a gate for the derivable half only — *a brief's `<title>` date equals its filename's, and its
description's `Brief NN` equals its masthead's `No. NN`* — and left the stale-summary half to a human,
because deciding whether a sentence describes *this* day requires knowing what the day was.

**It does not.** It requires knowing that **two days cannot share one summary.**

---

## The unit is the collision, and the collision is oracle-free

A description summarises one day's artefact. Ask it per-file — *is this sentence about this brief?* — and
you need an oracle: the brief's own content, read and judged, which is exactly the judgment the row
correctly assigned to a human. Ask it **pairwise** — *do two briefs of different dates carry the same
summary?* — and the oracle disappears. If two dates share one summary then at most one of them is
describing its own day, **and that is a fact about the pair, not an opinion about either.**

The check cannot say *which* of the two is stale. It does not need to: it needs to fail, name the pair,
and hand the answer to the only party that holds it — the run that wrote them. **An assertion that stops
exactly where its evidence stops is not a weak assertion; it is a correctly scoped one.**

This is **#109's distinction moved from an assembly to a corpus of claims.** That ruling drew the line
between the **collision** a build can see (two fragments writing one selector, two pages describing one
`@id`, two feeds sharing a `guid`) and the **consequence** only a render can see (which rule wins, what
it paints). Item 51's subject looked like a consequence — the meaning of a sentence — and it has a
collision underneath it that is every bit as exact as a duplicate `@id`.

**What it cost to not see that: the row named three briefs and the instrument found nine.**

| Collision | Briefs sharing one summary | Stale |
|---|---|---|
| 2026-09-08 → 09-09 | 2 | 09-09 |
| 2026-09-10 → 09-11 | 2 | 09-11 |
| 2026-10-10 → 10-12 | 2 | 10-12 |
| 2026-10-13 → 10-14 | 2 | 10-14 |
| 2026-10-17 → 10-18, 10-19 | 3 | 10-18, 10-19 |
| 2026-10-20 → 10-21 | 2 | 10-21 |
| 2026-10-25 → 10-26, 10-27 | 3 | 10-26, 10-27 |

Nine stale summaries in seven collisions, 8.7% of the 104 briefs that carry one. All nine rewritten
today from each brief's own Today section. The three the row named are among them; **the six it did not
name are the reason the unit matters**, and one of them (`2026-10-17` → `10-18` → `10-19`) shows the
compounding the row itself predicted: the stale text is copied forward from the stale copy, so the
distance from its true day grows by a day at a time.

---

## And the derivable half was not finished either

Limbs 1 and 3 — title date and description date against the filename — found **`2026-06-08`**, whose
`<title>` reads `2026-06-07` and whose description reads *Sunday 07 June 2026*, against its own masthead
reading *Monday · 08 June 2026 · Daily Brief · No. 11*. It is the **eleventh** instance of the class the
10-28 run repaired **ten** of, by hand, two days ago.

Nothing was careless: ten were found and ten were fixed. **A hand pass over a population is a measurement
of the files it opened.** This is 2026-09-13's *a hand-run assertion is a habit, not a gate* applied to a
one-off repair instead of to a recurring check — and the tell was available at the time, because a repair
that cannot state its denominator has not measured one.

---

## Two design notes that are the reason the gate has no exemption list

**(1) The brief's self-identification is a POSITION, not a string.** Three briefs name an earlier brief's
number in their description *on purpose* and are correct — `2026-07-09` (*Brief 28 planned to hold them*),
`2026-08-03` (*yesterday's daily commit (Brief 41 + Australia AR) never landed*), `2026-08-10` (*Brief 48
and the weekly review ride today's block*). A check that grepped for `Brief NN` would carry those three
as permanent exceptions. It does not have to: the brief names itself in exactly one place — `Brief NN.`
immediately after its date clause — and a reference in running prose is never there. **#113's method,
transferred from a name to a description:** a boundary the artefact supplies is exact where a boundary the
check guesses is not.

**(2) Limb 4's one exception is a literal, not a list of fourteen filenames.** Fourteen briefs from
2026-05-28 to 2026-06-11 carry the template's placeholder — the exact string `Yesterday, today,
tomorrow.` — which describes no day and so misdescribes none. Exempting the *string* covers a fifteenth
placeholder written tomorrow and cannot be stretched to cover a fifteenth stale summary; exempting the
*files* would have done the opposite of both. Proved: a control that puts the placeholder on a fifteenth
brief exits 0, and the printed count moves 14 → 15.

---

## What was built, measured, and deliberately NOT asserted

The obvious instrument for the half that is genuinely not derivable is **vocabulary provenance**: the
share of a description's distinctive words that appear nowhere in the brief's own rendered text. It was
built and measured over all 104 briefs that carry a summary, and **it does not separate.**

* median **7%**
* the corpus's **highest** scorer — `2026-09-27` at 75%, sixteen distinctive words, six of them absent —
  is a **correct** description written in honest paraphrase
* two of item 51's three known defects (`10-26`, `10-27` at 30%) rank **below ten correct descriptions**

A floor anywhere on that distribution either reds the build on good prose or passes the defect, which is
**#93's ratio reasoning** arriving at the same answer from the other side. It is printed on every run with
its top rows, so that no later run re-derives it, sees the known defects near the top, and believes it has
found a gate. **The negative result is the finding, and printing it is how it survives.**

Also printed and not asserted: **15 of the 20 weekly reviews carry no `<meta name="description">` at
all.** The founder reads the weekly review; a link to one previews with whatever the client invents.
Writing fifteen descriptions is editorial work and is **standing-queue item 56** — an instrument that
wrote the prose it checks would be reading its answer off its own field (#75, one desk over).

---

## The ruling

**Where a per-artefact question needs an oracle, ask whether the same defect is a COLLISION between
artefacts — because a collision is oracle-free.** Two artefacts that each claim to be the unique
description of a different thing cannot carry the same description; the check that notices needs no
access to what either one meant. It names the pair and stops there, because *which* one is wrong is
knowledge only the author has, and an assertion scoped to exactly its own evidence is correctly scoped
rather than weak.

**Corollary, and it is the half with teeth beyond briefs:** when a row declares half of its subject
*editorial*, that is a claim about the **unit** it chose, not about the subject. Re-ask it one level up
before accepting it. The operation's own surfaces where the same move is available and unmade: two
articles sharing a `dek`, two wave-packet captions sharing a sentence, two verdicts sharing a finding,
two queue rows sharing a specification.

---

## Proof

Standing assertion **40**, `qa_brief_head.py`, wired into `postbuild` in the same commit as this ruling's
repairs. Register moved to **40 tools · 12 build steps · 25 postbuild entries · 37 of 40 gating**, all
three derived by `qa_patch_queue` from their own homes rather than counted by hand.

Proved seven ways on `/tmp` copies, every injection asserted to have changed the file **before** the check
ran on it (#35 and its 09-14 addendum):

| | What | Exit | Limb |
|---|---|---|---|
| control | the repaired tree, 118 briefs and 20 reviews | 0 | — |
| bite 1 | one title date set back a day | 1 | 1 |
| bite 2 | one self-identified brief number off by one | 1 | 2 |
| bite 3 | weekday changed, numeric date left correct | 1 | 3 |
| bite 4 | **the real 10-26 defect restored exactly** | 1 | 4 |
| control | `Brief 28` mentioned in running prose | 0 | 2 silent |
| control | a fifteenth brief carrying the placeholder literal | 0 | 4 silent |

Bite 4 is the published defect rather than an invented one, per the 10-25 lesson that *a bite aimed at a
real published defect is the only one that can tell you where the limb's edge actually is.*
