from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from database import SessionLocal
from schemas.auth import UsuarioCreate, UsuarioResponse, Token
from services.auth_service import registrar_usuario, login_usuario
from core.security import create_access_token, create_refresh_token, SECRET_KEY, ALGORITHM

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/registro", response_model=UsuarioResponse)
def registro(data: UsuarioCreate, db: Session = Depends(get_db)):
    return registrar_usuario(db, data.email, data.password)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_usuario(db, form_data.username, form_data.password)


@router.post("/refresh", response_model=Token)
def refresh(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")

    return {
        "access_token": create_access_token({"sub": email}),
        "refresh_token": create_refresh_token({"sub": email}),
        "token_type": "bearer"
    }