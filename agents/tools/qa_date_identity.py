#!/usr/bin/env python3
"""Standing assertion 22 — every rendered date agrees with its own frontmatter.

WHY THIS EXISTS (2026-09-22, ruling #60)
----------------------------------------
Three rulings already cover how our lists are ORDERED — #57 (by which set),
#58 (by which tiebreak), #59 (decided by what). The 09-21 QA log named the
other side of the comparator as the next surface: **the value it is handed.**

A frontmatter `date:` is a bare `YYYY-MM-DD` string with no timezone, which
`z.coerce.date()` parses as **UTC midnight**. Eight `Intl.DateTimeFormat`
instances then rendered that instant with **no `timeZone` option**, which means
they asked the BUILD MACHINE what day it was. Every runner behind UTC answers
with the day before. Proved on 2026-09-22: the same commit, built once under
`TZ=UTC` and once under `TZ=America/Los_Angeles`, differed on **116 of 121
pages**, and the Singapore piece dated `2026-07-07` printed *July 6, 2026* in
English and ١٨ سبتمبر ٢٠٢٦-style shifts in Arabic. Our own CI happens to be UTC
and the operation's calendar is Asia/Dubai (UTC+4) — both land on the right
side of midnight, which is why nothing has ever shown. That is luck, not a
guard, and luck is what this file replaces.

WHAT IT ASSERTS
---------------
1. Article pages: the date printed in the `kicker-meta` block of
   `articles/<slug>/` and `ar/articles/<slug>/` equals the date in that slug's
   own frontmatter — in the language that page is written in, with Arabic pages
   in Arabic-Indic digits (the `qa_ar_language` contract, re-asserted here
   against the frontmatter rather than against the digit set).
2. Listing pages: every date carrier on every listing surface
   (`lead__byline`, `secondary__byline`, `piece__date`) is paired with the
   article it sits beside, and equals that article's frontmatter date. Home,
   Arabic home, both editions indexes and all browse facets are in scope.
3. Non-vacuity: the number of article pages checked must equal the number of
   approved pieces on disk, and the listing-pair count must be non-zero. A
   check that finds nothing to check has failed, not passed (08-16 trap).

The expected strings are built in Python from the frontmatter date with month
tables transcribed from `en-US` and `ar-EG`, so this tool shares no clock, no
locale and no formatter with the thing it judges — which is the whole point.

No third-party dependencies. Exit 0 clean, exit 1 with a sentence.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

EN_MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
AR_MONTHS = [
    "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
    "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر",
]
ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"

DATE_CARRIER_CLASSES = ("lead__byline", "secondary__byline", "piece__date", "kicker-meta")

EN_DATE_RE = re.compile(r"(?:" + "|".join(EN_MONTHS) + r") \d{1,2}, \d{4}")
AR_DATE_RE = re.compile(r"[٠-٩]{1,2} (?:" + "|".join(AR_MONTHS) + r") [٠-٩]{4}")
ANY_HREF_RE = re.compile(r'href="([^"]+)"')
ARTICLE_HREF_RE = re.compile(r"/articles/(\d{4}-\d{2}-\d{2}-[a-z0-9\-]+)/$")

# A listing row whose date has no frontmatter behind it, declared with its
# reason. See the listing branch in main() for why this is a named exemption
# rather than a silent skip.
DECLARED_NON_ARTICLE_ROWS = {"/madar/valence/"}


def ar_digits(n: int, width: int = 0) -> str:
    s = str(n).rjust(width, "0") if width else str(n)
    return "".join(ARABIC_DIGITS[int(c)] for c in s)


def expected_en(y: int, m: int, d: int) -> str:
    return f"{EN_MONTHS[m - 1]} {d}, {y}"


def expected_ar(y: int, m: int, d: int) -> str:
    return f"{ar_digits(d)} {AR_MONTHS[m - 1]} {ar_digits(y)}"


def read_frontmatter_dates() -> tuple[dict[str, tuple[int, int, int]], int]:
    """slug -> (y, m, d) for every APPROVED piece, EN and AR alike.

    A held piece contributes no page (#18), so it contributes no expectation
    either; its absence from the built site is qa_held_assets' job, not ours.
    """
    dates: dict[str, tuple[int, int, int]] = {}
    approved = 0
    for coll in ("articles", "articles-ar"):
        for f in sorted((REPO / "web" / "src" / "content" / coll).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            head = text.split("\n---", 1)[0]
            if not re.search(r"^approved:\s*true\s*$", head, re.M):
                continue
            m = re.search(r"^date:\s*(\d{4})-(\d{2})-(\d{2})\s*$", head, re.M)
            if not m:
                return {}, -1
            approved += 1
            y, mo, d = (int(x) for x in m.groups())
            slug = f.stem
            prior = dates.get(slug)
            if prior is not None and prior != (y, mo, d):
                print(
                    f"qa_date_identity: FAIL — {slug} carries {prior} in one language "
                    f"and {(y, mo, d)} in the other; a pair has one date."
                )
                sys.exit(1)
            dates[slug] = (y, mo, d)
    return dates, approved


def carriers(html: str) -> list[tuple[int, str]]:
    """(offset, inner text) for every element whose class is a date carrier.

    The element's own tag name is captured and used to close the match. Closing
    on a fixed `</div>|</p>` instead — the first draft of this file — makes one
    `<span class="piece__date">` swallow every list item after it on the
    editions index, which paired nine dates with the first slug on the page and
    failed a known-good control. That is the 2026-09-14 trap on the input side:
    an assertion scoped wider than the thing it checks finds the right string
    for the wrong reason, or the wrong string for no reason at all.
    """
    out = []
    for cls in DATE_CARRIER_CLASSES:
        pattern = r'<(div|p|span)\s[^>]*class="[^"]*\b' + re.escape(cls) + r'\b[^"]*"[^>]*>(.*?)</\1>'
        for m in re.finditer(pattern, html, re.S):
            out.append((m.start(), re.sub(r"<[^>]+>", " ", m.group(2))))
    return out


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "web" / "dist"
    if not dist.is_dir():
        print(f"qa_date_identity: FAIL — no dist at {dist}")
        return 1

    dates, approved = read_frontmatter_dates()
    if approved <= 0:
        print("qa_date_identity: FAIL — could not read a date out of every approved piece.")
        return 1

    failures: list[str] = []
    article_pages = 0
    listing_pairs = 0
    declared_rows: list[tuple[str, str, str]] = []

    for page in sorted(dist.rglob("index.html")):
        rel = page.relative_to(dist).as_posix()
        html = page.read_text(encoding="utf-8", errors="replace")
        arabic = rel.startswith("ar/")
        rx = AR_DATE_RE if arabic else EN_DATE_RE

        art = re.match(r"(?:ar/)?articles/([^/]+)/index\.html$", rel)
        found = carriers(html)

        if art:
            slug = art.group(1)
            if slug not in dates:
                failures.append(f"{rel}: served an article page for a slug no approved piece declares")
                continue
            y, mo, d = dates[slug]
            want = expected_ar(y, mo, d) if arabic else expected_en(y, mo, d)
            printed = [s for _, txt in found for s in rx.findall(txt)]
            if not printed:
                failures.append(f"{rel}: no date printed in any date carrier — the page lost its dateline")
                continue
            article_pages += 1
            for got in printed:
                if got != want:
                    failures.append(f"{rel}: prints {got!r}, frontmatter says {want!r}")
            continue

        # A listing surface. Pair each carrier with the link above it.
        for off, txt in found:
            href = ANY_HREF_RE.findall(html[:off])
            nearest = href[-1] if href else ""
            slug_m = ARTICLE_HREF_RE.search(nearest)
            if not slug_m:
                # Not an article row. The editions index carries exactly one such
                # row — the VALENCE standing instrument, served from public/ with
                # a hand-written "August 2026" and no frontmatter to agree with
                # (08-17 orphan audit; the Arabic editions index still has no
                # VALENCE row, which is an open editorial question, not a defect).
                # Named rather than skipped, so a SECOND unfrontmattered date row
                # cannot arrive unnoticed behind this exemption.
                if nearest in DECLARED_NON_ARTICLE_ROWS:
                    declared_rows.append((rel, nearest, txt.strip()))
                    if not txt.strip():
                        failures.append(f"{rel}: the {nearest} listing row prints no date at all")
                else:
                    failures.append(
                        f"{rel}: a date carrier at offset {off} sits beside {nearest or 'no link'}, "
                        f"which is neither an article nor a declared standing row"
                    )
                continue
            printed = rx.findall(txt)
            if not printed:
                # NOT a skip. A date carrier that yields nothing this check can
                # read is the silent-pass trap: the first draft of this file
                # skipped such carriers, and the Latin-digits-in-Arabic bite —
                # the real 09-21 defect, nine browse pages for seven days —
                # walked straight through it while the total quietly dropped by
                # one and the tool still printed PASS.
                failures.append(
                    f"{rel}: a date carrier at offset {off} prints "
                    f"{txt.strip()[:60]!r}, which is not a date in this page's language"
                )
                continue
            slug = slug_m.group(1)
            if slug not in dates:
                failures.append(f"{rel}: links {slug}, which no approved piece declares")
                continue
            y, mo, d = dates[slug]
            want = expected_ar(y, mo, d) if arabic else expected_en(y, mo, d)
            listing_pairs += 1
            for got in printed:
                if got != want:
                    failures.append(f"{rel}: {slug} listed as {got!r}, frontmatter says {want!r}")

    if article_pages != approved:
        failures.append(
            f"non-vacuity: {article_pages} article pages carried a dateline against "
            f"{approved} approved pieces on disk — the populations must match by name"
        )
    if listing_pairs == 0:
        failures.append("non-vacuity: zero listing dates were paired with an article; this check read nothing")
    if len(declared_rows) != 1:
        failures.append(
            f"non-vacuity: {len(declared_rows)} declared standing rows carried a date, expected exactly 1 "
            f"(the VALENCE row on the English editions index)"
        )

    if failures:
        print(f"qa_date_identity: FAIL — {len(failures)} finding(s).")
        for f in failures[:40]:
            print(f"  ✗ {f}")
        if len(failures) > 40:
            print(f"  … and {len(failures) - 40} more")
        print(
            "  A rendered date that disagrees with its frontmatter means the formatter "
            "resolved the value against something other than the zone it was parsed in."
        )
        return 1

    print(
        f"qa_date_identity: PASS — {article_pages} article datelines and {listing_pairs} "
        f"listing dates all agree with their own frontmatter, in both languages, "
        f"with Arabic in Arabic-Indic digits. The rendered day is a function of the "
        f"date field, not of the build machine's clock. "
        f"{len(declared_rows)} declared standing row carries a date with no frontmatter behind it."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
