from loguru import logger
from distutils.command.config import config
from .misc import check_folder
from loggers import setup_logging
from typing import Any, Dict, List, Optional
from pathlib import PurePath
import pprint
from enums import RunMode

from attrs import define

@define
class Process_options:
    configured: Dict[str, Any]
    _args: Optional[Dict[str, Any]]
    _yaml: Optional[Dict[str, Any]]

    @classmethod
    def from_args(cls, args: Optional[Dict[str, Any]]):
        return cls(
            configured={},
            args=args,
            yaml=None,
        )


    def _process_logging_options(self):
        """
        change logger level
        """
        # TODO: change to PurePath
        from constants import DEFAULT_LOG_FILE_DIR
        logger.debug('process logging options')

        filename = self._args['logfile'].split('/')[-1]

        # args and default
        self.configured['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{filename}"

        if 'logfile' in self._yaml and self._yaml['logfile'] is not None:
            # yaml
            self.configured['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{self._yaml['logfile']}"

        check_folder(DEFAULT_LOG_FILE_DIR)
            
        setup_logging(self._args)

    def _process_common(self):
        logger.debug("process common options")
        common = self._yaml['common']

        self.configured.update({'common': common})

    def _process_api(self):
        """
        setting which source api featrue do you want
        """
        logger.debug("process api options")

        bbgo = self._yaml['bbgo']
        ccxt = self._yaml['ccxt']
        api = {
            'bbgo':bbgo,
            'ccxt':ccxt
        }
        self.configured.update(api)

        
    def _process_exchange_options(self):
        logger.debug("process exchange options")
        # TODO: process exchange yaml
        exchange_yaml = self._yaml['exchange']
        
        exchange = {**exchange_yaml}
        self.configured.update({'exchange': exchange})


    def _process_sync_options(self):
        logger.debug("process sync options") 

        ## process yaml sync 
        yaml_sync_dict = self._yaml['sync']
        sync = {
            **yaml_sync_dict,
        }

        # args
        if self._args['startAt'] is not None:
            sync['startAt'] = self._args['startAt']
        if self._args['endAt'] is not None:
            sync['endAt'] = self._args['endAt']

        self.configured.update({'sync':sync})
        
     
    def _process_persistece_options(self):
            logger.debug("process persistence options") 

            from constants import (DEFAULT_DB_HOST, DEFAULT_DB_PORT, DEFAULT_DB_USER,
            DEFAULT_USERDATA_DIR, DEFAULT_DB_DIR, DEFAULT_DB_NAME)
            config_persistence = self._yaml['persistence']

            # default and args
            persistence = {
                **config_persistence,
            }
            if self._args is not None:
                # args
                if self._args['db_path'] != DEFAULT_DB_DIR:
                    #TODO: implement USERDATA_DIR and purePath
                    persistence['path'] = self._args['db_path']
                    # logger.debug(f"db_path: {self._args['db_path']}")
                
                if self._args['db_name'] != DEFAULT_DB_NAME:
                    persistence['db_name'] = self._args['db_name']
                
                if self._args['db_user'] != DEFAULT_DB_USER:
                    persistence['user'] = self._args['db_user']
                
                if self._args['db_port'] != DEFAULT_DB_PORT:
                    persistence['port'] = self._args['db_port']
                
                if self._args['db_host'] != DEFAULT_DB_HOST:
                    persistence['host'] = self._args['db_host']

            self.configured.update({"persistence":persistence})
