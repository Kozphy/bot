from exchanges.kucoin.client import Kucoin_client
from exchanges.bbgo_grpc.bbgo_client import BBGO_client

from typing import Optional, Dict, Any
from attrs import define
import ccxt

@define
class Kucoin:
    client: Kucoin_client
    bbgo_client: Optional[BBGO_client]
    ccxt_client: Optional[ccxt.kucoin]
    

    @classmethod
    def from_client(cls, configured, client: Kucoin_client,
    bbgo_client:BBGO_client=None, ccxt_exchange: ccxt.kucoin=None) -> 'Kucoin':
        return cls(
            client = client.active_service(configured),
            bbgo_client = bbgo_client,
            ccxt_client = ccxt_exchange
        )

        





    
    
    