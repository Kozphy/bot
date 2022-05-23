from kucoin.client import User
from attrs import define

@define
class Kucoin_user:
    user: User = User()
    exchange: str

    @classmethod
    def from_configured(cls, configured):
        return cls(
            exchange=configured['session'],
        )
        
    
    