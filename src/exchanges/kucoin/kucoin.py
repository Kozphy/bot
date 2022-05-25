# from kucoin.client import Market, User, Trade
# from bot.exchanges.kucoin.market.market import Kucoin_market
# from bot.exchanges.kucoin.trade.trade import Kucoin_trade
# from bot.exchanges.kucoin.user.user import Kucoin_user
from exchanges.kucoin.client import Kucoin_client
from exchanges.bbgo_grpc.bbgo_client import BBGO_client

from typing import Optional, Dict, Any
from attrs import define

@define
class Kucoin:
    client: Kucoin_client
    bbgo_client: Optional[BBGO_client]

    @classmethod
    def from_client(cls, configured, client: Kucoin_client,
    bbgo_client:BBGO_client=None) -> 'Kucoin':
        return cls(
            client=client.active_service(configured),
            bbgo_client=bbgo_client,
        )

        





    
    
    