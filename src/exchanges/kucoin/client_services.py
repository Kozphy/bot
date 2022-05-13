from exchanges.kucoin.market.market_facade import market_facade
from exchanges.bbgo_grpc.market_service import bbgo_market_service


# TODO: maybe need to change code architecture
class Client_services():
    def __init__(self, configured):
        self.configured = configured
        self.bbgo_options = configured['bbgo_grpc_service']
        self.market = self.get_market_services()
        self.market_method = [f for f in dir(self.market) if not f.startswith('_')]

        if self.configured['bbgo_grpc']:
            if self.bbgo_options['market']:
                self.grpc_server_host = self.configured['bbgo_grpc_server']['host']
                self.grpc_server_port = self.configured['bbgo_grpc_server']['port']
                self.bbgo_market_service = self.get_bbgo_market_service()
                self.bbgo_market_service_method = [f for f in dir(self.bbgo_market_service) if not f.startswith('_')]
                self.bbgo_market_service_attribute = [a for a in self.bbgo_market_service.__dict__.keys()]

    # TODO: need to fix dir issue
    def __dir__(self):
        if self.bbgo_options['market']:
            return list(self.__dict__.keys()) + self.bbgo_market_service_method
        return self.__dict__.keys()

    def __getattr__(self, func):
        ## delegate pattern
        def method(*args, **kwargs):
            if self.bbgo_options['market'] and func in self.bbgo_market_service_method:
                return getattr(self.bbgo_market_service, func)(*args, **kwargs)
            if func in self.market_method:
                return getattr(self.market, func)(*args, **kwargs)
            else:
                raise AttributeError(f'{func} is not defined')
        return method


    def get_bbgo_market_service(self):
        if self.bbgo_options['market']:
            return  bbgo_market_service(self.configured, self.grpc_server_host, self.grpc_server_port)

    def get_market_services(self):
        return market_facade(self.configured)
    

