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

## §1 — SECTOR SELECT (cursor-driven over a WIDE universe; skip exhausted)

The old 5-sector clock rotation exhausted itself (each niche swept 4–5×, runs returning 0 new names). We now rotate a **cursor** through a **20-sector universe** so we are always working relatively fresh ground.

**Procedure:**
1. Read the **Sector Rotation** table in `STATE.md` (sector id · passes · status · last-new-find).
2. Pick the **next non-EXHAUSTED sector after the last one run** (wrap around). Skip any sector marked `EXHAUSTED` unless every sector is exhausted (then pick the one with the oldest last-new-find and treat it as a fresh-angle re-sweep).
3. After the run, update that sector's row: increment `passes`; if the run found **0 new QUEUED names**, note it — **2 consecutive 0-new passes → mark `EXHAUSTED`** (it can be revived later by a new geographic lens or a down-cap sweep).
4. Also pick a **geographic lens** for this run and rotate it every run (by passes mod N) so a re-swept sector surfaces *different* names. **Asymmetry lives everywhere in the trustworthy world — hunt it globally, not just US/Europe.** Rotate across, and actively pursue the under-covered Eastern democracies where we've been thin:
   `{ US micro · Canada (TSX/TSXV) · UK (AIM/LSE) · Continental Europe (Deutsche Börse/Euronext/SIX) · Nordics (Stockholm/Helsinki/Oslo/Copenhagen) · **Japan (TSE/JASDAQ)** · **South Korea (KOSPI/KOSDAQ)** · **Taiwan (TWSE/TPEx)** · Australia/NZ (ASX/NZX) }`. Give **Japan, South Korea, Taiwan** at least their fair share of runs — a genuinely global sweep, not a token one.

   **JURISDICTION-TRUST FILTER (hard):** only surface companies domiciled/primary-listed in a **liberal democracy with rule of law, trustworthy financial institutions, and reliable disclosure** — the set above (roughly OECD democracies + Taiwan/Korea). **Exclude on sight** mainland-China (incl. most HK/VIE structures), Russia, **Israel**, and other authoritarian or weak-rule-of-law markets → `JURISDICTION_KILL`, no matter how cheap. We want asymmetry we can actually trust to be real.

   **NON-ENGLISH-FILING DILIGENCE (hard — Japan/Korea/Taiwan and any non-English filer):** `snapshot.py` gives the live price, but SEC fundamentals are US-only, so these names carry real data risk. Before qualifying one as CANDIDATE+, do **more** diligence, not less: obtain and **read the actual primary-language filings** (annual/quarterly report, TSE/DART/MOPS disclosure) — translate them — and independently confirm, with high confidence, each of: **order book / backlog, revenue, gross & operating margin, net cash/debt, share count/dilution.** Don't accept an English summary or an aggregator as the basis. Until each of those is verified from the primary filing, **cap C ≤ 2** and hold the name as a lead (Bench/QUEUED), not a qualified CANDIDATE. State currency, units, and GAAP-vs-IFRS/local-GAAP explicitly.

   A sector is only truly EXHAUSTED once *multiple geographies* are dry — a US-dry sector is often wide open in Japan or Korea.

**The 20-sector universe (all non-defense):**

