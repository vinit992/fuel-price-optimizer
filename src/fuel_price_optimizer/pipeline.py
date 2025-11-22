from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
from .features import add_features
from .model import train_model
from .config import MODEL_DIR

FEATURE_COLS = [
    "price","cost","comp1_price","comp2_price","comp3_price",
    "comp_mean","comp_min","price_vs_comp_min","price_vs_comp_mean",
    "price_lag1","volume_lag1","volume_ma7","price_ma7",
    "comp_mean_ma7","dayofweek","is_weekend","month"
]

def run_training(df):
    df = add_features(df)
    X = df[FEATURE_COLS]
    y = df["volume"]

    X_train, X_test, y_train, y_test = (
        X.iloc[:-60],
        X.iloc[-60:],
        y.iloc[:-60],
        y.iloc[-60:],
    )

    model = train_model(X_train, y_train, MODEL_DIR/"rf_demand_model.joblib")

    y_pred = model.predict(X_test)

    metrics = {
        "rmse": float(mean_squared_error(y_test, y_pred, squared=False)),
        "r2": float(r2_score(y_test, y_pred)),
    }

    return model, df, metrics
