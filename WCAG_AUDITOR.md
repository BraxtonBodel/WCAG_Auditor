# 🗺️ Roadmap: WCAG AI-Auditor Pro
**De Full Stack Developer a AI Engineer**

Este plan maestro detalla la evolución técnica para transformar el motor de búsqueda vectorial actual en una plataforma SaaS escalable para el sector Ecommerce.

---

## 🛠️ Stack Tecnológico Consolidado

| Capa | Herramientas |
| :--- | :--- |
| **Frontend** | **Next.js 15** + **Shadcn UI** (Tailwind CSS) |
| **Backend** | Python 3.14 + FastAPI |
| **AI Orchestration** | **LangChain** |
| **Modelos (LLM/Embed)** | Ollama (nomic-embed-text, llama3) |
| **Vector Database** | PostgreSQL + pgvector (**Supabase** para Cloud) |
| **Scraping** | BeautifulSoup4 / Playwright |
| **Deployment** | **Vercel** (Frontend) + Docker (Backend/Ollama) |

---

## 🚀 Fases de Desarrollo

### Fase 1: El Motor de Inteligencia (Completada ✅)
**Objetivo:** Consolidar la precisión de la búsqueda semántica local.
- **Feature:** Auditoría mediante lenguaje natural (Texto -> Criterio).
- **Logros:**
  - Base de datos poblada con 15 criterios oficiales WCAG 2.2.
  - Filtro de precisión con **Threshold de 0.70** para evitar ruido.
  - Generación de embeddings locales con Ollama.



### Fase 2: Ingesta de Código Real (Scraping Quirúrgico)
**Objetivo:** Pasar de descripciones manuales a auditorías de HTML vivo.
- **Feature:** `POST /audit/url/`. Extracción automática de componentes críticos de tiendas online.
- **Tareas:**
  - Implementar un **Scraper Quirúrgico** que extraiga solo elementos semánticos relevantes: `<nav>`, `<form>`, `<img>`, `<button>`.
  - "Limpieza de Ruido": Eliminar clases CSS dinámicas y scripts para no saturar el contexto de la IA.

### Fase 3: Generación de Soluciones (RAG con LangChain)
**Objetivo:** No solo identificar el error, sino proveer la solución técnica.
- **Feature:** "AI Fix Recommendations" con snippets de código.
- **Tareas:**
  - Implementar arquitectura **RAG (Retrieval-Augmented Generation)** usando **LangChain**.
  - Usar un LLM (Llama 3) para redactar explicaciones técnicas y corregir el HTML extraído.



### Fase 4: Escalabilidad, UI y Despliegue (Cloud & UX)
**Objetivo:** Convertir el proyecto en una herramienta visual y profesional.
- **Frontend Pro:** Construir un dashboard moderno usando **Shadcn UI** para mostrar tarjetas de error y comparativas de código.
- **Persistencia Cloud:** Migrar de PostgreSQL local a **Supabase** para manejar usuarios y auditorías históricas.
- **Deployment:** Desplegar el frontend en **Vercel** con CI/CD automatizado desde GitHub.

---

## 🎯 Producto Final: "Accessibility Lens"
Un consultor de accesibilidad automatizado que permite a desarrolladores:
1. **Escanear URLs:** Análisis instantáneo de páginas de producto o procesos de checkout.
2. **Visualizar Fallos:** Interfaz limpia en Shadcn que resalta los errores detectados en el DOM.
3. **Aplicar Fixes:** Copiar directamente el código corregido por la IA para cumplir con WCAG.

---

## 📈 KPIs de Transición (Habilidades a Masterizar)
* [ ] Dominio de **Vector Ops** y optimización de búsqueda semántica.
* [ ] Orquestación de agentes y cadenas con **LangChain**.
* [ ] Procesamiento de datos no estructurados (**Web Scraping** y limpieza de HTML).
* [ ] Implementación de interfaces de alta calidad con **Shadcn UI** y **Next.js**.

---

## 🏗️ Metodología de Trabajo: "Code & Explain"

Nuestro proceso de construcción prioriza el aprendizaje profundo sobre la velocidad de implementación.

1. **Construcción Manual:** El usuario escribe el código. El Asistente **NO** genera código automáticamente ni reescribe bloques enteros.
2. **Análisis Line-by-Line:** Antes de avanzar, el Asistente disecciona el código escrito por el usuario, explicando:
   - **Sintaxis:** ¿Por qué se escribe así en Python?
   - **Lógica:** ¿Qué está haciendo el programa en ese punto?
   - **Contexto:** ¿Por qué usamos esta librería o patrón específico?
3. **Iteración Guiada:** Solo se avanza al siguiente bloque cuando el actual ha sido completamente comprendido y funciona correctamente.