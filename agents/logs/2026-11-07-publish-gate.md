# Publish gate — 2026-11-07

**Nothing publishes, and for the first time in this sequence SERVED BYTES CHANGED anyway.** No flag
moved; the content collection is unchanged at **44 EN / 44 AR**. But today's content function
**repaired a sentence in both editions of a piece that is already live**, so this gate is not the
nothing-happened record the last four have been.

## The ordering was wrong today, and it is written down rather than smoothed

The rule is *the publish gate runs in writing before any editorial commit* (CHARTER §3, RUNBOOK). This
run committed `1of5` — containing the repair to both served editions of
`2026-05-26-bahrain-bqa-public-grades`, the Arabic composition, the Editor's disposition 3 and the
Verifier's re-trace — **and wrote this gate afterwards**, inside the quality function. #96's *commit at
the close of every standing function* and the publish-gate rule point in opposite directions on a day
when the content function changes a served byte, and this run resolved the conflict by banking the work
and is recording the cost instead of claiming the order was right.

**What would have been caught by doing it in the right order: nothing, today.** Every row below passes
and the build is green. **That is exactly why it is worth writing down** — a gate run after the commit
that reads clean is indistinguishable from a gate run before it, which is the 2026-09-13 silent-pass
trap aimed at a procedure rather than at an assertion. The correct shape, for the next run that
repairs a served piece: the gate's rows for the repair are written and checked *in the content
function*, before its own commit, and the quality function then re-reads them.

## 1 · The served repair — the rows that actually applied today

| Row | State |
|---|---|
| The claim repaired is traced to a register read today | ☑ HTTP 200, 2,635,898 bytes, `Last-Modified` 2026-10-04, upload path dated 2026-07 |
| The repair carries the register's dated state, not a new estimate (#117) | ☑ both editions |
| No new figure introduced | ☑ three facts, each a probe recorded today |
| No quotation reproduced from a PDF extraction (#129) | ☑ nothing quoted in either repaired page |
| Both editions repaired in the same commit | ☑ — a pair carries only what both languages share (#42) |
| Verifier trace on the repair, axes 1 and 3 | ☑ `2026-11-07-bahrain-bqa-five-cycles-verification-retrace.md` §3 |
| Build clean after the change | ☑ exit 0, **39 of 39** gating green |
| Arabic Editor's gate on the Arabic repair | ☐ **owed** — the AR sentence is prose this desk composed, and it ships to the origin tonight in a commit the Arabic Editor has not gated |

**That last row is an open hole and it is named rather than waved through.** The AR repair is one
sentence, composed from a probe and carrying no quotation, and holding the EN half back to wait for the
gate would leave the pair disagreeing on the served page — which #42 forbids more loudly. So both went,
and the Arabic Editor's read is queued as the first row of tomorrow's content function. *The choice was
between an ungated Arabic sentence and a pair that contradicts itself; this gate records which one was
taken and why.*

## 2 · The Bahrain pair — the rows that are still the real gate

| Row | State |
|---|---|
| Editor five-test verdict on file | ☑ `2026-11-02-bahrain-bqa-five-cycles.md` |
| Editor dispositions 1 and 2 | ☑ `2026-11-05-bahrain-bqa-five-cycles-dispositions.md` |
| Editor disposition 3 (the batch's four-grade shape) | ☑ `2026-11-07-bahrain-bqa-five-cycles-disposition-3.md`, C4 and C5 applied in the same commit |
| Verifier verdict on file | ☑ `2026-11-03`, re-opened and **CLOSED today** on both dispositions, axes 1 and 3 PASS |
| **Arabic composition** | ☑ **LANDED TODAY** — `content-drafts/drafts/2026-11-07-bahrain-bqa-five-cycles-ar.md`, composed from the Arabic register and not from the English draft |
| Arabic Editor's gate (Gate 4) | ☐ **owed, and it is now the pair's binding constraint** |
| Hero still `/web/public/stills/<slug>.svg` | ☐ not commissioned |
| og card `/web/public/og/<slug>.png` | ☐ not generated |
| `edition:` field | ☐ **blocked on founder issue #13**, stated default **2026-11-08** at tomorrow's weekly review |
| Caps at compose, code points, tashkeel +1 | ☑ AR `dek 158/200 · title 47/100`, counted on the composed strings and **corrected after counting** — the hand-off line was written at 191/158 from an estimate and the measured number replaced it |
| `annotation == sentence`, per leaned-on register | ☑ every figure read by the composing desk in the Arabic column or the Arabic PDF, with one stated exception (the Gold Seals pair, read in English, with the reason) |
| Named humans — gender read from register | ☑ **0 of 0** — the composition names no individual |
| Acronyms expanded in the body, each in `sources[]` | ☑ **0 expanded, 0 needed** — the Arabic body carries no Latin acronym at all |
| Registers with no archival snapshot | ☑ **2 of 5 accepted** (disposition 1) — **and the row is widened today: the Arabic edition cites DIFFERENT URLs for the same two documents, so the accepted-risk row names FOUR URLs, not two** |

## 3 · The single-copy risk, amended a second time and in the honest direction

The 11-05 and 11-06 gates recorded the two first-party PDFs as single-copy and accepted. Yesterday's
gate amended that: each has an Arabic edition, **and a second edition on the same host is not
independent persistence — if the host goes, both go.** Today adds the sharper half: **one of those two
Arabic editions cannot be read at all.** The Arabic annual report is served (HTTP 200, 12,967,817
bytes) and carries **zero `/ToUnicode` CMaps**, so 14,497 text-showing strings map to 1,990,133 bytes
of glyph indices and no character stream. **A second edition that no client can read is not a second
copy of the claim; it is a second copy of the file.** The Gold Seals pair therefore stays attributed to
the English edition, where it was read (#131).

## 4 · Held-leak

**VACUOUS**, per the 2026-08-09 inversion: nothing is held in the content collection at all — both
Bahrain editions are drafts outside `web/src/content/**` — so the held-mode sweep has nothing to find
and says so rather than reporting a pass.

---

**Signed** · Manager · 2026-11-07 · *the gate found nothing wrong and still earned its keep, because
the thing it had to record was its own lateness and one ungated Arabic sentence going to the origin
tonight.*
