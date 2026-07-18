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
