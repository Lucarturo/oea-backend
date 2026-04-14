from pydantic import BaseModel
from typing import Optional


class EmpresaCreate(BaseModel):
    nombre: str
    nit: str
    logo_url: Optional[str]


class EmpresaResponse(BaseModel):
    id: int
    nombre: str
    nit: str
    logo_url: Optional[str]

    class Config:
        from_attributes = True