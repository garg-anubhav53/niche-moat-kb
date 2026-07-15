# Deployment Checklist — Niche Moat KB Hourly Routine

Follow this step-by-step to get the routine running.

---

## Phase 1: GitHub Setup (5 minutes)

- [ ] **Create a new GitHub repo** named `niche-moat-kb`
  - Make it **public** (free file hosting)
  - Initialize with README (will overwrite with ours)

- [ ] **Clone the repo locally:**
  ```bash
  git clone https://github.com/YOUR-USERNAME/niche-moat-kb.git
  cd niche-moat-kb
  ```

- [ ] **Copy KB files from this local checkout** into the repo directory:
  ```bash
  cp /tmp/niche-moat-kb/* . && git add -A
  ```

- [ ] **Commit and push:**
  ```bash
  git commit -m "init: niche-moat-kb doctrine, routine, and structures"
  git push origin main
  ```

- [ ] **Verify on GitHub:** Visit `github.com/YOUR-USERNAME/niche-moat-kb` — should see all 8 files

---

## Phase 2: GitHub PAT Setup (3 minutes)

- [ ] **Create a GitHub Personal Access Token** (classic, not fine-grained):
  - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Click "Generate new token (classic)"
  - **Scopes needed:** `repo` (full control of private repositories)
  - **Expiration:** No expiration (or 90 days if required)
  - **Save the token** — you'll need it in Phase 3

- [ ] **Verify PAT has `repo` scope** (required for git push from routine)

---

## Phase 3: Claude Routine Setup (10 minutes)

- [ ] **Log into claude.ai/code/routines**

- [ ] **Click "Create New Routine"** (or "New" button if available)

- [ ] **Fill in these fields:**
  - **Name:** `niche-moat-hourly`
  - **Description:** `Cross-industry niche moat scout, hourly, find 2x+ re-rating candidates`
  - **Model:** Claude Sonnet 4.6 (NOT Haiku, NOT Opus)
  - **Cadence:** `Every 1 hour` (or in cron: `0 * * * *`)

- [ ] **Environment Setup:**
  - Click "Create New Environment" (or "Edit Environment" if one exists)
  - Name it: `niche-moat-prod`
  - Add these environment variables:
    ```
    GH_PAT=<paste the PAT token from Phase 2>
    KB_REPO_URL=https://github.com/YOUR-USERNAME/niche-moat-kb.git
    KB_LOCAL_PATH=/tmp/niche-moat-kb
    ```
  - Save the environment

- [ ] **Paste the Routine Prompt:**
  - In the "Prompt" field, paste the **entire text** of `ROUTINE-PROMPT.md`
  - Append this at the very end:
    ```
    ## Auto-Commit & Push
    
    After routine completes, run:
    ```bash
    cd ${KB_LOCAL_PATH}
    git add DIGEST.md UNIVERSE.md KILL-LIST.md INDEX.md
    git -c user.name=niche-moat-bot -c user.email=kb-routine@local commit -m "scout $(date +'%Y-%m-%d %H:%M'): routine run"
    git push origin main
    ```
    If git push fails, report error in output but continue next run.
    ```

- [ ] **Save the Routine** (click Save or Create)

---

## Phase 4: First Test Run (5 minutes)

- [ ] **In the Routine page, click "Run Now"** (don't wait for next hour)

- [ ] **Wait 2–3 minutes for execution**

- [ ] **Check the output for:**
  - ✅ "Candidates Passed Triage" section (at least 2–3 candidates found)
  - ✅ "Candidates Killed" section (showing triage gates applied)
  - ✅ "Git push succeeded" message at the end
  - ✅ No authentication errors

- [ ] **If push failed:**
  - Go back to Phase 2 and verify GH_PAT is correct
  - Test the token locally: `curl -H "Authorization: token <TOKEN>" https://api.github.com/user`
  - If valid, update the environment variable in the routine and re-run

- [ ] **If candidates found are all defense-sector or low-quality:**
  - The first run scouts opportunistically; quality improves as universe builds
  - This is normal; let it run for 1 week

---

## Phase 5: Verify GitHub Sync (2 minutes)

- [ ] **Go to your GitHub repo** (`github.com/YOUR-USERNAME/niche-moat-kb`)

- [ ] **Check "Commits" tab:**
  - Should see at least 1 new commit from the test run
  - Message should include "scout [timestamp]"

- [ ] **Check files:**
  - `UNIVERSE.md` should show new candidates in the "Universe Map" table
  - `KILL-LIST.md` should show killed candidates

- [ ] **If nothing changed:**
  - The routine executed but didn't push
  - Check GH_PAT again; try manually from local: `git push origin main`

---

## Phase 6: Set to Hourly (1 minute)

- [ ] **Go back to the routine** on claude.ai/code/routines

- [ ] **Check cadence is set to "Every 1 hour"** (it should be from Phase 3)

- [ ] **Click "Enable Routine"** or toggle to ON

- [ ] **Verify:** The routine should now run automatically every hour

---

## Phase 7: Monitor (Ongoing)

- [ ] **Check GitHub repo once per day:**
  - New commits appearing every ~1 hour
  - UNIVERSE.md growing (new QUEUED candidates added)
  - KILL-LIST.md capturing triage failures

- [ ] **After 1 week:**
  - Universe should have ~150–200 candidates
  - Review DIGEST.md to see if any candidates are promoted to CANDIDATE or WATCH
  - If asymmetry looks high, consider deep-dive on top 3–5

- [ ] **After 1 month:**
  - Decide if you want to deploy the weekly deep-dive agent (separate Sonnet agent that promotes QUEUED → WATCH)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Git push failed — authentication" | Check GH_PAT value; regenerate if expired; verify `repo` scope |
| "No candidates found" | Sector rotation may have hit a dry sector; check logs; re-run next hour |
| "All candidates are cap-kills" | First few runs may scout outside the band; filter improves as triage refines |
| "Token usage too high (>6k)" | Reduce Stage 1 from 5 searches to 4; run weekly deep-dive separately |
| "Routine not running on schedule" | Verify cadence is "Every 1 hour" and "Enable Routine" toggle is ON |

---

## Success Criteria (End of Week 1)

- [ ] Routine runs automatically every hour (no manual trigger needed)
- [ ] GitHub repo receives new commits every ~1 hour (visible in commit history)
- [ ] UNIVERSE.md has 150+ candidates screened
- [ ] KILL-LIST.md shows diverse kill reasons (cap, coverage, price, sector)
- [ ] Token usage per run averages 4,000–5,000 (not exceeding 6,000)
- [ ] At least 1 candidate flagged for deeper diligence

---

## Next: Weekly Deep-Dive Agent (Optional)

Once the hourly routine is stable (1–2 weeks), create a separate **weekly agent** that:
1. Reads UNIVERSE.md and pulls top-5 QUEUED candidates
2. Runs full moat + asymmetry diligence (1.5–2k tokens per candidate)
3. Promotes strong ones to CANDIDATE or WATCH
4. Outputs investment memo per candidate

This keeps the hourly routine lean while allowing thorough analysis on non-critical time.

---

## Cost Summary

- **Hourly routine:** ~$250–300/month (Sonnet 4.6, ~730 runs/month)
- **Weekly deep-dive agent** (optional): ~$50–75/month (Sonnet, 4 runs/month × 5 candidates)
- **Total:** $250–375/month for hourly scout + weekly deep-dive

---

## Questions?

Check:
1. `README.md` — overview and thesis
2. `ROUTINE-PROMPT.md` — detailed prompt logic
3. `SETUP.md` — full technical setup guide

Good luck!
