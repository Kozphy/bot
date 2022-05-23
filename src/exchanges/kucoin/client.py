from kucoin.client import Market
from datetime import datetime, timedelta
import math
from exchanges.kucoin.client_services import Client_services
import pprint
import inspect

class Client:
    def __init__(self, configured, is_sandbox=False):
        self.configured = configured
        self.__is_sandbox = is_sandbox
        self.accepted_pairs = None

    def active_service(self, is_sandbox=False):
        client = Client_services.from_config(self.configured,
         is_sandbox=is_sandbox)

        # check accecpt pair and get all pairs list
        self.accepted_pairs = client.market_services.get_accept_pairs()
        # pprint.pprint(self.accepted_pairs)
        # exit()

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

