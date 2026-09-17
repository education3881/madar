#!/usr/bin/env python3
"""
qa_arabic_shaping.py — standing assertion 17: Arabic renders AS ARABIC.

The question this answers was named in the 2026-09-15 QA log and carried, owed and
unanswered, through 09-16:

    qa_render proves a page draws ink, keeps its ground and carries its accent.
    It cannot see whether Arabic renders as Arabic — joined script rather than
    disconnected letterforms — which is the one render defect this operation has
    actually shipped (VALENCE, 2026-08-18).

That defect was not a missing font and not a broken glyph. It was `letter-spacing`.
Arabic is a cursive script: its letters are *joined*, and the shaping engine draws
the connecting strokes. Insert tracking between the letters and the joins are pulled
apart — the word is still legible as a sequence of shapes, and it is no longer a
word. Tracking is a Latin display convention and is never applied to Arabic.

The obstacle, also named in the 09-16 log, is that **joining has no stable pixel
oracle**: a screenshot of joined Arabic and a screenshot of broken Arabic differ in
ways no threshold can name, and a diff against a golden image fails on every
legitimate edit (ruling #35, and qa_render's own design note). So this check does
not look at pixels. It asks the browser the question whose answer *causes* the
defect, and the answer is a **computed style**:

    ASSERTION — no element whose own text is Arabic may compute a `letter-spacing`
                other than `normal`.

Computed style is the right instrument precisely because the cascade is the hard
part. The site's built CSS carries ~130 `letter-spacing` declarations across mono
labels, kickers, display headings and one standalone instrument; deciding by hand
which of them can reach an Arabic run means re-implementing selector matching,
inheritance, media queries and specificity — that is, writing a worse browser. The
browser is already a dependency (qa_render, 2026-09-15). Ask it.

WHY A COMPUTED-STYLE READ AND NOT A GREP OVER THE CSS
    A grep finds declarations; it cannot find *which elements they land on*, and an
    assertion scoped wider than the thing it checks finds the right string for the
    wrong reason (2026-09-14, the masking trap). The reverse error is worse here:
    the VALENCE page sets `letter-spacing:.005em` on `body`, so the defect arrives
    by INHERITANCE onto elements whose own rules say nothing about tracking at all.
    No grep over selectors would ever have found that. The browser resolves it in
    one call.

HOW THE PAGE IS LOADED
    The target page is loaded **unmodified**, inside an iframe on a probe page
    served from the same origin. Nothing is injected into the artefact under test;
    the probe walks the iframe's document and reports. This matters because the
    thing being measured is the cascade, and appending so much as a <script> to the
    page under test would make the measured artefact not the served one (#52: an
    assertion must be able to say which artefact it read — including that it read
    the real one).

NON-VACUITY
    Each target declares the minimum number of Arabic-bearing elements it must
    find. A page that reports zero Arabic elements has not passed; it has failed to
    look (2026-08-16, the silent-pass trap; #52's third corollary). The English
    pages are targets for exactly this reason and are the highest-yield ones: they
    carry Arabic inside Latin chrome — the cross-language link, the still's caption
    — which is the single most likely place for a Latin-tuned tracking rule to land
    on an Arabic run.

Dependencies: Python 3 standard library, plus a headless Chrome/Chromium on PATH —
the same browser qa_render already requires. If no browser is found this exits 1
rather than skipping (RUNBOOK, 2026-09-13).

Usage:
    python3 agents/tools/qa_arabic_shaping.py web/dist [--report]

--report prints every Arabic-bearing element and its computed tracking, and exits 0
without judging. That is the calibration mode.
"""

import argparse
import http.server
import json
import os
import pathlib
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading

BROWSERS = (
    "google-chrome-stable",
    "google-chrome",
    "chromium-browser",
    "chromium",
)

# The Arabic ranges the corpus actually uses: Arabic, Supplement, Extended-A and the
# two presentation-forms blocks. Deliberately NOT ٠-٩ alone — Arabic-Indic
# digits are not cursive and carry no joins, so a digit run is not evidence of shaping.
ARABIC_LETTERS = r"ؠ-يٮ-ۓۺ-ۿݐ-ݿࢠ-ࢽﭐ-﷿ﹰ-﻿"

# label, path, minimum Arabic-bearing elements expected
TARGETS = [
    ("AR home", "/madar/ar/", 20),
    ("AR article", "/madar/ar/articles/2026-05-25-bo-teacher-chalk/", 20),
    ("AR editions", "/madar/ar/editions/", 10),
    ("AR browse", "/madar/ar/browse/", 10),
    # The English pages carry Arabic inside Latin chrome. Highest-yield targets.
    ("EN home", "/madar/", 2),
    ("EN article", "/madar/articles/2026-05-25-bo-teacher-chalk/", 2),
    # The known-broken control: the one page whose Arabic joins have actually broken,
    # and the one page that sets tracking on `body` where it can reach by inheritance.
    ("VALENCE", "/madar/valence/", 1),
]

