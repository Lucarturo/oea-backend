from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from db.models.evaluacion import Evaluacion
from db.models.estado import Estado
from db.models.hallazgo import Hallazgo
from schemas.evaluacion import EvaluacionCreate

router = APIRouter(prefix="/evaluacion", tags=["Evaluación"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/evaluar")
def evaluar(data: EvaluacionCreate, db: Session = Depends(get_db)):

    # ✅ Crear evaluación
    evaluacion = Evaluacion(
        auditoria_id=data.auditoria_id,
        numeral_id=data.numeral_id,
        estado_id=data.estado_id,
        observacion=data.observacion
    )

    db.add(evaluacion)
    db.flush()  # 👈 obtenemos ID sin commit

    # ✅ Obtener estado
    estado = db.query(Estado).filter_by(id=data.estado_id).first()

    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")

    # 🔍 DEBUG (puedes quitar luego)
    print("====== DEBUG ======")
    print("Estado ID:", estado.id)
    print("Estado Nombre:", estado.nombre)

    # 🔥 MAPEO REAL SEGÚN TU BD
    ESTADOS_CRITICOS = [6, 9, 12]
    ESTADOS_MEDIOS = [5, 8, 11]

    print("Crítico:", estado.id in ESTADOS_CRITICOS)
    print("Medio:", estado.id in ESTADOS_MEDIOS)
    print("===================")

    # ✅ Generación de hallazgos
    if estado.id in ESTADOS_CRITICOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="No cumple",
            severidad="Alta"
        )
        db.add(hallazgo)

    elif estado.id in ESTADOS_MEDIOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="Parcial",
            severidad="Media"
        )
        db.add(hallazgo)

    # ✅ Guardar todo
    db.commit()

    return {
    "mensaje": "Evaluación creada correctamente",
    "estado": estado.nombre,
    "hallazgo_generado": estado.id in (ESTADOS_CRITICOS + ESTADOS_MEDIOS)
}