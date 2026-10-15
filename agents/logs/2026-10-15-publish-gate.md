# Publish gate — 2026-10-15 (Asia/Dubai)

**Subject:** a **citation disposition and one factual correction on one already-published piece**, both
editions — two live pages. No flag changed. No piece shipped. No piece was held. `approved: true` on both
before and after.

**Scope of the change, per file:**

| Piece | EN | AR | What changed |
|---|---|---|---|
| `2026-07-04-kenya-cbe-grade10-pathways` | ✅ | ✅ | **One dead source removed** (Education News (Kenya), *withdrawn and unarchived* — ruling #100's fourth disposition, the only one that removes a link). The quotation it was credited with is **re-sourced to the Daily Nation register already on file**, whose annotation now carries the quotation as read. **EN body corrected: the association's name.** AR body was already right and is untouched. |

---

## The correction, stated plainly

The English body read *"Willy Kuria, the serving principal who chairs the **Kenya Senior School Heads
Association**"*. The register says **Kenya Secondary Schools Heads Association**, and so does the Arabic
edition (*رابطةَ مديري المدارس الثانوية في كينيا*). The English was wrong from publication on 2026-07-04 —
**103 days** — and the likely mechanism is visible once stated: the piece's own dominant noun is *senior
school* (the roll-out, the cohort, the placement, three times in the same paragraph), and the institution's
name was composed from the piece's vocabulary rather than from the source's. Corrected to the register's own
words.

**The channel that caught it is the Arabic edition, for the second time in twelve days (#86, 2026-10-03).**
And the reason it could is structural rather than lucky: the English annotation carries only the acronym
*KESSHA*, so the `annotation == sentence` hand-off check (2026-09-13) had nothing to compare the expansion
against — **an expansion the annotation does not contain is unreachable by a check that reads the
annotation.** Arabic cannot carry a Latin acronym as a name, so the Arabic composer had to go back to the
register and expand it. Filed as **ruling #101**.

## The disposition, per ruling #100

| Question | Answer |
|---|---|
| Is it dead? | **Yes.** `educationnews.co.ke/principals-sound-alarm…/` returns **308 → 404** on two reads (2026-10-15, 09:21 UTC). The 308 is a trailing-slash normalisation, not a content move. |
| Does the host live? | **Yes — 200 at the root**, which is #54's *go look* signature. |
| Scheme moved? | **No.** The WordPress ID permalink `?p=508411` returns **200 and serves a listing page** with no Kuria text — a **false-alive shape**: a sweep probing that URL would score it healthy. |
| Parent's or archived copy? | **No.** Wayback holds **zero snapshots** of the URL. |
| Superseded? | **No successor posting found.** |
| **Disposition** | **Withdrawn and unarchived → the link is removed.** |
| Does the annotation survive its register? | **The claim does, in a different register.** The quotation is carried verbatim by the Daily Nation piece already cited in the same `sources[]`, read in served text today: *"We have a serious staffing deficit. Under CBE, we need qualified personnel for specialised subjects like aviation, marine technology, and building and construction. Currently, we don't have these staff. I doubt there is a school in the country that is fully equipped with these teachers," said national chairperson of the association, Mr Willy Kuria.* The body's elision is restored in our own prose, as published. |

**A wall is not a death, and the route round one is recorded rather than remembered.** `nation.africa`
returns **403 to a machine** (bot wall — it is one of the 42 walled URLs yesterday's full-population sweep
counted, 12.3% of our outbound promises). The same article is served in full, to a machine, at
**`beta.nation.co.ke`** on the identical path. The citation keeps the canonical URL, because that is the URL
a reader should open; the mirror is a **verification route**, and it is written down here because the
alternative is each future run re-discovering it or recording the claim as unverifiable.

---

## The gate, item by item

| Gate item | State | Evidence |
|---|---|---|
| **Editor verdict on file, `approve`** | ✅ **pre-existing, unchanged** | The piece shipped through the five-test rubric on 2026-07-04. **This change is a correction to a named institution and a citation disposition, not a re-commission** — the frame, the argument and all four STEM numbers are untouched. |
| **Verifier verdict on file** | ✅ **pre-existing** + this document is the trace for the delta | No figure moved. The non-numeric axes are what moved: **noun (#45)** — corrected; **quotation (#46)** — re-read verbatim in served text and unchanged in the body. |
| **Arabic gate** | ✅ **taken in this run** | The AR body needed **no correction** — it already carried the register's own *الثانوية*. The AR annotation was recomposed in Arabic, not translated, and carries the quotation and one new named entity: **Murang'a High School → مدرسة مورانغا الثانوية** (transliteration from the register's own spelling, `Murang'a`; the name was already present in no form, so this is a first use). Named-human gender: **Mr Willy Kuria, masculine, read from the register's own *"Mr"* and *"he added"*, not from the name** (#86, binding). |
| **`dek` / `title` caps** | ✅ **not touched** | No capped frontmatter string changed. `qa_pair_frontmatter` CLEAN. |
| **Hero still + share card on disk** | ✅ **pre-existing** | No asset added or removed. `qa_held_assets`: **0 held slugs, 44 approved slugs, 88 control assets all served**. |
| **`npm run build` clean** | ✅ | **exit 0, twice** — once with the repair on disk and once after the content commit. 134 routed pages, 134 sitemap URLs, 134 lastmod. |
| **Standing assertions green** | ✅ **29 of 29 gating** | All **17** `postbuild` gates CLEAN (verified by name against `package.json`: 17 of 17 appear in the build log); the **12** build-step assertions run by hand, all exit 0. Full table in `agents/logs/qa-2026-10-15.md`. |
| **Held-slug leak zero** | ✅ **inverted mode, correctly** | All-approved mode per the 2026-08-09 rule: `approved:false` count in the build path = **0**, 44 approved. |
| **EN/AR parity** | ✅ | **12 source URLs each** after the removal, same as each other. `qa_pair_frontmatter` CLEAN, `qa_body_links` PASS — every source URL an approved article declares is rendered. |
| **No credential, token or key** | ✅ | Nothing of the kind touched. |
| **Every citation in the changed files resolves** | ✅ **probed** | The removed URL is **gone from the corpus** (`grep` over `web/src/**`: zero hits; two hits remain in a July **recon memo**, which is unpublished and is a dated record of what was read then — deliberately not rewritten). The outbound population moves **342 → 341**. |

**Gate verdict: PASS.** Two live pages change; both carry a correction a reader can check against a register
a reader can open.
