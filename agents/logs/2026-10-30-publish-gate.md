# Publish gate — 2026-10-30

**No `approved` flag moved today.** The gate is written out a row per piece anyway, because **a correction
to a published body is editorial** and served bytes changed on 89 documents: one pair's body and
annotations, and the marginalia heading on all 88 article pages.

Standing position: Edition 05 closed 2026-10-13, twelve flags in one commit; **no live edition**, so
nothing is held and the flag sweep runs in its all-approved inversion (2026-08-09 rule). `qa_census`
reads **approved 88 / held 0**; the held-slug leak assertion is vacuous by construction and says so.

## Row per piece

| Slug | Editions touched | What changed | Editor | Arabic Editor | Verifier | Assets | Flag |
|---|---|---|---|---|---|---|---|
| `2026-07-28-england-report-cards-first-term` | EN + AR | **body + annotations.** (a) **A correction**: the sentence *the second instrument has not reported yet* was true when written and was falsified by Ofsted publishing the evaluation's interim summary on 9 October 2026; both editions now say it has reported in part, with the date and the window. (b) **A dated follow-up of two paragraphs in each edition**, reading the September 2026 context measure after its date. (c) **Three registers added to both editions.** | **accepted as a dated follow-up and a correction, not a rewrite (#41).** The spine is untouched: the piece argues the regime built to judge schools is now itself judged and the readings disagree, and the follow-up adds a register that both confirms the measure arrived and bounds what it does. The correction is #117 with a third party's clock on it, which is the day's forward question | **accepted.** Composed, not translated. Every quoted string is carried in its own language inside guillemets **and the English original beside it** where the claim is about an English document's bytes (#112), because a translated quotation is not a quotation | **figures traced to served text today, 30 October 2026**: 50 similar schools; nine variables in four groups counted off the register's own list; nearly 3,300 inspections; just 15%; nearly 3,200 full inspections; 73% / 58%; 88% / 68%; 17% / 44%; 18% / 57%; 41% of 119; 65% / 47%. All printed in both bodies. **The two evaluation figures are labelled in the body as quoted by Ofsted rather than read in the evaluation**, whose summary is a ten-page PDF no client here can open | hero still and og card unchanged and on disk | **unchanged `true`** |
| all 88 article pages | EN + AR | **chrome**: the marginalia rail's label promoted from `<h4>` to `<h2>`, with its stylesheet selector following the tag and the reason written at the point of change | n/a — no editorial content | **accepted**: no Arabic text changed; the Arabic label `المرجع الميداني` is the same string at the same pixel, measured | n/a | n/a | n/a |

## Gate conditions

- **`npm run build` exit 0** — yes, four times today, the last on the committed tree.
- **Twenty-five postbuild assertions green** — yes, including standing assertion **40** (`qa_brief_head`)
  wired this morning.
- **Twelve build-job assertions green** — yes, via `build_job_gates.py` against the same `dist`, so the
  local gate set is the deploy's gate set rather than two-thirds of it (the 10-20 lesson).
- **Held-slug leak zero** — vacuously, and named as vacuous: there are no held pieces.
- **Hero stills and og cards** — unchanged; no new slug, so nothing new is owed.
- **Editor and Arabic verdicts on file** — for a correction to a published piece, recorded in this gate
  rather than as new verdict files, per the Edition 05 precedent for in-place corrections.
- **Figure discipline** — every quantity added to a body today was read in served text from the register
  that publishes it, on 2026-10-30. `qa_annotation_figures` refused one of my own annotation quantities
  before this was true (`370`, a PDF's file size, written into an annotation and into no body); it was
  **rewritten in words rather than registered**, because a file size is not a published figure.
- **#119 applied to this run's own quotations:** eighteen Latin quoted spans were added to annotations
  today and **all eighteen read `found` against the served bytes**. The three document names are quoted in
  the form each page **prints as its own heading** — *Similar schools model for attainment: overview*,
  *Considering the context of schools in challenging circumstances: an analysis of similar schools data*,
  *Evaluation of Ofsted's renewed approach to education inspection: summary of interim findings*. **None is
  taken from a `<title>`, a slug, an `og:title` or a result list.**
- **#101 applied:** the body expands `SEN`, `EHC`, `EAL`, `IDACI`, `POLAR4`, `FSM` and `IDSR` nowhere that
  the annotations do not expand them in the register's own words; `qa_acronym_evidence` green.
- **#117 applied:** the follow-up's one forward-looking clause is attributed to a dated register (the
  terms of reference putting the full report in 2027) rather than asserted.
- **Founder-facing artefacts** — `qa_artefact_render` green on all 139; **`qa_brief_head` green on 118
  briefs and 20 reviews** for the first time, after nine editorial rewrites and one date repair.
