import logging
from typing import Any, Dict, List
from bot.exchanges.kucoin.client import Client
from bot.exchanges import Exchange
from bot.enums import RunMode
import sys
import asyncio

logger = logging.getLogger(__name__)

def start_sync(configured: Dict[str, Any], yaml) -> None:
    """
    Download data
    """
    logger.debug("start sync")
    try: 
        ## init config
        # print(args)
        configured['runmode'] = RunMode.SYNC
        # print(configured)
        exchange = Exchange(configured, yaml)
        exchange = exchange.init_exchange()
        client = Client(configured, yaml)
        client = client.init_client()
        # migrations_update(configured)

        exit()


        
        asyncio.run(client.get_klines())
      
        # data = asyncio.run(client.get_trade_histories())
        # print(data)

        

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

