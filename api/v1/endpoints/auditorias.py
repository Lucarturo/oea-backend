from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.auditoria import Auditoria

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_auditorias(db: Session = Depends(get_db)):
    return db.query(Auditoria).all()


@router.get("/{id}")
def obtener_auditoria(id: int, db: Session = Depends(get_db)):
    return db.query(Auditoria).filter(Auditoria.id == id).first()