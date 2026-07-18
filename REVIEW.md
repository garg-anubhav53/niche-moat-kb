# REVIEW — KB Self-Audit Log

Every ~6th run (§7 REFLECT), the routine steps back from finding names to audit the KB's own health, then makes corrective edits the same run. This is the append-only log of those audits: what was checked, what was wrong, what changed, and the systemic fix to carry forward.

Three standing questions:
1. **Right input data?** Are financials quote-anchored, checker-passed, filing-verified — or thin/unverified? (A CANDIDATE graded without a solid baseline is a defect.)
2. **Exploring the universe well?** Sector coverage (5-19 vs. re-mining 0-4), geographic spread, hit-rate trend, grade mix.
3. **False negatives?** Re-check a couple of recent triage-kills with real numbers — did we wrongly kill a good name on a snippet?

---

## Audit log

### 2026-07-18 — Candidate-list prune (multi-agent workflow) surfaced the biggest systemic leak
- **What:** 33 deep-dived names assessed for genuine asymmetry → only **10 kept** (FAA.VI, EUZ.DE, GENC, PDEX, ELVA, ANIK, FEW.F, CEMX.TO, 6743.T, LBL.AX); 23 culled.
- **The pattern (root cause):** almost every reject was a *genuinely good business* where the **asymmetry wasn't available at today's price** — already re-rated / near 52-wk high (4549.T, HURC, ETON, IOF.L, EPEN.ST), at consensus fair value (CGS.L, CODA, EKF.L, SINT.ST, REC.L), upside capped <2x or symmetric/inverted (DETEC.HE, OFLX, KVHI, SMID, HBB, KMK), slow multi-year grind with no dated trigger (HURC, OFLX, JOUT, 6742.T), or structural-discount value traps (CIX, NATR). The routine was qualifying on **moat + quality** but not on whether the **mispricing was still on the table.**
- **Fix shipped:** added the **Asymmetry Gate** (METHOD.md + ROUTINE §4) — a name qualifies as CANDIDATE+ only if entry is still open (not near high / not at PT / not already 2x'd), realistic bull ≥~2x, payoff skewed, and a *discrete* trigger or CORE-grade quality. Fail → PARK, not CANDIDATE. Diffuse catalysts (cycle-turns / buyback-someday / analyst-may-notice / coverage-void-alone) explicitly don't count.
- **Next systemic fix:** the gate needs the §3.5 baseline to carry 52-wk range + analyst PT so it can be applied mechanically; ensure fetchers pull those two fields.


### 2026-07-18 — Baseline established (methodology upgrade, not an automated run)
- **Data quality:** Financial diligence just moved from snippet-based to a mandatory §3.5 baseline: quote-anchored fetch (haiku) + deterministic `tools/fin_check.py` reconciliation + calibrated trust tags + filing verification in deep-dive. Earlier memos (runs 1–39) were graded WITHOUT this — treat their financial figures as provisional until re-verified. **Action for next REFLECT runs:** re-verify the financial baselines of the current WATCH/CORE/CATALYST names (GENC, EUZ.DE, ELVA.TO) and top CANDIDATEs (ANIK, CODA) against primary filings; downgrade any that don't hold to NEEDS-DATA.
- **Universe:** Sectors 0–4 exhausted; expanded to 20 sectors + geo lens (fixed this session). Early new-sector runs (5–19) are landing (Winmark, HNL.DE, etc.). Watch that runs actually advance the cursor into 5-19 rather than drifting back.
- **False negatives:** Not yet audited. The ~600+ triage-kills from runs 1–39 were snippet-based; a sample should be re-checked once §3.5 is live.
- **Systemic fix to carry forward:** the two-tier "fetch cheap / reason well" split + deterministic checker is the durable lever; keep pushing quality into *structure* (scripts, quote-anchors), not *exhortation*.

### 2026-07-18 — §7 REFLECT run #42 (42%3=0)
- **Bench re-pricing:** snapshot.py blocked (Yahoo Finance not accessible in remote execution environment) → fell back to web searches for all 13 bench names. Prices as of 2026-07-18: WINA $385.44, CODA $9.84-$10.00, OFLX ~$29.85 (~$308M cap), JOUT $46.25, SMID $30.22, ETON $37.57, DETEC.HE ~€11.25 (ambiguous — €8.38 cited June 26; €11.25 stated as "last close"; likely more recent; flagged as SINGLE-SOURCE), EKF.L 25.4p, 6823.T ¥3,485, 6742.T ¥608, CGS.L ~338p (June 29), EPEN.ST 156.20 SEK, 4549.T ~¥3,050+ (near 52-wk high per earlier data; not fresh-searched).
- **Buy-zone triggered: 6742.T Kyosan Electric ¥608 < ¥720 buy-zone.** However: ⚑non-EN (Japan TSE, J-GAAP only); already in UNIVERSE.md as CANDIDATE Grade C (C=3); requires primary-language yuho verification before promotion to QUEUED_HOT. Flagged but NOT auto-promoted.
- **CODA approaching buy-zone:** at $9.84-$10.00, at the upper boundary of $8-10 buy-zone. Not yet triggered. Monitor.
- **Right input data:** All 13 bench prices are web-search-sourced (trust ~), not snapshot.py verified. Non-EN filers (6742.T, 6823.T, 4549.T) have additional trust caps. The buy-zone trigger for 6742.T must be verified from snapshot.py or live quote before acting.
- **Universe exploration:** Run #42 sector 14 Japan geo lens; 5889.T CANDIDATE Grade B/C is the only new name promoted. 4668.T Meiko PARK 5/12 confirmed (no moat + structural juku decline). Running total 63 names.
- **False negatives:** Not formally audited this run. The ~600+ prior triage-kills remain unaudited; systematic re-check deferred to a future REFLECT run once snapshot.py access is restored.
- **Systemic fix to carry forward:** The web-search fallback for bench re-pricing works but is trust-capped. Priority: restore snapshot.py or implement an alternative reliable price feed so bench updates are ✓-trust rather than ~-trust.

### 2026-07-18 — Ironclad price/valuation via public API (not LLM web-reading)
- **Problem:** even with quote-anchoring, an LLM reading price/market-cap/revenue off web pages isn't trustworthy; and the 52-week framing was noise.
- **Fix:** `tools/snapshot.py TICKER` — live price (Yahoo chart, no auth, US+foreign) + most-recent revenue/GM/net-income/shares from **SEC EDGAR XBRL** (primary filing), then **computes market cap = live price × shares** and P/S, P/E itself (no aggregator trust). Handles the dual-class / stale-cover-page trap (falls back to weighted-avg diluted; flags staleness so a wrong market cap can't ship). Foreign filers → live price only, cap C≤2.
- **Caught a real error:** GENC cover-page tag was stale (2014, 8.0M shares) → would have printed a $128M market cap; true current count is 14.66M → **$235M** cap, P/S 1.92, P/E 13.7. Exactly the silent false-precision we were worried about.
- **Gate change:** dropped the 52-week-range test entirely. Entry test is now purely **live price vs. fair value** — the gap is the asymmetry.
- **Next:** extend snapshot.py to also pull cash/total_debt from SEC XBRL (CashAndCashEquivalents, Debt tags) so net-cash is API-sourced too, not fetcher-read.

### 2026-07-18 — Memo red-team (FAA/ELVA/PDEX external critique) → Opus adversarial pass added
- **What happened:** a separate deep human+Claude review of three shortlist memos found the SAME class of errors in all three: **fabricated/stale load-bearing numbers presented as verified** (FAA wrong auditor + invented founding family + backwards concentration; PDEX "20% GM" was 31%; ELVA stale $9.59 price anchor), **one-offs inflating a "cheap" multiple** (PDEX Monogram gain → really ~24x not 17x), **absence-of-catalyst scored as catalyst** (FAA R=5 on "coverage void"), **survivorship base rates** (FAA "3 of 4 re-rated" = the winners), **hard-rule overrides** (FAA granted A with C=3), **revenue-quality mislabeling** (FAA "recurring" = services; PDEX growth cannibalizing high-margin repair), **missed thesis-flipping disclosures** (PDEX 2028 contract extension), **unfalsifiable triggers** (PDEX Sept-3 EPS is CVR-contaminated), and **asymmetry already captured** (ELVA spiked 40%, gap paid out).
- **Fix shipped:** METHOD.md **Adversarial Red-Team (12 failure modes)** + a mandatory **OPUS pass on every cleared candidate** (§5) whose job is to BREAK the thesis and output a **RISK PROFILE** (load-bearing assumption, clean operating earnings & what it's actually worth, informative trigger, moat durability 3/5/10yr, revenue-quality decomposition, the disclosure that would flip it, return if nothing re-rates). A name is CONFIRMED only after surviving all 12.
- **Applied to the motivating names:** FAA.VI, PDEX, ELVA all flagged RED-TEAM FAILED in DIGEST with corrected reads (FAA → Bench high-single-digit compounder; PDEX → HOLD ~24x clean; ELVA → asymmetry spent).
- **Deepest lesson (the cascade):** one fabricated number becomes a confident false narrative downstream — the critic himself built a whole "no pricing power" thesis on PDEX's fake 20% GM. The only defense is **re-derive every load-bearing number from the primary filing for a single stated period BEFORE reasoning**, and treat "too good to be true" as a data alarm.
