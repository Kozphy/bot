import logging
from kucoin.client import Trade

logger = logging.getLogger(__name__)

class Kucoin_trade(Trade):
    def __init__(self, api=None, secrect=None, passphrase=None):
        self.__api = api
        self.__secrect = secrect
        self.__passphrase = passphrase
        # self.market = None
        # self.User = None
        # self.trade = None
        # self.client = None
    
    def init_trade(self, is_sandbox=True):
        return Trade(is_sandbox=is_sandbox)
    
    def get_order_book(self, symbol, limit):
        return self.get_order_book(symbol, limit)
    
    def get_trades(self, symbol, limit):
        return self.get_trades(symbol, limit)
    
    def get_symbols(self):
        return self.get_symbols()
    
    def get_symbol(self, symbol):
        return self.get_symbol(symbol)
    
    def get_symbol_ticker(self, symbol):
        return self.get_symbol_ticker(symbol)
    
    def get_symbol_ticker_24h(self, symbol):
        return self.get_symbol_ticker_24h(symbol)
    
    def get_symbol_order_book(self, symbol, limit):
        return self.get_symbol_order_book(symbol, limit)
    
    def get_symbol_trades(self, symbol, limit):
        return self.get_symbol_trades(symbol, limit)
    
    def get_symbol_candles(self, symbol, resolution, startAt, endAt):
        return self.get_symbol_candles(symbol, resolution, startAt, endAt)
    
    def get_symbol_candles_last(self, symbol, resolution):
        return self.get_symbol_candles_last(symbol, resolution)
    
    def get_symbol_candles_first(self, symbol, resolution):
        return