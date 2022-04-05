""" 
Cryptocurrency Exchanges support
"""
import logging
import ccxt
from typing import Dict, Any

logger = logging.getLogger(__name__)

class Exchange:
    def __init__(self, config: Dict[str, Any], validate: bool = True) -> None:
        """
        Initializes this module with the given config,
        it does basic validation whether the specified exchange and pairs are valid.
        :return: None
        """
        _config: Dict = {}
        self._api: ccxt.exchange = None
        
        
    def __init_ccxt(self, exchange_config: Dict[str, Any], ccxt_module: CcxtModuleType = ccxt, 
    ccxt_kwargs: Dict = {}) -> ccxt.Exchange:
        """
        Initialize ccxt with given config and return valid
        ccxt instance.
        """
        pass