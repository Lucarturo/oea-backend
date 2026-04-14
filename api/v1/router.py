from fastapi import APIRouter

from api.v1.endpoints import empresas
from api.v1.endpoints import evaluaciones
from api.v1.endpoints import auth  # 🔥 IMPORTANTE

api_router = APIRouter()

# 🔹 Empresas
api_router.include_router(empresas.router, prefix="/empresas", tags=["Empresas"])

# 🔹 Evaluaciones
api_router.include_router(evaluaciones.router, prefix="/evaluaciones", tags=["Evaluaciones"])

# 🔥 Auth (LO QUE TE FALTA)
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])