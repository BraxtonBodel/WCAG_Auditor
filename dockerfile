# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para pgvector/psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiamos e instalamos requerimientos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido del proyecto (incluyendo accessibility_ai)
COPY . .

# Comando para ejecutar la aplicación
# Nota: Ajustamos el path al main.py según tu estructura
CMD ["uvicorn", "accessibility_ai.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]