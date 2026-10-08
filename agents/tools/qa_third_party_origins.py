#!/usr/bin/env python3
"""
qa_third_party_origins — standing assertion #31: the served pages fetch nothing
from an origin we do not own.

WHY THIS FILE EXISTS (2026-10-08)
---------------------------------
Because the privacy posture was a *belief* for 136 days, and then it was a
*measurement* for 20 more without being a *gate*.

The CHARTER's growth loop says *"Privacy posture is intact: no third-party
trackers, ever"*, and every daily brief has printed a version of *"the site
carries no third-party tracker by design"*. On **2026-09-18** Growth counted
that claim against the bytes for the first time
(`agents/growth/2026-09-18-third-party-surface-audit.md`) and found it **true as
stated** — no analytics, no tag manager, no pixel, no embed — and also found
what the claim's own wording stepped around: **two origins, 360 references,
120 of 121 pages**, every one of them fetched automatically before a reader saw
a word. `fonts.googleapis.com` and `fonts.gstatic.com`, for the five typefaces.

Not a tracker. Still the one request the site made on a reader's behalf that
the reader never asked for, and — this being a bilingual publication written
for readers in MENA — the Arabic edition's single point of failure: a reader
whose network throttles `fonts.gstatic.com` fell through a four-face fallback
stack to a generic serif, and standing assertion 18 could not see it, because
it measures the font **this runner** resolved and not the reader's.

The fonts were self-hosted on **2026-10-08** (queue item 4, 20 days open, three
displacements, reached the head by the 10-05 tiebreak). This file exists because
**the fix is one line of markup and the regression is one line of markup.** A
third-party `<link>` is the easiest thing in this repository to add back: it is
what every font vendor's documentation tells you to paste, it costs nothing
visible, and nothing we owned would have said a word. A privacy posture that
depends on nobody pasting a snippet is the 09-13 defect exactly — *a green check
that costs a human's attention is paid for out of the runs that have least of
it* — except that here there was no check at all, only a sentence in a charter.

WHAT THIS CHECK ENUMERATES, AND THE DISTINCTION IT IS BUILT ON
-------------------------------------------------------------
The whole value of this assertion is one classification, and the 09-18 audit
stated it before any code existed:

    "A citation is a link a reader chooses to follow. It is not a third-party
     request and must never be counted as one — conflating the two would make
     our own method look like a privacy problem."

This publication's entire method is **named primary sources read in served
text**. Its pages therefore point at ~180 external origins on purpose, and the
share rail points at `wa.me` and `x.com`. If this check counted origins it would
report the publication's greatest strength as its largest defect, fail on every
build, and be switched off inside a week.

So it does not classify by **origin**. It classifies by **who initiates the
fetch**, which is a property of the element and the attribute:

  AUTOMATIC — the reader's browser fetches it with no action, before or during
  render. These are asserted, and a non-ours origin here is a DEFECT:
      <link href>          only for rel values that fetch or open a connection:
                           stylesheet, preconnect, dns-prefetch, preload,
                           modulepreload, prefetch, prerender, icon,
                           apple-touch-icon, mask-icon, manifest
      <script src>, <img src|srcset>, <iframe src>, <frame src>, <embed src>,
      <object data>, <source src|srcset>, <video src|poster>, <audio src>,
      <track src>, <input src>, <use href|xlink:href>, <image href|xlink:href>
      @import and url(...) inside <style> blocks and style="" attributes

  READER-INITIATED — fires only on a click, and is NOT asserted:
      <a href>             the sources[] citations and the share rail

  DECLARATIONS — markup that names a URL without fetching it, NOT asserted:
      <link rel=alternate|canonical|author|license>   feed autodiscovery, canonical
      <meta property=og:image>, <meta name=twitter:image>
                           fetched by a scraper we hand the page to, not by the
                           reader's browser; their format and origin are
                           `qa_consumer_surface`'s subject, not this one

Both unasserted classes are **counted and printed** rather than silently
dropped. A check that ignores a category without saying so is indistinguishable
from a check that cannot see it.

TWO FAILURE-TO-CHECK GUARDS, because a silent pass is the house defect
----------------------------------------------------------------------
Per the 2026-08-16 silent-pass trap and the 09-14 bite rule, this check refuses
to report a green it has not earned:

  exit 2 — no HTML found at all. An empty enumeration is not a clean site.
  exit 3 — some page carries NO automatic reference whatsoever. Every page
           built from `Base.astro` links at least our own stylesheet and the
           font bundle; a page with nothing to classify means the parser stopped
           matching the served shape, which is the 09-14 trap — *an injection
           that fails to change the artefact reads exactly like a passing
           control*, here in its standing form. VALENCE is the one deliberate
           exception: it is a standalone file with an inline stylesheet and no
           external reference of any kind, which is why the 09-18 audit called
           it "the exception and the proof". It is exempted by name.

Usage:
    python3 agents/tools/qa_third_party_origins.py web/dist
"""

