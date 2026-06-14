# Designer proposal — the per-issue visual language, and the transition ritual

**From:** Designer → Manager (for the founder discussion 2026-06-13)
**Date:** 2026-06-12
**Companion artefact:** `/design-assets/issues-page/2026-06-12-issues-page-prototype.html`

## 1. The accident we are adopting

The founder noticed it before we did: the May stills stand on **sand** (`#E8E2D0`), the June stills on **paper** (`#FAFAF7`). It was drift, not decision. But it is *good* drift — it reads as eras, the way a magazine's bound volumes read on a shelf. This proposal adopts the accident retroactively and makes it grammar:

> **Issue 01 — the sand era.** The founding survey; warm ground, object-on-table.
> **Issue 02 — the paper era.** The instrument in use; pieces drawn on the page itself.

## 2. The grammar: identity by deployment, not by palette

The system's five-token rule stands — it is the moat that keeps us looking like one publication across decades, and I will not propose a sixth hex casually. Within five tokens, each issue gets a distinct identity from four dials:

| Dial | What varies | Issue 01 | Issue 02 |
|---|---|---|---|
| **Ground** | The still/card backing neutral | sand `#E8E2D0` | paper `#FAFAF7` |
| **Motif** | One geometric gesture, used on the issue divider and the issue's grid tiles | the horizon line (a single rule, field-survey register) | the thread (two nodes, one connecting line — matching, bridging, diglossia) |
| **Numeral state** | The issue number's color carries time | closed issues: **ink** on their ground | the current issue: **orange** — the survey marker, "the eye lands here" |
| **Density** | Sage-to-orange ratio in the issue's data graphics | sage-dominant, orange scarce | same rule; the ratio is a constant, the *application* differs per motif |

The numeral rule is the heart of it: **orange always means now.** It is the same semantics the system already assigns to orange on diagrams — "what changed, what crossed a threshold." Applied to issues: the current issue is the threshold.

## 3. The transition ritual (what happens when an issue closes)

The founder asked how we *transition*. Proposal — when the Editor declares an issue closed:

1. Its numeral flips **orange → ink**. (One token change; the page itself shows time.)
2. Its block on the Issues page flips ground **paper → its era ground** (Issue 02's blocks will flip to whatever ground Issue 03 vacates — see the ladder, §4).
3. Its motif is retired from new assets and archived in SYSTEM.md — motifs are never reused.
4. The new issue opens with: a declared theme line (Editor), a chosen ground (Designer, from the ladder), a new motif (Designer), and an issue line in the registry (Web Developer).

Four steps, three owners, one push. The ritual is small enough to never be skipped.

## 4. Phase 2, for discussion — the ground ladder (the only place I'd touch color)

If the founder wants *more* color differentiation per issue than sand/paper alternation gives, the honest mechanism is a **pre-approved ladder of grounds** — neutrals only, chosen now, contrast-verified now, deployed one per issue in order. Candidates (all warm-neutral, all AA-compatible as grounds under ink):

| Ladder | Hex | Character |
|---|---|---|
| sand (in system) | `#E8E2D0` | the founding warmth |
| paper (in system) | `#FAFAF7` | the instrument itself |
| stone *(new)* | `#DDD9CE` | cooler, archival |
| clay *(new)* | `#E5D5C5` | warmer, terracotta-adjacent |

Stone and clay would be **ground-role only** (the same forbidden-uses line as sand: never page background, never behind body type). This is a SYSTEM.md amendment — it needs the weekly's ratification, and I am genuinely ambivalent: the five-token rule has been the system's spine for 18 days and its restraint is why the publication already looks older than it is. My recommendation: **Phase 1 now, ladder only when Issue 04 exists** — alternation covers three issues honestly.

## 5. What this is NOT

- Not a redesign. Body pages don't change at all; the article reading experience is untouched.
- Not a new color per issue chosen by mood. Every ground is pre-approved or already in the system.
- Not automatic. The Editor closes issues; the Designer assigns grounds and motifs; the page renders declarations.

— Designer · 2026-06-12
