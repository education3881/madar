import sys, time, json, urllib.request, urllib.error
sys.path.insert(0,"/home/runner/work/madar/madar/agents/tools")
import qa_claim_registers as Q

# The set issue #12's default B authorises, derived from the register as it
# stood on 2026-10-24 (the issue's own date) rather than remembered: the 23
# live-only rows. Two of them ARE web.archive.org URLs and are excluded with
# the reason recorded; the first five of the remaining 21 in sorted order.
NAMED = sorted(r["url"] for r in json.load(open("/tmp/madarwork/reg-1024.json"))["registers"]
               if r.get("state") == "live-only")
excluded = [u for u in NAMED if "web.archive.org" in u]
submittable = [u for u in NAMED if "web.archive.org" not in u]
print(f"named {len(NAMED)} · excluded as already-an-archive-URL {len(excluded)} · submittable {len(submittable)}")
batch = submittable[:5]
out = []
for u in batch:
    req = urllib.request.Request("https://web.archive.org/save/" + u,
                                 headers={"User-Agent": Q.UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            status, note = r.status, r.headers.get("Content-Location") or r.url
    except urllib.error.HTTPError as e:
        status, note = e.code, e.reason
    except Exception as e:
        status, note = None, type(e).__name__
    print(f"  {str(status):>5}  {u[:92]}")
    out.append({"url": u, "submit_status": status, "note": str(note)[:160]})
    time.sleep(8)
json.dump(out, open("save5.json", "w"), indent=2)
print("\nverifying each against the availability API, same instrument as the read:")
time.sleep(20)
for row in out:
    st = Q.archive_state(row["url"])
    row["after"] = st
    print(f"  archived={st.get('archived')}  snap={st.get('snapshot','-')}  {row['url'][:88]}")
    time.sleep(4)
json.dump(out, open("save5.json", "w"), indent=2)