PROBE = """<!doctype html>
<html><head><meta charset="utf-8"><title>probe</title></head>
<body>
<script>
(function () {
  var AR = /[%(ranges)s]/;
  var f = document.createElement('iframe');
  f.style.width = '1200px';
  f.style.height = '1400px';
  f.style.border = '0';
  f.addEventListener('load', function () {
    var out = [], seen = 0;
    try {
      var d = f.contentDocument, w = f.contentWindow;
      var all = d.querySelectorAll('*');
      for (var i = 0; i < all.length; i++) {
        var el = all[i], own = '';
        for (var j = 0; j < el.childNodes.length; j++) {
          if (el.childNodes[j].nodeType === 3) own += el.childNodes[j].nodeValue;
        }
        if (!AR.test(own)) continue;
        seen++;
        var cs = w.getComputedStyle(el);
        var ls = cs.letterSpacing;
        var tracked = ls && ls !== 'normal' && parseFloat(ls) !== 0;
        if (tracked) {
          out.push({
            tag: el.tagName.toLowerCase(),
            cls: (el.getAttribute('class') || '').slice(0, 70),
            ls: ls,
            lang: el.closest('[lang]') ? el.closest('[lang]').getAttribute('lang') : '',
            text: own.replace(/\\s+/g, ' ').trim().slice(0, 34)
          });
        }
      }
      document.title = 'QASHAPE:' + JSON.stringify({ seen: seen, bad: out });
    } catch (e) {
      document.title = 'QASHAPE:' + JSON.stringify({ error: String(e) });
    }
  });
  f.src = '%(target)s';
  document.body.appendChild(f);
})();
</script>
</body></html>
"""


def serve(dist: pathlib.Path):
    """Serve a copy of dist under /madar/, the path the built absolute URLs assume."""
    root = tempfile.mkdtemp(prefix="qa_shaping_root_")
    shutil.copytree(dist, os.path.join(root, "madar"))

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=root, **kw)

        def log_message(self, *a):
            pass

    httpd = socketserver.TCPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1], root


def probe(browser: str, root: str, port: int, path: str):
    """Load `path` unmodified inside a probe page and return the computed-style report."""
    page = PROBE % {"ranges": ARABIC_LETTERS, "target": f"http://127.0.0.1:{port}{path}"}
    fd, probe_path = tempfile.mkstemp(suffix=".html", dir=os.path.join(root, "madar"))
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(page)
    url = f"http://127.0.0.1:{port}/madar/{os.path.basename(probe_path)}"
    profile = tempfile.mkdtemp(prefix="qa_shaping_profile_")
    try:
        res = subprocess.run(
            [
                browser, "--headless", "--disable-gpu", "--no-sandbox",
                "--hide-scrollbars", "--window-size=1200,1400",
                f"--user-data-dir={profile}",
                "--virtual-time-budget=8000",
                "--dump-dom", url,
            ],
            capture_output=True, text=True, timeout=120,
        )
        m = re.search(r"QASHAPE:(\{.*?\})</title>", res.stdout, re.S)
        if not m:
            return None
        return json.loads(m.group(1))
    finally:
        shutil.rmtree(profile, ignore_errors=True)
        try:
            os.unlink(probe_path)
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dist", help="the built site (web/dist)")
    ap.add_argument("--report", action="store_true", help="print tracking, judge nothing")
    args = ap.parse_args()

    dist = pathlib.Path(args.dist).resolve()
    # #52: print the input, whether this passes or fails.
    print(f"qa_arabic_shaping: {dist}")
    if not dist.is_dir():
        print(f"FAIL  {dist} is not a directory", file=sys.stderr)
        return 1
    if not (dist / "index.html").exists():
        print(f"FAIL  {dist} has no index.html — this is not a built dist", file=sys.stderr)
        return 1

    browser = next((b for b in BROWSERS if shutil.which(b)), None)
    if browser is None:
        print(
            "FAIL  no headless Chrome/Chromium on PATH — qa_arabic_shaping cannot run.\n"
            "      A check that silently does not run is a green light wired to nothing.",
            file=sys.stderr,
        )
        return 1

    httpd, port, root = serve(dist)
    findings, rows = [], []
    try:
        for label, path, floor in TARGETS:
            if not (dist / path.replace("/madar/", "").lstrip("/") or "index.html"):
                pass
            rep = probe(browser, root, port, path)
            if rep is None:
                findings.append(f"{label}: the probe returned nothing — the page did not load")
                continue
            if "error" in rep:
                findings.append(f"{label}: probe error — {rep['error']}")
                continue
            rows.append((label, path, floor, rep))
    finally:
        httpd.shutdown()
        shutil.rmtree(root, ignore_errors=True)

    total_seen = 0
    for label, path, floor, rep in rows:
        seen, bad = rep["seen"], rep["bad"]
        total_seen += seen
        if args.report:
            print(f"{label:12s} arabic elements={seen:4d}  tracked={len(bad)}")
            for b in bad:
                print(f"    {b['ls']:>8}  <{b['tag']} class=\"{b['cls']}\"> lang={b['lang']!r}  {b['text']}")
            continue
        # Non-vacuity first: a check that swept nothing has failed, not passed.
        if seen < floor:
            findings.append(
                f"{label}: found {seen} Arabic-bearing element(s), expected at least {floor} — "
                f"the page did not render, or the probe did not reach it"
            )
        for b in bad:
            findings.append(
                f"{label}: <{b['tag']} class=\"{b['cls']}\"> computes letter-spacing "
                f"{b['ls']} on Arabic text ({b['text']}) — tracking breaks the joins"
            )

    if args.report:
        return 0

    if findings:
        print(f"\nFAIL qa_arabic_shaping — {len(findings)} defect(s):", file=sys.stderr)
        for f in findings:
            print(f"  - {f}", file=sys.stderr)
        print(
            "\n  Arabic is cursive. Tracking is a Latin display convention; applied to an\n"
            "  Arabic run it pulls the joins apart and the word stops being a word.\n"
            "  Set letter-spacing: normal for the rule that reaches this element.",
            file=sys.stderr,
        )
        return 1

    print(
        f"CLEAN qa_arabic_shaping — {len(rows)} targets, {total_seen} Arabic-bearing elements; "
        f"every one computes letter-spacing: normal"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
