import logging
from typing import Any, Dict, List
from exchanges.kucoin.client import Client
from exchanges import Exchange
from enums import RunMode
import sys
import asyncio
import click


logger = logging.getLogger(__name__)


def start_sync(configured) -> None:
    """
    Download data
    """
    logger.debug("start sync")
    try: 
        ## init config
        configured['runmode'] = RunMode.SYNC
        print(configured)
        # exit()
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
    

