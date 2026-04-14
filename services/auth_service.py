from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

from db.models.usuario import Usuario
from db.models.rol import Rol
from core.security import create_access_token, create_refresh_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def registrar_usuario(db: Session, email: str, password: str):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    rol_admin = db.query(Rol).filter(Rol.nombre == "admin").first()

    nuevo = Usuario(
        email=email,
        password=hash_password(password),
        rol=rol_admin
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


def login_usuario(db: Session, email: str, password: str):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    return {
        "access_token": create_access_token({"sub": user.email}),
        "refresh_token": create_refresh_token({"sub": user.email}),
        "token_type": "bearer"
    }