import logging
from kucoin.client import Market
import math
from datetime import datetime
logger = logging.getLogger(__name__)

class Kucoin_market:
    def __init__(self,is_sandbox=False):
        self.market = Market()
        self.is_sandbox = is_sandbox

    def get_klines(self, symbol, startAt, endAt, type, sandbox):
        # print(datetime.today().timestamp())
        endAt = math.floor(datetime.today().timestamp()*1000)
        startAt =  endAt - 60*60*24*7
        print(endAt)
        # startAt = time
        klines = client.get_kline('BTC-USDT', '1day',startAt=startAt, endAt=endAt)
        print(klines)
