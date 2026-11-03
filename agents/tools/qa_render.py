#!/usr/bin/env python3
"""
qa_render.py — standing assertion 14: the page RENDERS.

Every other assertion this operation owns reads *structure*: a thing is present,
resolves, parses, matches, agrees. Not one of them has ever looked at a pixel.
Three render-class defects are already in the record and all three were found by
a human happening to look:

  * 2026-08-18  the Arabic wordmark's letter-joins broke on the VALENCE share card
  * 2026-08-16  the daily brief rendered edge-to-edge for two days
  * 2026-09-14  an undefined CSS token put a country label in the wrong colour on
                76 browse pages — visible to the eye, invisible to all thirteen checks

The open design problem (named in the 2026-09-14 QA log) is that a render check has
no stable oracle: a screenshot diff fails on every legitimate edit. So this asserts
*properties* of the rendering, never its identity, and the properties are chosen from
the defects that have actually bitten:

  P1  NOT BLANK        ink coverage above a floor, PER 900px BAND   (no screenful blank)
  P2  LEGIBLE          ink-dark pixels present, on paper     (not white-on-white)
  P3  ACCENT PRESENT   the declared kiln-orange reaches the raster
                       (an undefined token evaporates into the inherited ink —
                        structurally invisible, visibly wrong: the 09-14 class)

THE RULER WAS WIDENED TWICE ON 2026-11-03, UNDER STANDING-QUEUE ITEM 28 (ruling #126)
-------------------------------------------------------------------------------------
Item 28 asked which of our four render assertions rest on an oracle nobody has
interrogated — *not* what the check enumerated, which six rulings already ask, but
**what its ruler can represent once the thing is inside it.** This one had two
answers and both were in the arithmetic rather than in the target list.

**EXTENT.** `--screenshot` under `--headless=new` captures the VIEWPORT, not the
document — old headless captured the full page, and the flag name did not change
when the behaviour did. Measured 2026-11-03: every raster this tool had ever read
was exactly 1200x900, against documents 2,559 to 5,648 px tall, so the ruler held
**15.9% to 35.2% of each page** while the output printed one line per "page". It
was never a regression: the floors were calibrated on 2026-09-15 from the same
viewport crop, and today's viewport numbers reproduce that range to the digit. The
shot is now taken at the document's own height, verified rather than assumed (see
`page_height` below).

**POSITION.** A pixel population count has no coordinates. Widening the raster
alone would have *reduced* sensitivity: on the EN home the whole-page dark
fraction is 0.0053 and passes a 0.003 floor, while its own last band reads
**0.0006 — five times below that floor and invisible to the average.** So P1 is
asserted per 900px band: the property is now *no screenful of any page is blank*,
which is what the 2026-08-16 edge-to-edge defect actually was, rather than *the
page as a whole drew something*, which no page with a masthead can fail.

Measured on this build at full height, per band, before any floor was chosen
(#93 — a floor above today's reality reds every build): band ink runs 0.0114 to
0.0612 across all fourteen bands of the four targets, so BAND_INK_FLOOR sits at
0.006, below today's worst band and twenty times above a blank one.

**What is measured per band and deliberately NOT asserted, with what would
falsify the decline:** per-band *dark* and per-band *accent*. The EN home's
footer band reads dark 0.0006 and the EN article's reads 0.0008 — both legible,
both small muted type, and `dark` counts only pixels within 90 of INK. A per-band
dark floor at the whole-raster 0.003 would red this build today; a floor low
enough to pass the footer (0.0005) sits too close to what a genuinely
white-on-white band produces (~0) to separate them. The ruler cannot hold
per-band legibility because it is an ABSOLUTE count, and the decline expires the
day the ruler is made relative to the band's own ink — that is the falsifier, and
it is standing-queue item 73, not a sibling instrument (#125: a decline may not
name a sibling without naming the sibling's limb, and there is no sibling here).

Cost, measured rather than assumed: the widening takes this assertion from a
1.08 Mpx read per target to 3.1-6.8 Mpx, 1.5-2.3 s to shoot and 1.3-3.0 s to
decode, plus one `--dump-dom` pass per target to learn the height.

Scope is deliberately narrow, because crying wolf on correct output is how a standing
assertion gets ignored (2026-08-25, ruling #35): four pages and one share card.

Dependencies: Python 3 standard library, plus a headless Chrome/Chromium on PATH.
The browser is the one dependency the QA toolkit has ever taken, and it is taken
because no amount of parsing can answer "does this look right". If no browser is
found this exits 1 rather than skipping: a check that silently does not run is a
green light wired to nothing (RUNBOOK, 2026-09-13).

Usage:
    python3 agents/tools/qa_render.py web/dist [--report]

--report prints the measured properties for every target and exits 0 without
judging them. That is the calibration mode; the floors below were set from it.
"""

