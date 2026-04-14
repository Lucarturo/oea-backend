from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 🔥 Base de datos simple (sin problemas)
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necesario para SQLite
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
