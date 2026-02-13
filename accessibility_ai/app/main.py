from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from . import utils
from . import models, schemas

from .database import get_db, engine, Base
from .utils import obtener_embedding_de_ollama


with engine.connect() as connection:
    connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    connection.commit()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="WCAG Auditor Api")

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Auditor de Accesibilidad con IA 🤖"}    

@app.post("/guidelines/")
async def create_update_guideline(guideline: schemas.GuidelineCreate, db: Session = Depends(get_db)):
    #Conexion con ollama

    vector = await utils.obtener_embedding_de_ollama(guideline.description)

    if vector is None:
        raise HTTPException(status_code=500, detail="Error al generar el vector")
    
    current_db_guideline = db.query(models.WCAGGuideline).filter(
        models.WCAGGuideline.success_criterion == guideline.success_criterion
    ).first()

    if current_db_guideline:
        current_db_guideline.description = guideline.description
        current_db_guideline.level = guideline.level
        current_db_guideline.embedding = vector
        msg = f"Criterio {guideline.success_criterion} actualizado."
    else:
        current_db_guideline = models.WCAGGuideline(
            success_criterion = guideline.success_criterion,
            description = guideline.description,
            level = guideline.level,
            embedding = vector
        )

        db.add(current_db_guideline)
        msg = f"Criterio {guideline.success_criterion} creado."
    
    db.commit()
    return{"status" : msg}

@app.get("/audit/")
async def audit_accessibility_issue(error_description: str, db: Session = Depends(get_db)):
    query_vector = await utils.obtener_embedding_de_ollama(error_description)

    TRESHOLD = 0.70

    if not query_vector:
        raise HTTPException(status_code=500, detail="No se pudo procesar la descripcion")
    
    #Realizamos busqueda por similitud de coseno
    query = text(""" 
        SELECT success_criterion, description, level,
                (1 - (embedding <=> :vector)) as similarity
        FROM wcag_guidelines
        WHERE (1 - (embedding <=> :vector)) >= :threshold
        ORDER BY similarity DESC
        LIMIT 3
    """)

    result = db.execute(query, {"vector": str(query_vector), "threshold": TRESHOLD})

    matches = [
        {
            "criterion": row[0],
            "description": row[1],
            "level": row[2],
            "similarity_score": round(row[3], 5)
        }
        for row in result
    ]

    return {
        "input_error": error_description,
        "results_found": len(matches),
        "suggested_guidelines": matches
    }
        