def get_by_id(db, auditoria_id, empresa_id):
    return db.query(Auditoria).filter(
        Auditoria.id == auditoria_id,
        Auditoria.empresa_id == empresa_id
    ).first()