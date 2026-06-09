#!/usr/bin/env python3
"""daily_brief.py — Memory Wall 每日 brief.

每天 14:00 ET launchd 触发:
1. yfinance 拉 6 ticker 今日 OHLCV + 5d/30d delta
2. Anthropic Sonnet 4.6 写 brief
3. 写到 briefs/YYYY-MM-DD.md
4. git commit + push

Cost: ~$0.02-0.04/day.
Requires: ANTHROPIC_API_KEY in env (~/.config/anthropic_key fallback).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BRIEFS = REPO / "briefs"

TICKERS = [
    {"sym": "AVGO", "name": "Broadcom",       "thesis": "Custom AI ASICs + networking switches (1.6T Tomahawks, TPU successor)"},
    {"sym": "INTC", "name": "Intel",          "thesis": "Server CPUs + 2026 foundry roadmap recovery cycle"},
    {"sym": "ARM",  "name": "ARM Holdings",   "thesis": "Datacenter Neoverse design-win royalty compound (Graviton 5, Grace 2, Cobalt)"},
    {"sym": "MU",   "name": "Micron",         "thesis": "HBM3E + DDR5 — direct memory-wall play, HBM4 ramp Q3"},
    {"sym": "STX",  "name": "Seagate",        "thesis": "Mass-storage tier for AI training data lakes"},
    {"sym": "WDC",  "name": "Western Digital","thesis": "NAND for inference cache + storage tier"},
]


def get_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    keyfile = Path.home() / ".config" / "anthropic_key"
    if keyfile.exists():
        return keyfile.read_text().strip()
    return None


def fetch_price_snapshot(sym: str) -> dict:
    """Returns {price, delta_1d_pct, delta_5d_pct, delta_30d_pct, vol_ratio}."""
    try:
        import yfinance as yf
    except ImportError:
        return {"error": "yfinance not installed"}
    try:
        t = yf.Ticker(sym)
        h = t.history(period="40d", auto_adjust=True)
        if len(h) < 31:
            return {"error": f"insufficient history ({len(h)} bars)"}
        close = float(h["Close"].iloc[-1])
        prev = float(h["Close"].iloc[-2])
        c5 = float(h["Close"].iloc[-6])
        c30 = float(h["Close"].iloc[-31])
        vol_today = float(h["Volume"].iloc[-1])
        vol_avg30 = float(h["Volume"].iloc[-31:].mean())
        return {
            "price": round(close, 2),
            "delta_1d_pct": round((close - prev) / prev * 100, 2),
            "delta_5d_pct": round((close - c5) / c5 * 100, 2),
            "delta_30d_pct": round((close - c30) / c30 * 100, 2),
            "vol_ratio": round(vol_today / vol_avg30, 2) if vol_avg30 > 0 else 0,
        }
    except Exception as exc:
        return {"error": str(exc)[:200]}


def build_brief_prompt(snapshots: list[dict]) -> str:
    payload = []
    for tk, snap in zip(TICKERS, snapshots):
        payload.append({**tk, "snapshot": snap})
    return (
        "You are writing today's Memory Wall Tracker daily brief.\n"
        "Audience: solo investors + ML/quant researchers following Druckenmiller's Q1 2026 AI inference memory basket.\n"
        "Tone: honest, calibrated, no hype words. Numbers > vibes.\n\n"
        "Input — 6 tickers + Druckenmiller's thesis + today's price snapshot:\n\n"
        f"{json.dumps(payload, indent=2)}\n\n"
        "Write a markdown brief with this structure:\n\n"
        "## Top-line\n"
        "1-paragraph synthesis of today's basket moves. What's leading, what's lagging, any red flags.\n\n"
        "## Per-ticker (one bullet per ticker, ≤30 words each)\n"
        "For each ticker: current price + delta vs 5d/30d + the single most relevant thesis hook from today.\n\n"
        "## Mispricing flags\n"
        "Any ticker where today's price action diverges from the thesis (e.g. 'AVGO -2% on positive ARM design win news → contrarian setup'). "
        "If nothing diverges, write 'None flagged today.'\n\n"
        "## Tomorrow's watch\n"
        "1-2 catalysts or data releases to monitor.\n\n"
        "## Predictions log (rolling)\n"
        "Carry over yesterday's open predictions. Don't open new ones today unless conviction is exceptional.\n\n"
        "Use [src:yf] for price-derived claims. No fluff. No 'overall' or 'in conclusion'. End directly."
    )


def call_claude(prompt: str, api_key: str) -> str | None:
    try:
        import anthropic
    except ImportError:
        return None
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    if not msg.content:
        return None
    return msg.content[0].text


def git_commit_and_push(brief_path: Path) -> bool:
    try:
        subprocess.run(["git", "-C", str(REPO), "add", str(brief_path)], check=True)
        subprocess.run(
            ["git", "-C", str(REPO), "commit", "-m",
             f"brief: {brief_path.stem} daily Memory Wall update"],
            check=True,
        )
        subprocess.run(["git", "-C", str(REPO), "push"], check=True)
        return True
    except subprocess.CalledProcessError as exc:
        print(f"[git] {exc}", file=sys.stderr)
        return False


def main():
    api_key = get_api_key()
    if not api_key:
        print("[brief] no ANTHROPIC_API_KEY — abort", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).date().isoformat()
    out = BRIEFS / f"{today}.md"
    if out.exists() and "--force" not in sys.argv:
        print(f"[brief] {out} already exists, use --force to overwrite")
        return 0

    print(f"[brief] fetching 6 ticker snapshots...", file=sys.stderr)
    snapshots = [fetch_price_snapshot(t["sym"]) for t in TICKERS]

    print(f"[brief] calling Claude Sonnet 4.6...", file=sys.stderr)
    prompt = build_brief_prompt(snapshots)
    body = call_claude(prompt, api_key)
    if not body:
        print("[brief] Claude returned empty", file=sys.stderr)
        return 1

    header = (
        f"# Memory Wall daily brief — {today}\n\n"
        f"> Generated {datetime.now(timezone.utc).isoformat()} by Claude Sonnet 4.6\n\n"
    )
    out.write_text(header + body, encoding="utf-8")
    print(f"[brief] wrote {out}")

    if "--no-push" not in sys.argv:
        if git_commit_and_push(out):
            print(f"[brief] pushed to GitHub")

    return 0


if __name__ == "__main__":
    sys.exit(main())
