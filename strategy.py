from model import load_model

def predict(df):
    model = load_model()
    X = df[['rsi', 'macd', 'sma']].iloc[-1:]
    prediction = model.predict(X)[0]
    return prediction  # 1 = Buy, 0 = Hold/Sell