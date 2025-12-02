import yfinance as yf
import pandas as pd


def fetch_info(symbol):


    try:

        ticker = yf.Ticker(symbol)


        ticker_info = ticker.info
        

        if not ticker_info:
            raise ValueError(f"No historical data found for ticker '{symbol}'")
        
        metrics ={
            "Name": "longName",
            "City": "city",
            "State": "state",
            "Current Price": "regularMarketPrice",
            "PE Ratio": "trailingPE",
            "EPS": "trailingEps",
            "Dividend Yield": "dividendYield",
            "Quarterly Earnings Growth": "earningsQuarterlyGrowth",
            "Total Debt": "totalDebt",
            "Gross Margin": "grossMargins"
        }
        
        values = {}
        for label, key in metrics.items():
                values[label] = ticker_info.get(key)
        

        
        return values
        


        


    

    except Exception as e:
        print(e)
        return None


def fetch_hisitorical_data(symbol, time):
    try:
        ticker = yf.Ticker(symbol)


        ticker_info = ticker.history(period = time)
        

        if ticker_info.empty:
            raise ValueError(f"No historical data found for ticker '{symbol}'")
        
        metrics ={
            "Open": "Open",
            "Close": "Close",
            "High": "High",
            "Low": "Low",
            "Volume": "Volume",
            "Dividends": "Dividends",
            "Stock Splits": "Stock Splits",
        }
        
        values = {}
        for label, key in metrics.items():
            values[label] = ticker_info[key].tolist()
        
        return values
    

    except Exception as e:
        print(e)
        return None
