"""
bot constants
"""

from typing import List, Tuple
from pathlib import Path
from exchanges import Kucoin
__version__ = '0.0.1'

## bot
BOT_NAME = 'bot'
BOT_DIR = f'{Path.cwd()}/src'


## cmd Directory and name
CMD_DIR = f'{BOT_DIR}/cmd'
CMD_NAME1 = 'scripts'
CMD_1 = f'{CMD_DIR}/{CMD_NAME1}'


## user data dir
DEFAULT_USERDATA_DIR_NAME = 'user_data'
DEFAULT_USERDATA_DIR = f'{BOT_DIR}/{DEFAULT_USERDATA_DIR_NAME}'

## alembic
ALEMBIC_CONFIG_FILE = f'{BOT_DIR}/alembic.ini'

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
# support_exchange_api = ['kucoin']
support_exchanges = {
     'kucoin': Kucoin
}
support_bbgo_grpc = ['kucoin', 'binance', 'ftx', 'max', 'okex']

## .env
DEFAUT_ENV = '.env'

