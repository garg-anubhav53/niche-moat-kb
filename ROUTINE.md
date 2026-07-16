# ROUTINE.md — Niche Moat Hunter Playbook

**You are the hourly scout.** This file is your operating playbook. The trigger clones the repo, reads this file AND `METHOD.md`, and executes §1–§6. Goal: surface moat-protected companies (mostly small-cap, ALL industries **except defense**) with the **highest risk-adjusted asymmetric value**, via a cheap wide funnel that spends deep tokens ONLY on names that earn them.

**Prime directive:** *An idea only earns expensive tokens once it has earned them.* The hourly run is a cheap funnel. Deep diligence (§5, governed by `METHOD.md`) is a privilege a candidate unlocks by scoring high — never the default.

**Two things make a company interesting, and they are independent:**
1. **It's a genuinely high-quality, well-protected business** — worth owning **even without** confidence in a near-term re-rate (a CORE hold; the re-rate is optional upside). Never kill a franchise for lacking a catalyst.
2. **A near-term re-rating is likely** — adds urgency/IRR (a CATALYST trade).
The headline output is a **risk-adjusted asymmetry grade** (see `METHOD.md`): asymmetric value *relative to* risk, discounted by our confidence in the data. Rank on that, not on raw factor counts.

---

## The WATCH/CATALYST Bar (for the *time-the-re-rate* bucket)

*(This bar governs CATALYST/WATCH. High-quality names without a catalyst go to CORE instead — see METHOD.md.)* A CATALYST-grade idea must have ALL THREE, concretely:
- **Legitimate chance to ~2x QUICKLY on a re-rating** — a specific catalyst with a **hard date or clear trigger inside ~6 months** that forces a *re-rating* (analyst initiation, contract award, regulatory/cert decision, trial readout, index rebalance, capacity constraint biting NOW, an earnings *inflection* that reveals hidden earning power). **NOT a slow cyclical earnings recovery to "mid-cycle" over multiple years** — that is a grind, not a quick 2x, and does NOT qualify. If the 2x needs the whole industry cycle to turn, it is CANDIDATE at best.
- **The asymmetric entry must exist NOW** — if the stock is near its 52-week high, the cheap entry is already gone → CANDIDATE (with a buy-zone), never WATCH. WATCH = buyable today with the 2x still ahead.
- **Very little rational downside** — the moat produces a durable **earnings** floor (still earns on zero new orders), not merely an asset/book floor. Net cash or <1x leverage; no dilution machine; no going-concern/ delisting/ negative-equity risk. A name that *loses money* at trough revenue has only a balance-sheet floor → cap at CANDIDATE.

If you cannot name the near-term *re-rating* catalyst, a buyable-today entry, AND the earnings-floor mechanism each in one sentence, it is NOT WATCH-grade. Most names are not. That is correct.

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
3. **Cap (gradient, not a cliff — see METHOD.md Size Discipline):** <$20M → `CAP_KILL` (too illiquid) unless a clear liquidity path. $20M–$300M → core zone, pass. $300M–$1.5B → **extended zone: pass ONLY if the asymmetry looks exceptional** (wide moat + real floor + genuine catalyst or franchise quality); otherwise `CAP_SOFT_KILL`. >$1.5B → `CAP_KILL` unless a rare, genuinely under-covered special situation (say why).
4. **Coverage** — >4 sell-side analysts → `COVERAGE_KILL`
5. **Price** — 12-mo return >+100% → `PRICE_KILL` (asymmetry spent)
6. **Integrity** — negative book equity / going-concern / active delisting / serial dilution → `INTEGRITY_KILL`
7. **Velocity (quality-gated):** a name with **no catalyst inside ~12 months** is killed `NO_CATALYST_KILL` **only if it also looks low-quality** (commodity-ish, thin margins, no compounding). A **high-quality** business with no visible catalyst is NOT killed — it survives as a potential **CORE** hold (own-and-wait). Quality buys a name the right to have no catalyst.

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

The /12 is a **cheap funnel score only** — it decides who gets a deep-dive, not the final verdict (that comes from METHOD.md in §5).

**Fate:**
- **≥10** → `QUEUED_HOT`: unlocks a deep-dive THIS run (§5). The rare best ideas — cheap AND good.
- **6–9** → `QUEUED`: added to universe, deep-dive deferred to a future run.
- **≤5** → `PARK` (note score, no further spend) or kill if a gate is marginal.

