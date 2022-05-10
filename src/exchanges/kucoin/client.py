from kucoin.client import Market
from datetime import datetime, timedelta
import math
# from bot.exchanges.kucoin import Kucoin
from exchanges.kucoin.client_interface import Client_interface

class Client:
    def __init__(self, configured, is_sandbox=False):
        self.configured = configured
        self.bbgo_grpc = configured['bbgo_grpc']
        self._apikey = configured['apikey']
        self.__is_sandbox = is_sandbox
        self.accepted_pairs = None

    def init_client(self):
        client = Client_interface(self.configured)
        print(dir(client))
        # client.grpc_get_kline(self.configured)
        exit()

        # check accecpt pair and get all pairs list
        self.accepted_pairs = client.get_accept_pairs()

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