"""
This module contains the configuration class
"""
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from bot.enums import runmode
from bot.configuration.load_config import load_yaml_setting

logger = logging.getLogger(__name__)

class Configuration:
    """
    Class to read and init bot configuration
    Reuse this class for the bot, every script that required configuration
    """

    def __init__(self, args: Dict[str, Any], runmode = None):
        self.args = args
        self.config: Optional[Dict[str,Any]] = None
        self.runmode = runmode
    
    def get_config(self) -> Dict[str, Any]:
        """
        Return the config. Use this method to get the bot config
        :return: Dict: Bot config
        """
        logging.debug("Checking config whether exist")
        if self.config is None:
            self.config = self.load_config()

        return self.config
    def load_from_files(self, files: List[str]) -> Dict[str, Any]:
        config: Dict[str, Any] = {}
        
        
    def load_config(self, config: Dict[str, Any]) -> Dict[str, Any]:

        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
        # Load all configs
        config = self.load_yaml_setting(self.args.get("config", []))
    
    def _process_common_options(self, config: Dict[str, Any]) -> None:
        