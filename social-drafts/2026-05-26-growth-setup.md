# Growth setup — Instagram + Buttondown

**From:** Growth (with Manager review)
**To:** Vini
**Date:** 2026-05-26

Everything in this file that doesn't require account creation has been drafted. The account-creation steps are listed at the bottom — they need you (or someone with the dedicated `education3881@gmail.com` inbox open) because of the email-verification step in each platform's sign-up.

---

## Buttondown — recommendation and setup

**Recommendation: use Buttondown, not Substack.**

Reasons, in editorial register:

1. **No recommendation feed.** Substack's "Recommended for you" surface and Notes-style social layer pull subscribers toward an attention-economy register that pulls against Madār's posture. Buttondown does not push subscribers anywhere; the email arrives, the reader reads, the relationship ends until the next email.
2. **Cleaner reading experience.** Buttondown's email rendering is closer to a well-typeset memo than to a magazine layout. For a publication whose visual identity is editorial-print, this is a meaningful match.
3. **No social-byline cluster.** Substack puts the writer's face and a "writes for *Publication*" badge at the top of every email. Madār's editorial position is that the publication is the author; bylines for editors and designers belong on each piece, not on every email.
4. **Open architecture.** Buttondown supports custom domains, JSON exports, RSS, and a straightforward API — useful when we want to move the list later (and we will eventually, regardless of platform choice).
5. **Free tier sufficient for now.** Buttondown's free tier covers 100 subscribers; the paid tier is reasonable when we cross that line.

### Buttondown account setup (the part that needs you)

Estimated time: 4 minutes.

1. Open **https://buttondown.email/register**.
2. Sign up with **education3881@gmail.com**. Confirm via the email it sends.
3. Newsletter name: **Madār**. Description: *An editorial publication on early childhood and K–12 education, written slowly, in two languages.*
4. Choose username: **madar** (if available). Fall back to **madar-publication**.
5. Avatar: upload `/design-assets/wordmark/madar-wordmark.svg` (or a PNG export from it; the avatar field may require PNG).
6. Once you reach the dashboard, go to **Settings → Embedding**. Copy the form HTML — that's what the Web Developer needs to wire into the site footer.

### Footer embed snippet (Web Developer wires this once you have the form URL)

The current site footer renders without an embedded form. Once you have the Buttondown form URL, here is the exact patch to apply to `web/src/components/SiteFooter.astro` — Web Developer can apply this in one small commit:

```astro
<!-- Insert this block inside .site-footer__cell--nav, after the <ul> -->
<form
  action="https://buttondown.email/api/emails/embed-subscribe/madar"
  method="post"
  target="popupwindow"
  onsubmit="window.open('https://buttondown.email/madar', 'popupwindow')"
  class="site-footer__subscribe"
>
  <label for="bd-email" class="uppercase">Newsletter</label>
  <input id="bd-email" type="email" name="email" placeholder="email" required />
  <button type="submit" class="uppercase">Subscribe</button>
</form>
```

With matching CSS (kept deliberately understated — no glow, no animation, no banner):

```css
.site-footer__subscribe {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-block-start: 1rem;
  max-width: 240px;
}
.site-footer__subscribe label { font-family: var(--font-mono); font-size: 10.5px; letter-spacing: 0.08em; opacity: 0.7; }
.site-footer__subscribe input {
  background: transparent;
  border: none;
  border-block-end: 1px solid var(--color-rule);
  padding: 0.35rem 0;
  font-family: var(--font-body);
  font-size: 14px;
  color: var(--color-ink);
}
.site-footer__subscribe input:focus { outline: none; border-block-end-color: var(--color-orange); }
.site-footer__subscribe button {
  align-self: flex-start;
  background: none;
  border: none;
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.12em;
  color: var(--color-orange);
  border-block-end: 1px solid var(--color-orange);
  padding: 0 0 2px;
  cursor: pointer;
}
```

