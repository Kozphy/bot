import logging 
from bot.exchanges import Exchange
# from kucoin.client import Market, User, Trade
# from bot.exchanges.kucoin.market.market import Kucoin_market
# from bot.exchanges.kucoin.trade.trade import Kucoin_trade
# from bot.exchanges.kucoin.user.user import Kucoin_user
from bot.exchanges.kucoin.client import Client
from datetime import datetime
import time
import math

logger = logging.getLogger(__name__)

class Kucoin(Exchange):
    def __init__(self, configured, yaml):
        super().__init__(configured, yaml)
        self.__client = None


    def create_client(self, is_sandbox=False):
        self.__client = Client(self.yaml, self.configured,
        is_sandbox)
        return self.__client


    
    
    