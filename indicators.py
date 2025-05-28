import ta

def add_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close'], window=14).rsi()
    df['macd'] = ta.trend.MACD(close=df['close']).macd()
    df['sma'] = ta.trend.SMAIndicator(close=df['close'], window=20).sma_indicator()
    df.dropna(inplace=True)
    return df