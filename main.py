# https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories

import sys
from datetime import date
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import yfinance as yf

pytrends = TrendReq(hl='en_US', tz=360)

# all_keywords = [x.replace("-", " ") for x in sys.argv[1:]]
all_keywords = ['bitcoin']

today = date.today()
start = '2010-01-01'

frame = f'{start} {today.strftime("%Y-%m-%d")}'

stockdf = yf.download('BTC-USD',
                        start=start,
                        end=today.strftime("%Y-%m-%d"),
                        progress=False
                        )

normalizer = stockdf['Close'].max() / 100

pytrends.build_payload(all_keywords, timeframe=frame, geo='')

df = pytrends.interest_over_time()
df.head(20)

plt.style.use('dark_background')
plt.figure().patch.set_facecolor('#121212')
plt.axes().set_facecolor('#080808')
linewidth = 1

colors = ['silver', 'teal', 'green', 'magenta', 'skyblue']

for i, x in enumerate(all_keywords):
    plt.plot(df[x], color=colors[i], label=x + ' trend', linewidth=linewidth)

plt.plot(stockdf['Close'] / normalizer, color="orange", label="bitcoin price", linewidth=linewidth)

plt.ylabel('Percentage of all-time highest value')

plt.legend()
plt.grid(color='#303030')

# wherever you run this from, it will save the image there.
# plt.savefig(f'{"_".join(sys.argv[1:])}.png', dpi=120)

plt.show()
