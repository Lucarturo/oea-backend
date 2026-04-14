from pydantic import BaseModel


class EvaluacionCreate(BaseModel):
    auditoria_id: int
    numeral_id: int
    estado_id: int
    observacion: str | None = None
    