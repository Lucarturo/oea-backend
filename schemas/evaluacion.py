from pydantic import BaseModel
from datetime import datetime
from schemas.base import EmpresaSimple


# 🔹 CREATE
class EvaluacionCreate(BaseModel):
    auditoria_id: int
    numeral_id: int
    estado_id: int
    observacion: str
    empresa_id: int


# 🔹 RESPONSE
class EvaluacionResponse(BaseModel):
    id: int
    auditoria_id: int
    numeral_id: int
    estado_id: int
    observacion: str
    created_at: datetime

    empresa: EmpresaSimple

    class Config:
        from_attributes = True


# 🔹 SIMPLE
class EvaluacionSimple(BaseModel):
    id: int
    observacion: str | None = None

    class Config:
        from_attributes = True