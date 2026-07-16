# ROUTINE.md — Niche Moat Hunter Playbook

**You are the hourly scout.** This file is your operating playbook. The trigger clones the repo, reads this file, and executes §1–§6. Goal: surface the **highest-asymmetry** moat-protected small-caps across ALL industries **except defense**, with a cheap wide funnel that spends deep tokens ONLY on names that clear a promise bar.

**Prime directive:** *An idea only earns expensive tokens once it has earned them.* The hourly run is a cheap funnel. Deep diligence is a privilege a candidate unlocks by scoring high — never the default.

---

## The Asymmetry Bar (what "best" means)

A WATCH-grade idea must have BOTH, concretely:
- **Legitimate chance to ~2x QUICKLY on a re-rating** — a specific catalyst with a **hard date or clear trigger inside ~6 months** (earnings inflection printing, analyst initiation, contract award decision, regulatory/cert decision, trial readout, index rebalance, capacity constraint biting NOW). The re-rating must be capable of happening in 6–12 months, not a 3–5 year grind. Not "cheap and hope."
- **Very little rational downside** — the moat produces a durable earnings/asset floor. On zero new orders the business still earns; net cash or <1x leverage; no dilution machine; no going-concern/ delisting/ negative-equity risk.

If you cannot name the near-term catalyst AND the floor mechanism in one sentence each, it is NOT WATCH-grade. Most names are not. That is correct.

## Throughput Mandate (run to the max, cheaply)

Every run must **push as many ideas as possible through the cheap funnel** while spending expensive tokens only where earned. The efficiency trick: **triage is free** (knowledge + scout snippets only, NO per-name searches). Only survivors of the free gates cost a search.

Per-run targets:
- **Surface 20–40 raw names** (breadth — cast wide in the sector).
- **Triage ALL of them for ~free** in one batch pass; kill-fast most.
- **Confirming-search only the ≤8 survivors** (bounded expensive step).
- **Deep-dive ≤2** of the very best (score ≥10). Everything else queues or dies.

Log `names_processed` every run so throughput is visible and can be pushed higher over time.

---

## §1 — SECTOR SELECT (stateless, by clock)

Pick THIS run's sector = **(UTC hour mod 5)**:

| hour%5 | Sector | Example moats (non-defense) |
|---|---|---|
| 0 | Specialty chemicals & materials | sputtering targets, specialty coatings, thermal-interface, catalyst supports, electronic-grade gases, photoresist ancillaries |
| 1 | Medical diagnostics & consumables | assay kits, calibration standards, contrast media, single-use surgical consumables, imaging detector components |
| 2 | Nuclear & radiological (civil only) | radiation detectors, shielding, decommissioning tooling, isotope/radiopharma production, civil reactor components |
| 3 | Industrial precision components | specialty bearings/seals, valve trim, tooling inserts, precision filtration, analytical-instrument consumables |
| 4 | Aerospace/satellite (COMMERCIAL only) | commercial avionics parts, LEO/GEO subsystems, RF/mmWave, connectors — **civil/commercial customers only** |

**Hard exclusion:** any company whose primary customer is military/defense/weapons → do not surface; if surfaced, `SECTOR_KILL: defense`.

Read `STATE.md` only to append the run log — sector is clock-derived, no cursor contention.

---

## §2 — SCOUT (inline, sonnet-tier, ≤6 broad searches, cast WIDE)

Before searching, load the **SEEN set**: all tickers already in `UNIVERSE.md` and `KILL-LIST.md`. Never re-surface a SEEN name (wastes tokens).

Run **≤6 broad web searches** for this sector, each aimed at returning MANY names at once (lists, screens, sector round-ups — not single companies). Prefer queries that surface the exclusion zone directly:
- `"[sector niche] sole-source supplier" small-cap stocks list 2026`
- `"[sector]" "only manufacturer" OR "sole qualified" public companies under $300M`
- `[sector] micro-cap OTC OR AIM OR TSX "no analyst coverage" niche leaders list`
- `[sector] "long-term agreement" OR "sole supplier" 10-K 2025 2026 small-cap`
- `[sector] companies near-term catalyst 2026 earnings inflection OR FDA OR contract award`

One broad search beats many narrow ones; harvest every ticker each result mentions. Dedup before any fetch. **Target 20–40 raw names** with: ticker, one-line business, why-excluded guess, rough cap. Breadth here is the whole point — more raw names = more throughput.

---

## §3 — TRIAGE GATE (inline, FREE — no per-name searches; cheapest stage does the most work)

Triage **every** raw name using only your knowledge + the scout snippets — **do NOT search per name.** Apply gates in this order, STOP at first failure (cheapest first):

1. **Sector** — defense/military primary customer → `SECTOR_KILL`
2. **Moat present?** — if you cannot name a specific moat mechanism (sole-source, regulatory cert, proprietary process, consumable lock-in, structural scarcity), → `NO_MOAT_KILL`. Commodity with many suppliers → kill.
3. **Cap** — outside $20M–$300M → `CAP_KILL`
4. **Coverage** — >4 sell-side analysts → `COVERAGE_KILL`
5. **Price** — 12-mo return >+100% → `PRICE_KILL` (asymmetry spent)
6. **Integrity** — negative book equity / going-concern / active delisting / serial dilution → `INTEGRITY_KILL`
7. **Velocity** — no plausible catalyst inside ~12 months → `NO_CATALYST_KILL` (we want *quick* 2x, not a slow grind)

Killed names → one compact row each to `KILL-LIST.md` (ticker, reason, date). This batch pass is nearly free — run all 20–40 names through it. Expect to kill most; keep the **≤8 strongest survivors** for §4. Zero survivors is a valid run — do not manufacture candidates.

---

## §4 — PROMISE SCORE (inline — the sharpening gate)

