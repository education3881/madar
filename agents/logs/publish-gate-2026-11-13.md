# Publish gate — 2026-11-13

**Subject: a REPAIR to four served annotations on three already-published pieces. No flag moves, no piece
ships, no asset is added.** The gate is run in writing anyway, because the bytes are editorial and served,
and the skill's rule is about the bytes rather than about the flag.

| Gate | State |
|---|---|
| Pieces touched | `2026-07-07-india-parakh-hpc` (EN + **AR**), `2026-07-16-australia-naplan-reset` (EN), `2026-07-07-poland-ukrainian-students` (EN) |
| What changed | the **first `sources[]` annotation** of each file, which now carries the institution's full name as its own register prints it (#101 clause 1, first branch), with the read and its date |
| What did NOT change | **no body**, no `title`, no `dek`, no `related:`, no `approved:` flag, no hero still, no og card, no cited URL |
| Editor verdict on file | the three pieces were approved under their own verdicts in July 2026 and are unchanged in substance; this is a **#101 correction to a named institution written in the register's own words** (clause 4), which the standing prohibitions bind every piece to |
| Arabic Editor | the AR repair is a **composition** decision and not a copy — the Arabic annotation carries the Arabic expansion the Arabic body already composed, and the Latin token in parentheses, because Arabic cannot carry the Latin acronym as a name (#101's structural point) |
| Verifier | the four annotations were read against their pieces' own frontmatter before and after; evidence confirmed present for all 6 / 4 / 3 / 4 name-words respectively |
| `dek` / `title` caps | untouched, therefore not re-measured — and said so rather than ticked |
| `npm run build` | **exit 0**; 27 `postbuild` assertions green; all 12 build-job gates green via `build_job_gates` |
| `qa_acronym_evidence` | **14 of 14** anchored expansions evidenced in their own annotations — CLEAN |
| `qa_annotation_figures` | failed once on the Arabic read-date `١٣`, cleared by a hand-written register row with real provenance (#114 clause 2); **OK** |
| `qa_pair_frontmatter` | CLEAN — the pair still agrees about every fact that belongs to the piece rather than to a language |
| `qa_claim_registers` / `qa_citation_identity` | CLEAN and **unmoved** — 361 registers and 241 quotation-bearing registers, the same numbers as before the repair, which is the evidence that no new register was cited and no new quotation claimed |
| Held-slug leak | zero; nothing is held in the corpus and the in-flight piece has no draft on disk |

**Signed off by the Manager** on the four gates that apply (Editor's standing prohibitions, Arabic
composition, build, assertions). The two that do not apply — a Verifier wave verdict and an asset check —
are named as not applying rather than marked green.