from __future__ import annotations

import os
import re
import sys
from urllib.parse import urlparse

# Our own origin. The site's canonical host, from web/astro.config.mjs `site`.
OURS = {"education3881.github.io"}

# Pages that legitimately carry no automatic external reference. VALENCE is a
# standalone instrument with its own inline stylesheet (2026-08-08); the 09-18
# audit measured it at zero third-party origins and called it the proof.
NO_AUTO_REF_OK = {"valence/index.html", "valence.html"}

# <link rel> values that cause a fetch or open a connection to the origin.
FETCHING_REL = {
    "stylesheet", "preconnect", "dns-prefetch", "preload", "modulepreload",
    "prefetch", "prerender", "icon", "shortcut icon", "apple-touch-icon",
    "apple-touch-icon-precomposed", "mask-icon", "manifest",
}

# (tag, attribute) pairs the browser fetches without the reader acting.
AUTO_ATTRS = {
    "script": ("src",),
    "img": ("src", "srcset"),
    "iframe": ("src",),
    "frame": ("src",),
    "embed": ("src",),
    "object": ("data",),
    "source": ("src", "srcset"),
    "video": ("src", "poster"),
    "audio": ("src",),
    "track": ("src",),
    "input": ("src",),
    "use": ("href", "xlink:href"),
    "image": ("href", "xlink:href"),
}

