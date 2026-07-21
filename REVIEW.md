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

### 2026-07-20 — §7 REFLECT run #45 (45%3=0)

**1. Data quality audit (last 2 memos):**
- **RSL2.DE-2026-07-20.md** (R. Stahl AG): Correctly PARKed Grade D (Q3/F2/R1/C3). ATEX/IECEx process moat real, but revenue declining 3 years, EBIT near-zero FY2026, FCF burning, net debt growing, analyst PT only +12% above price. Memo correctly flags "Financials verified against primary filing: NO" (web-search-sourced, not primary-filing anchored). Triage kill reason update: TSTL.L COVERAGE_KILL applied correctly.
- **HNL.DE-2026-07-19.md** (Dr. Hönle AG): Correctly PARKed Grade D (Q2/F2/R2/C3). UV curing process moat real but 3 German analysts (not 0 as scouted), stale price anchor, and EV/Revenue 0.94x with €38.8M debt (not "0.55x P/S cheap" as triage snippet claimed). Memo correctly identifies these data errors and flags no primary filing verification.
- **Both memos properly formatted.** The "Financials verified against primary filing: NO" flag is the correct call in both cases — these are web-search-sourced baselines, not primary-filing anchored. No data quality defects found in these two memos beyond already-noted limitations.

**2. Kill list description errors — corrected this run:**
- **TPE.DE entry**: Kill list incorrectly described TPE.DE as "Technotrans SE (Xetra: TTR1.DE)" — a completely different company. TPE.DE is **PVA TePla AG** (SiC crystal growth furnaces + plasma systems + acoustic microscopy for semiconductor wafer inspection; ~70% semiconductor segment). Technotrans SE is TTR1.DE (thermal management for printing). The CAP_KILL conclusion was still correct (PVA TePla confirmed at ~€822M cap + 8 analysts = CAP_KILL + COVERAGE_KILL), but the company description was wrong. Fixed in KILL-LIST this run.
- **ELG.DE entry**: Kill list described ELG.DE as "ElringKlinger AG" — incorrect. ElringKlinger is ELK.DE. ELG.DE is **Elmos Semiconductor SE** (automotive ICs for LiDAR, driver assistance, ultrasonic park assist; ~€600-900M cap). CAP_SOFT_KILL conclusion remains correct. Fixed in KILL-LIST this run.
- **Root cause:** Company-ticker confusion when processing German XTRA names under time pressure. The analytical kill decision was correct in both cases; only the description field was wrong. **Systemic fix:** verify company name matches ticker via primary source (company website or official exchange listing) before writing kill list entry.

