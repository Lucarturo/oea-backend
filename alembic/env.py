import sys
import os

# 🔥 1. AJUSTAR RUTA (PRIMERO SIEMPRE)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# -------------------------------------

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 🔥 2. IMPORTS DESPUÉS DEL PATH
from db.base import Base
from db.session import DATABASE_URL

# 🔥 3. IMPORTAR MODELOS (OBLIGATORIO PARA ALEMBIC)
from db.models import empresa
from db.models import usuario
from db.models import auditoria
from db.models import estructura
from db.models import evaluacion
from db.models import estado
from db.models import criterio

# -------------------------------------

config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔥 4. CONFIGURAR BASE DE DATOS
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# 🔥 5. METADATA
target_metadata = Base.metadata

# -------------------------------------

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()

# -------------------------------------

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# -------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()