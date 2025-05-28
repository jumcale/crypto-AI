from data_collector import get_historical_data
from indicators import add_indicators
from model import train_model
from strategy import predict
from trader import place_order

def run():
    df = get_historical_data()
    df = add_indicators(df)
    model = train_model(df)
    signal = predict(df)
    place_order(signal)

if __name__ == '__main__':
    run()