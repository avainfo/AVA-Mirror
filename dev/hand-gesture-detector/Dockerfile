FROM python:3-slim
LABEL authors="anton"

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]