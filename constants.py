"""
bot constants
"""

from typing import List, Tuple
from pathlib import Path

## bot
BOT_NAME = 'bot'
BOT_DIR = f'{Path.cwd()}/{BOT_NAME}'

## user data dir
DEFAULT_USERDATA_DIR_NAMR = 'user_data'
DEFAULT_USERDATA_DIR = f'{BOT_DIR}/{DEFAULT_USERDATA_DIR_NAMR}'

## config file
DEFAULT_CONFIG_DIR_NAME = 'config'
DEFAULT_CONFIG_NAME = 'config.yaml'
DEFAULT_CONFIG_DIR = f'{DEFAULT_USERDATA_DIR}/{DEFAULT_CONFIG_NAME}'
CONFIG = f'{DEFAULT_CONFIG_DIR}/{DEFAULT_CONFIG_NAME}'

## logfile
DEFAULT_LOG_FILE_DIR_NAME = 'log'
DEFAULT_LOG_FILE_NAME = 'bot_record'
DEFAULT_LOG_FILE_DIR = f'{BOT_DIR}/{DEFAULT_LOG_FILE_DIR_NAME}'
LOG_FILE = f'{DEFAULT_LOG_FILE_DIR}/bot_record'

## exchange
DEFAUT_EXCHANGE = 'kucoin'

## .env
DEFAUT_ENV = '.env'