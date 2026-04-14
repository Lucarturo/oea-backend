from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# 🔥 IMPORTANTE: importa tu Base y engine
from database import Base, engine

# 👇 importa tus routers (ajusta según tu proyecto)
# from api.empresas import router as empresas_router
# from api.auth import router as auth_router

app = FastAPI(
    title="OEA Backend API",
    version="1.0.0"
)

# ✅ CORS (para frontend futuro)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción puedes restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 CREAR TABLAS AUTOMÁTICAMENTE
Base.metadata.create_all(bind=engine)


# ===============================
# 🟢 ENDPOINTS BÁSICOS
# ===============================

@app.get("/")
def root():
    return {"message": "API OEA funcionando 🚀"}


@app.get("/salud")
def salud():
    return {"status": "ok"}


# ===============================
# 🧩 INCLUIR ROUTERS
# ===============================

# 👉 descomenta cuando tengas tus routers
# app.include_router(empresas_router, prefix="/empresas", tags=["Empresas"])
# app.include_router(auth_router, prefix="/auth", tags=["Auth"])


# ===============================
# 🧠 DEBUG INFO (opcional)
# ===============================

@app.get("/debug-db")
def debug_db():
    database_url = os.getenv("DATABASE_URL")
    return {
        "database_url_detected": bool(database_url),
        "database_url_preview": database_url[:20] + "..." if database_url else None
    }