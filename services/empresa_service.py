from sqlalchemy.orm import Session
from db.models.empresa import Empresa
from services.auditoria_service import registrar_log


def crear_empresa(db: Session, data, user):
    nueva = Empresa(
        nombre=data.nombre,
        nit=data.nit,
        logo_url=data.logo_url,
        usuario_id=user.id
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    registrar_log(db, user, "CREATE", "empresas")

    return nueva


def listar_empresas(db: Session, user, skip: int, limit: int):
    return db.query(Empresa)\
        .filter(Empresa.usuario_id == user.id)\
        .filter(Empresa.deleted == False)\
        .offset(skip)\
        .limit(limit)\
        .all()


def eliminar_empresa(db: Session, id: int, user):
    empresa = db.query(Empresa).filter(Empresa.id == id).first()

    empresa.deleted = True
    db.commit()

    registrar_log(db, user, "DELETE", "empresas")

    return empresa