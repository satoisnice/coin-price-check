import json
import websocket
import pandas as pd

coins = ['BTCUSDT', 'ETHUSDT', 'XMRUSDT'] #coins to price check
coins = [coin.lower() + '@kline_3m' for coin in coins] #add kline to get the candle

coins = '/'.join(coins)

socket = f"wss://data-stream.binance.vision:443/ws{coins}"
def on_message(socket, msg):
    msg = json.loads(msg)
    print(msg)
