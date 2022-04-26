import logging
from kucoin.client import Market
import asyncio

logger = logging.getLogger(__name__)

class Kucoin_market():
    def __init__(self, symbols, timeframe, startAt, endAt, is_sandbox=False):
        self.market = Market()
        self.is_sandbox = is_sandbox
        self.symbols =  symbols
        self.timeframe = timeframe
        self.startAt = startAt
        self.endAt = endAt

    async def asy_to_thread(self, fn, req_args):
        res = await asyncio.gather(asyncio.to_thread(fn, **req_args))
        return res

    def get_symbol_list(self, currency_pair="USDS"):
        """
        Request via this endpoint to get the transaction currency for the entire trading market.

        :return market ticker :list
        """
        return self.market.get_symbol_list(market=currency_pair)
    
    def get_market_list(self):
        return self.market.get_market_list()
    
    
    # def sync_kline():
    #     """
    #     write info to database
    #     """
    #     pass


