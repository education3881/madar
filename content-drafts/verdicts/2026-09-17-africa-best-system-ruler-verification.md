# Verification verdict — `2026-09-14-africa-best-system-ruler`

**Verifier · 2026-09-17** · Edition 05 (AFRICA) **mandated slot 3**, row 4 of the wave ledger
**Pair verdict of record:** `2026-09-15-ed05-best-system-pair-verdict.md` (four notes returned, all closed in-run, PASS, BANKED)
**Recon of record:** `2026-08-16-ed05-best-system-africa.md` → re-verified `2026-09-04-ed05-best-system-reverification.md`; blocker reads `2026-09-06-ed05-pasec-2019-report-read.md` and `2026-09-11-ed05-timss-2019-national-report-read.md`
**Commission:** `2026-09-04-ed05-best-system-commission.md` + addendum 2026-09-06
**P1 clock:** opened 2026-09-15 (banking), expires 2026-09-22 — **closed today, day 2 of 7.**

---

## VERDICT: **FAIL with five items.**

**Three closed in-run, in both languages. Two routed, because neither is a fidelity
fix and neither is mine to make.**

Every load-bearing figure traces. All four primaries were re-fetched today and read
in the body — not against the recon, against the documents — and the recon held on
every figure it cleared. The failures are where this edition's failures have been
since 09-08: **not one of the five items is a number.** Two are a hedge and a scope,
one is a vintage, one is a crown handed out on a reading nobody did, and one is a
publisher that no longer exists.

---

## 1. Coverage — what was re-read today, and by which route

Per #27 the drafter's compose-time read is channel one; this pass is the second,
independently routed channel. **Four of the ten registers are PDFs and were downloaded
and read with a text extractor rather than through a summarising fetch**, which is the
stronger route and the one that made items 1 and 2 visible.

| # | Register | Signature today | Route | Read |
|---|---|---|---|---|
| 1 | World Bank HCI 2020 country brief, Mauritius | **200** (158 KB, PDF) | curl → pdftotext | in full, both pages |
| 2 | CONFEMEN/PASEC, PASEC2019 international report | **200** (5.4 MB, PDF) | curl → pdftotext | Ch. 5 pp. 219–240, Graphique 3.62 p. 143, fn. 47 p. 235 |
| 3 | CONFEMEN's own page for the report | **200** | curl | locator confirmed under the `www.` form |
| 4 | CGD — Le Nestour, 19 Jan 2021 | **403 to our client / 200 by a second route** | curl refused, fetch served | in full |
| 5 | Reddy et al. (2021), TIMSS 2019 Gr 9 national report | **200** (4.2 MB, PDF) | curl → pdftotext | pp. 1, 14, 17–18, Figures 7 and 8 |
| 6 | HSRC press release, 8 Dec 2020 | **200** | fetch | in full |
| 7 | DBE TIMSS 2023 Highlights | **200** (1.4 MB, PDF) | curl → pdftotext | §1.3, §2.6.1, §3.1, §8 |
| 8 | La Nouvelle Tribune, Feb 2026 | **200** | fetch | in full |
| 9 | Educ'Action — the Baba-Moussa interview | **404 — AND THE PUBLISHER'S ROOT IS 404** | four routes, all refused | **not read — see item 5** |
| 10 | GPE — Hounkpodoté, 8 Oct 2018 | **200** | curl | in full |

