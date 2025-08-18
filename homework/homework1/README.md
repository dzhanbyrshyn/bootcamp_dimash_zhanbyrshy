
# Cross-timezone Crypto Signals
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Crypto trades 24/7, but liquidity and trading activity are not evenly distributed throughout the day. Volume clusters around major financial centers (i.e., Asia, 
Europe, and the US), creating distinct “sessions.” Traders lack clarity on whether heavy trading activity in one session (e.g., Asia) foreshadows price moves 
or volatility in the next (e.g., US). This project studies BTC/ETH at an hourly level, summarizing “sessions” by time zone and testing whether high‑activity 
sessions predict higher volatility or directional bias in the subsequent session by analyzing BTC and ETH volume and returns across global sessions to detect 
whether cross-session dynamics provide useful predictive information.

## Stakeholder & User
The primary users are active crypto traders who decide whether to increase, reduce, or hold exposure before the next major regional session begins. 
Secondary users include quantitative researchers who are interested in studying market microstructure in digital assets. 
The context of use is short-term decision making: traders evaluating overnight or cross-timezone risk before a new trading session starts.

## Useful Answer & Decision
The project is descriptive and predictive in nature. On the descriptive side, it will show how BTC and ETH behave in each region’s session, in terms of trading volume and volatility. 
On the predictive side, it will test whether sessions with unusually high volume tend to be followed by more volatile or directional next sessions. 

The expected artifact is a notebook and a short write-up with charts and concise explanations of these findings.

**Decision window:** the answer is designed for short-term traders who reassess risk every session (about every 8 hours), so that they can decide whether to hold, reduce, or increase exposure before the next timezone’s trading activity begins.

## Assumptions & Constraints
- Session cutoffs: Asia (00:00–08:00 UTC), Europe (08:00–16:00 UTC), US (16:00–24:00 UTC)  
- Hourly OHLCV data for BTC and ETH is available and representative enough to study session effects  
- Results will be compared across several months to capture different regimes  
- API limits or exchange differences may affect the precision of reported volumes  
- Goal is insight and learning, not production-ready trading signals  

## Known Unknowns / Risks
- Market regime changes (bull vs bear) may alter the effect  
- Exchange-specific reporting differences may introduce noise  
- Weekend activity may behave differently comparing to weekdays  
- Relationships may weaken or disappear as market structure evolves  

## Lifecycle Mapping
Goal → Stage → Deliverable  
Define whether cross-timezone crypto activity can be structured as a decision problem → Problem Framing & Scoping (Stage 01) → README.md with scoping text and repo skeleton  

## Repo Plan
- Subfolders will include: /data/, /src/, /notebooks/, /docs/  
- Updates and commits will be made regularly after each bootcamp stage milestone
