from distutils.command.config import config
import logging
from .misc import check_folder
from loggers import setup_logging
from typing import Any, Dict, List, Optional
from pathlib import PurePath
import pprint
from enums import RunMode

logger = logging.getLogger(__name__)


class Process_options:
    setting_format = Optional[Dict[str, Any]]
    def __init__(self, args: setting_format):
        self._args = args
        self._config: self.setting_format = None
        self._yaml: self.setting_format = None

    def _process_logging_options(self, args: setting_format):
        """
        change logger level
        """
        # TODO: change to PurePath
        from constants import DEFAULT_LOG_FILE_DIR
        logger.debug('process logging options')

        filename = self._args['logfile'].split('/')[-1]

        # args and default
        args['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{filename}"

        if 'logfile' in self._yaml and self._yaml['logfile'] is not None:
            # yaml
            args['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{self._yaml['logfile']}"

        check_folder(DEFAULT_LOG_FILE_DIR)
            
        setup_logging(args)

    def _process_api(self, args: setting_format):
        """
        setting which source api featrue do you want
        """
        logger.debug("process api options")
        # print(self._yaml)
        bbgo = self._yaml['bbgo']
        ccxt = self._yaml['ccxt']
        args.update(bbgo)

        
    def _process_exchange_options(self, args: setting_format):
        logger.debug("process exchange options")
        # TODO: process exchange yaml
        exchange_yaml = self._yaml['exchange']
        
        exchange = {**exchange_yaml}
        args.update(exchange)




    def _process_sync_options(self, args: setting_format):
        logger.debug("process sync options") 

        ## process yaml sync 
        yaml_sync_dict = self._yaml['sync']
        # pprint.pprint(self._yaml)
        # print('\n')
        # print(yaml_sync_dict)
        # exit()
        if args['runmode'] == RunMode.SYNC:
            args['symbols'] = yaml_sync_dict['sync_symbols']

        # process startAt amd emdAt
        if 'startAt' in args == False or args['startAt'] is None:
            args['startAt'] = yaml_sync_dict['startAt']
        if 'endAt' in args == False or args['endAt'] is None:
            args['endAt'] = yaml_sync_dict['endAt']

        del yaml_sync_dict['startAt']
        del yaml_sync_dict['endAt']
        del yaml_sync_dict['sync_symbols']

        args.update(yaml_sync_dict)
        
     
    def _process_persistece_options(self, args: setting_format):
            logger.debug("process persistence options") 

            from constants import (DEFAULT_DB_HOST, DEFAULT_DB_PORT, DEFAULT_DB_USER,
            DEFAULT_USERDATA_DIR, DEFAULT_DB_DIR, DEFAULT_DB_NAME)
            # print(self._yaml)
            config_persistence = self._yaml['persistence']
            config_db_path: str = str(PurePath(DEFAULT_USERDATA_DIR,config_persistence['path']))
            config_db_name: str = config_persistence['name']
            config_db_user: str = config_persistence['user']
            config_db_port: int = config_persistence['port']
            config_db_host = config_persistence['host']

            # default and args
            persistence = {
                'db': config_persistence['db'],
                'db_password': config_persistence['password'],
                'db_path': args['db_path'],
                'db_name': args['db_name'],
                'db_user': args['db_user'],
                'db_port': args['db_port'],
                'db_host': args['db_host'],
            }
            # print(args, '\n')
            # print(config_persistence, '\n')

            # TODO: refactor
            # config
            if args['db_path'] == DEFAULT_DB_DIR and DEFAULT_DB_DIR != config_db_path:
                persistence['db_path'] = config_persistence['path'] 
                # print("database_path: " + db_path)
            
            if args['db_name'] == DEFAULT_DB_NAME and DEFAULT_DB_NAME != config_db_name:
                persistence['db_name'] = config_persistence['name']
                # print("database name: " + db_name)
            
            if args['db_user'] == DEFAULT_DB_USER and DEFAULT_DB_USER != config_db_user:
                persistence['db_user'] = config_persistence['user']

            if args['db_port'] == DEFAULT_DB_PORT and DEFAULT_DB_PORT != config_db_port:
                persistence['db_port'] = config_persistence['port']

            if args ['db_host']  == DEFAULT_DB_HOST and DEFAULT_DB_HOST != config_db_host:
                persistence['db_host'] = config_persistence['host']
            args.update(persistence)