| id | Sector | Example moats |
|---|---|---|
| 0 | Specialty chemicals & materials | sputtering targets, coatings, electronic-grade gases, catalysts |
| 1 | Medical diagnostics & consumables | assays, calibration standards, contrast media, single-use surgical |
| 2 | Nuclear & radiological (civil) | detectors, shielding, decommissioning, isotopes/radiopharma |
| 3 | Industrial precision components | bearings/seals, valve trim, tooling inserts, precision filtration |
| 4 | Aerospace/satellite (commercial) | avionics parts, LEO/GEO subsystems, RF/mmWave, connectors |
| 5 | Testing, inspection & certification | labs, standards, calibration services, NDT, product certification |
| 6 | Vertical / mission-critical software & data | niche SaaS, exchange/market data, regulatory/compliance systems |
| 7 | Specialty food & agricultural ingredients | flavors, enzymes, cultures, seed traits, feed additives |
| 8 | Building & infrastructure products | code-driven materials, fire/safety products, specialty fittings |
| 9 | Environmental, waste & water treatment | hazmat/nuclear waste, filtration media, water chemicals, recycling |
| 10 | Value-added / sole-line distribution | pricing-power distributors, spec-in resellers, aftermarket parts |
| 11 | Electrical & power components | connectors, sensors, transformers, grid protection, magnetics |
| 12 | Life-science tools & lab consumables | reagents, chromatography, CDMO, bioprocess consumables |
| 13 | Rail & transport safety systems | signaling, axle/brake components, certification-locked hardware |
| 14 | Consumer niche & branded franchises | small durable category-monopoly brands, razor-and-blade consumer |
| 15 | Exchanges, data & niche insurance/financials | moaty micro-cap financial infrastructure, specialty underwriting |
| 16 | Energy-transition picks-and-shovels (non-commodity) | grid, storage components, efficiency, metering |
| 17 | Semiconductor & electronics supply chain | equipment consumables, materials, test/inspection, subsystems |
| 18 | Precision instruments & sensing | metrology, optical/photonic, analytical instruments, IoT sensing |
| 19 | Specialty healthcare services & niche pharma | orphan/niche formulations, specialty compounding, device services |

**Hard exclusion:** any company whose primary customer is military/defense/weapons → `SECTOR_KILL: defense`.

---

## §2 — SOURCE NAMES (systematic enumeration first, web search second)

Load the **SEEN set** (all tickers in `UNIVERSE.md` + `KILL-LIST.md` + reviewed CIKs in `COVERAGE.md`). Never re-surface a SEEN name.

**§2A — SYSTEMATIC ENUMERATION (the primary top-of-funnel; deterministic, near-zero LLM).** This is where most of the coverage comes from — march a *known* universe best-first, not hope-and-search.
- **US (fully enumerable):** run `python3 tools/screen.py --min-rev 20 --max-rev 400 --min-gm 45 --profitable-only`. It returns the ranked **worthwhile universe** (~78 profitable high-GM microcaps) + the denominator. Take the next **8–12 highest-ranked names NOT in SEEN** as this run's worklist. Update `COVERAGE.md` (reviewed count, coverage %, cursor). Refresh the screen when the cached list is >~2 weeks old.
- **Japan/Korea (if `EDINET_KEY` / `OPENDART_KEY` env vars are set):** run the analogous `screen_jp.py`/`screen_kr.py`; else fall through to §2B for these markets.
- **Other exchanges:** enumerate the listing (exchange list) for a denominator where possible; otherwise §2B.

**§2B — WEB-SEARCH SCOUT (supplement — for markets not yet enumerable, and situation-angles).** Only after §2A, and mainly for the non-US geo lens. Apply THIS run's **geographic lens** (from §1); append the region to queries.

Run **≤6 broad web searches**, each aimed at returning MANY names at once (lists/screens/round-ups, not single companies). **Rotate across TWO angle-families so we don't re-mine the same lists every pass** — pick 3 from the moat-angle set and 2-3 from the situation-angle set:

**Moat angles:** 
- `"[sector niche] sole-source supplier" small-cap stocks [region] 2026`
- `"[sector]" "only manufacturer" OR "sole qualified" public companies under $1B [region]`
- `[sector] micro-cap [region] "no analyst coverage" niche leaders list`
- `[sector] >40% gross margin small-cap "market leader" [region]`

**Situation angles (surface names the moat-lists miss):**
- `[sector] recent spin-off OR carve-out small-cap [region] 2025 2026`
- `[sector] orphaned post-IPO OR de-SPAC under-followed [region]`
- `[sector] activist OR 13D OR insider buying cluster small-cap 2026`
- `[sector] raised guidance OR record backlog small-cap [region] 2026`
- `[sector] "long-term agreement" OR "sole supplier" 10-K 2025 2026 small-cap`
- `[sector] companies near-term catalyst 2026 earnings inflection OR FDA OR contract award`

One broad search beats many narrow ones; harvest every ticker each result mentions. Dedup before any fetch. **Target 20–40 raw names** with: ticker, one-line business, why-excluded guess, rough cap. Breadth here is the whole point — more raw names = more throughput.

