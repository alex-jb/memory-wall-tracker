# LinkedIn — Memory Wall Tracker

I open-sourced **Memory Wall Tracker** — a Brier-audited daily research feed on a focused 6-stock AI inference basket.

The thesis comes from Stan Druckenmiller's Q1 2026 13F: 30+ new positions in AVGO / INTC / ARM / MU / STX / WDC. His framing — "inference > training; the bottleneck shifts from GPU compute to memory bandwidth, IO, and networking" — is the contrarian read to the NVDA-only AI infrastructure narrative.

Most stock newsletters cherry-pick winners. This one publishes every prediction with a timestamp and **grades itself honestly at resolution** via Brier score.

How it works:
🟢 Daily 14:00 ET, Claude Sonnet 4.6 reads yfinance data + writes a structured brief
🟢 Each brief carries forward open predictions with `resolve_by` dates
🟢 Resolved predictions get Brier-scored; the mean across resolved positions is published
🟢 Cost: ~$0.03/day. Architecture: yfinance + Anthropic SDK + launchd cron + GitHub Pages

The differentiation isn't the thesis. The differentiation is the willingness to be graded.

Companion to my [SpaceX-IPO-Tracker](https://github.com/alex-jb/spacex-ipo-tracker) which uses the same Brier-audit pattern on a different basket.

Live: vibexforge.com/memory-wall
Code: github.com/alex-jb/memory-wall-tracker (MIT, bilingual README EN + 中文)

Not financial advice. Public research with public Brier audit.

What other public research feeds get graded honestly at resolution? Drop links in the comments — I'd love to see the prior art on calibration-honest investing newsletters.
