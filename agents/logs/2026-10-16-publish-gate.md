# Publish gate — 2026-10-16 (Asia/Dubai)

**What is shipping:** a correction to one published pair, `2026-06-20-oman-school-performance-ratings`,
EN and AR, in one commit. No flag moves, no new piece, no asset changes. The corpus stays at **44 EN /
44 AR, all approved**.

## The correction, stated plainly

Both editions named the Omani inspectorate, **in the present tense**, as the *Oman Authority for Academic
Accreditation and Quality Assurance of Education*. That has not been its name since **12 January 2026**.
**Royal Decree 12/2026** (22 Rajab 1447; Official Gazette 1630a, 13 January 2026) renames it the **Oman
Authority for Quality Assurance of Education** in Article I, and in Articles III and IV moves professional
licences and the national and international studies to it from the Ministry of Education, with those
divisions' officers.

The piece published **2026-06-20**, five months after the decree. The wrong name has been served in both
languages for **118 days**.

**And the annotation was not silent — it was wrong in a way nothing we own can read.** Both editions
carried a `gov.om` source whose parenthetical said *"the issuing body and its mandate; renamed in 2026"*.
That page says **nothing about a rename**: read in served text today it prints the short name as its title
and the long, former name in its management listing, with no date and no instrument. The annotation was
**right by accident and sourced to a document that does not support it** — which is why the body could sit
beside it for 118 days without any check objecting.

## How it was found, and by which instrument

Not by a regex. **By the forced-rendering control, ruling #101 clause 3**, applied deliberately for the
first time: where two editions render one institution, the edition that *cannot* carry the acronym is the
control. Arabic cannot, so the AR annotations were read first — and the AR side carries both names, the
long one in two Times of Oman citations and the short one in the gov.om and oaaaqa.gov.om entries, with
the rename flagged. The disagreement between *the piece's own two editions' annotations* is what pointed
at the register. Neither `qa_pair_frontmatter` nor the `annotation == sentence` check can see it: both
editions made the **same** error in the body (#42, #86 — parity is a floor), and the annotation did carry
a name, so there was no silence to notice (#101's own defect, one turn out).

## What was written, and in whose words

Both bodies now use the current name in the present tense, name the former name with the date it stopped
being the name, and say why the launch and the first evaluation phase keep the older name — *because that
is the name their own registers print* (#101 clause 4: a correction to a named institution is written in
the register's own words, not in a better paraphrase).

Both annotation sets: the `gov.om` parenthetical now states what that page actually prints and that it says
nothing about a rename; and a **new source** carries the decree itself, in each edition's own language,
with its number, both dates, the Gazette issue, and the two articles it is cited for.

## The gate, item by item

| Gate | State |
|---|---|
| Editorial verdicts on file | **Not required** — this is a correction to a published pair under #100/#101, not a commission. No flag moves. |
| Arabic gate | **Taken in-run.** The AR sentence is composed, not translated: `وكان اسمُها … حتى 12 يناير 2026، حين أسقط المرسومُ السلطانيُّ رقم 12/2026 «الاعتماد الأكاديمي» من اسمها`. The decree is cited in Arabic from its own Arabic-language register, not transliterated out of the English note. |
| `annotation == sentence`, both editions | **Pass, and it is now true rather than vacuous** — the expansion in each body is the expansion in that body's own `sources[]`. |
| `dek` / `title` caps | **Untouched.** Neither field was edited. |
| Hero still, og card | **Untouched**, both on disk and resolving in both built pages. |
| `npm run build` | **exit 0**, read from the exit code and not through a filter (the 10-15 addendum's rule). |
| 17 `postbuild` assertions | **green** — exit 0 on the build that gates them. |
| 12 CI build-step assertions, re-run by hand on this `dist` | **green, twelve exit-0 readings printed individually** (`qa_dist_input`, `qa_robots`, `qa_hreflang_clusters`, `qa_body_links`, `qa_lastmod`, `qa_held_assets`, `qa_reachability`, `qa_jsonld`, `qa_a11y_lang`, `qa_ar_language`, `qa_consumer_surface`, `qa_geo_fields`). |
| `qa_pair_frontmatter` | **CLEAN** — 44 pairs, 682 citations, 342 distinct URLs, three declared asymmetries unchanged. The new decree source is present on both sides, so the pair gained a shared annotation rather than an asymmetry. |
| Held-slug leak | **n/a in held mode and asserted in the inverted mode** (08-09 rule): `qa_held_assets` reads 0 held slugs, 44 approved, 88 control assets. |
| Both new/changed URLs probed | `decree.om/2026/rd20260012/` **200**, `gov.om/en/authority-for-academic-accreditation-…` **200**, both read in served text today and not from a result list (#41). |
| Repair present in the served artefact | Verified in `dist`, not in the source: EN page carries `Royal Decree 12/2026` ×3 and the current name ×5; AR page carries `12/2026` ×3 and `الهيئةُ العُمانية لضمان جودة التعليم`; `decree.om` ×2 on each. |

**Verdict: PASS.** Committed and pushed as the content function's own commit, per ruling #96.