TAG_RE = re.compile(r"<([a-zA-Z][a-zA-Z0-9:-]*)((?:\s+[^<>]*?)?)/?>", re.S)
ATTR_RE = re.compile(r"""([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*("([^"]*)"|'([^']*)')""", re.S)
STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>(.*?)</style>", re.S | re.I)
CSS_URL_RE = re.compile(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", re.I)
CSS_IMPORT_RE = re.compile(r"""@import\s+(?:url\(\s*)?['"]([^'"]+)['"]""", re.I)


def strip_noise(html: str) -> str:
    """Remove HTML comments and <script> BODIES — keeping the opening tags.

    The body of a script is source, not markup: VALENCE's inline script composes
    `<a href="${s.u}">` inside a template literal, and an assertion that read it
    would report a pointer no consumer can see (the 2026-09-14 rule — scope the
    assertion to the thing it checks). The opening tag must survive, because
    `<script src>` is the single most important thing this check looks for.
    """
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(
        r"(<script\b[^>]*>)(.*?)(</script>)",
        lambda m: m.group(1) + " " + m.group(3),
        html,
        flags=re.S | re.I,
    )
    return html


def attrs_of(blob: str) -> dict:
    out = {}
    for m in ATTR_RE.finditer(blob):
        out[m.group(1).lower()] = (m.group(3) if m.group(3) is not None else m.group(4))
    return out


def split_srcset(value: str):
    for part in value.split(","):
        url = part.strip().split()[0] if part.strip() else ""
        if url:
            yield url


def classify(url: str):
    """-> ('ours'|'third'|'inert', host). Inert = relative, data:, blob:, #, mailto:."""
    u = url.strip()
    if not u or u.startswith(("#", "data:", "blob:", "about:", "javascript:")):
        return "inert", ""
    if u.startswith("//"):
        u = "https:" + u
    p = urlparse(u)
    if not p.scheme and not p.netloc:
        return "inert", ""          # relative or root-relative: our own origin
    if p.scheme in ("mailto", "tel", "sms"):
        return "inert", ""
    host = (p.netloc or "").lower().split("@")[-1].split(":")[0]
    if not host:
        return "inert", ""
    return ("ours" if host in OURS else "third"), host


def scan(html: str):
    """-> (auto, anchors, declared) — each a list of (why, url)."""
    auto, anchors, declared = [], [], []
    body = strip_noise(html)

    for m in TAG_RE.finditer(body):
        tag = m.group(1).lower()
        a = attrs_of(m.group(2) or "")

        if tag == "a":
            if a.get("href"):
                anchors.append(("a[href]", a["href"]))
            continue

        if tag == "link":
            href = a.get("href")
            if not href:
                continue
            rel = (a.get("rel") or "").strip().lower()
            rels = set(rel.split()) | {rel}
            if rels & FETCHING_REL:
                auto.append(("link[rel=%s]" % (rel or "?"), href))
            else:
                declared.append(("link[rel=%s]" % (rel or "?"), href))
            continue

        if tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if a.get("content") and key in (
                "og:image", "og:image:secure_url", "twitter:image", "og:url", "og:audio", "og:video"
            ):
                declared.append(("meta[%s]" % key, a["content"]))
            continue

        for attr in AUTO_ATTRS.get(tag, ()):
            val = a.get(attr)
            if not val:
                continue
            if attr == "srcset":
                for u in split_srcset(val):
                    auto.append(("%s[srcset]" % tag, u))
            else:
                auto.append(("%s[%s]" % (tag, attr), val))

        if a.get("style"):
            for u in CSS_URL_RE.findall(a["style"]):
                auto.append(("%s[style url()]" % tag, u))

    for block in STYLE_BLOCK_RE.findall(body):
        for u in CSS_URL_RE.findall(block):
            auto.append(("style url()", u))
        for u in CSS_IMPORT_RE.findall(block):
            auto.append(("style @import", u))

    return auto, anchors, declared


def main() -> int:
    dist = sys.argv[1] if len(sys.argv) > 1 else "web/dist"
    if not os.path.isdir(dist):
        print("FAIL qa_third_party_origins — no such directory: %s" % dist)
        return 2

    pages = []
    for root, _dirs, files in os.walk(dist):
        for f in sorted(files):
            if f.endswith(".html"):
                pages.append(os.path.join(root, f))
    pages.sort()

    if not pages:
        print("FAIL qa_third_party_origins — no HTML in %s. An empty "
              "enumeration is not a clean site (08-16 silent-pass trap)." % dist)
        return 2

    defects = []          # (page, why, url, host)
    bare = []             # pages with no automatic reference at all
    n_auto = n_anchor = n_declared = 0
    hosts_auto = {}
    anchor_hosts = set()

    for path in pages:
        rel = os.path.relpath(path, dist).replace(os.sep, "/")
        html = open(path, encoding="utf-8", errors="replace").read()
        auto, anchors, declared = scan(html)
        n_auto += len(auto)
        n_anchor += len(anchors)
        n_declared += len(declared)

        if not auto and rel not in NO_AUTO_REF_OK:
            bare.append(rel)

        for why, url in auto:
            kind, host = classify(url)
            if kind == "third":
                defects.append((rel, why, url, host))
                hosts_auto[host] = hosts_auto.get(host, 0) + 1
        for _why, url in anchors:
            kind, host = classify(url)
            if kind == "third":
                anchor_hosts.add(host)

    print("qa_third_party_origins — %d served page(s)" % len(pages))
    print("  automatic references (asserted) ....... %d" % n_auto)
    print("  reader-initiated <a href> (NOT asserted) %d, across %d external origin(s)"
          % (n_anchor, len(anchor_hosts)))
    print("  declarations (NOT asserted) ........... %d  [link rel=alternate/canonical, og/twitter image]"
          % n_declared)
    print("  the second line is the publication working as designed: a citation is a link a")
    print("  reader chooses to follow, and counting it here would report our own method as a defect.")

    if bare:
        print("\nFAIL qa_third_party_origins — %d page(s) carry NO automatic reference "
              "at all, so there was nothing to classify:" % len(bare))
        for rel in bare[:20]:
            print("  %s" % rel)
        if len(bare) > 20:
            print("  ... and %d more" % (len(bare) - 20))
        print("Every page built from Base.astro links at least our own stylesheet and the")
        print("font bundle. Nothing matched, which means the parser stopped seeing the")
        print("served shape — a green here would be the 09-14 trap in standing form.")
        return 3

    if defects:
        print("\nDEFECT — %d automatic reference(s) to an origin we do not own, "
              "on %d page(s):" % (len(defects), len({d[0] for d in defects})))
        for host, n in sorted(hosts_auto.items(), key=lambda kv: -kv[1]):
            print("  %-34s %d reference(s)" % (host, n))
        print("  first %d, by page:" % min(12, len(defects)))
        for rel, why, url, _host in defects[:12]:
            print("    %s  %s -> %s" % (rel, why, url[:96]))
        if len(defects) > 12:
            print("    ... and %d more" % (len(defects) - 12))
        print("\nFAIL qa_third_party_origins — the reader's browser contacts "
              "%d origin(s) we do not own before the reader asks it to." % len(hosts_auto))
        return 1

    print("\nCLEAN qa_third_party_origins — every one of the %d automatic references "
          "across %d pages\nresolves to our own origin or to a relative path. The reader's "
          "browser contacts\nnobody but us before the reader acts." % (n_auto, len(pages)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
