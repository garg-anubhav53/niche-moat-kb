# Niche Moat KB — Cross-Industry Asymmetric Upside Hunter

An hourly Claude Routine that scouts for undervalued, moat-protected small-caps across all industries (except defense), and spends deep-research tokens **only** on the names that clear a high asymmetry bar.

## The Thesis
Find companies where (a) the moat is defensible enough to be the downside floor, and (b) the market hasn't priced it, with (c) a specific catalyst that forces a ~2x re-rating. Institutions are structurally excluded from these $20–300M, thinly-traded, under-covered names — an individual is not.

## Architecture — cheap funnel, gated depth
- **Hourly funnel (~4–5k tokens):** one sector per run (UTC hour mod 5), ≤4 searches, kill-fast triage gates, then a 0–10 **promise score**. All five sectors covered every 5 hours.
- **Promise gate:** only a candidate scoring **≥8/10** unlocks a deep-dive (max one per run). 5–7 queue for later; ≤4 park or die. Deep tokens never touch a mediocre name.
- **Deep-dive:** answers the five asymmetry questions (moat, floor, catalyst, what's-priced, what-kills-it); promotes to WATCH only if moat + floor + a <~12-month catalyst all confirm.

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
