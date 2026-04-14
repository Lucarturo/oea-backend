from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.base import Base


class Auditoria(Base):
    __tablename__ = "auditorias"

    id = Column(Integer, primary_key=True)
    usuario_email = Column(String)
    accion = Column(String)
    tabla = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)