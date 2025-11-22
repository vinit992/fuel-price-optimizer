import pathlib

# Path configuration
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR = OUTPUT_DIR / "model"
BACKTEST_DIR = OUTPUT_DIR / "backtests"
REPORT_DIR = OUTPUT_DIR / "reports"

# Create dirs if missing
for d in [OUTPUT_DIR, MODEL_DIR, BACKTEST_DIR, REPORT_DIR]:
    d.mkdir(exist_ok=True, parents=True)

# Optimization guardrails
OPT_CONFIG = {
    "max_daily_change": 2.0,
    "min_margin": 0.5,
    "max_vs_comp_min": 3.0,
    "grid_step": 0.2,
}
