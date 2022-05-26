# alembic
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from pathlib import Path

from alembic_scripts.utils.configuration_alembic import Configuration_alembic
from persistence.migrations import init_db_url
from persistence.mysql.kline import exchanges_meta
from persistence.mysql.kucoin_kline import kucoin_kline_meta
from loguru import logger

## temporarily, stop reflection bbgo database to currently use database
# from persistence.mysql.bbgo_db_reflect import bbgo_db_meta

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [exchanges_meta]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_db_url():
    execute_ph = str(Path.cwd()).split('/')[-1]
    ## if not programmatically execute
    if execute_ph == 'src':
        c = Configuration_alembic.from_options()
        configured = c.get_config()
        url = init_db_url(**configured['persistence'])
        config.set_main_option('sqlalchemy.url', url)
        logger.debug(f"db url is {url}")
        # print('In autogenerate mode url is: ' + url)
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
    connectable = config.attributes.get('connection', None)
    
    if connectable is None:
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
    else:
        context.configure(
            connection=connectable,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()
        
# change getting db_url process in cmd mode
get_db_url()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
