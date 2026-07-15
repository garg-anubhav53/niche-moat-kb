# Niche Moat KB — Cross-Industry Asymmetric Upside Hunter

An hourly-running Claude Routine that scouts for undervalued, moat-protected small-cap companies across all industries (except defense), identifies the highest-asymmetry re-rating candidates, and maintains a persistent universe of opportunities.

---

## The Thesis

**The edge:** Most institutional investors are excluded from companies with strong moats that trade at $20–300M market cap in thin volumes. These are exactly the names where:
- The moat is defensible (sole-source, regulatory lock-in, proprietary process, consumable recurrence)
- The market hasn't priced it in yet (coverage void, category mislabeling, foreign listing, fresh IPO)
- The re-rating catalyst is visible (analyst initiation, strategic contract win, capacity constraint)
- The floor is real (moat = durable earnings base, protected downside)

**Target outcome:** 2–3x upside on re-rating when the market eventually recognizes the moat. Minimal downside because the moat itself IS the value floor.

---

## How It Works

### The Hourly Routine

Every hour, the routine:

1. **Scouts** for niche-moat candidates across 5 rotating industry sectors (chemistry, medical, nuclear, industrial, aerospace)
2. **Triages** with automated gates (cap, volume, analysts, book equity, price move)
3. **Quick-screens** for moat characteristics (gross margin, revenue stability, market size)
4. **Classifies** the moat type (monopoly, sole-source, regulatory, consumable, scarcity, etc.)
5. **Updates** the persistent UNIVERSE map and KILL-LIST
6. **Commits** all changes to GitHub (audit trail)

**Token budget:** 4,000–5,000 per run (~$0.30–0.40)
**Time:** ~90 seconds per run

### The Universe Map

`UNIVERSE.md` maintains a persistent rotation through all candidates ever found:
- **WATCH:** moat verified, asymmetry confirmed (ready to act)
- **CANDIDATE:** moat plausible, needs deeper diligence
- **QUEUED:** passed triage, waiting for full diligence
- **Killed:** failed triage (price, cap, coverage, integrity, sector)

Weekly deep-dive agent promotes QUEUED → CANDIDATE → WATCH based on full forensic analysis.

---

## Key Files

| File | Purpose |
|------|---------|
| `DIGEST.md` | Doctrine, current WATCH list, macro observations |
| `UNIVERSE.md` | Persistent candidate map, rotation cursor, moat classifications |
| `KILL-LIST.md` | Failed triage (price-kills, cap-kills, sector-kills, etc.) |
| `INDEX.md` | Quick company reference (ticker, sector, moat, cap, analysts) |
| `ROUTINE-PROMPT.md` | The exact prompt for the hourly Claude Routine |
| `SETUP.md` | Complete setup instructions for GitHub + Claude Routines |

---

## Quick Start

### 1. Create GitHub Repo

```bash
git clone https://github.com/YOUR-USERNAME/niche-moat-kb.git
cd niche-moat-kb
git add .
git commit -m "init: niche moat kb, doctrines and structures"
git push origin main
```

### 2. Create Claude Routine

Go to `claude.ai/code/routines`:
- **Name:** `niche-moat-hourly`
- **Cadence:** Every 1 hour
- **Prompt:** Copy entire text from `ROUTINE-PROMPT.md`
- **Environment:** Set `GH_PAT` with repo write scope

### 3. Run Test

Click **Run Now**. Verify:
- Candidates were found
- Triage gates applied
- KB files updated
- Git push succeeded

### 4. Monitor

Check `UNIVERSE.md` weekly:
- How many new QUEUED candidates added?
- Which sectors are being covered?
- Any patterns in moats being found?

---

## Sector Rotation Schedule

Each hour cycles through one of 5 industries:

| Run # (mod 5) | Sector | Example Moats |
|---|---|---|
| 0 | Specialty chemicals & materials | Sputtering targets, coatings, thermal interface, catalyst supports |
| 1 | Medical diagnostics & consumables | Lab test kits, imaging components, calibration standards, contrast agents |
| 2 | Nuclear & radiological | Radiation detectors, shielding, decommissioning equipment, security instruments |
| 3 | Industrial precision components | Specialty bearings, seals, fasteners, valve trim, tooling inserts |
| 4 | Aerospace & satellite subsystems | Avionics, antenna systems, propulsion components, RF subcomponents |

