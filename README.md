# Madār · مدار

**→ Read it: [education3881.github.io/madar](https://education3881.github.io/madar/)**
· [العربية](https://education3881.github.io/madar/ar/)
· [Editions](https://education3881.github.io/madar/editions/)
· [About](https://education3881.github.io/madar/about/)
· [RSS (EN)](https://education3881.github.io/madar/rss.xml)
· [RSS (AR)](https://education3881.github.io/madar/ar/rss.xml)

*Education, written slowly, in two languages · التعليم، بتأنٍّ، بلغتين*

A fully automated, agent-operated editorial publication on early childhood and K–12 education,
sourced from underrepresented geographies and presented with artistic seriousness. Every piece is
published in **English and Arabic** — Arabic is composed, not translated — and stands on **named
primary sources** read as served text.

This is Vini's personal project — independent of any institutional affiliation. It is, by design, a
geo-political manifesto: who we cover, what we cover, and the care with which we cover them is the
point.

*Made in spite of, not because of.*

---

## What is published

**38 pieces in English, 38 in Arabic — 100% parity — across 35 countries**, in four monthly
editions:

| Edition | Month | Theme |
|---|---|---|
| **04** *(current)* | August 2026 | **The measurement question** — what a score actually measures, and who defines, moves and defends the thresholds that turn a child's work into a label |
| 03 | July 2026 | Continuity — does the certificate still get issued? |
| 02 | June 2026 | — |
| 01 | May 2026 | — |

Two kinds of piece: **field notes** we report ourselves, and **curated readings** of one carefully
chosen source worth listening to. Two to three pieces an issue. One issue a month. A research
instrument, not a magazine.

Also here: **[VALENCE — the Chemistry of Education](https://education3881.github.io/madar/valence/)**,
a standalone interactive instrument.

## How it is made

The publication is run day to day by a team of **eleven Claude personas**, each defined in
[`/agents/`](./agents/). The Manager runs the operation as its CEO; the founder's only standing
action is the `git push`.

```
Founder ──► Manager/CEO ──┬── Editor (the filter — every piece clears the rubric in writing)
                          │      └── Researcher · Content Creator · Content Creator II · Verifier
                          ├── Arabic Editor ── Arabic Content Creator
                          ├── Web Developer
                          ├── Designer
                          └── Growth
```

The operating mandate is [`/agents/CHARTER.md`](./agents/CHARTER.md); the routing diagram in
[`/agents/RUNBOOK.md`](./agents/RUNBOOK.md) is canonical. Five standing functions run every day —
content, quality, growth, research-to-learn, and a daily brief — on a scheduled cadence, without
being prompted.

**Two things make the output verifiable rather than merely produced.** The
[guidebook](./agents/guidebook/) is a numbered register of **34 standing rulings** on sourcing and
figure discipline, each opened by a real defect and each binding on every draft that follows it —
*a total is a figure and must be added*; *a ranking is not a measurement*; *a parity check counts
files, not language*. And every run logs a written [QA and publish gate](./agents/logs/) before
anything is staged.

## Repository layout

| Folder | Purpose |
|---|---|
| [`/agents/`](./agents/) | The eleven personas, plus the [charter](./agents/CHARTER.md), [runbook](./agents/RUNBOOK.md), [daily briefs](./agents/briefs/), [guidebook](./agents/guidebook/), [QA logs](./agents/logs/), [weekly reviews](./agents/reviews/), [growth audits](./agents/growth/), [stats](./agents/stats/) and [tools](./agents/tools/) |
| [`/docs/`](./docs/) | Canonical project rules: geographic scope, topics, quality bar, voice |
| [`/web/`](./web/) | The Astro site source — what gets built and deployed |
| `/content-drafts/` | Recon briefs, dossiers, drafts and Editor's verdicts, before anything reaches `/web/src/content/` |
| `/social-drafts/` | Growth's captions and newsletter drafts |
| `/design-assets/` | Mood boards, hero visuals, design specs |

## Build and deploy

```bash
cd web
npm ci
npm run build     # 81 routes + a sitemap; /valence/ is served from public/
```

Deployment is automatic: **GitHub Actions on push to `main`** → GitHub Pages
([`.github/workflows/astro-pages.yml`](./.github/workflows/astro-pages.yml)). The workflow checks
out full history because the sitemap's `lastmod` is derived from git.

**Standing quality assertions**, run against the built output before any push:

```bash
python3 agents/tools/qa_ar_language.py       web/dist   # no Latin-script vocabulary in Arabic chrome
python3 agents/tools/qa_consumer_surface.py  web/dist   # og:locale/type/site_name, raster cards, sitemap lastmod, print CSS
python3 agents/tools/madar_stats.py --log               # corpus counts, parity, countries, cadence
```

## Status

- [x] Brand name chosen — **Madār · مدار**
- [x] Visual direction — bilingual wordmark, hand-drawn *Stills*, one kiln-orange mark per piece
- [x] Astro site builds and deploys (GitHub Actions → Pages)
- [x] Four editions live, EN/AR at full parity
- [x] Bilingual RSS, structured data, raster share cards
- [ ] Custom domain
- [ ] First newsletter issue sent

---

*No third-party trackers, by design.*
