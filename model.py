from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)
    X = df[['rsi', 'macd', 'sma']]
    y = df['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'ai_trading_bot/model.pkl')
    return model

def load_model():
    import joblib
    return joblib.load('ai_trading_bot/model.pkl')