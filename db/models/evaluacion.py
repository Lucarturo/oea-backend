from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.base import Base


class Evaluacion(Base):
    __tablename__ = "evaluaciones"  # 🔥 CORRECTO

    id = Column(Integer, primary_key=True, index=True)
    auditoria_id = Column(Integer)
    numeral_id = Column(Integer)
    estado_id = Column(Integer)
    observacion = Column(String)
    created_at = Column(DateTime)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))  # 🔥 FIX AQUÍ

    empresa = relationship(
        "Empresa",
        back_populates="evaluaciones"
    )