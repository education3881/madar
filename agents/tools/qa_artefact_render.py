#!/usr/bin/env python3
"""
qa_artefact_render.py — standing assertion 33: the FOUNDER-FACING artefact renders.

The 2026-08-23 perimeter rule put the briefs, the weekly reviews and the memos in
scope, because the brief is the one page the founder actually opens and it had
rendered edge-to-edge for two days while the publication was checked six ways.
Three things have been asserted about those artefacts since: that they **exist**,
that they carry a **container**, and (from 2026-10-12) that they **contact nobody**.
All three are properties of the markup. **None is a property of the render.**

Standing-queue item 12 named the two bites, and both were already in hand:

  A  THE TAIL RENDERS      2026-10-12: the daily brief stopped dead after the
                           statistics panel. The pasted panel carried the first
                           line of the generator's CSS comment block — an HTML
                           comment opened and never closed — which swallowed the
                           Tomorrow section, the forward question and the footer.
                           It passed every structural count the artefact has (one
                           `main`, one `/main`, one `/body`, one `/html`, panel
                           once, panel CSS once), because **an unclosed comment
                           does not overflow a container, it deletes it.**

  B  NOTHING OVERFLOWS     2026-05-28: Brief No. 01 has rendered with its
                           right-hand column one word wide for 137 days, because
                           a 44-character unbreakable path in a `<code>` element
                           blows out the left column of that brief's two-column
                           grid. Found by screenshotting it for an unrelated
                           reason. 76 of the 79 briefs carrying `<code>` tokens
                           carry one of 28+ characters, and whether each visibly
                           breaks depends on its container — which nothing had
                           ever asked.

**Assertion A is NOT "the artefact has a `<footer>`", and the item's own wording is
corrected here rather than implemented as written.** Item 12 specified *every
founder-facing artefact renders its own footer*. Counted over the corpus: **113 of
127 artefacts carry a `<footer>` element** and the newest brief and newest weekly
review are both in the fourteen that do not — they end in a styled `div`. An
assertion written to the item's letter would have failed on correct artefacts and
been switched off inside a week (#35). The property that actually matters is
template-agnostic and is what the 10-12 defect violated: **the document renders to
its own end.** The oracle is the source file's own tail — strip the markup, take
the last visible characters, and require them in the rendered `body.textContent`.
A file is compared only against itself, so no template is privileged.

**Why a render and not a parse.** Python's `html.parser` recovers from an unclosed
comment differently from a browser, and the browser is the consumer: the founder
opens this in Chrome. The DOM measured here is the DOM he gets.

Scope: `agents/briefs/*.html` and `agents/reviews/*.html` — the two artefact
families the CHARTER names as the proof-of-work contract. The quarantined desktop
runner's orphans are excluded by name: they are a record of a run that failed, not
an artefact rendered for anybody.

Dependencies: Python 3 standard library plus a headless Chrome/Chromium on PATH —
the same single dependency qa_render.py takes, for the same reason. If no browser
is found this exits 1 rather than skipping: a check that silently does not run is a
green light wired to nothing (RUNBOOK, 2026-09-13).

Usage:
    python3 agents/tools/qa_artefact_render.py .            # assert
    python3 agents/tools/qa_artefact_render.py . --report   # measure, exit 0
    python3 agents/tools/qa_artefact_render.py . --only 2026-10-18

Exit codes: 0 = clean · 1 = a founder-facing artefact does not render · 2 = cannot
measure (no browser, no corpus).
"""

import argparse
import functools
import html.parser
import http.server
import json
import pathlib
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading

VIEWPORT = 1280          # the width every brief render inspection in the record used
IFRAME_HEIGHT = 3000
TEXT_FLOOR = 0.90        # share of the source's visible text the render must carry
OVERFLOW_TOL = 2         # px; sub-pixel rounding in a 1280-wide layout is not a defect

BROWSERS = (
    "google-chrome-stable",
    "google-chrome",
    "chromium-browser",
    "chromium",
)

FAMILIES = ("agents/briefs", "agents/reviews")

