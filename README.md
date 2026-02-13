# WCAG Accessibility AI Auditor

Este proyecto es una herramienta de auditoría de accesibilidad web impulsada por Inteligencia Artificial. Utiliza **Búsqueda Semántica** y **Vectores de Características (Embeddings)** para relacionar reportes de errores en lenguaje natural con los criterios de éxito oficiales de las **WCAG 2.2** (Web Content Accessibility Guidelines).

## Propósito del Proyecto
El sistema permite que equipos tecnológicos auditen su cumplimiento con normas de accesibilidad de manera automática. A diferencia de las búsquedas tradicionales por palabras clave, esta solución emplea **IA** para entender la intención semántica, permitiendo encontrar criterios relevantes incluso cuando el reporte no utiliza terminología técnica exacta.

## Stack Tecnológico Completo

La arquitectura se basa en un ecosistema de microservicios y bases de datos vectoriales optimizado para el rendimiento:

### Backend & AI
* **Lenguaje:** Python 3.14.3 (Configurado para evitar conflictos con la versión del sistema en macOS).
* **Framework API:** FastAPI (Implementación asíncrona para alta concurrencia).
* **Motor de IA:** Ollama (Desplegado localmente para privacidad y baja latencia).
* **Modelo de Embeddings:** `nomic-embed-text` (Optimizado para recuperación de texto).
* **ORM:** SQLAlchemy.

### Base de Datos & Almacenamiento
* **Base de Datos:** PostgreSQL 16.
* **Extensión Vectorial:** `pgvector` (Almacenamiento de embeddings de 768 dimensiones y cálculo de similitud de cosenos).

### Infraestructura & Herramientas
* **Contenedores:** Docker & Docker Compose (Orquestación de API, DB y Ollama).
* **Arquitectura:** Darwin/arm64 (Optimizado para chips Apple Silicon).
* **Gestión de Entorno:** Python venv para aislamiento de dependencias.



## Características Principales

* **Ingesta de Lineamientos Oficiales:** Procesamiento de criterios WCAG reales y generación de vectores semánticos mediante el endpoint `/guidelines/`.
* **Búsqueda Semántica de Errores:** Recuperación de pautas mediante comparación matemática de vectores en lugar de coincidencias de texto exactas.
* **Filtrado de Calidad (Thresholding):** Lógica implementada a nivel de SQL para descartar sugerencias con una similitud inferior al **0.70**, reduciendo falsos positivos.
* **Validación de Datos:** Uso de esquemas Pydantic para asegurar la integridad de la información en cada transacción.

## Configuración y Ejecución

### Pasos Iniciales
1. **Levantar Infraestructura:**
   ```bash
   docker-compose up -d