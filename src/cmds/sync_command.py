from loguru import logger
from typing import Any, Dict, List
# from exchanges.kucoin.client import Client
from exchanges import Exchanges
from enums import RunMode
from configuration import Configuration
from persistence.migrations import migration_upgrade, migration_downgrade
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
        configured = Configuration.from_options(ctx.obj).get_config()
        configured['common']['runmode'] = RunMode.SYNC
        logger.debug('print debug')
        pprint.pprint(configured)
        
        marketplace = Exchanges.init_exchange(configured).marketplace
        client = marketplace.client
        bbgo_client = marketplace.bbgo_client

        client.check_paries(symbols=configured['sync']['sync_symbols'])
        

        if configured['bbgo']['bbgo_grpc_services']['market'] == True:
            data = asyncio.run(bbgo_client.grpc_get_kline(limit=20))

        migration_upgrade(configured, 'head')
        # migration_downgrade(configured)
        # exit()

        data = asyncio.run(client.market_services.histories.get_klines(
            symbols=configured['sync']['sync_symbols'],
            startAt=configured['sync']['startAt'],
            endAt= configured['sync']['endAt'],
            timeframes=configured['sync']['timeframes']
        ))

        # pprint.pprint(data)
      
        # data = asyncio.run(client.get_trade_histories())

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

