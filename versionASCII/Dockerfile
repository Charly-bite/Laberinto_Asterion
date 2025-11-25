FROM python:3.11-slim
WORKDIR /app

# Install minimal build deps
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the repository files
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=5000

CMD ["gunicorn", "webapp.app:app", "--bind", "0.0.0.0:5000", "--workers=1"]
