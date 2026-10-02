#!/usr/bin/env python3
"""
qa_consumer_surface.py — standing assertions for the three non-browser
consumers of this site: the social scraper, the crawler, and the printer.

Added 2026-08-24, extending the line of work that began on 08-18.

WHY THIS FILE EXISTS
--------------------
Three runs in a row have now found multi-month defects by asking one question:
*what does the consumer actually receive?*

  08-18  og:image was an SVG on all 76 article pages. It existed, the URL was
         absolute, every link check passed — and no social consumer renders
         SVG, so 83 days of shares carried no card.
  08-23  every Arabic page printed its country, region, level and themes in
         English. `lang="ar"` and `dir="rtl"` were both present and correct;
         the content inside them was not. Ruling #33.
  08-24  (this file) three more surfaces, all confirmed defective.

The pattern is stable enough to be worth naming: our checks were written to
catch metadata being ABSENT or MALFORMED. Every one of these defects was
metadata that was present, well-formed, and wrong — or, in two cases today,
absent in a way that has a harmful DEFAULT rather than no effect at all.

WHAT IT ASSERTS
---------------
1. og:locale is present and agrees with <html lang>.
   The Open Graph default when og:locale is absent is en_US. Every Arabic page
   has been serving an Arabic title and an Arabic description under an implicit
   claim of American English since 25 May. Absence was not neutral.

2. og:type is 'article' on article routes and 'website' everywhere else.
   It was hardcoded to 'article' on all 82 pages, including both home pages,
   About, and both editions indexes.

3. og:site_name is present.

4. og:image, where present, is a raster file (the 08-18 rule, restated here so
   the whole head is covered by one assertion), and it carries og:image:alt and
   twitter:image:alt, non-empty and within the 420 characters the consumer
   accepts (added 2026-09-15).

   Every constant in (1) and (4) is a claim about a machine we do not own, so
   each one now carries the date we last opened its owner's register and who
   attested it. See EXTERNAL_IMAGE_FORMATS below, added 2026-10-02: the
   accepted-format list is derived from that table rather than declared beside
   it, the provenance prints on every run, and one member of the list turns out
   to be attested by nobody we can currently read.

5. sitemap.xml carries a <lastmod> on every <loc>. It carried none from
   2026-07-02 until today.

6. The built CSS contains a print block that (a) hides the share rail and
   (b) expands source URLs. A printed Madār piece with no citation URLs is not
   a citable document, which is the only thing this publication claims to be.

SILENT-PASS TRAP (08-16)
------------------------
An assertion that finds nothing to check has FAILED, not passed. Zero pages
located, or zero sitemap <loc> entries, exits 2 — never 0.

Usage:  python3 agents/tools/qa_consumer_surface.py [dist_dir]
Exit:   0 clean · 1 defects found · 2 nothing to check (assertion is broken)
"""

import re
import sys
from pathlib import Path

DIST = Path(sys.argv[1] if len(sys.argv) > 1 else "web/dist")

META = re.compile(
    # `twitter:*` added 2026-08-26 — the Twitter card tags are a promise about
    # the OG image, so they have to be readable in the same pass that checks it.
    r'<meta\s+(?:property|name)="((?:og|twitter):[a-z_:]+)"\s+content="([^"]*)"', re.I
)
HTML_LANG = re.compile(r'<html\s+lang="([a-z-]+)"', re.I)

