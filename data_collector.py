import pandas as pd
from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

client = Client(API_KEY, API_SECRET)
client.API_URL = BASE_URL

def get_historical_data(symbol='BTCUSDT', interval='1h', lookback='1000'):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=int(lookback))
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df[['open', 'high', 'low', 'close', 'volume']].astype(float)