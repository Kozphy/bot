from kucoin.client import Market
import math
from datetime import datetime, timedelta
from bot.exchanges.kucoin.market.market_interface import market_interface
from bot.exchanges.kucoin.user.user import Kucoin_user
from bot.exchanges.kucoin.trade.trade import Kucoin_trade
# from kucoin.base_request.base_request import KucoinBaseRestApi
from ..misc import isodate_to_datetime_ms
from bot.enums import RunMode
# from bot.exchanges.kucoin import Kucoin

class Client:
    def __init__(self, yaml, configured, is_sandbox):
        self.yaml = yaml
        self.configured = configured
        yaml_key_struct = self.yaml['exchange']['apikey']
        self.__api = yaml_key_struct['public']
        self.__secrect = yaml_key_struct['secret']
        self.__passphrase = yaml_key_struct['password']
        self.__is_sandbox = is_sandbox
        self.accepted_pairs = None
            
    def process_request_params(self):
        """
        Process api request parameters
        """
        sync_dict = self.configured['sync_dict']
        symbols = sync_dict['sync_pairs']

        if self.configured['runmode'] != RunMode.SYNC:
            symbols = self.configured['trade_pairs']
            
        require_params = {
            RunMode.SYNC: {
                'symbols': symbols, 
                'timeframe': sync_dict['timeframe'],
                'startAt': isodate_to_datetime_ms(self.configured['startAt']),
                'endAt': isodate_to_datetime_ms(self.configured['endAt'])
            },
            RunMode.LIVE: {
                'symbols': symbols,
            },
            RunMode.BACKTEST:{
                'symbols': symbols,
            },
        }
        
        if self.configured['runmode'] in require_params:
            return require_params[self.configured['runmode']]

    def init_client(self):
        params = self.process_request_params()
        # print(params)
        market_client = market_interface(**params)
        support_client = {
            RunMode.SYNC: market_client,
            'trade': Kucoin_trade,
            'user': Kucoin_user
        }

        # check accecpt pair and get all pairs list
        self.accepted_pairs = market_client.get_accept_pairs()
        print(self.configured['startAt'])
        print(self.configured['endAt'])

        if self.configured['runmode'] in support_client:
            client = support_client[self.configured['runmode']]
            return client 

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

    # def request_time_format(self):
    #     determine_time = {
    #         'startAt': self.isodate_to_datetime_ms(self.configured['startAt']),
    #         'endAt': self.isodate_to_datetime_ms(self.configured['endAt']),
    #     }
    #     return determine_time['startAt'], determine_time['endAt']