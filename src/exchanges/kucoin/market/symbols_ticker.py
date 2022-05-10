import logging
import re
import aiohttp
from exceptions import BotException
import numpy as np
import time
from .market_api import Kucoin_market
from  exchanges.misc import split_pairs_to_request_format

logger = logging.getLogger(__name__)

class Symbols_Ticker(Kucoin_market):
    def get_accept_pairs(self, reg="\S+-USDT$", currency_pair="USDS"):
        """
        filter out pairs which exchnage allow
        :return filtered pairs :list
        """
        symbols = self.configured['symbols']
        pairs = self.get_symbol_list(currency_pair)
        origin_pairs = [pair['name'] for pair in pairs]
        r = re.compile(reg)
        # TODO: not very understand why
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
            symbol = symbol.split('/')
            symbol = symbol[0] + '-' + symbol[1]
            if symbol not in accept_pairs:
                Not_accept.append(symbol)

        if len(Not_accept) > 0:
            raise(BotException(f"{Not_accept} not accept pair in exchange"))

        return None

        # stop = time.time()
        # print('Time: ', stop - start)
    

    
