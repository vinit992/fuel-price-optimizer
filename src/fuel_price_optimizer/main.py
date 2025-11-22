import json
import pandas as pd
from datetime import datetime

from .config import DATA_DIR, REPORT_DIR, BACKTEST_DIR, MODEL_DIR, OPT_CONFIG
from .pipeline import run_training, FEATURE_COLS
from .optimizer import recommend_price
from .summary import save_summary

def main():
    df = pd.read_csv(DATA_DIR/"oil_retail_history.csv")
    df["date"] = pd.to_datetime(df["date"])

    model, df_feat, metrics = run_training(df)

    today = json.load(open(DATA_DIR/"today_example.json"))

    last_row = df_feat.iloc[-1]

    today_row = {
        **today,
        "date": pd.to_datetime(today["date"]),
        "price_lag1": last_row["price"],
        "volume_lag1": last_row["volume"],
        "volume_ma7": last_row["volume_ma7"],
        "price_ma7": last_row["price_ma7"],
        "comp_mean_ma7": last_row["comp_mean_ma7"],
        "comp_mean": last_row["comp_mean"],
        "comp_min": last_row["comp_min"],
        "dayofweek": last_row["dayofweek"],
        "is_weekend": last_row["is_weekend"],
        "month": last_row["month"]
    }

    rec = recommend_price(today_row, model, FEATURE_COLS, OPT_CONFIG)

    out = {
        "date": today["date"],
        "recommended_price": rec["recommended_price"],
        "expected_volume": rec["predicted_volume"],
        "expected_profit": rec["expected_profit"],
        "metrics": metrics
    }

    json.dump(out, open(REPORT_DIR/"today_recommendation.json","w"), indent=2)

    summary = f"""
Fuel Price Optimization Report
===============================

Recommended price: {rec['recommended_price']}
Expected volume: {rec['predicted_volume']}
Expected profit: {rec['expected_profit']}

Test RMSE: {metrics['rmse']}
Test R2: {metrics['r2']}
"""

    save_summary(summary, REPORT_DIR/"summary_document.pdf")

if __name__ == "__main__":
    main()
