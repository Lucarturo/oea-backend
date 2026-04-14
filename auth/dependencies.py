from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# 🔐 Configuración JWT (debe coincidir con auth.py)
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

# 🔑 Swagger usa esto para autenticación
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ✅ Obtener usuario actual desde token
def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str = payload.get("sub")
        rol: str = payload.get("rol")

        if email is None or rol is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return {
            "email": email,
            "rol": rol
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


# 🔐 Verificación de roles (RBAC)
def require_role(required_roles: list):
    def role_checker(user=Depends(get_current_user)):

        if user["rol"] not in required_roles:
            raise HTTPException(status_code=403, detail="No autorizado")

        return user

    return role_checker