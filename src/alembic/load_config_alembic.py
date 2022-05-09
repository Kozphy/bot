from bot.configuration.load_config import Load_config
from bot.src.exceptions import OperationalException
import logging
try:
    from yaml import CLoader as Loader, CSafeLoader as CSLoader, CDumper as Dumper
except:
    from yaml import Loader, Dumper


logger = logging.getLogger(__name__)

class Load_config_alembic(Load_config):
    def determine_destination(self):
        logger.debug('Determine destination in alembic env')
        from bot.src.constants import (USERDATA_DIR_alembic_autogenerate,
        DEFAULT_CONFIG_DIR_NAME, DEFAULT_CONFIG_NAME)
        user_dir = USERDATA_DIR_alembic_autogenerate
        config_dir_name = DEFAULT_CONFIG_DIR_NAME
        config_name = DEFAULT_CONFIG_NAME

        destination = f"{user_dir}/{config_dir_name}/{config_name}"
        return destination 

    def load_yaml_setting(self):
        logger.debug('Parse yaml file in alembic env')
        destination = self.determine_destination()

        try:
            with open(destination, 'r') as f:
                yaml = CSLoader(stream=f).get_data()
            return yaml
        except FileNotFoundError as e:
            logger.error(e)
            raise OperationalException(f"file {destination} not found")



        