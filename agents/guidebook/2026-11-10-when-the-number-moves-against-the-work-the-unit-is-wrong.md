# Ruling #138 — When the number moves against the work, the unit is wrong

**Filed** 2026-11-10, from the daily run's content and quality functions jointly, taking the standing
queue's own head — **item 85**, the board's one DEFECT, at 3 days.
**Family** — assertion discipline (*how a check earns trust*), its **fifty-second** member.
**Related** — #57 (equal counts are not an agreement), #70, #116 (an ordering rule can express only the
distinctions its keys can hold), #123 (a probe wider than its subject manufactures the defect), #113 (a
boundary the artefact supplies), #86 clause 2, #134, #112, #35.

---

## The statement

**An instrument's UNIT is a claim, and it is a different claim from the one the instrument is about.
When the two diverge, every number the instrument prints is well-formed, self-consistent, and about
something else. The cheapest detector for the divergence is a direction: if the number moves AGAINST the
work — rises as the defect is repaired, or falls as it spreads — the unit is wrong, and no amount of
arithmetic care will find it, because the arithmetic is not what is broken.**

Four instances were found in one run, in one morning, by taking one queue row. They are not four
findings; they are one shape in four places, and the shape is that the operand being measured is not the
operand in question.

---

## Instance 1 — the cure is a member of the population (the detector's own case)

Standing-queue item 85 read: *32 gender determinations about named humans are served in 14 of the 44
Arabic pieces, and NOT ONE of them has evidence on file.* The count came from
`agents/tools/arabic_side_reach.py`, which finds a closed class of five Arabic honorific pairs.

On the morning of 2026-11-08 the row stood at **32**. Ten tokens were read against their registers and
their provenance written into the annotations, as **#86 clause 2** requires: *where no register carries
it, the determination is written down in the annotation as this edition's own, with its date.*

On the morning of 2026-11-10 the same tool over the same corpus printed **39**.

The seven are not drift and nothing had been composed. **`arabic_side_reach` reads the body PLUS the
frontmatter, and a provenance record of a gender determination IS a gender determination** — written in
Arabic, beside a name, inside the annotation the detector reads. The sentence *«الدكتورة» هنا تحديدٌ
تملكه هذه الطبعةُ وحدها* is, to any parse, an honorific attached to a person.

The run then read the remaining twelve and wrote them up. At the close of the day the tool printed **54**.

| | tokens | determinations with no provenance |
|---|---|---|
| 2026-11-07, row raised | 32 | 19 |
| 2026-11-10, start of run | 39 | 12 |
| 2026-11-10, close of run | **54** | **0** |

**The count rose 69% while the thing it was raised about went to zero.** Reading ten determinations did
not leave 22 to do; it left 29. On that count the row could never have closed — not because the work was
not done, but because **the repair enters the population at roughly 1.2 tokens per determination
repaired.**

This is **#57's family with a mechanism #57 does not name.** #57 says *count against the population,
never against yesterday's number*, and the operation has obeyed it for five weeks. Obeying it here would
not have helped: every count **was** taken against the population, three times, correctly. The population
itself was the wrong set.

