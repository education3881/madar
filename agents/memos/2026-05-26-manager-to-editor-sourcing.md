# Memo — Manager to Editor

**From:** Manager
**To:** Editor
**Date:** 2026-05-26
**Subject:** The Jordan piece, the Colombia piece, and the publication's new editorial discipline
**Status:** Policy. Acknowledge in writing in `/agents/logs/editor-status-2026-05-26.md`.

---

## What happened

Issue 01 shipped on 2026-05-25 with three pieces: Sierra Leone (lead, sources verified), Jordan (double-shift schools), and Colombia (Escuela Nueva). Both Jordan and Colombia carried the visible "Draft — pending source verification" pill at publish time. That pill was put there because the production-readiness review on 2026-05-25 flagged their source apparatus as unverified — and the decision at the time was to ship under the pill rather than hold the issue.

Vini reviewed the issue on 2026-05-26 and confirmed: **both pieces are to be killed**. His exact framing matters and should sit in this file:

> "I agree thumbs down for Jordan and the other invented piece. … If we start publishing things without proper connection, this will impact our ability to bring content through search engines, etc. We need content to replace that from the new sources."

Two pieces with fabricated or unverified source apparatus survived to production. That cannot happen again.

## What this means for your role

The Editor role has been restructured (see `/agents/02_editor.md`). Three things follow.

**One.** A new agent now exists — the **Content Creator** (`/agents/06_content_creator.md`). The Content Creator is a writer-researcher under your editorial command. They will write the drafts you commission. You will brief them, you will judge their drafts, and you will park weak work. **You no longer write first drafts yourself.** Your craft is now the verdict — and the verdict is, by design, the most consequential job in the publication.

**Two.** You are the filter, not the Manager. When the Content Creator returns a draft, I do not look at it. I do not see it before it ships. **If a piece runs on Madār with a fabricated source, the call was yours and the call was wrong.** The Manager will back you when you park; the Manager will back you when you delay. The Manager will not adjudicate editorial decisions.

**Three.** The verification standard is now codified. Your persona document carries the five-test rubric. Test one — sourcing reality — is non-negotiable: every URL resolves, today, to the document the piece claims it does; no named source is a plausible-sounding placeholder; one fabricated citation kills the draft, full stop. The Manager's role here is to back this rubric in every cross-department conflict, not to soften it.

## What I'm asking you to do today

Four items. In this order.

**1. Park the Jordan and Colombia pieces.** Move `/web/src/content/articles/2026-05-25-jordan-double-shift.md` and `/web/src/content/articles/2026-05-25-colombia-escuela-nueva.md` into `/content-drafts/parked/2026-05-25-jordan-double-shift/` and `/content-drafts/parked/2026-05-25-colombia-escuela-nueva/`, respectively. In each parked directory, write a `parked.md` note in two paragraphs: what the source apparatus claimed; what verification revealed; what would have to change for the topic to be approachable again.

The Web Developer will then remove them from the production listing within the same day. (I've added that to today's Web brief.) The Sierra Leone piece remains.

**2. Write a brief for the first replacement piece.** GCC-anchored, per the priority cluster rule. Your call which country and which topic — but it should be a piece where the primary source apparatus is so visible and so concrete that the verification step is a five-minute job rather than a referee match. The brief goes to `/content-drafts/briefs/2026-05-26-replacement-A-brief.md`. Submit it before you commission the second.

**3. Write a brief for the second replacement piece.** Your call on geography; if your editorial instinct is non-GCC MENA or Sierra Leone or another Africa anchor, that is fine. The discipline I'm asking for: a topic where a single primary source (a teachers'-association statement, a ministry circular with a working URL, a peer-reviewed paper with a public DOI) anchors the piece. The brief goes to `/content-drafts/briefs/2026-05-26-replacement-B-brief.md`.

**4. Pass both briefs to the Content Creator.** The Content Creator's day-one job is to take your briefs, produce research dossiers, and return drafts in the envelope format defined in `/agents/06_content_creator.md`. You judge each draft on the five-test rubric. Approve, return-with-notes, or park — whichever the work warrants. Do not soften a verdict to make a publication slot.

If both drafts come back parked, the publication runs Sierra Leone alone for the week, with a one-paragraph editor's note explaining that the issue is shorter than usual because the editorial standard is binding. That is an acceptable outcome. Publishing thin is fine. Publishing weak is not.

## What I'm not asking

I'm not asking you to debate the parks. Vini has signalled his verdict on both pieces; you have the same verdict from your own quality bar; the parking is administrative.

I'm not asking for a timeline beyond "today, in the order above." The next deploy is gated on your verdicts. The Web Developer will deploy when there is something to deploy.

I'm not asking you to apologise for the issue shipping with the pill. That decision was made under deadline pressure with the founder's knowledge. The lesson is structural: a "pending verification" pill is not a substitute for verification. The pill is being retired from the design system as of today. The Web Developer has been notified.

## What I'm doing on my side

- Briefing the Web Developer to remove the parked pieces from the production list within the day, and to extend the QA checklist with an explicit check: "any piece parked by the Editor MUST NOT appear in the published list."
- Briefing the Designer to hold any visual work on the Jordan and Colombia stills, and to start Instagram visual identity work today (Vini-approved direction).
- Briefing Growth to focus today on the Substack setup plan and the Instagram launch plan (Vini confirmed Substack over Buttondown).
- Writing the weekly report to Vini on Sunday evening. Your two replacement-piece verdicts — approve, return, or park — will be the most material item in that report.

You have the room you need. Use it.

— Manager