import argparse
import collections
import functools
import http.server
import json
import os
import pathlib
import re
import shutil
import socketserver
import struct
import subprocess
import sys
import tempfile
import threading
import zlib

# --- the design system's five colour tokens (web/src/styles/global.css) ---------
PAPER = (0xFA, 0xFA, 0xF7)
INK = (0x0E, 0x1B, 0x2C)
ORANGE = (0xD9, 0x4F, 0x2A)

# Radii in RGB euclidean distance. PAPER→INK is ~383 apart, so 90 cannot reach paper.
INK_RADIUS = 90
PAPER_RADIUS = 40  # anything further from paper than this counts as ink of some kind

BROWSERS = (
    "google-chrome-stable",
    "google-chrome",
    "chromium-browser",
    "chromium",
)


# --- PNG, decoded without a dependency -----------------------------------------


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png(path):
    """Return (width, height, [(r,g,b), ...]) for an 8-bit RGB/RGBA PNG."""
    raw = pathlib.Path(path).read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path}: not a PNG")
    pos, idat, hdr, plte = 8, bytearray(), None, None
    while pos < len(raw):
        (length,) = struct.unpack(">I", raw[pos : pos + 4])
        kind = raw[pos + 4 : pos + 8]
        data = raw[pos + 8 : pos + 8 + length]
        if kind == b"IHDR":
            hdr = struct.unpack(">IIBBBBB", data)
        elif kind == b"PLTE":
            plte = [tuple(data[i : i + 3]) for i in range(0, len(data), 3)]
        elif kind == b"IDAT":
            idat += data
        elif kind == b"IEND":
            break
        pos += 12 + length
    if hdr is None:
        raise ValueError(f"{path}: no IHDR")
    width, height, depth, colour, compress, filt, interlace = hdr
    # Screenshots come back RGBA (6); the share cards are palette PNGs (3).
    if depth != 8 or colour not in (2, 3, 6) or interlace != 0:
        raise ValueError(
            f"{path}: unsupported PNG (depth {depth}, colour {colour}, interlace {interlace})"
        )
    if colour == 3 and not plte:
        raise ValueError(f"{path}: palette PNG with no PLTE")
    channels = {2: 3, 3: 1, 6: 4}[colour]
    stride = width * channels
    data = zlib.decompress(bytes(idat))
    out, prev = [], bytearray(stride)
    at = 0
    for _ in range(height):
        ftype = data[at]
        line = bytearray(data[at + 1 : at + 1 + stride])
        at += 1 + stride
        if ftype == 1:
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 0xFF
        elif ftype == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xFF
        elif ftype == 3:
            for i in range(stride):
                left = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 0xFF
        elif ftype == 4:
            for i in range(stride):
                left = line[i - channels] if i >= channels else 0
                upleft = prev[i - channels] if i >= channels else 0
                line[i] = (line[i] + _paeth(left, prev[i], upleft)) & 0xFF
        elif ftype != 0:
            raise ValueError(f"{path}: bad filter type {ftype}")
        if colour == 3:
            out.extend(plte[i] for i in line)
        else:
            for x in range(0, stride, channels):
                out.append((line[x], line[x + 1], line[x + 2]))
        prev = line
    return width, height, out


def near(pixel, target, radius):
    dr = pixel[0] - target[0]
    dg = pixel[1] - target[1]
    db = pixel[2] - target[2]
    return dr * dr + dg * dg + db * db <= radius * radius


def is_accent(pixel):
    """Kiln-orange, including its antialiased blends.

    A tight radius around #D94F2A counts only the solid core of a stroke, which on
    a 10.5px mono kicker is a handful of pixels — the check would then be measuring
    type size, not the presence of the accent. This asks the question the eye asks:
    is this pixel warm? Neither of the other two warm tokens can answer yes — sand
    (#E8E2D0) has r-g = 6 and sage (#7A8471) has r-g = -10.
    """
    r, g, b = pixel
    return r >= 100 and (r - g) >= 40 and (g - b) >= 5


