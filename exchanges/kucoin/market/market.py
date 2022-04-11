import logging
from kucoin.client import Market
import math
from datetime import datetime
from .pairs import Pairs

logger = logging.getLogger(__name__)

class Kucoin_market(Pairs):
    def __init__(self, symbols, timeframe, startAt, endAt,is_sandbox=False):
        self.market = Market()
        self.is_sandbox = is_sandbox
        self.symbols =  symbols
        self.timeframe = timeframe
        self.startAt = startAt
        self.endAt = endAt
    


    def get_klines(self):
        # print(datetime.today().timestamp())
        # startAt = time
        klines = self.market.get_kline('BTC-USDT', '1day',startAt=self.startAt, endAt=self.endAt)
        print(klines)   

    def get_trade_history(self):
        pass
