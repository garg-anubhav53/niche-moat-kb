#!/usr/bin/env python3
"""Moat-language retrieval — SEC EDGAR full-text search (efts.sec.gov, keyless, cloud-reachable).

Instead of hoping web-search round-ups surface the same names, this finds companies
whose OWN 10-K filings assert a moat, in their own words. Primary-source grounded,
no LLM, no fabrication risk: every hit is a real filing phrase you can read.

  python3 tools/fts.py                       # default high-signal moat phrases, last ~2yr
  python3 tools/fts.py --since 2024-01-01 --q "sole source" "only qualified supplier"

Ranks companies by how many DISTINCT moat-phrases their filings match (a 10-K that
says several is a stronger signal). Output → a ranked worklist (CIK+name) for §3 triage.
Deterministic. SEC allows ~10 req/s; we stay well under.
"""
import sys, json, urllib.request, urllib.parse, argparse

UA = {"User-Agent": "niche-moat-kb research (research@example.com)"}
DEFAULT_PHRASES = [
    "sole supplier", "sole source", "only manufacturer", "only FDA-cleared",
    "only FDA-approved", "exclusive supplier", "sole qualified supplier",
    "de facto standard", "only commercially available", "sole provider",
]

def search(phrase, form="10-K", since=None, pages=8):
    """Yield (cik, name, date) for filings matching an EXACT phrase."""
    out = []
    for pg in range(pages):
        q = urllib.parse.urlencode({"q": f'"{phrase}"', "forms": form, "from": pg*10})
        url = f"https://efts.sec.gov/LATEST/search-index?{q}"
        if since:
            url += f"&dateRange=custom&startdt={since}&enddt=2099-12-31"
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                hits = json.load(r).get("hits", {}).get("hits", [])
        except Exception as e:
            sys.stderr.write(f"  '{phrase}' pg{pg}: {e}\n"); break
        if not hits: break
        for h in hits:
            src = h.get("_source", {})
            names = src.get("display_names") or []
            date = src.get("file_date", "")
            for nm in names:
                cik = None
                if "CIK" in nm:
                    cik = nm.split("CIK")[-1].strip(" )").lstrip("0") or "0"
                out.append((cik, nm.split("(CIK")[0].strip(), date))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", nargs="*", default=DEFAULT_PHRASES, help="exact moat phrases")
    ap.add_argument("--since", default=None, help="YYYY-MM-DD filing-date floor (recency)")
    ap.add_argument("--form", default="10-K")
    ap.add_argument("--pages", type=int, default=8, help="pages (x10 hits) per phrase")
    ap.add_argument("--top", type=int, default=50)
    a = ap.parse_args()

    comp = {}  # cik -> {name, phrases:set, latest date}
    for ph in a.q:
        for cik, name, date in search(ph, a.form, a.since, a.pages):
            if not cik: continue
            e = comp.setdefault(cik, {"name": name, "phrases": set(), "date": date})
            e["phrases"].add(ph)
            if date > e["date"]: e["date"] = date
            if len(name) > len(e["name"]): e["name"] = name

    rows = sorted(comp.items(), key=lambda kv: (len(kv[1]["phrases"]), kv[1]["date"]), reverse=True)
    print(f"# SEC full-text moat-language retrieval — {a.form}, phrases: {', '.join(a.q)}")
    print(f"# {len(rows)} companies asserting >=1 moat phrase in their own filings"
          + (f" (since {a.since})" if a.since else "") + "\n")
    print(f"{'#':<4}{'CIK':<12}{'#phr':<6}{'latest':<12}{'phrases matched':<40}company")
    for i, (cik, e) in enumerate(rows[:a.top], 1):
        ph = ", ".join(sorted(e["phrases"]))[:38]
        print(f"{i:<4}{cik:<12}{len(e['phrases']):<6}{e['date']:<12}{ph:<40}{e['name']}")
    print("\n```json")
    print(json.dumps({"source": "sec-fts", "form": a.form, "since": a.since,
                      "worklist": [{"cik": c, "name": e["name"], "n_phrases": len(e["phrases"]),
                                    "phrases": sorted(e["phrases"]), "latest": e["date"]}
                                   for c, e in rows[:a.top]]}, ensure_ascii=False))
    print("```")

if __name__ == "__main__":
    main()
