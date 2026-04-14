from sqlalchemy import Column, Integer, String
from database import Base

class Estado(Base):
    __tablename__ = "estados"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    valor = Column(Integer)