#!/usr/bin/env python3
"""Insider-buying cluster retrieval — SEC Form 4 open-market purchases (EDGAR, keyless).

Multiple insiders buying on the open market is one of the strongest small-cap signals.
This scans recent daily indexes for Form 4s, fetches each, keeps only OPEN-MARKET
PURCHASES (transactionCode P, acquired), and aggregates by issuer — flagging companies
with 2+ distinct insider buyers. Deterministic. Bounded fetch (threads).

  python3 tools/insiders.py --days 3 --max 200 --min-buyers 2
"""
import sys, json, urllib.request, argparse, re
from datetime import date, timedelta
from concurrent.futures import ThreadPoolExecutor

UA = {"User-Agent": "niche-moat-kb research@example.com"}

def get(url, timeout=30):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def form4_paths(d):
    q = (d.month - 1)//3 + 1
    url = f"https://www.sec.gov/Archives/edgar/daily-index/{d.year}/QTR{q}/form.{d:%Y%m%d}.idx"
    try: txt = get(url)
    except Exception: return []
    out = []
    for line in txt.splitlines():
        if line.startswith("4 ") or line[:2] == "4 ":
            parts = [p for p in line.split("  ") if p.strip()]
            path = line.split()[-1]
            if path.endswith(".txt"): out.append("https://www.sec.gov/Archives/" + path)
    return out

def parse(url):
    try: t = get(url)
    except Exception: return None
    iss = re.search(r"<issuerName>(.*?)</issuerName>", t)
    tk = re.search(r"<issuerTradingSymbol>(.*?)</issuerTradingSymbol>", t)
    owner = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", t)
    # any non-derivative open-market purchase: code P + acquired A
    codes = re.findall(r"<transactionCode>(.*?)</transactionCode>", t)
    ad = re.findall(r"<transactionAcquiredDisposedCode>\s*<value>(.*?)</value>", t)
    buy = ("P" in codes) and ("A" in ad)
    if not iss or not buy: return None
    return (iss.group(1).strip(), tk.group(1).strip() if tk else "", owner.group(1).strip() if owner else "?")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3)
    ap.add_argument("--max", type=int, default=200, help="cap Form 4s fetched")
    ap.add_argument("--min-buyers", type=int, default=2)
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()

    paths = []
    d = date.today()
    for i in range(a.days + 3):
        if len(paths) >= a.max: break
        paths += form4_paths(d - timedelta(days=i))
    paths = paths[:a.max]
    sys.stderr.write(f"scanning {len(paths)} Form 4 filings...\n")
    with ThreadPoolExecutor(max_workers=12) as ex:
        res = [r for r in ex.map(parse, paths) if r]

    agg = {}
    for iss, tk, owner in res:
        e = agg.setdefault(iss, {"tk": tk, "buyers": set(), "n": 0})
        e["buyers"].add(owner); e["n"] += 1
        if tk: e["tk"] = tk
    rows = [(k, v) for k, v in agg.items() if len(v["buyers"]) >= a.min_buyers]
    rows.sort(key=lambda kv: len(kv[1]["buyers"]), reverse=True)

    print(f"# Insider-buying clusters — Form 4 open-market PURCHASES, last ~{a.days}d ({len(paths)} filings scanned)")
    print(f"# {len(rows)} issuers with >= {a.min_buyers} distinct insider buyers\n")
    print(f"{'#':<4}{'buyers':<8}{'buys':<6}{'ticker':<9}issuer")
    for i, (iss, v) in enumerate(rows[:a.top], 1):
        print(f"{i:<4}{len(v['buyers']):<8}{v['n']:<6}{v['tk']:<9}{iss}")
    print("\n```json")
    print(json.dumps({"source": "form4-clusters", "worklist": [
        {"issuer": k, "ticker": v["tk"], "buyers": len(v["buyers"]), "buys": v["n"]} for k, v in rows[:a.top]]}))
    print("```")

if __name__ == "__main__":
    main()
