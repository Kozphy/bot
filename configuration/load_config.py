"""
This module contain functions to load the configuration file
"""
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CSafeLoader as CSLoader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from pathlib import Path
import logging
from typing import Any, Dict
from dotenv import dotenv_values
from bot.exceptions import OperationalException
from bot import main

logger = logging.getLogger(__name__)



def load_yaml_setting(args: Dict[str, Any], destination: Path=None) -> Dict[str, Any]:
    logger.debug('check userdir whether define in cli')
    print(main.args)
    if 'user_data_dir' in args and args['user_data_dir'] is None:
        args['user_data_dir'] = f'{Path.cwd()}/user_data'
            
    
    
    # print(args)
    # exit()
    # print(sys.stdin)
    # exit() 
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