# --- the overflow baseline, and why this check has one ------------------------
# Assertion A (the tail renders) is clean on all 127 artefacts, so it gates the
# whole corpus with nothing excused. Assertion B is not: **25 of 127 artefacts
# overflow at 1280px**, measured 2026-10-19 when this tool was built, and every
# one of them is historical. Two mechanisms, both diagnosed rather than guessed:
#
#   * SEVEN briefs (2026-08-10 → 08-18) render the founder's copy-paste push
#     block in `<pre class="push">` with `white-space: pre`, and the shell line
#     `cd "/Users/vini/Documents/..." && git add -A && …` does not wrap. Those
#     documents are **7,277 to 34,254 px wider than the viewport** — the worst
#     layout defect in the operation's record, in the artefact the CHARTER names
#     as the proof-of-work contract, unseen for 62 days.
#   * SEVENTEEN briefs (2026-05-28 → 06-17) and ONE review set `li { display:
#     grid; grid-template-columns: 1.5rem 1fr }` for a hanging bullet. **Grid
#     blockifies its children**, so a `<strong>`, `<code>` or `<span class=mono>`
#     written inline inside such an `<li>` becomes its own grid item and is
#     auto-placed into the 24px bullet column, where its text overflows by 11 to
#     190 px. This is Brief No. 01's "right-hand column one word wide" (item 12),
#     and the mechanism is the same in all eighteen.
#
# **Measurement B is PRINTED AND DELIBERATELY NOT ASSERTED, and the reason is a
# finding rather than a caveat.** The two mechanisms above were found by this
# probe. But when the SAME shape was injected fresh into a clean brief during the
# proof — a `white-space: pre` paragraph carrying the 100-character push command —
# **the probe did not bite.** Measured on the injected element: `scrollWidth` and
# `clientWidth` both returned 1028 for text far wider than 1028px, and
# `documentElement.scrollWidth` stayed at the 1280px viewport. **Chrome does not
# report inline-direction text overflow in `scrollWidth` on an `overflow: visible`
# block.** The 25 artefacts below were caught because their overflow is a GRID
# ITEM escaping its column, which `scrollWidth` does report, and because in seven
# of them it propagated to the document. So the instrument finds a real defect
# class and its sensitivity to the class it was commissioned for is **unknown**.
# A check that cannot be shown to fail on the defect it exists to catch does not
# gate a build (CLAUDE.md, non-negotiables: *prove an assertion both ways*). It
# reports, with its blind spot printed beside its findings, exactly as
# `qa_third_party_origins` prints `<a href>` and `og:image` without asserting
# them. The correct oracle is a Range rectangle rather than `scrollWidth`, and it
# is **standing-queue item 28**.
#
# The 25 are listed rather than counted, because a count with no membership list
# is this operation's oldest recurring defect (#57, and the three instances the
# 2026-10-18 review found in one week).
OVERFLOW_BASELINE = {
    # the push-block seven — document wider than the viewport
    "agents/briefs/2026-08-10-daily-brief.html",
    "agents/briefs/2026-08-11-daily-brief.html",
    "agents/briefs/2026-08-12-daily-brief.html",
    "agents/briefs/2026-08-13-daily-brief.html",
    "agents/briefs/2026-08-16-daily-brief.html",
    "agents/briefs/2026-08-17-daily-brief.html",
    "agents/briefs/2026-08-18-daily-brief.html",
    # the blockified-inline nineteen — inline content auto-placed into a 24px column
    "agents/briefs/2026-05-28-daily-brief.html",
    "agents/briefs/2026-05-29-daily-brief.html",
    "agents/briefs/2026-05-31-daily-brief.html",
    "agents/briefs/2026-06-01-daily-brief.html",
    "agents/briefs/2026-06-03-daily-brief.html",
    "agents/briefs/2026-06-04-daily-brief.html",
    "agents/briefs/2026-06-05-daily-brief.html",
    "agents/briefs/2026-06-06-daily-brief.html",
    "agents/briefs/2026-06-08-daily-brief.html",
    "agents/briefs/2026-06-09-daily-brief.html",
    "agents/briefs/2026-06-10-daily-brief.html",
    "agents/briefs/2026-06-11-daily-brief.html",
    "agents/briefs/2026-06-12-daily-brief.html",
    "agents/briefs/2026-06-14-daily-brief.html",
    "agents/briefs/2026-06-15-daily-brief.html",
    "agents/briefs/2026-06-16-daily-brief.html",
    "agents/briefs/2026-06-17-daily-brief.html",
    "agents/reviews/2026-09-20-weekly-review.html",
}


