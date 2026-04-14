from db.models.auditoria import Auditoria


def registrar_log(db, user, accion, tabla):
    log = Auditoria(
        usuario_email=user.email,
        accion=accion,
        tabla=tabla
    )
    db.add(log)
    db.commit()