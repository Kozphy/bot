from configuration.load_config import Load_config
from exceptions import OperationalException
try:
    from yaml import CLoader as Loader, CSafeLoader as CSLoader, CDumper as Dumper
except:
    from yaml import Loader, Dumper
from loguru import logger



class Load_config_alembic(Load_config):
    def determine_destination(self):
        logger.debug('Determine destination in alembic env')
        from alembic_scripts.utils.constants import (USERDATA_DIR_alembic_cli,
        DEFAULT_CONFIG_DIR_NAME, DEFAULT_CONFIG_NAME)
        user_dir = USERDATA_DIR_alembic_cli
        config_dir_name = DEFAULT_CONFIG_DIR_NAME
        config_name = DEFAULT_CONFIG_NAME

        destination = f"{user_dir}/{config_dir_name}/{config_name}"
        return destination 




        