# Decision record — the Editions system (founder decisions, 2026-06-14)

**From:** Manager (recording the founder's live decisions) → Designer + Web Developer + Editor + Arabic Editor
**Context:** Vini reviewed the 2026-06-12 Issues-page proposal and decided the four open questions directly. Build authorised **now**, ahead of the domain move. This record supersedes the relevant defaults in `2026-06-12-issue-transition-coordination.md` and the Designer's Phase-1 recommendation.

## The four decisions

1. **Naming → "Editions" / «الإصدارات».** Not "Issues". Routes: `/editions/` + `/ar/editions/`. Nav: "Editions · الإصدارات".
2. **Per-edition identity → each edition gets a genuinely distinct look and feel.** Overrides the Designer's Phase-1 "sand/paper alternation only" recommendation.
3. **Palette → expanded, but cohesive.** Vini: *"each edition would have a unique look and feel, not necessarily using orange for current. you can include more colors in the palette given that it is the same style."* So: (a) the five-token restraint is relaxed by founder decision — more colours are permitted; (b) the binding constraint is now **"same style"** — cohesion, not a fixed count. The "orange = current" semantic is **dropped**; the current edition is marked by a "Current" tag and position, not colour.
4. **Sequencing → build before the domain move.** Overrides the "after-cutover" rule. Accepted cost: these URLs get re-crawled once at cutover; inbound ≈ 0 today, so the cost is near its lifetime minimum (consistent with the domain memo's own logic).

## The cohesion discipline (how "more colours, same style" stays one publication)

The system that keeps distinct editions reading as siblings rather than different sites:

- **Fixed frame, never varied:** the wordmark, the four typefaces, ink `#0E1B2C` for all body text, the reading-page background, the layout grammar, the macron rule motif. Body/article pages do **not** change per edition.
- **Per-edition variables, drawn from a curated ladder:** a **ground** (the era backing) and an **accent** (the edition's signature, used only for kickers, rules, the edition numeral, and hovers — never body text). Each accent is chosen at the same muted, warm-editorial saturation as the house orange, so they read as one family.

| Edition | Period | Ground | Accent | Motif | Status |
|---|---|---|---|---|---|
| 01 | May 2026 | sand `#E8E2D0` | terracotta `#D94F2A` (house) | horizon (single rule) | closed |
| 02 | June 2026 | paper `#FAFAF7` | pine `#2F6F6A` | thread (two nodes, one line) | **current** |
| 03 *(reserve)* | — | stone `#DDD9CE` | amber-clay `#B0682E` | — | — |
| 04 *(reserve)* | — | clay `#E5D5C5` | slate `#46618C` | — | — |

Editions 03–04 are pre-approved reserve so future opens are a one-line registry add, not a fresh palette debate. All grounds are ground-role only (never page background, never behind body type); all accents verified legible at kicker/numeral sizes.

## Build scope (this push)

In scope: `edition` schema field + backfill (Ed 1 = pre-June, Ed 2 = June); `editions.ts` registry; `/editions/` + `/ar/editions/` themed pages; nav link; sitemap +2 URLs; cold-build verification.

**Deliberately deferred + flagged to Vini:** the homepage still frames everything as "Issue 01". Fixing that label correctly is coupled to an editorial decision — should the homepage show **only the current edition** (magazine model; previous editions live on the Editions page) or **stay a full catalogue**? Not made unilaterally in a build. Teed up for Vini.

**Sign-offs still required before live:** Editor on EN labels/theme lines; **Arabic Editor on all AR strings** (الإصدارات, period and theme lines, "Current"/«الحالي», "Previous editions"/«الإصدارات السابقة») — drafted now, marked pending verification.

— Manager · 2026-06-14
