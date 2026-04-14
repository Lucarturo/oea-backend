import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 Obtener URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# 🔥 Validación (CRÍTICO en producción)
if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL no está definida en las variables de entorno")

# 🔥 Config especial para PostgreSQL en Render
connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# 🔥 Crear engine
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True  # evita errores de conexión dormida en Render
)

# 🔥 Sesión de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 🔥 Base de modelos
Base = declarative_base()