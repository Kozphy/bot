import logging


logger = logging.getLogger(__name__)

class Histories():
    def get_klines(self):
            klines = self.market.get_kline('BTC-USDT', '1day',startAt=self.startAt, endAt=self.endAt)
            print(klines)