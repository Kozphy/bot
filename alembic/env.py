# alembic
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from pathlib import Path
# context.config.set_main_option('prepend_sys_path', str(Path.cwd()))
import sys
sys.path.append(str(Path.cwd().parent))
# print(sys.path)
from bot.alembic.configuration_alembic import Configuration_alembic
from bot.persistence.migrations import setting_alembic_cfg
from bot.persistence.models import metadata_obj

# logger = logging.getLogger(__name__)
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [metadata_obj]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_db_url(autogenerate):
    print(vars(config))
    # exit()
    if autogenerate:
        c = Configuration_alembic()
        configured = c.get_config()
        config_persistence = configured['persistence']
        # print(config_persistence)
        _, url = setting_alembic_cfg(config_persistence)
        config.set_main_option('sqlalchemy.url', url)
        print(url)
    return None
    
def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    if hasattr(vars(config.cmd_opts), 'autogenerate'):
        autogenerate = vars(config.cmd_opts)['autogenerate']
        get_db_url(autogenerate)

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # url = get_configured_db()
    url = get_db_url()
    connectable = engine_from_config(
         config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
