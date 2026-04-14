def get_by_auditoria(db, auditoria_id):
    return db.query(Evaluacion).options(
        joinedload(Evaluacion.estado)
    ).filter(Evaluacion.auditoria_id == auditoria_id).all()