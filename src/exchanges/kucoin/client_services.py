from exchanges.kucoin.market.market_facade import Market_facade
from exchanges.bbgo_grpc.market_service import bbgo_market_service

from attrs import define
from typing import Dict, Any, Optional
from pprint import pprint

# TODO: maybe need to change code architecture
@define
class Client_services:
    market_services: Market_facade
    bbgo_options: bool
    bbgo_servies_options: Dict[str, Any]
    bbgo_server_host: Optional[str]
    bbgo_server_port: Optional[str]

    @classmethod
    def from_config(cls, configured: Dict[str, Any],
     is_sandbox: bool) -> 'Client_services':
        return cls(
            bbgo_options = configured['bbgo_grpc'],
            bbgo_servies_options = configured['bbgo_grpc_services'],
            bbgo_server_host = configured['bbgo_grpc_server']['host'],
            bbgo_server_port = configured['bbgo_grpc_server']['port'],
            # TODO: add bbgo market services
            # bbgo_market_service = cls.get_bbgo_market_service(),
            market_services = Market_facade.from_market(configured, is_sandbox),
        )

    
    # def __init__(self, configured):
    #     self.configured = configured
    #     self.bbgo_options = configured['bbgo_grpc_service']
    #     self.market_histories = self.get_market_services('histories')
    #     self.market_symbols_ticker =  
        
    #     self.market_method = [f for f in dir(self.market) if not f.startswith('_')]

    #     if self.configured['bbgo_grpc']:
    #         if self.bbgo_options['market']:
    #             self.grpc_server_host = self.configured['bbgo_grpc_server']['host']
    #             self.grpc_server_port = self.configured['bbgo_grpc_server']['port']
    #             self.bbgo_market_service = self.get_bbgo_market_service()
    #             self.bbgo_market_service_method = [f for f in dir(self.bbgo_market_service) if not f.startswith('_')]
    #             self.bbgo_market_service_attribute = [a for a in self.bbgo_market_service.__dict__.keys()]

    # TODO: need to fix dir issue
    # def __dir__(self):
    #     if self.bbgo_options['market']:
    #         return list(self.__dict__.keys()) + self.bbgo_market_service_method
    #     return self.__dict__.keys()

    # def __getattr__(self, func):
    #     ## delegate pattern
    #     def method(*args, **kwargs):
    #         if self.bbgo_options['market'] and func in self.bbgo_market_service_method:
    #             return getattr(self.bbgo_market_service, func)(*args, **kwargs)
    #         if func in self.market_method:
    #             return getattr(self.market, func)(*args, **kwargs)
    #         else:
    #             raise AttributeError(f'{func} is not defined')
    #     return method

    def get_bbgo_market_service(self):
        if self.bbgo_options['market']:
            return  bbgo_market_service(self.configured, self.grpc_server_host, self.grpc_server_port)


    

