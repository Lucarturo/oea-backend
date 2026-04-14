from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from api.v1.router import api_router

# 🔥 IMPORTAR TODOS LOS MODELOS (UNA SOLA VEZ)
import db.models

app = FastAPI(
    title="OEA Backend",
    version="1.0.0"
)

# 🌐 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ en producción restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔗 ROUTES
app.include_router(api_router, prefix="/api/v1")

# 🗄️ CREAR TABLAS (solo en desarrollo)
Base.metadata.create_all(bind=engine)


# ❤️ HEALTH CHECK
@app.get("/")
def home():
    return {
        "status": "ok",
        "service": "OEA Backend",
        "version": "v1",
        "docs": "/docs"
    }