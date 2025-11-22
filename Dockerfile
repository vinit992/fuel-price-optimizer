# ---- Base image ----
FROM ghcr.io/astral-sh/uv:python3.10-bookworm AS builder

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY fuel_price_optimizer.py .
COPY oil_retail_history.csv .
COPY today_example.json .

# Create environment + install dependencies
RUN uv sync --frozen

# ---- Runtime image ----
FROM ghcr.io/astral-sh/uv:python3.10-bookworm

WORKDIR /app

# Copy environment + app from builder stage
COPY --from=builder /app /app

# Default command (run pipeline)
CMD ["uv", "run", "python", "fuel_price_optimizer.py"]
