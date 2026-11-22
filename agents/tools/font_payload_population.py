#!/usr/bin/env python3
"""
font_payload_population — the corpus-wide reading of what a reader actually
downloads in webfonts, and of every fetch that pays for fewer than N painted
characters.

THIS IS A MEASUREMENT AND A REGISTER MAINTAINER, NOT AN ASSERTION. It carries no
`qa_` prefix, so it is outside the `qa_*.py` glob `qa_patch_queue` counts and no
gate ratio in this repository moves because it exists. It fails no build. The
reason is #93's floor, already written into `qa_font_payload`'s own header: the
reductions this measurement argues for are out of one lane's reach, so a ceiling
above today's reality would red every build until somebody else's work landed.
*Assert the shape, print the size.*

WHY IT EXISTS AT ALL, WHEN ASSERTION 39 ALREADY MEASURES THIS.

`qa_font_payload` probes **six** fixed pages and says so in its header — "it is a
sample and it says so". Standing-queue item 123 is open on exactly that
property: a fixed probe set declares a population a reader infers from a green
light. Standing-queue item **117** — the 2026-11-15 weekly review's growth bet —
asked for the other number: the same quantity over the whole served corpus,
*with the worst page named*.

The bet was set on the technique `qa_selector_coverage` uses — one browser
launch over `DOMParser` for 135 documents in 1.9 s — and **that technique cannot
answer this question.** A parsed document has no network and no layout, and a
woff2 file is transferred only when a layout engine must paint a glyph out of
it. So the population has to be *rendered*, once each, with its requests logged.
Measured rather than assumed: 143 documents in **81 seconds**, which is cheap
enough to re-read every week and far too slow for a build step.

METHOD — and the method is *reuse*, deliberately.

This script imports `qa_font_payload` and replaces exactly one name: `PAGES`.
The `@font-face` parser, the `unicode-range` carve, the painted-run probe, the
Arabic block table and the request log are the gate's own code. Nothing about
the measurement is reimplemented, so this reading and the gate's reading cannot
disagree about method — only about population. That is the whole point: when the
two disagree, the difference IS the sample's error, and it is attributable.

Usage:
    python3 agents/tools/font_payload_population.py .                  # read
    python3 agents/tools/font_payload_population.py . --threshold 5    # default
    python3 agents/tools/font_payload_population.py . --json out.json

Exit 0 = the reading was taken. Exit 2 = it could not be taken (no dist, no
Chrome, no font stylesheet) — never silently green, because a measurement that
reports nothing reads exactly like a corpus with nothing to report.
"""

from __future__ import annotations

import collections
import contextlib
import importlib.util
import io
import json
import pathlib
import re
import sys

PAGE_RE = re.compile(
    r"^\s{2}(\S.*?)\s{2,}([\d,]+) bytes over (\d+) file\(s\)\s+(\S+)\s*$")
FILE_RE = re.compile(
    r"^\s+([\d,]+)\s+(\S+\.woff2)\s+(\d+) chars\s+([\d,]+) b/char\s*$")


def die(msg: str) -> int:
    print("REFUSED font_payload_population — %s" % msg)
    return 2


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = pathlib.Path(args[0] if args else ".").resolve()
    threshold = 5
    if "--threshold" in sys.argv:
        threshold = int(sys.argv[sys.argv.index("--threshold") + 1])
    json_out = None
    if "--json" in sys.argv:
        json_out = pathlib.Path(sys.argv[sys.argv.index("--json") + 1])

    dist = root / "web" / "dist"
    if not dist.is_dir():
        return die("no built site at %s — this reading needs a render, not a parse" % dist)

    tool = root / "agents" / "tools" / "qa_font_payload.py"
    if not tool.is_file():
        return die("assertion 39 is not on disk at %s, and this script is its population half" % tool)
    spec = importlib.util.spec_from_file_location("qa_font_payload_mod", tool)
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)

    pages = [(p.relative_to(dist).as_posix(), p.relative_to(dist).as_posix())
             for p in sorted(dist.rglob("*.html"))]
    if not pages:
        return die("0 html documents under %s" % dist)
    sample = len(gate.PAGES)
    gate.PAGES = pages

    argv_keep = sys.argv
    sys.argv = ["qa_font_payload", str(dist), "--report"]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            gate.main()
    finally:
        sys.argv = argv_keep
    raw = buf.getvalue()

    cur, data = None, collections.OrderedDict()
    for line in raw.split("\n"):
        m = PAGE_RE.match(line)
        if m:
            cur = m.group(4)
            data[cur] = {"bytes": int(m.group(2).replace(",", "")), "files": []}
            continue
        m = FILE_RE.match(line)
        if m and cur:
            data[cur]["files"].append(
                (int(m.group(1).replace(",", "")), m.group(2), int(m.group(3))))

    if len(data) != len(pages):
        return die("parsed %d page blocks out of %d rendered — the gate's report "
                   "format moved and this reader did not follow it"
                   % (len(data), len(pages)))

    total = sum(v["bytes"] for v in data.values())
    by_face, by_page, instances = collections.Counter(), collections.Counter(), 0
    zero = []
    for url, v in data.items():
        for size, face, painted in v["files"]:
            if painted == 0:
                zero.append((url, face, size))
            if painted < threshold:
                by_face[face] += size
                by_page[url] += size
                instances += 1
    waste = sum(by_face.values())

    print("font_payload_population — the corpus reading, rendered rather than parsed")
    print("  documents rendered ......... %d of %d served .html in dist" % (len(data), len(pages)))
    print("  assertion 39's sample ...... %d page(s) — this reading is %.1fx that population"
          % (sample, len(data) / sample))
    print("  corpus font payload ........ {:,} bytes, summed over every document".format(total))
    print("     NOT a page weight and NOT a download: a reader who visits one page pays")
    print("     that page's line, and the sum is the corpus's exposure, not anyone's bill.")
    print("  fetches painting < %d chars . %d fetch(es), {:,} bytes, %.1f%% of the corpus payload"
          .format(waste) % (threshold, instances, 100.0 * waste / total if total else 0.0))
    print("  pages carrying one ......... %d of %d" % (len(by_page), len(data)))
    print("  fetches painting ZERO ...... %d  (assertion 39 limb 2's subject, asserted on the sample "
          "and now read on the population)" % len(zero))
    for url, face, size in zero:
        print("      DEAD FETCH  %-56s %s" % (face, url))

    print("\n  by face — every fetch that paints fewer than %d characters:" % threshold)
    for face, b in by_face.most_common():
        print("      {:>12,}  {}".format(b, face))

    print("\n  worst pages:")
    for url, b in by_page.most_common(8):
        detail = [(s, f, c) for s, f, c in data[url]["files"] if c < threshold]
        worst = max(detail, key=lambda t: t[0] / max(t[2], 1))
        print("      {:>10,}  {:<46} {:,} b/char on {}".format(
            b, url, worst[0] // max(worst[2], 1), worst[1]))

    if json_out:
        json_out.write_text(json.dumps({
            "documents": len(data), "threshold": threshold,
            "corpus_payload_bytes": total, "waste_bytes": waste,
            "waste_fetches": instances, "pages_affected": len(by_page),
            "dead_fetches": len(zero),
            "by_face": dict(by_face), "worst_pages": by_page.most_common(12),
        }, indent=1), encoding="utf-8")
        print("\n  written .................... %s" % json_out)

    print("\nREAD font_payload_population — the reading was taken over the whole population. "
          "Nothing here is asserted (#93).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