**3. False negatives re-checked:**
- **KRMD (KORU Medical Systems):** Correctly PARKed in UNIVERSE.md (quality=0, growth-stage losses, regulatory moat real but no earnings floor). The prior mention of "CAP_KILL (~$400M+, 9 analysts)" was a mis-citation — KRMD is not in KILL-LIST, it's in UNIVERSE as PARK 4/12. Current cap ~$179M, 5 analysts confirmed — PARK status correct (quality=0 blocks promotion regardless of cap or coverage). No change needed.
- **6742.T (Kyosan Electric):** Prior REFLECT (run #42) flagged ¥608 < ¥720 buy-zone as "BUY-ZONE TRIGGERED." Confirmed WRONG — current price ¥864 (confirmed by Agent 1 web search 2026-07-18), which is ABOVE the ¥720 buy-zone. The ¥608 figure was a stale/wrong source. WATCHLIST.md corrected this run: 6742.T flag removed, price updated to ¥864 (above buy-zone). No buy-zone trigger.

**4. Bench re-pricing (2026-07-20):**
All bench prices confirmed by web search agents (trust ~ not ✓ — snapshot.py remains blocked). Key finding:

| Ticker | Last price | Buy-zone | Status |
|---|---|---|---|
| WINA | ~$385.44 | ≤ ~20–22x PE | Above buy-zone |
| CODA | ~$9.84–$10.00 | $8–10 | Approaching (at upper boundary) |
| OFLX | ~$29.85 (~$308M) | ~$190–220M cap | Above buy-zone |
| DETEC.HE | **€8.38–8.70** | **≤€9.5** | **⚠ IN BUY-ZONE** |
| 4549.T | ~¥3,050+ | ¥2,000–2,400 | Above buy-zone |
| 6823.T (Rion) | ~¥3,485 | ¥2,200–2,400 | Above buy-zone |
| EKF.L | ~25.4p | ≤£80M cap (~14–16p) | Above buy-zone |
| 6742.T (Kyosan) | **¥864** | ¥720 | Above buy-zone (prior ¥608 flag was WRONG) |
| CGS.L | ~338p | 200–230p | Above buy-zone |
| EPEN.ST | ~156.20 SEK | 115–130 SEK | Above buy-zone |
| JOUT | ~$46.25 | $38–40 | Above buy-zone |
| SMID | ~$30.22 | ~$22–24 | Above buy-zone |
| ETON | ~$37.57 | ~$22–26 | Above buy-zone |

**Buy-zone triggered: DETEC.HE at €8.38–8.70 < €9.50 accumulate zone.** Promoted to QUEUED_HOT this run. §5 bench-promotion update memo written: memos/DETEC.HE-bench-2026-07-20.md. Adversarial red-team: CLEARED (12 failure modes; 2 flags embedded in Q=3). Grade B / CANDIDATE unchanged. Analyst count updated to 4 (from 3 in July 16 memo); consensus avg raised to €13.30 (from €12.18); gap to consensus now ~59% at €8.38. H1 2026 confirmed NOT yet published (August 6, 2026 — 17 days).

**5. Universe exploration audit:**
- Systematic enumeration (screen_eu.py, snapshot.py, EDINET API) remains blocked by proxy 403 — web search agents are the only working data source. This is a standing limitation carried from runs #37–45.
- Sector 17 (Semiconductor & electronics supply chain, 2nd pass, European geo lens) run this session: 23 names processed, 22 killed (15 new + 7 already-seen), 1 new QUEUED (CML.L 7/12).
- Sectors 18–19 active, sectors 0–4 THIN/EXHAUSTED, sectors 5–19 in rotation. No new sectors exhausted this run.

**6. Systemic fixes shipped this run:**
- Kill list company descriptions corrected for TPE.DE (PVA TePla, not Technotrans) and ELG.DE (Elmos Semiconductor, not ElringKlinger).
- WATCHLIST.md 6742.T price corrected ¥608 → ¥864 (buy-zone trigger removed).
- DETEC.HE promoted to QUEUED_HOT in WATCHLIST.md with §5 update memo.

---

### 2026-07-20 — §7 REFLECT run #48 (48%3=0)

**1. Data quality audit:**
- **STX.L.md REMS data defect corrected (run #48):** financials/STX.L.md previously claimed "REMS LOCK-IN + PROCESS + BRAND" as moat type. OPUS adversarial red-team (run #47, memos/STX.L-2026-07-20.md) confirmed ACCRUFeR has **NO REMS program**; NCE exclusivity expired July 2024; moat rests solely on a polymorph patent (Oct 2035) + prescriber habit + brand inertia. Moat type header corrected to "POLYMORPH PATENT + BRAND + INSTALLED-BASE (prescriber habit)." Correction notice block added to STX.L.md. This was the most significant KB data defect resolved this run.
- **MDP.TO Gleolan US rights corrected:** financials/MDP.TO.md §4 baseline revealed Gleolan US rights were **SURRENDERED March 2025** (NXDC agreement terminated) — triage moat claim was wrong. EMA Gleolan rights always with medac GmbH Germany. Real US moat = GRAFAPEX (treosulfan, 7-yr US orphan exclusivity ~Dec 2031). MDP.TO UNIVERSE.md and COVERAGE.md entries updated.
- **DXRX.L company name corrected:** Triage initially confused DXRX.L with "Diagnostyx plc" (formerly Yourgene Health). DXRX.L is **Diaceutics PLC** — a diagnostic commercialisation and data analytics platform (87% GM consistent with software/data model, NOT lab services). Correction added to financials/DXRX.L.md header.
- **SEDANA.ST price error corrected:** §4 baseline revealed actual price SEK 8.74 vs. triage assumption SEK 28-35. All SEDANA.ST calculations updated to use SEK 8.74. This was a ~3-4x price discrepancy.

**2. Bench re-pricing (2026-07-20):**
All bench prices confirmed by web search (trust ~ — snapshot.py remains blocked by Yahoo Finance 403). Key findings:

| Ticker | Last price | Buy-zone | Status |
|---|---|---|---|
| WINA | ~$385.44 | ≤ ~20–22x PE | Above buy-zone |
| CODA | ~$9.84–$10.00 | $8–10 | Approaching upper boundary |
| OFLX | ~$29.85 (~$308M) | ~$190–220M cap | Above buy-zone |
| EKF.L | ~25.4p | ≤~14-16p (~£80M cap) | Above buy-zone |
| 6823.T (Rion) | ~¥3,485 | ¥2,200–2,400 | Above buy-zone |
| 6742.T (Kyosan) | ~¥864 | ¥720 | Above buy-zone (prior ¥608 flag was WRONG — confirmed run #45) |
| **CGS.L** | **~260p** | **200-230p** | **⚠ APPROACHING (338p→260p; T-30-60p to trigger)** |
| EPEN.ST | ~156.20 SEK | 115-130 SEK | Above buy-zone |
| JOUT | ~$46.25 | $38–40 | Above buy-zone |
| SMID | ~$30.22 | ~$22–24 | Above buy-zone |
| ETON | ~$37.57 | ~$22–26 | Above buy-zone |
| **RX.V** | **~C$14.50 (~C$161M cap)** | **≤C$10-11/sh** | **DATA ERROR CORRECTED (prior C$7.50 was May 2023 stale data); now in extended zone — reassess asymmetry at corrected price** |
| 4549.T | ~¥3,050+ | a pullback to fair multiple | Above buy-zone (at 52-wk high area; not fresh-searched) |

**No buy-zone triggers this run.** CGS.L is approaching (T-30-60p). RX.V price corrected from stale 2023 data; buy-zone updated to ≤C$10-11/sh; now in extended zone at C$161M cap.

**WATCHLIST.md changes this run:**
- DETEC.HE removed — graduated to CANDIDATE Grade B in run #45; should not remain on bench.
- CGS.L price updated 338p → 260p with ⚠ APPROACHING flag.
- RX.V price corrected C$7.50 → C$14.50; buy-zone updated to ≤C$10-11/sh; extended zone noted.

**3. False negatives re-checked:**
- **PHO.OL (Photocure ASA, Oslo Bors):** COVERAGE_KILL confirmed valid. OPUS agent confirmed ≥4-7 Norwegian regional analysts (Pareto, DNB Markets, ABG Sundal Collier, Arctic, Carnegie confirmed). Photocure has a genuine REGULATORY MONOPOLY moat (sole FDA+EMA approved blue-light cystoscopy agent Hexvix/Cysview/HAL; 94% GM; patent to 2036; debt-free) — a quality kill, not a thesis kill. REVISIT ONLY IF analyst count drops to ≤2 through broker attrition AND cap corrects to ≤£30M.
- **RX.V (BioSyent, TSX-V):** WATCHLIST price corrected from stale May 2023 data (C$7.65 close = historical match). Current price ~C$14.50 (~C$161M cap) is in the extended zone; buy-zone ≤C$10-11/sh requires meaningful pullback. Quality thesis (62-quarter profit streak, 21% NI margin, net cash) intact; asymmetry not available at current price.

**4. Universe exploration audit:**
- Sector 10 (2nd pass, UK/European wholesale distributors): ~38 names processed; 0 new QUEUED. Structural thinness confirmed — PE consolidation removed most quality names, dominant distributors are private, over-covered, or >£1.5B cap. Sector 10 not yet EXHAUSTED (only 1 consecutive 0-new pass per ROUTINE.md rule).
- Deferred queue completions: SEDANA.ST → CANDIDATE Grade C (§5); MDP.TO → COVERAGE_KILL (§4); DXRX.L §4 complete + analyst count verified → §5 deferred.
- Systematic enumeration (screen_eu.py, screen_tw.py, EDINET API) remains blocked by proxy 403 — web search agents remain only working data source. Standing limitation.

**5. Systemic fixes shipped this run:**
- WATCHLIST.md DETEC.HE removed (graduated; no longer bench-eligible).
- WATCHLIST.md CGS.L price updated 338p → 260p with approach flag.
- WATCHLIST.md RX.V price corrected C$7.50-8.00 → C$14.50 with full correction note; buy-zone updated.
- STX.L.md moat type corrected from REMS_LOCK-IN to POLYMORPH PATENT + BRAND + INSTALLED-BASE; correction block added.
- UNIVERSE.md SEDANA.ST status QUEUED → CANDIDATE Grade C; MDP.TO QUEUED → COVERAGE_KILL.
- UNIVERSE.md DXRX.L entry: analyst count corrected from "4-5 borderline" to "2-3 confirmed PASSES gate"; §4 financial data added; status updated to §5 deferred run #49.

---

## 2026-07-21 — §7 REFLECT run #51 (51%3=0)

**Bench re-pricing (snapshot.py proxy-blocked; web-search fallback; all prices tagged ~):**

1. **4549.T Eiken Chemical (Japan FIT/LAMP)** — POTENTIAL BUY-ZONE. §7 REFLECT web-search confirms ¥2,145–2,354 range (2026-07-21 ~). Buy-zone is ¥2,000–2,400. **At ¥2,145–2,354 the stock is AT OR NEAR the lower boundary of the buy-zone** — first time in KB history 4549.T has traded inside its buy-zone. ⚑non-EN rule: yuho primary filing verification required before promoting to QUEUED_HOT. WATCHLIST updated. Note: price tagged ~ (web-search only); cannot tag ✓ until filing-anchored price confirmation.
2. **ELVA.TO Electrovaya** — Amazon warrant deal CONFIRMED FIRED July 15 2026. Stock C$15.89 at time of §7 check = **above buy-zone US$8.00-10.50 / C$11.00-14.50**. CATALYST → CANDIDATE. Re-entry thesis: pullback to C$11-13 / US$8-9 restores asymmetry if Amazon cumulative commitment US$280M + Jamestown factory ramp on-track. UNIVERSE.md and STATE.md updated.
3. **FAA.VI Fabasoft** — €11.80-12.00 range observed (below the €11.50-14.50 buy-zone lower end). More attractive entry than at memo write (€13.75). German E-Akte rollout catalyst unchanged.
4. **REC.L Record plc** — 54.11p (–37% from triage price ~86p). Watch for earnings catalyst confirmation.
5. **GENC Gencor Industries** — $15.18-15.20 range. IN BUY-ZONE ($12-16). Q3 FY2026 results expected August 2026 = hard-dated catalyst. NOTE: GENC WATCH memo (memos/GENC-2026-07-16.md) lacks the OPUS 12-mode adversarial red-team check. Deferred to run #52 after Q3 August 2026 data is available. Rationale: adversarial red-team on a name with a hard-dated Q3 catalyst is best run post-Q3 when the key load-bearing number (backlog → revenue conversion) can be verified directly.

**Sector 15 EXHAUSTED:**
- Sector 15 (Exchanges/data/niche financials) 3rd pass US geo lens (run #51): ~20 names processed; 18 killed; 2 PARKed (SAMG 5/12 Silvercrest UHNW RIA; HNNA 4/12 Hennessy Advisors mutual fund manager). **0 new QUEUED — 2nd consecutive 0-new pass → SECTOR 15 EXHAUSTED.** Structural finding: US exchange/clearing operators all >$7B cap; specialty insurance quality names $500M+ extended zone or reserve-concern-riddled; financial data providers absorbed by S&P/MSCI/FactSet; remaining RIAs/fund managers (SAMG, HNNA, GAMCO) have AUM-stickiness but floors are AUM-dependent not earnings-floor.
- REVIVE condition: new geo lens needed — Nordic/Scandinavian financial data niche (Oslo Bors/Nasdaq Stockholm micro-cap financial infrastructure) or ASX Australian securities infrastructure.

**False negatives re-checked:**
- **EAH.L (ECO Animal Health, AIM):** PARK valid confirmed. Generic tylvalosin erosion from China-based API manufacturers into EU markets = structural discount, not temporary mispricing. EV/EBITDA ~4x appears cheap but correctly prices eroding moat. Q≈1 disqualifies from Quality Bench. PARK 6/12 confirmed valid.
- **WATR.L (Water Intelligence, AIM):** PARK valid confirmed. 4 AIM analysts (knocked coverage axis to 0 in scoring), thin 5.6% net margin, no hard-dated catalyst — all three failure modes confirmed. Valid kill; not a false negative.

**Systemic fixes shipped this run:**
- WATCHLIST.md 4549.T price updated ¥3,050+ → ¥2,145–2,354 with POTENTIAL BUY-ZONE flag.
- UNIVERSE.md ELVA.TO status CATALYST → CANDIDATE; re-entry thesis noted.
- STATE.md Sector 15 passes 2→3; status ACTIVE→EXHAUSTED.
- STATE.md CATALYST count 1→0 (ELVA.TO graduated to CANDIDATE).
- UNIVERSE.md + STATE.md counter strings updated: 71→73 (SAMG PARK + HNNA PARK added); DXRX.L QUEUED→PARK corrected.
- KILL-LIST.md Sector 15 3rd pass US section added (18 kills, 2 PARKs).
- COVERAGE.md Sector 15 3rd pass US section added (EXHAUSTED status declared).

---

## 2026-07-21 — v4 TOOLING & METHODOLOGY UPGRADE (human-directed, out-of-band)

Applied by the operator after a diligence session, not by a REFLECT run:

1. **`tools/screen_tw.py` upgraded GM-only → full value-quality screen.** The TWSE `t187ap06_L_ci` endpoint exposes complete keyless fundamentals (revenue, gross profit, operating income, net income to parent, **EPS**), not just gross margin. The tool now outputs gross/operating/net margin, net income, EPS, derived share count, and — when a price feed is reachable — a live **P/E + market cap**. New flags `--min-om` and `--max-pe` (value gate). Price fetch is best-effort with query1→query2 fallback and **degrades to fundamentals-only when the feed is proxy-blocked** (so it still works in the cloud env). Taiwan is now our one non-English market with keyless primary-source fundamentals — rotate it in heavily.
2. **§3.5 PRICE-FEED FAILSAFE added.** Yahoo (snapshot.py price) is a known recurring proxy-block in the cloud. Rule: never tag a web-scraped price ✓ — mark it ~ (single-source), cap confidence, and a ~-price alone cannot support a CANDIDATE+ grade or Asymmetry-Gate pass. This closes the silent-✓ leak flagged in prior REVIEW entries.
3. **§1 DATA-REACHABILITY PRIORITY added.** US (SEC) and Taiwan (TWSE) are the two keyless, reachable, primary-source markets — give them the most enumeration runs. Japan/Korea are key-gated and often proxy-blocked → web-scout only until keys/feeds are wired.
4. **Geo override set to Taiwan** for the next run to exercise the upgraded screener end-to-end.

**Systemic fix still open:** restore a reachable live-price feed in the cloud env (the Asymmetry Gate depends on it); until then, foreign valuation runs at ~-trust.
