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
   the whole head is covered by one assertion).

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
    r'<meta\s+(?:property|name)="(og:[a-z_:]+)"\s+content="([^"]*)"', re.I
)
HTML_LANG = re.compile(r'<html\s+lang="([a-z-]+)"', re.I)

RASTER = (".png", ".jpg", ".jpeg", ".webp", ".gif")
EXPECTED_LOCALE = {"en": "en_US", "ar": "ar_AR"}


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
    print(f"pages checked: {checked} · sitemap <loc>: {locs} · <lastmod>: {lastmods}")
    if defects:
        print(f"\nDEFECTS: {len(defects)}")
        for d in defects[:60]:
            print("  ✗ " + d)
        if len(defects) > 60:
            print(f"  … and {len(defects) - 60} more")
        return 1

    print("CLEAN — og:locale, og:type, og:site_name, og:image raster, "
          "sitemap lastmod, print block all pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
