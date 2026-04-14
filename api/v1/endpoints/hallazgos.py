from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.hallazgo import Hallazgo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/auditoria/{auditoria_id}")
def obtener_hallazgos(auditoria_id: int, db: Session = Depends(get_db)):
    return db.query(Hallazgo).join(
        Evaluacion, Hallazgo.evaluacion_id == Evaluacion.id
    ).filter(
        Evaluacion.auditoria_id == auditoria_id
    ).all()