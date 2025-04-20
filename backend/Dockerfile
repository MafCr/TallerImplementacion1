FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema para SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt antes del código para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

ENV PYTHONPATH=/app
CMD ["python", "-m", "app.main"]