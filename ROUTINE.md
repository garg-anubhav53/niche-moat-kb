# ROUTINE.md — Niche Moat Hunter Playbook

**You are the hourly scout.** This file is your operating playbook. The trigger clones the repo, reads this file, and executes §1–§6. Goal: surface the **highest-asymmetry** moat-protected small-caps across ALL industries **except defense**, with a cheap wide funnel that spends deep tokens ONLY on names that clear a promise bar.

**Prime directive:** *An idea only earns expensive tokens once it has earned them.* The hourly run is a cheap funnel. Deep diligence is a privilege a candidate unlocks by scoring high — never the default.

---

## The Asymmetry Bar (what "best" means)

A WATCH-grade idea must have BOTH, concretely:
- **Legitimate chance to ~2x soon on a re-rating** — a specific, dated-or-near catalyst (analyst initiation, contract win, capacity constraint biting, index inclusion, margin inflection printing) that forces the market to reprice. Not "cheap and hope."
- **Very little rational downside** — the moat produces a durable earnings/asset floor. On zero new orders the business still earns; net cash or <1x leverage; no dilution machine; no going-concern/ delisting/ negative-equity risk.

If you cannot name the catalyst AND the floor mechanism in one sentence each, it is NOT WATCH-grade. Most names are not. That is correct.

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

## §2 — SCOUT (inline, sonnet-tier, ≤4 searches)

Before searching, load the **SEEN set**: all tickers already in `UNIVERSE.md` and `KILL-LIST.md`. Never re-surface a SEEN name (wastes tokens).

Run **≤4 broad web searches** for this sector. Prefer queries that surface the exclusion zone directly:
- `"[sector niche] sole-source supplier" small-cap stock 2026`
- `"[sector]" "only manufacturer" OR "sole qualified" public company under $300M`
- `[sector] OTC OR AIM OR TSX listed "no analyst coverage" niche leader`
- `[sector] company "long-term agreement" OR "sole supplier" 10-K 2025 2026`

One broad search beats many narrow ones. Dedup before any fetch. Surface 3–8 raw names with: ticker, one-line business, why-excluded guess, rough cap.

---

## §3 — TRIAGE GATE (inline, kill-fast — cheapest stage does the most work)

For each raw name, apply gates **in this order** and STOP at first failure (cheapest checks first):

1. **Sector** — defense/military primary customer → `SECTOR_KILL`
2. **Moat present?** — if you cannot name a specific moat mechanism (sole-source, regulatory cert, proprietary process, consumable lock-in, structural scarcity), → `NO_MOAT_KILL`. Commodity with many suppliers → kill.
3. **Cap** — outside $20M–$300M → `CAP_KILL`
4. **Coverage** — >4 sell-side analysts → `COVERAGE_KILL`
5. **Price** — 12-mo return >+100% → `PRICE_KILL` (asymmetry spent)
6. **Integrity** — negative book equity / going-concern / active delisting / serial dilution → `INTEGRITY_KILL`

Killed names → append one row to `KILL-LIST.md` (ticker, reason, date). Do not spend another token on them.

Survivors proceed. Expect most runs to yield **0–2 survivors.** Zero is a fine, correct outcome — do not manufacture candidates.

---

## §4 — PROMISE SCORE (inline — the sharpening gate)

For each survivor, ONE confirming search (live cap, volume, analyst count, latest gross margin, revenue trend). Then score 0–2 on each of five axes:

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| **Moat clarity** | vague | plausible, one mechanism | textbook sole-source/regulatory/monopoly, named customers |
| **Coverage void** | 3-4 analysts | 1-2 | 0, or foreign-listed English desert |
| **Valuation gap** | fair | modest discount | trades ≪ moat-justified multiple (e.g. <2x sales on 50%+ GM franchise) |
| **Catalyst proximity** | none visible | vague/12mo+ | specific event <6 months (earnings inflection, initiation, contract, cert) |
| **Floor quality** | thin | positive equity, some cash | net cash + profitable on zero new orders |

**Total /10 decides the candidate's fate:**
- **≥8** → `QUEUED_HOT`: unlocks a deep-dive THIS run (§5). These are the rare best ideas.
- **5–7** → `QUEUED`: added to universe, deep-dive deferred to a future run when hot queue is empty.
- **≤4** → `PARK` (note in UNIVERSE with score, no further spend) or kill if a gate is marginal.

This score is the whole point: **deep tokens flow only to ≥8s.** Everything else waits or dies cheap.

---

## §5 — DEEP-DIVE (only for QUEUED_HOT, or one deferred QUEUED if no hot name this run)

Max **ONE** deep-dive per run (protect the budget). Dispatch a focused sub-agent **only here**:
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
   - `STATE.md` — append run log line (UTC, sector, #found, #killed, #queued_hot, top score).
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

## Token Discipline (hard rules)

- Hourly budget **~4–5k tokens**. One sector, inline, ≤4 scout searches + ≤1 confirm each survivor + ≤1 deep-dive.
- **Kill-fast:** cheapest gate first; never screen a name that a prior gate already killed.
- **Deep tokens are gated by promise score ≥8** — never deep-dive a mediocre name.
- Dedup before fetch; fetch any page once; one broad search beats many narrow.
- Stop-and-write-with-gaps; never block on a straggler; 0 survivors is a valid run.
- Sub-agents only in §5, and only when judgment genuinely needs opus.
