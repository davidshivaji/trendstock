from datetime import date
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.max_colwidth', 1000)
import yfinance as yf
today = date.today()

# ticks = []
# coins = ['ETH-USD', 'BTC-USD', 'LTC-USD']
#
#
# for coin in coins:
#     ticker = yf.Ticker(coin).info['regularMarketPrice']
#     ticks.append(ticker)

aapldf = yf.download('AAPL',
                        start="2004-01-01",
                        end=today.strftime("%Y-%m-%d"),
                        progress=False
                        )

aapldf['Close'].head()
