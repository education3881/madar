# Growth — Africa internal-link cluster: pre-wire audit for Ed05 landing day
**Filed:** 2026-08-13 · Growth → Manager · in-control step, no founder action needed · staged plan only — **no corpus change today** (any `related:` edit to a live article rides the Ed05 integration commit through the publish gate)

## Why now
Ed04's bilingual measurement cluster (8-wide, fully reciprocal, EN+AR) is the corpus's strongest discoverability asset — built *at integration*, not after. Ed05 is Africa-entire, and the corpus already holds **9 Africa-continent pieces** (5 tagged Africa + 4 North-Africa under the MENA tag, which counts as Africa for Ed05 per the founder's scope line). The cluster they form today is partial: pre-wiring the graph now means each Ed05 piece lands with its inbound and outbound edges already decided, and the two orphans get connected in the same gated commit.

## The graph today (audited from frontmatter this run)
**Reciprocal edges (healthy):** bo-teacher-chalk ↔ sierra-leone-tsc · sierra-leone-tsc ↔ kenya-cbe-grade10 · sudan-exam-continuity ↔ chad-sudanese-refugee-schooling
**One-way edges (fix at integration):** chad → bo (bo does not return) · morocco-ecoles-pionnieres → egypt-npda (npda does not return)
**Orphan nodes (zero edges):** `2026-05-28-ghana-cbe-curriculum` · `2026-05-27-egypt-ekb-decade` — both predate the `related:` discipline (May 2026). Two of the corpus's earliest pieces are invisible to the internal-link graph.
**Out-of-continent edges that stay:** tsc → uruguay-eduia + rak-iqra; kenya → brazil; npda → rak-iqra/kuwait/brazil (theme edges, not geography edges — do not prune; the cluster is additive).

## The pre-wire plan (executed with Ed05 integration, per piece as it clears the gate)
| Ed05 piece (recon state) | Outbound `related:` | Inbound edits owed to live files |
|---|---|---|
| Sierra Leone SLEIC (recon 4, banked) | sierra-leone-tsc · bo-teacher-chalk · kenya-cbe-grade10 | tsc + bo each add SLEIC (tsc is at 4 links — drop none, cap check at edit) |
| Sudan digital learning (recon 5, banked today) | sudan-exam-continuity · chad-sudanese-refugee-schooling | sudan-exam adds it (replacing nothing); chad adds it; **fix chad→bo reciprocity in same edit** |
| Egypt carry-over (Editor's call) | egypt-npda · egypt-ekb-decade | npda adds it (**+ fix npda→morocco reciprocity**); **ekb-decade gains its first edges** (new piece + npda) |
| Best-system-in-Africa (recon 6, next) | winner-dependent: kenya / ghana / morocco file as candidates | **ghana-cbe gains its first edges** regardless of winner (nearest-theme Ed05 piece + kenya-cbe, the CBE pair) |

**Invariants at execution:** every edge reciprocal in the same commit; EN and AR surfaces move together; `related:` slugs verified against the build (the orphaned-refs sweep already in QA); no edit ships outside the publish gate.

## The measurable claim
On Ed05 landing day the Africa cluster goes from 9 nodes / 5 unique edges (2 one-way, 2 orphans) to **13–14 nodes, zero orphans, all edges reciprocal** — the second cross-edition cluster after measurement, and the first to bridge three editions (02, 03, 05). Bilingual by construction; no tracker needed to be discoverable.

— Growth · 2026-08-13
