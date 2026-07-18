#!/usr/bin/env python3
"""Ironclad live snapshot: current price (Yahoo) + SEC-reported fundamentals →
market cap and valuation COMPUTED by us, never trusted from an aggregator.

  python3 tools/snapshot.py GENC

- Price: Yahoo chart endpoint (live, no auth; works for US + foreign suffixes).
- Fundamentals (US filers): SEC XBRL companyfacts — most-recent revenue, gross
  profit (or revenue−COGS), shares outstanding, net income, with tag fallbacks
  and quarter-duration filtering for a clean TTM.
- market cap = live price × SEC shares · P/S, GM, P/E computed here.
- Foreign filer (no CIK): live price only; fundamentals must come from the IR
  filing (cap confidence per METHOD.md). Prints what it has + a JSON block that
  can be piped into fin_check.py.

Zero external deps (urllib). Fails soft: any piece it can't get is marked null.
"""
import sys, json, urllib.request
from datetime import date, datetime as _dt

UA = "niche-moat-kb research (contact: research@example.com)"

def _get(url, headers=None, timeout=12):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def price(ticker):
    try:
        j = json.loads(_get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"))
        m = j["chart"]["result"][0]["meta"]
        return {"price": m.get("regularMarketPrice"), "currency": m.get("currency"),
                "exchange": m.get("fullExchangeName"), "asof_ts": m.get("regularMarketTime")}
    except Exception as e:
        return {"price": None, "error": f"price fetch failed: {e}"}

def cik_for(ticker):
    try:
        d = json.loads(_get("https://www.sec.gov/files/company_tickers.json", {"User-Agent": UA}))
        for v in d.values():
            if v["ticker"].upper() == ticker.upper():
                return str(v["cik_str"]).zfill(10)
    except Exception:
        pass
    return None

REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
       "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"]
GP  = ["GrossProfit"]
COGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold", "CostOfServices"]
NI  = ["NetIncomeLoss"]
DEI_SH = ["EntityCommonStockSharesOutstanding"]

def _dur(e):
    if "start" not in e or "end" not in e: return None
    try:
        y1,m1,d1 = map(int, e["start"].split("-")); y2,m2,d2 = map(int, e["end"].split("-"))
        return (date(y2,m2,d2) - date(y1,m1,d1)).days
    except Exception:
        return None

def _units(facts, tax, tag):
    try:
        u = facts["facts"][tax][tag]["units"]
        return u.get("USD") or u.get("shares") or next(iter(u.values()))
    except Exception:
        return []

def _collect(facts, tags, tax="us-gaap"):
    out = []
    for t in tags:
        out += _units(facts, tax, t)
    return out

def _latest_annual(entries):
    ann = [e for e in entries if (_dur(e) or 0) >= 340 and (_dur(e) or 0) <= 380]
    ann.sort(key=lambda e: e["end"])
    return ann[-1] if ann else None

def _ttm(entries):
    """Sum the last 4 distinct ~quarterly (80-100d) periods; else latest annual."""
    q = [e for e in entries if 80 <= (_dur(e) or 0) <= 100]
    # dedupe by (start,end), newest first
    seen, uniq = set(), []
    for e in sorted(q, key=lambda e: e["end"], reverse=True):
        k = (e["start"], e["end"])
        if k in seen: continue
        seen.add(k); uniq.append(e)
    if len(uniq) >= 4:
        last4 = uniq[:4]
        return {"val": sum(e["val"] for e in last4), "period": f"TTM to {last4[0]['end']}", "kind": "TTM(4Q)"}
    a = _latest_annual(entries)
    if a: return {"val": a["val"], "period": f"FY to {a['end']}", "kind": "FY"}
    return None

