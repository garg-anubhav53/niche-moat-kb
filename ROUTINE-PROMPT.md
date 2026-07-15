# Niche Moat KB — Hourly Routine Prompt

**Run as:** Claude Routine, hourly, Sonnet 4.6 model
**Token budget:** 4,000–5,000 per run
**Goal:** Scout for undervalued niche-moat companies across all industries (except defense), pass through fast triage, add viable candidates to UNIVERSE, update WATCH list.

---

## Stage 1: Scout — Find Niche Moat Candidates (Sonnet, 1.5k tokens)

Use 4–5 broad web searches to surface candidates in DIFFERENT sectors each run:
- Run 1: Specialty chemicals & materials (sputtering targets, specialty coatings, thermal management)
- Run 2: Medical device consumables & diagnostics (lab instruments, test kits, imaging components)
- Run 3: Nuclear & radiological security supply chain
- Run 4: Industrial equipment with sole-source components (bearings, seals, precision fasteners)
- Run 5: Niche aerospace/satellite subsystems

**Search template:** "[Sector] small-cap companies $50-300M market cap sole-source supplier" OR "niche monopoly [industry] public stock" OR "[industry] OTC Pink or AIM listed 0-2 analysts"

**Output:** Ticker, company name, sector, brief moat description, market cap estimate, analyst count.

**Max 5 searches. Stop and output results.**

---

## Stage 2: Triage Gate — Apply Auto-Kill Filters (Haiku, 1.5k tokens)

For each candidate from Stage 1:

**Auto-kill if ANY apply:**
1. Market cap >$300M OR <$20M → CAP_KILL
2. Daily dollar volume >$3M → LIQUIDITY_KILL
3. >4 sell-side analysts → COVERAGE_KILL
4. 12-month return >+100% → PRICE_KILL
5. Negative book equity (if findable) → INTEGRITY_KILL
6. Defense sector → SECTOR_KILL
7. Commodity product (no moat signal) → SECTOR_KILL
8. Active bankruptcy or delisting notice → INTEGRITY_KILL

**Pass/Fail:** For each candidate, render one-line verdict. Kill if fails any gate.

**Output:** List of candidates that PASS all gates. Add tickers that FAIL to KILL-LIST.md with reason.

---

## Stage 3: Quick Screen — Grab Live Market Data (Haiku, 1.0k tokens)

For each PASSING candidate:
1. Current price and market cap
2. Current daily volume (USD) — confirm <$3M
3. Analyst count (if any)
4. Gross margin (if from latest filing)
5. Revenue trend (last 2 quarters, if available)

**Output:** One-paragraph summary per candidate: "[Ticker] — $[market_cap]M, $[gross_margin]% GM, [analysts] analysts, [volume] daily vol. [One-line signal: backlog/order/margin strength/etc.]"

---

## Stage 4: Moat Check — Identify Moat Type (Sonnet, 0.5k tokens)

For each PASSING candidate (max 2–3, depth-over-breadth):

**Classify moat into one of:**
- MONOPOLY (sole producer)
- SOLE_SOURCE (design-locked, requalification barrier)
- REGULATORY (FDA/FAA/NRC approved, approval is the moat)
- PROCESS (proprietary manufacturing, difficult to copy)
- CONSUMABLE (recurring replacement, installed-base stickiness)
- SCARCITY (supply-constrained, geographic protected)

**Output:** "[Ticker]: [Moat Type] — [one-sentence explanation]. Potential 2x catalyst: [re-rating event]."

---

## Stage 5: Update KB Files (Haiku, 0.5k tokens)

**UNIVERSE.md:**
- Add all new PASSING candidates to the "Universe Map" table with status=QUEUED
- Update "Rotation Cursor" to the next candidate to deep-dive (if one is queued)
- Increment "Universe size" counter

**KILL-LIST.md:**
- Add all KILLED candidates with reason and date

**INDEX.md:**
- Add high-confidence moat candidates (CANDIDATE or better) to the quick-reference table

**DIGEST.md:**
- If any candidate reaches WATCH status (moat CONFIRMED + asymmetry VALIDATED), add to "Current WATCH List"
- Update date stamp

---

## Final Output Format

```
# Niche Moat KB — Hourly Scout Report [DATE/TIME]

## Candidates Passed Triage (added to UNIVERSE)
- [Ticker 1]: $[cap]M, [sector], moat=[TYPE], signal=[one-line]
- [Ticker 2]: $[cap]M, [sector], moat=[TYPE], signal=[one-line]

## Candidates Killed (added to KILL-LIST)
- [Ticker A]: [REASON]
- [Ticker B]: [REASON]

## Next Deep-Dive Candidate (in QUEUED queue)
- [Ticker C]: for full diligence on [DATE+1]

## KB Status
- Universe size: [N]
- Current WATCHes: [count]
- Queued for deep-dive: [count]
```

---

## Token Budget Allocation

| Stage | Model | Token Budget | Note |
|-------|-------|-------------|------|
| 1. Scout | Sonnet | 1,500 | 4-5 searches, broad sweeps |
| 2. Triage | Haiku | 1,500 | Mechanical gate checks |
| 3. Quick Screen | Haiku | 1,000 | Live market data pulls |
| 4. Moat Check | Sonnet | 500 | Moat classification |
| 5. KB Update | Haiku | 500 | File writes |
| **TOTAL** | | **5,000** | Per hourly run |

**Tuning:** If token budget exceeded, drop Stage 4 (Moat Check) and push to weekly deep-dive agent.

---

## Rules for This Run

1. **No deep diligence.** This is a triage + queue funnel. Full diligence happens separately on WATCH-promoted candidates.
2. **Stop and output if stuck.** If a search returns no results or data is unavailable, skip that sector and move to next.
3. **Sector rotation.** Cycle through 5 sectors per hour so universe grows across ALL industries, not just current focus.
4. **No defense sector.** Anything with keywords "defense," "military," "weapons," "aerospace (if primary customer is defense)" → SECTOR_KILL.
5. **Moat-first.** Only advance to CANDIDATE status if you can identify a specific moat mechanism (not just "small company with revenue growth").