---

## §3 — TRIAGE GATE (inline, FREE — no per-name searches; cheapest stage does the most work)

Triage **every** raw name using only your knowledge + the scout snippets — **do NOT search per name.** Apply gates in this order, STOP at first failure (cheapest first):

1. **Sector** — defense/military primary customer → `SECTOR_KILL`
2. **Moat present?** — if you cannot name a specific moat mechanism (sole-source, regulatory cert, proprietary process, consumable lock-in, structural scarcity), → `NO_MOAT_KILL`. Commodity with many suppliers → kill.
3. **Cap (gradient, not a cliff — see METHOD.md Size Discipline):** <$20M → `CAP_KILL` (too illiquid) unless a clear liquidity path. $20M–$300M → core zone, pass. $300M–$1.5B → **extended zone: do NOT reflexively kill.** Keep it if it has *either* franchise-quality (a wide/durable moat, high returns) *or* a genuine near-term catalyst — i.e. it could plausibly be a CORE or grade-A/B. Only `CAP_SOFT_KILL` if it's *also* mediocre (no standout moat AND no catalyst). An ~$800M grade-A name is exactly what we want. >$1.5B → `CAP_KILL` unless a rare, genuinely under-covered special situation (say why). *(EUZ.DE at ~$1.1B cleared this and became our first CORE — extended-zone quality is real.)*
4. **Coverage** — >4 sell-side analysts → `COVERAGE_KILL`
5. **Price** — 12-mo return >+100% → `PRICE_KILL` (asymmetry spent)
6. **Integrity** — negative book equity / going-concern / active delisting / serial dilution → `INTEGRITY_KILL`
7. **Velocity (quality-gated):** a name with **no catalyst inside ~12 months** is killed `NO_CATALYST_KILL` **only if it also looks low-quality** (commodity-ish, thin margins, no compounding). A **high-quality** business with no visible catalyst is NOT killed — it survives as a potential **CORE** hold (own-and-wait). Quality buys a name the right to have no catalyst.

Killed names → one compact row each to `KILL-LIST.md` (ticker, reason, date). This batch pass is nearly free — run all 20–40 names through it. Expect to kill most; keep the **≤8 strongest survivors** for §3.5. Zero survivors is a valid run — do not manufacture candidates.

**Provisional vs. confirmed kills (critical):** Free triage may kill outright only on gates that a snippet reliably settles — `SECTOR_KILL` (defense), obvious `NO_MOAT`, clearly-out cap (a household-name >$1.5B or a <$20M nano), obvious `PRICE_KILL` (>+100%), unambiguous `COVERAGE_KILL`. But **borderline financial calls — cap near a boundary, integrity/floor, valuation — must NOT be settled on a snippet.** A name you'd kill on `INTEGRITY`/`CAP_SOFT`/floor grounds, or *qualify* as a candidate, goes to §3.5 for the real numbers first. Snippet-level financial kills are the exact error we're fixing.

---

## §3.5 — FINANCIAL BASELINE (mandatory before qualify OR financial-kill; full spec in METHOD.md)

Get the reported numbers before scoring or financially killing a survivor.

1. **Live price + real valuation, programmatically (mandatory):** run `python3 tools/snapshot.py TICKER` for each survivor. It returns the **live current price** and (US filers) most-recent **revenue/GM/net-income/shares from SEC XBRL**, then **computes market cap = live price × shares** and P/S, P/E — authoritative, no aggregator trust. Heed its stale-shares/dual-class warnings. Foreign (no CIK) → live price only; pull fundamentals from the IR filing and cap **C ≤ 2**.
2. **Fetcher (haiku) fills the rest from the filing:** cash, total debt, FCF, revenue 3–5yr trend, plus a **fair-value estimate** (moat-justified multiple / analyst PT). Quote-anchored; a bare number is untrusted.
3. **Reconcile deterministically:** run `python3 tools/fin_check.py <<'JSON' … JSON` on the snapshot JSON + filing figures, **including a `provenance` map**. Any FAIL, or floor-critical figures not filing-anchored → ⚠/~, never ✓ (internal consistency ≠ truth).
4. **You triangulate & trust-tag** (✓ = snapshot/filing-anchored + checker-pass · ~ single-source · ⚠ = disagree or checker-FAIL · ? unverified). Foreign names with no primary filing → **cap C ≤ 2**, note currency/units/GAAP-vs-IFRS. **Coach which numbers to trust vs doubt.**

