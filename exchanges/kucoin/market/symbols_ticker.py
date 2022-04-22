import logging
import re
import aiohttp
from bot.exceptions import BotException
import numpy as np
import time
from .market_api import Kucoin_market

logger = logging.getLogger(__name__)

class Symbols_Ticker(Kucoin_market):
    def get_accept_pairs(self, reg="\S+-USDT$", currency_pair="USDS"):
        """
        filter out pairs which exchnage allow
        :return filtered pairs :list
        """
        pairs = self.get_symbol_list(currency_pair)
        origin_pairs = [pair['name'] for pair in pairs]
        r = re.compile(reg)
        # TODO: not very understand why
        pairs_done = list(filter(r.match, origin_pairs))

        self.check_accept_pairs(pairs_done)

        return pairs_done

    def check_accept_pairs(self, accept_pairs) -> None:
        """
        check if pairs is valid
        :retur None
        """
        # start = time.time()
        Not_accept = []
        for x in self.symbols:
            symbol = x.split('/')
            symbol = symbol[0] + '-' + symbol[1]
            if symbol not in accept_pairs:
                Not_accept.append(x)

        if len(Not_accept) > 0:
            raise(BotException(f"{Not_accept} not accept pair in exchange"))

        return None

        # stop = time.time()
        # print('Time: ', stop - start)
    
    def pairs_info_to_database(self, pairs):
        """
        Store pairs info to database
        :return: None
        """
        self.get_accept_pairs()
        
        pass
        

    def get_symbol_list(self, currency_pair="USDS"):
        """
        Request via this endpoint to get the transaction currency for the entire trading market.

        :return market ticker :list
        """
        # TODO: store data to database
        return self.market.get_symbol_list(market=currency_pair)
    
    def get_market_list(self):
        return self.market.get_market_list()