from kucoin.client import Market
import math
from datetime import datetime, timedelta
from bot.exchanges.kucoin.market.market import Kucoin_market
from bot.exchanges.kucoin.user.user import Kucoin_user
from bot.exchanges.kucoin.trade.trade import Kucoin_trade
from kucoin.base_request.base_request import KucoinBaseRestApi
from bot.enums import RunMode
# from bot.exchanges.kucoin import Kucoin

class Client:
    def __init__(self,yaml, configured, is_sandbox):
        self.yaml = yaml
        self.configured = configured
        # self.market = self.init_market()
        self.__api = None
        self.__secrect = None
        self.__passphrase = None
        self.__is_sandbox = is_sandbox

        yaml_key_struct = self.yaml['exchange']['apikey']
        self.__api = yaml_key_struct['public']
        self.__secrect = yaml_key_struct['secret']
        self.__passphrase = yaml_key_struct['password']

    def process_request_params(self):
        sync_dict = self.configured['sync_dict']
        require_params = {
            RunMode.SYNC: {'symbols': sync_dict['sync_pairs'], 
            'timeframe': sync_dict['timeframe'],
            'startAt': self.isodate_to_datetime_ms(self.configured['startAt']),
            'endAt': self.isodate_to_datetime_ms(self.configured['endAt'])
            },
        }
        
        if self.configured['runmode'] in require_params:
            return require_params[self.configured['runmode']]

    def init_client(self):
        params = self.process_request_params()
        # print(params)
        support_client = {
            RunMode.SYNC: Kucoin_market(**params),
            'trade': Kucoin_trade,
            'user': Kucoin_user
        }
        if self.configured['runmode'] in support_client:
            return support_client[self.configured['runmode']]
        

    @staticmethod
    def current_request_time():
        """
        Get server and local time in millisecond
        :return localtime, servertime
        """
        client = Market()
        servertime = client.get_server_timestamp()
        localtime = math.floor(datetime.today().timestamp()*1000)
        return localtime, servertime

    @staticmethod 
    def isodate_to_datetime_ms(timer):
        min_time = datetime.min.time()
        result = datetime.combine(timer, min_time).timestamp()*1000
        return round(result)

    # def request_time_format(self):
    #     determine_time = {
    #         'startAt': self.isodate_to_datetime_ms(self.configured['startAt']),
    #         'endAt': self.isodate_to_datetime_ms(self.configured['endAt']),
    #     }
    #     return determine_time['startAt'], determine_time['endAt']