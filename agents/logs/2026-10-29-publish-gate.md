# Publish gate — 2026-10-29

**No `approved` flag moved today.** The gate is written out a row per piece anyway, because **a correction
to a published body is editorial** and five served documents' bytes changed. Four of the five are changes
to article bodies or annotations; the fifth pair is the two home pages, which carry no article.

Standing position: Edition 05 closed 2026-10-13, twelve flags in one commit; **no live edition**, so
nothing is held and the flag sweep runs in its all-approved inversion (2026-08-09 rule). `qa_census`
reads **approved 88 / held 0**; the held-slug leak assertion is vacuous by construction and says so.

## Row per piece

| Slug | Editions touched | What changed | Editor | Arabic Editor | Verifier | Assets | Flag |
|---|---|---|---|---|---|---|---|
| `2026-07-04-kenya-cbe-grade10-pathways` | EN + AR | **body**: the `KJSEA` expansion removed from the opening sentence of both editions, under #101 clause 1's second branch. The evidenced descriptive clause that follows it is unchanged in both | correction accepted on the ruling's own reasoning; no frame change, no figure touched | **required and given** — the Arabic edition's own rendering «تقييمٌ للتعليم الإعدادي في كينيا» is *removed*, which withdraws a determination the Arabic composer was forced to make with no register behind it. The withdrawal is the conservative direction | no figure moved; no trace axis re-opened | unchanged | **unchanged `true`** |
| `2026-07-07-singapore-psle-sbb` | EN + AR | **annotation only**: one source added, `seab.gov.sg/psle/`, quoting the board's own first sentence verbatim | accepted; a first-party register added, none replaced | accepted; the Arabic annotation carries the English sentence inside guillemets, because the claim is about an English document's bytes (#112) | the quoted token reads **`confirmed`** against the served bytes today | — | **unchanged `true`** |
| `2026-06-08-sierra-leone-tsc-teacher-matching` | EN + AR | **annotation only**: one source added, `tsctmis.org`, quoting the printed heading span and the strapline | accepted | accepted | the strapline token reads **`found`**; the heading token was re-cut after the register refused my first form (see the QA log, refusal 3) | — | **unchanged `true`** |
| `2026-06-10-rak-iqra-arabic-diglossia` | EN + AR | **annotation + body**: one source added (`povertyactionlab.org`) for the J-PAL name; the operator's programme-page annotation re-read and extended; one source added (the evaluator's trial page); and **a dated follow-up of three paragraphs composed in both editions** | **accepted as a dated follow-up and not a rewrite (#41).** The spine is untouched: the piece argued the foundation let someone else mark its homework, and the follow-up reports what the marker has since published and what the operator has not | **accepted.** Composed, not translated; every quoted string from both registers is carried in its own language inside guillemets, because both documents are English and a translated quotation is not a quotation | **figures traced to the evaluator's own served text today**: `0.19` SD word reading, `0.09` SD overall literacy, `0.17` learning-adjusted years, nineteen private of twenty-six schools, two-thirds native speakers, ages five to eight. All printed in both bodies; the quarter-of-a-year equivalence is the evaluator's own sentence, carried with its ruler named | hero still and og card unchanged and on disk | **unchanged `true`** |
| `/` and `/ar/` (home pages) | EN + AR | **chrome**: the masthead strapline promoted from `<p>` to `<h1>`, with `font-weight` pinned in both and `letter-spacing` pinned in the Arabic one | n/a — no editorial content | **accepted**: no Arabic text changed; the pin exists to stop display tracking reaching an Arabic run | n/a | n/a | n/a |

## Gate conditions

- **`npm run build` exit 0** — yes, four times today, the last on the committed tree.
- **Twenty-four postbuild assertions green** — yes.
- **Twelve build-job assertions green** — yes, via `build_job_gates.py` against the same `dist`, so the
  local gate set is the deploy's gate set rather than two-thirds of it (the 10-20 lesson).
- **Held-slug leak zero** — vacuously, and named as vacuous: there are no held pieces.
- **Hero stills and og cards** — unchanged; no new slug, so nothing new is owed.
- **Editor and Arabic verdicts on file** — for a correction to a published piece, recorded in this gate
  rather than as new verdict files, per the Edition 05 precedent for in-place corrections.
- **Figure discipline** — every quantity added to a body today was read in served text from the register
  that publishes it, on 2026-10-29, and every quantity added to an annotation is printed in its own body.
  `qa_annotation_figures` refused thirteen of my own annotation quantities before this was true (QA log,
  refusal 4), and they were **removed from served prose rather than registered**, because they were an
  HTTP status code, a queue number and a ruling number.
- **#119 clause applied to this run's own quotations, retroactively as of 10-28:** eight quoted spans were
  added to annotations today. Six are read from the form the document **prints** — a first body sentence
  (SEAB, J-PAL), an `<h1>` span and a strapline (tsctmis), and quoted prose from the evaluator's results
  section. Two are read from the operator's programme page's running prose. **None is taken from a
  `<title>`, a slug, an `og:title` or a result list**, and the one I did compose out of two `<h1>` lines
  was caught by the gate and re-cut.
