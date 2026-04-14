import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 URL de base de datos
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/oea_db"

# 🔥 Engine
engine = create_engine(DATABASE_URL)

# 🔥 Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔥 Base (ESTO ES LO QUE TE FALTABA)
Base = declarative_base()