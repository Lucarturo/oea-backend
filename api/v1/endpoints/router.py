from fastapi import APIRouter

from api.v1.endpoints import (
    evaluaciones,
    hallazgos,
    auditorias,
    empresas,
    capitulos,
    estados,
    numerales
)

# 🔥 Router principal de la API v1
api_router = APIRouter()


# 🔥 REGISTRO DE ENDPOINTS

api_router.include_router(
    evaluaciones.router,
    prefix="/evaluaciones",
    tags=["Evaluaciones"]
)

api_router.include_router(
    hallazgos.router,
    prefix="/hallazgos",
    tags=["Hallazgos"]
)

api_router.include_router(
    auditorias.router,
    prefix="/auditorias",
    tags=["Auditorías"]
)

api_router.include_router(
    empresas.router,
    prefix="/empresas",
    tags=["Empresas"]
)

api_router.include_router(
    capitulos.router,
    prefix="/capitulos",
    tags=["Capítulos"]
)

api_router.include_router(
    estados.router,
    prefix="/estados",
    tags=["Estados"]
)

api_router.include_router(
    numerales.router,
    prefix="/numerales",
    tags=["Numerales"]
)

api_router.include_router(
    auth.router,
    prefix="/auth", 
    tags=["Auth"]
)