**Write `financials/[TICKER].md`** (quote-anchored figures + checker verdict + tags + sources + as-of) — this, not the snippet, is the evidence for §4.
- Basics solid → §4; apply financial gates on verified figures (fail cap/floor/integrity → kill citing the number).
- Basics unobtainable or key figures stay ⚠/? → **NEEDS-DATA** (not CANDIDATE), C low, note what's missing. Never qualify a name whose financials you couldn't read.

---

## §4 — PROMISE SCORE (inline — the sharpening gate; uses the §3.5 baseline, NOT snippets)

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

**ASYMMETRY GATE (apply after scoring — the leak we fixed).** A high /12 is not enough. Using the snapshot.py **live price** and computed valuation vs. a fair-value estimate (METHOD.md → Asymmetry Gate): (1) **mispriced at the live price now** — trades materially below defensible fair value (the gap = the asymmetry); if already at/above fair value, nothing to capture; (2) realistic bull ≥ ~2x from the live price; (3) upside skewed above downside; (4) a *discrete* trigger OR CORE-grade standalone quality (diffuse "cycle turns / buyback someday / analyst may notice" does NOT count). **Fail → not a live CANDIDATE — split it:** if it's genuinely high-quality (Q≥4) + **durable moat** + real floor and fails *only on price*, add it to the **QUALITY BENCH (`WATCHLIST.md`)** with a buy-zone (a great business to buy on the dip — monitored in §7); everything else → `PARK`. Judge the live price vs. value — NOT the 52-week range.

**CORE override (quality-without-catalyst):** If Moat + Business quality + Floor together = **6/6** (a genuinely high-quality, well-protected business) but Catalyst = 0, the name still **QUEUES** even if the total is ≤9 — flag it `QUEUED_CORE` — **provided it still passes the Asymmetry Gate (mispriced at the live price, ≥2x, skewed).** We want to own great protected businesses and wait; but a franchise already trading at fair value is a PARK, not a CANDIDATE. Do not let a missing catalyst bury a *cheap* franchise — but do not qualify an *expensive* one.

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

Deep-dive **up to TWO** names per run — but ONLY genuine `QUEUED_HOT` (score ≥10, quality ≥1). If two clear the bar, do both; if one, do one; if none, pull the single highest-scoring deferred QUEUED from `STATE.md`. Never deep-dive a name below the bar to fill a quota.

**Fetch cheap, reason well, then RED-TEAM hard (three tiers):**
- **Fetchers = haiku, pure retrieval.** Pull the raw material — actual latest filing statements (income statement, balance sheet, cash flow) from EDGAR/IR + `snapshot.py` — verbatim, no interpretation.
- **First-pass reasoner = sonnet (NO schema).** Reads the fetched material, applies METHOD.md, writes the provisional memo (grade/tier/Q-F-R-C).
- **ESCALATION — throw OPUS at every cleared candidate.** If the first pass lands the name at **CANDIDATE-or-better OR flags high apparent asymmetry that price doesn't bar** (i.e. a name we'd plausibly want to watch), it earns a mandatory **OPUS adversarial pass** (`agentType`/model = opus) that runs the **Adversarial Red-Team (METHOD.md — the 12 failure modes)** and produces the **RISK PROFILE**. Its job is to BREAK the thesis: re-derive every load-bearing number from primary source, strip one-offs, decompose revenue quality, stress moat durability 3/5/10yr, hunt the disclosure that flips it, check the asymmetry isn't already captured. **A name is only CONFIRMED as CANDIDATE+/graded after surviving the Opus red-team.** If it doesn't survive, downgrade (PARK/Bench/PASS) and record why. Widen the scope here — a fuller, more complete diagnosis is the point; don't be narrow on a name with a real chance of being interesting.

