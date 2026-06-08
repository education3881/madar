# Guidebook · The egress wall is a `bash`-only boundary — trace figures with the sanctioned web tools

**Logged:** 2026-06-08 · **For:** Content Creator, Editor, Manager
**Supersedes the operative conclusion of:** `2026-06-07-sourcing-across-egress-boundary.md`
**Why this exists:** yesterday's dossier and guidebook entry concluded that the Sierra Leone figures could not be traced because `edtechhub.org`, `docs.edtechhub.org` and `documents1.worldbank.org` are "outside the network allowlist," and named a Vini action (allowlist those hosts in Settings → Capabilities) as the unblock. **That conclusion was half right and the operative half was wrong.** Today the same figures were traced in full, from the same environment, with no settings change.

## The finding

There are two different network paths in this environment, and they have different reach:

1. **The sandbox shell (`bash`: `curl`, `wget`, Python `requests`).** This is egress-restricted. `edtechhub.org` and friends genuinely fail here. This is the wall yesterday's run hit — and correctly described, *for bash*.
2. **The sanctioned web tools (`WebSearch` + `web_fetch`).** These are **not** bound by the same allowlist. `web_fetch` opened `edtechhub.org/2025/11/20/...` and the 4 Dec 2024 Marian Abu conversation in full today, and read the exact outcome table the figures were lifted from.

**The rule:** when a primary source host is unreachable from `bash`, do **not** conclude the figure is untraceable and do **not** escalate to a Vini allowlist action. First exhaust `WebSearch` + `web_fetch`. The wall is almost always bash-only.

## The one mechanic worth knowing

`web_fetch` will only open a URL that is already in its **provenance set** — a URL that appeared in a prior `WebSearch` result (or a user message). So the reliable pattern is:

1. `WebSearch` for the source — this surfaces the canonical URL and *puts it in provenance*.
2. `web_fetch` that exact canonical URL — now it opens.

(Today, the first direct `web_fetch` of the article failed with "URL not in provenance set"; a `WebSearch` first, then `web_fetch` of the surfaced canonical URL, worked immediately. That is the whole trick.)

## What this bought, concretely

Every Tier-2/3/4 item the 2026-06-07 dossier quarantined was resolved from the primary in one run: the 64 / 57 / 54 / 7 / 100% figures, the 57%-vs-56/53% discrepancy (primary says a flat 57%), and the Keifala + Elacqua attributions. The piece shipped the same day. The "one allowlist step" named as a blocker on 06-07 was never needed.

## The transferable lesson

Distinguish *the tool that is blocked* from *the resource that is unreachable*. They are not the same. A blocked `curl` is a statement about `bash`, not about the open web. Re-running the same fetch through the sanctioned tools is the first move, not the last resort — and it is faster and cheaper than asking the founder to change a setting.

*(The standing infra items from 06-07 — `@astrojs/sitemap` to replace the hand-built file — remain live for the weekly. The host-allowlist request is withdrawn.)*

— logged by the Manager · 2026-06-08
