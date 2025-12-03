import matplotlib.pyplot as plt
from process_data import returns
from pull_data import fetch_hisitorical_data
import pandas as pd
# Close Price
def plot_close_price(symbol, period):
    df_close = pd.Series(fetch_hisitorical_data(symbol, period)["Close"])
    
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(df_close.index, df_close.values, color='blue', label="Close Price")
    ax.set_title(f"{symbol} Close Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    fig.tight_layout()
    return fig

#  Daily / Multi-day Returns 
def plot_returns(symbol, period):
    df_close = pd.Series(fetch_hisitorical_data(symbol, period)["Close"])
    
    fig, ax = plt.subplots(figsize=(7,4))
    
    # Compute returns using your process_data file
    metrics = returns(symbol, period)
    
    # Plot daily returns
    daily_returns = ((df_close - df_close.shift(1)) / df_close.shift(1) * 100)
    ax.plot(daily_returns.index, daily_returns.values, color='orange', label="Daily Return")
    
    # 5-day, 15-day, 30-day returns
    for days in [5, 15, 30]:
        multi_day = ((df_close - df_close.shift(days)) / df_close.shift(days) * 100)
        ax.plot(multi_day.index, multi_day.values, label=f"{days}-Day Return")
    
    ax.set_title(f"{symbol} Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Return (%)")
    ax.legend()
    fig.tight_layout()
    return fig


def plot_volatility(symbol, period):
    df_close = pd.Series(fetch_hisitorical_data(symbol, period)["Close"])
    
    daily_returns = df_close.pct_change().iloc[-30:]  # last 30 days
    thirty_day_vol = daily_returns.rolling(window=30).std() * (252**0.5)  # annualized
    
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(thirty_day_vol.index, thirty_day_vol.values, color='red', label="30-Day Volatility")
    ax.set_title(f"{symbol} 30-Day Volatility")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")
    ax.legend()
    fig.tight_layout()
    return fig


print(plot_returns("MSFT","1mo"))