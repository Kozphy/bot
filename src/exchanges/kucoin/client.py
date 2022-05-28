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
    rest_services: Dict[str, Market_facade]
    
    available_pairs: Optional[List[str]] = field()

    @classmethod
    def active_service(cls, configured: Dict[str, Any]) -> 'Kucoin_client':
        return cls(
            rest_services = {
                'market': Market_facade.from_client(configured, 
                cls.get_auth(cls, configured)),
                }
        )
    
    @available_pairs.default
    def check_pairs(self):
        available_pairs = self.rest_services['market'].symbols_ticker.get_accept_pairs()
        self.rest_services['market'].symbols_ticker.check_accept_pairs(available_pairs)
        return available_pairs

    def get_auth(self, configured):
        exchange = configured['exchange']
        apikey = exchange['apikey']
        version_api = False if apikey['version'] == 2 else True
        auth = {
            'key': apikey['public'],
            'secret': apikey['secret'],
            'is_v1api': version_api,
            'passphrase': apikey['password'],
        }
        return auth



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

