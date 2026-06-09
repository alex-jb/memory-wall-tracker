# Contributing

Thanks for considering a contribution. `memory-wall-tracker` is intentionally small — a daily Claude-managed research feed on Stan Druckenmiller's Q1 2026 13F AI inference memory basket.

## Quick start

```bash
git clone https://github.com/alex-jb/memory-wall-tracker.git
cd memory-wall-tracker
pip install yfinance anthropic
ANTHROPIC_API_KEY=sk-ant-... python scripts/daily_brief.py
```

Output goes to `briefs/YYYY-MM-DD.md` and auto-commits if you remove `--no-push`.

## What we welcome

- **Better catalyst monitoring** — improve the prompt section that lists 30-day catalysts. PRs that add specific earnings dates / supplier signals / Polymarket price feeds are great.
- **Brier audit resolver** — current predictions log lives in markdown. A `scripts/resolve_brier.py` that walks past briefs + grades open predictions against actual yfinance closes would be killer.
- **Add tickers (or remove them)** — if Druckenmiller's next 13F adds positions, propose adding them. If a thesis breaks (e.g. STX margin compression confirmed), propose removing.
- **GitHub Pages improvements** — the `_config.yml` is minima; better theme + jekyll-feed integration welcome.

## What we'll reject

- Real-time trading hooks. This is research, not a bot.
- Subscription / paywall infra. This stays free and public.
- Recommendations to add NVDA. NVDA is the basket Druckenmiller is contrarian against; including it defeats the thesis.

## Style

- Python 3.10+
- Single-purpose scripts in `scripts/`
- Brief markdown structure stays consistent across days (top-line / per-ticker / mispricing flags / catalysts / predictions log)

## Not financial advice

This is public research with public Brier audit. Don't trade on it without your own analysis. We're scoring ourselves honestly; you're responsible for your own positions.

## License

By contributing, you agree your contributions are licensed under MIT.
