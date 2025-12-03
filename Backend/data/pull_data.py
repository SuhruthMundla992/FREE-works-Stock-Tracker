import yfinance as yf
import pandas as pd


def fetch_info(symbol):


    try:

        ticker = yf.Ticker(symbol)


        ticker_info = ticker.info #dictionary of common information
        

        if not ticker_info: #checks if data is present
            raise ValueError(f"No historical data found for ticker '{symbol}'")
        
        metrics ={ #metrics I am presenting
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
        
        values = {} #adds metrics of info to easy to process data
        for label, key in metrics.items():
                values[label] = ticker_info.get(key)
        

        
        return values
        


        


    

    except Exception as e:
        print(e)
        return None

#same thing but for hisotircal data
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
