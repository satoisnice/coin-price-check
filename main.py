import json
import websocket
import pandas as pd

coins = ['BTCUSDT', 'ETHUSDT', 'XMRUSDT'] #coins to price check
coins = [coin.lower() + '@kline_3m' for coin in coins] #add kline to get the candle

coins = '/'.join(coins)
print(coins)
