#!/usr/bin/env python3
"""
build_font_bundle.py — mirror the Google Fonts css2 response into a self-hosted,
same-origin font bundle under web/public/fonts/.

WHY THIS EXISTS, and why it is a mirror rather than a hand-written stylesheet.

Until 2026-10-08 `Base.astro` carried two `preconnect` hints and one stylesheet
`<link>` to `fonts.googleapis.com`, so every one of the 120 served pages made
three requests to origins we do not own before a reader saw a word — 360
third-party references, counted 2026-09-18 in
`agents/growth/2026-09-18-third-party-surface-audit.md` and filed as a P1 that
then sat on the standing queue for twenty days.

The migration is a **mirror**, deliberately, because the one thing that must not
change is the rendering. Google's css2 response is not a list of five fonts; it
is 73 `@font-face` blocks over 34 distinct woff2 files, carved into
`unicode-range` subsets so a Latin-only page never downloads the Arabic cut.
Hand-writing five `@font-face` rules would have been shorter and would have
silently shipped the whole Arabic face to every English reader — a performance
regression dressed as a privacy fix. So this script:

  1. fetches the exact css2 URL the layout used to carry, with a Chrome UA so
     the response is woff2 rather than ttf;
  2. downloads every distinct file it names, byte-for-byte;
  3. renames each to a deterministic, readable name derived from the family,
     style, weight set and subset — Google's own names are content hashes and
     carry no meaning;
  4. re-emits the stylesheet with the SAME family names, styles, weights,
     unicode-ranges and `font-display`, pointing at `./<name>.woff2`.

`url()` is RELATIVE on purpose. The bundle is served from `<base>/fonts/`, so a
relative reference resolves under any base, and the site's base string keeps
exactly one home (`withBase`, src/lib/urls.ts) instead of being copied into a
stylesheet where nothing would ever check it.

Re-run to refresh the faces. It is not a build step and not an assertion: it
writes into `web/public/`, and a tool that rewrites served bytes on every build
is the opposite of a gate. The assertion that *guards* this work is
`qa_third_party_origins.py`.

Usage:
    python3 agents/tools/build_font_bundle.py            # writes web/public/fonts/
    python3 agents/tools/build_font_bundle.py --dry-run  # report, write nothing
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys
import urllib.request

CSS2_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500"
    "&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500"
    "&family=JetBrains+Mono:wght@400;500"
    "&family=Amiri:ital,wght@0,400;0,700;1,400"
    "&family=Cairo:wght@400;500;600;700"
    "&display=swap"
)

# A Chrome UA is required: the css2 endpoint content-negotiates on User-Agent and
# serves ttf to anything it does not recognise. urllib's default UA gets ttf.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT_DIR = ROOT / "web" / "public" / "fonts"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse(css: str):
    """One record per @font-face block, in source order.

    The subset name is carried only in a CSS comment *immediately before* each
    block (`/* arabic */`) — the sole place Google states it — so the comment is
    read backwards from the block's own start offset rather than carried forward
    across the scan. The first draft of this function carried it forward and
    produced names shifted by one: an `amiri-italic-400-latin-ext` holding
    U+0000-00FF, which is latin. A filename is a claim like any other.

    A block with no preceding comment is named `sN` by position, so an unnamed
    subset still gets a stable filename rather than a collision.
    """
    out = []
    for i, m in enumerate(re.finditer(r"@font-face\s*\{(.*?)\}", css, re.S)):
        body = m.group(1)
        fam = re.search(r"font-family:\s*'([^']+)'", body)
        url = re.search(r"url\((https://[^)]+)\)", body)
        if not (fam and url):
            continue
        sty = re.search(r"font-style:\s*([^;]+);", body)
        wgt = re.search(r"font-weight:\s*([^;]+);", body)
        rng = re.search(r"unicode-range:\s*([^;]+);", body)
        dsp = re.search(r"font-display:\s*([^;]+);", body)
        before = re.findall(r"/\*\s*([a-z0-9\-\[\]]+)\s*\*/", css[: m.start()])
        out.append(
            {
                "family": fam.group(1),
                "style": sty.group(1).strip() if sty else "normal",
                "weight": wgt.group(1).strip() if wgt else "400",
                "url": url.group(1),
                "range": rng.group(1).strip() if rng else None,
                "display": dsp.group(1).strip() if dsp else "swap",
                "subset": before[-1] if before else f"s{i}",
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"build_font_bundle — fetching css2 with a Chrome UA")
    css = fetch(CSS2_URL).decode("utf-8")
    recs = parse(css)
    if not recs:
        print("FAIL — no @font-face blocks parsed out of the css2 response.")
        return 1

    # One filename per distinct remote file. A variable font is served once and
    # declared at several weights, so the same URL legitimately appears in
    # several blocks; the name must therefore carry the *set* of weights.
    weights: dict[str, set[str]] = {}
    for r in recs:
        weights.setdefault(r["url"], set()).add(r["weight"])

    # A distinct file must describe a distinct coverage. If one URL turned up
    # under two different unicode-ranges, or two files claimed the same name, the
    # mirror would be wrong in exactly the way a filename cannot show — so both
    # are asserted rather than assumed.
    ranges: dict[str, set] = {}
    for r in recs:
        ranges.setdefault(r["url"], set()).add(r["range"])
    bad = {u: v for u, v in ranges.items() if len(v) > 1}
    if bad:
        print(f"FAIL — {len(bad)} file(s) served under more than one unicode-range.")
        return 1

    names: dict[str, str] = {}
    for r in recs:
        if r["url"] in names:
            continue
        ws = sorted(weights[r["url"]], key=lambda x: int(re.sub(r"\D", "", x) or 0))
        wtag = ws[0] if len(ws) == 1 else f"{ws[0]}-{ws[-1]}var"
        names[r["url"]] = (
            f"{slug(r['family'])}-{r['style']}-{wtag}-{slug(r['subset'])}.woff2"
        )
    if len(set(names.values())) != len(names):
        print("FAIL — two distinct files resolved to the same filename.")
        return 1

    print(
        f"  {len(recs)} @font-face block(s) over {len(names)} distinct file(s), "
        f"{len({r['family'] for r in recs})} famil(ies)"
    )

    if args.dry_run:
        for u, n in sorted(names.items(), key=lambda kv: kv[1]):
            print(f"    {n:<52} <- {u.rsplit('/', 1)[-1]}")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total = 0
    for u, n in sorted(names.items(), key=lambda kv: kv[1]):
        blob = fetch(u)
        if blob[:4] != b"wOF2":
            print(f"FAIL — {n} is not woff2 (magic {blob[:4]!r}); UA negotiation changed.")
            return 1
        (OUT_DIR / n).write_bytes(blob)
        total += len(blob)
        print(f"    {len(blob):>7,}  {n}  sha256:{hashlib.sha256(blob).hexdigest()[:12]}")

    header = f"""/* Madār — self-hosted web fonts. GENERATED by agents/tools/build_font_bundle.py.
   Do not hand-edit: re-run the generator.

   A mirror of the Google Fonts css2 response the layout carried until
   2026-10-08, with the SAME families, styles, weights, unicode-ranges and
   font-display, and with every url() pointing at this directory. The subsetting
   is preserved on purpose — {len(names)} files rather than {len({r['family'] for r in recs})},
   so an English page does not download the Arabic cut.

   url() is relative, so the bundle resolves under any site base and the base
   string keeps its single home in src/lib/urls.ts.

   Licences. All five families are under the SIL Open Font License 1.1, whose
   section 2 requires the copyright notice and the licence to travel with the
   font. Each upstream notice is served verbatim beside the faces it covers,
   copied from the same repository the files came from and not paraphrased:

     ./licences/Amiri-OFL.txt              Copyright 2010-2022 The Amiri Project Authors
     ./licences/Cairo-OFL.txt              Copyright 2009 The Cairo Project Authors
     ./licences/CormorantGaramond-OFL.txt  Copyright 2015 the Cormorant Project Authors
     ./licences/JetBrainsMono-OFL.txt      Copyright 2020 The JetBrains Mono Project Authors
     ./licences/Newsreader-OFL.txt         Copyright 2020 The Newsreader Project Authors

   This stylesheet is their inbound path: the licences are not pages, they are
   files that must accompany these bytes, so they are deliberately NOT added to
   sitemap customPages — the same disposition the served manifest got on
   2026-10-06, and for the same reason (08-17's orphan rule is about pages a
   reader should find, not about every byte in public/). */

"""
    blocks = []
    for r in recs:
        lines = [
            "@font-face {",
            f"  font-family: '{r['family']}';",
            f"  font-style: {r['style']};",
            f"  font-weight: {r['weight']};",
            f"  font-display: {r['display']};",
            f"  src: url('./{names[r['url']]}') format('woff2');",
        ]
        if r["range"]:
            lines.append(f"  unicode-range: {r['range']};")
        lines.append("}")
        blocks.append(f"/* {r['family']} · {r['style']} {r['weight']} · {r['subset']} */\n" + "\n".join(lines))

    (OUT_DIR / "madar-fonts.css").write_text(header + "\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"  wrote {len(names)} woff2 ({total:,} bytes) + madar-fonts.css")
    return 0


if __name__ == "__main__":
    sys.exit(main())
