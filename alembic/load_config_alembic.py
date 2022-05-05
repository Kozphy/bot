from bot.configuration.load_config import Load_config
import logging

logger = logging.getLogger(__name__)

class Load_config_alembic(Load_config):
    def determine_destination(self):
        logger.debug('Determine destination in alembic env')
        from bot
    def load_yaml_setting(self):
        logger.debug('Parse yaml file in alembic env')
        