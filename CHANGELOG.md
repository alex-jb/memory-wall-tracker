# Changelog

## [Unreleased]

### Added
- Brier audit resolver script (planned) — walks past briefs + grades open predictions against actual yfinance closes

## [0.1.0] — 2026-06-09

### Added
- Initial release.
- 6-ticker basket: AVGO / INTC / ARM / MU / STX / WDC (Druckenmiller Q1 2026 13F).
- `scripts/daily_brief.py` — pulls yfinance prices + calls Claude Sonnet 4.6 + auto-commits brief.
- 14:00 ET launchd cron via `~/Library/LaunchAgents/com.alexji.memory-wall-brief.plist`.
- `briefs/2026-06-09.md` baseline brief with full thesis breakdown per ticker.
- GitHub Pages via `_config.yml` + `index.md`.
- `launch/awesome-list-prs.md` — 3 targeted submission PRs (awesome-investing / awesome-llm-apps / r/investing wiki).
- Bilingual README (EN + 中文).
- MIT license.

[0.1.0]: https://github.com/alex-jb/memory-wall-tracker/releases/tag/v0.1.0
