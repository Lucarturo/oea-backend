from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Criterio(Base):
    __tablename__ = "criterios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    estado_id = Column(Integer, ForeignKey("estados.id"))