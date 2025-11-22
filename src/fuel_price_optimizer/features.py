import pandas as pd
import numpy as np

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("date").copy()
    df["dayofweek"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)
    df["month"] = df["date"].dt.month

    df["comp_mean"] = df[["comp1_price", "comp2_price", "comp3_price"]].mean(axis=1)
    df["comp_min"]  = df[["comp1_price", "comp2_price", "comp3_price"]].min(axis=1)

    df["price_vs_comp_min"] = df["price"] - df["comp_min"]
    df["price_vs_comp_mean"] = df["price"] - df["comp_mean"]

    df["price_lag1"] = df["price"].shift(1)
    df["volume_lag1"] = df["volume"].shift(1)

    df["volume_ma7"] = df["volume"].rolling(7, min_periods=1).mean().shift(1)
    df["price_ma7"] = df["price"].rolling(7, min_periods=1).mean().shift(1)
    df["comp_mean_ma7"] = df["comp_mean"].rolling(7, min_periods=1).mean().shift(1)

    df = df.dropna().reset_index(drop=True)
    return df
