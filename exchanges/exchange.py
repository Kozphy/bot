""" 
Cryptocurrency Exchanges support
"""
import logging
from typing import Dict, Any
# from bot.exchanges import Connector
from bot.exceptions import ExchangeError
from bot.enums import RunMode

logger = logging.getLogger(__name__)

class Exchange:
    def __init__(self, configured, yaml, validate: bool = True) -> None:
        """
        Initializes this module with the given config,
        it does basic validation whether the specified exchange and pairs are valid.
        :return: None
        """
        self.configured = configured
        self.yaml = yaml
        # self._exchange_name = exchange
        self._exchange = None

    def init_exchange(self):
        """
        init exchange which is selected by user and
        checking exchange is support or not
        :return exchange obj is selected by user :obj
        """
        from bot.constants import support_exchange
        if self.configured['runmode'] == RunMode.SYNC:
            name = self.configured['sync_dict']['session']

        if name not in support_exchange:
            raise ExchangeError(f'{name} exchange not support')
        
        self._exchange = support_exchange[name](self.configured, self.yaml)
        
        return self._exchange

        
 