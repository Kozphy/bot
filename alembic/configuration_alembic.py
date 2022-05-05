from bot.configuration import Configuration
from bot.alembic.load_config_alembic import Load_config_alembic
from typing import Dict, Any
import logging
from copy import deepcopy

logger = logging.getLogger(__name__)

class Configuration_alembic(Configuration):
    def __init__(self):
        self.db_para = None

    def get_config(self) -> Dict[str, Any]:
        logger.debug("Checking alembic config whether exist in alembic env")
        if self.db_para is None:
            self.db_para = self.load_config()
        return self.db_para
        
    def load_config(self) -> Dict[str, Any]:
        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
        # Load all configs
        load = Load_config_alembic()
        yaml = load.load_yaml_setting()
        yaml_copy = deepcopy(yaml)
        db_para = self._process_persistece_options(yaml_copy)
        return db_para

    def _process_persistece_options(self, yaml):
        logger.debug("Processing persistence options in alembic env")
        # TODO: write another function for alembic autogenerate 
        persistence = yaml['persistence']
        db_para = {
            'db': persistence['db'],
            'user': persistence['user'],
            'password': persistence['password'],
            'host': persistence['host'],
            'dbname':persistence['name'],
            'port': persistence['port'],
        }
        return db_para