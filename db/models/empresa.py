from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    nit = Column(String)
    logo_url = Column(String)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    deleted = Column(Boolean, default=False)

    usuario = relationship("Usuario")