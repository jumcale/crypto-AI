from flask import Flask, jsonify
import pandas as pd
from data_collector import get_historical_data
from indicators import add_indicators
from strategy import predict

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = get_historical_data()
    df = add_indicators(df)
    signal = predict(df)
    return jsonify({'trade_signal': 'BUY' if signal == 1 else 'HOLD'})

if __name__ == '__main__':
    app.run(debug=True)