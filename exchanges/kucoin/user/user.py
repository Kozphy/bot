import logging

logger = logging.getLogger(__name__)

class Kucoin_user():
    def __init__(self, api, secrect, passphrase):
        self.__api = api
        self.__secrect = secrect
        self.__passphrase = passphrase