**CORE override (quality-without-catalyst):** If Moat + Business quality + Floor together = **6/6** (a genuinely high-quality, well-protected business) but Catalyst = 0, the name still **QUEUES** even if the total is ≤9 — flag it `QUEUED_CORE`. We want to own great protected businesses and wait; the deep-dive will grade it as a CORE hold. Do not let a missing catalyst bury a franchise.

**Hard quality rule (anti-value-trap):** Business quality must be **≥1** for a name to ever reach WATCH. A quality=0 name is a value trap no matter how cheap — cap it at PARK/CANDIDATE and never deep-dive it. We want a *good business* at an asymmetric price, not a bad business that looks cheap.

This score is the whole point: **deep tokens flow only to ≥10s that are also genuinely good businesses.** Everything else waits or dies cheap.

**WATCH guardrail (hard):** The inline scout may NEVER write a name to the DIGEST WATCH list. The best a scout pass can do is `QUEUED_HOT`. A name becomes WATCH **only** when ALL of these hold:
1. A §5 deep-dive has actually written `memos/[TICKER]-[DATE].md` (the file must exist and be committed).
2. The 2x catalyst is a genuine near-term **re-rating** (not a multi-year cyclical recovery).
3. The stock is **not near its 52-week high** — the asymmetric entry still exists today.
4. The floor is an **earnings** floor (profitable at trough), not merely an asset/book floor.
If any of 2–4 fail, the name is **CANDIDATE with a buy-zone**, not WATCH. There is no "conditional" or "cautious WATCH" status — it is WATCH or it is CANDIDATE. A deep-dive that scores ~9/12 with a cyclical catalyst and an asset-only floor is a **CANDIDATE**, full stop.

---

## §5 — DEEP-DIVE (only for QUEUED_HOT ≥10, or one deferred QUEUED if none this run)

Deep-dive **up to TWO** names per run — but ONLY genuine `QUEUED_HOT` (score ≥10, quality ≥1). If two clear the bar, do both (they are the point of the whole run); if one, do one; if none, pull the single highest-scoring deferred QUEUED from `STATE.md` and do that one. Never deep-dive a name below the bar to fill a quota. Dispatch a focused sub-agent **only here**:
- Moat + floor reasoning that needs judgment → **opus** sub-agent, ≤8 tool calls, NO schema (heavy writer), returns a distilled verdict.
- If the name is mechanical to verify → keep inline on sonnet.

**The deep-dive MUST apply `METHOD.md` in full** — that file is the analytical core. Concretely:
1. **Score the four sub-assessments** Q / F / R / C (each 1–5) with evidence.
2. **Run the Skeptic's Confirmation Checklist** (all 10 items) — for the moat/contract/milestone, mark each CONFIRMED / PLAUSIBLE / UNVERIFIED / RED-FLAG with a one-line evidence note. Be rigorous that revenue will be recognized, won't be lost, won't go to a competitor, and the moat stays sticky over time (in-source/license-away risk). RED-FLAGs that threaten the thesis core cap the grade.
3. **Do the Historical Base-Rate step** — name 2–4 analogous past companies, state whether they re-rated and the swing factor; consult the sibling `rerating-situations-kb` where useful. Output a one-line base rate. No credible analog re-rated → R is low, say so.
4. **Assess data quality / coverage confidence** explicitly (feeds C) — is the disclosure good, did we find the true comparable set, what are the open unknowns.
5. **Produce the Risk-Adjusted Asymmetry grade (A/B/C/D) and Tier (CORE/CATALYST/WATCH/CANDIDATE/PARK)** per METHOD.md, plus buy-zone / upgrade-trigger / downgrade-trigger.

Write the full verdict to `memos/[TICKER]-[YYYY-MM-DD].md`, ending with the required summary block from METHOD.md.

**Status assignment:**
- **CORE** — Q≥4 & F≥4 (own-and-hold quality; catalyst optional). A high-quality protected business with no near-term catalyst belongs HERE, not killed.
- **CATALYST/WATCH** — only if it clears the four WATCH tests below (near-term re-rate, buyable-today, earnings floor, memo on file) AND confidence is adequate. Low confidence → WATCH-to-verify.
- **CANDIDATE** — real but entry/timing/confidence off; track the buy-zone.
- **PARK / PASS** — asymmetry too thin.

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
