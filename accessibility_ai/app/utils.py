import os
import httpx

url_ollama = os.getenv("OLLAMA_URL", "http://ollama:11434/api/embeddings")

async def obtener_embedding_de_ollama(texto_a_convertir: str):
    
    datos = {"model": "nomic-embed-text", "prompt": texto_a_convertir}

    # Configuramos un tiempo de espera más largo (ej. 60 segundos)
    timeout = httpx.Timeout(60.0) 

    try:
        async with httpx.AsyncClient(timeout=timeout) as cliente:
            respuesta = await cliente.post(url_ollama, json=datos)
            respuesta.raise_for_status()
            return respuesta.json().get("embedding")
    except httpx.ReadTimeout:
        print("Error: Ollama tardó demasiado en responder.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None