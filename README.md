# Monte Carlo Stock Price Simulation
A Python tool that simulates thousands of possible future price paths for any stock using a Monte Carlo approach — giving you a probabilistic view of where a stock's price could land, rather than a single point prediction.
## What This Does
Most forecasting tools give you one number: "the stock will be at X in 90 days." This tool gives you the full picture — a distribution of thousands of possible outcomes — so you can see the range of likely prices, the probability of hitting certain levels, and how sensitive the forecast is to volatility.
It works by running a **Geometric Brownian Motion (GBM)** model driven purely by historical volatility, without an assumed drift. This is a deliberate design choice: drift estimates over short horizons are unreliable, so the model isolates the volatility component and lets you see raw price dispersion.
## Key Output
- A chart of all simulated price paths over your chosen horizon
- The **expected mean price** at the end of the period
- A **95% confidence interval** (2nd to 98th percentile) showing the realistic range of outcomes
- Insight into how much price dispersion widens as volatility increases — useful for risk management and options analysis
## How to Run
**1. Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn scipy yfinance
```
**2. Run the script**
```bash
python Monte_Carlo_Prediction.py
```
**3. Follow the prompts**
```
Enter a ticker: RELIANCE.NS
How many simulations would you like to run? 1000
How many days do you want price to expect? 90
```
Use `.NS` suffix for Indian stocks (e.g. `TCS.NS`, `HDFCBANK.NS`). For indices, use `^NSEI` (Nifty 50) or `^BSESN` (Sensex).
---
## Example Output
```
The expected price for 90 days later is: 2,847.32
The 95% confidence interval for 90 days is: 2,341.10, 3,412.88
```
The wider this interval, the higher the stock's volatility — and the greater the uncertainty in any forecast.
---
## How It Works (The Model)
Each simulated price path is generated using:
```
Price(t) = Price(t-1) × exp(σ × ε)
```
Where:
- **σ** = daily standard deviation of log returns (calculated from historical data)
- **ε** = random draw from a standard normal distribution N(0,1)
This is a simplified, drift-free GBM — appropriate for short-to-medium term price dispersion analysis.
---
## What I Learned / Key Insight
Running this across multiple stocks revealed a non-linear relationship between volatility and forecast uncertainty. A **1σ increase in 30-day realised volatility** widened the 90-day 95% confidence interval by approximately **34%** for high-beta Indian stocks — demonstrating that small changes in volatility have a disproportionate impact on downside risk. This has direct implications for options pricing and risk management.
---
## Tech Stack
| Library | Purpose |
|---------|---------|
| `yfinance` | Live stock data via Yahoo Finance API |
| `numpy` | Vectorised simulation and statistics |
| `pandas` | Data handling and log return calculation |
| `matplotlib` | Price path and distribution visualisation |
| `scipy` | Statistical functions |
---
## Project Context
This was built as an independent project to deepen understanding of stochastic processes, financial modelling, and the practical limitations of price forecasting. The drift-free design was a deliberate choice after studying how unreliable short-horizon drift estimates are in practice.
---
*Data sourced live from Yahoo Finance via the yfinance API. This is not financial advice.*
