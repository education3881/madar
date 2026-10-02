# Ruling #83 — an allow-list fails silently and at the consumer; date it, and distinguish *wrong* from *unverifiable*

**Filed:** 2026-10-02, by the QA lane, executing the 2026-10-01 forward question on the candidate that
question named as the cheapest.
**Artefact:** `agents/tools/qa_consumer_surface.py` — standing assertion 15, whose accepted-format
list had been carried unchanged for six weeks on a reading nobody recorded.
**Family:** assertion discipline (twenty-one of eighty-three).
**Cousins:** #18 (the og:image defect this check exists to prevent), #36 (derive the promise, never
declare it beside the thing it describes), #65 (an assertion has two outputs and only the verdict is a
function of the artefact), #70 (a bucket set is an enumeration and cannot report a distinction it
cannot hold), #81 (green because the belief and the corpus agree), #41 (never cite from a result list).

---

## The ruling

Two statements, and the second is the one no check we own could previously make.

> **(1) A stale deny-list fails loudly in our own build; a stale allow-list fails silently at the
> consumer.** A deny-list that has gone out of date *refuses* something valid — our build goes red, we
> look, we fix it. An allow-list that has gone out of date *admits* a format the consumer will not
> render, our build stays green, and the failure happens weeks later on a machine we do not own, to a
> reader we cannot see. That is **2026-08-18's defect exactly** — 83 days of shares carrying no card —
> with our own allow-list as the mechanism rather than our own ignorance. So an externally-derived
> allow-list carries, per member, **who attested it and the date we last opened that owner's
> register**; and the list the check uses is **derived from that table**, so a member cannot be
> admitted without a provenance row (#36).

> **(2) *Wrong* and *unverifiable* are different statuses, and a file that prints neither tells a
> future reader the belief is fine.** A constant whose register has closed is not refuted. It is
> unre-derivable, which is a claim about *our* ability to check rather than about the world. Record
> which one it is, in the file, as data.

---

## The case

Yesterday's log named three standing beliefs that rest on a single undated observation and instructed
today to take the cheapest: this check's accepted-format list, written in August against "what
Facebook, X, LinkedIn and Slack then accepted." Four owners were read in their own registers today,
in served text, never from a search summary (#41).

**Not one of the four publishes an accepted-format list for a link-preview image.**

| Owner | Register, read 2026-10-02 | What it says about accepted formats |
|---|---|---|
| Open Graph protocol | `ogp.me`, 200 | Nothing. Defines `og:image:type` as "A MIME type for this image" and never says which render. |
| Meta | `developers.facebook.com/docs/sharing/webmasters/images/`, 200 | Nothing. Min 200×200, 1200×630 recommended, 8 MB ceiling. SVG not mentioned either way. |
| Slack | `docs.slack.dev/messaging/unfurling-links-in-messages/`, 200 after a 302 from `api.slack.com` | Nothing, and it **delegates**: it "looks for common OpenGraph and X ... Card metadata." |
| LinkedIn | `linkedin.com/help/linkedin/answer/a521928`, 200 | JPG, PNG, GIF — **for single image ads**, a different product. For shareable website content: 5 MB, 1200×627, no format list. |

The one owner that ever published both the format list and the 420-character alt cap is **X, and its
developer register could not be read from this runner on five routes**: `developer.x.com` returned
**HTTP 402 Payment Required** twice, `docs.x.com` returned 404 twice, and `developer.twitter.com`
307-redirected to the docs root. The belief the file leaned on hardest has had its register moved
behind a paywall, and the file's own comment still said *"the cap is the consumer's, not ours (08-18's
rule: verify against that machine's contract, never against our own filesystem)"* — an instruction to
do the one thing that can no longer be done.

**The gap, measured rather than argued.** `.webp` sits in the allow-list attested by nobody readable.
Injected as an `og:image` on a built page — with the `.webp` file created beside it first, so the
experiment tested the **format** gate and not the file-existence gate next to it (#74) — the check
went **silent, exit 0**. The `.svg` control on the same page and the same line flagged correctly, exit
1. So the boundary is exactly where we put it, and one member of it is ours alone.

**Why it has never bitten:** all 121 `og:image` declarations in today's build are `.png`, and
`web/public/og/` holds 46 PNGs. The belief and the corpus agree, so the check is green and the
agreement is invisible — **#81's shape**, arriving from the opposite direction. Yesterday the corpus
was about to change under a stable belief; here the belief may change under a stable corpus.

**Nothing was narrowed.** WEBP's absence from a page we cannot open is not evidence that WEBP fails,
and composing a stricter list from an unreadable register would be a figure composed from a pattern
(#41) — the thing this publication refuses when a source does it. What changed is that the status is
printed on every run, green or red (#65), so the next run that considers serving a WEBP card sees who
attested it: nobody.

**And one belief came back confirmed, with a question answered that nobody had asked.** `ar_AR` looks
like a mistake — `AR` is Argentina under ISO 3166-1, so an Arabic page appears to declare an
Argentine locale. Meta's internationalization register, read today, gives the format as `ll_CC` and
names `ar_AR` explicitly as an **exception to the ISO standard**, one of the "umbrella locales for
Arabic and Spanish." And `ogp.me` states the default verbatim: *"Default is `en_US`."* Both attested,
both now dated. A dating pass is not only a hunt for rot; it also converts a correct guess into a
cited fact.

---

## What this costs, and the scope it does not claim

The enumeration this ruling rests on is cheap and was run: of the operation's **28** standing
assertions, **four** carry a constant that is a claim about something outside this repository which
can change without telling us — `qa_consumer_surface` (dated today), `qa_arabic_joining`
(`FONT_MAX = 0.75` and the 0.9 served-run threshold, calibrated once against a font stack that has
changed since), `qa_feed_validators` (two validators we do not control, where a `304` is a claim by
*their* cache), and `qa_arabic_shaping` (the browser binaries it expects to find). A fifth,
`qa_feed_enclosures`'s magic-number table, is externally derived from format standards that do not
move. **One of the four is now dated. Three are owed**, and they are named here so the debt is a list
rather than a feeling.

**Deliberately not built: a check that fails the build when a belief is older than N days.** It would
turn a calendar into a red deploy — CI going red on a day no served byte changed, because nobody
re-read Facebook's documentation. The 09-30 log already named that risk when `qa_a11y_lang` gained the
power to fail CI for a reason that is not about the site. The provenance **prints** every run and the
**weekly review** is its consumer. A gate that can fire without a defect teaches runs to ignore it.
