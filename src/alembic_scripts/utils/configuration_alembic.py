from configuration import Configuration
from configuration.process_options import Process_options
from alembic_scripts.utils.load_config_alembic import Load_config_alembic
from typing import Dict, Any, Optional
from loguru import logger
from copy import deepcopy

from attrs import define, field

@define
class Configuration_alembic(Configuration):
 
    def load_config(self) -> Dict[str, Any]:
        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
        # Load all configs
        load = Load_config_alembic()
        destination = load.determine_destination()
        self.process._yaml = load.load_yaml_setting(destination)
        self.process._process_persistece_options()

    # def _process_persistece_options(self, yaml):
    #     logger.debug("Processing persistence options in alembic env")
    #     # TODO: write another function for alembic autogenerate 
    #     persistence = yaml['persistence']
    #     db_para = {
    #         'db': persistence['db'],
    #         'user': persistence['user'],
    #         'password': persistence['password'],
    #         'host': persistence['host'],
    #         'dbname':persistence['name'],
    #         'port': persistence['port'],
    #     }
    #     return db_para