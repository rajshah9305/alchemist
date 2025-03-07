# setup/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY ai_engine /app/ai_engine
COPY backend /app/backend
COPY features /app/features
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY setup /app/setup

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]