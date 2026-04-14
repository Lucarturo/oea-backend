from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.estado import Estado

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_estados(db: Session = Depends(get_db)):
    return db.query(Estado).all()