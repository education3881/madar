# Growth — Substack setup + Instagram launch plan (2026-05-26)

**From:** Manager → Growth
**Subject:** Today's department goal — concrete setup plans for Substack (newsletter) and Instagram (social). Vini confirmed Substack over Buttondown this morning.

---

## 1. Substack — newsletter setup (confirmed direction)

Vini's morning note: *"I agree with you about substack."* We are on Substack, not Buttondown. The reasoning we built up over the past two days holds: Substack's editorial-publication mode (sections, archive, podcast hooks if we ever want one, native bilingual handling, decent reader app, no per-subscriber fees at this scale) is a better fit than Buttondown's lighter footprint, even at the cost of being a more visible platform. The trade-off — that we are then a "Substack publication" in the public eye — is acceptable for v0.1.

### Setup steps (in order, to be executed by Vini at his terminal when he next has 25 minutes)

1. **Create the Substack publication.**
   - Email: `education3881@gmail.com` (the dedicated project email)
   - Publication name: `Madār · مدار`
   - Subdomain: `madar.substack.com` (preferred). If taken, fall back in order: `madarpublication.substack.com` → `madareditorial.substack.com`.
   - Tagline (Substack calls this "subtitle"): **"Education, written slowly, in two languages."** No Arabic line in the Substack subtitle — Substack's typography handling for the Arabic line in the subtitle field is unreliable, and we'd rather lead with the English line cleanly than ship a broken bilingual line. The Arabic line lives in the publication's About page and in the welcome email, where we control the type.
   - No paid tiers at launch. Free-only. We can introduce paid in 6+ months when we have an honest subscriber count and a sense of what readers value.
   - Category: "Education" (Substack's category, not ours).

2. **Configure sections.** Substack supports up to ~5 sections per publication. Use them as Madār's editorial structure, not Substack's marketing categories. Initial sections:
   - **Field notes** — original reporting / commentary (the publication's longer-form pieces)
   - **Curated** — readings of a single source, like the Bahrain BQA piece
   - **Letter from the editors** — once-an-issue close-the-loop note
   - **عربي** — pieces published in Arabic (initially empty; signals the bilingual posture)

3. **About page.** Reuse the content from `/web/src/pages/about.astro` content — but **strip any country list, any country count, any "we don't cover X" line**. The geography-internal rule applies on Substack identically. Copy is to be drafted by the Editor before we publish the About page; Growth's job is the platform configuration, not the copy.

4. **Welcome email.** Substack lets you set the email that new subscribers receive on day one. The first version is short:
   - **Subject:** A research instrument, not a magazine
   - **Body:** four short paragraphs. (1) Thank for subscribing. (2) What Madār publishes — field notes and curated readings, two to three pieces an issue, one issue a month. (3) The slow-cadence promise — we will not crowd your inbox. (4) The bilingual posture in one sentence. Close: *"— The Editors."*
   - Send to Editor for copy before configuration.

5. **First import.** Once setup is complete and the welcome email is approved, post **Issue 01** as a single Substack post containing both the Sierra Leone piece (lead) and the Bahrain piece (curated), with the publication's website as the canonical URL on each. Add a one-paragraph editor's note at the top explaining that Issue 01 is two pieces rather than three because the editorial bar held back two drafts — the new sourcing discipline made visible. Do not name the parked pieces.

6. **Embed.** Add the Substack subscribe-by-email form to the site footer. The Web Developer will need ~30 minutes for the embed once the Substack URL is live. Growth provides the embed code; the Web Developer reviews for performance impact and ships.

### Substack things we are explicitly NOT doing

- **No imports from existing newsletters.** There is no existing list. We start at zero. Anyone who says otherwise is wrong.
- **No "Substack Notes."** Notes is Substack's Twitter-equivalent feed. The publication does not need a second feed; it has Instagram for the social register. Notes posting can come later, never at launch.
- **No cross-promotion / recommendations engine.** Off at launch. Madār has no business recommending other publications until it has an editorial line stable enough to recommend from.
- **No comments on posts.** Off at launch. A two-pieces-a-month publication does not need to manage a comments thread. The publication's email reply ([the dedicated education3881@gmail.com](mailto:education3881@gmail.com)) is the channel for reader correspondence.

## 2. Instagram — launch plan (confirmed direction)

Vini's morning note included: *"designer and growth … can think about the instagram page."* The Designer is producing the visual identity (handle, profile photo, grid templates, story templates) — see `/social-drafts/2026-05-26-designer-instagram-and-issue01.md`. Growth's job here is the account setup, the launch sequence, and the posting cadence.

### Setup steps (to be executed by Vini at his terminal when convenient)

1. **Create the Instagram account.**
   - Email: `education3881@gmail.com`
   - Handle: `@madar.publication` (preferred). Fallbacks: `@madar.editorial`, `@madar.read`, `@madar.magazine`. Check availability; do not use one with numbers or underscores.
   - Display name: `Madār · مدار`
   - Category: "Publisher" or "News & Media" (Designer's brief specifies; final call is yours at sign-up after seeing what Instagram surfaces).
   - Bio: as drafted in the Designer brief.
   - Single link: `https://education3881.github.io/madar/` — when we have a custom domain, this updates.
   - Profile photo: the wordmark PNG the Designer will produce at `/design-assets/instagram/profile-1080.png`.
   - Two-factor authentication ON at first login. Use the dedicated project email's recovery, not Vini's personal phone, unless he prefers otherwise.

2. **The opening grid (first nine posts).** The grid is the publication's reading shelf — what a new visitor sees in one glance. Plan it on paper before posting any of it. The proposed nine:
   - Post 1: Sierra Leone — lead-piece grid post (hero still + title)
   - Post 2: Sierra Leone — pull paragraph (the "lan fɔ lan" close)
   - Post 3: Bahrain — curated-piece grid post
   - Post 4: Bahrain — pull paragraph (the "what does a state commit to when it puts seventy-six named verdicts in public" line)
   - Post 5: The publication's wordmark on `--color-paper` (a quiet introduction-of-self post, captioned with the tagline only)
   - Post 6: A "reading shelf" still life — the BQA report on a desk, captioned with the document's title and date
   - Post 7: A typographic post — the publication's About paragraph (the slow-cadence one), set in Newsreader on `--color-paper`
   - Post 8: A macron-rule quiet post (the Designer's "quiet rule" divider)
   - Post 9: Sierra Leone — a second pull paragraph (the chalk-and-tin paragraph)

   Post these in the **reverse** of the order above. Instagram displays the grid most-recent-first, so the first-time visitor sees Post 1 in the top-left when posts are made in order 9, 8, 7… 1. The grid the visitor reads is the grid Growth designs.

3. **Cadence.** Three posts a week at launch — Monday, Wednesday, Friday at 10am Gulf time. No weekend posting at first; the publication is editorial, not always-on. Reassess after four weeks against engagement and against the founder's read of the rhythm.

4. **What goes in captions.** Every caption ends with the URL to the piece on the Madār site. Captions are short (≤ 80 words) and in the publication's voice. The caption is not the piece. The caption is the invitation to read the piece. Arabic captions for pieces with Arabic versions, once we have any.

5. **Hashtags.** Sparing. Two to four per post. Use specific publication-relevant tags (#bilingualpublication #educationjournalism #curatedreading) over generic ones (#education #learning). Never hashtag a geography. (Geography-internal rule applies on social copy.)

### Instagram things we are explicitly NOT doing at launch

- **No reels.** The format is wrong for this publication and the Designer is not yet set up to produce them.
- **No paid promotion.** Organic only at launch.
- **No DM auto-responder.** A two-pieces-a-month publication should answer DMs from a human.
- **No "follow for follow" outreach.** The publication earns its audience by being good, not by reciprocity.
- **No re-grams of other education accounts.** The publication's voice is its own. (We may, separately, recommend a piece via a story, occasionally, when it is genuinely good and clearly attributed.)

## 3. Deliverables today

This is a working brief — Growth's job today is the *plan*, not the execution. The setup steps require Vini at his terminal (for account creation, authentication, payment-info-where-relevant). Today's outputs:

1. **A `growth-setup.md` file** confirming the above plan, with any departures from it documented in writing (e.g. if `@madar.publication` is taken). Save at `/social-drafts/2026-05-27-growth-setup-handover.md`.
2. **Substack welcome email copy** drafted for the Editor's review. Save at `/social-drafts/2026-05-26-substack-welcome-email-draft.md`.
3. **First Substack post copy** — the Issue 01 post combining Sierra Leone and Bahrain, with the editorial note about the two-pieces issue. Save at `/social-drafts/2026-05-26-substack-issue-01-draft.md`. Editor approves before send.
4. **Instagram caption drafts for the first 9 posts.** Save at `/social-drafts/2026-05-26-instagram-grid-captions-draft.md`. Editor approves before any post.

When the deliverables above are with the Editor for approval, Growth's today is done. Setup execution happens on Vini's machine on his time.

— Manager
