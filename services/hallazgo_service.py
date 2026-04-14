from db.models.hallazgo import Hallazgo

ESTADOS_CRITICOS = [6, 9, 12]
ESTADOS_MEDIOS = [5, 8, 11]


def generar_hallazgo(db, evaluacion, estado):

    if estado.id in ESTADOS_CRITICOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="No cumple",
            severidad="Alta"
        )
        db.add(hallazgo)
        return True

    elif estado.id in ESTADOS_MEDIOS:
        hallazgo = Hallazgo(
            evaluacion_id=evaluacion.id,
            tipo="Parcial",
            severidad="Media"
        )
        db.add(hallazgo)
        return True

    return False