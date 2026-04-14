from pydantic import BaseModel


class EmpresaSimple(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True


class EvaluacionSimple(BaseModel):
    id: int
    score: int

    class Config:
        from_attributes = True

class EvaluacionSimple(BaseModel):
    id: int
    observacion: str | None = None