import plotly
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import pandas_datareader as web
import requests

headers = {
    'X-CMC_PRO_API_KEY': 'd8ff9db7-c90e-4ff4-8654-ad3a9fe00c53',
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '20',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for x in coins:
    print(x['symbol'], x['quote']['USD']['price'])


start = datetime(2021, 1, 1)
end = datetime(2022, 1, 1)
crypto_c = 'BTC'
df = web.DataReader(crypto_c, 'yahoo', start, end)
df = df.reset_index()

fig = go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high= df['High'],low=df['Low'], close=df['Adj Close']
                                    )])
plotly.offline.plot(fig, filename='candlestick.html')