# ---------------------------------------------------------------------------
# WHEN WAS EACH EXTERNAL EXPECTATION LAST DERIVED FROM THE WORLD?
# Added 2026-10-02, answering the 2026-10-01 forward question.
# ---------------------------------------------------------------------------
# Every constant below is a claim about a machine this operation does not own.
# The assertion runs daily; the belief inside it does not. The accepted-format
# list was written in August 2026 and carried unchanged for six weeks on the
# strength of a reading nobody recorded — which is the exact defect class
# ruling #18 was filed on, pointed at our own instrument instead of at a source.
#
# So the beliefs are dated here, as data rather than as prose, and the
# allow-list below is DERIVED from this table (#36) — a format cannot be
# accepted by the check without a provenance row saying who attested it and
# when we last read them say so.
#
# What the 2026-10-02 derivation found, and it is not what the old comment
# claimed. The comment credited the format list to four consumers. Read in
# their own registers today, NOT ONE OF THE FOUR publishes an accepted-format
# list for a link-preview image:
#
#   ogp.me                     states no formats at all. It defines
#                              `og:image:type` as "A MIME type for this image"
#                              and never says which are rendered.
#   Meta (webmasters/images)   states no formats. Dimensions (min 200x200,
#                              1200x630 recommended) and an 8 MB ceiling only.
#                              SVG is not mentioned either way.
#   Slack (docs.slack.dev)     states no formats, and delegates: it "looks for
#                              common OpenGraph and X ... Card metadata."
#   LinkedIn (help a521928)    names JPG, PNG, GIF — for SINGLE IMAGE ADS, a
#                              different product. For shareable website content
#                              it gives 5 MB and 1200x627 and no format list.
#
# The one owner that ever published both the format list and the 420-character
# alt cap is X, and ON 2026-10-02 X'S DEVELOPER REGISTER COULD NOT BE READ
# FROM THIS RUNNER ON FIVE ROUTES: developer.x.com returned HTTP 402 Payment
# Required twice, docs.x.com returned 404 twice, and developer.twitter.com
# 307-redirected to the docs root. The cap is therefore not wrong — it is
# UNVERIFIABLE, which is a different status, and this file used to record the
# two identically.
#
# The consequence is specific and it points one way. This is an ALLOW-list, so
# a stale member is admitted rather than rejected: a deny-list that goes stale
# refuses something valid and fails loudly in our own build, while an allow-list
# that goes stale ACCEPTS a format the consumer will not render, and that
# failure is silent and happens at the consumer. That is 2026-08-18's defect
# exactly — 83 days of shares carrying no card — with our own allow-list as the
# mechanism. `.webp` is the member no readable register attests, and the only
# reason it has never bitten is that all 121 cards this build serves are PNG:
# the belief and the corpus agree, which is ruling #81's shape.
#
# Nothing is narrowed on this reading. Composing a stricter list from an
# unreadable register would be a figure composed from a pattern (#41), and WEBP
# being absent from a paywalled page is not evidence that WEBP fails. What
# changes is that the status is now printed, so a run that ever considers
# serving a WEBP card sees who attested it: nobody.
#
#   attested_by  — the owner whose own register names this format, read in
#                  served text on `derived`, never from a search summary (#41).
#   derived      — the date WE last opened that register, not the date it was
#                  written. A belief with an old date here is not wrong; it is
#                  undated, and undated is the status this block exists to end.
EXTERNAL_IMAGE_FORMATS = [
    # ext      attested_by                                      derived       status
    (".png",  "LinkedIn help a521928 (ads list); X, when readable", "2026-10-02", "attested"),
    (".jpg",  "LinkedIn help a521928 (ads list); X, when readable", "2026-10-02", "attested"),
    (".jpeg", "LinkedIn help a521928 (ads list); X, when readable", "2026-10-02", "attested"),
    (".gif",  "LinkedIn help a521928 (ads list); X, when readable", "2026-10-02", "attested"),
    (".webp", "nobody readable — X only, register 402 on 2026-10-02", "2026-10-02", "UNATTESTED"),
]
RASTER = tuple(ext for ext, _, _, _ in EXTERNAL_IMAGE_FORMATS)

# The 420 cap's sole owner is X and its register is paywalled (above). Carried
# unchanged, with the status recorded rather than implied.
ALT_CAP = 420
ALT_CAP_PROVENANCE = ("X developer docs", "2026-08-18 (last readable); "
                      "re-derivation refused 402 on 2026-10-02", "UNVERIFIABLE")

# `ar_AR` is the one belief in this file its owner confirms in its own voice,
# and the derivation answered a question nobody had asked: AR is Argentina
# under ISO 3166-1, so `ar_AR` looks like a typo for an Arabic locale. It is
# not. Meta's internationalization register, read 2026-10-02, gives the format
# as `ll_CC` ("a two-letter language code" + "a two-letter country code") and
# names `ar_AR` explicitly as an exception to the ISO standard — one of the
# "umbrella locales for Arabic and Spanish." Attested, dated, and correct.
# The `en_US` default is ogp.me's own words, read the same day: "Default is
# `en_US`." So absence is not neutral, as the header has said since 08-24.
EXPECTED_LOCALE = {"en": "en_US", "ar": "ar_AR"}
LOCALE_PROVENANCE = ("ogp.me (format + en_US default); Meta "
                     "developers.facebook.com/docs/internationalization "
                     "(ll_CC, ar_AR named as an ISO exception)", "2026-10-02",
                     "attested")


