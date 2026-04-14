from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.numeral import Numeral

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_numerales(db: Session = Depends(get_db)):
    return db.query(Numeral).all()