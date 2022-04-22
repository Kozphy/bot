import logging
from typing import Any, Dict, List
from bot.configuration import Configuration
from bot.exchanges import Exchange
from bot.enums import RunMode
from bot.persistence.engine import init_db
import sys


logger = logging.getLogger(__name__)

def start_sync(args: Dict[str, Any]) -> None:
    """
    Download data
    """
    logger.debug("start sync")
    try: 
        ## init config
        print(args)
        c = Configuration(args=args, runmode=RunMode.SYNC)
        configured, yaml = c.get_config()
        exchange = Exchange(configured, yaml)
        print(configured)
        exchange = exchange.init_exchange()
        client = exchange.create_client()
        client = client.init_client()
        # client.get_accept_pairs()
        # client.get_klines()

        

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

