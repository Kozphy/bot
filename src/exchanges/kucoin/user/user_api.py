from kucoin.client import User
from attrs import define, field
from exchanges.request_handler import Request_handler

@define
class Kucoin_user(User):
    request_handler: Request_handler 
    key: str
    secret: str
    passphrase: str
    is_v1api: bool
    exchange: str
    is_sandbox: bool


    @classmethod
    def from_configured(cls, configured):
        return cls(
            exchange=configured['session'],
        )
        
    
    