from bot.configuration import Configuration
from bot.alembic.load_config_alembic import load_yaml_setting
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class Configuration_alembic(Configuration):
    def __init__(self):
        self._yaml = None

    def get_config(self) -> Dict[str, Any]:
        logger.debug("Checking alembic config whether exist")
        if self._yaml is None:
            self._yaml = self.load_config()

        
    def load_config(self) -> Dict[str, Any]:
        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
        # Load all configs
        self._yaml = load_yaml_setting()
        return self._yaml

    def _process_persistece_options(self, yaml):
        logger.debug("Processing alembic persistence options")
        # TODO: write another function for alembic autogenerate 
        db_para = {
            'db': yaml['db'],
            'user': yaml['user'],
            'password': yaml['password'],
            'host': yaml['host'],
            'dbname':yaml['name'],
            'port': yaml['port'],
        }