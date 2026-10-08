#!/usr/bin/env bash
# Proof harness for qa_third_party_origins (standing assertion #31), 2026-10-08.
#
# Per #35 (prove both ways), #74 (prove the BITE first and as carefully as the
# control) and the 2026-09-14 rule (an injection that fails to change the
# artefact reads exactly like a passing control — so assert the mutation).
#
# Everything runs on a COPY of dist in a scratch directory, so a failed
# experiment cannot leave a mutation in the tree. That is the 2026-10-07
# precedent, adopted after a proof harness mutated the file it was proving.
#
# Nothing here is hardcoded about the corpus. The 10-07 harness went stale
# within the hour on its own `#89` and `85 rows`; every number below is derived
# from the tree at run time.
#
# Usage:  bash agents/tools/proofs/qa_third_party_origins_proof.sh [web/dist]

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
SRC_DIST="${1:-$ROOT/web/dist}"
TOOL="$ROOT/agents/tools/qa_third_party_origins.py"
WORK="$(mktemp -d /tmp/qa31-proof-XXXXXX)"
trap 'rm -rf "$WORK"' EXIT

pass=0; fail=0

say() { printf '\n== %s\n' "$*"; }

# Fresh copy of dist for each case: an injection must never be able to leak into
# the next case and make a later bite pass for the wrong reason.
fresh() {
  rm -rf "$WORK/dist"
  cp -r "$SRC_DIST" "$WORK/dist"
}

run() { python3 -I "$TOOL" "$WORK/dist" >"$WORK/out" 2>&1; echo $?; }

# A page every build produces, derived rather than named.
PAGE_REL="$(cd "$SRC_DIST" && ls index.html 2>/dev/null || true)"
if [ -z "$PAGE_REL" ]; then
  echo "ABORT — no index.html in $SRC_DIST; nothing to inject into."
  exit 9
fi

# expect <label> <wanted-exit> <must-appear-in-output-or-"-">
expect() {
  local label="$1" want="$2" needle="$3" got
  got="$(run)"
  if [ "$got" != "$want" ]; then
    printf 'FAIL  %-58s exit %s, wanted %s\n' "$label" "$got" "$want"
    sed -n '1,8p' "$WORK/out" | sed 's/^/        /'
    fail=$((fail+1)); return
  fi
  if [ "$needle" != "-" ] && ! grep -qF "$needle" "$WORK/out"; then
    printf 'FAIL  %-58s exit %s but output never says %s\n' "$label" "$got" "$needle"
    fail=$((fail+1)); return
  fi
  printf 'ok    %-58s exit %s\n' "$label" "$got"
  pass=$((pass+1))
}

# inject <file> <sed-expression> — and PROVE the file changed (09-14).
inject() {
  local f="$WORK/dist/$1" expr="$2" before after
  before="$(md5sum "$f" | cut -d' ' -f1)"
  perl -0pi -e "$expr" "$f"
  after="$(md5sum "$f" | cut -d' ' -f1)"
  if [ "$before" = "$after" ]; then
    printf 'FAIL  INJECTION DID NOT CHANGE THE FILE: %s\n' "$1"
    fail=$((fail+1)); return 1
  fi
  return 0
}

echo "qa_third_party_origins — proof harness"
echo "source dist: $SRC_DIST"
echo "scratch:     $WORK"
echo "page used for injections: $PAGE_REL"

# ---------------------------------------------------------------- THE BITES
# The bite goes first. A control that runs before any bite has been shown to
# work is a green with nothing behind it.

say "BITE 1 — the REAL defect, re-injected exactly as it shipped until 2026-10-08"
# Not a composed bite: this is the verbatim markup removed from Base.astro today,
# which is the qa_chrome_links precedent — re-inject your own history, because a
# check proved only against invented defects is a check proved against your
# imagination.
fresh
inject "$PAGE_REL" 's{<head>}{<head><link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin /><link href="https://fonts.googleapis.com/css2?family=Amiri\&display=swap" rel="stylesheet" />}' \
  && expect "the shipped Google Fonts markup" 1 "fonts.googleapis.com"
grep -qF "fonts.gstatic.com" "$WORK/out" \
  && { printf 'ok    %-58s both origins named\n' "and it names gstatic too"; pass=$((pass+1)); } \
  || { printf 'FAIL  %-58s gstatic not named\n' "and it names gstatic too"; fail=$((fail+1)); }

say "BITE 2 — the tracker the CHARTER forbids, as a <script src>"
fresh
inject "$PAGE_REL" 's{</head>}{<script src="https://cdn.analytics.example/track.js"></script></head>}' \
  && expect "third-party script[src]" 1 "cdn.analytics.example"

say "BITE 3 — a tracking pixel as <img src>"
fresh
inject "$PAGE_REL" 's{</body>}{<img src="https://pixel.example.net/p.gif" width="1" height="1" /></body>}' \
  && expect "third-party img[src]" 1 "pixel.example.net"

say "BITE 4 — @import inside a <style> block"
fresh
inject "$PAGE_REL" 's{</head>}{<style>\@import "https://evil-css.example/x.css";</style></head>}' \
  && expect "third-party style @import" 1 "evil-css.example"

