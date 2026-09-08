#!/usr/bin/env python3
"""
qa_body_links — standing assertion #10 (2026-09-06).

The 2026-09-04 forward question: ten checks read `dist` or the origin and every
one of them enumerates URLs and their metadata; none reads an ARTICLE for what
it promises the reader. This answers it — and the first thing the answer found
is that the obvious assertion ("every in-body internal link dereferences") is a
silent pass: no article in either language composes a markdown link in its
body (0 of 76, by design — the reader's links are the sources list and the
related rail, both generated from frontmatter). An assertion with nothing to
enumerate has failed, not passed (2026-08-16), so the surface is re-derived to
what the article ACTUALLY promises, and each promise is asserted by EXISTENCE
in the built page (ruling #37), never by presence in the frontmatter:

  1. `related:` — every slug an approved article declares must (a) name an
     approved article in the SAME collection and (b) be rendered as an <a href>
     inside <nav class="related"> on the built page. RelatedReading.astro
     filters unresolvable slugs SILENTLY (robustness: a parked piece can never
     leave a dead link) — which is exactly a green light wired to nothing for a
     typo'd or stale slug. The component keeps its silence for the reader; this
     check breaks it for the operation.
  2. `sources[].url` — every source URL an approved article declares must be
     rendered as an <a href> in <ol class="sources"> on the built page, and no
     approved page may carry a placeholder source (the template's own
     "PLACEHOLDER SOURCE" / example.com convention) — a held piece may, an
     approved one may not.
  3. In-body markdown links — enumerated and REPORTED as a count; internal ones
     (`/...` or our origin) are dereferenced to dist. A zero is printed as a
     count, not claimed as a pass.
  4. Twin rails + dead ends (added the same day, from the Growth audit): an EN
     piece and its `arabicVersion` twin declare the same `related:` list, and
     the rail graph has no dead ends — every approved page has a rail and is
     pointed at by at least one piece. Twelve of thirty-eight pages failed this
     on first contact (six Edition-01 pages with no rail, six Edition-03/04
     pages nothing pointed at) and one twin rail had drifted (Singapore).

Scope: only files in the build path with `approved: true` (held files are not
built; their promises are gated at the wave flip). Both collections.

Usage: python3 agents/tools/qa_body_links.py [dist_dir] [--src web/src/content]
Exit 0 = PASS, 1 = FAIL (defects listed), 2 = usage/setup.

Proved per ruling #35 on 2026-09-06: control (the real build) silent; bite 1 — a
bogus `related:` slug added to an approved EN article and the site rebuilt →
FAIL(1) naming slug and page; bite 2 — one source <a> removed from a built AR
page → FAIL(1) naming URL and page; bite 3 — a placeholder source title on an
approved page → FAIL(1). See agents/logs/qa-2026-09-06.md.
"""
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

ORIGIN = "https://education3881.github.io/madar"


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    if yaml is None:
        print("qa_body_links: PyYAML missing — cannot parse frontmatter", file=sys.stderr)
        sys.exit(2)
    data = yaml.safe_load(m.group(1)) or {}
    return data if isinstance(data, dict) else {}


def body(text: str) -> str:
    m = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    return text[m.end():] if m else text


def hrefs_in(block: str) -> set:
    return set(re.findall(r'href="([^"]+)"', block))