**Egress proved before any silence was read as a fact about the world** (#54): `example.com`
200, `google.com` 200, and two distinct refusal signatures observed in the same minute
(`cgdev.org` 403, `eduactions.org` 404) — which is what makes the two dispositions
below different from each other rather than both "dead".

**#54's new checklist row, answered for every non-200:** source 4 is signature 2, *a
server denying **us***, and it is not a death — the publisher's root refuses our client
identically, and the document was read by a second route the same minute. Source 9 is
signature 1, a 404 with a served body, **and the search branch #54 prescribes has no
publisher to search** — see item 5.

---

## 2. Items

### ITEM 1 — **FAIL · the uniqueness claim is carried into a cell where the report names two countries.** Both languages. **CLOSED in-run.**

The piece, at the crown of ruler four:

> Senegal, it says, is the only country that between 2014 and 2019 manages to reduce
> inequality of performance — **a finding it repeats for mathematics.**

The report does not repeat that finding for mathematics. It repeats a *different* one.
Read as served today, p. 227:

> « En revanche, le Sénégal, **à nouveau, et le Tchad** se caractérisent par une
> diminution significative de leur variabilité. Au Sénégal, à l'image des résultats en
> lecture, les élèves les moins performants progressent davantage que les élèves les
> plus performants. Au Tchad, la moindre variabilité résulte essentiellement d'une
> diminution de la performance des élèves les plus performants. »

Table 5.8 confirms it in figures: Senegal SD **−12.9** (SE 4.5) and **Chad SD −10.3**
(SE 4.8). What the report repeats for mathematics is that Senegal's weakest pupils
progressed most. What it does **not** repeat is *le seul pays*. The "only" belongs to
the reading cell, p. 225, where the report grounds it on the reading standard deviation.

**Why this is the same defect the pair verdict already caught once.** Note 1 of the
09-15 verdict struck a `***` significance mark that had been carried from the
mathematics column and applied "at that level"; ruling **#51** — *a claim inherits the
scope of its register* — was filed on it. **Two sections later, in the same piece, the
same shape survived that verdict**: a qualifier printed in one cell, carried into the
next. A ruling filed on a piece does not sweep the piece.

**And it is the piece's own thesis, violated at its crown.** This is the article whose
argument is that a rank without its ruler is an opinion with decimal places. Its fourth
crown was handed out one cell wider than the register hands it out.

**Closed.** Both bodies and both `sources[]` annotations now carry the report's two
cells separately, with Chad named and the two mechanisms distinguished as the report
distinguishes them.

### ITEM 2 — **FAIL · a hedge in the register, absent from both bodies AND from both annotations.** **CLOSED in-run.**

The same sentence. The report, p. 225, as served:

> « Le Sénégal **apparaît comme** le seul pays qui, entre 2014 et 2019, parvient à
> réduire les inégalités de performance **puisque son écart-type diminue de 16 points.** »

*Apparaît comme.* The piece wrote **is**. The house rule is that a hedge in a source's
citation must appear in the sentence that uses it, and that the source's own grammar
is preferred over a firmer paraphrase; here the hedge was not in the citation either —
the annotation said "named on p. 225 as the only country that reduces performance
inequality", which is the same flattening one layer up.

**This is why it is filed as a separate item and not folded into item 1.** The 09-13
rule and ruling #53 both describe the failure as *annotation right, body wrong* — the
drafter composes the citation with the register open and the sentence from memory of
the citation. **This one is different and worse: the annotation was wrong too.** The
`annotation == sentence` hand-off line cannot catch a defect that is identical on both
sides of the comparison. What catches it is re-opening the register, which is what
ruling #53 requires a re-read to do and what this pass did.

Recorded, because it is the honest reading: the flattening is almost certainly
unconscious and it is almost certainly *correct* as a matter of fact — Senegal probably
is the only such country. That is exactly what makes it the kind of thing that stands.
A hedge dropped from a claim that happens to be true is still a claim the owner did not
make.

**Closed.** Both bodies now read *appears as*; both annotations carry « apparaît comme »
verbatim beside it, with the report's own stated reason (a standard deviation it gives
as falling 16 points) and the cell the claim is made in.

### ITEM 3 — **FAIL · ruler two crowns two of the four countries its own register names, and the piece gives no reading for the narrowing.** Both languages. **ROUTED TO THE EDITOR — not closed.**

The paragraph reports the register accurately:

> Gabon, Senegal, Benin and Burkina Faso cleared 410 and sat just above the global median

Verified verbatim today: *"With HLO scores over 410, Gabon, Senegal, Benin, and Burkina
Faso are just above the median of HLO scores at the global level."* **Four countries.**

The next paragraph then says:

> So ruler two crowns **Senegal and Benin**.

Nothing in the register singles out those two on this ruler. Everything the blog says
about Senegal and Benin specifically is about **progress** — *"The most striking results
are the significant progress in Niger and Benin, followed closely by Senegal"* — which
is **ruler three**, one section down, where the piece already crowns Niger. The
income-relative claim the blog makes is made of the francophone results *as a group*
(*"not below what we would expect considering their level of development"**)**, and it
crowns nobody.

**Why this is the sharpest item and why I will not fix it.** On a ruler whose stated
question is *how much a system produces given its means*, the four are not
interchangeable: Gabon is an upper-middle-income country and Burkina Faso is one of the
poorest in the world, and the piece drops the country with the **strongest** claim on
its own ruler alongside the one with the weakest — without a sentence either way. The
commission named "Senegal and Benin" at the top, so the narrowing is inherited rather
than invented; but the commission wrote that line before blocker 1 was closed, and the
09-06 report read revised the commission twice already.