**The deep-dive MUST apply `METHOD.md` in full** — that file is the analytical core. Concretely:
0. **Verify the §3.5 Financial Baseline against the primary filing** (fetched above) — confirm revenue/margin trend, net cash/debt, share-count/dilution, and FCF are real; resolve any ⚠ DISCREPANT figures; scan the statements for going-concern, receivables/inventory build, capitalized-cost/one-time flattering, related-party items. State "verified against 10-K/20-F: YES/PARTIAL/NO".
1. **Score the four sub-assessments** Q / F / R / C (each 1–5) with evidence.
2. **Run the Skeptic's Confirmation Checklist** (all 10 items) — for the moat/contract/milestone, mark each CONFIRMED / PLAUSIBLE / UNVERIFIED / RED-FLAG with a one-line evidence note. Be rigorous that revenue will be recognized, won't be lost, won't go to a competitor, and the moat stays sticky over time (in-source/license-away risk). RED-FLAGs that threaten the thesis core cap the grade.
3. **Do the Historical Base-Rate step** — name 2–4 analogous past companies, state whether they re-rated and the swing factor; consult the sibling `rerating-situations-kb` where useful. Output a one-line base rate. No credible analog re-rated → R is low, say so.
4. **Assess data quality / coverage confidence** explicitly (feeds C) — is the disclosure good, did we find the true comparable set, what are the open unknowns.
5. **Produce the Risk-Adjusted Asymmetry grade (A/B/C/D) and Tier (CORE/CATALYST/WATCH/CANDIDATE/PARK)** per METHOD.md, plus buy-zone / upgrade-trigger / downgrade-trigger.

Write the full verdict to `memos/[TICKER]-[YYYY-MM-DD].md`, ending with the required summary block from METHOD.md — **including the OPUS RED-TEAM RESULT (12 checks: pass/fail + what it caught), the RISK PROFILE (load-bearing assumption · clean operating earnings & what it's actually worth · informative trigger · moat durability 3/5/10yr · revenue-quality decomposition · the disclosure that would flip it · return if nothing re-rates), and the HUMAN VERIFICATION CHECKLIST.** We surface a strong *candidate for a human to vet*, not an AI verdict — but the Opus pass must have genuinely tried to break it first.

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

## §7 — REFLECT (KB self-review; run when `total_runs` is a multiple of 3)

Every 3rd run, before §6, spend a small budget stepping back from finding names to auditing whether the KB itself is healthy. Read `REVIEW.md` (prior findings), sample the KB, and answer three questions with evidence:

1. **Are we reading the right input financial data?** Sample 3–4 recent `financials/*.md` + memos. Are figures quote-anchored, checker-passed, and filing-verified — or thin/single-source/unverified? Any CANDIDATE/WATCH graded without a solid baseline is a defect — flag it and downgrade to NEEDS-DATA.
2. **Are we exploring the universe well?** Look at sector coverage (are 5-19 actually being worked, or are we drifting back to 0-4?), geographic spread, hit-rate trend, and grade mix (all C's and no A/B? too many PARKs?). Are we stuck re-mining?
3. **False-negative risk:** re-check **2 recent triage-kills** through §3.5 (real numbers). Did we wrongly kill a good name on a snippet (stale cap, old going-concern, split-adjusted price)? If so, revive it to QUEUED and log the pattern.

4. **Re-price the QUALITY BENCH (`WATCHLIST.md`):** run `python3 tools/snapshot.py TICKER` on each bench name, update its `Last price`. If any has **dipped into its Buy-zone**, promote it to `QUEUED_HOT` (deep-dive at the new price) and note the trigger fired. This is cheap (live price only) and is the whole point of the bench — catching the dip.

**Then drive it forward — make the corrective edits this run:** mark a sector EXHAUSTED or revive one with a new geo; re-queue a wrongly-killed name; downgrade an under-verified CANDIDATE to NEEDS-DATA; promote a bench name that dipped; adjust the rotation priority. Append a dated entry to `REVIEW.md`: what you checked, what was wrong, what you changed, and the one systemic fix to make next. Keep it to the highest-leverage findings, not a laundry list.

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
