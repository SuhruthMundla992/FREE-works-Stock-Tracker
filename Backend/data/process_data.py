from pull_data import fetch_hisitorical_data,fetch_info
import yfinance as yf
import pandas as pd
import statistics as st
import math
def returns(symbol, time):
    df_close = pd.Series(fetch_hisitorical_data(symbol=symbol,time=time)["Close"])

    daily = ((df_close - df_close.shift(1))/ df_close.shift(1) *100).iloc[-1]
    five_day = ((df_close - df_close.shift(5))/ df_close.shift(5) *100).iloc[-1]
    fifteen_day = ((df_close - df_close.shift(15))/ df_close.shift(15) *100).iloc[-1]
    thirty_day = ((df_close - df_close.shift(30))/ df_close.shift(30) *100).iloc[-1]

    daily_returns = df_close.pct_change().iloc[-30:]
    thirty_day_volatility = daily_returns.std(ddof=1) * math.sqrt(252)

    info = {
        "Daily Return": daily,
        "5 day Return": five_day,
        "15 day Return": fifteen_day,
        "30 day Return": thirty_day,
        "30 day Volatility": thirty_day_volatility
    }

    return info



def get_recommend(symbol):
    stock = yf.Ticker(symbol)
    return stock.recommendations


print(returns("MSFT","2mo"))
print(get_recommend("MSFT"))


