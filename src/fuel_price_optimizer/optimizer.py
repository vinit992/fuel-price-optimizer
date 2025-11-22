import numpy as np
import pandas as pd

def recommend_price(row, model, feature_cols, config):
    last_price = row.get("price_lag1", row["price"])
    step = config["grid_step"]

    candidates = np.arange(
        last_price - config["max_daily_change"],
        last_price + config["max_daily_change"] + 1e-9,
        step,
    )
    candidates = np.round(candidates, 2)

    feats = []
    for p in candidates:
        feats.append({
            **row,
            "price": p,
            "price_vs_comp_min": p - row["comp_min"],
            "price_vs_comp_mean": p - row["comp_mean"]
        })

    X = pd.DataFrame(feats)[feature_cols]
    preds = model.predict(X)
    preds = np.maximum(preds, 0)

    profits = []
    for p, v in zip(candidates, preds):
        if (p - row["cost"]) < config["min_margin"]:
            profits.append(-1e12)
        elif (p - row["comp_min"]) > config["max_vs_comp_min"]:
            profits.append(-1e12)
        else:
            profits.append((p - row["cost"]) * v)

    best = np.argmax(profits)
    return {
        "recommended_price": float(candidates[best]),
        "predicted_volume": float(preds[best]),
        "expected_profit": float(profits[best])
    }
