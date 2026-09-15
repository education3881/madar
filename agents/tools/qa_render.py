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

  P1  NOT BLANK        ink coverage above a floor            (the page drew something)
  P2  LEGIBLE          ink-dark pixels present, on paper     (not white-on-white)
  P3  ACCENT PRESENT   the declared kiln-orange reaches the raster
                       (an undefined token evaporates into the inherited ink —
                        structurally invisible, visibly wrong: the 09-14 class)

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
import os
import pathlib
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
            shoot(browser, url, str(out))
            rows.append((label, measure(str(out)), floors))

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
            continue
        if not m["bg_is_light"]:
            findings.append(
                f"{label}: the page's dominant colour is {m['background']}, not a light ground"
            )
        if m["ink_frac"] < ink_floor:
            findings.append(
                f"{label}: P1 blank — ink coverage {m['ink_frac']:.4f} below floor {ink_floor}"
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
    print(f"CLEAN qa_render — {len(rows)} targets rendered; not blank, legible, accent present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
