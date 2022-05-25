"""
This module contains the configuration class
"""
from loguru import logger
from pathlib import Path
from typing import Any, Dict, List, Optional
from copy import deepcopy
from configuration.process_options import Process_options

from attrs import define

@define
class Configuration:
    """
    Class to read and init bot configuration
    Reuse this class for the bot, every script that required configuration
    """
    process: Process_options


    @classmethod
    def from_options(cls, args: Dict[str, Any]):
        return cls(
            process = Process_options.from_args(args),
        )

    def get_config(self) -> Dict[str, Any]:
        """
        Return the config. Use this method to get the bot config
        :return: Dict: Bot config
        """
        logger.debug("Checking configured whether exist")
        if len(self.process.configured) == 0:
            self.load_config()

        return self.process.configured
    
        
    def load_config(self) -> Dict[str, Any]:

        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
            
        # Load all configs
        self.process.load_yaml()
        self._merge_args_yaml() 

    def _merge_args_yaml(self):
        """
        The command permission is args > .env > config
        While cmd permission biggger than another one, override smaller one.
        """

        logger.debug('merge config and yaml')

        # exit()
        self.process._process_logging_options()
        self.process._process_common()
        self.process._process_api()
        self.process._process_sync_options()
        self.process._process_exchange_options()
        self.process._process_persistece_options()
        

        
