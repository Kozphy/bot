from loguru import logger
from typing import Any, Dict, List
from exchanges.kucoin.client import Client
from exchanges import Exchange
from enums import RunMode
from configuration import Configuration
import sys
import asyncio
import pprint



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
        client = client.active_service()
        # print(dir(client))
        if configured['bbgo_grpc_service']['market'] == True:
            data = asyncio.run(client.grpc_get_kline(limit=20))
        # print(data)
        # migrations_update(configured)

        data = asyncio.run(client.get_klines())
        pprint.pprint(data)
      
        # data = asyncio.run(client.get_trade_histories())

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

