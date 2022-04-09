"""
This module contains the configuration class
"""
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
# from bot.enums import runmode
from bot.configuration.load_config import load_yaml_setting
from copy import deepcopy
from bot.configuration.process_options import Process_options

logger = logging.getLogger(__name__)

class Configuration(Process_options):
    """
    Class to read and init bot configuration
    Reuse this class for the bot, every script that required configuration
    """

    def get_config(self) -> Dict[str, Any]:
        """
        Return the config. Use this method to get the bot config
        :return: Dict: Bot config
        """
        logging.debug("Checking config whether exist")
        if self._config is None:
            self._config = self.load_config()

        # print(self._args)

        return self._config, self._yaml
        
        
    def load_config(self) -> Dict[str, Any]:

        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
            
            
        # Load all configs
        self._yaml = load_yaml_setting(self._args)
        configured = self._merge_args_yaml(self._args) 

        # self._process_logging_options(config)
        return configured

    def _merge_args_yaml(self, args:Dict[str,Any]) -> Dict[str, Any]:
        """
        The command permission is args > .env > config
        While cmd permission biggger than another one, override smaller one.
        """

        logging.debug('merge config and yaml')
        configured = deepcopy(args)
        self._process_logging_options(configured)
        self._process_sync_options(configured)
        
        
        return configured

        
