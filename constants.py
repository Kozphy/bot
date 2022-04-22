"""
bot constants
"""

from typing import List, Tuple
from pathlib import Path
from bot.exchanges.kucoin import Kucoin

## bot
BOT_NAME = 'bot'
BOT_DIR = f'{Path.cwd()}/{BOT_NAME}'

## user data dir
DEFAULT_USERDATA_DIR_NAME = 'user_data'
DEFAULT_USERDATA_DIR = f'{BOT_DIR}/{DEFAULT_USERDATA_DIR_NAME}'

## database 
DEFAULT_DB_USER = 'root'
DEFAULT_DB_HOST = 'localhost'
DEFAULT_DB_DIR_NAME = 'db'
DEFAULT_DB_NAME = 'test'
DEFAULT_DB_DIR = f'{DEFAULT_USERDATA_DIR}/{DEFAULT_DB_DIR_NAME}'
DATABASE = f'{DEFAULT_DB_DIR}/{DEFAULT_DB_NAME}'
DEFAULT_DB_PORT = 8080

## config file
DEFAULT_CONFIG_DIR_NAME = 'config'
DEFAULT_CONFIG_NAME = 'config.yaml'
DEFAULT_CONFIG_DIR = f'{DEFAULT_USERDATA_DIR}/{DEFAULT_CONFIG_NAME}'
CONFIG = f'{DEFAULT_CONFIG_DIR}/{DEFAULT_CONFIG_NAME}'

## logfile
DEFAULT_LOG_FILE_DIR_NAME = 'log'
DEFAULT_LOG_FILE_NAME = 'bot_record'
DEFAULT_LOG_FILE_DIR = f'{BOT_DIR}/{DEFAULT_LOG_FILE_DIR_NAME}'
LOG_FILE = f'{DEFAULT_LOG_FILE_DIR}/{DEFAULT_LOG_FILE_NAME}'

## exchange
DEFAUT_EXCHANGE = 'kucoin'
support_exchange = {
     'kucoin': Kucoin
}

## .env
DEFAUT_ENV = '.env'

