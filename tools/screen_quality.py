#!/usr/bin/env python3
"""US quality screen that SEES FINANCIALS — ROE/ROIC, not gross-margin-gated (SEC XBRL, keyless).

The gross-margin screen (screen.py) is structurally blind to banks, insurers, exchanges,
and asset managers — they report no GrossProfit line. This ranks the FULL filer set by
return on equity + net margin, and flags QUIET COMPOUNDERS (revenue up >=4 of the last 5
years + profitable + not diluting). Deterministic, ~15 HTTP calls, zero LLM.

  python3 tools/screen_quality.py --min-roe 15 --min-nm 8
"""
import sys, json, urllib.request, argparse, os

UA = {"User-Agent": "niche-moat-kb research@example.com"}
C = "/tmp/fq_cache"; os.makedirs(C, exist_ok=True)

def frame(tag, period, unit="USD", tax="us-gaap"):
    fn = f"{C}/{tax}_{tag}_{unit}_{period}.json"
    if os.path.exists(fn):
        try: return {int(d["cik"]): d for d in json.load(open(fn)).get("data", [])}
        except Exception: pass
    url = f"https://data.sec.gov/api/xbrl/frames/{tax}/{tag}/{unit}/{period}.json"
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                raw = json.load(r)
            json.dump(raw, open(fn, "w")); return {int(d["cik"]): d for d in raw.get("data", [])}
        except Exception: pass
    sys.stderr.write(f"  frame fail {tag} {period}\n"); return {}

def rev_year(y):
    out = {}
    for t in ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"]:
        for c, d in frame(t, f"CY{y}").items(): out.setdefault(c, d["val"])
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-roe", type=float, default=15.0, help="%")
    ap.add_argument("--min-nm", type=float, default=8.0, help="net margin %")
    ap.add_argument("--min-rev", type=float, default=25.0, help="$M")
    ap.add_argument("--max-rev", type=float, default=20000.0, help="$M")
    ap.add_argument("--top", type=int, default=60)
    a = ap.parse_args()

    revs = {y: rev_year(y) for y in range(2020, 2026)}
    ni = frame("NetIncomeLoss", "CY2024"); ni.update({k: v for k, v in frame("NetIncomeLoss", "CY2025").items()})
    eq = {}
    for p in ["CY2025Q4I", "CY2024Q4I"]:
        for c, d in frame("StockholdersEquity", p).items(): eq.setdefault(c, d)
    names = {}
    for y in (2024, 2025):
        for t in ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"]:
            for c, d in frame(t, f"CY{y}").items(): names.setdefault(c, d.get("entityName"))

    rows = []
    for cik, r24 in {**revs[2024], **revs[2025]}.items():
        # latest revenue 2025 else 2024
        R = revs[2025].get(cik) or revs[2024].get(cik)
        if not R or not (a.min_rev*1e6 <= R <= a.max_rev*1e6): continue
        n = ni.get(cik); e = eq.get(cik)
        if not n or n["val"] <= 0: continue
        if not e or e["val"] <= 0: continue
        roe = n["val"] / e["val"] * 100
        nm = n["val"] / R * 100
        # sanity caps: nm>60% or roe>60% almost always = revenue-tag undercount (esp. financials) or a
        # one-off/leverage artifact, not a clean compounder — drop (keeps the tool a usable lead-gen).
        if roe < a.min_roe or roe > 60 or nm < a.min_nm or nm > 60: continue
        # quiet-compounder: revenue up in >=4 of last 5 transitions
        seq = [revs[y].get(cik) for y in range(2020, 2026)]
        ups = sum(1 for i in range(1, 6) if seq[i] and seq[i-1] and seq[i] > seq[i-1])
        have = sum(1 for i in range(1, 6) if seq[i] and seq[i-1])
        compounder = have >= 4 and ups >= 4
        cagr = None
        if seq[0] and seq[-1] and seq[0] > 0:
            cagr = ((seq[-1]/seq[0])**(1/5)-1)*100
        rows.append(dict(cik=cik, name=names.get(cik, str(cik)), rev=R/1e6, roe=roe, nm=nm,
                         cagr=cagr, comp=compounder,
                         score=roe*0.5 + nm*0.3 + (min(cagr, 30)*0.2 if cagr else 0) + (10 if compounder else 0)))
    rows.sort(key=lambda x: x["score"], reverse=True)
    print(f"# US quality screen (ROE-based — INCLUDES financials) — ROE>={a.min_roe:.0f}% netM>={a.min_nm:.0f}% profitable")
    print(f"# {len(rows)} names; ★ = quiet compounder (rev up >=4/5yr)\n")
    print(f"{'#':<4}{'ROE%':<6}{'netM%':<7}{'5yCAGR':<8}{'rev$M':<9}{'★':<3}company")
    for i, x in enumerate(rows[:a.top], 1):
        cg = f"{x['cagr']:.0f}" if x['cagr'] is not None else "-"
        print(f"{i:<4}{x['roe']:<6.0f}{x['nm']:<7.0f}{cg:<8}{x['rev']:<9.0f}{'★' if x['comp'] else ' ':<3}{x['name']}")
    print("\n```json")
    print(json.dumps({"source": "roe-quality", "worklist": [{k: x.get(k) for k in ('cik','name','roe','nm','cagr','comp','rev')} for x in rows[:a.top]]}))
    print("```")

if __name__ == "__main__":
    main()