The embed is **footer-only, no modal, no banner, no home-page hero placement**. This is deliberate per editorial posture.

---

## Instagram — handle, bio, posting posture

### Handle preference order (the part that needs you)

Estimated time: 2 minutes.

1. Open **https://www.instagram.com/accounts/emailsignup/**.
2. Sign up with **education3881@gmail.com**. The Instagram app on phone is easier than web.
3. Try handle in this order:
   - **@madar** (almost certainly taken — common Arabic word)
   - **@madar.publication**
   - **@madar.editorial**
   - **@madarmagazine** (last resort — *magazine* slightly off-brand but acceptable)
4. Full name field: **Madār · مدار**
5. Bio: use the English version below for the English bio field, and add the Arabic line on a new line if Instagram permits multi-line. Madār is bilingual and both scripts should be visible in the profile.

### Instagram bio — English

```
An editorial publication on early childhood and K–12 education.
Written slowly, in two languages.
education3881.github.io/madar/
```

(150 chars — Instagram bio limit is 150. This fits.)

### Instagram bio — Arabic (paste into the same bio field on a new line, or use the alternative-language bio feature)

```
منشورٌ تحريريٌّ عن التعليم في الطفولة المبكّرة والتعليم العامّ.
نكتبُ بتأنٍّ، بلغتَين.
```

### First-week Instagram posture

Listed so the account doesn't open at the wrong tempo:

1. **Follow zero accounts on day one.** A publication that follows no one and posts slowly reads differently than one that opens with a follow-spree. Resist the temptation.
2. **No introduction post.** The first post is the Sierra Leone Still (the painterly SVG, exported as a 1080×1080 PNG) with a one-line caption: *Issue 01 · Sierra Leone · "The teacher in Bo who still uses last term's chalk."* And the link in bio. No emoji. No "🚀 we're live!"
3. **One post per week for the first month.** No reels. No stories. No carousels. Editorial register only.
4. **Mute Instagram's notification spam from the app** so it doesn't pull your attention. Posting once a week does not require checking the app daily.

### First post — image + caption

**Image:** `/web/dist/stills/2026-05-25-bo-teacher-chalk.svg` (need a PNG export at 1080×1080 for IG). The Designer can produce this; alternatively, any reasonable SVG-to-PNG converter at 1080×1080 will do for the first post.

**Caption (English):**

```
Issue 01 · Sierra Leone

"The teacher in Bo who still uses last term's chalk."

A field note on Sierra Leone's Free Quality School Education policy at ten,
and the people whose unpaid hours the policy quietly relies on.

Read it: link in bio.
```

**Caption (Arabic — secondary, optional for first post):**

```
العدد الأول · سيراليون

«المعلّمة في بو التي ما زالت تستخدم طباشير الفصل الماضي.»

تقريرٌ ميدانيٌّ عن سياسة التعليم المجاني في سيراليون بعد عشر سنوات،
وعن الناس الذين تعتمد هذه السياسة على ساعاتهم غير المدفوعة بصمت.

الرابط في السيرة الذاتية.
```

---

## What is on Vini's plate only

In order of how long each takes:

1. **Enable GitHub Pages source** (30 seconds — see *DEPLOY_STATUS.md* in the repo root). This is the one switch standing between the pushed code and a live site at `https://education3881.github.io/madar/`.
2. **Revoke the `madar-deploy-once` PAT** (30 seconds — https://github.com/settings/personal-access-tokens, click "Revoke").
3. **Create the Buttondown account** (4 minutes — see above).
4. **Create the Instagram account** (2 minutes — see above).
5. **Approve or revise the newsletter draft** (15 minutes — see `2026-05-26-newsletter-issue-01.md`). Earliest send is Thursday 2026-05-28.

Total Vini time today: ~22 minutes spread across whenever, none of it blocking on each other.

All other work — source review on Jordan/Colombia, Issue 02 slate decision, Web Developer's footer embed wiring after Buttondown URL is in — is sequenced for the days that follow.
