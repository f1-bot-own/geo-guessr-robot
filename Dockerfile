FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (ca-certificates for SSL, curl)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Ensure data and mount directories exist for database / cache storage
RUN mkdir -p /app/data /data && chmod -R 777 /app/data /data

# Expose port for Telegram Mini App web server
EXPOSE 8080

# Launch Telegram bot polling and embedded web server
CMD ["python", "main.py"]