def is_article_route(rel: str) -> bool:
    """/articles/<slug>/ and /ar/articles/<slug>/ only."""
    return "/articles/" in "/" + rel


def main() -> int:
    if not DIST.is_dir():
        print(f"FATAL: dist not found at {DIST}", file=sys.stderr)
        return 2

    pages = sorted(p for p in DIST.rglob("*.html"))
    # /valence/ is a hand-written standalone instrument with its own head,
    # deliberately outside the Astro layout. Excluded by name, not silently.
    pages = [p for p in pages if "valence" not in p.parts]
    if not pages:
        print("FATAL: zero pages located — the assertion is broken, not passing.",
              file=sys.stderr)
        return 2

    defects: list[str] = []
    checked = 0

    for page in pages:
        rel = str(page.relative_to(DIST))
        html = page.read_text(encoding="utf-8", errors="replace")
        head = html[: html.lower().find("</head>") + 7]

        lang_m = HTML_LANG.search(html)
        if not lang_m:
            defects.append(f"{rel}: no <html lang>")
            continue
        lang = lang_m.group(1)[:2]

        og = {k.lower(): v for k, v in META.findall(head)}
        checked += 1

        want_locale = EXPECTED_LOCALE.get(lang)
        got_locale = og.get("og:locale")
        if not got_locale:
            defects.append(f"{rel}: og:locale MISSING (lang={lang}; OG defaults to en_US)")
        elif want_locale and got_locale != want_locale:
            defects.append(f"{rel}: og:locale={got_locale} but lang={lang} (want {want_locale})")

        want_type = "article" if is_article_route(rel) else "website"
        got_type = og.get("og:type")
        if got_type != want_type:
            defects.append(f"{rel}: og:type={got_type!r} (want {want_type!r})")

        if not og.get("og:site_name"):
            defects.append(f"{rel}: og:site_name MISSING")

        img = og.get("og:image")
        if img and not img.lower().endswith(RASTER):
            defects.append(f"{rel}: og:image is not raster — {img}")

        # ---- the card must EXIST at the URL declared (added 2026-08-27) --
        # Presence is a declaration; existence is the asset. On 08-26 the five
        # non-article pages declared `https://…github.io/og/brand-card.png` —
        # present, raster, absolute, and missing the `/madar` base, so the
        # first consumer to dereference it would have got a 404. This check
        # maps the declared URL back to a file in dist and requires it to be
        # there. A card URL we cannot serve is a promise with nothing behind
        # it — same family as ruling #36.
        if img:
            from urllib.parse import urlparse
            path = urlparse(img).path
            base_prefix = "/madar/"
            if not path.startswith(base_prefix):
                defects.append(
                    f"{rel}: og:image URL escapes the site base — {img}")
            elif not (DIST / path[len(base_prefix):]).is_file():
                defects.append(
                    f"{rel}: og:image declares {img} but no such file in dist")

        # ---- the card promise (added 2026-08-26) -------------------------
        # Two assertions the 08-18 raster check could not make, because it was
        # scoped to pages that HAVE an og:image and every article does.
        #
        # (1) EVERY served page needs a card. The five non-article pages —
        #     /, /ar/, /editions/, /ar/editions/, /about/ — had none for 93
        #     days, and they include both front doors, i.e. the URLs a reader
        #     is most likely to share.
        # (2) `twitter:card=summary_large_image` is a PROMISE of a large image.
        #     Declaring it with no image is the same defect class as declaring
        #     an SVG: metadata a machine we do not own will act on and find
        #     nothing behind. The promise must track the asset, both ways.
        if not img:
            defects.append(f"{rel}: og:image MISSING — this page shares with no card")
        tw = og.get("twitter:card")
        if tw == "summary_large_image" and not img:
            defects.append(f"{rel}: twitter:card promises a large image and none is declared")
        if img and tw != "summary_large_image":
            defects.append(f"{rel}: has an og:image but twitter:card={tw!r} — the card is wasted")

        # ---- the card must SAY WHAT IT IS (added 2026-09-15) -------------
        # 08-18 asked whether the consumer can render the asset. This asks the
        # question one reader further out: what does the share look like to
        # someone who cannot see the image? Every page has declared an
        # og:image since 25 May and not one declared og:image:alt — 113 days of
        # shares carrying a picture and no description of it, on a surface
        # where the description is not ours to add later. The text existed the
        # whole time, composed in both languages as the hero still's alt.
        # Twitter rejects an image alt over 420 characters, so the cap is the
        # consumer's, not ours (08-18's rule: verify against that machine's
        # contract, never against our own filesystem).
        if img:
            for key in ("og:image:alt", "twitter:image:alt"):
                text = (og.get(key) or "").strip()
                if not text:
                    defects.append(f"{rel}: {key} MISSING — the card describes itself to nobody")
                elif len(text) > ALT_CAP:
                    defects.append(f"{rel}: {key} is {len(text)} chars, over the "
                                   f"{ALT_CAP} the consumer accepts")

    # ---- sitemap lastmod -----------------------------------------------
    # sitemap-index.xml points at the sitemaps, not at pages — counting its
    # single <loc> would make lastmods fall one short of locs forever.
    sitemaps = [p for p in DIST.glob("sitemap-*.xml") if p.name != "sitemap-index.xml"]
    if not sitemaps:
        print("FATAL: no sitemap-*.xml in dist — cannot check lastmod.", file=sys.stderr)
        return 2
    locs = lastmods = 0
    for sm in sitemaps:
        xml = sm.read_text(encoding="utf-8", errors="replace")
        locs += xml.count("<loc>")
        lastmods += xml.count("<lastmod>")
    if locs == 0:
        print("FATAL: sitemap carries zero <loc> — assertion is broken.", file=sys.stderr)
        return 2
    if lastmods < locs:
        defects.append(f"sitemap: {locs} <loc> but only {lastmods} <lastmod>")

    # ---- print stylesheet ----------------------------------------------
    css = "".join(
        p.read_text(encoding="utf-8", errors="replace") for p in DIST.rglob("*.css")
    )
    inline = "".join(
        p.read_text(encoding="utf-8", errors="replace") for p in pages[:1]
    )
    css += inline
    if "@media print" not in css:
        defects.append("css: no @media print block in built output")
    else:
        if ".share-inline" not in css.split("@media print", 1)[1][:2500]:
            defects.append("css: print block does not hide the share rail")
        if "attr(href)" not in css:
            defects.append("css: print block does not expand source URLs (attr(href))")

    # ---- report ---------------------------------------------------------
    # The provenance is printed on every run, green or red. A belief carried on
    # trust is invisible precisely because the check around it passes (#65: an
    # assertion has two outputs, and only the verdict is guaranteed to be a
    # function of the artefact — the record is what later runs read as true).
    unattested = [e for e, _, _, s in EXTERNAL_IMAGE_FORMATS if s != "attested"]
    print(f"pages checked: {checked} · sitemap <loc>: {locs} · <lastmod>: {lastmods}")
    print(f"external beliefs · image formats {''.join(RASTER)} "
          f"derived {EXTERNAL_IMAGE_FORMATS[0][2]}"
          + (f", UNATTESTED: {' '.join(unattested)}" if unattested else "")
          + f" · alt cap {ALT_CAP} {ALT_CAP_PROVENANCE[2]} ({ALT_CAP_PROVENANCE[1]})"
          + f" · locales {sorted(EXPECTED_LOCALE.values())} {LOCALE_PROVENANCE[2]}"
          f" {LOCALE_PROVENANCE[1]}")
    if defects:
        print(f"\nDEFECTS: {len(defects)}")
        for d in defects[:60]:
            print("  ✗ " + d)
        if len(defects) > 60:
            print(f"  … and {len(defects) - 60} more")
        return 1

    print("CLEAN — og:locale, og:type, og:site_name, og:image raster + alt, "
          "sitemap lastmod, print block all pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
