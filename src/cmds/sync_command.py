import logging
from typing import Any, Dict, List
from exchanges.kucoin.client import Client
from exchanges import Exchange
from enums import RunMode
from configuration import Configuration
import sys
import asyncio
import pprint

logger = logging.getLogger(__name__)


def start_sync(ctx: Dict[str, Any]) -> None:
    """
    Download data
    """
    logger.debug("start sync")
    try: 
        ## init config
        ctx.obj['runmode'] = RunMode.SYNC
        configured, _ = Configuration(ctx.obj).get_config()
        pprint.pprint(configured)
        exchange = Exchange(configured)
        exchange = exchange.init_exchange()
        # exit()
        client = Client(configured)
        client = client.init_client()
        # print(dir(client))
        client.grpc_get_kline(configured)
        # migrations_update(configured)

        exit()

        asyncio.run(client.get_klines())
      
        # data = asyncio.run(client.get_trade_histories())
        # print(data)

        

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

