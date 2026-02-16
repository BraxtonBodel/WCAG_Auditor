from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from . import utils
from . import models, schemas
from typing import List, Optional

from .database import get_db, engine, Base
from .utils import obtener_embedding_de_ollama
from .scraper import extract_html_content, AccessibilityIssue


@app.on_event("startup")
def startup_db_client():
    try:
        with engine.connect() as connection:
            connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            connection.commit()

        models.Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente.")
    
    except Exception as e:
        print(f"Advertencia: No se pudo conectar a la base de datos: {e}")

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

@app.post("/audit/url")
async def audit_url_accessibility(url: str, db: Session = Depends(get_db)):
    issues = extract_html_content(url)

    results_found = []

    for issue in issues:
        query_vector = await utils.obtener_embedding_de_ollama(issue.issue_description)

        wcag_info = None
        if query_vector:
            query = text(""" 
                SELECT success_criterion, description, level,
                        (1 - (embedding <=> :vector)) as similarity
                FROM wcag_guidelines
                WHERE (1 - (embedding <=> :vector)) >= 0.70
                ORDER BY similarity DESC
                LIMIT 1
            """)

            match = db.execute(query, {"vector" : str(query_vector)}).fetchone()

            if match:
                wcag_info = {
                    "criterion" : match[0],
                    "description": match[1],
                    "level": match[2]
                }
        
        results_found.append({
            "element": issue.html_content,
            "issue": issue.issue_description,
            "suggestion": issue.suggested_fix,
            "wcag_match": wcag_info
        })
    
    return {
        "url": url,
        "total_issues": len(results_found),
        "audit_results" : results_found
    }

@app.get("/guidelines/", response_model=List[schemas.GuidelineResponse])
def get_guidelines(db: Session = Depends(get_db)):
    return db.query(models.WCAGGuideline).all()