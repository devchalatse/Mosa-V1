# Dockerfile
FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy wait-for-it
COPY ./scripts/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

CMD ["./scripts/wait-for-it.sh", "giveflow_db:5432", "--timeout=30", "--strict", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
