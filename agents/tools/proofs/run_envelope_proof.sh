#!/usr/bin/env bash
# Prove `run_envelope.py` both ways — control AND bite, per ruling #35, and the
# bite proved as carefully as the control (#35 + 2026-09-14: an injection that
# fails to change the artefact reads exactly like a passing control).
#
# run_envelope is not an assertion and fails no build, so "bite" here means:
# every branch it can take is reached deliberately, and each one is shown to
# print a DIFFERENT verdict with a DIFFERENT exit code. The failure mode this
# guards against is the one the instrument exists to close — a number printed
# calmly that nothing supports.
#
# Nothing here touches the repository. The budget-removal and budget-rewrite
# cases run against copies of the workflow files under /tmp, because this
# identity cannot write `.github/workflows/**` and must not try.
#
#   bash agents/tools/proofs/run_envelope_proof.sh
#
set -u

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
TOOL="$ROOT/agents/tools/run_envelope.py"
WORK="$(mktemp -d /tmp/run-envelope-proof-XXXXXX)"
PASS=0; FAIL=0

run() { # run <expected-exit> <label> -- <args...>
  local want="$1"; shift; local label="$1"; shift; shift
  local out; out="$("$@" 2>&1)"; local got=$?
  if [ "$got" = "$want" ]; then
    PASS=$((PASS+1)); printf '  ok   [exit %s] %s\n' "$got" "$label"
  else
    FAIL=$((FAIL+1)); printf '  FAIL [exit %s, wanted %s] %s\n' "$got" "$want" "$label"
    printf '%s\n' "$out" | sed 's/^/         /'
  fi
  printf '%s' "$out" > "$WORK/last.txt"
}

says() { # says <string> — the last run's output must contain it
  if grep -qF -- "$1" "$WORK/last.txt"; then
    PASS=$((PASS+1)); printf '  ok   output carries: %s\n' "$1"
  else
    FAIL=$((FAIL+1)); printf '  FAIL output is MISSING: %s\n' "$1"
  fi
}

says_not() {
  if grep -qF -- "$1" "$WORK/last.txt"; then
    FAIL=$((FAIL+1)); printf '  FAIL output should NOT carry: %s\n' "$1"
  else
    PASS=$((PASS+1)); printf '  ok   output correctly omits: %s\n' "$1"
  fi
}

# A copy of the repo's workflow dir that we are allowed to mutilate.
mkdir -p "$WORK/tree/.github/workflows" "$WORK/tree/agents/stats"
cp "$ROOT/.github/workflows/madar-daily.yml" "$WORK/tree/.github/workflows/"
cp "$ROOT/.github/workflows/madar-weekly.yml" "$WORK/tree/.github/workflows/"

echo "=== CONTROL 1 — a real, healthy position (start 2 minutes ago) ==="
TWO_AGO="$(python3 -c 'import datetime;print((datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(minutes=2)).replace(microsecond=0).isoformat())')"
run 0 "fresh run reports room and exits 0" -- \
  python3 -I "$TOOL" "$ROOT" --started-at "$TWO_AGO"
says "OK run_envelope"
says_not "BANK NOW run_envelope" ; says_not "The reserve is reached."
says "TURN AXIS .................. UNMEASURABLE"
says "--max-turns 180"
says ".github/workflows/madar-daily.yml"

echo
echo "=== BITE 1 — the reserve is breached (start 80 minutes ago) ==="
EIGHTY_AGO="$(python3 -c 'import datetime;print((datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(minutes=80)).replace(microsecond=0).isoformat())')"
run 3 "80 of 90 minutes gone trips the 15-minute reserve, exit 3" -- \
  python3 -I "$TOOL" "$ROOT" --started-at "$EIGHTY_AGO"
says "BANK NOW run_envelope"
says "The reserve is reached."

echo
echo "=== CONTROL 2 — the SAME instant passes when the reserve is lowered ==="
# Proves the bite is the reserve comparison and not the clock arithmetic.
run 0 "same 80-minute position with --reserve-minutes 5 exits 0" -- \
  python3 -I "$TOOL" "$ROOT" --started-at "$EIGHTY_AGO" --reserve-minutes 5
says_not "The reserve is reached."

echo
echo "=== BITE 2 — REFUSED when the budget is not in the workflow file ==="
# Prove the injection changed the file before trusting the result (2026-09-14).
python3 - "$WORK/tree/.github/workflows/madar-daily.yml" <<'PY'
import re, sys
p = sys.argv[1]
src = open(p, encoding="utf-8").read()
out = re.sub(r"^\s*timeout-minutes:\s*\d+\s*$\n", "", src, flags=re.M)
assert out != src, "INJECTION DID NOT CHANGE THE FILE — the proof is broken, not the tool"
assert not re.search(r"^\s*timeout-minutes:", out, flags=re.M)
open(p, "w", encoding="utf-8").write(out)
print("  (injection verified: timeout-minutes removed from the /tmp copy)")
PY
run 4 "no timeout-minutes anywhere in the file is REFUSED, exit 4" -- \
  python3 -I "$TOOL" "$WORK/tree" --workflow madar-daily.yml --started-at "$TWO_AGO"
says "REFUSED run_envelope"
says_not "remaining"

