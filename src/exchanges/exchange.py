""" 
Cryptocurrency Exchanges support
"""
import logging
from typing import Dict, Any
# from bot.exchanges import Connector
from exceptions import ExchangeError
from enums import RunMode

logger = logging.getLogger(__name__)

class Exchange:
    def __init__(self, configured) -> None:
        """
        Initializes this module with the given config,
        it does basic validation whether the specified exchange and pairs are valid.
        :return: None
        """
        self.configured = configured
        self._exchange = None

    def init_exchange(self):
        """
        init exchange which is selected by user and
        checking exchange is support or not
        :return exchange obj is selected by user :obj
        """
        from constants import support_exchange_api, support_bbgo_grpc
        name = self.configured['session'].lower()
        # if self.configured['runmode'] == RunMode.SYNC:
        #     name = self.configured['sync_dict']['session'].lower()

        if name not in support_exchange_api:
            raise ExchangeError(f'{name} exchange is not support')

        if self.configured['bbgo_grpc'] == True:
            if name not in support_bbgo_grpc:
                raise ExchangeError(f'{name} exchange is not support bbgo_grpc')
        

        
        self._exchange = support_exchange_api[name](self.configured)
        
        return self._exchange
    



        
        


 