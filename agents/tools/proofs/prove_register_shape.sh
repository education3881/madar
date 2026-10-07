#!/usr/bin/env bash
# Proof harness for standing assertion 30, qa_register_shape (ruling #90).
#
# Runs every branch of the assertion against a COPY of the tree in /tmp, so the
# real working tree is never mutated and a failed experiment cannot leave a
# bite behind. Per ruling #74: every injection is asserted to have CHANGED the
# file before the check is run on it — an injection that fails to change the
# artefact reads exactly like a passing control.
#
# Usage: bash agents/tools/proofs/prove_register_shape.sh
set -u

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
TOOL="agents/tools/qa_register_shape.py"
PASS=0; FAIL=0

# The values this harness falsifies are DERIVED from the tree, never hardcoded.
# They were hardcoded on the first write and all four range bites broke the
# same day — because the thing they prove moved, by the ruling they prove.
# The #74 guard caught it ("INJECTION DID NOT CHANGE THE FILE") rather than
# letting four non-injections read as passes, which is the whole reason that
# guard exists. A proof harness is an artefact like any other: a fixture that
# names a moving number goes stale exactly like a staged patch does (#75).
eval "$(python3 - "$ROOT" <<'PY'
import re,sys,pathlib
root=pathlib.Path(sys.argv[1])
idx=(root/"agents/guidebook/INDEX.md").read_text(encoding="utf-8")
hi=max(int(m) for m in re.findall(r'^\| (\d+) \|',idx,re.M))
h=re.search(r'\*\*([A-Za-z\-]+) rows, 1 → (\d+)',idx)
fam=re.search(r'([a-z\-]+) of ([a-z\-]+) rulings',idx[idx.index("families the register makes visible"):])
print(f"HI={hi}")
print(f"S1WORD={h.group(1)}")
print(f"S1NUM={h.group(2)}")
print(f"RATIO='{fam.group(0)}'")
print(f"RATIODEN={fam.group(2)}")
PY
)"
echo "derived from the tree: register ends at #$HI · §1 count line '$S1WORD rows, 1 → $S1NUM' · families ratio '$RATIO'"
echo

work() {            # fresh copy of the tree for one experiment
  local d; d="$(mktemp -d /tmp/qrs.XXXXXX)"
  cp -a "$ROOT/CLAUDE.md" "$d/" 2>/dev/null
  mkdir -p "$d/agents" "$d/content-drafts"
  cp -a "$ROOT/agents/." "$d/agents/" 2>/dev/null
  cp -a "$ROOT/content-drafts/." "$d/content-drafts/" 2>/dev/null
  echo "$d"
}

# changed <dir> <relpath> <before-sha>  — ruling #74's guard
changed() {
  local now; now="$(sha256sum "$1/$2" | cut -d' ' -f1)"
  [ "$now" != "$3" ]
}

run() {             # run <label> <expected-exit> <dir> [args...]
  local label="$1" want="$2" dir="$3"; shift 3
  local out; out="$(cd "$dir" && python3 "$ROOT/$TOOL" . "$@" 2>&1)"; local got=$?
  if [ "$got" -eq "$want" ]; then
    PASS=$((PASS+1)); printf '  PASS  %-58s exit %d\n' "$label" "$got"
  else
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s exit %d, wanted %d\n' "$label" "$got" "$want"
    echo "$out" | sed 's/^/        /'
  fi
  LAST_OUT="$out"
}

# inject <label> <relpath> <sed-expr> <expected-exit> [args...]
inject() {
  local label="$1" rel="$2" expr="$3" want="$4"; shift 4
  local d; d="$(work)"
  local before; before="$(sha256sum "$d/$rel" | cut -d' ' -f1)"
  sed -i "$expr" "$d/$rel"
  if ! changed "$d" "$rel" "$before"; then
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s INJECTION DID NOT CHANGE THE FILE\n' "$label"
    rm -rf "$d"; return
  fi
  run "$label" "$want" "$d" "$@"
  rm -rf "$d"
}

echo "=== CONTROL — the real tree, both limbs, must be silent ==="
run "control, both limbs" 0 "$ROOT"
run "control, --shape only" 0 "$ROOT" --shape
run "control, --register only" 0 "$ROOT" --register

echo
echo "=== LIMB 1 BITES — shape ==="

# 1. a cell removed from a guidebook ruling row (the 10-04 defect, 5 rows)
inject "ruling row loses a cell (the 10-04 defect)" \
  agents/guidebook/INDEX.md \
  's#^| 50 | \(.*\) | \(.*\) | \(.*\) |$#| 50 | \1 | \2 |#' 1 --shape

