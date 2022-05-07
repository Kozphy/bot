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
from .misc import check_folder

logger = logging.getLogger(__name__)
class Load_config():
    def determine_destination(self, args):
        logger.debug('determine where is user_data_dir')
        from bot.constants import (CONFIG, BOT_DIR, DEFAULT_USERDATA_DIR, 
        DEFAULT_CONFIG_NAME, DEFAULT_CONFIG_DIR_NAME)
        # use default
        user_dir = DEFAULT_USERDATA_DIR 
        config_dir_name = DEFAULT_CONFIG_DIR_NAME
        config_name = DEFAULT_CONFIG_NAME

        
        if args['user_data_dir'] != DEFAULT_USERDATA_DIR:
            # user_data_dir use args
            user_dir = f"{BOT_DIR}/{args['user_data_dir']}"
            check_folder(f"{user_dir}/{config_dir_name}")

        if args['config'] != CONFIG:
            # config use args
            config_name = args['config']

        destination = f"{user_dir}/{config_dir_name}/{config_name}"
        return destination


    def load_yaml_setting(self, args) -> Dict[str, Any]:
        destination = self.determine_destination(args)
        
        logger.debug('parse yaml file')
        try:
            with open(destination, 'r') as f:
                yaml = CSLoader(stream=f).get_data()
            return yaml
        except FileNotFoundError as e:
            logger.error(e)
            raise OperationalException(f"file {destination} not found")



