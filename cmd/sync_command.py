import logging
from typing import Any, Dict, List
from bot.configuration.configuration import Configuration
from bot.enums import RunMode
import sys
# from bot.exchange.kucoin import 

logger = logging.getLogger(__name__)

def start_sync(args: Dict[str, Any]) -> None:
    """
    Download data
    """
    try: 
        c = Configuration(args=args, runmode=RunMode.SYNC)
        c.get_config()
        # print(Kucoin.has())

    except KeyboardInterrupt:
        sys.exit('SIGINT received, aborting ...')
    