# 2. a row wrapped across physical lines (the 10-06 ledger defect)
d="$(work)"
before="$(sha256sum "$d/agents/guidebook/INDEX.md" | cut -d' ' -f1)"
python3 - "$d/agents/guidebook/INDEX.md" <<'PY'
import sys,re
p=sys.argv[1]; L=open(p,encoding="utf-8").read().splitlines()
for i,l in enumerate(L):
    if l.startswith("| 50 |"):
        half=len(l)//2
        L[i:i+1]=[l[:half], l[half:]]   # break one row across two lines
        break
open(p,"w",encoding="utf-8").write("\n".join(L)+"\n")
PY
if changed "$d" agents/guidebook/INDEX.md "$before"; then
  run "row wrapped across two lines (the 10-06 defect)" 1 "$d" --shape
else
  FAIL=$((FAIL+1)); echo "  FAIL  wrapped-row injection did not change the file"
fi
rm -rf "$d"

# 3. a table row with no header governing it.
#    NOTE: this bite is the one that FAILED on first run and changed the tool.
#    Appending an orphan row to RUNBOOK.md passed, because the file's earlier
#    `| Thing | Path |` header was still governing at end-of-file and the orphan
#    happened to be the same width. A header now loses authority at the next
#    heading, so the orphan row must sit under its own heading to be orphaned —
#    which is what a real stray table looks like.
d="$(work)"
printf '\n## A heading, which ends the previous table header authority\n\n| orphan row | with no header above it |\n' \
  >> "$d/agents/RUNBOOK.md"
run "orphan row under a later heading (width coincides)" 1 "$d" --shape
rm -rf "$d"

# 3b. and the continuation case must still be SILENT — the guidebook's §1/§3
#     blocks are one table interrupted by prose, and prose is not a heading.
d="$(work)"
printf '\n| H1 | H2 |\n|---|---|\n| a | b |\n\nprose interrupting the table\n\n| c | d |\n' \
  >> "$d/agents/RUNBOOK.md"
run "continuation block after PROSE stays silent (control)" 0 "$d" --shape
rm -rf "$d"

# 4. FENCE CONTROL — a piped shell line inside a fence must stay SILENT,
#    and the same line with the fence removed must BITE. This is the pair
#    that proves the fence rule is a rule and not a blanket exemption.
d="$(work)"
printf '\n```bash\n|| [ $? -eq 3 ]\n```\n' >> "$d/agents/RUNBOOK.md"
run "shell pipe INSIDE a fence stays silent (control)" 0 "$d" --shape
rm -rf "$d"
d="$(work)"
printf '\n|| [ $? -eq 3 ]\n' >> "$d/agents/RUNBOOK.md"
run "same shell pipe with NO fence bites" 1 "$d" --shape
rm -rf "$d"

# 5. ESCAPED-PIPE CONTROL — the 23-day-wrong specification. A row that
#    correctly escapes a pipe must stay silent; the naive split would fail it.
d="$(work)"
printf '\n| H1 | H2 |\n|---|---|\n| a row quoting `x \\| y` | and staying well-formed |\n' \
  >> "$d/agents/RUNBOOK.md"
run "row with a correctly ESCAPED pipe stays silent" 0 "$d" --shape
rm -rf "$d"

echo
echo "=== LIMB 2 BITES — the four homes of the range ==="

inject "§3's heading says the wrong range" agents/guidebook/INDEX.md \
  "s/^## 3\\. The ruling register — #1–#$HI/## 3. The ruling register — #1–#$((HI-1))/" 1 --register

inject "the series-integrity line says the wrong range" agents/guidebook/INDEX.md \
  "s/\*\*Series integrity: #1–#$HI/**Series integrity: #1–#$((HI-1))/" 1 --register

inject "§1's count NUMERAL disagrees with its rows" agents/guidebook/INDEX.md \
  "s/\*\*$S1WORD rows, 1 → $S1NUM/**$S1WORD rows, 1 → $((S1NUM-1))/" 1 --register

inject "§1's count WORD disagrees while the numeral is right" agents/guidebook/INDEX.md \
  "s/\*\*$S1WORD rows, 1 → $S1NUM/**Thirteen rows, 1 → $S1NUM/" 1 --register

inject "CLAUDE.md's non-negotiable range is stale" CLAUDE.md \
  "s/currently \*\*#1–#$HI\*\*/currently **#1–#$((HI-1))**/" 1 --register

# THE SIXTH HOME — the families list's ratio denominator. This is the one that
# was stale on the real tree when the limb was written, and the one the 10-04
# consolidation had already named once.
inject "the families list's ratio DENOMINATOR is stale" agents/guidebook/INDEX.md \
  "s/$RATIO/twenty-eight of thirteen rulings/" 1 --register