def find_browser():
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return path
    return None


def source_text(path):
    """
    The visible text of a source file, read COMMENT-NAIVELY and on purpose.

    **This function was rewritten during its own proof and the first version is
    worth recording, because it was wrong in the most dangerous way available.**
    It used `html.parser`, whose recovery from an unclosed comment is the same as
    a browser's: it swallowed the rest of the document too. So the expected tail
    and the rendered tail agreed perfectly, the bite passed, and the check read
    green on the exact defect it was written for. **The oracle was reading its
    answer off the broken artefact** — the 2026-09-14 trap on the input side
    (*where does the string I am looking for also legitimately appear?*), and
    the reason the RUNBOOK says to prove the bite as carefully as the control.

    So: strip script and style bodies, strip properly-closed comments, then strip
    tags. An UNCLOSED comment is deliberately not honoured — it eats one tag's
    worth of characters and the rest of the document's text survives, which is
    the asymmetry the assertion needs. A browser cannot be naive here; a ruler
    must be.
    """
    s = path.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?is)<script\b.*?</script\s*>", " ", s)
    s = re.sub(r"(?is)<style\b.*?</style\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)          # closed comments only
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-zA-Z#0-9]+;", "x", s)
    return re.sub(r"\s+", " ", s).strip()


# --- the probe ----------------------------------------------------------------
# One Chrome launch, one DOM dump. Each artefact is loaded in turn into a single
# iframe sized to the stated viewport, measured, and removed, so 127 artefacts
# cost one browser rather than 127.

HARNESS = """<!doctype html>
<html><head><meta charset="utf-8"><title>QA-RUNNING</title></head>
<body style="margin:0"><pre id="out"></pre>
<script>
const TARGETS = __TARGETS__;
const VIEWPORT = __VIEWPORT__;
const TOL = __TOL__;

function measure(doc) {
  const res = {tail: "", overflow: [], docOverflow: 0, elements: 0, comments: 0};
  if (!doc || !doc.body) { res.error = "no document"; return res; }
  // innerText, NOT textContent: textContent includes the text inside a
  // <script> element, so an unclosed <script> that swallows the rest of the
  // document reads LONGER than the source. Measured at 117.8% during the
  // proof. innerText is what a reader sees, which is what is being asserted.
  const t = (doc.body.innerText || doc.body.textContent || "").replace(/\\s+/g, " ").trim();
  res.tail = t.slice(-400);
  res.textLen = t.length;
  res.docOverflow = doc.documentElement.scrollWidth - VIEWPORT;
  // a comment node carrying a closing tag means markup was swallowed by it
  const walker = doc.createTreeWalker(doc, NodeFilter.SHOW_COMMENT);
  while (walker.nextNode()) {
    if (/<\\//.test(walker.currentNode.nodeValue || "")) res.comments++;
  }
  const all = doc.body.querySelectorAll("*");
  res.elements = all.length;
  for (const el of all) {
    const over = el.scrollWidth - el.clientWidth;
    if (over <= TOL) continue;
    const cs = doc.defaultView.getComputedStyle(el);
    // an element that declares its own scrolling is not overflowing, it is scrolling
    if (cs.overflowX !== "visible") continue;
    if (cs.display === "inline") continue;   // inline boxes report their line box
    res.overflow.push({
      tag: el.tagName.toLowerCase(),
      cls: (el.className || "").toString().slice(0, 40),
      over: over,
      disp: cs.display,
      client: el.clientWidth,
      text: (el.textContent || "").replace(/\\s+/g, " ").trim().slice(0, 70)
    });
  }
  res.overflow.sort((a, b) => b.over - a.over);
  res.overflow = res.overflow.slice(0, 6);
  return res;
}

(async () => {
  const out = [];
  for (const t of TARGETS) {
    const f = document.createElement("iframe");
    f.setAttribute("scrolling", "no");
    f.style.cssText = "width:" + VIEWPORT + "px;height:__IFH__px;border:0;" +
                      "position:absolute;left:0;top:0;visibility:hidden";
    document.body.appendChild(f);
    await new Promise((resolve) => {
      let done = false;
      const fin = () => { if (!done) { done = true; resolve(); } };
      f.onload = fin;
      f.onerror = fin;
      setTimeout(fin, 4000);
      f.src = t;
    });
    let r;
    try { r = measure(f.contentDocument); }
    catch (e) { r = {error: String(e)}; }
    r.url = t;
    out.push(r);
    f.remove();
  }
  document.getElementById("out").textContent = JSON.stringify(out);
  document.title = "QA-DONE";
})();
</script></body></html>
"""


def serve(root, harness_bytes):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(root), **kw)

        def do_GET(self):
            if self.path.startswith("/__qa_harness__"):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(harness_bytes)))
                self.end_headers()
                self.wfile.write(harness_bytes)
                return
            super().do_GET()

        def log_message(self, *a):
            pass

    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), Handler)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def run_probe(browser, root, urls):
    harness = (
        HARNESS.replace("__TARGETS__", json.dumps(urls))
        .replace("__VIEWPORT__", str(VIEWPORT))
        .replace("__IFH__", str(IFRAME_HEIGHT))
        .replace("__TOL__", str(OVERFLOW_TOL))
    )
    httpd = serve(root, harness.encode("utf-8"))
    port = httpd.server_address[1]
    try:
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [
                    browser,
                    "--headless=new",
                    "--disable-gpu",
                    "--no-sandbox",
                    "--hide-scrollbars",
                    f"--user-data-dir={profile}",
                    "--virtual-time-budget=180000",
                    "--window-size=%d,900" % VIEWPORT,
                    "--dump-dom",
                    f"http://127.0.0.1:{port}/__qa_harness__",
                ],
                capture_output=True,
                text=True,
                timeout=600,
            )
    finally:
        httpd.shutdown()
    dom = proc.stdout
    if "QA-DONE" not in dom:
        raise RuntimeError(
            "the probe did not finish (title is not QA-DONE) — "
            "measuring nothing and reporting it as clean is the defect this "
            "whole file exists to stop.\nstderr: %s" % proc.stderr[-800:]
        )
    m = re.search(r'<pre id="out">(.*?)</pre>', dom, re.S)
    if not m:
        raise RuntimeError("no result block in the dumped DOM")
    return json.loads(
        m.group(1).replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
        .replace("&amp;", "&")
    )


