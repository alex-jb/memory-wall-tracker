# Memory Wall Tracker · 内存墙跟踪器

> [English](README.md) · [中文](README.zh-CN.md)

**Brier 审核的 AI 推理内存板块每日研究。**

> "推理 > 训练;AI 瓶颈从 GPU 算力转向内存带宽、IO 和网络。"
> —— Stanley Druckenmiller Q1 2026 13F 论点(根据公开报道转述)

Stan Druckenmiller Q1 2026 13F 罕见地一口气开 30+ 新仓位,主线是 **NVDA 之外的 AI 推理基础设施**。6 个核心 ticker:

| Ticker | 公司 | 内存墙论点 |
|---|---|---|
| **AVGO** | Broadcom | 定制 AI ASIC + 网络交换芯片 |
| **INTC** | Intel | 服务器 CPU + Optane 死后继承 |
| **ARM** | ARM Holdings | 数据中心 Neoverse 中标提速 |
| **MU** | Micron | HBM3E + DDR5 直接内存墙票 |
| **STX** | Seagate | AI 训练数据湖的大容量存储 |
| **WDC** | Western Digital | 推理缓存 + 存储分层 NAND |

每天纽约时间 14:00,Claude 管理的 brief 覆盖:
- 每个 ticker 当日价格 / 量能 / 资金流
- Catalyst 监控(财报、中标、供货合同)
- Mispricing 信号(Polymarket / 期权 ≠ 技术信号 时标记)
- Brier 审核的预测日志——公开

## 为什么做 Brier 审核

大多股票 newsletter 只挑赢家。这个 newsletter 公开每个预测 + 时间戳,事后按实际价格 resolves。Brier 分是差异化——任何人都能发牛市预测,少数人会接受诚实评分。

## 来源

- Druckenmiller Q1 2026 13F([SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001536411))
- [Motley Fool: Druckenmiller AI 推理篮子报道](https://www.fool.com/investing/2026/05/24/why-billionaire-stanley-druckenmiller-dumped-nvidi/)
- [Acquirers Multiple: Druckenmiller 2026-03 播客笔记](https://acquirersmultiple.com/2026/03/stanley-druckenmiller-massive-disruption-ahead/)

## 架构

- 每天 14:00 ET launchd cron 触发 `scripts/daily_brief.py`
- 抓 Yahoo Finance + 最新 13F + Tavily catalyst news
- Claude Sonnet 4.6 输出结构化 brief
- 输出: `briefs/YYYY-MM-DD.md`
- 自动 publish 到 GitHub Pages

## 路线图

- [x] Baseline (2026-06-09)
- [ ] 每日 brief cron
- [ ] Brier 审核 pipeline(1mo / 3mo / 6mo 结算)
- [ ] 公开 Brier 榜单 memory-wall.alex-jb.com
- [ ] 加 bonus ticker: NVDA (对照)、SK 海力士 ADR、AVAV、KLAC

## 相关

- [SpaceX-IPO-Tracker](https://github.com/alex-jb/spacex-ipo-tracker) — 同 pattern, SpaceX 纯洁 ticker
- [Orallexa](https://github.com/alex-jb/orallexa-ai-trading-agent) — 多 agent 量化研究栈

## 许可

MIT