def is_light(pixel):
    r, g, b = pixel
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) >= 190


# The site's own header band, which carries no hero still. Proved necessary on
# 2026-09-15: with the accent token neutralised in the served CSS, whole-page
# accent on the two home pages barely moved (949→900, 849→817) because the hero
# still's own kiln-orange stroke is an SVG literal and does not read the token.
# The field the assertion exists to check was masked by a neighbour that
# legitimately carries the same colour — the 2026-09-14 trap, in a new place.
CHROME_BAND = 120

# A screenful. P1 is asserted per band of this many rows, because a pixel count has
# no coordinates and a page-wide average cannot represent a blank region (#126).
BAND = 900
BAND_INK_FLOOR = 0.006


def band_rows(width, height, pixels):
    """Per-BAND ink/dark/accent fractions, top to bottom. The position the count lost."""
    rows = []
    for top in range(0, height, BAND):
        band = pixels[top * width : (top + BAND) * width]
        n = len(band)
        if not n:
            continue
        ink = dark = accent = 0
        for p in band:
            if not near(p, PAPER, PAPER_RADIUS):
                ink += 1
                if is_accent(p):
                    accent += 1
                elif near(p, INK, INK_RADIUS):
                    dark += 1
        rows.append(
            {
                "top": top,
                "bottom": top + n // width,
                "ink": ink / n,
                "dark": dark / n,
                "accent": accent,
            }
        )
    return rows


def measure(path):
    width, height, pixels = read_png(path)
    total = len(pixels)
    counts = collections.Counter(pixels)
    background = counts.most_common(1)[0][0]
    ink_px = accent_px = dark_px = 0
    for p in pixels:
        if not near(p, PAPER, PAPER_RADIUS):
            ink_px += 1
            if is_accent(p):
                accent_px += 1
            elif near(p, INK, INK_RADIUS):
                dark_px += 1
    band = pixels[: CHROME_BAND * width]
    return {
        "bands": band_rows(width, height, pixels),
        "w": width,
        "h": height,
        "total": total,
        "background": background,
        "bg_is_light": is_light(background),
        "ink_frac": ink_px / total,
        "dark_frac": dark_px / total,
        "accent_page": accent_px,
        "accent_chrome": sum(1 for p in band if is_accent(p)),
    }


# --- serving the built site the way the browser will meet it -------------------


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(dist):
    """Serve dist under /madar/ (the site's own base path) on an ephemeral port."""
    root = tempfile.mkdtemp(prefix="qa_render_")
    os.symlink(pathlib.Path(dist).resolve(), pathlib.Path(root) / "madar")
    handler = functools.partial(_Quiet, directory=root)
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1], root


VIEWPORT_W = 1200
# Generous ceiling. A page taller than this is not silently cropped — the tool says so.
MAX_SHOT_H = 12000

_HEIGHT_PROBE = """<!doctype html><html><head><meta charset="utf-8"><title>h</title></head>
<body><script>
(function () {
  var f = document.createElement('iframe');
  f.style.width = '%(w)dpx'; f.style.height = '%(h)dpx'; f.style.border = '0';
  f.addEventListener('load', function () {
    try {
      var d = f.contentDocument;
      document.title = 'H:' + JSON.stringify({h: d.documentElement.scrollHeight});
    } catch (e) { document.title = 'H:' + JSON.stringify({error: String(e)}); }
  });
  f.src = '%(url)s'; document.body.appendChild(f);
})();
</script></body></html>
"""


def page_height(browser, root, port, url, at):
    """The document's own scrollHeight, laid out in a VIEWPORT_W x `at` box.

    Two passes rather than one, because `--screenshot` under --headless=new captures
    the viewport and there is no CLI flag for a full-page capture (#126). The probe
    is served over http from the same root as the target so the iframe is
    same-origin; a file:// probe cannot read into it and returns null.
    """
    page = _HEIGHT_PROBE % {"w": VIEWPORT_W, "h": at, "url": url}
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, dir=root, encoding="utf-8"
    ) as fh:
        fh.write(page)
        name = pathlib.Path(fh.name).name
    res = subprocess.run(
        [
            browser,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--window-size={VIEWPORT_W},{at}",
            "--virtual-time-budget=8000",
            "--dump-dom",
            f"http://127.0.0.1:{port}/{name}",
        ],
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )
    m = re.search(r"<title>H:(.*?)</title>", res.stdout, re.S)
    if not m:
        raise RuntimeError(f"could not measure the document height of {url}")
    got = json.loads(m.group(1))
    if "error" in got:
        raise RuntimeError(f"height probe failed on {url}: {got['error']}")
    return int(got["h"])