Three options, and the Editor's call:

1. **Crown the register's own set** — all four that cleared 410 — and let the reader see
   the spread of incomes inside it. Costs one clause, gains the piece its own thesis.
   **The Verifier's recommendation.**
2. **State the basis for the narrowing** — but no register read for this piece ranks the
   four by income-adjusted performance. Composing one from GDP per capita and the HLO
   values would be a figure composed from a pattern (#41), and the piece's own argument
   forbids exactly that.
3. **Retire the crown on ruler two** and report the band as the analyst reports it.

Until the Editor rules, this ruler's crown is an unsourced narrowing sitting in a piece
about unsourced narrowings. **The pair cannot flip with it unresolved.**

### ITEM 4 — **FAIL · two vintages printed in the register, dropped from both bodies; "pre-COVID" stood in for a date fourteen years older.** **CLOSED in-run.**

The brief prints a year in parentheses beside **every** complementary indicator. Read as
served today:

> "In Mauritius, **40 percent (2006)** of 10-year-olds cannot read and understand a
> simple text… lower than the average for its region (80%)"
> "Mauritius spends **4.8 percent (2018)** of its GDP in government education spending…
> higher than both the regional average (4.0%)"

Both bodies printed the figures bare. The piece's vintage defence for the whole
paragraph was the brief's own blanket statement — *all data represent the status of
countries pre-COVID-19* — and that is a **floor, not a date**: a reader told "pre-COVID"
reads 2006 data as roughly 2019 data. The commission's own standing prohibition is
explicit and was written for this brief — *no figure from a country brief compared
across countries without both vintages stated* — and the learning-poverty sentence is a
cross-country comparison against a regional average whose own vintage the brief does not
give.

**Closed.** Both bodies now carry the years on the figures and say plainly that
pre-COVID is a floor and not a date, with the fourteen-year gap named.

*Everything else in the Mauritius paragraph traces exactly*: HCI 0.62 up from 0.60
between 2010 and 2020; 12.4 expected years → 9.4 learning-adjusted; 473 on a 300–625
scale; 98 in 100 surviving to five; "lack of data prevents comparison of HCI by gender"
with Table 1 giving 12.2 / 12.7 for expected years and a dash for the test score and the
learning-adjusted years. The crown sentence's scoping — *"on a single country brief read
against the regional averages the brief itself prints, not on a continental table"* —
is correct and is the 09-15 verdict's note 2 holding.

### ITEM 5 — **FAIL · the register behind the piece's closing demonstration no longer serves, and neither does its publisher.** **ROUTED — to the Editor, with the #54 procedure run and recorded.**

Source 9, the Educ'Action interview, is the register the piece's penultimate section
rests on entirely, and it is the origin case of **ruling #49**. It returns **404**, and
so does every other path on that host **including `/`**.

#54's procedure, run in order and each step recorded:

1. **Publisher's root probed first** — `eduactions.org/`, `https://eduactions.org`,
   `www.eduactions.org/`: **404 on all three.** A LiteSpeed server is answering and
   serving nothing. This is where #54's table stops being sufficient: it assumes a 404
   means *the publisher is alive and the path is not*, and prescribes a search of the
   publisher. **Here there is no publisher at that address to search.**
2. **Searched by headline, not by slug** — the document is still indexed, under exactly
   the title the piece describes. **That is a result list and it does not ride (#41).**
   It establishes that the document existed and was titled as the piece says. It cannot
   establish what the body says, which is the whole of the piece's claim.
3. **Three alternate publisher addresses probed** — all `000`. No re-slug, no migration.
4. **Two archives tried.** The Internet Archive's availability API confirms a snapshot
   **exists and is marked 200, captured 2025-04-27**; its body could not be read from
   this runner today — every route returned a challenge page or "Temporarily Offline",
   and `archive.ph` returned **429**. That is signature 2 stacked on signature 1: *the
   document is archived and we were refused today*, which is not the same as gone.

**What the piece claims and what can now be checked.** The claim has two halves. The
half about the **bound** — that PASEC 2024 is the last international evaluation *before
2030*, and that a PASEC 2028 cycle is named — is independently anchored on source 8,
read as served today at 200: *« la publication est annoncée pour le dernier trimestre
2026 »* and *« anticiper la transition vers le cycle d'évaluation Pasec 2028 »*. The
half about the **headline** — that a headline kept the superlative and dropped the
bounding clause — rests on source 9 alone and **cannot be verified today by any route
this operation is willing to cite.**

**Why I am not editing the source line.** Citation disposition is the Editor's, and this
operation's practice is settled: the 09-09 verdict recorded Sierra Leone's 404 and left
it; the 09-16 re-probe wrote *"No source line was edited by this run."* Recording is the
Verifier's job. But the annotation currently reads "read in served text" with no date,
and that is a promise the URL no longer keeps.

Options for the Editor:

1. **Carry as fetched-on-date (#41)** — the annotation states the date it was read and
   that the publisher's whole host returned 404 on 2026-09-17. Honest, and leaves a
   reader with a dead link and our word.
2. **Add the archive snapshot as the locator of record beside it**, re-ranked per #43 as
   what it is — an archive of a newspaper interview, not the newspaper. Requires reading
   the snapshot first, which today's runner could not do.
3. **Retire the demonstration.** The section's *argument* survives on source 8; what
   would be lost is the specific example, which is also the example ruling #49 was
   earned on.

**The Verifier's recommendation is 2, contingent, then 1:** attempt the snapshot read
from a run whose egress the archive does not refuse, and fall back to 1 with the host's
death stated. **Do not drop it silently** — a register that vanished after we read it is
itself part of the record, and #49 is cited by number in four artefacts.

---

## 3. What traces — the full figure trace

**Every load-bearing figure in the piece was re-anchored today against the primary, not
against the recon.** Recorded compactly because none of it failed.

**PASEC (report body, read today):** the trend chapter's ten countries and the
Hausa/Zarma/Arabic exclusion, p. 220 verbatim ✓ · Niger largest gain in all four series
— start language **+76.9\*\*\*** (Table 5.1), start maths **+89.2\*\*\***, end reading
**+67.5\*\*\***, end maths **+56.0\*\*\*** ✓ · end-of-primary reading mean 500.0 → 519.8,
**+19.8\*\*\***, against maths 500.0 → 501.4, **+1.4** unstarred ✓ · **"Niger and Benin the
only two countries whose *gains* were statistically significant"** — Table 5.7 shows five
significant differences and exactly two of them positive, so the piece's word *gains* is
load-bearing and correct ✓ · Niger P10 **+51.6** against P90 **+139.3**, Benin P10
**+25.5** against P90 **+128.6**, both Table 5.2 ✓ · Benin mean +66.5 with the report's
own *« plafonne à quelque 25 points… près de 130 points »* ✓ · Rho means rising at all
four levels, 0.54→0.61, 0.40→0.50, 0.49→0.54, 0.45→0.54 (Tables 5.9–5.12) — and the
piece's *"on average"* is exactly the scope the recon corrected the blog down to ✓ ·
rural–urban explanation **rejected** in the report's own words, *« permettent donc
globalement d'infirmer l'hypothèse »*, p. 232 ✓ · Senegal rural–urban maths gap −38.2 ✓ ·
Burundi *« le seul pays qui a connu une régression aussi bien en lecture qu'en
mathématiques »* ✓ · class size Graphique 3.62, Niger 39.6 → 40.7, Congo 55.2 → 57.2,
eight of ten falling ✓ · Table 5.13 policy register verbatim including **70%** and
*« résiliation des contrats »* ✓ · footnote 47 verbatim ✓ · p. 224 *« devra être confirmée
par la prochaine étude PASEC »* ✓.

**TIMSS 2019 (report body, read today):** 285 → 389 = **104**, stated by the report as
one standard deviation, twice, bounded 2003–2019 ✓ · decomposition **+67 / +20 / +17**,
all cycle-to-cycle differences statistically significant ✓ · six points a year, **7.4**
then **4.6**, with *"it would take the country longer to reach the achievement levels to
which it aspires"* ✓ · range **320 → 252**, best gains at the lower end, *"since 2011…
very little improvement at the top end"* ✓ · **11 → 41 percent** ✓ · Reader's Guide p. 14,
scale 0–1000, centrepoint 500, **SD 100 by construction** — the piece says *"104 points,
which is one standard deviation on the TIMSS scale"* and never "a one-SD gain", which is
#48's corollary carried exactly ✓ · the seam: Gr 8 for 1995/1999/2003 and Gr 9 from 2003,
**21 points**, *"provides the bridge"*, *"from 1995 to 2003 there was no significant
change"* ✓ · **0.9 SD appears nowhere in either body** (grep: zero) ✓.

**TIMSS 2023 (report body, read today):** 389 → 397 with *"not statistically significant,
indicating that achievement levels have remained relatively stable"* ✓ · the reliability
reservation quoted to the right row — **Grade 9 Mathematics**, *"exceeds 15% but does not
exceed 25%"* ✓ · Grade 5 **362**, and the report's own list of the lowest performers ends
on it ✓ · counts held to their cycles, **39 + 7** for 2019 and **59 + 6** for the 2023
fourth grade, both verbatim ✓.

**GPE (read today):** Hounkpodoté, CONFEMEN, **8 October 2018**, on **PASEC 2014**, *"these
results demonstrate that despite progress in access to education, more schooling is not
leading to more learning"* ✓ — vintage and round both carried in the sentence, which is
#47 honoured.

**Guardrails — 8 of 8 carried in prose, none silently avoided.** No "best" without its
ruler in the same sentence ✓ · no composite, and the piece says so outright ✓ ·
improvement never without its floor — Niger ✓ (the 09-15 note 4 fix holding), South
Africa ✓, Benin ✓, Senegal ✓ · Niger's French-tested qualifier in-sentence ✓ · Le
Nestour's inference attributed to him and the report's disclaimer quoted where the list
appears ✓ · *"sack"* appears once, in the sentence refusing it ✓ · **Seychelles named
nowhere in either language** (grep: zero) ✓ · aggregator tier cited nowhere, category
named once, in the lede ✓.

**Schema and state.** EN title **53**/100, dek **162**/200; AR title **58**/100, dek
**145**/200 — code points, tashkeel counted. `related:` resolves to three slugs, all held,
all present; `qa_body_links` reports 0 rail dead ends. Still on disk, og card on disk,
both withheld from `dist` by the build hook. **`approved: false` in both files; no stale
`approved: true` duplicate anywhere in the tree** (#18). **Numeral multiset re-computed
after every edit: EN 109 tokens, AR 102, zero Arabic-only figures**; the seven
English-only tokens are the grade labels 5, 8 and 9, which Arabic renders as ordinal
words — the Zambia-pair precedent, unchanged by today's edits.

---

## 4. Carried to the gate — notes, not failures

1. **The piece is 2,332 words against a commission cap of ≤2,300.** It was ~2,250 at
   banking; today's three closures added the rest, and every added word is a hedge, a
   scope or a vintage. I have tightened them twice and will not cut register-bearing
   prose to meet a length. **The Editor owns the cap and can waive its own commission.**
2. **"He spent two years as a technical adviser to PASEC before writing it."** The
   annotation attributes this to "the author's bio **on the served page**". Read twice
   today by two prompts, the blog page carries a linked byline and **no biographical
   text at all**. The fact may well be true on the author's separate profile page; the
   citation as written points at a page that does not carry it. Not fixed here because
   it is one word of sourcing, not a claim about the world — but it is #52's shape
   applied to a citation, and it should be re-pointed or dropped at the gate.
3. **The report's running footer reads "ÉVALUATION PASEC2020" through Chapter 5** against
   PASEC2019 on the cover and title — the #38 drift the 09-06 read flagged. The piece
   cites by title and is correct. Recorded so no later reader "corrects" it.
4. **Source 4 is walled to our client (403) and readable by another route.** Carried as
   read, with both signatures named. No action — but the confirmation read should not be
   surprised by it.

---

## 5. Disposition

**The pair stays HELD.** Items 1, 2 and 4 are closed in both languages and the piece is
better for them. **Items 3 and 5 are open and both are the Editor's**, and item 3 in
particular cannot be waived quietly: it is a crown resting on no reading, in the piece
whose subject is crowns resting on no reading.

**Verification backlog for Edition 05 is now zero** — four pairs banked, four verified.
The ceiling (drafting ≤ 3 ahead of the last verdict) is clear with room for Egypt and
Rwanda both.

**What the wave still owes before it can flip:** three confirmation reads (Zambia, Sierra
Leone, Sudan), this pair's two open items, the Arabic Editor's two register questions
from 09-15, the three reciprocal `related:` edges into row 4, and a completed
`qa_sources_alive --held-only` sweep — which is a **P1 to the Web Developer since 09-16
and is now also mine**: the ledger makes that sweep the last step before the flip commit,
and it has never once finished.

— Verifier · 2026-09-17
