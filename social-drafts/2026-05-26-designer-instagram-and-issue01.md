# Designer — Instagram identity + Issue 01 hero visuals (2026-05-26)

**From:** Manager → Designer
**Subject:** Today's department goal — Instagram visual identity, and stills for Sierra Leone (existing) + Bahrain (new) only. Do NOT spend craft on Jordan or Colombia; they are parked.

---

## 1. Instagram visual identity (working draft v0.1)

The Madār Instagram presence should read, on a glance, as the publication. Not a tease-version of it. Not "the publication for phones." The same wordmark, the same five-token palette, the same macron motif, the same restraint.

### Handle, name, bio (passed to Growth for setup)

- **Handle:** `@madar.publication` (preferred) or `@madar.editorial` (fallback if the first is taken). Avoid handles with numbers or underscores — they read as inauthentic in this category.
- **Display name:** `Madār · مدار`
- **Category:** "Publisher" or "News & Media" — final call is Growth's after they check what Instagram's recent UI defaults to.
- **Bio (English-first, Arabic line below):**
  > Education, written slowly, in two languages.
  > التعليم، بتأنٍّ، بلغتين

  No emoji. No "🇧🇭 🇸🇱" flag run. No "linktree" link — the single link goes to `https://education3881.github.io/madar/`. Geography stays out of the bio per the internal-only rule.
- **Profile photo:** the wordmark, square-cropped, on `--color-paper` (#FAFAF7), with breathing room equal to one half-stem. Generated at 1080×1080. Source SVG at `/design-assets/wordmark/madar-wordmark.svg`.

### Grid system

The Instagram grid is a publication, not a feed. The composition is the grammar. Four post types:

1. **Lead-piece post** — square. The hero still from the lead piece, with the piece's title set in Cormorant Garamond at the lower-left corner. No URL on the image. Caption carries the URL.
2. **Curated-piece post** — square. The hero still, with the kicker ("Curated · Bahrain · Issue 01") at the top, the title at the centre-bottom, in the same type family as the website. Visual continuity with the home page.
3. **Pull-paragraph post** — square. Type only, on `--color-paper`. A single paragraph from the piece (40–80 words), set in Newsreader regular, max-width 32ch. A small macron motif at the foot. The point of these is to give the feed a different rhythm from the hero stills.
4. **Quiet rule post** — square, used as a divider between issues. The macron-and-baseline-rule motif, centred, on `--color-paper`. Nothing else. Use sparingly — at most one a week.

### Story templates

Two only, for now:

- **New piece** — a vertical 1080×1920 that fades from `--color-paper` at the top into the hero still, with the piece title at 40% from the top in Cormorant Garamond, and the URL at the foot in JetBrains Mono.
- **The reading shelf** — a single still photograph of the source document the piece read, lying on a table next to a notebook. Use sparingly; only for pieces where this composition exists. Bahrain is a candidate (a printed BQA report next to a notebook). Sierra Leone is not — the Bo piece is built on a composite character and a still life would mislead.

### Things to avoid (hard rules)

- No animated carousels with text-on-screen. The publication is not a TikTok account.
- No "10 things you didn't know about ___" templates. The publication is not a listicle account.
- No country flags as design elements. Geography stays editorial, not decorative.
- No quoting from within a piece without the piece's URL in the caption.
- No use of stock photography from international NGOs. If we cannot source an original visual, we make a typographic post.

## 2. Hero stills — what to make today

### Sierra Leone (existing — keep)

The current still at `/web/public/stills/2026-05-25-bo-teacher-chalk.svg` is the approved hero for the Sierra Leone lead. No changes today. If you want to refine it after Issue 01 settles, propose changes via the Editor.

### Bahrain (new — make today, P1)

The Bahrain piece needs a hero still by end-of-day so the build references a real image. File path: `/web/public/stills/2026-05-26-bahrain-bqa-public-grades.svg`.

**Brief from the Editor (paraphrased for visual direction):**

- **Theme:** a regulatory line read as a quiet horizontal slab. The publication's macron motif extended into the page.
- **Mood:** measured, institutional, not warm but not cold. Office-light. Bureaucratic in the dignified sense, not the resigned sense.
- **Dominant emotion:** the still concentration of a building that publishes its own grades on a website, and the residual question of what that costs and earns.
- **Visual references:** (a) the regulated grid of a school facade at midday — vertical strokes, single strong horizontal; (b) the printed top-edge of a published report sitting on a desk.
- **What this piece is NOT:** a stack of report-cards. A chalkboard. A picture of a school. A picture of children. A picture of the Bahraini flag.

**Constraints:**
- Same SVG format as the Sierra Leone still — atmospheric composition, no photographic content, no figurative elements.
- Aspect ratio: 8:5 wide (matches the lead-piece thumb on the home page) — but composed so that a square crop for Instagram preserves the centre.
- Palette: `--color-sand` (#E8E2D0) as ground, `--color-ink` (#0E1B2C) for line work, `--color-orange` (#D94F2A) used at most twice as a small accent — restraint is the brand.
- Filesize budget: ≤ 8KB for the SVG.

### Jordan and Colombia — do NOT make stills

The parked-pieces brief from the Editor is clear: the topics are not coming back without primary-source verification. Visual work on these pieces is on hold. The mockups under `/design-assets/article-mockups/article-02-jordan-textbook/` and `/design-assets/article-mockups/article-03-colombia-escuela-nueva/` stay in the design archive as craft artefacts but are not referenced from production.

## 3. Deliverables today (in priority order)

1. **Bahrain hero still** — P1. Saved at `/web/public/stills/2026-05-26-bahrain-bqa-public-grades.svg`. Sized and composed per the brief above.
2. **Instagram profile photo** — P1. Saved at `/design-assets/instagram/profile-1080.svg` (and a PNG export at `/design-assets/instagram/profile-1080.png` for upload).
3. **Two grid posts** — P2. The first is the Sierra Leone lead-piece post (square, using the existing still + headline). The second is the Bahrain curated-piece post. Save at `/design-assets/instagram/2026-05-26-sierra-leone-grid.svg` and `/design-assets/instagram/2026-05-26-bahrain-grid.svg`.
4. **One pull-paragraph post template** — P2. The template SVG with placeholder text, saved at `/design-assets/instagram/post-template-pull-paragraph.svg`.
5. **Two story templates** — P3. As described above, saved at `/design-assets/instagram/story-template-new-piece.svg` and `/design-assets/instagram/story-template-reading-shelf.svg`.

P1 items are required for today's deploy and the Instagram account's first day. P2 items should land before the Growth agent posts the first piece (planned for tomorrow). P3 items are a backlog this week.

## 4. How to flag a blocker

If something in this brief conflicts with the design system in `/design-assets/design-system/SYSTEM.md`, raise it as a Designer-side memo at `/agents/logs/designer-status-2026-05-26.md` and we'll resolve it before the deploy. The system document is the source of truth on any disagreement between this brief and previous design decisions.

— Manager
