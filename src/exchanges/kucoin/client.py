from kucoin.client import Market
from datetime import datetime, timedelta
import math
import pprint
import inspect

from  exchanges.utils.misc import convert_symbols_to_request_format
from typing import Dict, Any, List, Optional
from exchanges.kucoin.market.market_facade import Market_facade
from attrs import define, field

@define
class Kucoin_client:
    market_services: Market_facade
    
    available_pairs: Optional[List[str]] = field()

    @classmethod
    def active_service(cls, configured: Dict[str, Any]) -> 'Kucoin_client':
        return cls(
            market_services = Market_facade.from_market(configured),
        )
    
    @available_pairs.default
    def check_pairs(self):
        available_pairs = self.market_services.symbols_ticker.get_accept_pairs()
        self.market_services.symbols_ticker.check_accept_pairs(available_pairs)
        return available_pairs


    @staticmethod
    def get_server_and_current_time():
        """
        Get server and local time in millisecond
        :return localtime, servertime
        """
        client = Market()
        servertime = client.get_server_timestamp()
        localtime = math.floor(datetime.today().timestamp()*1000)
        return servertime, localtime

