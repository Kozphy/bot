import logging 
from .misc import check_folder
from bot.loggers import setup_logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class Process_options:
    setting_format = Optional[Dict[str, Any]]
    def __init__(self, args: setting_format, runmode = None):
        self._args = args
        self._config: self.setting_format = None
        self._yaml: self.setting_format = None
        self._runmode = runmode

    # @property
    # def get_args(self):
    #     return self._args
    
    # @property
    # def get_config(self):
    #     return self._config
    
    # @property
    # def get_runmode(self):
    #     return self._runmode
    def _process_logging_options(self, args: setting_format):
        """
        change logger level
        """
        from bot.constants import BOT_DIR, DEFAULT_USERDATA_DIR, DEFAULT_LOG_FILE_DIR
        logger.debug('process logging options')

        filename = self._args['logfile'].split('/')[-1]

        # args and default
        args['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{filename}"

        if 'logfile' in self._yaml and self._yaml['logfile'] is not None:
            # yaml
            args['logfile'] = f"{DEFAULT_LOG_FILE_DIR}/{self._yaml['logfile']}"

        check_folder(DEFAULT_LOG_FILE_DIR)
            
        setup_logging(args)

    def _process_sync_options(self, args: setting_format):
        logger.debug("process sync options") 

        ## process yaml sync 
        # print(self._yaml) 
        config_sync_dict = self._yaml['sync']
        if config_sync_dict['sync_pairs'] == 'trade_pairs':
            config_sync_dict['sync_paris'] = self._yaml['trade_pairs']
        
        args['sync_dict'] = {'session': self._yaml['session'] ,**config_sync_dict}

        # process startAt amd emdAt
        if args['startAt'] is None:
            args['startAt'] = config_sync_dict['startAt']
        if args['endAt'] is None:
            args['endAt'] = config_sync_dict['endAt']

        # process mode 
        args['runmode'] = self._runmode
        
     
        