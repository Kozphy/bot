# alembic
from loguru import logger
from constants import ALEMBIC_CONFIG_FILE
from alembic.config import Config
from alembic import command, script
from alembic.runtime import migration

from sqlalchemy import engine
from sqlalchemy_utils.functions import create_database, database_exists


support_databases = {
    'MYSQL': "mysql+mysqldb://"
}

support_ssl = ['MYSQL']

def setting_alembic_cfg(configured):
    logger.debug("Setting alembic context env")
    db_para = {}
    for (key, value) in configured['persistence'].items():
        if key == 'name':
            db_para.update({'dbname': value})
            continue
        if key not in ['ORM', 'path']:
            db_para.update({key: value})


    url = init_db_url(**db_para)
    alembic_cfg = Config(ALEMBIC_CONFIG_FILE)
    alembic_cfg.set_main_option("script_location", "./src/alembic_scripts")
    alembic_cfg.set_main_option("sqlalchemy.url", url)
    logger.debug(f"db url is {url}")
    return alembic_cfg, url, configured['persistence']['name']


def init_db_url(db, user, password, host, dbname, port, charset="utf8mb4", ssl=False, echo=True, future=True) -> str:
    db = db.upper()

    if db not in support_databases:
        raise Exception("Database not supported")
    db_url = f"{support_databases[db]}{user}:{password}@{host}:{port}/{dbname}?charset={charset}"

    return db_url
    
def migration_upgrade(configured, revision, sql=None, tag=None):
    alem_config, url, db_name = setting_alembic_cfg(configured)
    if database_exists(url) == False:
        logger.debug(f'{db_name} database not exists, create it')
        create_database(url)
        command.upgrade(alem_config, revision, sql, tag)
    # check revirsion whether is head
    if check_current_head(alem_config, engine.create_engine(url)) == False:
        logger.debug(f'upgrade {db_name} database schema')
        command.upgrade(alem_config, revision, sql, tag)
    
    # command.history(alem_config, verbose=True)

# TODO: implement alembic downgrade in cmd with bot config
def migration_downgrade(configured, revision='base'):
    alem_config, _, db_name = setting_alembic_cfg(configured)
    logger.debug(f'downgrade {db_name} database schema')
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