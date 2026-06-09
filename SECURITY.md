# Security Policy

## What memory-wall-tracker handles

- Your `ANTHROPIC_API_KEY` (read from env or `~/.config/anthropic_key`)
- Public market data via yfinance
- Markdown briefs that get committed + pushed to GitHub

## What memory-wall-tracker does NOT do

- Touch any of your trading accounts or brokerages
- Execute any trades
- Collect telemetry
- Receive any user data — the input is solely your ticker basket config + Claude's research

## Reporting a vulnerability

Email: **xji1@mail.yu.edu**

Don't open a public GitHub issue. I'll respond within 72 hours.

## API key hygiene

- Never commit a real `ANTHROPIC_API_KEY`
- Use `~/.config/anthropic_key` (chmod 600) + the launchd plist pattern, OR `.env` + `python-dotenv`
- Rotate if leaked

## Not financial advice

Public research, public Brier audit. Don't trade on it without independent analysis.
