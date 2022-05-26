""" 
Cryptocurrency Exchanges support
"""
from typing import Dict, Any, Optional
from exceptions import ExchangeError
from enums import RunMode
from exchanges.kucoin.client import Kucoin_client
from exchanges.bbgo_grpc.bbgo_client import BBGO_client

from attrs import define



@define
class Exchanges:
    marketplace: Optional[Any]

    @classmethod
    def init_exchange(cls, configured):
        """
        init exchange which is selected by user and
        checking exchange is support or not
        :return exchange obj is selected by user :obj
        """
        from constants import support_exchanges, support_bbgo_grpc
        

        name = configured['exchange']['marketplace'].lower()


        if name not in support_exchanges:
            raise ExchangeError(f'{name} exchange is not support')

        if True in configured['bbgo'].keys():
            if name not in support_bbgo_grpc:
                raise ExchangeError(f'{name} exchange is not support bbgo_grpc')
        

        cls.marketplace = cls.marketplace_facotry(cls,name, configured) 
        return cls.marketplace

    

    def marketplace_facotry(self, name, configured):
        """
        marketplace factory
        :param name: exchange name
        :return: exchange obj
        """
        from constants import support_exchanges

        client = {
            'kucoin': [Kucoin_client, BBGO_client],
        } 
        exchange = support_exchanges[name].from_client(configured, *client[name])
        
        return exchange