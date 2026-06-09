# r/investing (or r/SecurityAnalysis)

**Title**:
Open-source Brier-audited daily research on Druckenmiller's Q1 2026 AI inference basket

**Body**:

I built this for myself and figured I'd open-source it.

Druckenmiller's Q1 2026 13F showed 30+ new positions in AI inference memory / IO / networking — AVGO, INTC, ARM, MU, STX, WDC. His public commentary frames it as "inference > training, the bottleneck shifts from GPU compute to memory bandwidth." That's a structurally different bet than the NVDA momentum trade.

Most stock newsletters publish bullish theses and quietly forget the losers. This one publishes every prediction with a `resolve_by` date and scores itself with Brier at resolution. Mean Brier < 0.25 = better than coin-flip. Above 0.25 = worse than random and you should ignore me.

Daily brief at 14:00 ET. Claude Sonnet 4.6 + yfinance. About $0.03/day to run.

What's in a brief:
- Top-line per-ticker price + delta (1d / 5d / 30d)
- Thesis check per ticker
- Mispricing flags when price action diverges from the thesis  
- Catalyst monitor (next 30 days)
- Predictions log (rolling — carries over yesterday's open predictions)

Repo: github.com/alex-jb/memory-wall-tracker (MIT, bilingual README EN + 中文)
Live: vibexforge.com/memory-wall

What I'd love feedback on:
1. Is 6 the right basket size, or should I do a 12-ticker version with sector splits (memory / networking / storage)?
2. Brier conflates "confidently wrong" with "correctly uncertain" — should I be doing reliability diagrams instead?
3. Anyone seen prior art on calibration-honest public stock research feeds? I'd love to learn the failure modes before I hit them.

Not financial advice. Public research with public audit.
