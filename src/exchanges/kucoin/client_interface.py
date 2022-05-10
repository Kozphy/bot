from exchanges.kucoin.market.market_facade import market_facade
from exchanges.bbgo_grpc.market_service import bbgo_market_service

class NonDelegatableItem(AttributeError):
    pass

class Client_interface():
    def __init__(self, configured):
        self.configured = configured
        self.bbgo_options = configured['bbgo_grpc_service']
        self.market = self.get_market_interface()
        self.market_method = [f for f in dir(self.market) if not f.startswith('_')]

        if self.configured['bbgo_grpc']:
            self.bbgo_market_service = self.get_bbgo_market_service()
            self.bbgo_market_service_method = [f for f in dir(self.bbgo_market_service) if not f.startswith('_')]
            self.bbgo_market_service_attribute = [a for a in self.bbgo_market_service.__dict__.keys()]


        # print(self.bbgo_market_service_method)
        # print('\n')
        # print(self.market_method)
    
    def __getattr__(self, func):
        ## delegate pattern
        def method(*args):
            if func in self.bbgo_market_service_method:
                return getattr(self.bbgo_market_service, func)(*args)
            if func in self.market_method:
                return getattr(self.market, func)(*args)
            else:
                raise AttributeError(f'{func} is not defined')
        return method


    def get_bbgo_market_service(self):
        if self.bbgo_options['market']:
            return  bbgo_market_service()

    def get_market_interface(self):
        return market_facade(self.configured)
    

