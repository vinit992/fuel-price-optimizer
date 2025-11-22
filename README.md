# fuel-price-optimizer

# Fuel Price Optimization — Machine Learning System

## 🎯 Objective
Predict daily fuel demand and recommend the optimal daily retail price that maximizes profit, subject to business constraints.

Profit = (price - cost) × predicted_volume

---

## 🚀 Features
- Full data pipeline (ingestion → cleaning → features)
- RandomForest-based demand prediction
- Grid-search price optimization with business guardrails:
  - Max daily price change
  - Minimum margin enforcement
  - Competitor alignment
- Automatic summary report generator (PDF/markdown)
- Dockerized runtime
- Works with uv (ultra-fast Python environment manager)

---

## 📦 Project Structure
