import logging
from typing import Any, Dict, List
from bot.configuration import Configuration
from bot.exchanges import Exchange
from bot.enums import RunMode
import sys

logger = logging.getLogger(__name__)

def start_sync(args: Dict[str, Any]) -> None:
    """
    Download data
    """
    try: 
        ## init config
        c = Configuration(args=args, runmode=RunMode.SYNC)
        configured, yaml = c.get_config()
        exchange = Exchange(configured, yaml)
        print(configured)
        exchange = exchange.init_exchange()
        exchange.request_time_format()
        # market = exchange.init_market()
        # client = exchange.client
        # print(dir(exchange))
        # exchange.get_kline()
        # print(exchange._api)
        

        

    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

