# The standing ledger — one row per piece, no edition framing

**Opened 2026-11-08 at the weekly review, by applying GitHub issue #13's stated default (option B) on the
date it fell due.** This is the live ledger. `_EDITION_05_STATUS.md` is a **closed-edition record** and
nothing is planned from it.

> **A decision made by silence is visible as one.** Issue #13 — *what the next piece is an edition of,
> twelve days after Edition 05 closed* — was opened 2026-10-25 with three options and a stated default:
> *if there is no reply by 2026-11-08, the operation applies option B.* It was open **fourteen days**, no
> reply arrived, and the default is applied here. **B was chosen as the default not because it is the best
> option but because it is the only one the operation can execute without a word from the founder** —
> options A and C both need a frame, and only he can set one. *A default the operation cannot execute is
> not a default* (the rule issue #8 settled).
>
> **What B costs, recorded rather than glossed:** no shared throughline, no registry row six, no cover, and
> the Editions page stops growing at five. The founder's recommendation in the issue was *A if you have a
> frame in mind this week; otherwise C* — so the operation is now running the option its own
> recommendation ranked **third**, and it will keep saying so. **Issue #13 stays open**, because applying a
> default settles what happens next week and not what the publication is. A frame arriving on any later day
> supersedes this file for pieces after it; pieces already shipped as singles stay shipped (#41 —
> supersede, don't resurrect).

## How a piece ships here

Each piece ships **the day its own gate closes** — no wave, no all-or-nothing flip, and the 71-day
invisibility of Edition 05 cannot recur. The gate is unchanged; what changes is that it is read per piece
rather than per wave. Eight cells, and a piece ships when all eight are filled:

1. Editor's brief · 2. EN draft · 3. Editor five-test verdict · 4. AR composition ·
5. Arabic Editor's gate · 6. Verifier verdict · 7. Hero still + og card · 8. `approved: true` in both
editions, in one commit with its assets (the 2026-06-14 rule)

**THE RAIL STEP, ADDED 2026-11-12 BY THE GROWTH FUNCTION — cell 1 names the forward edges and cell 8
writes them.** Standing-queue item 72 measured the defect and then said in writing that the useful half
is the half that stops it regenerating: *a rail is curated when a piece is written, and at that moment
only the older pieces exist, so every follow-up can point back and none can point forward, and nothing
ever goes back.* 149 edges, 22 still backward after the 11-07 Editor pass. The fix is two lines in this
gate rather than another sweep:

- **Cell 1 (the Editor's brief) names the pieces this one follows up** — by slug, under *Cross-link* —
  and states that the **forward** edge into each of them is owed.
- **Cell 8 adds those forward edges to the older pieces' `related:` in the SAME commit as the flip**,
  both editions, capped at the proven maximum of 6 rails per piece. A flip that adds a backward rail and
  no forward one is incomplete in the same way a piece without its hero still is incomplete
  (the 2026-06-14 rule, applied to the graph instead of to the assets).

*Why here and not in a template file: there is no commission template any more. Editions closed, the
eight cells in this file ARE the template, and a step written anywhere else is a step nobody is told to
read (`CLAUDE.md`'s own rule about a binding queue nobody is told to read).* The first instance is on
disk the same day: `2026-11-12-england-ofsted-exempt-cohort-brief.md` names both Bahrain pieces and the
forward edges owed to them. **This closes item 72's regeneration half only** — the 22 declined backward
edges stay open, their judgment expiring when a later piece turns one of those comparisons into a real
follow-up.

**The Verifier's verdict is scheduled the run after the pair verdict** (2026-09-06) and **drafter ≠
verifier is structural** — neither is relaxed by the absence of a wave. The ceiling stays **one fresh piece
per day at most**, and the standing rule holds: **quality over slot, hold rather than ship thin.**

## In flight

**ONE ROW IN FLIGHT. CELL 1 OF EIGHT FILLED TODAY, AND SEVEN CELLS ARE OPEN.**

| Piece | Brief | EN draft | Editor verdict | AR | AR gate | Verifier | Still + og | Flag | Open cells |
|---|---|---|---|---|---|---|---|---|---|
| **Twenty-three schools moved in a year, on a ruler that runs every two** (title PROVISIONAL) · slug `2026-11-22-abu-dhabi-irtiqaa-biennial-yield` | **FILLED 2026-11-22** — `content-drafts/briefs/2026-11-22-abu-dhabi-irtiqaa-biennial-yield-brief.md`, off `content-drafts/recon/2026-11-22-abu-dhabi-irtiqaa-candidate-recon.md` | — **and it does not open until owed read 1 lands**, because the UAE Unified School Inspection Framework can move the subject | — | — | — | — | — | — | **SEVEN** |

**Reconciled against disk 2026-11-22. CELL 1 FILLS ON A NEW SINGLE, AND THE FIRST CANDIDATE'S PARK REASON
EXPIRED WHILE THE PARK ITSELF HELD.**

- **The pool had one banked entry and it is parked again for a different reason.** KHDA Dubai went back
  into the pool on 2026-11-11 under ruling #139, its TLS objection withdrawn on the merits. Measured today:
  the host has **rotated its certificate** to a GlobalSign Atlas R46 DV TLS CA 2026 Q4 chain that sends the
  intermediate and verifies `OK` — so the condition #139 was filed about **expired on its own, eleven days
  later**. And the register is still unreadable: `web.khda.gov.ae` now answers every client we own with
  **HTTP 200 and a 954-byte Imperva/Incapsula block page**, and `WebFetch` returns no text at all. *A
  park's reason has a shelf life and the park does not inherit it — a park is re-measured when it is
  reached, never read.* Queue row raised, because `qa_sources_alive` scores a WAF block as ALIVE: it is a
  **200**.
- **The commission is ADEK, Abu Dhabi**, and the spine is a unit this corpus has not used. Both Bahrain
  pieces and the England single asked how much of a published distribution's movement belongs to the
  schools and how much to the instrument; England answered it in the **scale's** unit. This register asks it
  in the **cadence's**: *23 private schools advanced from Acceptable to Good in one academic year* against
  *Irtiqa'a inspections are conducted biennially*, forty lines apart on one page, reconciled nowhere.
- **Both language faces were read in served text, and they disagree about a CATEGORY.** The English
  separates a six-point **scale** of grades from six core **standards** of what is graded; the Arabic calls
  both **معايير**, and both sets number six. The figures agree exactly — 13 / 51 / 93 / 42 / 5 — which is what
  makes the wording legible as a finding rather than an error. Standing-queue item 81 live, as editorial
  material.
- **Four reads are owed before the draft and they are named in the brief**, not left to the drafter (#101,
  #151): the national framework (gates cell 2), a prior-year distribution, ADEK's own private-school count
  to settle whether 204 is the population, and whether per-school ratings are published.
- **No percentages are authorised** until owed read 3 lands, because a share of a subset read as a share of
  a sector is #111's defect.

**THE PIECE BELOW SHIPPED ON 2026-11-21 AND WAS NOT SERVED TO A READER UNTIL 2026-11-22.** The 11-21 run
banked all five function commits to `origin` and then died at `error_max_turns` (181 turns, 43 of 90
minutes), and `madar-daily.yml`'s publish step carries `if: success()` — so no deploy was dispatched, and
the live origin served the 11-20 build with both editions of this piece 404ing for a day while brief 137
told the founder it had shipped. **Shipped and served are different events and this ledger records the
first one** (CLAUDE.md's standing derivation: the commit that introduced `approved: true`). The strand was
observed rather than assumed — `qa_prior_publication --observe`, 5 commits — and the day's publication
rides on **this** run's push. Standing-queue item 77, third daily instance.

**The 2026-11-21 note below stands unaltered.**

**NOTHING WAS IN FLIGHT AT THE 2026-11-21 CLOSE. The row that stood here shipped that day.**

| Piece | Shipped | Cells |
|---|---|---|
| **The cohort that was frozen by rule** · slug `2026-11-12-england-ofsted-exempt-cohort` | **2026-11-21** | **EIGHT OF EIGHT** |

**Reconciled against disk 2026-11-21. CELL 8 FILLS AND THE PIECE SHIPS — the first single ever shipped
against this ledger, and the first piece to ship in twelve days.** Publish gate in writing at
`agents/logs/2026-11-21-publish-gate.md`.

- **Both editions are `approved: true`** at `web/src/content/articles/2026-11-12-england-ofsted-exempt-cohort.md`
  and `web/src/content/articles-ar/2026-11-12-england-ofsted-exempt-cohort.md`, with the hero still and the
  og card copied from `design-assets/` into `web/public/` **in the same commit as the text** (2026-06-14).
  Corpus **45 EN / 45 AR → 46 / 46**, parity 100%.
- **All six conditions discharged by name** — (A) the eleven grade renderings declared in the SERVED Arabic
  annotation as this edition's own, dated 2026-11-17, naming the two strings a *different* regulator
  publishes in Arabic on the Bahrain piece; (B) sources 3 and 4 marked SINGLE-CHANNEL in both editions;
  (C) §A1 rewritten; (D) §A4's first two strikes withdrawn and the third kept; (E) source 5's annotation
  repaired, the one of the four that reaches a reader (#114); (F) the cap line corrected to `dek: 198/200`.
- **THE RAIL STEP'S FIRST INSTANCE AT CELL 8, AND IT HIT THE CAP.** Two forward edges went in at 3 → 4
  rails. The third, into `2026-07-28-england-report-cards-first-term`, had **no slot: that page already
  carried 6, the proven maximum.** `2026-08-28-sierra-leone-sleic-outcomes` was displaced for it, in both
  editions, because it is the only one of that page's six rails about *pupil examination outcomes* rather
  than about an instrument that grades schools — and the new piece is the same country, the same regulator
  and the direct counterpart. **The rail step as written does not say what happens at the cap**, and now
  there is a worked instance: *displace with the reason written down, never silently decline.* Queue item
  raised today.
- **EVERY QUOTED SPAN IN BOTH EDITIONS WAS READ AGAINST ITS REGISTER'S OWN BYTES BEFORE THE FLIP, AND SIX
  DEFECTS CAME BACK — FIVE OF THEM WRITTEN THIS MORNING.** 65 of 65 EN body spans and 34 of 34 Latin
  annotation tokens are now byte-identical. Four of the six were apostrophes and nested quotes: the
  registers serve U+2019 and U+2018/U+2019 where our fresh annotations carried U+0027 and straight doubles
  — **ruling #150's fourth firing and its first inside a served annotation.** One was our own markdown
  `**her**` sitting *inside* a quotation, which makes a quotation of nobody's bytes. One was a title whose
  own page lower-cases *state-funded* where its predecessor capitalises it. *The compose-time discipline
  arrived at the gate, which is the margin 2026-07-27 says is the wrong one — and it arrived because the
  two citation gates had no row for a new piece and correctly failed the build rather than narrowing.*


| Piece | Brief | EN draft | Editor verdict | AR | AR gate | Verifier | Still + og | Flag | Open cells |
|---|---|---|---|---|---|---|---|---|---|
| **The cohort that was frozen by rule** (title CONFIRMED 2026-11-15) · slug `2026-11-12-england-ofsted-exempt-cohort` | **2026-11-12** | **2026-11-14**, rev 1 and rev 2 **2026-11-16**, **rev 3 2026-11-18** (the #117 repair the Arabic gate sent back) | **FILLED 2026-11-16 — APPROVE on all five tests**; line 6 **corrected 2026-11-18** from `editorial futures: 0` to `1` | **FILLED 2026-11-17** — `content-drafts/drafts/2026-11-17-england-ofsted-exempt-cohort-ar.md`, three registers re-opened by the Arabic desk | **FILLED 2026-11-18 — APPROVE.** `content-drafts/verdicts/2026-11-18-england-ofsted-exempt-cohort-arabic-gate.md`. Eleven grade renderings judged as a set and approved as words, with **condition A** on cell 8; transliteration and the gender chain verified 1 of 1; the EN editorial future repaired in both editions today | **FILLED 2026-11-19 — PASS WITH FOUR ITEMS.** `content-drafts/verdicts/2026-11-19-england-ofsted-exempt-cohort-verification.md`. The body traces clean; four of the five registers were re-opened independently today and every load-bearing figure and quoted sentence is present verbatim, register 4 declared as not re-fetched. The four items are in the APPARATUS and are bound to cell 8 | **FILLED 2026-11-20.** `design-assets/stills/2026-11-12-england-ofsted-exempt-cohort.svg` (1200×600, paper-cream, two palette tokens, no fills, no text) and `design-assets/og/2026-11-12-england-ofsted-exempt-cohort.png` (1200×600, 7,800 b, rasterised from the still). Brief and delivery record: `content-drafts/briefs/2026-11-20-england-ofsted-exempt-cohort-hero-brief.md`. **Both STAGED at `design-assets/` and NOT in `web/public/`** — see the note below; cell 8 copies them across in the flip commit (2026-06-14) | — | **ONE — cell 8 only**, and cell 8 now carries **six conditions — two from the Arabic gate and four from the Verifier** — (A) the eleven renderings declared in the served Arabic `sources[]` as this edition's own, dated, because the hand-off is not served and the annotation is (#86 clause 2 / #114), naming the two strings a DIFFERENT regulator publishes in Arabic on `2026-10-23-bahrain-bqa-five-cycles`; (B) sources 3 and 4 marked SINGLE-CHANNEL; and from the Verifier (C) §A1 rewritten, (D) §A4's first two strikes withdrawn, (E) **source 5's annotation repaired, which is the one of the four that is SERVED (#114)**, (F) hand-off line 1 corrected to `dek: 198/200` — plus the rail step's forward edges into `2026-07-28-england-report-cards-first-term` and both Bahrain pieces |

**Reconciled against disk 2026-11-20. CELL 7 FILLS, AND THE ASSETS ARE DELIBERATELY NOT IN `web/public/`
BECAUSE A PIECE MID-GATE IS NEITHER HELD NOR APPROVED.** Hero brief and delivery record at
`content-drafts/briefs/2026-11-20-england-ofsted-exempt-cohort-hero-brief.md`.

- **The still is the regulator's own measuring edge, drawn once, in three spans** — graduated, then a
  continuous line carrying **no graduations at all** for the eight years the best-graded schools were not
  routinely inspected, then graduations resumed at twice the pitch, then a cap. A **second** edge sits
  apart, turned out of true, its six graduations hanging below its line with two further strokes set away
  from the six, and **nothing joins the two edges**. One kiln-orange mark has come away from the first
  edge where measurement resumed. **Nothing in it encodes a proportion**, which is the commission's first
  guardrail applied to a drawing: there is no composite of the two rulers and the still may not build one.
- **Looked at and rejected once before being accepted** (2026-08-18 clause 4). The first render put the
  composition in the lower-left quadrant and dropped the orange mark onto the bracket's own upright, where
  it read as part of the bracket rather than as a graduation come adrift.
- **AND THE PLACEMENT QUESTION WAS MEASURED, NOT ASSUMED.** `heldAssets.mjs` withholds a piece's assets
  from `dist` by reading **held slugs out of the content collection**, and this piece has no file in
  `web/src/content/` at all — at cell 7 of eight it is not held, it is **absent**. A card placed in
  `web/public/og/` today would be copied into `dist` whole and served at a guessable URL while its article
  page 404s: **the exact 2026-09-09 defect `heldAssets` exists to close**, with the still's own `<title>`
  serving the unshipped piece's subject in readable text. Proved on a scratch `dist` this morning —
  `qa_held_assets` **exited 0 and printed CLEAN** with the orphan card sitting in it, because limb 1
  enumerates **held** slugs and limb 3 enumerates **approved** ones and *a piece mid-gate is in neither
  set*. Queue item **140**. So the assets are staged at `design-assets/` and cell 8 copies them across in
  the flip commit, which is the 2026-06-14 rule executed rather than quoted.
- **No flag moved and the corpus is unchanged at 45 EN / 45 AR.** **One cell remains**: cell 8, carrying
  **six conditions** (A–F) and the rail step's forward edges.

**The 2026-11-19 note below stands unaltered.**

**Reconciled against disk 2026-11-19. CELL 6 FILLS ON A PASS WITH FOUR ITEMS, AND THREE OF THE FOUR ARE
ONE DEFECT: A FAILED RETRIEVAL RECORDED AS THE REGISTER'S SILENCE.** Verdict at
`content-drafts/verdicts/2026-11-19-england-ofsted-exempt-cohort-verification.md`.

- **The body traces clean, and that is the headline.** Four of the five first-party registers were
  re-opened today **independently of the drafter**, read as served text rather than through a summariser,
  and **every load-bearing figure and every quoted sentence is present verbatim** — the 367 / 263 / 104
  Figure 3 row, the two seventeens in their opposite directions, 3,900 and 3,400, the thirteen-year
  average, 21,957 / 3,262 / 3,188, the 99% safeguarding sentence and the 15% disqualification.
  **Register 4 was NOT re-fetched and the verdict says so**, because a verification that does not name
  what it skipped is a verification whose coverage is assumed — which is this morning's item 41 arriving
  at the editorial desk on the day it closed at the instrument desk.
- **THREE OF §A's FOUR COMPOSE-TIME CORRECTIONS ARE WRONG, ALL IN ONE DIRECTION.** §A1 states that the
  statistical release *"does not contain"* the sentence *"Only 17% of previously exempt schools that had a
  graded inspection this year remained outstanding."* **It is in that release's own Key findings, verbatim**
  — and with it falls §A1's second limb, the claimed *denominator error*: the register **names** the
  graded-inspection denominator in the same sentence, which is the denominator the body correctly uses.
  §A4 strikes two further sentences as unconfirmed and **both are in their registers**, one of them the
  sentence immediately following a sentence the body quotes.
- **The class, and it is #101 moved one step earlier.** A drafter's failure to find is indistinguishable,
  in the written record, from the register's failure to print — all three were written as facts about
  Ofsted and all three are facts about a search. **A positive claim about a register can be re-checked by
  anybody who opens it; a negative claim can be re-checked only by somebody who already suspects it**,
  the test for *this is not here* being the same unsuccessful search that produced the claim. Nothing we
  own has a limb for a string we said was ABSENT.
- **The fourth correction is RIGHT, which is what makes the other three legible.** The Department's
  2 September 2024 page states nothing about retrospectivity — `retrospectiv` verified absent in its
  served text today. One correct strike beside three incorrect ones, written in the same hour by the same
  method. #41 working exactly as written.
- **ONE OF THE FOUR ITEMS REACHES A READER.** Source 5's annotation is **served** while a hand-off is not
  (#114), and it currently reads *"Not carried, because it was not read"* about wording the register does
  carry — true about our reading, misleading about Ofsted. Condition E on cell 8.
- **The cap line is wrong by a transposed digit inside the rule that exists to stop exactly this.**
  Hand-off line 1 reads `dek: 188/200`; the dek is **198**. Both are under the cap so nothing could have
  shipped wrong — what is damaged is the ruler, because the 2026-07-27 amendment made the recorded count a
  returned-unread condition so the cap would be measured at the desk and not at the backstop. Raised as
  queue item **133**: the count is derivable from the draft and the hand-off line asserts it, so it is
  gateable and is currently gated by goodwill.
- **The named human is verified and her provenance is NECESSARY, not belt-and-braces.** Register 2 carries
  *"Ofsted's Chief Inspector, Amanda Spielman, said:"* and, read whole today, **no third-person pronoun and
  no gendered title for her anywhere on it** — so the feminine genuinely cannot be read there, and
  register 5's standfirst is the only channel. The Arabic gate reached this independently on 11-18.
- **And the verifier nearly filed a fabricated finding against that very sentence.** The first pass
  reported the attribution ABSENT because the page sets its apostrophe as **U+2019** and the needle
  carried U+0027. A matcher wrong about a character class manufactured an absence — ruling **#150** and
  item 129's forward question, met in the wild one day old, at the editorial desk. It is the same trap as
  items 1–3, committed by the verifier against the drafter instead of by the drafter against the register,
  **which is why those three are filed as a class and not as carelessness.**
- **No flag moved and the corpus is unchanged at 45 EN / 45 AR.** Cell 7, the hero still and og card, is
  the next content function's first action.

**The 2026-11-18 note below is superseded in its CELL-6-OPEN reading and kept for the record.**

**Reconciled against disk 2026-11-18. CELL 5 FILLS ON AN APPROVE, AND THE GATE'S OWN FINDING IS THAT A
COMPOSED GRADE NAME READS EXACTLY LIKE A QUOTED ONE.** Verdict at
`content-drafts/verdicts/2026-11-18-england-ofsted-exempt-cohort-arabic-gate.md`.

- **Transliteration and the gender chain: VERIFIED, 1 of 1.** أماندا سبيلمان, feminine, read off Ofsted's
  own speech-page standfirst (*"reflects on **her** first speech"*) and **not** off her own texts' *"His
  Majesty's Chief Inspector"*, where the *His* is the monarch's. The 2026-10-04 error in its original
  shape, met and declined by the composer before the gate could reach it.
- **The eleven renderings are APPROVED AS WORDS, and the gate's addition came from reading them against the
  CORPUS rather than against the piece.** Two of the eleven — **غير ملائم** and **جيد** — are already in
  our served Arabic text on `2026-10-23-bahrain-bqa-five-cycles`, where they are **the BQA's own published
  Arabic grade names**, read out of the Bahraini portal's own Arabic CSV. So one string now stands in this
  corpus with two opposite evidential statuses: a **quotation** on one piece and a **composition** on the
  other, indistinguishable in the served text, and only one of them challengeable against a register.
  **That is #101 one level down — a composed grade name is a quotation with its evidence removed**, and
  worse than an acronym because it reads like a quotation.
- **The words were NOT changed, on an evidential reason rather than an aesthetic one.** `غير ملائم` is the
  only Arabic bottom-grade name this publication has ever served and it arrived from a regulator; coining
  a second one to dodge the collision would make this edition less consistent with its own corpus in order
  to look more careful. The two scales differ where it would matter (*مرضٍ* and *يحتاج إلى تحسين* are each
  unique to one instrument) and the two colliding labels sit at the same rank on both — recorded as a
  convenience, not as a justification.
- **CONDITION A ON CELL 8, and it is the one a hand-off cannot discharge.** #86 clause 2 requires an
  undeclinable determination to be written into the **annotation**, with its date. The eleven are declared
  in the composition's hand-off, and **the hand-off is not served while the annotation is** (#114). Cell 8
  does not close until the Arabic `sources[]` carries the eleven as this edition's own, dated 2026-11-17,
  naming Ofsted's non-publication in Arabic as the reason, and naming the two Bahrain collisions.
- **THE EDITORIAL FUTURE IS REPAIRED IN BOTH EDITIONS TODAY, AND THE ENGLISH IS THE ONE THAT WAS WRONG.**
  The EN body read *"the only one that will ever exist on that scale"* — a claim about all future time,
  ours and no register's — while its hand-off line 6 reported `editorial futures: 0`. It had passed the
  Editor's five tests and three earlier reads. Both editions now attribute the comparability claim to the
  guidance that makes it, *published 1 December 2025, last updated 2 November 2026*, and say the
  re-measurement **has no counterpart** on that scale. Line 6 corrected to `1`. **Ruling #149's first
  independent confirmation on a second artefact:** a matcher reporting zero Arabic futures reports its own
  blindness, and a *composer* cannot set the verb without deciding whether the prefix attaches.
- **Two registers are SINGLE-CHANNEL and cell 8 must say so** (condition B): sources 3 and 4 were not
  re-opened by the Arabic desk and carry the English compose-time read of 11-14. Stated by the composer
  rather than discovered by the gate.
- **The three questions the composing desk said it does not own are all answered**, including *do not name
  the minister*: naming a human in Arabic forces a gender determination and no first-party pronoun for her
  was read, so *بقرار الوزيرة* stands (#86 clause 1 forbids reading it off the name).
- **No flag moved and the corpus is unchanged at 45 EN / 45 AR.** Cell 6, the Verifier's verdict, is the
  next content function's first action, scheduled the run after the pair verdict (2026-09-06).

**The 2026-11-16 note below is superseded in its CELL-4-OPEN reading and kept for the record.**

**WEEKLY RECONCILIATION — 2026-11-15, by the weekly review, against disk rather than against this file's
own account of itself.** Every number below was counted; none was carried.

| Reconciled | Found on disk |
|---|---|
| Served corpus | **45 EN and 45 AR**, 100% parity, **zero** `approved: false` in either edition |
| Assets | a hero still and an og card for **every** served slug; the three extras are VALENCE's pair and the brand card, which are chrome and not pieces |
| Registry | **five** editions, all `status: 'closed'`; the sixth `'current'` a grep finds is the TypeScript union on line 25, not a row. `hasOpenEdition` derived and **false** |
| The one piece that shipped this fortnight | `bahrain-bqa-five-cycles`, **2026-11-09**, with all eight cells on disk: Editor verdict 11-02, Verifier verdict 11-03, three dispositions, a verification retrace 11-07, Arabic gate 11-09 |
| In flight | **one row**, `2026-11-12-england-ofsted-exempt-cohort`, **three cells open** as of 2026-11-18 — cells 1 to 5 filled; the AR composition landed 11-17 and the Arabic Editor's gate APPROVED 11-18 |
| Edition 05's closed record | owes **one** item, unchanged: the SLEIC *Final Learning Report 2026* citation upgrade, walled by rendering and not dead (#70). Nothing published is wrong while it waits |

**THE FIRST SINGLE SHIPPED AND THE LEDGER WORKED, WHICH IS THE FORTNIGHT'S ONE EDITORIAL FACT.** Issue
#13's default was applied on 2026-11-08 and a piece reached readers on **2026-11-09** — the first in
**forty-three days**, and the first ever to ship against a per-piece gate rather than a wave. Edition 05's
71 held days did not recur, and the thing that replaced them was a nine-day gate on one piece. Said
plainly: **B is still the option this operation's own recommendation ranked third, and it shipped.**

**And `CLAUDE.md` described this ledger wrongly for six of those days — ruling #144, filed in this review's
consolidation.** Its item 4 read *one row is in flight (`bahrain-bqa-five-cycles`, three cells open) and
nothing has shipped since 2026-09-27* from 11-09 to 11-15, under a standing rule whose predicate is this
file's **name**. The name was right the whole time. Corrected, and the rule widened from its noun to its
sentence; the full working is in the ruling. **The lesson for this file specifically: a ledger is read
through whatever points at it, and the pointer was stale while the ledger was true.**

### The served-tense mandate, executed on #117's scope — and the scope has a gap this fortnight exposed

The window is *every editorial future in the SERVED corpus whose date has arrived since the last review.*
The 11-08 review executed 11-02 → 11-08 and found one in-window date string, shielded. This review
executed **11-09 → 11-15** over both editions:

* **33 in-window date strings across both editions, and every one is a READ DATE** — *read 2026-11-10*,
  *re-read 2026-11-09*, *this register refused the re-read on 2026-11-10* — past-tense records of our own
  reading, which is the opposite of an editorial future. **Zero unshielded futures.**
* **31 future-verb sentences on dates that arrived earlier**, swept again across all 45 EN pieces, and all
  31 are shielded in the three ways #117 enumerated: inside a quotation, inside a `sources[]` annotation,
  or attributed to a dated register (*the emirate's May 2026 announcement put Iqra into…*, *Ofsted's own
  12 June 2026 update put the change from September 2026*).
* The Arabic half is **printed and not asserted** per #117 clause 4: **591** bound-prefix candidates
  (`سـ` homographic with ordinary nouns) across the 45 Arabic pieces. A string match cannot separate
  them, and a check reporting zero for Arabic reports its own blindness.

**THE GAP, NAMED AND MEASURED AT ZERO.** #117's clause selects on **when a date arrived**. The exposure is
created by **when a page started being served**. `bahrain-bqa-five-cycles` entered the served corpus on
**2026-11-09** carrying its entire future-date population at once — dates that arrived in October, before
any review's window, on a page no reader could load until the ninth. **No review has ever read them under
this clause, and none ever will, because the arrival filter can only see the sliver that arrives inside a
window.** Measured this morning: the piece carries **four** future-verb sentences in its body, all
rhetorical (*this piece will not write it as one*), **zero** dated editorial futures — so the exposure is
real in principle and **zero in fact today**. That makes it a coverage question and not a DEFECT under
#116's boundary, and it is raised as a standing-queue row rather than patched here. *It is #143 and #144's
shape a third time in one morning: the enforcement's selector is a date and the fact's unit is a
publication event.*

**Reconciled against disk 2026-11-16. CELL 3 FILLS, AND ALL FIVE TESTS HAVE NOW BEEN READ.** Revision
verdict at `content-drafts/verdicts/2026-11-16-england-ofsted-exempt-cohort-tests-3-4-5.md`.

- **Test 3 PASSES and the remedy was a MOVE, executed as one.** The why-now is paragraph three — the
  2 September 2024 / 10 November 2025 / 10 November 2026 sequence landing on the regulator's own
  sentence to parents, *"the new grades can't be compared to the old ones"* — built entirely from
  sentences already in the draft. Nothing re-reported, no register re-read. **And it carries no relative
  date**, which is #117 honoured at compose time in the one place in a piece where the pull toward *six
  days ago* is strongest.
- **Test 4 PASSES on a structural reason rather than on the absence of a slip. No school is named
  anywhere in 3,700 words** — the cohort is 367 schools and not one is put on the record as having lost
  a grade, which is this subject's whole dignity exposure. The only named human is Amanda Spielman, in
  office. What earns it is *What the frozen cohort does and does not prove*, which states **before** the
  conclusion that the cohort holds the grade constant and **not the school**.
- **Test 5 PASSES with ONE REQUIRED AMENDMENT, and the amendment is the day's editorial finding.** The
  brief's rail named two Bahrain pieces and **missed `2026-07-28-england-report-cards-first-term`** —
  *The verdict, taken apart* — **the same regulator and the same replacement instrument**, covering
  England's first term with no overall grade. That is the second half of this piece's own why-now, and
  we published it in July. A rail step that enumerates the pieces a commission follows up **is an
  enumeration, and it was missing a member** (#57 / #70). The rail gains a third edge in the brief; the
  one owed sentence was written into the body the same run as **revision 2**.
- **No instrument of ours could have found it.** `qa_body_links` resolves the rails a piece *declares*
  and can no more see a rail never declared than the 2026-08-17 orphan sweep could see a page nothing
  pointed at. **A missing cross-link is the orphan defect at the level of the ARGUMENT rather than of
  the site graph**, and the only reader who can find one is a reader who knows the whole corpus. The
  RAIL STEP added on 2026-11-12 closed item 72's *regeneration* half; this is the half it does not
  reach — **the step makes a commission name its predecessors and cannot check that it named them
  all.**
- **Both 11-15 artefact defects discharged:** the dek is written out at **198/200** code points, counted
  by counting rather than by reading the claim, and source 6's URL is pasted from the verdict rather
  than re-found. Both optional items executed too — §A2 sharpened with the Figure 3 row (**367 · 17%
  outstanding · 62% good · 17% requires improvement · 4% inadequate**, one row, four columns apart, so
  the body's refusal to print a bare *17%* is **necessity and not caution**), and the correction's
  closing sentence now names the date of the clause it corrects.
- **No flag moved and the corpus is unchanged at 45 EN / 45 AR.** Cell 4 is the next content function's
  first action, and the Verifier's verdict is scheduled the run after the pair verdict (2026-09-06).

**The 2026-11-15 note below is superseded in its CELL-3-OPEN reading and kept for the record.**

**Reconciled against disk 2026-11-15. CELL 3 IS JUDGED AND IT IS A RETURN, SO THE CELL DOES NOT FILL —
AND TEST 1 WAS RE-VERIFIED RATHER THAN ACCEPTED.** Verdict at
`content-drafts/verdicts/2026-11-15-england-ofsted-exempt-cohort.md`.

- **Test 1 PASS, re-verified against the bytes the registers are serving today.** All eight citations
  fetched: six first-party registers at **200**, both Madār predecessors at **200**, and **35 of 35
  quoted tokens present verbatim** — #112's method applied *before* publication instead of after it.
  Every unquoted figure checked in its register's own table: Figure 3's **263 / 104 / 367**, Figure 1's
  **21,725 / 18 / 70 / 9 / 3**, register 5's six evaluation areas and five grade names, register 4's two
  dates. **§A4's strike is confirmed in the strongest form available: the word *retrospective* occurs
  nowhere in either register that could have carried it.**
- **And Figure 3 is sharper than §A2 knew.** The two seventeens are not fourteen weeks apart in two
  registers; the statistical release's own row for all previously exempt schools reads **367 · 17
  outstanding · 62 good · 17 requires improvement · 4 inadequate** — **one table, one row, four columns
  apart.** The draft's refusal to print a bare *17%* is necessity, not caution.
- **Two Test 1 defects of ARTEFACT, neither an error of fact.** Source 6 carries **no URL** — it is the
  only register cited for a property of the *page* rather than for a claim in the body, so the drafter's
  habit of writing the address beside the claim had no claim to attach it to, and the slug is not
  reconstructible from the title. Supplied by the Editor, fetched, 200. And the **dek is not in the
  draft at all**: the hand-off reports `dek: 188/200` for a string that appears nowhere, which is a
  measurement with no artefact under it. Required on the revision; the Editor does not write it.
- **Test 2 PASS.** **Test 3 FAILS and the draft is RETURNED.** The reader does not know by paragraph two
  why this is in front of them in November 2026. The answer is in the piece and it is a long way down —
  the instrument has been withdrawn and replaced, so the 2022 re-measurement is the only one that will
  ever exist, and the first release under the replacement landed **10 November 2026, five days ago**.
  The remedy is a move, not a rewrite; nothing is re-reported.
- **Tests 4 and 5 were NOT JUDGED**, because the protocol says a verdict does not progress past a failed
  test. Said plainly rather than quietly skipped: *a list of five ticks with two unexamined reads exactly
  like a full read.*
- **The drafter's three open calls are decided** so the revision is one pass: the title is **kept** (a
  *thirteen years* title would drop the word *average*, and a title cannot carry a qualifier); the struck
  retrospectivity claim **stays out of the body** and remains published in the annotation, which is
  served (#114); and the Bahrain correction **stays last**, with its closing sentence to name the date of
  the clause it corrects.

**The 2026-11-14 note below is superseded in its CELL-3-OPEN reading and kept for the record.**

**Reconciled against disk 2026-11-14. CELL 2 IS FILLED, AND COMPOSING FROM THE OPEN REGISTERS CORRECTED
THE BRIEF FOUR TIMES.** The EN draft is at `content-drafts/drafts/2026-11-14-england-ofsted-exempt-cohort.md`,
3,678 words of envelope, with all five registers re-opened and read in served text at compose time per
the 2026-09-13 rule. **Four corrections, and the second is the piece's spine:**

- **The brief's headline quotation is not in the register it is attributed to.** The brief prints *"Only
  17% of previously exempt schools that had a graded inspection this year remained outstanding"*; the
  statistical release prints *"In 2021/22, we inspected nearly 500 schools that were previously exempt"*
  and *"Of these, 17% retained their outstanding grade, while 21% were judged requires improvement or
  inadequate."* The brief's summary carries a **denominator error**: nearly 500 were inspected, **367**
  had graded inspections (Figure 3: 263 primary, 104 secondary), and the percentages sit on the 367.
- **THE 17% COLLISION IS INSIDE 2022, not between 2022 and 2026.** Guardrail 2 warned about two 17%s four
  years apart. There is a **third**, and the first two are **fourteen weeks apart in one cohort from one
  regulator**: the statistical release's 17% is the share **retaining outstanding**; the 22 November 2022
  news release's is the share **rated requires improvement** (*"around a fifth were rated requires
  improvement (17%) or inadequate (4%)"*). Near-opposites, both correctly cited, and **no numeric check
  this operation owns could tell them apart.** The body therefore prints no bare *17%* anywhere.
- **The two registers' arithmetic does not close and the piece does not close it.** The news release says
  *"over 80% (308) … did not retain the outstanding grade"*; 17% of 367 is about 62, and 308 + 62 is 370.
  Under *no composite of rulers* (#29/#30) each figure is reported as its own register printed it.
- **A claim that arrived from a SEARCH SUMMARY and not from a register is struck** — that the
  Department's announcement states the change is not retrospective. The register was asked directly and
  **carries no such sentence**. That is **#41 catching its own defect on the way into a draft** rather
  than at a verdict, which is the margin #49 says is the right one. Two further brief sentences (the 88%
  trend since 2019, and safeguarding as *"met"/"not met"*) were not confirmed today and are not in the
  body.

**The gender read is a READ, 1 of 1**, and the hand-off line carries it: the 22 November 2022 release
introduces *"Ofsted's Chief Inspector, Amanda Spielman, said:"* and — confirmed by asking the page
directly today — carries **no third-person pronoun and no gendered title for her anywhere**. The feminine
comes from Ofsted's own speech standfirst, *"reflects on **her** first speech"*. The trap is named for the
Arabic composer: her own texts print *"His Majesty's Chief Inspector"* and that **His** is the monarch's.

**Cell 3 is the Editor's five-test verdict and it is the next content function's first action**, named
rather than implied. The draft leaves **three calls open for the Editor** that the drafter does not own:
the title, whether the struck retrospectivity claim belongs in the body, and whether the Bahrain
self-correction should open the piece instead of closing it.

**The 2026-11-13 note below is superseded in its CELL-2-OPEN reading and kept for the record.**

**Reconciled against disk 2026-11-13. BOTH OPEN GATES RESOLVED AND CELL 2 OPENS.** The 11-12 row said
cell 2 opens on a gate and not on the calendar. The gate opened today, from two first-party reads
recorded at `content-drafts/recon/2026-11-13-ofsted-the-two-gates-resolved.md`:

- **Gate 1, the operational voice** — Ofsted's own release of **22 November 2022** puts *Ofsted's Chief
  Inspector, Amanda Spielman* on the record about this exact cohort: *"The exemption was a policy founded
  on the hope that high standards, once achieved, would never drop"* and *"These outcomes show that
  removing a school from scrutiny does not make it better."* The Saudi bar is met by the operator of the
  instrument, inside the 2021–26 dateline. The union voices on the same story are representative rather
  than operational and are **not** carried.
- **Gate 2, the dated removal** — and it **corrected the commission**. The September 2024 removal of
  single-word overall judgements is the **Department for Education's** act, announced **2 September 2024**
  as *"scrapped with immediate effect"*, not the regulator's. The piece's frame — *the instrument has been
  replaced by its own author* — now has to say **which** author: the 10 November 2025 framework is
  Ofsted's own, the 2 September 2024 grade removal is the Department's. Two changes, two owners, fourteen
  months apart.
- **The gender read is a READ and not a declaration**, settled on Ofsted's own standfirst — *"Ofsted's
  Chief Inspector reflects on **her** first speech"* — after the release the voice comes from turned out
  to carry no pronoun at all, against the brief's own assumption that English registers carry them.

**Drafting is the next content function's first action.** It was not started today: the ceiling is one
fresh piece per day and this run's content slot was spent opening the gate that forbade drafting. *Named
rather than implied, so an unstarted draft does not read like a quiet day.*

**The 2026-11-12 note below is superseded in its GATED reading and kept for the record.**

**Reconciled against disk 2026-11-12. CELL 1 IS FILLED and the row is a commission rather than a
candidate:** the Editor's brief is at `content-drafts/briefs/2026-11-12-england-ofsted-exempt-cohort-brief.md`,
written off the 11-11 recon plus today's two owed reads (`content-drafts/recon/2026-11-12-ofsted-the-two-owed-reads.md`).
**Cell 2 does not open on the calendar, it opens on a gate:** the brief carries two open gates — the
operational voice (the Saudi bar: no named, operational, recent voice, no draft) and the dated first-party
read of the September 2024 removal of single-word overall judgements — and **drafting may not start until
gate 1 resolves or the piece is parked.** That is stated here and not only in the brief, because a row
reading *seven open cells* otherwise looks like six days of ordinary work queued behind it.

**What today's reads changed, recorded because it is the frame and not a detail.** The 11-11 recon
proceeded on a regulator that answered the Bahrain single's closing question with a cohort frozen by rule.
That stands. What the reads add is that the regulator has since **removed the overall grade entirely** —
`State-funded schools inspections and outcomes as at 31 August 2026`, published **2026-11-10**, two days
before this commission, is the first release of a framework in effect from **10 November 2025** — and
tells parents in its own voice that *"the new grades can't be compared to the old ones."* The piece is
commissioned on that pair: the measurement exists exactly once, and the instrument that produced it has
been replaced by its own author.

**The 2026-11-11 note below is superseded in its *candidate* reading and kept for the record.** Recon at `content-drafts/recon/2026-11-11-instrument-vs-schools-candidate-recon.md`: **candidate 1 (KHDA Dubai) parked and then UN-PARKED the same run, the park being wrong — ruling #139**, measured — `web.khda.gov.ae` serves its leaf certificate with no
intermediate, so the chain cannot be built by any client that verifies one — **and that is a `tls-chain` condition, which #80 ruled on 2026-10-01 is NOT an access failure**: the leaf's own AIA address yields an intermediate against which it verifies `OK`, valid to 18 December 2026, so every browser reads the register and only our client cannot; **candidate 2 (Ofsted, England) PROCEED**, because the regulator exempted outstanding
schools from routine inspection from May 2012, lifted the exemption in November 2020, re-graded the frozen
cohort and printed the yield beside the stock in one release — *"Only 17% of previously exempt schools that
had a graded inspection this year remained outstanding"* against *"Eighty-eight per cent of all schools are
good or outstanding."* **That is the Bahrain single's closing question answered by a regulator's own
arithmetic**, and the recon's contribution is that the piece's claim *the register that would settle it is
one nobody publishes anywhere* is false.

**Three reads are owed before the Editor's brief, and they are named in the recon rather than left to the
drafter:** the newest `state-funded-schools-inspections-and-outcomes` release for a current stock figure
(the one read is *as at 31 August 2022* and the piece is read in the reader's present, #117), Ofsted's
first-party account of the September 2024 removal of single-word overall judgements (a second instrument
change on the same register), and the Editor's call on whether an England candidate needs a Gulf register
to carry it or whether `bahrain-bqa-five-cycles` is a sufficient anchor **inside our own corpus** — which
would be the first time a single leans on a published predecessor that way.

**The 2026-11-10 note below is superseded by the paragraph above and kept for the record.** `bahrain-bqa-five-cycles` filled its eighth cell on 2026-11-09 and moved to *Shipped as
singles* below. **This is a state, not a gap, and the daily run must not read an empty table as a quiet
day:** with no wave to fall back on, an empty in-flight row means the next piece needs the first cell —
the Editor's brief, which needs the Researcher's recon first — and nothing downstream can advance until
it exists. **Standing rule for this file, from today: the run that empties this table names the next
commission's candidate in the same commit, or states plainly in the brief that it did not.** An empty
pipeline that nobody names reads exactly like a pipeline between pieces, which is the 71-day shape option
B was adopted to prevent, one scale down.

**Named today, not commissioned:** the obvious successor is the question the Bahrain single closed on, and
the operation does **not** yet have recon on it. Recon is the Researcher's and it precedes the Editor's
brief; it is queued as the next content function's first action rather than improvised at the end of a run
whose content function was spent on the board's head.

## Shipped as singles

| Piece | Shipped | Note |
|---|---|---|
| `2026-10-23-bahrain-bqa-five-cycles` — five cycles of public school grading | **2026-11-09** | The first single, and the first piece shipped since **2026-09-27** — a gap of **43 days**, named rather than smoothed. Also the first piece in this publication's history to ship with **no `edition:` field at all**, which needed no code change: the schema has always declared it optional and `/editions/` skips a null. Five gates bit on it before it could ship and every one was right. Corpus 45 EN and 45 AR. |

**Assets of record:** still at `web/public/stills/2026-10-23-bahrain-bqa-five-cycles.svg`, card at
`web/public/og/2026-10-23-bahrain-bqa-five-cycles.png` (1200×600, rendered by
`web/scripts/make-og-card.mjs` and **looked at**, per 2026-08-18). `heldAssets.mjs` no longer strips
either, the piece being approved.

## Standing prohibitions — these bind every piece here

Carried from Edition 05's commissions, where they were written, and they **outlive the edition**: they are
the terms four of those six pieces were commissioned under and they bind any successor piece on the same
ground.

- No **"best"** without its ruler in the same sentence; no composite of rulers (#29, #30).
- **Improvement never without its floor.**
- **Announced ≠ measured**, labelled at the figure — and from #117, an editorial future is written with its
  register's date attached or it is not written.
- The positive posture **never denies context** (the Sudan commission's term).
- A pair carries only what **both languages share** (#42) — and a figure printed only in an annotation is
  still published (#114).
- A named human's gender is read off the register's **pronoun, gendered title, or a morpheme the register
  prints** (#86 clause 1 as amended by **#134**), never off how a name sounds; where no register carries
  it, the determination is declared in the annotation as this edition's own, with its date (#86 clause 2).
- An **acronym** is expanded in the body only if `sources[]` expands it (#101).
- **Emphasis in the Arabic edition is carried by SYNTAX and by the register's own «  », and nothing
  visual replaces italic (settled 2026-11-15, standing-queue item 39).** Arabic typography has no italic
  convention — the same fact as *tracking is never applied to Arabic* (2026-08-18 clause 4) — and the
  house had said so three times as three point fixes (`[dir="rtl"] .pullquote`, the 10-17 strapline,
  #115), which is why the question kept returning as though it were open. It is not open: a slant, a
  tracking change or a weight shift would each be an import from a script that is not this one. **The
  converse binds too, and it is where the rule was being broken:** a run of **Latin** text inside an
  Arabic body keeps the Latin script's own conventions, italic included, because a journal title or a
  foreign-language phrase marks itself the way its own script marks it. The composer marks such a run
  with its `lang`, which the accessibility family has wanted since 2026-09-13.
- Where an acronym and a name are in **different languages**, the pair may be printed only if the **institution itself prints both together** in the body's language, and the annotation carries the owner's pairing in the owner's words with its register and date (**#141**). A translation is never silently promoted to an expansion; where the owner prints no name in our language, the body keeps the acronym.

## The hand-off lines a draft cannot reach the Editor without

A hand-off missing any of these is **returned unread** — the same teeth in every case:

- `dek: NNN/200 · title: NN/100` (code points, tashkeel +1 each) — 2026-07-27
- `annotation == sentence` per leaned-on source — 2026-09-13
- `named humans — gender read from register: N of M` — #86
- `acronyms expanded in the body: N, each expanded in sources[]: ☐` — #101
- `cross-language pairs: M, each printed together by the owner: ☐` — **#141**
- `editorial futures: N, each attributed to a dated register: ☐` — #117

**Re-measured 2026-11-10 (`agents/tools/arabic_side_reach.py`): 1 of 45 published pairs carries the #86
line and 1 carries the #101 line** — and it is the same pair, `2026-10-23-bahrain-bqa-five-cycles`, the
first piece drafted under all five hand-off lines and now shipped. The figure was **0 of 44** when
measured on 2026-11-07, because every published hand-off predates its rule — the 10-04 second amendment's
limb two, *a point-of-filing rule never reconciles backward*, on an obligation rather than a count. **The
step discontinuity is now visible in the register as one row**, which is what that limb asks for: the
rule's start date is the first row that satisfies it, and the 44 rows before it are a known error with a
known size.
