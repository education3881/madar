# Educational Website (working title)

A fully automated, agent-operated editorial publication on education, sourced from underrepresented geographies and presented with artistic seriousness.

This is Vini's personal project — independent of any institutional affiliation. It is, by design, a geo-political manifesto: who we cover, what we cover, and the care with which we cover them is the point.

## Architecture at a glance

```
You (Founder)
    │
    └── Manager  ◄──── single point of contact for the founder
            │
            ├── Editor          (content quality)
            ├── Web Developer   (the site itself)
            ├── Growth          (sustainable reach + community)
            └── Designer        (visual identity + hero visuals)
```

Each agent is a Claude persona defined in [`/agents/`](./agents/). The Manager invokes specialists by reading their persona file at the start of the relevant work. Cross-cutting rules live in [`/docs/`](./docs/) so the same rules don't get duplicated five times.

## Repository layout

| Folder | Purpose |
|---|---|
| [`/agents/`](./agents/) | The five AI agent personas (Manager, Editor, Web Developer, Growth, Designer) |
| [`/docs/`](./docs/) | Canonical project rules: charter, geographic scope, topics, quality bar, voice |
| [`/web/`](./web/) | The Astro site source — what gets built and deployed |
| `/content-drafts/` | Where the Editor drops drafts for Vini's QA before they go live in `/web/src/content/` |
| `/social-drafts/` | Where Growth drops Instagram captions and newsletter drafts for Vini to send |
| `/design-assets/` | Where Designer drops mood boards, hero visuals, and design specs |

## How to interact with the system

You (Vini) talk to the **Manager**. In Cowork mode that means starting a conversation like:

> "Manager: time for this week's editorial planning. What's queued?"

or

> "Manager: I want a piece on early-childhood literacy in Sierra Leone. Brief the Editor."

The Manager reads its own persona file, then invokes the relevant specialist agent by reading that agent's persona file before drafting the work. Substantial decisions are always escalated back to you with options and a recommendation.

## Status

- [ ] Brand name chosen
- [ ] Visual direction (mood boards reviewed)
- [ ] Seed content drafted and reviewed
- [ ] Astro site builds locally
- [ ] GitHub Pages deployment live
- [ ] First Instagram + newsletter edition
