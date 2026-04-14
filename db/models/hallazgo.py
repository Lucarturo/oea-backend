from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base
from db.models.evaluacion import Evaluacion  # 🔥 IMPORT DIRECTO


class Hallazgo(Base):
    __tablename__ = "hallazgos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

    evaluacion_id = Column(Integer, ForeignKey("evaluaciones.id"))

    evaluacion = relationship(
        Evaluacion,  # 🔥 USAR CLASE, NO STRING
        backref="hallazgos"
    )