# HN Show — Memory Wall Tracker

**Title** (≤80 chars):
Show HN: Memory Wall Tracker — Brier-audited daily research on Druckenmiller's AI basket

**URL**:
https://github.com/alex-jb/memory-wall-tracker

**Body**:

I kept seeing the AI infrastructure thesis get framed as "buy more NVDA" and it never felt quite right — NVDA's compute lead is real but the *bottleneck* in production AI inference is increasingly memory bandwidth, IO, and networking, not raw FLOPS. Then Stan Druckenmiller's Q1 2026 13F came out with 30+ new positions in exactly that thesis: AVGO / INTC / ARM / MU / STX / WDC.

So I built a public Brier-audited research feed that tracks it.

Daily 14:00 ET, a Claude Sonnet 4.6 call pulls yfinance data for the 6 tickers and writes a structured brief: top-line / per-ticker thesis check / mispricing flags / catalyst monitor / predictions log. Every prediction gets a timestamp + a `resolve_by` date and is graded against actual price action when it resolves. The Brier score is the differentiation — anyone can publish bullish theses, few will get scored honestly.

Cost: ~$0.03/day. Architecture: yfinance + Anthropic SDK + launchd cron + git auto-commit + GitHub Pages.

The repo is intentionally a small case study, not a SaaS:
- 6-ticker basket (no NVDA — NVDA is the basket we're contrarian against; including it defeats the thesis)
- Daily brief in `briefs/YYYY-MM-DD.md`
- Companion site at vibexforge.com/memory-wall reads the latest brief from GitHub raw

Companion to my earlier [SpaceX-IPO-Tracker](https://github.com/alex-jb/spacex-ipo-tracker) which uses the same Brier-audit pattern on the SpaceX pure-play basket.

The roadmap (and the more interesting part) is the Brier resolver — a script that walks past briefs, grades open predictions at 1mo / 3mo / 6mo, and publishes a public leaderboard. Right now the math lives in [council-diff/brier.ts](https://github.com/alex-jb/council-diff/blob/main/src/brier.ts) (TypeScript) and [council-diff-py/brier.py](https://github.com/alex-jb/council-diff-py/blob/main/council_diff/brier.py) (Python).

Looking for feedback on:
- Is the 6-ticker basket the right grain, or should I do a 12-ticker version with sector splits?
- Best practice for evaluating "the model was confidently wrong" vs "the model was correctly uncertain" — Brier conflates both. Should I be doing reliability diagrams instead?

Not financial advice. Public research with public Brier audit.
