from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.evaluacion import EvaluacionCreate, EvaluacionResponse
from services.evaluacion_service import (
    crear_evaluacion,
    listar_evaluaciones,
    obtener_evaluacion
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EvaluacionResponse)
def crear(data: EvaluacionCreate, db: Session = Depends(get_db)):
    evaluacion, estado, hallazgo = crear_evaluacion(db, data)
    return evaluacion


@router.get("/", response_model=list[EvaluacionResponse])
def listar(db: Session = Depends(get_db)):
    return listar_evaluaciones(db)


@router.get("/{id}", response_model=EvaluacionResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return obtener_evaluacion(db, id)