> **A register written in the same form as its subject cannot be told from its subject by an instrument
> that reads the form.** The fix is not arithmetic and not diligence. It is either a boundary the
> artefact supplies (#113) — a provenance clause is positionally identifiable, as a brief's self-
> identification was in #121 — or two populations reported separately instead of one sum.

---

## Instance 2 — the channel belongs to a person and was counted by piece

The same row classified its own population by **piece**: *four of the 14 pieces have no second channel of
any kind, the English edition carrying no gendered pronoun or title at all*, and it sent those four
first. That instinct was right and its unit was wrong.

A determination is about a **person**. Measured per person over the twelve remaining:

- **19** distinct gender determinations, not 32 or 39 or 54 tokens;
- **7 of the 12 remaining had no second channel at all** — on pieces the row calls both-channel.

`2026-09-14-africa-best-system-ruler` carries **13 English masculine forms and 5 feminine** and was
classified both-channel on exactly that evidence. The human in it whose gender Arabic commits —
CONFEMEN's secretary-general — **has no English gendered form anywhere in the piece.** A piece-level rate
averages over precisely the case the row exists to find, and it does so most confidently on the
figure-dense pieces, where the denominator is largest.

**And one member of the population was never a member.** `2026-06-10-rak-iqra-arabic-diglossia`'s الشيخ
sits inside **مؤسسة الشيخ سعود بن صقر القاسمي** — the Foundation's own registered name. Bucket A's
stated boundary is *an honorific states that the next token names a person*; an **eponymous institution**
defeats it, and the honest population was 19 of 20 candidates. That is #123 exactly: a probe wider than
its subject manufactures a member of the set it was aimed at.

---

## Instance 3 — a quotation mark cannot carry a negation

Writing the provenance required saying, repeatedly, *this register does not print a gendered form.* Two of
those sentences named the absent form **inside quotation marks**:

- `'Dr. Tarek Shawki'` — while stating that the AUC register titles him **Dean**, never Doctor.
- `'la secrétaire générale'` — the French feminine, offered as the counterfactual the register could not
  have printed about a woman.

`qa_citation_identity` turned the build red on both, verdict **absent**. It was right and the prose was
right. **A quoted identity token asserts *the bytes carry this*; the surrounding prose asserted the
opposite; and the gate reads the operand, never the sentence around it.**

So **an annotation correctly reporting an absence is byte-indistinguishable from one misattributing a
quotation.** This is #101's *the annotation's silence read as agreement* inverted — here **the
annotation's quotation read as assent** — and it is the only instance in the four where the instrument
caught the error, because the quotation mark is a boundary the artefact supplies and the negation is not.
**Binding:** a form a register does **not** print is named without quotation marks, and the reason is
written at the point of change.

---

## Instance 4 — the precondition measured the wrong operand, and manufactured six defects

`lastmod_tree_guard.py` was built 2026-10-15, closing standing-queue item 8, to refuse one specific
unsupportable comparison: *a git-derived `<lastmod>` against a working-tree build.* Exit **4 = REFUSED**,
and it is deliberately neither drift nor unreachable, because *an unsupportable number being read as one
of the other two* was the whole defect it exists to stop.

Its limb asks: **is the working tree clean now?**

This run edited nine served annotations, built `dist`, wrote its logs, committed, pushed, and then ran
`qa_served_manifest --check`. At comparison time the tree was spotless — so the guard allowed it — and
every `<lastmod>` in that `dist` had been resolved against a HEAD **one commit behind** the one the guard
was reading. The tool reported **6 pages as SILENT CONTENT CHANGE**: three pieces, both editions. That is
the single direction `qa_served_manifest` calls its assertion and the one no other instrument of ours can
see, because after a deploy origin equals build by construction.

**All six were false.** Rebuilding from the byte-identical committed tree returned **CLEAN, 0 silent
content changes.**

The question is never *is the tree clean* but **does `dist` contain what the tree now contains**, and the
exact operand for that was already on disk in both callers: **HEAD's committer timestamp against `dist`'s
newest file mtime.** Added today as limb 2, no new artefact and no served byte touched, proved per #35
with one bite red (clean tree, `dist` stamped before the HEAD commit → `REFUSED(4)` with the lag printed)
and three controls (the real post-commit build → silent; the same copy stamped after HEAD → silent; no
`dist` at all → refused for the cannot-establish reason rather than assumed clean).

> **A precondition that measures the wrong operand reads exactly like a precondition that passed** — and
> the report it green-lights is a manufactured defect indistinguishable from a real one. #35 requires the
> bite to be proved as carefully as the control; this points #35 at the guard rather than at the
> assertion, where the failure is silent in both directions at once.

---

## Why these are one ruling and not four

Each is a well-formed measurement of the wrong thing, and in each case **every number was internally
correct**:

| Instrument | Unit it measured | Unit of the claim |
|---|---|---|
| `arabic_side_reach` | honorific tokens, body + annotation | determinations about persons |
| item 85's channel cell | pieces with a gendered English form | **persons** with one |
| `qa_citation_identity` | the quoted string | what the sentence says about the string |
| `lastmod_tree_guard` | is the tree clean now | was `dist` built at this HEAD |

**None of them can be caught by checking the arithmetic, and three of the four cannot be caught by
re-running them.** What exposed the first was a **direction**: the number went up while the defect went
away. That is the contribution here, because it is cheap and nobody has to be clever to apply it.

**Binding, in three clauses.**

1. **A row that carries a count states the count's UNIT**, and the unit is the thing the row is about —
   a determination, a person, a page, a claim — never the token the detector happens to match.
2. **Before trusting an instrument's trend, check the direction against the work.** If the number rises
   as the defect is repaired, or falls as it spreads, stop and re-ask what is being counted. A monotone
   agreement with yesterday is what #57 forbids; **a monotone disagreement with the work is a stronger
   signal and costs one comparison.**
3. **An instrument whose output includes its own repair reports two populations or none.** Where the
   remedy a rule mandates is written in the same form, field and language as the subject the rule
   governs, the instrument either finds a positional boundary (#113) or prints subject and provenance
   separately — a single sum of the two is a number about neither.

**The general form, and it outlives all four instances:** *count the unit before you count the
population.* #57 made the operation check its counts against sets rather than against memory; #116 made
it check that an ordering's keys can hold the distinctions it needs. This is the step before both —
**the set itself is a claim, and the quickest way to test it is to watch which way the number moves when
you do the work.**

---

## What it cost and what it bought

Item 85 **closed** at 3 days: **19 of 19 determinations now carry provenance in both editions**, four
evidenced by their own cited register, eight declared as this edition's own with the settling fetch
named, three of those eight because the register **refused us** outright, and **zero wrong** across all
nineteen — where #86's own sample of ten had found two. The row closed on its population, while its
count moved 32 → 54 in the other direction.

And a distribution worth carrying forward, because it is the first measurement of it this operation has:
**of the twelve determinations read today, only four are evidenced by their own register.** Five were
answered by registers that print no gender **by house style** — UNESCO, Elsevier, Careers360, a bilingual
authority's English face — and three were refused. **For three of the five silent ones the settling
register is the owner's own ARABIC face, and we cited its English one.** #86 clause 2 was written as the
exception path; measured over the full population, **it is the majority path.** A rule whose exception
branch carries two thirds of its instances is misdescribing its own subject, and that is the next thing
this family should be asked.

*(Noted and deliberately NOT filed as a second ruling: that last paragraph is a measurement at n = 19 and
a rule amendment on it would be #116's threshold mistake — a guarantee stated as arithmetic nobody did.
It is recorded here and carried to the weekly review.)*
