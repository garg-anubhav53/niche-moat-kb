# Niche Moat KB — Cross-Industry Asymmetric Upside Hunter

An hourly Claude Routine that scouts for moat-protected companies (mostly small-cap, all industries except defense) and spends deep-research tokens **only** on the names that earn them — then grades each on **risk-adjusted asymmetric value**.

## The Thesis
Own moat-protected businesses where the moat is the downside floor, bought below what the moat is worth. **Two independent reasons to be interested, decoupled:** (1) a genuinely high-quality, protected business is worth owning *even without* a near-term re-rate (**CORE** — own & wait); (2) a likely near-term re-rating adds urgency (**CATALYST** — time the trade). Smaller cap = likelier off institutional radar, so size is a **gradient** (core zone $20–300M; larger allowed if asymmetry is exceptional — an ~$800M grade-A name qualifies; >$1.5B out).

## Architecture — cheap funnel, gated depth, rigorous deep-dive
- **Hourly funnel (~5–7k tokens):** one sector/run (UTC hour mod 5), ≤6 broad searches, **free** batch triage of 20–40 names, a /12 funnel score on ≤8 survivors. All five sectors covered every 5 hours.
- **Gate:** ≥10 → deep-dive now; 6–9 → queue; a 6/6 quality-and-floor name with no catalyst still queues (`QUEUED_CORE`). Deep tokens never touch a mediocre name.
- **Deep-dive (`METHOD.md`):** four sub-scores (Quality, Floor, Re-rate, Confidence) + a 10-item **skeptic's confirmation checklist** (revenue recognized? not lost? not captured by a rival? moat stays sticky?) + a **historical base-rate** analog check + a final **risk-adjusted asymmetry grade (A/B/C/D)** and tier.

## Files
| File | Purpose |
|------|---------|
| `ROUTINE.md` | The playbook the routine reads and executes each run (§1–§6) |
| `DIGEST.md` | Doctrine, the asymmetry bar, promise score, current WATCH list |
| `UNIVERSE.md` | Persistent candidate map + statuses + moat classifications |
| `STATE.md` | Run log, counters, deferred deep-dive queue |
| `KILL-LIST.md` | Triage failures (price/cap/coverage/integrity/sector/no-moat) |
| `INDEX.md` | Quick company reference |
| `memos/` | Deep-dive verdicts (`[TICKER]-[DATE].md`) |

## Operations
- **Repo:** `github.com/garg-anubhav53/niche-moat-kb`
- **Routine:** hourly, model = Sonnet 4.6, environment = KB-routines (`env_01JNimwQmpamYWmvHD8uABXm`, holds `GH_PAT`)
- **Git auth:** routine clones/pushes via `https://x-access-token:${GH_PAT}@github.com/...`
- **Sector rotation:** stateless, by clock — no cursor contention
- Edit `ROUTINE.md` and push to change routine behavior without touching the trigger.

## What "best" means here
Every WATCH must have, in one sentence each: **the catalyst** that re-rates it ~2x soon, and **the floor mechanism** that makes a rational permanent loss unlikely. No catalyst or no floor → not WATCH-grade.

*Last updated: 2026-07-16*