def fundamentals(cik):
    try:
        facts = json.loads(_get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", {"User-Agent": UA}))
    except Exception as e:
        return {"error": f"SEC facts failed: {e}"}
    rev = _ttm(_collect(facts, REV))
    gp_entries = _collect(facts, GP)
    cogs_entries = _collect(facts, COGS)
    gp = _ttm(gp_entries) if gp_entries else None
    if gp is None and rev and cogs_entries:
        c = _ttm(cogs_entries)
        if c and rev["kind"] == c["kind"]:
            gp = {"val": rev["val"] - c["val"], "period": rev["period"], "kind": rev["kind"] + " (rev−COGS)"}
    ni = _ttm(_collect(facts, NI))
    sh = _shares(facts)
    return {"revenue": rev, "gross_profit": gp, "net_income": ni, "shares": sh,
            "entity": facts.get("entityName")}

def _latest(entries):
    e = [x for x in entries if x.get("end")]
    return sorted(e, key=lambda x: x["end"])[-1] if e else None

def _shares(facts):
    """Pick the freshest reliable share count. Cover-page dei is best WHEN fresh,
    but dual-class firms hide it (dimensioned) and old tags go stale — so
    weighted-average diluted (always current, captures both classes + dilution)
    is the robust fallback. Flag staleness so a wrong market cap can't slip out."""
    cands = []
    dei = _latest(_units(facts, "dei", "EntityCommonStockSharesOutstanding"))
    wad = _latest(_units(facts, "us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"))
    wab = _latest(_units(facts, "us-gaap", "WeightedAverageNumberOfSharesOutstandingBasic"))
    bs  = _latest(_units(facts, "us-gaap", "CommonStockSharesOutstanding"))
    if dei: cands.append(("dei cover-page", dei))
    if wad: cands.append(("wtd-avg diluted", wad))
    elif wab: cands.append(("wtd-avg basic", wab))
    if bs: cands.append(("balance-sheet", bs))
    if not cands: return None
    src, e = sorted(cands, key=lambda c: c[1]["end"], reverse=True)[0]  # freshest wins
    try:
        age = (date.today() - _dt.strptime(e["end"], "%Y-%m-%d").date()).days
    except Exception:
        age = None
    return {"val": e["val"], "asof": e["end"], "source": src,
            "stale": (age is not None and age > 460), "age_days": age}

def main():
    if len(sys.argv) < 2:
        print("usage: snapshot.py TICKER"); sys.exit(2)
    t = sys.argv[1]
    p = price(t)
    print(f"# {t} — live snapshot")
    print(f"price: {p.get('price')} {p.get('currency','')}  ({p.get('exchange','?')})  [Yahoo, live]")
    cik = cik_for(t)
    out = {"ticker": t, "price": p.get("price"), "currency": p.get("currency")}
    if not cik:
        print("SEC: no CIK (foreign/OTC filer) — fundamentals must come from the IR filing; cap confidence C≤2 (METHOD.md).")
        print("\n```json\n" + json.dumps(out) + "\n```")
        return
    f = fundamentals(cik)
    if "error" in f:
        print("SEC:", f["error"]); print("\n```json\n" + json.dumps(out) + "\n```"); return
    rev, gp, ni, sh = f.get("revenue"), f.get("gross_profit"), f.get("net_income"), f.get("shares")
    print(f"entity: {f.get('entity')}  [SEC EDGAR XBRL, primary filing]")
    if rev: print(f"revenue: {rev['val']:,} USD  ({rev['period']}, {rev['kind']})")
    if gp and rev and rev['val']:
        gm = gp['val']/rev['val']*100; print(f"gross profit: {gp['val']:,}  → gross margin {gm:.1f}%  ({gp['kind']})")
    if ni: print(f"net income: {ni['val']:,} USD  ({ni['period']})")
    if sh:
        warn = "  ⚠STALE — market cap unreliable, verify share count in latest filing" if sh.get("stale") else ""
        print(f"shares out: {sh['val']:,}  ({sh['source']}, as of {sh['asof']}){warn}")
    # computed valuation
    mktcap = pe = ps = gm = None
    if p.get("price") and sh and not sh.get("stale"):
        mktcap = p["price"] * sh["val"]
        print(f"\nCOMPUTED (live price × SEC shares — not trusted from an aggregator):")
        print(f"  market cap: {mktcap:,.0f} {p.get('currency')}")
        if rev and rev['val']:
            ps = mktcap/rev['val']; print(f"  P/S: {ps:.2f}  (mktcap ÷ {rev['kind']} revenue)")
        if ni and ni['val'] and ni['val'] > 0:
            pe = mktcap/ni['val']; print(f"  P/E: {pe:.1f}")
        if gp and rev and rev['val']:
            gm = gp['val']/rev['val']*100
    out.update({"revenue": rev and rev['val'], "gross_margin": gm and round(gm,1),
                "net_income": ni and ni['val'], "shares": sh and sh['val'],
                "market_cap": mktcap and round(mktcap), "ps": ps and round(ps,2), "pe": pe and round(pe,1),
                "provenance": {"revenue": "filing", "shares": "filing", "cash": "none", "total_debt": "none"}})
    print("\n```json  # pipe into fin_check.py (add cash/total_debt from the filing)\n" + json.dumps(out) + "\n```")

if __name__ == "__main__":
    main()
