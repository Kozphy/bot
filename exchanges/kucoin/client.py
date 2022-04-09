from kucoin.client import Market
import math
from datetime import datetime, timedelta
# from bot.exchanges.kucoin import Kucoin

class Client:
    # def __init__(self,api, secrect, passphrase):
    #     self.__api = api
    #     self.__secrect = secrect
    #     self.__passphrase = passphrase


    def current_request_time():
        """
        Get server and local time in millisecond
        :return localtime, servertime
        """
        client = Market()
        servertime = client.get_server_timestamp()
        localtime = math.floor(datetime.today().timestamp()*1000)
        return localtime, servertime

    # def request():