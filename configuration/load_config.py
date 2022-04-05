"""
This module contain functions to load the configuration file
"""
from tabnanny import check
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CSafeLoader as CSLoader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from pathlib import Path
import logging
from typing import Any, Dict, Optional
from dotenv import dotenv_values
from bot.exceptions import OperationalException
from bot.constants import (CONFIG, BOT_DIR, DEFAULT_USERDATA_DIR, 
DEFAULT_CONFIG_NAME, DEFAULT_CONFIG_DIR_NAME)
from .misc import check_folder

logger = logging.getLogger(__name__)

# def _process_datadir_options(self, config, yaml: Dict[str, Any]):
#     logger.debug("process datadir options")
#     # check_folder(f"{BOT_DIR}/{self.args['user_data_dir']}") 
    
#     # args
#     config['user_data_dir'] = f"{BOT_DIR}/{self.args['user_data_dir']}"

#     if self.args['user_data_dir'] == DEFAULT_USERDATA_DIR:
#         ## default or config
#         config['user_data_dir'] = f"{BOT_DIR}/{yaml['user-data-dir']}"

#     check_folder(f"{config['user_data_dir']}") 

def load_yaml_setting(args) -> Dict[str, Any]:
    logger.debug('check userdir whether define in cli')
    
    # use default
    user_dir = DEFAULT_USERDATA_DIR
    config_dir_name = DEFAULT_CONFIG_DIR_NAME
    config_name = DEFAULT_CONFIG_NAME

    
    if args['user_data_dir'] != DEFAULT_USERDATA_DIR:
        # user_data_dir use args
        user_dir = f"{BOT_DIR}/{args['user_data_dir']}"
        check_folder(f"{user_dir}/{config_dir_name}")

    if args['config'] != CONFIG:
        # config use args or default
        config_name = args['config']

    destination = f"{user_dir}/{config_dir_name}/{config_name}"


    logger.debug('parse yaml file')
    try:
        with open(destination, 'r') as f:
            yaml = CSLoader(stream=f).get_data()
        return yaml
    except FileNotFoundError:
        raise OperationalException(f"file {destination} not found!")



# def load_yaml_from_cli(path: str) -> Dict[str,Any]:
#     """
#     Loads a config file from the given path 
#     :param path: path as str
#     :return: configuration as dictionary
    # """
    # try:
        # Read config path from stdin
        # print(args)
        # with open(path) if path
        
    # except:

# def get_env_setting():
#     logger.info('parse env file')
#     p = Path('./user_data')
#     q = p / '.env'
#     config = None 
#     with open(q, 'r') as f:
#         config = dotenv_values(stream=f)
#     return config

# get_env_setting()