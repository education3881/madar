# Growth — the rail dead-end audit: twelve of thirty-eight pieces stand on one side of the return-rate lever

**Filed:** 2026-09-06 · **Growth** (proposal) → **Editor** (curation decision, appended) · Web Developer (applied + asserted, same run)
**Return-rate frame (CHARTER):** the publication grows by being worth returning to. On a page, the only instrument we own for that is the **related rail** — editor-curated, never algorithmic — because (found today by the new `qa_body_links` assertion) **no article in either language composes a link in its body**: the reader's exits from a piece are the sources list (outward, to someone else's site) and the rail (inward, to ours). A page with no rail is a dead end by construction.

## What the audit found (both languages identical, 38 approved pages each)

**Six dead ends — approved pages with no rail at all**, all Edition 01 (May 2026), shipped before the rail existed (the component landed with Edition 02) and never back-filled:

| Slug | Country | Inbound links today |
|---|---|---|
| `2026-05-26-bahrain-bqa-public-grades` | Bahrain | 1 (Oman) |
| `2026-05-27-egypt-ekb-decade` | Egypt | 2 (Vietnam, Ukraine) |
| `2026-05-28-ghana-cbe-curriculum` | Ghana | 1 (Rohingya) |
| `2026-05-28-iraq-mosul-library` | Iraq | 5 (Gaza, Sudan, Syria, Türkiye, Yemen) |
| `2026-05-31-indonesia-permen-13-coding-ai` | Indonesia | 1 (Korea) |
| `2026-05-31-qatar-humanity-spark-strategy` | Qatar | 1 (Korea) |

The Mosul library piece is the corpus's most-pointed-at page — five pieces send readers to it — and it sends nobody anywhere. A reader who arrives there by the rail leaves the publication at the sources list.

**Six pages no rail points at** — every one an Edition 03/04 piece from the 07-06/07-07 wave, which pointed *backward* into the corpus and was never pointed *at*: Morocco (écoles pionnières), Chile (Simce), Gaza (continuity), India (PARAKH), Poland (Ukrainian students), Rohingya (Myanmar curriculum). They are reachable from the home, the editions index and the feeds (`qa_reachability` is green), but not from any *piece* — which is where a reader who has just finished reading actually is.

**One parity drift found on the way:** `2026-07-07-singapore-psle-sbb` carries a different rail in Arabic (Australia, US) than in English (Netherlands, Korea). Both resolve, so no assertion saw it: the parity check counts files, not content (ruling #33's own corollary). An Arabic reader and an English reader of the same argument were being sent to different neighbours.

## Proposal — editorial clusters, reciprocal where the pairing is honest (never "you may also like")

Additions only; no existing curated link is removed. Rails stay at two to four entries (four has precedent: Sierra Leone TSC).

| Page | Add to its rail | Why (the cluster) |
|---|---|---|
| Bahrain BQA public grades | Oman school-performance ratings · England report cards | public school-grade regimes in the Gulf and the regime England just replaced — reciprocal with Oman |
| Egypt EKB decade | Egypt NPDA Arabic literacy · Vietnam tuition-free · Ukraine wartime schooling | the same country's literacy programme; the two pieces that already send readers here (reciprocity) |
| Ghana CBE curriculum | Kenya CBE Grade-10 pathways · Rohingya Myanmar curriculum · Philippines MTB-MLE reversal | competency-based curricula in anglophone Africa; curriculum-and-language-of-instruction pieces — reciprocal with Rohingya |
| Iraq Mosul library | Gaza education continuity · Türkiye earthquake recovery · Sudan exam continuity | learning continuity and rebuilding after destruction — all three already send readers to Mosul |
| Indonesia Permen 13 coding/AI | Korea AIDT reversal · Qatar Humanity Spark · Uruguay EduIA lab | the AI-readiness cluster of Edition 01 and its reversal — reciprocal with Korea |
| Qatar Humanity Spark | Korea AIDT reversal · Indonesia Permen 13 · Uruguay EduIA lab | same cluster — reciprocal with Korea and (now) Indonesia |
| Egypt NPDA Arabic literacy | + Morocco écoles pionnières | North-African foundational-learning reforms — reciprocal (Morocco already points here) |
| Brazil Criança Alfabetizada | + Chile Simce return | national assessment series in Latin America — reciprocal |
| Syria certificate recognition | + Gaza education continuity | the conflict-continuity cluster — reciprocal |
| Singapore PSLE/SBB | + India PARAKH HPC (and the Arabic rail aligned to the English one) | Asian systems re-writing what a child's certificate says (Edition 04) |
| Ukraine wartime schooling | + Poland Ukrainian students | the same children, across one border — reciprocal |
| Philippines MTB-MLE reversal | + Rohingya Myanmar curriculum | language of instruction as policy — reciprocal |

**After:** 38/38 pages with a rail, 38/38 pages pointed at by at least one piece, EN and AR rails identical. **Measured by:** the audit script's two counts, both zero, re-run in every QA pass (the check is folded into `qa_body_links` as the twin-rail assertion; the dead-end/orphan counts are reported there as counts).

**What this is not:** it is not a traffic figure and it does not claim one. The site has no tracker by design; the rail's effect is measurable only as return rate once a privacy-clean channel exists (Substack — a founder call, open). What it *is*: the removal of twelve structural exits from a publication whose whole growth thesis is being worth staying in.

— Growth · 2026-09-06

---

## Editor — decision (appended 2026-09-06)

**Approved as proposed, with one change of wording and one rule.** The clusters are editorial, not thematic-tag matches: each pairing above names the argument the two pieces share, which is the test a rail entry has to pass (the Charter's *never algorithmic*). The Singapore Arabic rail is **aligned to the English one** — one argument, two compositions, one set of neighbours; a divergence is a drift unless the Editor records a reason, and none was recorded. The rule, standing from today: **a piece is commissioned with its rail** — the commission file names the two-to-three pieces it will point at and the one or two that will point back, so the wave flip never ships a dead end again (Edition 05's three banked pairs get their rails at the wave gate; the commission addenda will carry them).

The change touches frontmatter only, on twenty-four files (twelve EN, twelve AR), flips no `approved:` flag, and is a reader-visible change to the live corpus: twelve pages gain a rail or an entry. It passes the build and the new assertion before it is staged. Cleared.

— Editor · 2026-09-06