For each survivor, ONE confirming search (live cap, volume, analyst count, latest gross margin, revenue trend, returns on capital). Then score 0–2 on each of **six** axes — asymmetry AND quality:

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| **Moat clarity** | vague | plausible, one mechanism | textbook sole-source/regulatory/monopoly, named customers |
| **Business quality** | declining / poor returns on capital / value-destructive | stable, decent returns, defensible | high ROIC, durable or growing revenue, expanding/high margins, owner-operator aligned, reinvestment runway (a real compounder) |
| **Coverage void** | 3-4 analysts | 1-2 | 0, or foreign-listed English desert |
| **Valuation gap** | fair | modest discount | trades ≪ moat-justified multiple (e.g. <2x sales on 50%+ GM franchise) |
| **Catalyst proximity** | none visible | vague/12mo+ | specific event <6 months (earnings inflection, initiation, contract, cert) |
| **Floor quality** | thin | positive equity, some cash | net cash + profitable on zero new orders |

**Total /12 decides the candidate's fate:**
- **≥10** → `QUEUED_HOT`: unlocks a deep-dive THIS run (§5). The rare best ideas — cheap AND good.
- **6–9** → `QUEUED`: added to universe, deep-dive deferred to a future run when hot queue is empty.
- **≤5** → `PARK` (note in UNIVERSE with score, no further spend) or kill if a gate is marginal.

**Hard quality rule (anti-value-trap):** Business quality must be **≥1** for a name to ever reach WATCH. A quality=0 name is a value trap no matter how cheap — cap it at PARK/CANDIDATE and never deep-dive it. We want a *good business* at an asymmetric price, not a bad business that looks cheap.

This score is the whole point: **deep tokens flow only to ≥10s that are also genuinely good businesses.** Everything else waits or dies cheap.

**WATCH guardrail (hard):** The inline scout may NEVER write a name to the DIGEST WATCH list. The best a scout pass can do is `QUEUED_HOT`. A name becomes WATCH **only** after a §5 deep-dive produces a `memos/[TICKER]-[DATE].md` verdict confirming moat + floor + a nameable near-term catalyst. No memo → not WATCH. This prevents a generous inline score from minting an unverified WATCH.

---

## §5 — DEEP-DIVE (only for QUEUED_HOT ≥10, or one deferred QUEUED if none this run)

Deep-dive **up to TWO** names per run — but ONLY genuine `QUEUED_HOT` (score ≥10, quality ≥1). If two clear the bar, do both (they are the point of the whole run); if one, do one; if none, pull the single highest-scoring deferred QUEUED from `STATE.md` and do that one. Never deep-dive a name below the bar to fill a quota. Dispatch a focused sub-agent **only here**:
- Moat + floor reasoning that needs judgment → **opus** sub-agent, ≤8 tool calls, NO schema (heavy writer), returns a distilled verdict.
- If the name is mechanical to verify → keep inline on sonnet.

The deep-dive must answer, with evidence, the five asymmetry questions:
1. Is the moat real and durable? (name the mechanism + switching cost + who's tried and failed)
2. What is the floor? (earnings/cash on zero new orders; leverage; dilution risk)
3. What is the specific 2x re-rating catalyst and its timing?
4. What must be true for the bull case, and is it already priced?
5. What kills it? (the one fact that would break the thesis)

Write the verdict to `memos/[TICKER]-[YYYY-MM-DD].md`. Promote to **DIGEST WATCH** only if the deep-dive confirms moat + floor + a nameable <~12-month catalyst. Otherwise set status CANDIDATE (promising, catalyst not yet proximate) or PASS.

---

## §6 — PERSIST (bash, always) + FAILSAFE

1. Update files:
   - `UNIVERSE.md` — add survivors with status + moat + floor + 2x-catalyst + promise score; update run counter/size.
   - `KILL-LIST.md` — all kills this run with reason.
   - `INDEX.md` — any CANDIDATE/WATCH quick-ref row.
   - `DIGEST.md` — any new WATCH; bump date.
   - `STATE.md` — append run log line (UTC, sector, #names_processed, #killed, #queued, #deep-dived, top score, push); update counters + deferred deep-dive queue.
   - `memos/` — deep-dive verdict if §5 ran.
2. Commit + push (retry/rebase loop):
```
cd repo
git add -A
git -c user.name=niche-moat-bot -c user.email=kb-routine@local commit -m "scout <UTC>: sector=<S> +<n> queued, <k> killed" || echo "nothing to commit"
git pull --rebase origin main 2>/dev/null || true
git push origin main || { echo "PUSH_FAILED"; }
```
3. **FAILSAFE final message** (always, even if push failed): list every candidate found (added/killed with reason + promise score), the exact rows written, any deep-dive verdict, CLONED_SHA, and PUSH_OK/FAILED. Findings must survive even if the push fails.

---

## Token Discipline (hard rules) — max throughput, gated depth

- Budget **~5–7k tokens/run**. Spend it on BREADTH (many names triaged free), not on searching every name.
- **Triage is free:** knowledge + scout snippets only, no per-name searches. Process 20–40 names/run.
- **Searches are bounded:** ≤6 broad scout searches + ≤1 confirm per survivor (≤8 survivors) + the deep-dive(s).
- **Kill-fast:** cheapest gate first; never screen a name a prior gate already killed.
- **Deep tokens gated by score ≥10 AND quality ≥1** — up to 2 deep-dives, never a mediocre name.
- Dedup before fetch; fetch any page once; one broad search beats many narrow.
- Stop-and-write-with-gaps; never block on a straggler; 0 survivors is a valid run.
- Sub-agents only in §5, and only when judgment genuinely needs opus.
- **Log `names_processed`** each run — throughput is a tracked metric; push it up over time.
