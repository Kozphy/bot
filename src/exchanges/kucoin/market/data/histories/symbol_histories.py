from attrs import define
from exchanges.utils.misc import parse_number

from decimal import Decimal
from datetime import datetime
from typing import Dict, Any

@define
class Symbol_history:
    exchange: str
    symbol: str
    sequence: str
    ms_time: datetime
    price: Decimal
    size: Decimal
    side: str

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> 'Symbol_history':
        return cls(
            exchange= data['exchange'],
            symbol=data['symbol'],
            sequence=data['sequence'],
            ms_time=data['ms_time'],
            price=parse_number(data['price']),
            size=parse_number(data['size']),
            side=data['side'],
        )

