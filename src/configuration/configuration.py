"""
This module contains the configuration class
"""
from loguru import logger
from pathlib import Path
from typing import Any, Dict, List, Optional
from configuration.load_config import Load_config
from copy import deepcopy
from configuration.process_options import Process_options


class Configuration(Process_options):
    """
    Class to read and init bot configuration
    Reuse this class for the bot, every script that required configuration
    """
    def __init__(self, args):
        super().__init__(args)

    def get_config(self) -> Dict[str, Any]:
        """
        Return the config. Use this method to get the bot config
        :return: Dict: Bot config
        """
        logger.debug("Checking config whether exist")
        if self._config is None:
            self._config = self.load_config()

        return self._config, self._yaml
        
        
    def load_config(self) -> Dict[str, Any]:

        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
            
        # Load all configs
        load = Load_config()
        self._yaml = load.load_yaml_setting(self._args)
        configured = self._merge_args_yaml(self._args) 

        return configured

    def _merge_args_yaml(self, args:Dict[str,Any]) -> Dict[str, Any]:
        """
        The command permission is args > .env > config
        While cmd permission biggger than another one, override smaller one.
        """

        logger.debug('merge config and yaml')
        configured = deepcopy(args)
        self._process_logging_options(configured)
        self._process_api(configured)
        self._process_sync_options(configured)
        self._process_exchange_options(configured)
        self._process_persistece_options(configured)
        
        
        return configured

        
