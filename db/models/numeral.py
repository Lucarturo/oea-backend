from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Numeral(Base):
    __tablename__ = "numerales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    capitulo_id = Column(Integer, ForeignKey("capitulos.id"))

    capitulo = relationship("Capitulo")