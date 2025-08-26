# Dockerfile para Python - fastapi
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python3", "main.py"]
