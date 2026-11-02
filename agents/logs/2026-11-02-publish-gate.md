# Publish gate — 2026-11-02

**Nothing was published today and no flag moved.** This file exists because the day changed **served
bytes** on six already-approved pieces, and a change to the publication is gated in writing whether or not
it is a new piece.

## What moved in `web/src/content/**`

**Six files, frontmatter only — one `related:` entry added to each.** Three pairs, EN + AR:

| Piece | Forward rail added |
|---|---|
| `2026-06-20-oman-school-performance-ratings` | `2026-07-28-england-report-cards-first-term` |
| `2026-06-17-korea-aidt-reversal` | `2026-06-19-philippines-mtb-mle-reversal` |
| `2026-06-08-sierra-leone-tsc-teacher-matching` | `2026-09-27-rwanda-teacher-certification` |

No body text, no `title`, no `dek`, no figure, no citation and no flag was touched. Each addition is the
reverse of an edge the Editor had already curated in the other direction, between pieces about the same
instrument — the reasoning and the 31 edges deliberately **not** touched are in
`agents/growth/2026-11-02-the-related-rail-only-points-backwards-in-time.md`.

## The gate, row by row

| Gate | State |
|---|---|
| `npm run build` clean | **exit 0**, 134 pages |
| All gating assertions green | **38 of 41**, derived by `qa_patch_queue` from three homes — 26 `postbuild` + 12 build-job via `build_job_gates.py` |
| `qa_body_links` — every rail slug resolves | **PASS** |
| `qa_pair_frontmatter` — EN/AR parity | **44 pairs, 44 approved, 0 held**; rails identical piece for piece in both editions |
| Held-slug leak | **zero, and vacuously so** — there are no held pieces, so the 2026-08-09 inversion applies: the live assertion is `approved:false` count in the build path = 0, and it is 0 |
| `lastmod` consequence | the six pieces' `<lastmod>` moves, **correctly** — a rail is served markup, so a reader-visible byte did change on each of them, which is the 2026-09-06 rule satisfied rather than evaded |
| Editor verdict on file for anything flipped | **n/a — nothing flipped** |
| Hero still / og card for anything flipped | **n/a** |
| Credentials, tokens, keys | **none, ever** |

## The Bahrain piece — approved, and explicitly NOT gated

`2026-10-23-bahrain-bqa-five-cycles` received the **Editor's five-test verdict today: APPROVE** on all five
tests (`content-drafts/verdicts/2026-11-02-bahrain-bqa-five-cycles.md`). **It did not approach this gate
and must not, and the reasons are recorded so no later run mistakes an approval for a clearance:**

1. **`approved: false` stands.** It contributes no page, no sitemap entry, no feed item, no `lastmod` and
   no bytes.
2. **Arabic composition has not started**, so there is no pair; the Arabic Editor's gate has not run, and
   it carries a live **park condition** (the four populations must be holdable apart in Arabic).
3. **No Verifier verdict.** Scheduled the run after the pair verdict, per the 2026-09-06 rule.
4. **No hero still and no og card.**
5. **The edition field is HELD**, not guessed — there is no Edition 06, the registry exports
   `hasOpenEdition: false`, and the question is founder **issue #13**, default **2026-11-08**.

The verdict is the frame. The flag is five things away and one of them is not ours.

## Signed

Manager · 2026-11-02 · build exit 0, 38 of 41 gating assertions green, nothing published, one editorial
approval recorded and correctly unshipped.
