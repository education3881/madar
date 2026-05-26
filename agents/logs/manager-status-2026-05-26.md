# Manager status — 2026-05-26 (end of day)

**From:** Manager
**To:** Vini
**Subject:** Day one off-ops — what shipped, what was killed, what's queued

---

## What shipped today (in source; awaiting push)

The publication has a clean local build with two pieces, one bilingual frame, no broken references. Every change below is in the working tree at `/Users/vini/Documents/Claude/Projects/Educational Website` and built clean against Astro 5.18.1. They are not yet on the live site. **Push is the only blocker; the sandbox does not have terminal access to GitHub.**

1. **Home-page wordmark fixed (P0).** The SVG is now inlined at build time and inherits the theme ink. A typographic fallback renders even if the SVG is missing. Both the EN home (`web/src/pages/index.astro`) and the AR home (`web/src/pages/ar/index.astro`) are fixed. The proximate cause — wordmark loaded via `<img src>`, `currentColor` not inheriting, no fallback — has been codified as a new permanent rule in the Web Developer persona ("never ship without inlining").
2. **Jordan and Colombia pieces parked.** Both moved out of `/web/src/content/articles/` into `/content-drafts/parked/2026-05-25-jordan-double-shift/` and `/content-drafts/parked/2026-05-25-colombia-escuela-nueva/`, each with a `parked.md` explaining the verification failure and what would have to change for the topic to be reopened. Hero stills moved with them.
3. **Arabic home page cleaned.** Was hardcoded to reference the Jordan piece and surface Arabic excerpts from it; both have been removed. No production page references the parked pieces.
4. **Bahrain piece written, judged, approved, and moved to production.** The piece — *"Bahrain grades its schools, by name, in public"* — is a curated commentary on the BQA's 2024–2025 Performance Report. Five public-source citations, all verified today by the Editor; one named human (Dr. Maryam Hasan Mustafa, BQA Chief Executive) with biography verified via her INQAAHE bio. The piece replaces the Jordan slot in Issue 01.
5. **EKB piece briefed.** The Editor's brief for the Egyptian Knowledge Bank piece — replacing the Colombia slot — is at `/content-drafts/briefs/2026-05-26-replacement-B-brief.md`. Draft is due from the Content Creator by 2026-05-28.

## What was killed

- The Jordan double-shift piece. Park reason in `/content-drafts/parked/2026-05-25-jordan-double-shift/parked.md`. The topic is not closed; the specific draft is.
- The Colombia Escuela Nueva piece. Park reason in `/content-drafts/parked/2026-05-25-colombia-escuela-nueva/parked.md`. Same disposition.
- The "Draft — pending source verification" pill, as a design pattern. A piece is approved or it is parked; the in-between state is gone. The pill's existence on the live site was the wrong remedy for what was, on review, a sourcing failure. The Web Developer's QA checklist now treats parked-but-visible as a P0.

## What's structurally new

The agent architecture moved from five to six and the routing changed. This is the largest organisational change since the publication started.

- **A Content Creator agent now exists** (`/agents/06_content_creator.md`). Brilliant, bold, source-disciplined; writes the drafts. The Editor briefs them, judges them, parks them. The Manager does not interact with the Content Creator directly.
- **The Editor's role is now judgment, not production.** The five-test verdict rubric is codified in `/agents/02_editor.md`. The Editor is the filter; a piece that runs on Madār with a fabricated source is the Editor's call and the Editor's call alone.
- **The Manager runs the company, not the editorial side.** I do not approve content. I do not look over the Editor's verdicts. I set department goals, share cross-department signals, run the weekly report to you. The Editor's parks are backed without exception.
- **The Web Developer has a mandatory QA mandate.** Between feature work, the default activity is running the QA checklist against the live site, every day, and within 30 minutes of every deploy. The checklist is codified in `/agents/03_web_developer.md`; the first run is in `/agents/logs/qa-2026-05-26.md`.
- **The agents `README.md` has been rewritten to reflect the new structure.**

## Today's other deliverables (in source)

- **Manager → Editor sourcing memo** at `/agents/memos/2026-05-26-manager-to-editor-sourcing.md`. The conversation you asked for. Long-form. Sets the policy.
- **Designer brief** at `/social-drafts/2026-05-26-designer-instagram-and-issue01.md`. Instagram visual identity (handle, profile photo, grid, story templates) plus the Bahrain hero still to make today. The Designer is told, explicitly, not to spend craft on Jordan or Colombia.
- **Growth brief** at `/social-drafts/2026-05-26-growth-substack-and-instagram.md`. Substack setup (your morning confirmation noted; we are on Substack, not Buttondown), Instagram launch plan, first nine grid posts, posting cadence, what we are explicitly not doing.
- **QA report** at `/agents/logs/qa-2026-05-26.md`. Two P0 fixed in-session; one P1 (`/rss.xml` referenced in footer but not built) scheduled for tomorrow; three P2s on a small backlog. The full QA checklist will run daily, by the Web Developer, going forward.

## What I need from you, in order of priority

There is one item, and it is the only thing that blocks tomorrow.

**Push the working tree to `main` when you next sit at your terminal.** From the project root:

```bash
cd "/Users/vini/Documents/Claude/Projects/Educational Website"
git add -A
git status   # sanity-check the file list before committing
git commit -m "Madār — 2026-05-26: park Jordan + Colombia, ship Bahrain, fix wordmark, new agent architecture"
git push
```

The push will trigger the Pages build via the gh-pages workflow you already have set up. Within a minute or two, the live site will show the Bahrain piece in the secondary slot, the Jordan and Colombia pieces gone, and the wordmark rendering in the theme ink. The Web Developer will run the post-deploy QA pass automatically.

That's it from my side. Nothing else needs your decision today. The publication is running.

## A small note on tone

You said this morning: *"Make me proud. Remember: quality."* The discipline today has been quality at every checkpoint — the Bahrain piece is real reporting against a real document, every cited URL was opened on verdict day, every named human was cross-verified, the parked pieces are documented with the verification failure described in writing. The Editor's five-test rubric is binding, and it bound today. We held two slots empty rather than soften it.

We will sometimes ship a thin issue rather than a weak one. I think that is the right trade.

— Manager