def section(html: str, open_re: str) -> str:
    """Return the html from the first match of open_re to the matching close of
    that element's tag name (shallow — enough for <nav>/<ol> blocks here)."""
    m = re.search(open_re, html)
    if not m:
        return ""
    tag = re.match(r"<(\w+)", m.group(0)).group(1)
    end = html.find(f"</{tag}>", m.end())
    return html[m.start(): end if end != -1 else len(html)]


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    dist = Path(args[0] if args else "web/dist")
    src = Path("web/src/content")
    for i, a in enumerate(argv):
        if a == "--src" and i + 1 < len(argv):
            src = Path(argv[i + 1])
    if not dist.is_dir() or not src.is_dir():
        print(f"qa_body_links: need dist ({dist}) and src ({src})")
        return 2

    collections = {
        "en": (src / "articles", dist / "articles", "/madar/articles/"),
        "ar": (src / "articles-ar", dist / "ar" / "articles", "/madar/ar/articles/"),
    }
    defects = []
    n_pages = n_related = n_sources = n_body_links = n_body_internal = 0

    for lang, (sdir, ddir, base) in collections.items():
        files = sorted(sdir.glob("*.md"))
        approved = {}
        for f in files:
            fm = frontmatter(f.read_text(encoding="utf-8"))
            if fm.get("approved") is True:
                approved[f.stem] = fm
        for slug, fm in approved.items():
            n_pages += 1
            page = ddir / slug / "index.html"
            if not page.is_file():
                defects.append(f"[{lang}] {slug}: approved but not built at {page}")
                continue
            html = page.read_text(encoding="utf-8")

            # 1. related rail — declared slugs exist, are approved, and render.
            rel = fm.get("related") or []
            rail = section(html, r'<nav class="related"[^>]*>')
            rail_hrefs = hrefs_in(rail)
            for r in rel:
                n_related += 1
                if r not in approved:
                    defects.append(f"[{lang}] {slug}: related slug '{r}' is not an approved article in {sdir.name} (silently dropped by RelatedReading)")
                    continue
                want = f"{base}{r}/"
                if want not in rail_hrefs:
                    defects.append(f"[{lang}] {slug}: related slug '{r}' resolves but is NOT rendered in the related rail (expected href {want})")
            if rel and not rail:
                defects.append(f"[{lang}] {slug}: declares {len(rel)} related slug(s) but the built page has no <nav class=\"related\">")

            # 2. sources — every declared URL rendered as a link; no placeholders.
            sources = fm.get("sources") or []
            olist = section(html, r'<ol class="sources"[^>]*>')
            src_hrefs = hrefs_in(olist)
            for s in sources:
                n_sources += 1
                url = (s or {}).get("url", "") if isinstance(s, dict) else ""
                title = (s or {}).get("title", "") if isinstance(s, dict) else ""
                if re.search(r"PLACEHOLDER SOURCE", title, re.I) or re.match(r"^https?://example\.com/", url):
                    defects.append(f"[{lang}] {slug}: placeholder source on an APPROVED page — '{title[:60]}' {url}")
                    continue
                if not url:
                    defects.append(f"[{lang}] {slug}: source without a url — '{title[:60]}'")
                    continue
                if url not in src_hrefs:
                    # Astro escapes & as &amp; in attributes.
                    if url.replace("&", "&amp;") not in src_hrefs:
                        defects.append(f"[{lang}] {slug}: source url not rendered as a link in <ol class=\"sources\">: {url}")
            if sources and not olist:
                defects.append(f"[{lang}] {slug}: declares {len(sources)} source(s) but the built page has no <ol class=\"sources\">")

            # 3. in-body markdown links — count, and dereference internal ones.
            text = body((sdir / f"{slug}.md").read_text(encoding="utf-8"))
            for m in re.finditer(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
                target = m.group(1)
                n_body_links += 1
                internal = None
                if target.startswith(ORIGIN):
                    internal = target[len(ORIGIN):]
                elif target.startswith("/madar/"):
                    internal = target[len("/madar"):]
                elif target.startswith("/"):
                    internal = target
                if internal is not None:
                    n_body_internal += 1
                    p = internal.split("#")[0].split("?")[0]
                    cand = dist / p.strip("/")
                    ok = cand.is_file() or (cand / "index.html").is_file()
                    if not ok:
                        defects.append(f"[{lang}] {slug}: in-body internal link does not dereference to dist: {target}")

    # 4. Twin rails agree, and the rail graph has no dead ends (2026-09-06 audit).
    #    One argument in two compositions has one set of neighbours: an EN piece
    #    and its `arabicVersion` twin must declare the same `related:` list
    #    (found drifting on Singapore, 09-06 — both rails resolved, so nothing
    #    saw it: parity counts files, not content). Dead ends — an approved page
    #    with no rail, or one no rail points at — are reported as counts and
    #    FAIL, because the rail is the only in-page return path a reader has.
    en_src, _, _ = collections["en"]
    ar_src, _, _ = collections["ar"]
    en_fm = {f.stem: frontmatter(f.read_text(encoding="utf-8")) for f in en_src.glob("*.md")}
    ar_fm = {f.stem: frontmatter(f.read_text(encoding="utf-8")) for f in ar_src.glob("*.md")}
    en_ok = {s for s, d in en_fm.items() if d.get("approved") is True}
    ar_ok = {s for s, d in ar_fm.items() if d.get("approved") is True}
    n_twins = 0
    for s in sorted(en_ok):
        twin = en_fm[s].get("arabicVersion")
        if twin and twin in ar_ok:
            n_twins += 1
            a = list(en_fm[s].get("related") or [])
            b = list(ar_fm[twin].get("related") or [])
            if a != b:
                defects.append(f"[twin] {s}: related rail differs EN {a} vs AR {b} — one argument, one set of neighbours")
    dead_ends = []
    for lang, (sdir, ddir, base) in collections.items():
        fms = en_fm if lang == "en" else ar_fm
        ok = en_ok if lang == "en" else ar_ok
        inbound = {}
        for s in ok:
            for r in (fms[s].get("related") or []):
                if r in ok:
                    inbound[r] = inbound.get(r, 0) + 1
        for s in sorted(ok):
            out = [r for r in (fms[s].get("related") or []) if r in ok]
            if not out:
                dead_ends.append(f"[{lang}] {s}: no rail (dead end)")
            if inbound.get(s, 0) == 0:
                dead_ends.append(f"[{lang}] {s}: no piece points at it")
    defects.extend(dead_ends)

    print(f"qa_body_links: approved pages {n_pages} · related promises {n_related} · source promises {n_sources} · in-body links {n_body_links} (internal {n_body_internal}) · twin rails compared {n_twins} · rail dead ends {len(dead_ends)}")
    if n_body_links == 0:
        print("note: 0 in-body links composed in either language — reported as a count, not a pass; the assertion's substance is the rail and the sources list.")
    if n_related == 0 or n_sources == 0:
        print("FAIL — nothing to enumerate on a live corpus (silent-pass trap)")
        return 1
    if defects:
        print(f"FAIL({len(defects)}) — a promise the article makes in frontmatter is not kept on the built page:")
        for d in defects:
            print("  - " + d)
        return 1
    print("PASS — every related slug and every source URL an approved article declares is rendered on its built page; no placeholder sources on approved pages; twin rails agree; no rail dead ends.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
