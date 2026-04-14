from database import Base
from sqlalchemy import Column, Integer, String

class Capitulo(Base):
    __tablename__ = "capitulos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

