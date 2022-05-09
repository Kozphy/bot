import logging
from kucoin.client import Market
import asyncio

logger = logging.getLogger(__name__)

class Kucoin_market():
    timeframe_format = {
        '1m': '1min',
        '3m': '3min',
        '5m': '5min',
        '15m': '15min',
        '30m': '30min',
        '1h': '1hour',
        '2h': '2hour',
        '4h': '4hour',
        '6h': '6hour',
        '8h': '8hour',
        '12h': '12hour',
        '1d': '1day',
        '1w': '1week',
    }

    def __init__(self, symbols, timeframe, startAt, endAt, is_sandbox=False):
        self.market = Market()
        self.is_sandbox = is_sandbox
        self.symbols =  symbols
        self.timeframe = timeframe
        self.startAt = startAt
        self.endAt = endAt

    async def asy_to_thread(self, fn, req_args):
        # TODO: need to fix rate limit
        # reference article: https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/
        # In considering use https://github.com/vutran1710/PyrateLimiter, or other method
        res = await asyncio.gather(asyncio.to_thread(fn, **req_args), return_exceptions=True)
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


