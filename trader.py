from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL, TRADE_SYMBOL, TRADE_QUANTITY

client = Client(API_KEY, API_SECRET)
client.API_URL = BASE_URL

def place_order(signal):
    if signal == 1:
        order = client.order_market_buy(symbol=TRADE_SYMBOL, quantity=TRADE_QUANTITY)
        print("Buy order placed:", order)
    else:
        print("No trade signal.")