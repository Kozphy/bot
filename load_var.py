from yaml import load, dump
try:
    from yaml import CLoader as Loader, CSafeLoader as CSLoader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from pathlib import Path
import logging
from typing import Dict
from dotenv import dotenv_values
from bot.main import args

logger = logging.getLogger(__name__)

print(args)
# p = Path('./user_data')
# q = p / 'config.yaml'

# # print(dir(CSLoader))
# def get_yaml_setting() -> Dict:
#     logger.info('parse yaml file')
#     with open(q, 'r') as f:
#         yaml = CSLoader(stream=f).get_data()
#     return yaml

# def get_env_setting():
#     logger.info('parse env file')
#     p = Path('./user_data')
#     q = p / '.env'
#     config = None 
#     with open(q, 'r') as f:
#         config = dotenv_values(stream=f)
#     return config

# get_env_setting()