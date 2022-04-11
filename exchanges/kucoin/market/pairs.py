import logging
import re

logger = logging.getLogger(__name__)

class Pairs():
    def get_accept_pairs(self, reg="\S+-USDT$", currency_pair="USDS"):
        """
        filter out pairs which exchnage allow
        :return filtered pairs :list
        """
        pairs = self.get_symbol_list(currency_pair)
        origin_pairs = [pair['name'] for pair in pairs]
        r = re.compile(reg)
        # TODO: misunderstand
        pairs_done = list(filter(r.match, origin_pairs))


        return pairs_done

        

    def get_symbol_list(self, currency_pair):
        """
        Request via this endpoint to get the transaction currency for the entire trading market.

        :return market ticker :list
        """
        # TODO: store data to database
        return self.market.get_symbol_list(market=currency_pair)
    
    def get_market_list(self):
        return self.market.get_market_list()