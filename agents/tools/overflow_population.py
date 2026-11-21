#!/usr/bin/env python3
"""
overflow_population.py — WHO OVERFLOWS, AND AT WHAT WIDTH. A MEASUREMENT, NOT AN
ASSERTION.

Standing-queue item 47 (raised 2026-10-27, taken as the head 2026-11-21 at 25 days)
asked one question in two halves and forbade building anything before answering it:

  (a) **The only overflow gate this operation owns reads the artefacts, never the
      publication.** `qa_artefact_render` is the one tool of the forty-three in
      which `scrollWidth`/`clientWidth` appear at all, and its scope is
      `agents/briefs` and `agents/reviews`. So the pages a READER is served — two
      scripts, one of them RTL, with the longest unbreakable tokens in the corpus
      sitting in `<code>` inside article bodies — have never been measured for
      overflow at any width.

  (b) **`VIEWPORT = 1280`, one number, and an assertion with a parameter is an
      assertion about that parameter's value.** A layout correct at 1280 and
      broken at 390 is invisible to the gate, and the founder opens the brief on
      whatever is in his hand.

      How many of the served pages overflow at 1280?
      How many of the artefacts overflow at 390?

**This file has no `qa_` prefix and is outside the counting glob** (`qa_*.py`), so
no count in `CLAUDE.md` moves. That is deliberate and it is item 47's own
instruction: *measure both before building anything.* A floor chosen above today's
reality reds every build (#93); a floor chosen below it is a floor nobody set. The
number has to exist before the gate can.

**The oracle is borrowed verbatim from `qa_artefact_render`, including its known
blind spot, because a measurement that uses a DIFFERENT oracle from the gate it is
sizing cannot be compared with it.** That tool's own header records the finding:
Chrome does not report inline-direction TEXT overflow in `scrollWidth` on an
`overflow: visible` box, so this measures *boxes that escape their container*, not
*text wider than its column*. Reported here in the same words it is reported there,
so nobody reads a 0 as "nothing is wide."

One Chrome launch, one DOM dump, all targets loaded in turn into a single iframe.

  python3 agents/tools/overflow_population.py .                 # both halves
  python3 agents/tools/overflow_population.py . --widths 1280,390
"""

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qa_artefact_render as AR  # the oracle, borrowed rather than re-written

ARTEFACT_FAMILIES = ("agents/briefs", "agents/reviews")
TOL = AR.OVERFLOW_TOL


def probe(browser, root, urls, viewport):
    """qa_artefact_render's own harness, with the viewport as a parameter."""
    harness = (
        AR.HARNESS.replace("__TARGETS__", json.dumps(urls))
        .replace("__VIEWPORT__", str(viewport))
        .replace("__IFH__", str(AR.IFRAME_HEIGHT))
        .replace("__TOL__", str(TOL))
    )
    import re
    import subprocess
    import tempfile

    httpd = AR.serve(root, harness.encode("utf-8"))
    port = httpd.server_address[1]
    try:
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [browser, "--headless=new", "--disable-gpu", "--no-sandbox",
                 "--hide-scrollbars", f"--user-data-dir={profile}",
                 "--virtual-time-budget=240000",
                 "--window-size=%d,900" % viewport, "--dump-dom",
                 f"http://127.0.0.1:{port}/__qa_harness__"],
                capture_output=True, text=True, timeout=900,
            )
    finally:
        httpd.shutdown()
    if "QA-DONE" not in proc.stdout:
        raise RuntimeError(
            "the probe did not finish — measuring nothing and reporting it as "
            "clean is the defect this measurement exists to size.\n%s"
            % proc.stderr[-800:])
    m = re.search(r'<pre id="out">(.*?)</pre>', proc.stdout, re.S)
    if not m:
        raise RuntimeError("no result block in the dumped DOM")
    return json.loads(
        m.group(1).replace("&lt;", "<").replace("&gt;", ">")
        .replace("&quot;", '"').replace("&amp;", "&"))


def report(label, root, rels, viewport, browser):
    urls = ["/" + r for r in rels]
    rows = probe(browser, root, urls, viewport)
    bad = []
    errs = []
    for r in rows:
        if r.get("error"):
            errs.append((r.get("url"), r["error"]))
            continue
        doc_over = r.get("docOverflow", 0)
        el_over = r.get("overflow", [])
        if doc_over > TOL or el_over:
            bad.append((r["url"], doc_over, el_over))
    print("  %-24s %4d page(s) at %dpx — %d overflowing, %d unreadable"
          % (label, len(rows), viewport, len(bad), len(errs)))
    for url, doc_over, els in sorted(bad, key=lambda x: -max(
            [x[1]] + [e["over"] for e in x[2]])):
        worst = max([doc_over] + [e["over"] for e in els])
        print("      %-62s worst %+dpx" % (url[:62], worst))
        if doc_over > TOL:
            print("          document %dpx wider than the %dpx viewport"
                  % (doc_over, viewport))
        for e in els[:3]:
            print("          <%s class=%r> %+dpx past a %dpx box · %s"
                  % (e["tag"], e["cls"], e["over"], e["client"],
                     e["text"][:46]))
    for url, e in errs:
        print("      UNREADABLE %s — %s" % (url, e))
    return len(rows), len(bad), len(errs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--widths", default="1280,390",
                    help="comma-separated viewport widths (default 1280,390)")
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    widths = [int(w) for w in a.widths.split(",")]
    browser = AR.find_browser()
    if not browser:
        print("REFUSED overflow_population — no headless Chrome on this machine.")
        return 4

    dist = root / "web" / "dist"
    served = sorted(
        str(p.relative_to(dist)) for p in dist.rglob("*.html")
    ) if dist.is_dir() else []
    # the gate's own target list, read rather than re-derived (item 123 limb 2)
    artefacts = [str(p.relative_to(root)) for p in AR.collect(root)]

    print("overflow_population — item 47, both halves. MEASURED, NOT ASSERTED.")
    print("  oracle .......... qa_artefact_render's own probe, borrowed verbatim")
    print("  blind spot ...... scrollWidth is silent on inline-direction TEXT")
    print("                    overflow in an overflow:visible box. What is")
    print("                    measured is a BOX escaping its container. A 0")
    print("                    here does not mean nothing is wide (#28).")
    print("  tolerance ....... %dpx" % TOL)
    print()
    totals = {}
    for w in widths:
        print("THE PUBLICATION — web/dist, never measured for this before today")
        totals[("served", w)] = report("served pages", dist, served, w, browser) \
            if served else (0, 0, 0)
        print("THE FOUNDER-FACING ARTEFACTS — the gate's own corpus, at %dpx" % w)
        totals[("artefacts", w)] = report("artefacts", root, artefacts, w, browser)
        print()
    print("SUMMARY")
    for (fam, w), (n, bad, err) in sorted(totals.items()):
        print("  %-10s @%-5d %3d of %3d overflowing (%d unreadable)"
              % (fam, w, bad, n, err))
    return 0


if __name__ == "__main__":
    sys.exit(main())
