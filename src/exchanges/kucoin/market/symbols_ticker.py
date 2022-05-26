from loguru import logger
import re
import aiohttp
from exceptions import BotException
import numpy as np
import time
from .market_api import Kucoin_market

from attrs import define, field
from typing import Dict, Any

@define
class Symbols_Ticker:
    _market_api: Kucoin_market
    
    @classmethod
    def from_api(cls, configured: Dict[str, Any]) -> Kucoin_market:
        return cls(
            market_api=Kucoin_market.from_config(configured)
        )

    def get_accept_pairs(self, reg, currency_pair):
        """
        filter out pairs which exchnage allow
        :return filtered pairs :list
        """
        market: Kucoin_market = self._market_api
        pairs = market.get_symbol_list(currency_pair=currency_pair)
        origin_pairs = [pair['name'] for pair in pairs]
        r = re.compile(reg)
        # TODO: filter not very understand why this syntax work
        pairs_done = list(filter(r.match, origin_pairs))

        return pairs_done

    def check_accept_pairs(self, accept_pairs) -> None:
        """
        check if pairs whether valid in exchange
        :return None
        """
        # start = time.time()
        market: Kucoin_market = self._market_api

        Not_accept = []
        for symbol in market.symbols:
            if symbol not in accept_pairs:
                Not_accept.append(symbol)

        if len(Not_accept) > 0:
            raise(BotException(f"{Not_accept} not accept pair in exchange"))

        return None

        # stop = time.time()
        # print('Time: ', stop - start)
    

    
