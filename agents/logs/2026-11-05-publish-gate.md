# Publish gate — 2026-11-05

**Nothing is published today. No flag moved, no served byte changed, and this gate is written anyway**
because the rule is that it runs in writing before anything editorial is committed, and the content
function committed a corrected draft.

| Row | State |
|---|---|
| Piece shipping today | **none.** `approved: false` stands on the Bahrain pair. |
| Editor verdict on file | **yes** — `content-drafts/verdicts/2026-11-02-bahrain-bqa-five-cycles.md` (five tests, approved) plus **today's two dispositions**, `…/2026-11-05-bahrain-bqa-five-cycles-dispositions.md`. |
| Verifier verdict on file | **yes** — `…/2026-11-03-bahrain-bqa-five-cycles-verification.md`, **re-opened on the corrected paragraphs only** by today's disposition 2: figure axes 1 and 3 over the two struck sentences and their replacement. One row, next run. |
| Arabic gate | **not reached.** The Arabic composition was begun today and stopped by its own first step; nothing is composed, so there is nothing for the Arabic Editor to gate. |
| Hero still / og card | **not on disk.** Owed. |
| `edition:` field | **blocked**, founder issue **#13**, stated default 2026-11-08 — two days out and not yet arrived. |
| Registers with no archival snapshot | **2 of 5, both first-party PDFs, ACCEPTED** by today's Editor disposition 1, with the two URLs written out below. This row exists because that disposition made it a binding condition of this gate rather than of the draft. |
| `astro build` | **exit 0**, 39 of 42 gating assertions green. |
| Held-slug leak | **VACUOUS** (08-09 inversion) — nothing is held in `web/src/content/**`, so the held-mode sweep is a green light wired to nothing and is reported as such, not as a pass. Inverse assertion holds: `approved: false` in the build path = 0. |
| Served bytes changed by this run | **none.** A tool, a register, a `postbuild` entry, a draft, four logs and a brief. `qa_lastmod` unmoved at `2026-11-03T12:30:46Z`. |

**The two accepted single-copy registers, written out as disposition 1 requires:**

* `https://www.bqa.gov.bh/wp-content/uploads/2026/06/Annual-report-2025-.pdf` — carries *"22 government
  schools and 7 private schools received Gold Seals for outstanding performance"* and two figures.
* `https://www.bqa.gov.bh/wp-content/uploads/2025/09/Performance-Report-24-25-EN.pdf` — carries the
  batch of 76 government schools and the 26% at the top grade.

Both answer 200, both are the Authority's own, neither holds a snapshot anywhere, and this operation may
not ask for one under the default it applied on 2026-11-04 (founder issue **#12**, re-asked with a new
default of 2026-11-11). **An accepted risk that is not written down is an unrecorded one**, which is why
it is a row here and not a sentence in a verdict.

**Carried payload of this run's push:** no served change. The deploy this push dispatches republishes
the same 134 pages from a tree whose only content-collection difference from `c17b59c` is none at all.

---

**Signed** · Manager · 2026-11-05
