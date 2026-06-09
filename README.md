# Memory Wall Tracker

> [English](README.md) · [中文](README.zh-CN.md)

**Brier-audited daily research on the AI inference memory basket.**

> "Inference > training; the AI bottleneck shifts from GPU compute to memory bandwidth, IO, and networking."  
> — Stanley Druckenmiller's Q1 2026 13F thesis (paraphrased from public coverage)

Stan Druckenmiller's Q1 2026 13F showed an uncharacteristically large 30+ new positions, with the dominant theme being **AI inference infrastructure beyond NVDA**. The 6 tickers:

| Ticker | Company | Memory wall thesis |
|---|---|---|
| **AVGO** | Broadcom | Custom AI ASICs + networking switches |
| **INTC** | Intel | Server CPUs + Optane post-mortem still relevant |
| **ARM** | ARM Holdings | Datacenter Neoverse design wins accelerating |
| **MU** | Micron | HBM3E + DDR5 — direct memory wall play |
| **STX** | Seagate | Mass storage tier for AI training data lakes |
| **WDC** | Western Digital | NAND for inference cache + storage tier |

Each day at 14:00 ET, a Claude-managed brief covers:
- Daily price / volume / flow on each ticker
- Catalyst monitor (earnings, design wins, supply contracts)
- Mispricing flags (when Polymarket / options imply ≠ technical signal)
- Brier-audited prediction log — public

## Why Brier audit

Most stock newsletters cherry-pick winners. This one publishes every prediction with a timestamp + later resolves it against actual price action. The Brier score is the differentiation — anyone can publish bullish theses, few will get scored honestly.

## Sources

- Druckenmiller Q1 2026 13F filing ([SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001536411))
- [Motley Fool: Druckenmiller AI inference basket coverage](https://www.fool.com/investing/2026/05/24/why-billionaire-stanley-druckenmiller-dumped-nvidi/)
- [Acquirers Multiple: Druckenmiller 2026-03 podcast notes](https://acquirersmultiple.com/2026/03/stanley-druckenmiller-massive-disruption-ahead/)

## Architecture

- Daily 14:00 ET launchd cron triggers `scripts/daily_brief.py`
- Pulls Yahoo Finance + 13F latest + catalyst news via Tavily
- Claude Sonnet 4.6 produces structured brief
- Output: `briefs/YYYY-MM-DD.md`
- Auto-published to GitHub Pages

## Roadmap

- [x] Baseline (2026-06-09)
- [ ] Daily brief cron
- [ ] Brier audit pipeline (settle predictions at 1mo / 3mo / 6mo)
- [ ] Public Brier leaderboard at memory-wall.alex-jb.com
- [ ] Add bonus tickers: NVDA (control), SK Hynix ADR, AVAV, KLAC

## Related

- [SpaceX-IPO-Tracker](https://github.com/alex-jb/spacex-ipo-tracker) — same pattern, SpaceX-pure-play tickers
- [Orallexa](https://github.com/alex-jb/orallexa-ai-trading-agent) — multi-agent quant research stack

## License

MIT
