from sqlalchemy.orm import Session, joinedload
from db.models.evaluacion import Evaluacion
from db.models.estado import Estado
from db.models.hallazgo import Hallazgo
from db.models.empresa import Empresa
from fastapi import HTTPException


def crear_evaluacion(db: Session, data):
    # 🔥 VALIDAR EMPRESA
    empresa = db.query(Empresa).filter(Empresa.id == data.empresa_id).first()

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no existe")

    evaluacion = Evaluacion(**data.dict())

    db.add(evaluacion)
    db.flush()

    estado = db.query(Estado).filter_by(id=data.estado_id).first()

    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")

    ESTADOS_CRITICOS = [6, 9, 12]
    ESTADOS_MEDIOS = [5, 8, 11]

    hallazgo_generado = False

    if estado.id in ESTADOS_CRITICOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="No cumple",
            severidad="Alta"
        )
        db.add(hallazgo)
        hallazgo_generado = True

    elif estado.id in ESTADOS_MEDIOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="Parcial",
            severidad="Media"
        )
        db.add(hallazgo)
        hallazgo_generado = True

    db.commit()
    db.refresh(evaluacion)

    return evaluacion, estado, hallazgo_generado


def listar_evaluaciones(db: Session):
    return (
        db.query(Evaluacion)
        .options(joinedload(Evaluacion.empresa))  # 🔥 AQUÍ
        .all()
    )


def obtener_evaluacion(db: Session, evaluacion_id: int):
    evaluacion = (
        db.query(Evaluacion)
        .options(joinedload(Evaluacion.empresa))
        .filter(Evaluacion.id == evaluacion_id)
        .first()
    )

    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")

    return evaluacion