"""
This module contains the configuration class
"""
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from bot.enums import runmode
from bot.configuration.load_config import load_yaml_setting
from bot.constants import BOT_DIR, DEFAULT_USERDATA_DIR, DEFAULT_LOG_FILE_DIR
from bot.loggers import setup_logging
from copy import deepcopy
from bot.configuration.merge import per_args, per_config, per_default
from .misc import check_folder

logger = logging.getLogger(__name__)

class Configuration:
    """
    Class to read and init bot configuration
    Reuse this class for the bot, every script that required configuration
    """

    def __init__(self, args: Optional[Dict[str, Any]], config: Dict[str, Any] = None, runmode = None):
        self.args: Optional[Dict[str, Any]] = args
        self.config: Optional[Dict[str, Any]] = None
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

    # def load_from_files(self, files: List[str]) -> Dict[str, Any]:
    #     config: Dict[str, Any] = {}
        
        
    def load_config(self) -> Dict[str, Any]:

        """
        Extract information from sys.argv and load the bot configuration
        :return: Configuration dictionary
        """    
            
            
        # Load all configs
        yaml = load_yaml_setting(self.args)
        config = self._merge_args_yaml(self.args, yaml)
        

        # self._process_logging_options(config)

    def _merge_args_yaml(self, args:Dict[str,Any], yaml: Optional[Dict[str,Any]]) -> Dict[str, Any]:
        """
        The command permission is args > .env > config
        While cmd permission biggger than another one, override smaller one.
        """

        logging.debug('merge config and yaml')
        configured = deepcopy(args)
        self._process_logging_options(configured, yaml)
        # self._process_datadir_options(configured, yaml)
        
        
        # print(args) 
        # print(yaml)
        print(f'configured:{configured}')
        
        return configured

    def _process_logging_options(self,config , yaml: Dict[str, Any]):
        """
        change logger level
        """
        logger.debug('process logging options')

        filename = self.args['logfile'].split('/')[-1]

        # args and default
        config['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{filename}"

        if 'logfile' in yaml and yaml['logfile'] is not None:
            # yaml
            config['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{yaml['logfile']}"

        check_folder(DEFAULT_LOG_FILE_DIR)
            
        setup_logging(config)
        

    # def _process_datadir_options(self, config, yaml: Dict[str, Any]):
    #     logger.debug("process datadir options")

    #     # args
    #     config['user_data_dir'] = f"{BOT_DIR}/{self.args['user_data_dir']}"

    #     if self.args['user_data_dir'] == DEFAULT_USERDATA_DIR:
    #         ## default or config
    #         config['user_data_dir'] = f"{BOT_DIR}/{yaml['user-data-dir']}"
        
    def _process_sync_options(self):
        logger.debug("process sync options")
        
        pass
        