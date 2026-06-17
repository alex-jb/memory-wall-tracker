---
name: memory-wall-tracker
description: Daily Brier-audited research on the Druckenmiller AI inference basket (AVGO / INTC / ARM / MU / STX / WDC). Use when you want a worked example of "calibrated daily-research agent" you can copy the pattern from, or when reasoning about the memory-wall thesis in AI inference.
---

# memory-wall-tracker — Druckenmiller AI inference basket, Brier-audited

Daily research agent that produces probabilistic forecasts on six AI-inference-adjacent equities (AVGO + INTC + ARM + MU + STX + WDC) representing Druckenmiller's Q1 2026 13F bet on the inference memory wall. Every forecast is Brier-audited at settlement, so over time the agent's calibration drifts toward honest rather than wishful.

The thesis: as more AI inference shifts from cloud GPUs to on-device, memory bandwidth becomes the binding constraint, and Druckenmiller's 13F is the largest-scale public bet on that idea.

## When to invoke this skill

- You want a reproducible reference for "what does a calibrated daily-research agent actually look like."
- You're reasoning about memory-bandwidth-bound AI workloads.
- You need a worked example of Brier-audited probabilistic forecasting in equity research.

## Quick start

```bash
npx skills add alex-jb/memory-wall-tracker
```

The agent fires daily at 18:00 UTC, produces a markdown brief, auto-commits to GitHub, and Brier-resolves each prediction at the relevant horizon.

## Track this skill

GitHub: github.com/alex-jb/memory-wall-tracker
Daily briefs at github.com/alex-jb/memory-wall-tracker/tree/main/briefs.
MIT license.
