# Setup: Niche Moat KB Hourly Routine

## Step 1: GitHub Repository

1. Create a new GitHub repo: `niche-moat-kb` (public, free file hosting)
2. Clone this local directory to that repo:
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/niche-moat-kb.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Claude Routine Configuration

1. Log into claude.ai/code/routines (Anthropic Claude Code interface)
2. Click **Create New Routine**
3. Configure as follows:

| Field | Value |
|-------|-------|
| **Name** | `niche-moat-hourly` |
| **Description** | Hourly scout for cross-industry niche-moat companies, 2x+ asymmetric upside |
| **Model** | Claude Sonnet 4.6 |
| **Cadence** | Every 1 hour (cron: `0 * * * *`) |
| **Environment** | Create new; name: `niche-moat-prod` |
| **GH_PAT Scope** | Repo write access (for git push from routine) |

---

## Step 3: Environment Variables

In the Claude Routine environment configuration, set:

```
GH_PAT=<your GitHub Personal Access Token with repo write scope>
KB_REPO_URL=https://github.com/YOUR-USERNAME/niche-moat-kb.git
KB_LOCAL_PATH=/tmp/niche-moat-kb
```

---

## Step 4: Routine Script / Prompt

Copy the entire text from `ROUTINE-PROMPT.md` into the routine's **Prompt** field.

Append this auto-git-push suffix:

```
---

## Auto-Commit & Push (add to end of routine)

After all outputs, commit and push to GitHub:

1. Stage all KB files:
   git add DIGEST.md UNIVERSE.md KILL-LIST.md INDEX.md

2. Commit with timestamp:
   git -c user.name=niche-moat-bot -c user.email=kb-routine@local commit \
     -m "scout $(date +%Y-%m-%d\ %H:%M): [summary of candidates found/killed]"

3. Push to origin/main:
   git push origin main

If push fails (network, auth), the routine will report the error in the output file but continue to next run.
```

---

## Step 5: First Test Run

1. Click **Run Now** on the routine (don't wait for 1-hour cadence)
2. Check the output in the routine's execution log
3. Verify that:
   - At least 2–3 candidates were surfaced
   - Triage gates were applied
   - KB files were updated with git push success message
   - No errors in GH_PAT authentication

---

## Step 6: Monitor & Iterate

**What to monitor:**
- Token usage per run (should stay <5,500 for 4,000–5,000 budget)
- Sector rotation (ensure all 5 sectors are covered weekly)
- Universe growth (should add ~20–40 new QUEUED candidates per week)

**Adjust if needed:**
- If Stage 1 (Scout) is hitting token limits: reduce search depth from 5 to 4 searches
- If Stage 2/3 (Triage/Screen) time out: split into separate hourly runs (odd hours = scout, even hours = triage)
- If push failures persist: add retry logic with exponential backoff

---

## Step 7: Weekly Deep-Dive Agent

Separately (not part of hourly routine), create a weekly Sonnet agent that:
1. Reads UNIVERSE.md and pulls the QUEUED candidates
2. Runs full diligence (Stages 4–6 from the deep-dive framework)
3. Promotes strong candidates to CANDIDATE or WATCH status
4. Updates DIGEST.md with new WATCHes

This keeps the hourly routine lean (5k tokens) while allowing thorough analysis on weekends.

---

## File Structure

```
niche-moat-kb/
├── DIGEST.md            # Doctrine + current WATCH list
├── UNIVERSE.md          # Persistent candidate map + rotation cursor
├── KILL-LIST.md         # Triage failures
├── INDEX.md             # Quick company reference
├── ROUTINE-PROMPT.md    # The hourly routine script (this file)
├── SETUP.md             # Setup instructions (this file)
├── briefs/              # (future) Deep-dive brief summaries
│   └── [TICKER]-brief.md
└── memos/               # (future) Full forensic memos
    └── [TICKER]-[DATE].md
```

---

## GitHub Sync Workflow

Each hourly run:
1. Pulls latest KB files from GitHub (if running on multiple machines)
2. Executes Stage 1–5 (scout → update)
3. Commits changes
4. Pushes to origin/main

This creates a **linear, append-only history** of all candidates found, kills applied, and moats classified — a complete audit trail.

---

## Cost Estimate

**Per hourly run:**
- Model: Sonnet 4.6
- Tokens: ~4,000–5,000
- Estimated cost: ~$0.30–0.40 per run

**Per month (730 runs):**
- ~3.6M–3.65M tokens
- Estimated cost: ~$220–300

*(Adjust based on actual token consumption in first week.)*

---

## Next Steps

1. Create the GitHub repo
2. Set up the Claude Routine with the prompt from ROUTINE-PROMPT.md
3. Run the first test
4. Let it run hourly for 1–2 weeks to build universe
5. Then deploy the weekly deep-dive agent to promote candidates to WATCH
