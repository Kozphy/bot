from loguru import logger
import re
import aiohttp
from exceptions import BotException
import numpy as np
import time
from .market_api import Kucoin_market
from  exchanges.utils.misc import convert_symbols_to_request_format

from attrs import define, field
from typing import Dict, Any

@define
class Symbols_Ticker:
    _market_api: Kucoin_market
    
    @classmethod
    def from_api(cls, configured: Dict[str, Any], is_sandbox) -> Kucoin_market:
        return cls(
            market_api=Kucoin_market.from_config(configured, is_sandbox)
        )

    def get_accept_pairs(self, reg="\S+-USDT$", currency_pair="USDS"):
        """
        filter out pairs which exchnage allow
        :return filtered pairs :list
        """
        market: Kucoin_market = self._market_api
        symbols = market.symbols
        pairs = market.get_symbol_list(currency_pair=currency_pair)
        origin_pairs = [pair['name'] for pair in pairs]
        r = re.compile(reg)
        # TODO: filter not very understand why this syntax work
        pairs_done = list(filter(r.match, origin_pairs))
        self.check_accept_pairs(symbols, pairs_done)

        return pairs_done

    def check_accept_pairs(self, symbols, accept_pairs) -> None:
        """
        check if pairs is valid
        :return None
        """
        # start = time.time()
        Not_accept = []

        for symbol in symbols:
            if symbol not in accept_pairs:
                Not_accept.append(symbol)

        if len(Not_accept) > 0:
            raise(BotException(f"{Not_accept} not accept pair in exchange"))

        return None

        # stop = time.time()
        # print('Time: ', stop - start)
    

    
