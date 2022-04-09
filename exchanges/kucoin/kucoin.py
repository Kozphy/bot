import logging 
from bot.exchanges import Exchange
# from kucoin.client import Market, User, Trade
from bot.exchanges.kucoin.market.market import Kucoin_market
from bot.exchanges.kucoin.trade.trade import Kucoin_trade
from bot.exchanges.kucoin.user.user import Kucoin_user
# from bot.exchanges.kucoin.client import Client
from datetime import datetime
import time
import math

logger = logging.getLogger(__name__)

class Kucoin(Exchange):
    def __init__(self, configured, yaml):
        super().__init__(configured, yaml)
        self.__api = None
        self.__secrect = None
        self.__passphrase = None


        yaml_key_struct = self.yaml['exchange']['apikey']
        self.__api = yaml_key_struct['public']
        self.__secrect = yaml_key_struct['secret']
        self.__passphrase = yaml_key_struct['password']
        # print(self.__api)
        # print(self.__secrect)
        # print(self.__passphrase)
    

    def init_market(self, is_sandbox=False):
        return Kucoin_market(is_sandbox=is_sandbox)
        # self.client = Market()
    
    def init_user(self, is_sandbox=False):
        return Kucoin_user(is_sandbox)
        self.client = User(self, is_sandbox=False)

    def init_trade(self, is_sandbox=True):
        return Kucoin_trade(is_sandbox=is_sandbox)

    def request_time_format(self):

        print(self.configured['startAt'], self.configured['endAt'])
        # print(time.isoformat(datetime.today()))
        current_time = round(time.time() * 1000)
        print(current_time)  
        request_time_format = round(datetime.today().timestamp()*1000)
        print(type(request_time_format))


    # @property
    # def client(self):
    #     return self.client

    # @property.setter
    # def client(self, api, secrect, passphrase):
    #     Client(api, secret)
    # @property
    # def api(self):
    #     return None

    # @api.setter
    # def set_api(self, api):
    #     self._api = api

    # @property    
    # def sec_api(self):
    #     return None

    # @sec_api.setter
    # def sec_api(self, secrect):
    #     self._secrect = secrect

    # @property
    # def passphrase(self):
    #     return None
    
    # @passphrase.setter
    # def passphrase(self, passphrase):
    #     self._passphrase = passphrase
    
    
    