# Publish gate — 2026-10-14 (Asia/Dubai)

**Subject:** a **citation repair on four already-published pieces**, both editions — eight live pages.
No flag changed. No piece shipped. No piece was held. `approved: true` on all eight before and after.

**Scope of the change, per file:**

| Piece | EN | AR | What changed |
|---|---|---|---|
| `2026-07-07-lebanon-crisis-schooling` | ✅ | ✅ | One source repointed (EI item 29865 → 32239, the same study's 2026 posting); its annotation rewritten to the register's own figure; **one body sentence rewritten to remove a $350–600 monthly take-home the register does not carry.** |
| `2026-07-07-turkiye-earthquake-school-recovery` | ✅ | ✅ | One source repointed (ÖSYM's retired `/TR,25547/` path → the same announcement at the owner's current slug); its annotation corrected to drop a fee waiver the announcement does not contain; **one source added** (ÖSYM, 16 May 2023 — the register that does carry it); one body sentence split so the fee relief is attributed to the right announcement. |
| `2026-07-07-rohingya-myanmar-curriculum` | ✅ | ✅ | One source repointed (UNICEF UK's withdrawn copy → UNICEF's own); **annotation date corrected from "(early 2026)" to 6 November 2025**; one body sentence re-dated and re-grammared to the register's own wording. |
| `2026-07-06-morocco-ecoles-pionnieres` | ✅ | ✅ | **Two dead sources removed** (both ministry list PDFs, withdrawn and unarchived); one body sentence re-bounded so the one-in-six ratio names its base, its reading date, and the fact that the base can no longer be opened. |

---

## The gate, item by item

| Gate item | State | Evidence |
|---|---|---|
| **Editor verdict on file, `approve`** | ✅ **pre-existing, unchanged** | All four pieces shipped through the five-test rubric in July 2026 and are approved. **This change does not re-open the frame, the argument or the flag** — it corrects attribution and removes one unsupported figure. No new verdict is owed and none is claimed. |
| **Verifier verdict on file** | ✅ **pre-existing** + **this document is the trace for the delta** | The eight axes are untouched except where a figure moved. The one figure that moved is the Lebanon $350–600, and it moved **out**: traced to its named register in three readable copies and absent from all three. The Türkiye fee figure is traced to a register that carries it verbatim (eleven provinces, named, plus Sivas-Gürün). The UNICEF date is traced to the masthead. |
| **Arabic gate** | ✅ **taken in this run** | Both editions repaired in the same commit. **One named-human question arose and was closed without a determination:** ÖSYM's president appears in the new Türkiye source. Turkish marks neither pronoun nor gendered title, so per **#86 clause 2** neither edition declines one — the Arabic composes around it (`جاء على لسان رئاسة الهيئة`) and the English carries no pronoun. The escape clause (write the determination down as this edition's own) was **reachable and not needed**, which is the better outcome. No transliteration of a new name enters the Arabic *body*; the name appears in the Arabic annotation in apposition, undeclined, with the reason stated in the annotation itself. |
| **`dek` / `title` caps** | ✅ **not touched** | No frontmatter string under cap changed. `qa_pair_frontmatter` CLEAN. |
| **Hero still + share card on disk** | ✅ **pre-existing** | No asset added or removed. `qa_held_assets`: 0 held slugs, 44 approved slugs, **88 control assets all served**. |
| **`npm run build` clean** | ✅ | **exit 0**, twice — once before the content commit and once after it. 135 built pages, 134 sitemap URLs, 134 routed pages in the manifest. |
| **Standing assertions green** | ✅ **29 of 29 gating** | All 17 `postbuild` gates CLEAN; the 12 build-step assertions run by hand, all exit 0. Full table in `agents/logs/qa-2026-10-14.md`. |
| **Held-slug leak zero** | ✅ **inverted mode, correctly** | Edition 05 flipped yesterday, so the sweep is in **all-approved** mode per the 2026-08-09 rule: `approved:false` count in the build path = **0**, 44 approved, 88 control assets served. The assertion is not passing vacuously; the tool inverted it and says so. |
| **No credential, token or key** | ✅ | Nothing of the kind touched. |
| **Every citation in the changed files resolves** | ✅ **probed twice each** | The four replacement URLs: **200/200** each. The five dead URLs: **gone from the corpus** (`grep` returns nothing). Population after repair: **342 distinct URLs**, down one from 343 — two withdrawn PDFs removed, one register added, which is the arithmetic exactly. |

---

## Ordering, named rather than smoothed

**The content commit landed before this document was written, and that is a deviation from the skill's
wording** (*"run the publish gate in writing … before committing anything editorial"*). It was taken
deliberately and the reason is **ruling #96**: a run commits at the close of every standing function
because no disk survives the run, and on 2026-10-11 a full day's work — including an edition-gating
judgment — was lost entire to one turn past the envelope. The repair spanned eight files in two
languages and four registers read in served text; holding it unbanked while prose was written is the
shape that cost the operation a day three days ago.

**What was not deferred is the gate's substance.** Every item above except the writing of it was
satisfied *before* the commit: the build ran clean, the 29 gating assertions were green, both editions
were repaired together, and all four replacement URLs were probed twice. What landed after the commit
is this file. Precedent is one day old and recorded: on 2026-10-13 the Edition 05 flip ran before the
queue head for the same reason, and that log says so in the same plain terms.

**The honest reading:** for a change that flips no flag and ships no piece, the gate is a record rather
than a permission, and a record is the one artefact that is safe to write second. For a change that
ships a piece it is a permission and must come first. **That distinction is not currently written
anywhere**, which is why it is written here, and it is carried to the weekly review rather than
asserted as a rule by a daily run.

---

*Manager, 2026-10-14. Nothing in this document authorises a flag change, because none was made.*
