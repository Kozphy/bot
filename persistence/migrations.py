import logging
from tabnanny import verbose
# alembic
from bot.constants import ALEMBIC_CONFIG_FILE
from alembic.config import Config
from alembic import command, script
from alembic.runtime import migration
from sqlalchemy import engine
from sqlalchemy_utils.functions import create_database, database_exists

logger = logging.getLogger(__name__)

support_databases = {
    'MYSQL': "mysql+mysqldb://"
}

support_ssl = ['MYSQL']

def setting_alembic_cfg(configured):
    logger.debug("Setting alembic env")
    print(configured)
    db_para = {
            'db': configured['db'],
            'user': configured['db_user'],
            'password': configured['db_password'],
            'host': configured['db_host'],
            'dbname':configured['db_name'],
            'port': configured['db_port'],
        }

    url = init_db_url(**db_para)
    # print(url)
    alembic_cfg = Config(ALEMBIC_CONFIG_FILE)
    # print(vars(alembic_cfg.file_config))
    alembic_cfg.set_main_option("script_location", "./bot/alembic")
    alembic_cfg.set_main_option("sqlalchemy.url", url)
    return alembic_cfg, url


def init_db_url(db, user, password, host, dbname, port, charset="utf8mb4", ssl=False, echo=True, future=True) -> str:
    db = db.upper()

    if db not in support_databases:
        raise Exception("Database not supported")
    db_url = f"{support_databases[db]}{user}:{password}@{host}:{port}/{dbname}?charset={charset}"

    return db_url
    
def migrations_update(configured, revision='head'):
    alem_config, url = setting_alembic_cfg(configured)
    if database_exists(url) == False:
        create_database(url)
        command.upgrade(alem_config, revision)
    # check revirsion whether is head
    if check_current_head(alem_config, engine.create_engine(url)) == False:
        command.upgrade(alem_config, revision)
    
    # command.history(alem_config, verbose=True)

def migrations_downgrade(configured, revision='base'):
    alem_config, _ = setting_alembic_cfg(configured)
    command.downgrade(alem_config, revision)
    
def migration_show_history(configured, rev_range='base:current', verbose='True'):
    alem_config, _ = setting_alembic_cfg(configured)
    command.history(alem_config, verbose=verbose)

def migration_revision(configured, message='', autogenerate='True'):
    alem_config, _ = setting_alembic_cfg(configured)
    command.revision(alem_config, message=message, autogenerate=autogenerate)

def check_current_head(alembic_cfg, connectable):
    # type: (Config, engine.Engine) -> bool
    directory = script.ScriptDirectory.from_config(alembic_cfg)
    with connectable.begin() as connection:
        context = migration.MigrationContext.configure(connection)
        return set(context.get_current_heads()) == set(directory.get_heads())