def collect(root, only=None):
    out = []
    for family in FAMILIES:
        d = root / family
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.html")):
            if only and only not in p.name:
                continue
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="repository root (these artefacts are never built)")
    ap.add_argument("--report", action="store_true", help="measure and exit 0")
    ap.add_argument("--only", help="substring filter on the file name")
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    browser = find_browser()
    if not browser:
        print("REFUSED qa_artefact_render — no headless Chrome/Chromium on PATH.")
        print("  This check is not skippable: see the header.")
        return 2

    targets = collect(root, args.only)
    if not targets:
        print("REFUSED qa_artefact_render — no founder-facing artefacts found under %s"
              % ", ".join(FAMILIES))
        return 2

    urls = ["/" + str(p.relative_to(root)) for p in targets]
    results = run_probe(browser, root, urls)
    by_url = {r["url"]: r for r in results}

    failures = []
    overflowing = []
    tails_ok = overflow_ok = 0
    worst = []
    tail_ratios = []
    for p in targets:
        url = "/" + str(p.relative_to(root))
        r = by_url.get(url)
        rel = str(p.relative_to(root))
        if r is None or r.get("error"):
            failures.append((rel, "NOT MEASURED", r.get("error") if r else "missing"))
            continue

        # --- A: the document renders to its own end ---------------------------
        # Two oracles, both direct. A comment node carrying a closing tag means
        # markup was swallowed; a render that lost a share of the source's own
        # visible text means content was deleted rather than merely restyled.
        src_len = len(source_text(p))
        got_len = r.get("textLen", 0)
        ratio = (got_len / src_len) if src_len else 1.0
        swallowed = r.get("comments", 0)
        if swallowed or ratio < TEXT_FLOOR:
            why = []
            if swallowed:
                why.append("%d comment node(s) in the rendered DOM carry a closing "
                           "tag — markup was swallowed by an unclosed comment" % swallowed)
            if ratio < TEXT_FLOOR:
                why.append("the render carries %d of the source's %d visible "
                           "characters (%.1f%%, floor %.0f%%); render ends %r"
                           % (got_len, src_len, ratio * 100, TEXT_FLOOR * 100,
                              re.sub(r"\s+", " ", r.get("tail", ""))[-48:]))
            failures.append((rel, "TAIL NOT RENDERED", " · ".join(why)))
        else:
            tails_ok += 1
            tail_ratios.append((ratio, rel))

        # --- B: nothing overflows its container at the stated viewport --------
        over = r.get("overflow") or []
        doc_over = r.get("docOverflow", 0)
        overflows = bool(over) or doc_over > OVERFLOW_TOL
        baselined = rel in OVERFLOW_BASELINE
        if overflows:
            bits = []
            if doc_over > OVERFLOW_TOL:
                bits.append("document %dpx wider than the %dpx viewport" % (doc_over, VIEWPORT))
            for o in over[:3]:
                bits.append("<%s%s> overflows its %dpx box by %dpx: %r"
                            % (o["tag"], ("." + o["cls"].split()[0]) if o["cls"] else "",
                               o["client"], o["over"], o["text"][:48]))
            worst.append((max([doc_over] + [o["over"] for o in over]), rel))
            overflowing.append((rel, " · ".join(bits), baselined))
        else:
            overflow_ok += 1

    new_overflow = [o for o in overflowing if not o[2]]
    fixed = sorted(OVERFLOW_BASELINE - {o[0] for o in overflowing})

    if args.report:
        print("qa_artefact_render --report · %d artefacts rendered at %dpx"
              % (len(targets), VIEWPORT))
        print("  A  tail renders .......... %d of %d  (asserted)" % (tails_ok, len(targets)))
        if tail_ratios:
            lo, lorel = min(tail_ratios)
            print("     thinnest margin ...... %.1f%% of source text, floor %.0f%%  %s"
                  % (lo * 100, TEXT_FLOOR * 100, lorel))
        print("  B  nothing overflows ..... %d of %d  (MEASURED, NOT ASSERTED - see header)"
              % (overflow_ok, len(targets)))
        for sev, rel in sorted(worst, reverse=True)[:12]:
            print("     worst overflow ....... %6dpx  %s" % (sev, rel))
        for rel, kind, detail in failures[:40]:
            print("  %-18s %s\n      %s" % (kind, rel, detail))
        for rel, detail, _b in overflowing:
            print("     overflow  %s\n        %s" % (rel, detail))
        return 0

    if failures:
        print("FAIL qa_artefact_render — %d of %d founder-facing artefacts do not render"
              % (len({f[0] for f in failures}), len(targets)))
        for rel, kind, detail in failures:
            print("  %s" % rel)
            print("    %s: %s" % (kind, detail))
        print()
        print("  The brief is the artefact the CHARTER names as the founder's")
        print("  proof-of-work contract. A structural count cannot see either of")
        print("  these defects: an unclosed comment deletes a container rather")
        print("  than overflowing it, and an unbreakable token breaks a column")
        print("  without breaking any markup.")
        return 1

    print("OK qa_artefact_render — %d founder-facing artefacts rendered at %dpx in a "
          "real browser" % (len(targets), VIEWPORT))
    print("  A  tail renders .......... %d of %d · ASSERTED on all, nothing excused "
          "(the 2026-10-12 bite)" % (tails_ok, len(targets)))
    print("  B  nothing overflows ..... %d of %d · MEASURED, NOT ASSERTED"
          % (overflow_ok, len(targets)))
    print("       This probe reads scrollWidth, which Chrome does NOT grow for inline")
    print("       text overflowing an overflow:visible block - proved by injection, see")
    print("       the header. It therefore has a known blind spot on the exact class it")
    print("       was commissioned for, and a check that cannot be shown to bite does")
    print("       not gate a build. The Range-rectangle oracle is queue item 28.")
    if overflowing:
        print("       %d artefacts overflow today, every one historical; repair is queue "
              "item 27" % len(overflowing))
        for sev, rel in sorted(worst, reverse=True)[:5]:
            print("       %6dpx  %s" % (sev, rel))
    if new_overflow:
        print("       NEW since the 2026-10-19 baseline, and NOT excused by it:")
        for rel, detail, _b in new_overflow:
            print("       ! %s\n           %s" % (rel, detail))
    if fixed:
        print("       no longer overflowing - delete from OVERFLOW_BASELINE: %s"
              % ", ".join(fixed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
