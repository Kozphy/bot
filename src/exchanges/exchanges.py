""" 
Cryptocurrency Exchanges support
"""
import logging
from typing import Dict, Any, Optional
from exceptions import ExchangeError
from enums import RunMode
from exchanges.kucoin.client import Kucoin_client
from exchanges.bbgo_grpc.bbgo_client import BBGO_client
from constants import support_exchanges, support_bbgo_grpc

from attrs import define


logger = logging.getLogger(__name__)

@define
class Exchanges:
    marketplace: Optional[Any]
    # bbgo_options: bool
    # bbgo_servies_options: Dict[str, Any]
    # bbgo_server_host: Optional[str]
    # bbgo_server_port: Optional[str]

    @classmethod
    def init_exchange(cls, configured):
        """
        init exchange which is selected by user and
        checking exchange is support or not
        :return exchange obj is selected by user :obj
        """
        name = configured['exchange']['marketplace'].lower()

        if name not in support_exchanges:
            raise ExchangeError(f'{name} exchange is not support')

        if True in configured['bbgo'].keys():
            if name not in support_bbgo_grpc:
                raise ExchangeError(f'{name} exchange is not support bbgo_grpc')
        

        exchange = cls(
            marketplace= cls.marketplace_facotry(cls, name, configured)
        )
        
        return exchange
    

    def marketplace_facotry(self, name, configured):
        """
        marketplace factory
        :param name: exchange name
        :return: exchange obj
        """
        client = {
            'kucoin': [Kucoin_client, BBGO_client],
        } 
        exchange = support_exchanges[name].from_client(configured, *client[name])
        
        return exchange