say "BITE 5 — url() in a style=\"\" attribute"
fresh
inject "$PAGE_REL" 's{<body}{<body style="background:url(https://bg.example.org/t.png)"}' \
  && expect "third-party style url()" 1 "bg.example.org"

say "BITE 6 — an embedded <iframe src>"
fresh
inject "$PAGE_REL" 's{</body>}{<iframe src="https://embed.example.com/w"></iframe></body>}' \
  && expect "third-party iframe[src]" 1 "embed.example.com"

say "BITE 7 — PROTOCOL-RELATIVE preload, which has no scheme to match on"
fresh
inject "$PAGE_REL" 's{</head>}{<link rel="preload" as="font" href="//fonts.gstatic.com/s/x.woff2" crossorigin></head>}' \
  && expect "protocol-relative //host normalised" 1 "fonts.gstatic.com"

say "BITE 8 — srcset, where the URL is not the whole attribute"
fresh
inject "$PAGE_REL" 's{</body>}{<img srcset="https://cdn.example.io/a.png 1x, https://cdn.example.io/b.png 2x" src="/madar/stills/x.svg"></body>}' \
  && expect "third-party img[srcset] descriptor parsed" 1 "cdn.example.io"

say "BITE 9 — <use xlink:href>, the SVG surface our wordmark lives on"
fresh
inject "$PAGE_REL" 's{</body>}{<svg><use xlink:href="https://sprites.example/s.svg#m"/></svg></body>}' \
  && expect "third-party use[xlink:href]" 1 "sprites.example"

# ------------------------------------------------------- THE OVER-MATCH PROOFS
# These matter as much as the bites. A check that fails on a citation would be
# switched off inside a week, and this publication's whole method is citations.

say "CONTROL-NEGATIVE 1 — a CITATION must not bite (the 09-18 classification)"
fresh
inject "$PAGE_REL" 's{</body>}{<a href="https://www.unicef.org/reports/x">a named primary source</a></body>}' \
  && expect "external <a href> stays silent" 0 "NOT asserted"

say "CONTROL-NEGATIVE 2 — the share rail must not bite"
fresh
inject "$PAGE_REL" 's{</body>}{<a href="https://wa.me/?text=x">share</a><a href="https://x.com/intent/post?url=y">share</a></body>}' \
  && expect "wa.me and x.com stay silent" 0 "-"

say "CONTROL-NEGATIVE 3 — a DECLARATION must not bite (rel=alternate)"
fresh
inject "$PAGE_REL" 's{</head>}{<link rel="alternate" type="application/rss+xml" href="https://elsewhere.example/feed.xml"></head>}' \
  && expect "link[rel=alternate] stays silent" 0 "-"

say "CONTROL-NEGATIVE 4 — og:image is qa_consumer_surface's subject, not ours"
fresh
inject "$PAGE_REL" 's{</head>}{<meta property="og:image" content="https://scraped.example/card.png"></head>}' \
  && expect "og:image stays silent, deliberately" 0 "-"

# -------------------------------------------------- FAILURE-TO-CHECK GUARDS
say "GUARD 1 — an empty dist is not a clean site (exit 2)"
rm -rf "$WORK/dist"; mkdir -p "$WORK/dist"
expect "no HTML at all" 2 "empty enumeration is not a clean site"

say "GUARD 2 — a missing directory (exit 2)"
rm -rf "$WORK/dist"
expect "no such directory" 2 "no such directory"

say "GUARD 3 — a page with NO automatic reference (exit 3)"
# The 09-14 trap in standing form: if the parser stops seeing the served shape,
# every page classifies as clean and the check reports a green it never earned.
#
# The first draft of this case renamed `<link` and expected exit 3. It got exit
# 0 — correctly — because the English home carries 15 automatic references and
# only 3 are <link>: eleven <img src> stills and covers, and one <script src>,
# all still there and all still classifying clean. **A guard proved by an
# injection that does not reach the condition is not a proved guard**, which is
# #74 pointed at a harness instead of at an assertion. The attributes
# themselves are renamed instead, so the page really does arrive with nothing
# to classify.
fresh
inject "$PAGE_REL" 's{\bsrc=}{data-src=}g; s{\bhref=}{data-href=}g; s{\bsrcset=}{data-srcset=}g' \
  && expect "nothing left to classify is NOT a pass" 3 "nothing to classify"

# ----------------------------------------------------------------- CONTROL
say "CONTROL — the real tree, unmutated, after every bite above"
fresh
expect "untouched dist is silent" 0 "CLEAN qa_third_party_origins"

# The control must also be shown to have classified something. A silent check
# over an empty enumeration is the defect guard 1 exists for, and the control is
# where it would hide.
N="$(grep -oE 'automatic references \(asserted\) \.+ [0-9]+' "$WORK/out" | grep -oE '[0-9]+$')"
if [ "${N:-0}" -gt 0 ]; then
  printf 'ok    %-58s %s references classified\n' "and it classified a non-empty population" "$N"; pass=$((pass+1))
else
  printf 'FAIL  %-58s classified nothing\n' "and it classified a non-empty population"; fail=$((fail+1))
fi

printf '\n---------------------------------------------\n'
printf 'qa_third_party_origins proof: %d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ] || exit 1