---

## What Makes a Good Candidate

**Green flags:**
- Gross margin >40% (pricing power from moat)
- 0–3 sell-side analysts (coverage void)
- $20–300M market cap (exclusion zone sweet spot)
- <$3M daily volume (thin but tradeable)
- Revenue is recurring (consumables, contracts, frameworks) — not lumpy one-time sales
- Moat is defensible (sole-source, regulatory, process, supply-constrained)
- Earnings on a recovery path or inflection (not stagnant/declining)

**Red flags that kill the thesis:**
- 12-month return >+100% (asymmetry already spent)
- Negative book equity (floor is fake)
- Defense primary end-market (excluded by design)
- Commodity-like product with many competitors (no moat)
- Deteriorating gross margins (structural pressure)

---

## Integration with Other KBs

This routine is sibling to the **Semiconductor Backlog KB** routine but:
- **Broader scope:** all industries except defense (vs. semis-only)
- **Shorter cadence:** hourly (vs. every 2 hours)
- **Shallower per-run:** 5k token budget (vs. deeper dives on fewer names)
- **Persistent universe:** rotates through candidates systematically (vs. one-off scouts)

---

## Token Efficiency Tricks

1. **Sector rotation:** Don't search every sector every hour; cycle through 5 industries
2. **Triage first, deep-dive later:** Hourly is just funnel; Sonnet deep-dive is separate weekly
3. **Haiku for gates:** Cheap mechanical filtering (cap, volume, analysts, book equity)
4. **Stop and output:** If a search times out, move to next sector; don't wait for perfection
5. **No schema on heavy writes:** Avoid Sonnet + structured output on file updates

---

## Expected Results (First Month)

- **Universe size:** 100–150 new candidates screened
- **WATCH promotions:** 2–4 companies deemed asymmetry-ready
- **CANDIDATE pool:** 8–15 with moats plausible enough for deep-dive
- **Kill rate:** ~70% fail triage (expected due to cap, volume, coverage, price-already-moved)

---

## Costs

| Item | Monthly Cost |
|------|------|
| Claude Routine (Sonnet 4.6, ~730 runs × 5k tokens) | ~$250–300 |
| GitHub (free public repo) | $0 |
| **Total** | ~$250–300/month |

*(Estimate; adjust based on actual token consumption in first 2 weeks.)*

---

## FAQ

**Q: Why hourly vs. daily?**  
A: Hourly allows broad sector coverage (all 5 industries per day) with lightweight triage gates. Daily would compress runs; hourly spreads it out.

**Q: How is this different from screening?**  
A: Screening is top-down (rules + data). This is moat-first (pattern recognition + human judgment). Haiku can triage; Sonnet classifies moats.

**Q: Why avoid defense?**  
A: Defense procurement is slow and governed by sole-source rules already known to institutions. The moat is less information-based and more bureaucratic.

**Q: When do I actually buy?**  
A: When a candidate reaches WATCH status (moat confirmed, asymmetry validated, floor real, catalyst visible). That's when the opportunity thesis is complete.

**Q: Can I use this for other markets (crypto, growth stocks, etc.)?**  
A: The moat-first framework is universal. Swap out "markets" in the sector rotation, adjust cap/volume bands for your target universe.

---

## Future Enhancements

1. **Deep-dive agent (weekly):** Promote QUEUED → CANDIDATE with full diligence
2. **Catalyst monitor:** Track announced contracts, regulatory approvals, earnings dates for WATCH names
3. **Peer comparison:** Auto-build valuation comps for each moat type
4. **Acquisition target scoring:** Flag companies likely to be acquiree at premium multiple
5. **Sector thesis rotation:** Monthly updates on macro conditions per industry

---

## Support

For questions or improvements, add issues to the GitHub repo.

---

*Last updated: 2026-07-16*  
*Routine cadence: Hourly*  
*Model: Claude Sonnet 4.6 + Haiku 4.5*  
*Token efficiency target: 4–5k per run*