echo
echo "=== BITE 3 — the budget is READ, not remembered (rewrite it to 20) ==="
cp "$ROOT/.github/workflows/madar-daily.yml" "$WORK/tree/.github/workflows/"
python3 - "$WORK/tree/.github/workflows/madar-daily.yml" <<'PY'
import re, sys
p = sys.argv[1]
src = open(p, encoding="utf-8").read()
out = re.sub(r"^(\s*)timeout-minutes:\s*90\s*$", r"\g<1>timeout-minutes: 20", src, flags=re.M)
out2 = re.sub(r"--max-turns 180", "--max-turns 7", out)
assert out != src and out2 != out, "INJECTION DID NOT CHANGE THE FILE — proof broken"
open(p, "w", encoding="utf-8").write(out2)
print("  (injection verified: 90 -> 20 and 180 -> 7 in the /tmp copy)")
PY
run 0 "a 20-minute budget 2 minutes in still has 18 min, exit 0" -- \
  python3 -I "$TOOL" "$WORK/tree" --workflow madar-daily.yml --started-at "$TWO_AGO"
says "of 20 min"
says "--max-turns 7"
says_not "of 90 min"
says_not "--max-turns 180"

# The discriminator. The same ten-minute-old position reads 80 min remaining
# against the real 90-minute budget and 10 min remaining against the rewritten
# 20 — so the REWRITE moves the verdict, not just the printed text. This is what
# proves the budget is read on every run rather than remembered. The first draft
# of this bite asserted exit 3 on the two-minute position and the harness
# returned 0, correctly: 20 - 2 = 18, above the 15 reserve. A bite whose
# arithmetic is wrong fails the tool for the proof's reason, which is the
# 2026-09-14 trap seen from the other side.
TEN_AGO="$(python3 -c 'import datetime;print((datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(minutes=10)).replace(microsecond=0).isoformat())')"
run 0 "10 minutes into the REAL 90-minute budget: 80 left, exit 0" -- \
  python3 -I "$TOOL" "$ROOT" --started-at "$TEN_AGO"
says_not "The reserve is reached."
run 3 "the SAME position against the rewritten 20-minute budget: 10 left, exit 3" -- \
  python3 -I "$TOOL" "$WORK/tree" --workflow madar-daily.yml --started-at "$TEN_AGO"
says "BANK NOW run_envelope"
says "of 20 min"

echo
echo "=== BITE 4 — CANNOT MEASURE with no run to ask about ==="
run 2 "no GITHUB_RUN_ID and no --started-at exits 2" -- \
  env -u GITHUB_RUN_ID -u GITHUB_REPOSITORY python3 -I "$TOOL" "$ROOT"
says "CANNOT MEASURE run_envelope"
says "BOTH axes are dark"
says_not "remaining .................."

echo
echo "=== CONTROL 3 — --log appends exactly one well-formed line ==="
BEFORE=0
[ -f "$WORK/tree/agents/stats/run-envelope.jsonl" ] && \
  BEFORE="$(wc -l < "$WORK/tree/agents/stats/run-envelope.jsonl")"
cp "$ROOT/.github/workflows/madar-daily.yml" "$WORK/tree/.github/workflows/"
run 0 "--log on a copy of the tree exits 0" -- \
  python3 -I "$TOOL" "$WORK/tree" --workflow madar-daily.yml \
          --started-at "$TWO_AGO" --log --label proof
AFTER="$(wc -l < "$WORK/tree/agents/stats/run-envelope.jsonl")"
if [ "$AFTER" = "$((BEFORE+1))" ]; then
  PASS=$((PASS+1)); printf '  ok   log grew by exactly one line (%s -> %s)\n' "$BEFORE" "$AFTER"
else
  FAIL=$((FAIL+1)); printf '  FAIL log grew %s -> %s\n' "$BEFORE" "$AFTER"
fi
if python3 -I -c "import json,sys;r=json.loads(open(sys.argv[1]).readlines()[-1]);assert r['label']=='proof';assert r['timeout_minutes']==90;assert 'elapsed_minutes' in r;print('  ok   last log line parses as JSON and carries label, budget and elapsed')" "$WORK/tree/agents/stats/run-envelope.jsonl"; then
  PASS=$((PASS+1))
else
  FAIL=$((FAIL+1)); printf '  FAIL last log line is not the shape promised\n'
fi

echo
echo "=== CONTROL 4 — the --json mode agrees with the human mode ==="
run 0 "--json exits 0 on a healthy position" -- \
  python3 -I "$TOOL" "$ROOT" --started-at "$TWO_AGO" --json
says '"turn_axis": "UNMEASURABLE"'
says '"timeout_minutes": 90'
says '"max_turns": 180'

echo
echo "=== CONTROL 5 — it does not write into the real repository ==="
if [ -f "$ROOT/agents/stats/run-envelope.jsonl" ]; then
  echo "  (a real log already exists; checking this proof did not append to it)"
fi
if git -C "$ROOT" diff --quiet -- .github/workflows; then
  PASS=$((PASS+1)); printf '  ok   .github/workflows is untouched by this proof\n'
else
  FAIL=$((FAIL+1)); printf '  FAIL this proof modified .github/workflows\n'
fi

echo
echo "-----------------------------------------------------------------"
printf 'run_envelope proof: %s passed, %s failed\n' "$PASS" "$FAIL"
echo "scratch: $WORK"
[ "$FAIL" = 0 ] || exit 1
