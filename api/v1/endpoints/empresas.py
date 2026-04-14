from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.empresa import EmpresaCreate, EmpresaResponse
from services.empresa_service import crear_empresa, listar_empresas, eliminar_empresa
from core.security import get_current_user, require_role

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmpresaResponse)
def crear(
    data: EmpresaCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role("admin"))
):
    return crear_empresa(db, data, user)


@router.get("/")
def listar(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return listar_empresas(db, user, skip, limit)


@router.delete("/{id}")
def eliminar(
    id: int,
    db: Session = Depends(get_db),
    user = Depends(require_role("admin"))
):
    return eliminar_empresa(db, id, user)