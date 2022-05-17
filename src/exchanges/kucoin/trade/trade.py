from kucoin.client import Trade


class Kucoin_trade(Trade):
    def __init__(self, api=None, secrect=None, passphrase=None):
        self.__api = api
        self.__secrect = secrect
        self.__passphrase = passphrase
        # self.market = None
        # self.User = None
        # self.trade = None
        # self.client = None
    