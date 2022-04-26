import logging
from typing import Any, Dict, List
from bot.configuration import Configuration
from bot.exchanges import Exchange
from bot.enums import RunMode
from bot.persistence.engine import init_db
from bot.persistence.write_kline import kline_to_database
import sys
import asyncio

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
        # print(yaml)
        print(configured)
        exchange = exchange.init_exchange()
        client = exchange.create_client()
        client = client.init_client()
        data = asyncio.run(client.get_klines())
        
        if data is not None:
            db_para = {
                'db': configured['db'],
                'user': configured['db_user'],
                'password': configured['db_password'],
                'host': configured['db_host'],
                'dbname':configured['db_name'],
                'port': configured['db_port'],
            }
            engine = init_db(**db_para)
            kline_to_database(engine, data) 


        # data = asyncio.run(client.get_trade_histories())
        # print(data)

        

        
    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

