# COVERAGE — the denominator, and how much of it we've seen

The point of the top-of-funnel rework: stop *hoping* web search surfaces names, and instead **enumerate a known universe and march through it best-first**, so we can answer "what % of the worthwhile microcaps have we actually looked at?"

## The worthwhile universe (the denominator)

**US — fully enumerable via SEC frames (`tools/screen.py`, deterministic, ~4 API calls, zero LLM):**
- All filers reporting revenue: ~4,200
- Worthwhile subset — revenue $20–400M, gross margin 45–95%, **profitable**: **~78** (as of CY2025; ~236 if you include cash-burners)
- This is the denominator. Coverage % = (US names deep-reviewed) ÷ 78. **A run that reviews the top-10 unreviewed covers ~13% of the worthwhile US universe.** By a handful of passes we can honestly cover the *majority* of profitable high-margin US microcaps — and know it.
- The screen is ranked by a quality proxy (operating margin, gross margin, capped growth), so we march **best-first** — even partial coverage captures the best names.

**International data sources — VERIFIED (probed 2026-07-18):**

| Market | Bulk source | Key? | Status |
|--------|-------------|------|--------|
| **US** | SEC XBRL `frames` API | none | ✅ built+tested (`screen.py`) — full GM+profit filter, ~78 names |
| **Taiwan** | TWSE OpenAPI (keyless) | none | ✅ built+tested (`screen_tw.py`) — full GM filter, ~64 names |
| **Europe** (EU exchanges + UK) | filings.xbrl.org ESEF/UKSEF (keyless) | none | ✅ built+tested (`screen_eu.py`) — enumeration; per-name fundamentals |
| **Japan** | EDINET API v2 | free key | ✅ built+tested (`screen_jp.py`) — key set in env; **BUT proxy blocks outbound to EDINET (403 Forbidden run #42 and run #43)** — web search fallback used for both Japan runs; 0% EDINET systematic coverage to date; fix: allow `api.edinet-fsa.go.jp` in environment network policy |
| **Korea** | OpenDART (`opendart.fss.or.kr`) | free key | ⏳ `screen_kr.py` pending `OPENDART_KEY` |
| **Canada** | mostly via SEC (many TSX names file 40-F/20-F, already in US frames) + per-name Yahoo (.TO) | none | partial |
| **Australia/NZ** | no free bulk fundamentals; per-name Yahoo (.AX/.NZ) | none | per-name |
| **UK (also)** | Companies House API (free key) — but UK already covered by filings.xbrl.org UKSEF | free key | redundant |

**Build order:** Europe (filings.xbrl.org) + Taiwan (TWSE) are keyless → build next. Japan/Korea → build once the free keys are set as env vars in the routine environment. Canada is largely absorbed by the US frames (cross-listed 40-F filers); pure-domestic TSX names go per-name. For any market without bulk fundamentals, the denominator is "all listed in cap band" (exchange list) and we march per-name with `snapshot.py` price + the filing.

## Ledger — reviewed vs. remaining (updated by the routine)

| Universe | Denominator | Reviewed | Coverage % | Cursor (next best-unreviewed) |
|----------|-------------|----------|-----------|-------------------------------|
| US profitable high-GM microcaps | ~78 | 0 | 0% | run `screen.py`, start rank 1 |
| Japan (EDINET) | TBD (needs key) | 0 | — | pending EDINET key |
| Korea (OpenDART) | TBD (needs key) | 0 | — | pending OpenDART key |
| Other exchanges (list-enumerated) | per exchange | — | — | rotate |

*The routine refreshes `screen.py` periodically (the universe drifts as filings update), marks each reviewed CIK in SEEN, and advances the cursor down the ranked worklist. Never re-screen a SEEN ticker.*

## Sector 18 (Precision instruments & sensing) — Pass 2 Coverage Notes (run #46, 2026-07-20)

**US geo lens (Nasdaq/NYSE):** Structurally sparse. M&A wave removed most quality public micro-caps:
- FARO Technologies → acquired by Ametek, delisted Nasdaq July 2025 (sole-source 3D metrology moat was real)
- Luna Innovations (LUNA) → Nasdaq suspended Jan 2025; Form 25 + Form 15 filed; went dark (ODiSI OFDR moat real but thesis unexecutable)
- MTS Systems → acquired by Amphenol 2021; NI (National Instruments) → acquired by Emerson 2023; Thermon → acquired by CECO; Starrett → pending privatization
- Remaining public names (MLAB, TRNS, VPG, INTT, COHU, MASS) all either over-capped or already reviewed in prior runs
- Net result: **0 new QUEUED from US; 1 PARK (CLIR dev-stage INTEGRITY_KILL); 1 CAP_SOFT (Mistras Group ~$580M)**

**Taiwan geo lens (TWSE/TPEx):** Similarly thin. Most precision instrument names either >$1B cap (Chroma ATE 2360.TW, MPI Corp, Hiwin) or failed other gates:
- 6830.TW (MSSCorps) → INTEGRITY_KILL + CAP_SOFT: net losses, "CPO monopoly" investor narrative refuted (iST + Hongkang competing)
- 4537.TWO (Shuz Tung Machinery) → PARK 5/12: WisePioneer inspection niche real but not sole-source; legacy pipe bender dilutes moat; non-EN filing
- Net result: **0 new QUEUED from Taiwan; 1 PARK**

**Deferred queue resolutions:**
- HVO.L → COVERAGE_KILL: triage "0-1 analysts" was a data error; financial fetch confirmed 7 analyst estimates
- CML.L → PARK Grade D after §5: real PMR qualification moat; but adj PBT -£1.76m; rev declining -11%; sole analyst target 223p < 265p market price; asymmetry gate FAIL 4/4

**Sector 18 status: 2 passes complete. Next pass should use European geo lens (German XTRA precision instruments, Swiss SIX) or Japan non-EN secondary names (6853.T and 6858.T from deferred queue first).**

---

## Sector 19 (Specialty healthcare services & niche pharma) — Pass 2 Coverage Notes (run #47, 2026-07-20)

**UK AIM + ASX + Nordic/Canada geo lens:** ~38 names processed; ~27 killed; 4 advanced to QUEUED/WATCH; 1 Quality Bench addition (RX.V BioSyent).

**Coverage kills — notable high-quality names excluded by analyst count:**
- PHO.OL (Photocure ASA, Oslo Bors): sole FDA+EMA approved blue-light cystoscopy agent (Hexvix/Cysview, HAL); 94% gross margin; debt-free; patent to 2036. COVERAGE_KILL: 5-7 Norwegian regional analysts (Pareto, DNB Markets, ABG Sundal Collier, Arctic, Carnegie). KB baseline written at financials/PHO.OL.md.
- CUV.AX (Clinuvel Pharmaceuticals, ASX): sole FDA+EMA approved EPP treatment (afamelanotide/SCENESSE); REGULATORY MONOPOLY. COVERAGE_KILL: 7 ASX analysts.

**QUEUEDs advancing to §4/§5:**
- STX.L (Shield Therapeutics, AIM): ACCRUFeR #1 branded oral iron US; +54% FY2025 revenue; QUEUED_HOT → §5 → **WATCH Grade C** (Q2/F2/R3/C2). REMS moat fabricated; polymorph-only patent; 5x dilution; AOP controlling at 3.0p; Viatris terms confidential. Asymmetry Gate FAIL (cond3: fat downside). Buy-zone ~3.0–4.0p. memos/STX.L-2026-07-20.md.
- DXRX.L (Diaceutics, AIM): Precision Medicine Implementation (PMI) platform connecting pharma to lab networks; ~£120M cap; 4-5 analysts (borderline). QUEUED ~6-7/12; next §4 financial baseline.
- SEDANA.ST (Sedana Medical, Nasdaq Stockholm): AnaConDa inhaler device for volatile ICU sedation (isoflurane/sevoflurane); sole approved device for prolonged ICU volatile anaesthesia; ~$75M cap; 3 analysts. QUEUED ~7/12; next §4 financial baseline.
- MDP.TO (Medexus Pharmaceuticals, TSX): Gleolan (5-ALA fluorescence-guided glioma surgery; sole FDA/EMA approved); IXINITY, Rupall; ~C$120M cap; 3-4 analysts. QUEUED ~6/12; next §4 financial baseline. Moat concentration check needed (Gleolan vs. other drugs).

**IHC.L reclassification:** IHC.L (Inspiration Healthcare Group, AIM) reclassified from NO_MOAT_KILL to PARK. Prior kill description was applied without reading primary AIM filing; 0.4x P/S discount warrants investigation before full kill; SLE neonatal ICU ventilator specialist position may differentiate from general neonatal respiratory competitors (Dräger, F&P, Intersurgical). CAP_KILL concurrent at ~£20M. Revived to PARK pending primary filing read.

**Quality Bench addition:** RX.V (BioSyent Inc, TSX-V): Canadian specialty pharma; 62-quarter consecutive profit streak; 21% net income margin; net cash; high quality (Q≥4) but Asymmetry Gate fails at current price (at/near fair value; no discrete catalyst). Added to WATCHLIST Quality Bench. Buy-zone: ~C$5-6 (~30%+ cap correction).

**Notable PARK from §4 baseline (run #47b):**
- EAH.L (ECO Animal Health Group, AIM): Aivlosin/tylvalosin veterinary antibiotic; REGULATORY moat genuine but generic tylvalosin erosion is active (off-patent API; China generic entrants); EV/EBITDA ~4x structurally discounted not mispriced; NI margin 4.2% thin; Asymmetry Gate 4/4 fail. PARK 5/12. REVISIT IF generic erosion arrested ≥2 qtrs + cap below £40M. financials/EAH.md.

**Deferred queue update (run #47b):** 6853.T Kyowa Electronic Instruments resolved PARK Grade D (FCF negative; P/E 22.8x premium; Asymmetry Gate 4/4 fail; memo memos/6853.T-2026-07-20.md). Active deferred queue now: 6858.T only.

**Sector 19 status: 2 passes complete. Deferred queue: 6858.T Ono Sokki 6/12 (⚑non-EN yuho required before §5). Next sector rotation: Sector 10 (2nd pass, UK/European wholesale distributors).**

---

## Sector 10 (Value-added/sole-line distribution) — Pass 2 Coverage Notes (run #48, 2026-07-20)

**UK AIM + European exchanges geo lens:** ~38 names processed; 0 new QUEUED. Structural thinness confirmed as a durable characteristic of the sector, not a data gap.

**Why UK/European sole-line distribution is structurally thin for this screen:**
- **PE consolidation wave (2015-2023):** most quality micro-cap distributors with genuine niche exclusivity have been acquired by private equity (Bunzl, DCC, Diploma, Wolseley successors now large-cap; numerous former AIM distributors delisted/privatised). What remains public is either commodity-ish distribution or over-covered mid-cap.
- **Dominant moated names are private:** RS Group (formerly Electrocomponents), Brammer/Rubix, Würth, Hagemeyer all private or >£1.5B. The genuine "sole-line specialist with contractual switching costs" names tend to go private quickly.
- **AIM small-cap distributors reviewed:** ~20 UK AIM names at £20-300M cap; near-universal result: thin margins (3-8% EBIT), commodity product ranges, no contractual lock-in, multi-supplier switching easy. No QUEUED names survived.
- **European exchange names reviewed:** ~18 names on Xetra, Euronext, Nasdaq Stockholm in cap range; same structural result — food/industrial distributors with GM 15-30%, regional competitors, no moat claim.

**Net result: 0 new QUEUED from ~38 names; 1st consecutive 0-new pass for Sector 10 2nd pass.**

**Sector 10 status:** ACTIVE (not yet EXHAUSTED — ROUTINE.md requires 2 consecutive 0-new passes). Next pass should try Nordic specialist distributors (Stockholm/Oslo micro-cap) or Australian ASX distribution niche if any moated names remain unlisted.

---

## Sector 12 (Life-science tools & lab consumables) — Pass 3 Coverage Notes (run #49, 2026-07-20)

**Nordic / Canada / Australia geo lens:** ~20-25 names processed; 0 new QUEUED. 1st consecutive 0-new pass for Sector 12.

**Why Nordic/Canada/Australia life-sci tools is structurally thin at this cap range:**
- **Nordic:** Quality names are either (a) private/subsidiary of large-cap (Gyros Protein Technologies → Hamilton subsidiary; DIATEC Monoclonal → private; Nordic Bioscience → private), (b) development-stage INTEGRITY_KILL (pre-revenue biotech making up bulk of Nasdaq Stockholm life-sci listings), or (c) over-capped (Biotage AB ~SEK 7B; CELLINK/BICO ~SEK 5B). Names that survive Nordic screens often have thin revenues or are essentially lab services (not platform/consumable with moat). Israel explicitly excluded (JURISDICTION_KILL — hard rule applies to all Nordic-adjacent Israeli life-sci tools, which form a large part of the "Nordic" biotech pool, e.g., many dual-listed names).
- **Canada:** TSX/TSX-V life-sci tool names are sparse. Most quality Canadian life-sci tools either (a) cross-listed on Nasdaq/NYSE (already in SEEN set via US pass), (b) development-stage (no revenue), or (c) service-based CRO/CMO (no platform moat).
- **Australia:** ASX life-sci tool names at A$20-300M are predominantly development-stage (pre-clinical or Phase I/II therapeutics that happen to have "tools" in marketing materials) → INTEGRITY_KILL. Genuine ASX life-sci equipment/consumable manufacturers that might have moats are either private (Hologic ANZ subsidiary, BD ANZ subsidiary) or over-capped (CSL at A$130B).
- **Israel excluded (JURISDICTION_KILL):** Numerous Israeli life-sci tools companies (Given Imaging, Orbotech successors, many Nasdaq dual-listed diagnostics names) are excluded per JURISDICTION_KILL hard rule regardless of quality.

**Net result: 0 new QUEUED from ~20-25 names; 1st consecutive 0-new pass.**

**Sector 12 status:** ACTIVE (not yet EXHAUSTED — ROUTINE.md requires 2 consecutive 0-new passes). 1 pass to go before EXHAUSTED. Next pass options: US micro-cap life-sci tools (systematic SEC XBRL screen) or Japanese secondary OTC life-sci tool names (EDINET when proxy access restored). Do not attempt another Nordic/Canada/Australia pass — structural thinness now well-established.

**Deferred queue note (run #49):** DXRX.L (Diaceutics, AIM — Sector 19 crossover, not pure Sector 12) was the Sector 12/19 §5 deep-dive completed this run. Sector 12's own candidates (TSTL.L, 6823.T Rion) were previously resolved (TSTL.L → COVERAGE_KILL run #44; 6823.T → CANDIDATE Grade B run #40).

---

## Taiwan GEO OVERRIDE — Run #50 (2026-07-21)

**Screen:** `tools/screen_tw.py --min-gm 45 --min-om 12` → **TWSE OpenAPI proxy-blocked (403 Forbidden)**; fell back to §2B web-search scout for all Taiwan names. All data tagged ~.

**Coverage:** ~17 Taiwan names processed across TWSE (main board) and TPEX (OTC board), covering precision instruments (Sector 18 geo lens), semiconductor testing services, medical devices, specialty chemicals, and semiconductor equipment.

**Result: 0 new QUEUED. All names killed at §3 triage.**

### Kill summary (Taiwan run #50)

**No-Moat Kills (GM below 45% gate) — 7 names:**
- 8021.TW Topoint Technology — archery equipment OEM; GM ~27%; NO_MOAT_KILL
- 3289.TWO iST International — semiconductor testing services; GM 26.96%; NO_MOAT_KILL
- 8103.TW CviLux — electrical connectors; GM ~20%; NO_MOAT_KILL
- 3055.TW Spirox Medical — ENT devices; GM ~16%; NO_MOAT_KILL + CAP_SOFT concurrent
- 1733.TW Apex Biotech — OEM rapid diagnostic kits + glucose meters; GM ~28%; NO_MOAT_KILL
- 4746.TW Formosa Laboratories — API pharmaceutical intermediates CDMO; GM ~41.9%; NO_MOAT_KILL (below 45% gate)
- 3583.TW Scientech Electronics — semiconductor equipment agency + own-brand wet process equipment; GM ~30-32%; DUAL-KILL: NO_MOAT + CAP ($2.03B)

**Cap/Extended-Zone Kills — 5 names:**
- 4749.TWO Advanced Echem Materials — specialty semiconductor photoresists; cap ~$1.8B; CAP_KILL
- 7769.TW Hon. Precision — IC test handlers; cap well above $300M; CAP_SOFT_KILL
- 6146.TWO Sporton International — EMC/safety certification lab; cap ~$624M extended zone; declining revenue; CAP_SOFT_KILL
- 4736.TW TaiDoc Technology — OEM glucose meters/CGM; cap ~$377M extended zone; declining revenue; CAP_SOFT_KILL
- 5536.TWO Acter Group — fab EPC services; cap ~$4.7B + GM ~21% + revenue $1.3B; TRIPLE-KILL

**Coverage Kill — 1 name:**
- 4772.TWO Taiwan Speciality Chemicals Corporation — specialty semiconductor chemicals; ~5 analysts; COVERAGE_KILL

**Quality Kill — 1 name:**
- 6934.TWO HCmed Innovations Co. — vibrating mesh nebulizer CDMO; GM ~62% passes gate; cap ~$83M in zone; BUT pre-commercial losses (quality=0); $3-4M USD revenue (dev-stage); one-client concentration; QUALITY_KILL

**Triple-Kill — 2 names:**
- 6223.TWO MPI Corporation — probe cards; cap ~$18B + 11 analysts + revenue $418M; TRIPLE-KILL (cap + coverage + revenue)
- 5536.TWO Acter Group — (also counted above); TRIPLE-KILL (cap + no-moat + revenue)

### Notable near-misses
- **6223.TWO MPI Corporation:** Highest-quality Taiwan name encountered — probe cards 72% revenue, GM 53.8%, OP 28.5%. But cap ~$18B = 60x limit; 11 analysts. Would be high-priority QUEUED if cap corrects below $300M. Monitor for spinoff/restructuring.
- **6934.TWO HCmed:** Genuine niche CDMO moat structure (3 global players; FDA regulatory lock-in once device co-filed; multi-year CDMO relationships). Revisit if: (a) revenue reaches $20M+ USD, (b) net income positive, (c) second US client relationship confirmed.

### Deferred queue update (run #50)
- 6858.T Ono Sokki: **revised 6/12 → 8/12** with FY2026 guidance data (fwd P/E ~11x; net cash 31% of cap; orders > revenue; H1 FY2026 earnings July 29 2026 hard-dated). §5 STILL BLOCKED: (a) EDINET proxy-blocked; (b) GM unverified from primary filing. financials/6858.T.md written this run.

**Sector 18 status:** 2 passes complete. Taiwan geo lens EXHAUSTED (0 survivors from ~17 names). Next Sector 18 pass: European geo lens (German XTRA precision instruments / Swiss SIX) or Japan secondary names (post-EDINET access).

**GEO OVERRIDE cleared.** Next scheduled rotation: Sector 10 3rd pass (Nordic specialist distributors or ASX niche). Sector 15 now EXHAUSTED (2 consecutive 0-new passes).

---

## Sector 15 (Exchanges/data/niche financials) — Pass 3 Coverage Notes (run #51, 2026-07-21) → **EXHAUSTED**

**US geo lens:** ~20 names processed; 0 new QUEUED. 2nd consecutive 0-new pass → Sector 15 → **EXHAUSTED**.

**Why US exchanges/data/niche financials is structurally exhausted at $20-300M:**
- Exchange/clearing operators all large-cap ($7B+): CME, ICE, Cboe, Nasdaq, MarketAxess all massively above ceiling
- Specialty insurance (E&S/admitted) is extended zone: quality US E&S/specialty insurers (SKWD ~$1.5-2B, PLMR ~$2-3B, KNSL ~$6B, JRVR ~$400-600M, GBLI ~$500M, PRA ~$750M) are $400M+ extended zone or carry reserve quality concerns
- Financial data/analytics absorbed or private: S&P Global/MSCI/FactSet/Morningstar all >$10B; DFIN ~$1B coverage-heavy remaining
- Specialty financial services small-caps: RIAs/fund managers (SAMG, HNNA, GAMCO) have AUM-stickiness but floors are AUM-dependent not earnings-floor; secular passive/ETF pressure erodes pricing

**Net result: 0 new QUEUED; 2nd consecutive 0-new pass → SECTOR 15 EXHAUSTED.**
Best survivors: SAMG 5/12 PARK (Silvercrest UHNW RIA; moat real; fair-valued ~21x PE; AUM-dependent floor disqualifies); HNNA 4/12 PARK (Hennessy Advisors; weaker moat; thin AUM-dependent margins).

**REVIVE condition:** new geo lens required — Nordic/Scandinavian financial data niche (Oslo Bors/Nasdaq Stockholm micro-cap financial infrastructure) or ASX Australian securities infrastructure — before attempting another pass.

---

## Sector 10 (Value-added/sole-line distribution) — Pass 3 Coverage Notes (run #52, 2026-07-21) → **ACTIVE**

**Nordic specialist distributors + ASX niche geo lens:** ~17 names processed; 1 new QUEUED (ASX:XRF 9/12). Consecutive-0-new streak from 2nd pass BROKEN — Sector 10 remains **ACTIVE**.

**Names processed:**

**Cap Kills — 5 names (CAP_SOFT: $500M–$1.5B, limited asymmetry):**
- OEM-B.ST (OEM AB, Sweden) — Swedish industrial distributor; ~$1.1B USD cap; CAP_SOFT_KILL
- BIOG-B.ST (Biogaia, Sweden) — probiotic distributor/IP; ~$700M+ cap + >4 analysts; dual CAP_SOFT+COVERAGE_KILL
- MUSTI.HE (Musti Group, Finland) — Nordic pet products distributor; ~$760M USD cap; CAP_SOFT_KILL
- BERG-B.ST (Bergman & Beving, Sweden) — industrial specialist distributor; ~$735M USD cap + revenue ceiling; CAP_SOFT_KILL
- ASX:SNL (Supply Network Limited, Australia) — heavy truck parts distributor; ~$940M USD cap; CAP_SOFT_KILL

**Coverage Kill — 1 name:**
- ASX:NAN (Nanosonics, Australia) — medical device disinfection; 5-7 analysts; COVERAGE_KILL

**No-Moat Kills — 6 names:**
- ALLIGO-B.ST (Alligo AB, Sweden) — broadline workwear/industrial supplies distributor; 41% GM fails moat gate; NO_MOAT_KILL
- NORBT.OL (Norbit ASA, Norway) — hardware manufacturer not distributor; sector misclassification; NO_MOAT_KILL
- NZX:PGW (PGG Wrightson, NZ) — agricultural products distributor; 26% GM fails gate; NO_MOAT_KILL
- ASX:MXI (MaxiTRANS Industries, Australia) — trailer equipment distributor; 34% GM fails gate; NO_MOAT_KILL
- ASX:CYG (Coventry Group, Australia) — industrial distribution; GM uncertain; NO_MOAT_KILL
- VOLO.ST (Volati AB, Sweden) — industrial conglomerate; 30-35% GM fails specialty distributor gate; NO_MOAT_KILL

**Park — 1 name:**
- MMGR-B.ST (Momentum Group, Sweden) — technical industrial distribution; PARK 5/12 (quality borderline; margins thin; no hard-dated catalyst)

**Already Seen — 1 name:**
- ASX:DGL (DGL Group) — already killed in prior run; NOT duplicated

**Quality Bench Additions — 3 names (above buy-zone but durable moat; monitor for dip):**
- MEDI.OL (Medistim ASA, Norway) — patented TTFM cardiac surgery flow measurement; 80%+ global monopoly; 82% GM; above buy-zone (~$390-450M cap vs buy-zone ~$230-290M cap)
- SECARE.ST (Secare AB, Sweden) — ⚑non-EN conditional bench spot pending business/moat confirmation
- NZX:SKL (Skellerup Holdings, NZ) — diversified niche rubber/polymer OEM; quality real but ~NZD $720M cap extended zone

**1 new QUEUED:**
- **ASX:XRF (XRF Scientific Limited)** — 9/12; mining laboratory captive consumables (fusion discs, beads, platinum-ware for XRF/fire assay sample preparation); ~$207M USD cap; 48% GM; 1-2 analysts; English-language ASX filing; captive razor-blade model (lab equipment + consumable lock-in); §5 deep-dive deferred to run #53+

**Sector 10 status:** ACTIVE (3 passes complete; 1 new QUEUED this pass breaks consecutive-0-new streak). Next pass: Sector 10 4th pass with new geo lens (e.g. Southern Europe/DACH specialty distributors or Canadian TSX niche distributors).

---

## Deferred Queue Resolution + Sector 10 Pass 3 → ASX:XRF BENCH (run #53, 2026-07-21)

**ASX:XRF (XRF Scientific Limited)** — §5 deep-dive completed run #53. Outcome: **BENCH (WATCHLIST.md)**.
- Q4/F4/R1/C2 = 11/20. Asymmetry Gate FAIL 4/4.
- Moat: 10,000+ installed machines globally; platinum-group crucible consumable lock-in; process-certification switching cost (6-12 months re-validation); 50yr operating history. Q=4 is defensible.
- Financials confirmed: Revenue A$59.45M ✓; NPAT A$10.4M ✓; OCF A$10.1M ✓; net cash A$11.1M ✓ (ASX annual report). GM 48.43% ~ (aggregator).
- Price A$2.28 ~ = AT analyst consensus PT A$2.26-2.42 (1 analyst). No margin of safety.
- Buy-zone: A$1.40-1.65/sh (~A$200-235M cap). Promote to QUEUED_HOT on §7 REFLECT price check.
- memo: memos/XRF.AX-2026-07-21.md; financials: financials/XRF.AX.md.

---

## Sector 17 (Semiconductor & electronics supply chain) — Pass 3 Coverage Notes (run #53, 2026-07-21) — COMPLETE

**US micro-cap IC designers / semiconductor supply chain geo lens:** 32 names processed; 32 killed; **0 new QUEUED**.

**Structural finding:** The AI semiconductor supercycle 2025–2026 has pushed the vast majority of US-listed semiconductor supply chain companies above $1.5B. SIZE_KILL dominated (24 of 32). The $20–300M zone yields only ~6 genuine candidates (CVV, GSIT, INTT, MX, SVCO, RELL) after all gates — these require §3-§4 diligence in a future US semiconductor deep-dive pass.

**Complete kill table (32 names):**

| Ticker | Company | Cap (July 2026) | Kill Reason |
|--------|---------|----------------|-------------|
| CRDO | Credo Technology Group | ~$39.5B | SIZE_KILL |
| ALAB | Astera Labs | ~$10–40B | SIZE_KILL |
| MTSI | MACOM Technology | ~$19–29B | SIZE_KILL |
| VICR | Vicor Corporation | ~$12.9B | SIZE_KILL (+385%/1yr) |
| RMBS | Rambus Inc | ~$10B | SIZE_KILL |
| SMTC | Semtech Corporation | ~$11.64–14.59B | SIZE_KILL |
| MXL | MaxLinear Inc | ~$6.66–8.27B | SIZE_KILL |
| SIMO | Silicon Motion Technology | ~$3.54B | SIZE_KILL |
| PI | Impinj Inc | ~$4.81B | SIZE_KILL |
| VECO | Veeco Instruments | ~$4.2–4.86B | SIZE_KILL + M&A_KILL (being acquired by ACLS) |
| ACLS | Axcelis Technologies | ~$2.93–3.99B | SIZE_KILL |
| POWI | Power Integrations | ~$3.93–4.85B | SIZE_KILL |
| ACMR | ACM Research | ~$4.2–5.8B | SIZE_KILL + JURISDICTION concern (China-centric) |
| UCTT | Ultra Clean Holdings | ~$2.63–5.4B | SIZE_KILL |
| ICHR | Ichor Holdings | ~$3.2–3.9B | SIZE_KILL |
| AEHR | Aehr Test Systems | ~$2.2–2.76B | SIZE_KILL |
| NVTS | Navitas Semiconductor | ~$1.89–2.79B | SIZE_KILL |
| AXTI | AXT Inc | ~$2.0B | SIZE_KILL |
| ROG | Rogers Corporation | ~$2.4–2.9B | SIZE_KILL |
| KLIC | Kulicke & Soffa | ~$3.65–4.59B | SIZE_KILL |
| PLAB | Photronics | ~$2.65B | SIZE_KILL |
| COHU | Cohu Inc | ~$2.4–3.3B | SIZE_KILL |
| FORM | FormFactor | ~$3.5B+ | SIZE_KILL |
| PDFS | PDF Solutions | ~$2.14B | SIZE_KILL |
| BELFB | Bel Fuse Inc | ~$2.82B | SIZE_KILL |
| FEIM | Frequency Electronics | ~$642M | SECTOR_KILL (defense/space primary) |
| ULBI | Ultralife Corp | ~$109M | SECTOR_KILL (military primary) |
| PRKR | ParkerVision | ~$32M | SECTOR_KILL (patent assertion entity; no products) |
| PKE | Park Electrochemical | ~$423–588M | CAP_SOFT_KILL (extended zone) |
| LEDS | SemiLEDs | ~$12.8M | CAP_SOFT_KILL (below $20M minimum) |
| MRAM | Everspin Technologies | ~$344–700M | PRICE_KILL (+285%/1yr) |
| ASYS | Amtech Systems | ~$385M | PRICE_KILL (+430-572%/1yr) |

**Non-kills flagged for next US semiconductor pass (§3-§4 diligence required before QUEUED):**
- RELL (~$241-252M): Richardson Electronics — potential sole-source in plasma etch RF generator power tubes; SiC distribution JV; if verified, strong QUEUED candidate
- NVEC (~$444-474M): NVE Corporation — spintronic sensors + IsoLoop galvanic isolators; ~70% GM; proprietary IP; extended zone borderline
- SVCO (~$110-390M): Silvaco Group — TCAD process simulation EDA software; IPO 2024; high switching-cost tools for fabs/IDMs; cap range needs pinning
- GSIT (~$96-220M): GSI Technology — SRAM + Gemini APU (in-memory AI); 129 patents; but wide cap range and R&D-stage AI chip uncertain
- INTT (~$131M): inTEST Corporation — multi-segment semiconductor test/thermal/environmental; $53.9M backlog; Russell 2000 inclusion June 2026

**Sector 17 status:** ACTIVE (3 passes complete: pass 1 Korea/Taiwan, pass 2 European, pass 3 US micro-cap); next: 4th pass Japan secondary OEMs or US-listed non-killed names §3-§4 diligence. Pattern: zero new QUEUED from pass 3 (structural AI re-rating), 1 QUEUED (CML.L) from pass 2.

---

## Sector 17 (Semiconductor & electronics supply chain) — Shortlist §3-§4 Triage (run #54, 2026-07-21)

**5 non-kills from run #53 triaged this run (RELL, NVEC, SVCO, GSIT, INTT). Result: 0 new QUEUED, 0 new PARK-to-BENCH.**

| Ticker | Company | Triage result | Kill reason |
|--------|---------|--------------|-------------|
| RELL | Richardson Electronics | **NO_MOAT_KILL** | Blended GM 31.9% (7-quarter distribution growth streak; FY2025 revenue $241M; specialty high-power tubes, SiC wafers, KleerFax media); fails 45% GM gate — sole-source magnetron/plasma etch RF claim is valid but BLENDED margin is distribution economics |
| NVEC | NVE Corporation | **CAP_SOFT_KILL (PARK)** | ~$532M cap (~35x PE); 70% GM, 57% NI margin, net cash; spintronics IP (GMR/IsoLoop galvanic isolators) moat real but revenue FLAT ~$26M for years and annual dividend payout likely >100% of net income (drawing down cash reserves); no revenue recovery catalyst; for 2x need $1B+ cap (40x revenue) at flat $26M — no credible path. NOT bench material: revenue stagnant (not a compounder); payout draining reserves (not a sustainable cash-thrower). PARK not bench. |
| SVCO | Silvaco Group | **COVERAGE_KILL** | 5 analysts confirmed (IPO 2024, ~$390-450M cap); EDA/TCAD software; switching-cost moat is real but >4 analyst gate exceeded |
| GSIT | GSI Technology | **INTEGRITY_KILL** | Net loss $13.2M (worsening FY2025); defense 45.7% of Q4 revenue (SECTOR_KILL risk concurrent); Gemini APU in-memory AI chip development-stage; R&D-burning on AI chip with no commercial traction |
| INTT | inTEST Corporation | **PARK 6/12** | $131M revenue, GM 45.5% (barely at gate), NI margin 2.4% ($3.1M NI on ~$200M cap = 64x PE); multi-segment (semiconductor test, thermal, environmental) dilutes moat; Russell 2000 inclusion June 2026 drove price premium; no asymmetric entry; PARK not kill because 45.5% GM passes gate and multi-segment growing |

**Sector 17 status:** ACTIVE-SPARSE (3 passes + shortlist triage complete; 0 QUEUED from all US micro-cap work; AI supercycle re-rated essentially all US semi supply chain names above $1.5B; next pass = 4th pass Japan secondary OEM or Korean secondary KOSDAQ with fresh geo lens).

---

## Sector 10 (Value-added/sole-line distribution) — Pass 4 Coverage Notes (run #54, 2026-07-21)

**Canadian TSX + DACH specialty distributors + corporate action spin-off lens:** ~7 names processed; 0 new QUEUED. **1st consecutive 0-new pass since streak reset at pass 3 (XRF found).**

**Names processed and killed:**

| Ticker | Company | Kill reason |
|--------|---------|-------------|
| GUD.TO | Knight Therapeutics (TSX) | SECTOR_ADJACENT_KILL — specialty pharma, not distribution; C$414M TTM revenue (above ceiling); 8+ analyst coverage |
| ADIG | ADI Global Distribution (NYSE spin-off, debut Aug 4 2026) | **TRIPLE_KILL (SIZE_KILL + NO_MOAT_KILL + CAP_KILL)** — Revenue $4.8B FY2025 (10x+ our $400M ceiling); GM 22.3% (fails 45% gate — classic low-margin distribution economics); expected cap ~$1.5-2.2B (5x+ our $300M ceiling); $1B drawn debt ($400M senior notes + $600M term loan). Wholesale distributor of security/fire/AV products; 190+ branch locations North America + EMEA. Spin-off from Resideo Technologies. TRIPLE_KILL on all three primary gates. |
| OCTV | Octave Intelligence (NYSE, Hexagon spin-off May 2026) | SIZE_KILL + CAP_KILL — $1.6B+ revenue (4x ceiling); enterprise software (formerly Hexagon Asset Lifecycle Intelligence); cap too large |

**Canadian TSX distributors:** BioSyent (already on bench); all other TSX specialty distributors checked are either (a) too large, (b) pharma/sector-adjacent, or (c) private. Genuine specialty niche TSX distributors at C$20-300M cap are exhausted at this geo lens.

**DACH (Germany/Austria/Switzerland):** Quality German specialty distributors at small-cap (€20-300M) are overwhelmingly private (Würth, Rubix, RS Group successors, etc.). Public XTRA names in this size range with specialty distribution moats are not findable via web search — consistent with pass 2 finding (COVERAGE.md).

**Sector 10 status:** ACTIVE (4 passes; 1 consecutive 0-new pass after pass 3 XRF find; need 2 consecutive for EXHAUSTED; next 5th pass try East-European/Balkan specialty distribution or Japanese domestic secondary OTC sole-distributors).

---

## Why this matters
- **Measurable coverage** — we can state "we've reviewed X% of the worthwhile US universe," not "we searched a lot."
- **No wasted re-looks** — SEEN keyed by CIK/ticker; the ranked worklist is marched once.
- **Best-first** — even if we never hit 100%, we've covered the highest-quality names first.
- **Spend shifts to the top** — deterministic enumeration/pre-screen is nearly free; LLM tokens go only to names that already pass the hard numeric gates.

## Sector 6 (Vertical/Mission-Critical Software) — Pass 2 Coverage Notes (run #55, 2026-07-26)

**US + UK AIM geo lens + KB-internal analog thread-following:** ~54 names processed total; 3 new QUEUED (ELCO.L, TRB.L, APTD.L); 0 §5 deep-dives.

**All data tools proxy-blocked this run:** SEC EDGAR frames API (403 Forbidden), Yahoo Finance snapshot.py (no price), SEC FTS (403 Forbidden). Entire run conducted via §2B web-search subagent mode. All prices/financials tagged ~.

---

### KB-Internal Thread-Following (§2-QUALITY lens 4)

Mined FAA.VI and EUZ.DE memos for named analogs to identify pre-screened peers. FAA.VI memo used IDOX.L as a base-rate analog ("re-rated +3x"):

- **IDOX.L** → NOT_PUBLIC_KILL: AIM public sector/engineering compliance SaaS taken private via MBO May 2026 (~120p / ~£530M EV). Asymmetry was captured by private equity before our screen reached it. Confirmed IDOX was genuine (planning compliance, highways, grants management, EHS — deep UK council workflow lock-in); no re-entry path.
- **Lectra.PA** → CAP_SOFT_KILL + COVERAGE_KILL: Euronext Paris fashion/apparel PLM software; genuine vertical SaaS switching cost but cap ~€600-720M (2×+ ceiling) and 5+ analysts. Not re-enterable unless cap corrects below €250M.

Searching for IDOX analogs in the UK AIM vertical SaaS space surfaced the following batch of 6 names: ELCO.L, TRB.L, APTD.L (QUEUED), FNTL.L (NO_MOAT_KILL), SFT.L (NOT_PUBLIC_KILL).

---

### UK AIM Geo Lens — Kills

- **FNTL.L (Fonix Mobile)** → NO_MOAT_KILL: mobile carrier billing + messaging aggregator for utilities/broadcasters; GM ~55-60% but thin switching cost (utilities can and do switch to Bango/Eckoh/Boku); not mission-critical vertical SaaS.
- **SFT.L (Sopheon)** → NOT_PUBLIC_KILL: innovation portfolio management SaaS (Accolade stage-gate platform); AIM-listed until acquired and delisted 2023 (Sopheon B.V. buyout). No re-entry.

---

### UK AIM Geo Lens — QUEUED Survivors

**3 new QUEUED names from the UK AIM Sector 6 pass:**

**ELCO.L (Eleco plc, AIM)** — Score: 7/12
- Construction project management SaaS: Archidata, Spec, PlanSwift, Dds:D, StairDesigner, ElectroBIM
- ~35,000 users across architecture, engineering, construction
- GM: ~90% ~ (SaaS model; needs full financial baseline verification)
- Analysts: 3 ~ (Zeus Capital, Cenkos, WH Ireland — light AIM coverage for a construction SaaS)
- Cap: ~£55-80M ~
- Analyst consensus PT: ~185–218p ~ vs ~120p market price ~ (~55-80% below PT)
- Score breakdown: Moat=1 (real workflow switching cost in construction spec-writing; not regulatory monopoly), Quality=2 (SaaS GM profile, profitable ~, recurring), Coverage=2 (3 AIM analysts only), Valuation=1 (significant discount to consensus PT; not yet 2x confirmed), Catalyst=1 (general construction SaaS adoption; UK infrastructure spending), Floor=0 (conditional; §5 needed to verify FCF floor and churn)
- Next step: §4 financial baseline (GM%, NM%, FCF, churn, ARR growth) → §5 deep-dive

**TRB.L (Tribal Group plc, AIM)** — Score: 7/12
- Student Information System (SITS:Vision, ebs, edgesuite) for higher education — 135+ universities globally (UK, Australia, Middle East)
- Deep integration: enrollment, curriculum, compliance, OfS regulatory reporting, student records
- GM: ~49-50% ~ (not pure SaaS — includes professional services/implementation)
- Analysts: 3-5 ~ (Panmure Liberum, Shore Capital, others)
- Cap: ~£85-130M ~
- Score breakdown: Moat=1 (genuine SIS switching cost — 2+ yr data migration to switch; UK OfS regulatory integration; not textbook sole-source), Quality=1 (49% GM decent; profitable ~; but thin NM historically), Coverage=2 (3-5 AIM analysts; low for mission-critical HE infrastructure), Valuation=1, Catalyst=1 (international HE expansion + SaaS migration of legacy installs), Floor=1 (mission-critical system; low deinstall risk; conditional)
- Next step: §4 financial baseline → §5 deep-dive

**APTD.L (Aptitude Software Group plc)** — Score: 7/12
- Finance transformation SaaS: Aptitude RevStream (revenue accounting, IFRS 15), Aptitude Lease (lease accounting, IFRS 16), insurance finance (IFRS 17)
- Regulatory switching cost: IFRS compliance tools embedded in finance team workflows; switching requires full reaudit
- Target customers: telecoms, insurance, media, financial services
- GM: ~48% ~ (SaaS + professional services mix)
- Analysts: 2 ~ (Cenkos, others)
- Cap: ~£60-100M ~
- Score breakdown: Moat=1 (IFRS regulatory compliance = strong switching cost; but Oracle/SAP Finance also offer IFRS modules = competitive pressure), Quality=1 (profitable ~; 48% GM; SaaS growth stage), Coverage=2 (2 analysts), Valuation=1, Catalyst=1 (IFRS 17 insurance wave 2023-2026 driving new enterprise deals), Floor=1
- Next step: §4 financial baseline → §5 deep-dive

---

### US Geo Lens — Structural Finding

~25 US vertical SaaS names screened; ~23 killed by SIZE_KILL (caps $500M–$10B+); ~2 by COVERAGE_KILL or NO_MOAT; 0 new QUEUED. The $20–300M profitable vertical SaaS zone is nearly empty in US listings after the 2024-2026 software-sector recovery:
- **Size-kill dominated:** Most quality US vertical SaaS (field service, healthcare workflow, legal, education, construction) were either taken private 2021-2023 (PE roll-up wave) or re-rated past $300M on the recovery
- **No fresh US names below $300M cap with ≥45% GM, ≤4 analysts, profitable, and genuine vertical moat** found in this pass
- Notable SIZE_KILLs confirmed: Weave Communications (~$800M-1.2B, dental/optometry SaaS); others in the $500M-$3B range already reviewed in prior Sector 6 pass

**Sector 6 status:** ACTIVE (2 passes complete). Next pass: Nordic/DACH geo lens (Swedish/Danish/German vertical SaaS micro-cap, Nasdaq Stockholm / XTRA Frankfurt / Euronext). Prior runs found FAA.VI (Vienna ATC SaaS) as first WATCH-grade name — the geographic diversity of vertical SaaS moats suggests Nordic/DACH may hold undiscovered names in energy data management, regulatory compliance, or industrial SaaS. **3 QUEUED (ELCO.L, TRB.L, APTD.L) require §4+§5 before next sector pass.**

---

## Sector 8 (Building & Infrastructure Products) — Pass 2 Coverage Notes (run #55, 2026-07-26)

**EU geo lens (UK + Germany + France + Benelux building products):** ~12 EU/UK names screened; 0 new QUEUED; 1 BENCH addition (JHD.L → WATCHLIST.md); 1 PARK (LSC.L extended zone).

**Why EU building products is thin for this screen at £/€20–300M cap:**
- **Quality names are large-cap:** Kingspan (~€10B), Rockwool (~DKK 50B), Saint-Gobain (~€40B), Sika (~CHF 50B), Vicat, Sto dominate the ETICS/insulation/fire-safe materials market
- **UK AIM building products:** Most remaining AIM-listed building products companies at £20-300M have GM 25-40% (manufacturing economics, not IP-moated); commodity construction materials, low-specification switchable products, or service businesses with high overhead
- **Fire safety niche (LSC.L):** The regulated-maintenance model is attractive but the listed UK fire safety services market is dominated by larger groups (Marlowe plc, Hochiki, Nittan); London Security (LSC.L) at £415M cap is already extended zone
- **Spec-in flooring (JHD.L):** James Halstead (Polyflor) is the standout quality exception — 60-year compounder, spec-in architect model, 15.5% NM — but GM 44.5% is just below our 45% gate in a manufacturing context; revenue declining 2 consecutive years; added to Quality Bench

**Net result:** 0 new QUEUED from ~12 names; 1 consecutive 0-new pass for Sector 8 2nd pass.

**Kill summary:**

| Ticker | Company | Kill Reason |
|--------|---------|-------------|
| LSC.L | London Security plc | PARK: CAP_SOFT_KILL (£405-417M cap ~$520M USD = extended zone); NM 9.7% on 74% GM = enormous overhead; floor conditional. Revisit at ~£200-250M cap. |
| STO3.DE | Sto SE & Co. KGaA | SIZE_KILL: ETICS facade systems; ~€2-2.5B cap = 7-8× ceiling; genuine moat but wrong size |
| ALU.L | Alumasc Group plc | NO_MOAT_KILL: specialty building products (rainwater, drainage); GM ~35-40% fails 45% gate; commoditised |
| SEL.L | Stelrad Group plc | NO_MOAT_KILL: UK radiator manufacturer; GM ~25-30%; commodity product; multiple competitors |

**Quality Bench addition:** JHD.L (James Halstead plc) added to WATCHLIST.md Quality Bench (Q4/F3; buy-zone ~£200-250M cap ~1× trough revenue). GM 44.5% is just below the 45% gate but in manufacturing context this represents very high moat quality (not SaaS/services); spec-in architect model creates multi-year switching inertia; 60-year dividend growth track record; 15.5% NM. Revenue declining 2 consecutive years = headwind that cap may not yet fully reflect. Do not promote from bench until revenue stabilizes.

**Sector 8 status:** ACTIVE (2 passes complete). 1st consecutive 0-new-QUEUED pass for EU geo lens (pass 1 was Canada/AU). Next Sector 8 pass: US geo lens (specialty building products, US OTC/Nasdaq micro-cap — Trex, Simpson Manufacturing, Gibraltar already above $300M; look for sub-$300M specialty niche names) or Japan non-EN building materials (EDINET when access restored).

---

## §7 REFLECT — Run #57 (2026-07-27): Bench False-Negative Corrections (PHO.OL, CUV.AX)

**Trigger:** Run 57 = 57%3=0 → mandatory §7 REFLECT. Standing false-negative check: pre-v5.1 COVERAGE_KILLs re-examined for Q≥4 names wrongly killed on coverage count alone.

**Finding:** Two names killed in run #47 (2026-07-20) on COVERAGE_KILL are Q=4 regulatory monopolies and should be on the Quality Bench under v5.1 rules (coverage = ROUTER not KILLER for Q≥4).

| Ticker | Kill reason (pre-v5.1) | Q-score | v5.1 outcome | Buy-zone |
|--------|------------------------|---------|--------------|----------|
| PHO.OL | COVERAGE_KILL (5-7 analysts on Oslo Børs; run #47) | Q=4 (94% GM regulatory monopoly; sole FDA+EMA approved BLC agent; patent Dec 2036; 390+ US hospital systems) | BENCH (revived to WATCHLIST.md Quality Bench) | NOK ≤50-55/sh (~NOK 1.3-1.4B cap); current ~NOK 64.1 = ABOVE zone |
| CUV.AX | COVERAGE_KILL (7 ASX analysts; run #47) | Q=4 (sole approved drug for EPP; SCENESSE FDA 2019 / EMA 2014; no therapeutic alternative; rare disease regulatory monopoly) | BENCH (revived to WATCHLIST.md Quality Bench) | A$6-8/sh (~A$300-400M cap); current ~A$10.24 = ABOVE zone |

**Action taken:** Both added to WATCHLIST.md Quality Bench (run #57 §7 REFLECT). Neither triggers QUEUED_HOT today (both above buy-zone). Monitoring mode. CUV.AX §4 baseline not yet written — write on next run with filing access.

---

## Sector 7 (Specialty Food & Ag Ingredients) — Pass 2 Coverage Notes (run #57, 2026-07-27)

**Geo lens: European/UK AIM + US OTC/Nasdaq specialty ingredient names not captured in 1st pass (Japan/Korea/US micro-cap).**

**Pass result:** 10 names processed; ALL killed; 0 new QUEUED; 1st consecutive 0-new pass.

**Structural finding:** The Sector 7 2nd pass confirms the structural thinness identified in pass 1. The viable specialty ingredient / ag biologicals niche at $20-300M cap is structurally thin for four reasons:

1. **Pre-commercial dominates:** The most scientifically interesting names (Cibus, BIOX, BioHarvest, Evogene, Ginkgo) are pre-profitable development-stage companies with cash runway risks — they fail the anti-value-trap quality gate (earnings floor required)
2. **Distressed adjacents:** Several names (BIOX, NAII) show severe financial distress (90%+ stock declines, ongoing losses) rather than value mispricing — asymmetry gates fail badly
3. **Adjacent-sector pollution:** CDXS (pharma biocatalysis), AVD (crop chemicals) and DNA (platform services) appear in food/ag screens but are not specialty ingredient businesses
4. **Size/coverage kills:** MGPI ($536M revenue) and AVD ($515M revenue) are above ceiling; pre-v5.1 kills (MGPI coverage, Treatt coverage) confirmed again

**Individual kills summary:**

| Ticker | Company | Kill Type | Key Reason |
|--------|---------|-----------|------------|
| TTTRF/TET.L | Treatt plc | NO_MOAT_KILL + COVERAGE_KILL | GM ~26% fails gate; 8 analysts; natural extract supplier commodity-adjacent |
| CBUS | Cibus Inc | INTEGRITY_KILL | Pre-commercial; $3.6M revenue; cash runway Q1 2027 only |
| BIOX | Bioceres Crop Solutions | INTEGRITY_KILL | 90%+ stock decline; large GAAP losses; Argentine peso exposure |
| CDXS | Codexis | SECTOR_ADJACENT_KILL | Primarily pharma biocatalysis; pre-profitable |
| BHST | BioHarvest Sciences | CAP_TOO_SMALL_KILL | ~$40M cap at/below effective floor; pre-profitability |
| MGPI | MGP Ingredients | SIZE_KILL + NO_MOAT_KILL | $536M revenue above ceiling; ingredient GM very low |
| AVD | American Vanguard | SIZE_KILL + SECTOR_ADJACENT | $515M revenue above ceiling; crop chemicals not food ingredients |
| NAII | Natural Alternatives International | INTEGRITY_KILL | Net loss -$13.6M FY2025; ~$20M cap near floor |
| DNA | Ginkgo Bioworks | CAP_KILL + SECTOR_ADJACENT | ~$542M cap above ceiling; platform/services not specialty ingredient |
| EVGN | Evogene Ltd | CAP_TOO_SMALL_KILL | ~$5M cap far below floor; pre-commercial; already killed run #26 |

**Sector 7 status:** ACTIVE (not EXHAUSTED — only 1 consecutive 0-new pass; need 2 to declare EXHAUSTED). Structural assessment: the niche specialty ingredient / ag biologicals space has very few public companies in the $20-300M cap zone that are (a) profitable, (b) have a genuine moat beyond brand/scale, and (c) are below coverage radar. The sector may be structurally thin at any geo lens given: most quality ingredient companies are private (Amano Enzyme, Lallemand, Lesaffre, Kerry private divisions, Chr. Hansen private after Novozymes merger) or large-cap. **Do not declare EXHAUSTED after 2 consecutive 0-new passes if a fundamentally new geo lens has not been tried** — consider LATAM ag biologicals (Brazil: EMBRAPA licensees; Chile: specialty viticulture inputs) or Australian/NZ specialty food ingredients as a future 3rd pass geo lens if warranted.



---

## Sector 6 (Vertical/Mission-Critical Software) — Pass 3 Coverage Notes (run #58, 2026-07-27)

**Nordic/DACH geo lens:** Nasdaq Stockholm, Oslo Bors, XTRA Frankfurt, Euronext, Helsinki First North. ~28 names processed; **1 new QUEUED_HOT (NTECH.ST 10/12)**; ~27 killed; 1 consecutive new-find pass (breaks structural thin streak).

**All data tools proxy-blocked:** SEC EDGAR, Yahoo Finance, EDINET — entire run in §2B web-search mode; all prices/financials tagged ~.

---

### Key Find: NTECH.ST (Nordtech Group AB) — 10/12 QUEUED_HOT

**Why this was missed in prior Nordic sweeps:** Nordtech Group AB IPO'd on Nasdaq Stockholm on June 10, 2026 — only 47 days before this run. It was not yet public during the Sector 6 2nd pass (run #55 2026-07-26) and was dismissed as "Nordtech roll-up" in the §3 Nordic quick-triage of run #56. Run #58's dedicated Nordic/DACH Sector 6 pass did the IPO prospectus research that revealed the actual financials.

**What NTECH.ST is:** Nordic VMS serial acquirer — Constellation Software / Topicus analog, but on Nasdaq Stockholm at 47 days old. 23 acquisitions since founding ~2021. Verticals: dental clinic management (Opus Dental — dominant Scandinavia), healthcare HR/scheduling (Medhelp Care), public sector GIS/data (Adtollo), document management (Docunova).

**Key metrics (from IPO prospectus + Q2 2026 interim):**
- Revenue LTM March 2026: SEK 639M ✓
- H1 2026 revenue: SEK 383.9M (+50% YoY — acquisition-driven) ✓
- Adj. EBITA margin: 29% ✓
- Organic growth: 8–9% ✓
- Recurring revenue: 87% ✓
- Cash conversion: 104% ✓
- Net debt / Adj. EBITA: 0.4x ✓
- ROIC + organic: 22% ✓
- EV/EBITA: ~16.7x vs. VMS peers 25–30x

**Promise score: 10/12 (QUEUED_HOT).** Two analysts only (DNB Carnegie + Nordea). Fresh IPO = extreme coverage void. §5 OPUS adversarial red-team MANDATORY before grade confirmation. Key unknowns: gross margin (UNAVAILABLE), acquisition multiples paid per deal (UNAVAILABLE), unadjusted EBITA (what's in the "adj."?), and whether IPO price was above current price (post-IPO price discovery = warning signal). Financials baseline: financials/NTECH.ST.md.

---

### Structural Finding — Nordic/DACH Sector 6

**Why the space is thin at $20-300M cap:**

1. **Best names are private:** Visma (Norway), Unit4 (Netherlands), IFS (Sweden), Aareon (Germany), Cegid (France), Exact (Netherlands) — all confirmed NOT_PUBLIC_KILL. The private equity consolidation wave 2015–2023 absorbed most quality Scandinavian and German B2B SaaS names.

2. **Quality public names are over-capped:** Vitec Software (VITEC-B.ST, Sweden, ~SEK 30B = CAP_KILL), Tietoevry (TEM.HE, Finland, ~€4.5B SIZE_KILL), ATOSS Software (CAP_SOFT at ~€600M), WiseSolutions private. The Scandinavian VMS quality names that remain public are large-cap.

3. **The "thin Nordic SaaS" zone remains:** At $20-300M on Nordic exchanges, the space is populated by:
   - Recently-IPO'd rollups that need track record verification (NTECH.ST = exception; managed to clear despite newness)
   - Healthcare workflow companies with declining revenue or IFRS complexity
   - Services-heavy B2B software with 20-40% GM (not pure SaaS economics)
   - Pre-profitable development stage companies

**Notable kills:**
- IVU.DE: German transit VMS with real moat (81% GM) — but 6 analysts COVERAGE_KILL
- MLG.DE: Life insurance SaaS — NO_MOAT_KILL (20.5% GM)
- FAB.VI: Fabasoft AG = SEEN_KILL (= FAA.VI already WATCH-A)
- ZAL.OL: Zalaris HR SaaS — NO_MOAT_KILL (20-25% GM services-heavy)
- CARA.ST: Carasent eGP — INTEGRITY_KILL (losses)
- USU.DE: USU Software — COVERAGE_KILL + CAP_SOFT

**Sector 6 status:** ACTIVE (3 passes). 3rd pass: 1 new QUEUED_HOT (NTECH.ST). Consecutive 0-new streak from pass 1 (DACH mixed) broken by Nordic lens. Next pass if needed: UK AIM B2B SaaS re-screen (post-IDOX.L privatization), or Benelux enterprise SaaS (Exact-adjacent) or East-European tech exchanges (Warsaw GPW, Vienna, Prague).


---

## Sector 8 (Building & Infrastructure Products) — Pass 3 Coverage Notes (run #59, 2026-07-27) → **EXHAUSTED**

**US geo lens (Nasdaq/NYSE/OTC specialty building products):** ~35 names processed; **0 new QUEUED**; 0 bench additions; **2nd consecutive 0-new pass → Sector 8 EXHAUSTED**.

**All data tools proxy-blocked:** SEC EDGAR frames API (403), Yahoo Finance/snapshot.py (no price), SEC FTS (403). Entire run in §2B web-search mode; all caps/prices tagged ~.

---

### Structural Finding — Why US Specialty Building Products at $20-300M Cap is Exhausted

The US specialty building products sector at the $20-300M cap / ≥45% GM intersection is **structurally empty** for four compounding reasons:

1. **All quality moated names are large-cap:** The textbook US building products moats — SSD (Simpson Manufacturing, code-certified structural connectors), TREX (composite decking), AAON (semi-custom HVAC), PRM (Perimeter Solutions fire retardant) — are all $3-5B+ cap. These re-rated years ago and are now well-covered institutional positions.

2. **PE/M&A consolidation absorbed the micro-cap quality layer:** GCP Applied Technologies (specialty construction chemicals → Saint-Gobain 2022); Forterra (specialty concrete/steel pipe → Quikrete 2022); Continental Building Products (→ Saint-Gobain 2020); W.R. Grace (→ Standard Industries 2021, private). The micro-cap building products moat names that survived the 2015-2022 wave are now either private or have been absorbed. IDOX.L (UK equivalent) was taken private May 2026 by MBO.

3. **What remains at $20-300M cap fails the GM gate:** Commodity manufacturers (IIIN steel wire ~15-25% GM; NWPX pipe ~15-25%; BURCA boilers ~30-38%; TECOGEN CHP ~20-30%; EML hardware ~30-40%) universally fail the ≥45% GM threshold. Low GM = no pricing power moat.

4. **Service/installation businesses dominate the residual:** LMB (Limbach HVAC contractor), MG (Mistras inspection services), FIX (Comfort Systems contractor) are service businesses with contractor GM (~15-25%), not specialty products manufacturers.

**The notable exception encountered:** OFLX (Omega Flex) is already on the Quality Bench — it IS the $20-300M US specialty building products moat name. SMID (Smith-Midland) is also on bench. Both were found in earlier passes. Run #59 confirms no new additions exist in the US cap zone.

---

### Key Names Processed

**SIZE_KILL dominated (18 of ~35):** PRM, SSD, TREX, AAON, FIX, IBP, GMS, UFPI, APOG, NX, JELD, PATK, AZZ, AMWD, ROCK, PLPC, MG, CSWI

**NO_MOAT_KILL (7):** NWPX, BURCA, LMB, TECOGEN, UFAB, EML, IIIN

**SECTOR_ADJACENT (2):** NSSC (→ forwarded Sector 11 3rd pass as Q≈4 bench candidate), MG (Sector 5)

**NOT_PUBLIC (2):** FRTA (acquired Quikrete 2022), ACA (acquisition by CRH pending)

**PRICE_KILL (1):** PPIH (130%+ run + NO_MOAT concurrent)

**INTEGRITY_KILL (2):** SGBX, CITR

**SEEN_KILL (4):** CCF, CMT, SMID, OFLX

---

### Notable Near-Miss: NSSC (Napco Security Technologies)

The one genuinely high-quality name encountered was NSSC (Napco Security Technologies, Nasdaq, ~$900M-1.1B cap). Fire alarm systems + StarLink cellular monitoring subscription (SaaS-like recurring, dealer channel lock-in, NFPA 72 code-required). GM ~58-62%. Q≈4. But:
- **SECTOR_ADJACENT**: Security electronics, not building products → Sector 11
- **Extended zone** ($900M-1.1B) + 5-7 analysts likely → under v5.1 rules routes to Bench if Q≥4
- **Asymmetry Gate**: at $900M-1.1B with thick analyst coverage, likely priced to fair value

NSSC is forwarded to Sector 11 3rd pass worklist as a Q≈4 extended-zone bench candidate. Requires §3.5 financial baseline before formal bench designation.

---

**Sector 8 status: EXHAUSTED (3 passes complete: Canada/AU, EU, US; 2 consecutive 0-new-QUEUED passes after EU and US lens). REVIVE conditions: Japanese AIM/TSE building materials niche (EDINET access restored), or Australian ASX niche building products (different macro/regulatory context), or a specific corporate action (spin-off of specialty product division from large-cap building products conglomerate). Do not attempt a 4th US or European pass without a genuinely new angle.**

---

## Run #59 — Bench Re-Price (2026-07-27)

*All prices tagged ~ (single-source web search, Yahoo/aggregators proxy-blocked). No promotions triggered.*

| Ticker | Prior price | New price ~ | Buy-zone | Status |
|--------|------------|-------------|---------|--------|
| WINA | $385.44 | $385.44 ~ | ≤~20-22x PE | Unchanged; above zone |
| CODA | ~$10.00 | ~$10.00 ~ | $8-10 / ≤$107M cap | At buy-zone upper bound; cap ~$112.7M NOT triggered (need ≤$107M) |
| OFLX | ~$29.85 | ~$29.92 ~ | ~$190-220M cap | Stable; above zone |
| JOUT | ~$43.48 | ~$45.96 ~ | ~$38-40 | ⚠ REBOUNDED — further from buy-zone (was $43.48 approaching; now $45.96; approaching note REMOVED) |
| SMID | ~$30.22 | ~$30.28 ~ | ~$22-24 | Stable; above zone |
| ETON | ~$37.57 | ~$42.32 ~ | ~$22-26 | Rebounded above zone; further from trigger |
| XRF.AX | A$2.28 | A$2.12 ~ | A$1.40-1.65 | Declining slowly; still above zone (T-A$0.47 to upper bound A$1.65) |
| JHD.L | ~143p | ~128.44p ~ | ~£200-250M cap | ⚠ APPROACHING — was 143p → now 128.44p; Jun 22 low was ~124p; MONITOR CLOSELY (T-~4.4p from Jun 22 low; revenue stabilization required before promotion) |
| PHO.OL | NOK 64.10 | NOK 64.10 ~ | NOK ≤50-55 | Unchanged; above zone |
| CUV.AX | A$10.24 | A$10.20 ~ | A$6-8 | Stable; above zone |
| MEDI.OL | NOK 226 | NOK 226 ~ | ~$230-290M cap | Stable; above zone |
| EKF.L | 25.40p | 25.40p ~ | pullback/acceleration | Unchanged |
| CGS.L | 316.8p→260p | 260p ~ | ~200-230p | Confirmed 260p (prior 316.8p Jul 23 was a data error, reverted; T-30-60p from zone; not triggered) |

**No promotions to QUEUED_HOT triggered this run.**

**Notable: JHD.L at 128.44p is approaching its Jun 22 low of ~124p. The buy-zone (expressed as ~£200-250M cap) may be near. However, revenue must first stabilize (currently declining 2 consecutive years) before promotion to QUEUED_HOT is warranted. Monitor next run.**

---

## Sector 9 — Environmental / Waste / Water (2nd pass, US geo lens, Run #60, 2026-07-27)

**23 names processed. 21 kills. 1 PARK (PESI). 1 DEFERRED (CWCO). 0 new QUEUED. 2nd consecutive 0-new pass → Sector 9 US geo EXHAUSTED.**

### Size Kills (too large)
| Ticker | Company | Kill Reason |
|--------|---------|------------|
| ERII | Energy Recovery Inc. | **SIZE_KILL**: Water/industrial pressure-exchange technology; ~$2.4B cap (16× ceiling). High-quality moat (sole-source pressure exchanger) but entity too large by 10×. |
| NVRI | Enviri Group (prev Harsco) | **SIZE_KILL**: Industrial waste management / environmental services; ~$1.2B cap (4-8× ceiling). Revenue >$2B. |
| OPAL | OPAL Fuels | **SIZE_KILL**: RNG (renewable natural gas) from landfill/animal waste; ~$600-650M cap. Extended zone. Development-stage economics overlay. |

### Development-Stage / Integrity Kills
| Ticker | Company | Kill Reason |
|--------|---------|------------|
| SCWO | 374Water Inc. | **DEVELOPMENT_STAGE_KILL**: Hydrothermal oxidation (SCWO) technology for biosolids/organics; ~$30-45M cap; pre-revenue commercial stage; net losses; going-concern risk. Technology is novel but no durable commercial moat yet. |
| PCT | PureCycle Technologies | **DEVELOPMENT_STAGE_KILL**: Ultra-pure polypropylene recycling (UPR process); ~$250-400M cap; operations still ramping; cumulative losses >$200M; debt-heavy capital structure. No profitable floor. |
| AREC | American Resources Corp. | **DEVELOPMENT_STAGE_KILL + INTEGRITY_KILL**: Rare earth / carbon fiber recycling; development-stage; serial dilution; tiny revenue base; no established moat vs. primary producers. |
| CLIR | ClearSign Technologies | **DEVELOPMENT_STAGE_KILL**: Combustion optimization technology for industrial burners; ~$20-30M micro-cap; pre-revenue development-stage; no floor. |
| AERC | AER Advisors (AEI / env advisory) | **CAP_TOO_SMALL_KILL + DEVELOPMENT_STAGE**: Micro-cap; development-stage or very thin revenue base; no durable moat. |
| PYRGF | PyroGenesis Canada (OTC) | **DEVELOPMENT_STAGE_KILL**: Plasma torch systems for waste destruction + EAF/metalcasting; ~C$80-120M cap; net losses; multiple pivots; no dominant commercial revenue. |
| BCHT | Bluestar Israel Technology (env) | **DEVELOPMENT_STAGE_KILL + CAP_TOO_SMALL**: Micro-cap; development or pre-commercial stage environmental technology; no durable moat verified. |

### Moat-Absent / No-Moat Kills
| Ticker | Company | Kill Reason |
|--------|---------|------------|
| VIVK | Vivesto AB (env context mismatch) | **MOAT_ABSENT_KILL + SECTOR_ADJACENT**: Name appears environmental but primary business is oncology pharma (oxaliplatin formulation) — sector mismatch; wrong sector entirely. |
| QRHC | Quest Resource Holding | **MOAT_ABSENT_KILL**: ESG waste management + sustainability consulting; no proprietary technology or regulatory moat; broker/aggregator model; thin GM. |
| OBCI | Ocean Bio-Chem Inc. | **MOAT_ABSENT_KILL**: Marine/household cleaning and chemical products (Starbrite, Davis, etc.); consumer brand portfolio, not industrial environmental moat; competitive market; GM likely 40-50% but no regulatory lock-in or switching cost. Cap ~$50-80M in-zone but moat gate fails. |
| EVI | EVI Industries | **MOAT_ABSENT_KILL**: Commercial laundry equipment distributor; no proprietary moat (distributor model); thin margins; no pricing power beyond brand-rep. |
| GURE | Gulf Resources Inc. | **MOAT_ABSENT_KILL + INTEGRITY_CONCERN**: Chinese-listed bromine and chemical company on Nasdaq; JURISDICTION_CONCERN (China-domiciled VIE-style; majority China operations); regulatory moat unclear from English sources; bromine = commodity with cycle sensitivity. |
| TOMZ | (US env/water micro-cap) | **CAP_TOO_SMALL_KILL**: Micro-cap; cap below $20M floor or sub-threshold with no established moat. |

### Already-Seen (Prior Pass Kills)
| Ticker | Company | Kill Reason |
|--------|---------|------------|
| BLGO | BioLargo Inc. | **ALREADY_SEEN (Sector 9 1st pass run #28)**: AOS water treatment technology; micro-cap ~$30-50M; development-stage. Previously killed CAP_TOO_SMALL. |
| AQMS | Aqua Metals Inc. | **ALREADY_SEEN (Sector 9 1st pass run #28)**: Lead and lithium battery recycling; micro-cap ~$20-40M; development-stage. Previously killed CAP_TOO_SMALL. |
| LIQT | (env context) | **ALREADY_SEEN (prior sector run)**: Previously processed. |
| UCLE | (env context) | **ALREADY_SEEN (prior sector run)**: Previously processed. |

### §4 PARK
| Ticker | Company | Notes |
|--------|---------|-------|
| PESI | (US environmental services) | **§4 PARK — GM_THIN**: Passed initial §3 moat check (service contract moat / specialty hazardous waste handling) but gross margin confirmed ~28-35% in §4 baseline — fails ≥45% GM gate. Cannot add to bench. Would need structural shift to higher-margin services. |

### §4 Deferred (3rd Pass)
| Ticker | Company | Notes |
|--------|---------|-------|
| CWCO | Consolidated Water Co. (Cayman/Nasdaq) | **DEFERRED to Sector 9 3rd pass §4**: Caribbean and Cayman Islands water concession + desalination operations. Possible real moat (government-granted water concession; sole supplier in service areas; capital-intensive desalination barriers). Extended zone (~$200-280M cap). Requires §4 to confirm: concession expiry dates, revenue/GM from annual report, pricing mechanism under concession, renewal history. DO NOT promote to bench without §4 primary-filing verification. |

### Structural Finding — Sector 9 US Geo
The US environmental/water small-cap ($20-300M) universe is structurally poor for niche-moat hunting:
- **Development-stage clean-tech dominates** the micro-cap tier ($20-100M): PyroGenesis, 374Water, PureCycle, ClearSign, AREC are all burning cash with no profitable floor.
- **Scaled operators** with real moats (Energy Recovery ERII, Enviri NVRI, US Water Services) are all $500M-$2.5B+ — SIZE_KILL.
- **Mid-cap ($100-300M)** names are mostly distributors/services with thin GMs or commodity-adjacent.
- **Government/municipal water utilities** are either massive ($5B+: WTRG, AWK, SJW) or private.
- The one structural exception (CWCO, water concession moat) is extended-zone and needs §4 verification.

**Next pass recommendation: UK AIM environmental/water or ASX Australian water/environmental — different regulatory regime, smaller market = potential niche names not yet SEEN.**

**Sector 9 status: ACTIVE-THIN (US geo EXHAUSTED after 2 passes). Next: UK AIM/ASX 3rd pass.**

---

## Run #60 — §7 REFLECT Bench Re-Price (2026-07-27)

*All prices tagged ~ (single-source web search). 22 names repriced (20 prior + 2 new: IVU.DE + NSSC).*

| Ticker | Prior price | New price ~ | Buy-zone | Status |
|--------|------------|-------------|---------|--------|
| WINA | $385.44 | $385.44 ~ | ≤~20-22x PE | Unchanged; above zone |
| CODA | ~$9.84-10.00 | ~$9.84-10.00 ~ | $8-10 / ≤$107M cap | Approaching; cap ~$112.7M — NOT triggered |
| OFLX | ~$29.85 | ~$29.92 ~ | ~$190-220M cap | Stable; above zone |
| 4549.T | ~¥2,271-2,423 | ~¥3,010 ~ ⚑non-EN | ¥2,000-2,400 | ABOVE ZONE — recovered; POTENTIAL BUY-ZONE flag removed |
| 6823.T | ~¥3,585 | ~¥3,585 ~ ⚑non-EN | ~¥2,200-2,400 | Above zone |
| EKF.L | 25.40p | ~25.80p ~ | pullback/life-sci catalyst | Slightly higher; above zone |
| 6742.T | ~¥864 | ~¥864 ~ ⚑non-EN | ¥720 | Above zone |
| CGS.L | 260p | ~260p ~ | ~200-230p | T-30-60p; not triggered |
| ETON | ~$42.32 | ~$42.32 ~ | ~$22-26 | Above zone; further |
| SMID | ~$30.22 | ~$30.28 ~ | ~$22-24 | Stable; above zone |
| EPEN.ST | ~SEK 97-99 | ~SEK 97-99 ~ ⚑non-EN | SEK 115-130 | BELOW lower bound SEK 115 (stale Jul 17 data SEK 156.20 from bench agent — conflict; use Jul 21 confirmed price) |
| JOUT | ~$45.96 | ~$45.96 ~ | ~$38-40 | T-$5.96; above zone |
| RX.V | ~C$14.50 | ~C$14.50 ~ | ≤C$10-11 | Above zone |
| MEDI.OL | ~NOK 226 | ~NOK 226 ~ | ~$230-290M USD | Above zone |
| SECARE.ST | ~SEK 26.35 | ~SEK 22.05 ~ ⚑non-EN | TBD ⚑non-EN | Declining; quality/buy-zone TBD |
| NZX:SKL | ~NZD 6.13 | ~NZD 5.43 ~ | ~NZD 350-450M cap | Declining; still well above zone |
| XRF.AX | ~A$2.12 | ~A$2.12 ~ | A$1.40-1.65 | Drifting lower; T-A$0.47 |
| JHD.L | ~128.44p | ~128.44p ~ | ~£200-250M cap | ⚠ APPROACHING — bench agent confirmed Jul 22 low ~119p (below Jun 22 124p); recovered 128.44p |
| PHO.OL | ~NOK 64.1 | ~NOK 64.1 ~ | NOK ≤50-55 | Above zone |
| CUV.AX | ~A$10.24 | ~A$10.24 ~ | A$6-8 | Above zone |
| IVU.DE | NEW | ~€20 (~€346M cap) ~ | ≤~€200-250M cap | NEW BENCH — above zone |
| NSSC | NEW | ~$36.09 (~$1.44B cap) ~ | ~$22-26 | NEW BENCH — above zone (extended) |

**No promotions triggered. CODA most proximate to trigger ($112.7M cap vs $107M trigger). EPEN.ST below buy-zone lower bound but quality unverified (⚑non-EN; DO NOT promote). JHD.L Jul 22 low 119p confirmed by bench agent — revenue stabilization still required.**

---

## Sector 9 (Environmental/waste/water) — Pass 3 Coverage Notes (run #61, 2026-07-27)

**UK AIM + ASX environmental/water geo lens:** 15 names processed; 0 new QUEUED; Sector 9 EXHAUSTED globally.

**Instant kills (§3 triage):**
- SYM (Symphony Environmental, AIM, <£30M): CAP_TOO_SMALL_KILL — oxo-biodegradable additive masterbatches; near-profitability but sub-threshold cap
- MWG (Modern Water, AIM, micro-cap): CAP_TOO_SMALL_KILL + NOT_PROFITABLE — forward osmosis membranes + water monitoring; marginal revenue
- FORG/EQTEC (AIM, micro-cap): DEVELOPMENT_STAGE_KILL — proprietary gasification technology; pre-revenue technology licensing
- RNWH (Renew Holdings, LSE Main, ~£600M+): SIZE_KILL (>£500M cap) + Main Market not AIM — engineering services for regulated water/rail infrastructure; AMP8 framework contracts; genuine regulated moat but too large
- FLC (Fluence, ASX, ~A$96M): NOT_YET_PROFITABLE_KILL — modular water treatment technology; net losses in 2025; no floor
- PET.AX (Phoslock, ASX): NOT_PUBLIC_KILL — winding up/delisting from ASX; CSIRO-origin phosphate binder technology
- CNQ (Clean TeQ Water, ASX): DEVELOPMENT_STAGE_KILL — proprietary CIX/graphene water purification; pre-revenue/early commercial
- DEM (De.mem, ASX, small): NOT_YET_PROFITABLE_KILL — hollow fibre membrane water treatment; recurring revenue trend but not yet profitable
- CXL (Calix, ASX, ~A$112M): NOT_PROFITABLE_KILL — patent-protected flash calciner platform (water + CO2 capture); operating loss ~A$9M H1 FY26
- SDV (SciDev, ASX, ~A$21-67M): FLOOR_THIN_KILL — PFAS treatment chemistry; maiden net profit ~A$100K on A$50M H1 revenue; no floor
- EGL (The Environmental Group, ASX, ~A$107M): MOAT_SOFT_KILL — multi-sector environmental engineering + PFAS water tech; FY26 EBITDA guided -21%; specialist capability not sole-source IP
- WAT.AX (Waterco, ASX, mid-cap): MOAT_SOFT_KILL — pool/spa filtration equipment and chemical distribution; competitive market, dealer/distributor moat not durable

**§3.5 Financial baseline survivors:**
- PRV (Porvair, AIM, ~£300M): **NO_MOAT_KILL** — aerospace/nuclear certified filtration consumables; "60% of sales are consumable elements" narrative misleading; FY2025 blended GM = 35.4% (£68.7M GP / £193.98M revenue) — FAILS ≥45% GM gate. Note: £194M revenue, adj. OP £26.2M (13.5% margin), net cash £17.1M; aerospace/nuclear certifications are real moat but insufficient to compensate for GM gate failure.
- RIV (Rivco Australia, ASX, ~A$226M): **MOAT_SOFT_KILL** — sole ASX-listed water entitlement vehicle; 91.5 GL portfolio in Southern Murray-Darling Basin; GM 99.4% (A$51.8M GP / A$52.1M FY2025 revenue); 53% net margin; BUT the "moat" is the regulatory scarcity of the underlying asset class (government-allocated water entitlements), NOT a business competitive advantage — any capital can purchase water entitlements; revenue volatile (+116% H1 2025 YoY = water price-driven, not compounding business); investment manager model (Duxton Capital fees charged); more like a REIT than a moat business.
- WATR (Water Intelligence, AIM, ~£51M/~$65M USD): **MOAT_SOFT_KILL** — American Leak Detection franchise network (74 US franchises, 46 states) + proprietary acoustic/infrared detection hardware (Leakvue, Pulse); FY2025 revenue $90.4M (+9%); adj. EBITDA $16.5M (18.2% margin); PBT $6.4M (7.7% margin); net debt/EBITDA 1.17x; GM unconfirmed (likely 30-40% blended; franchise royalty high-margin + corporate store/device lower-margin); acoustic leak detection is not sole-source IP — alternatives exist in the market; franchise brands are softer than regulatory/process moats.

**Prior-pass kills added this run:**
- CWCO (Consolidated Water, US/Caribbean): NO_MOAT_KILL — FY2025 GM 37% ($48.4M GP / $132.1M revenue); fails ≥45% gate; additional integrity: Bahamas WSC $21M receivables 71% delinquent; Cayman concession "temporary" pending OfReg negotiations
- HYR.L (Hydrodec): NOT_PUBLIC_KILL — acquired Nov 2021 by Slicker Recycling; no longer listed
- AUG.L (Augean): NOT_PUBLIC_KILL — delisted from LSE
- RWI (Renewi): NOT_PUBLIC_KILL — acquired June 2025 by Macquarie Infrastructure; delisted

**Sector 9 structural finding (confirmed across 3 geo passes, 44+ names):**
Environmental/water/waste at $20-300M cap with ≥45% GM is globally structurally thin:
- Development-stage clean-tech dominates the micro-cap tier (pre-revenue, losses, no floor)
- Scaled operators with real moats are SIZE_KILL (Veolia, Xylem, Evoqua/Xylem, SUEZ, Severn Trent, United Utilities all >$1B)
- Mid-cap names ($100-300M) typically have MOAT_SOFT (engineering services, distributor models, brand moats) or NO_MOAT (GM <45%)
- Regulatory moat + high GM + profitable + $20-300M cap = extremely rare combination in this sector globally
- Government ownership/concession creates regulated revenue but government is also the counterparty risk (as in CWCO Bahamas receivables)

**Sector 9 status: EXHAUSTED globally (3 geo passes). Revive only with deep Japan/Korea/Taiwan lens (waste recycling precision chemistry or water analytical instruments — different sub-sectors than water treatment).**


---

## Sector 6 (Vertical/mission-critical software & data) — Pass 4 Coverage Notes (run #62, 2026-07-27)

**UK AIM B2B SaaS re-screen (post-IDOX privatization):** ~21 names processed (incl. 6 already-SEEN from prior passes); 12 new kills; 1 new QUEUED. Structural finding: UK AIM B2B SaaS at ≤£500M cap / ≥45% GM is structurally thin — quality names are private, SIZE_KILL'd, or already processed.

**Already-SEEN / prior pass kills (6):**
- IDOX.L: NOT_PUBLIC_KILL (taken private run #55 — Bowmark Capital buyout Dec 2024)
- SFT.L (Sopheon): NOT_PUBLIC_KILL (acquired Apryse run #55)
- FNTL.L (Fonix Mobile): NO_MOAT_KILL (carrier billing middleware; run #55)
- TRB.L (Tribal Group): COVERAGE_KILL (3-5 analysts; run #55/56)
- APTD.L (Aptitude Software): PARK Grade D (run #56 §5)
- ELCO.L (Elecosoft): PARK Grade D (run #55/56)

**New kills — Size kills (>£500M / ~$700M+):**
- KNOS.L (Kainos Group, ~£700M): SIZE_KILL — digital transformation and Workday implementation services; AIM-listed but market cap at ceiling; genuine digital services business but too large
- GBG.L (GB Group, ~£700M-1B): SIZE_KILL — identity verification and fraud detection SaaS; genuine recurring revenue moat; too large for our screen
- ALPH.L (Alpha Financial Markets, ~£1B+): SIZE_KILL — wealth/asset management consulting and tech services; too large

**New kills — Coverage kills:**
- TRCS.L (Tracsis, ~£170M): COVERAGE_KILL (19-20 analysts) + MOAT_SOFT — transport and rail data analytics SaaS; too many analysts; genuine data moat but not sufficiently concentrated

**New kills — No moat / GM gate:**
- BKS.L (Brickworks, UK — not the Australian BKS; AIM data/analytics company): NO_MOAT_KILL (GM 35.52% — fails ≥45% gate) + reclassified SECTOR_ADJACENT Sector 15 (financial data/benchmarking)

**New kills — Cap too small / pre-profitable:**
- TIDE.L (Tide Platform, AIM): CAP_TOO_SMALL_KILL — SME banking and fintech; £5.9M revenue; pre-profitable; no floor
- CKT.L (Checkit, AIM): CAP_TOO_SMALL_KILL — connected worker SaaS for frontline operations; ~$18.2M ARR; pre-profitable; no floor

**New kills — Not public / zombie:**
- PTRO.L (Petrofac, restructuring rump, AIM): NOT_PUBLIC_KILL — £498k market cap zombie; oilfield services restructuring vehicle; no investable equity

**New kills — Integrity / structural concern:**
- ESYS.L (Ebiquity, restructured as eSystems?): INTEGRITY_CONCERN — restructuring losses + operating losses; structural integrity concern; not investable

**New kills — Sector kill:**
- PEN.L (Pennant, AIM): SECTOR_KILL (defense training primary customer — ~50%+ revenue from MoD/defense training simulation systems)

**New parks:**
- ACSO.L (Accesso Technology, AIM): PARK — leisure/theme park ticketing and queue management SaaS; revenue declining (FY2024 ~$147M vs prior year higher); EBITDA thin; moat erosion vs in-house alternatives; no catalyst
- SPA.L (Spinnaker Acquisitions): PARK — low-conviction; GM ~55.5%; thin NM; no visible catalyst; monitor for change in fundamentals

**Single quality survivor:**
- **CER.L (Cerillion plc, AIM, ~£315.8M cap / ~$397M USD):** 9/12 QUEUED → Quality Bench conditional
  - Telecom BSS/OSS billing SaaS (Cerillion Skyline) for mid-market and challenger operators globally
  - FY2025: Revenue ~£45.4M~, GM ~81.5%~, NM ~37%~, NI ~£16.6M~ (all single-source)
  - H1 FY2026: Backlog £82.1M (record, +44% from £56.9M FY2025); orders doubled; largest contract in company history
  - 7 analysts all Strong Buy; consensus PT ~1,996p; current ~1,070p (~46% discount; below 52-wk low ~1,170p)
  - Score: 9/12 (Moat=1, Quality=2, Coverage=0 [7 analysts → v5.1 Bench route], Valuation=2, Catalyst=2, Floor=2)
  - §3.5 INCOMPLETE: net cash, FCF, dilution, capex require primary AIM filing verification
  - Buy-zone: ~850-900p / ~£250-265M cap (≥2x to ~£500-530M on backlog conversion + re-rating)
  - Bench conditional pending §3.5 — see financials/CER.L.md

**Sector 6 pass 4 structural conclusions:**
- UK AIM B2B SaaS at ≤£500M cap has been effectively exhausted: 4 passes, 21 unique names this pass, total 70+ names across all passes
- Quality survivors from all 4 passes: IDOX.L (private), APTD.L PARK, ELCO.L PARK, NTECH.ST PARK (Nordic), IVU.DE BENCH, CER.L BENCH conditional
- Structural dynamic confirmed: AIM SaaS names at quality tier either (a) get acquired/privatized (IDOX, Sopheon), (b) scale above £500M (Kainos, GB Group, Alpha Financial), or (c) get covered by >4 analysts (Tracsis)
- Only CER.L survived all gates this pass — moat confirmed real (mission-critical telecom billing), economics strong (81.5% GM, 37% NM), catalyst real (record backlog), valuation gap real (46% discount to consensus)
- Next action: Sector 5 Testing/Inspection/Certification 1st pass; revisit CER.L §5 when §3.5 complete

**Sector 6 status: ACTIVE (4 passes complete; 1 new survivor CER.L Bench conditional; next pass: Sector 5 1st pass or fresh geo lens).**
