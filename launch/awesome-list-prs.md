# Memory Wall Tracker — awesome-list PR templates

Three targeted lists for the Brier-audit / public-research angle.

---

## 1. awesome-investing (or awesome-finance)

**Target repo**: `karan/awesome-finance` or similar curated investing list

**File**: `README.md` under `### Research Tools` or `### Open Source`

**Line to add**:
```markdown
- [Memory Wall Tracker](https://github.com/alex-jb/memory-wall-tracker) - Brier-audited daily research on Stan Druckenmiller's Q1 2026 AI inference memory basket (AVGO/INTC/ARM/MU/STX/WDC). Daily Claude-managed brief at 14:00 ET. Every prediction timestamped + scored honestly at resolution. MIT, bilingual README.
```

**PR title**: Add Memory Wall Tracker — Brier-audited daily research

**PR body**:
Adds Memory Wall Tracker, an open-source daily research feed focused on Stan Druckenmiller's Q1 2026 13F AI inference memory basket. Same Brier-audit pattern as SpaceX-IPO-Tracker — every prediction is timestamped and gets scored against actual price action at resolution.

Daily brief at 14:00 ET via Claude Sonnet 4.6. ~$0.03/day operating cost. 6-ticker basket: AVGO/INTC/ARM/MU/STX/WDC.

Differentiation: most newsletters cherry-pick winners. This one publishes the Brier score. The willingness to be scored honestly is the moat.

MIT license. Bilingual README EN + 中文.

---

## 2. awesome-llm-apps

**Target repo**: `Shubhamsaboo/awesome-llm-apps`

**File**: `README.md` under `### Finance / Research` section

**Line to add**:
```markdown
- [Memory Wall Tracker](https://github.com/alex-jb/memory-wall-tracker) - Claude Sonnet 4.6-managed daily Brier-audited investment research on a focused 6-ticker basket. Demonstrates pattern of using LLM for production research that gets graded on actual outcomes. MIT.
```

**PR title**: Add Memory Wall Tracker to finance/research section

**PR body**:
Adds Memory Wall Tracker — an LLM-managed daily research feed that gets Brier-scored at resolution.

The pattern is interesting for the awesome-llm-apps audience: most LLM "research" outputs are evaluated on quality of writing or factual accuracy of summary. This one is graded on whether the recommendations actually pan out over time. Every brief timestamped, every prediction logged, every resolution graded honestly.

Companion to my SpaceX-IPO-Tracker (already in this list if added previously). Same architecture, different basket — Druckenmiller's Q1 2026 AI inference memory thesis.

MIT, bilingual README (EN + 中文), daily Claude Sonnet 4.6 cron at 14:00 ET, ~$0.03/day.

---

## 3. awesome-stock-research (or community subreddit wiki)

**Target**: r/investing wiki + r/SecurityAnalysis wiki (text submissions)

**Submission text**:

> **Memory Wall Tracker** — open-source Brier-audited daily research on Druckenmiller's Q1 2026 AI inference memory basket
>
> https://github.com/alex-jb/memory-wall-tracker
>
> 6 tickers (AVGO/INTC/ARM/MU/STX/WDC), Claude-managed daily brief at 14:00 ET, every prediction Brier-scored at resolution. MIT, bilingual README.
>
> The point isn't the picks. The point is the discipline — publishing predictions with timestamps and getting graded on whether they were right, instead of cherry-picking winners after the fact. Companion to SpaceX-IPO-Tracker which uses the same pattern on a different basket.
>
> Not financial advice. Public research with public Brier audit.

---

## Submission order

1. Day 1 (today after launch): awesome-llm-apps (technical audience, lowest controversy)
2. Day 2: awesome-investing / finance (broader investor audience)
3. Day 3: r/investing wiki + r/SecurityAnalysis (community-curated, slower but durable)