# ...and its SCOPE control, which is the half that was got wrong first: the
# series-integrity line quotes every superseded ratio ON PURPOSE, and asserting
# §3 wholesale made the register's record of its own drift a build failure.
d="$(work)"
before="$(sha256sum "$d/agents/guidebook/INDEX.md" | cut -d' ' -f1)"
python3 - "$d/agents/guidebook/INDEX.md" <<'PY'
import sys
p=sys.argv[1]; t=open(p,encoding="utf-8").read()
# a historical ratio quoted inside §3's narrative, outside the families bullets
t=t.replace("**Series integrity:",
            "*(historically this read seventeen of seventy-one rulings.)* **Series integrity:",1)
open(p,"w",encoding="utf-8").write(t)
PY
if changed "$d" agents/guidebook/INDEX.md "$before"; then
  run "a HISTORICAL ratio in §3's narrative stays silent (control)" 0 "$d" --register
else
  FAIL=$((FAIL+1)); echo "  FAIL  historical-ratio injection did not change the file"
fi
rm -rf "$d"

# and if the families list cannot be found at all, that is reported, not passed
inject "families list cue removed -> reported, not clean" agents/guidebook/INDEX.md \
  's/families the register makes visible/families the register makes plain/' 1 --register

# a ruling row deleted leaves every quoted home self-consistent and the
# POPULATION short — the #57 shape, and the one a four-home check alone misses
d="$(work)"
before="$(sha256sum "$d/agents/guidebook/INDEX.md" | cut -d' ' -f1)"
sed -i '/^| 50 | A superlative is a figure/d;/^| 50 |/d' "$d/agents/guidebook/INDEX.md"
if changed "$d" agents/guidebook/INDEX.md "$before"; then
  run "a ruling row DELETED — gap in the population" 1 "$d" --register
  echo "$LAST_OUT" | grep -q "missing ruling rows: #50" \
    && { PASS=$((PASS+1)); echo "  PASS  ...and it names #50 by number"; } \
    || { FAIL=$((FAIL+1)); echo "  FAIL  ...but it did not name #50"; }
else
  FAIL=$((FAIL+1)); echo "  FAIL  row-deletion injection did not change the file"
fi
rm -rf "$d"

# a duplicated ruling number
d="$(work)"
before="$(sha256sum "$d/agents/guidebook/INDEX.md" | cut -d' ' -f1)"
python3 - "$d/agents/guidebook/INDEX.md" <<'PY'
import sys
p=sys.argv[1]; L=open(p,encoding="utf-8").read().splitlines()
for i,l in enumerate(L):
    if l.startswith("| 50 |"):
        L.insert(i+1,l); break
open(p,"w",encoding="utf-8").write("\n".join(L)+"\n")
PY
if changed "$d" agents/guidebook/INDEX.md "$before"; then
  run "a ruling number DUPLICATED" 1 "$d" --register
else
  FAIL=$((FAIL+1)); echo "  FAIL  duplication injection did not change the file"
fi
rm -rf "$d"

echo
echo "=== FAILURE TO CHECK — a check that cannot look must not report clean ==="

d="$(work)"; rm -f "$d/agents/guidebook/INDEX.md"
run "INDEX.md absent -> exit 3, not 0" 3 "$d" --register
rm -rf "$d"

inject "§3's heading renamed -> exit 3, not 0" agents/guidebook/INDEX.md \
  's/^## 3\. The ruling register.*$/## 3. Something else entirely/' 3 --register

d="$(work)"
python3 - "$d/agents/guidebook/INDEX.md" <<'PY'
import sys,re
p=sys.argv[1]; L=open(p,encoding="utf-8").read().splitlines()
out=[l for l in L if not re.match(r'^\| \d+ \|',l)]
open(p,"w",encoding="utf-8").write("\n".join(out)+"\n")
PY
run "§3 has no numbered rows at all -> exit 3" 3 "$d" --register
rm -rf "$d"

d="$(mktemp -d /tmp/qrs.XXXXXX)"   # a tree with no markdown at all
run "no table rows in scope -> exit 3, not 0" 3 "$d" --shape
rm -rf "$d"

out="$(python3 "$ROOT/$TOOL" /tmp/does-not-exist-qrs 2>&1)"; got=$?
if [ "$got" -eq 3 ]; then PASS=$((PASS+1)); printf '  PASS  %-58s exit 3\n' "nonexistent root -> exit 3"
else FAIL=$((FAIL+1)); printf '  FAIL  %-58s exit %d\n' "nonexistent root" "$got"; fi

out="$(python3 "$ROOT/$TOOL" 2>&1)"; got=$?
if [ "$got" -eq 2 ]; then PASS=$((PASS+1)); printf '  PASS  %-58s exit 2\n' "no argument -> usage, exit 2"
else FAIL=$((FAIL+1)); printf '  FAIL  %-58s exit %d\n' "no argument" "$got"; fi

echo
echo "=== CONTROL RESTORED — the real tree is still silent after all of it ==="
run "control re-run, both limbs" 0 "$ROOT"

echo
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
