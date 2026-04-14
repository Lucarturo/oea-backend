from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.capitulo import Capitulo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_capitulos(db: Session = Depends(get_db)):
    return db.query(Capitulo).all()