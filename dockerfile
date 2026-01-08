# ---- Base image (PINNED PYTHON VERSION) ----
FROM python:3.12-slim

# ---- Environment settings ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System dependencies (needed for bcrypt, asyncpg) ----
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# ---- Install Python dependencies ----
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY . .

# ---- Expose port (FastAPI default) ----
EXPOSE 8000

# ---- Run the app ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