def document_height(browser, root, port, url):
    """Measure at 900, then CONFIRM at the measured height.

    A layout that depends on viewport height (`vh` units, a sticky full-height hero)
    cannot be captured in one pass, and a tool that assumed otherwise would measure
    the wrong raster in silence. None of this assertion's four targets carries a `vh`
    declaration — verified 2026-11-03 — but that is a fact about today's templates,
    not a property of the tool, so it is asserted here instead of trusted.
    """
    first = page_height(browser, root, port, url, 900)
    if first > MAX_SHOT_H:
        raise RuntimeError(
            f"{url}: document is {first}px, past the {MAX_SHOT_H}px shot ceiling — "
            "raise MAX_SHOT_H deliberately rather than letting the raster crop"
        )
    second = page_height(browser, root, port, url, first)
    if abs(second - first) > 2:
        raise RuntimeError(
            f"{url}: document height is viewport-dependent ({first}px measured at a "
            f"900px viewport, {second}px at {first}px) — this page cannot be captured "
            "in one raster and P1-per-band cannot be asserted on it"
        )
    return first


def shoot(browser, url, out, size="1200,900"):
    subprocess.run(
        [
            browser,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--window-size={size}",
            "--virtual-time-budget=8000",
            f"--screenshot={out}",
            url,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=180,
        check=False,
    )
    if not pathlib.Path(out).exists() or pathlib.Path(out).stat().st_size == 0:
        raise RuntimeError(f"no screenshot written for {url}")


# --- the targets and their floors ----------------------------------------------
#
# Floors are set well below the values measured on the known-good build of
# 2026-09-15 (--report: ink 0.0216-0.0506, dark 0.0066-0.0197, accent 629-1085),
# so an ordinary editorial change cannot trip them and a vanished element can.

# Where P3 is measured is per-target, and it is not a preference: each scope below
# is the one that was PROVED to bite when the accent token was neutralised in the
# served CSS (2026-09-15). On the home pages the hero still masks the whole-page
# count, so P3 reads the chrome band, 49 -> 0 and 32 -> 0 under the bite. On the
# article pages the chrome band carries no accent at all, so P3 reads the page,
# 674 -> 0 and 629 -> 0. An assertion measured where it cannot fail is not an
# assertion.
#
#         label,  path under the site,  ink,  dark,  accent floor, accent scope
TARGETS = [
    ("EN home", "/madar/", 0.010, 0.003, 15, "chrome"),
    ("AR home", "/madar/ar/", 0.010, 0.003, 15, "chrome"),
    ("EN article", "/madar/articles/2026-05-25-bo-teacher-chalk/", 0.010, 0.003, 200, "page"),
    ("AR article", "/madar/ar/articles/2026-05-25-bo-teacher-chalk/", 0.010, 0.003, 200, "page"),
]

# The card is a generated raster, not a rendering of ours; P3 on it asserts that the
# still's own warm mark survived the conversion (the 2026-08-18 defect class).
CARD = ("share card", "og/2026-05-25-bo-teacher-chalk.png", 0.010, 0.003, 200, "page")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dist", help="the built site (web/dist)")
    ap.add_argument("--report", action="store_true", help="print properties, judge nothing")
    args = ap.parse_args()

    dist = pathlib.Path(args.dist)
    if not dist.is_dir():
        print(f"FAIL  {dist} is not a directory", file=sys.stderr)
        return 1

    browser = next((b for b in BROWSERS if shutil.which(b)), None)
    if browser is None:
        print(
            "FAIL  no headless Chrome/Chromium on PATH — qa_render cannot run.\n"
            "      A check that silently does not run is a green light wired to nothing;\n"
            "      install a browser or remove this assertion deliberately, in writing.",
            file=sys.stderr,
        )
        return 1

    httpd, port, root = serve(dist)
    shots = tempfile.mkdtemp(prefix="qa_render_shots_")
    findings, rows = [], []
    try:
        jobs = [(label, f"http://127.0.0.1:{port}{path}", floors) for label, path, *floors in TARGETS]
        for label, url, floors in jobs:
            out = pathlib.Path(shots) / (label.replace(" ", "_") + ".png")
            # The whole document, not the 1200x900 viewport the flag name implies (#126).
            try:
                height = document_height(browser, root, port, url)
            except RuntimeError as exc:
                # A gate fails with a sentence, never with a traceback: a stack dump in
                # CI is read as a broken tool and switched off, which is how an
                # assertion stops being an assertion (2026-09-13).
                findings.append(f"{label}: {exc}")
                continue
            shoot(browser, url, str(out), size=f"{VIEWPORT_W},{height}")
            m = measure(str(out))
            if m["h"] != height:
                findings.append(
                    f"{label}: asked for a {VIEWPORT_W}x{height} raster and got "
                    f"{m['w']}x{m['h']} — the ruler is not holding the document"
                )
            rows.append((label, m, floors))

        label, rel, *floors = CARD
        card = dist / rel
        if not card.exists():
            findings.append(f"{label}: {rel} is not in the build")
        else:
            rows.append((label, measure(str(card)), floors))
    finally:
        httpd.shutdown()
        shutil.rmtree(root, ignore_errors=True)

    for label, m, (ink_floor, dark_floor, accent_floor, scope) in rows:
        accent = m["accent_chrome"] if scope == "chrome" else m["accent_page"]
        if args.report:
            print(
                f"{label:12s} {m['w']}x{m['h']}  bg={m['background']} light={m['bg_is_light']}  "
                f"ink={m['ink_frac']:.4f}  dark={m['dark_frac']:.4f}  "
                f"accent[{scope}]={accent} (page={m['accent_page']}, chrome={m['accent_chrome']})"
            )
            for b in m["bands"]:
                print(
                    f"             band {b['top']:5d}-{b['bottom']:<5d} ink={b['ink']:.4f}  "
                    f"dark={b['dark']:.4f}  accent={b['accent']}"
                )
            continue
        if not m["bg_is_light"]:
            findings.append(
                f"{label}: the page's dominant colour is {m['background']}, not a light ground"
            )
        if m["ink_frac"] < ink_floor:
            findings.append(
                f"{label}: P1 blank — ink coverage {m['ink_frac']:.4f} below floor {ink_floor}"
            )
        # P1 per band. The whole-raster fraction above cannot represent a blank region;
        # this is the same property with the position the count lost (#126).
        for b in m["bands"]:
            if b["ink"] < BAND_INK_FLOOR:
                findings.append(
                    f"{label}: P1 blank BAND — rows {b['top']}-{b['bottom']} carry ink "
                    f"{b['ink']:.4f}, below floor {BAND_INK_FLOOR} "
                    f"(whole raster {m['ink_frac']:.4f} passes)"
                )
        if m["dark_frac"] < dark_floor:
            findings.append(
                f"{label}: P2 illegible — ink-dark pixels {m['dark_frac']:.4f} below floor {dark_floor}"
            )
        if accent < accent_floor:
            findings.append(
                f"{label}: P3 accent absent — {accent} kiln-orange pixels in the {scope}, "
                f"floor {accent_floor}"
            )

    shutil.rmtree(shots, ignore_errors=True)

    if args.report:
        return 0
    if findings:
        print("FAIL  qa_render — the build does not look the way it parses:", file=sys.stderr)
        for f in findings:
            print(f"  - {f}", file=sys.stderr)
        return 1
    bands = sum(len(m["bands"]) for _, m, _ in rows)
    worst = min((b["ink"] for _, m, _ in rows for b in m["bands"]), default=0.0)
    thin = min((b["dark"] for _, m, _ in rows for b in m["bands"]), default=0.0)
    print(
        f"CLEAN qa_render — {len(rows)} targets rendered at their own document height, "
        f"{bands} bands of {BAND}px; not blank, legible, accent present. "
        f"Worst band ink {worst:.4f} (floor {BAND_INK_FLOOR}). "
        f"Per-band dark reaches {thin:.4f} and is PRINTED, NOT ASSERTED: an absolute "
        f"ink-dark count cannot separate a legible band of small muted type from a "
        f"white-on-white one, and the decline expires when the ruler is made relative "
        f"to the band's own ink (queue item 73, not a sibling instrument)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
