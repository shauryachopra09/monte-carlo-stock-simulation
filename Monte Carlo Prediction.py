import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf

ticker=input("enter a ticker: ")
start_date="2020-1-1"

def import_stock_data(ticker, start="2010-1-1"):
    data=pd.DataFrame()
    stock=yf.Ticker(ticker)
    data=stock.history(start=start)
    return data

data=import_stock_data(ticker, start_date)

plt.figure(figsize = (10,6))
plt.plot(data['Close'], label="Close price")
plt.title(f'Close price of {ticker} since {start_date}')
plt.xlabel('Date')
plt.ylabel('Close price (inr)')
plt.legend()
plt.grid(True)
plt.show()

def log_returns(stock_data):
    log_returns=np.log(1+stock_data["Close"].pct_change())
    log_returns=log_returns[1:]
    return log_returns

log_return=log_returns(data)
print(log_return.tail())

plt.figure(figsize = (10,6))
plt.plot(log_return, label="Log Returns")
plt.title(f'Log Return of {ticker} since {start_date}')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.legend()
plt.grid(True)
plt.show()

def volatility_calc(lr):
    daily_volatility=np.std(lr)
    return daily_volatility

log_return=log_returns(data)
print(volatility_calc(log_return))

num_simulations=int(input("How many simulations would you like to run? "))
num_days=int(input("How many days do you want price to expect?"))
last_price=data['Close'].iloc[-1]

def run_montecarlo(num_simulations, num_days, last_price, log_return):
    daily_volatility=volatility_calc(log_return)
    all_simulations=[]
    for x in range(num_simulations):
        price_series=[last_price]
        for y in range(1, num_days):
            price=price_series[-1]*np.exp(np.random.normal(0,daily_volatility))
            price_series.append(price)
        all_simulations.append(price_series)
    simulation_df=pd.DataFrame(all_simulations).transpose()
    return simulation_df
log_return=log_returns(data)
simulation_df=run_montecarlo(num_simulations, num_days, last_price, log_return)
print(simulation_df.head())

simulation_df.plot(legend=False)
plt.suptitle(f'Monte Carlo Simulation for: {ticker}')
plt.axhline(y=last_price, color='r', linestyle='--')
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()

day_n_prices=simulation_df.iloc[-1]
lower_bound=np.percentile(day_n_prices, 2)
upper_bound=np.percentile(day_n_prices, 98)
mean_price=np.mean(day_n_prices)
print(f'The expected price for {num_days} days later is: {mean_price}')
print(f'the 95% confidence interval for {num_days} days is: {lower_bound},{upper_bound}')

