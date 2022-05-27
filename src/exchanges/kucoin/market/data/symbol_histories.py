from attrs import define
from exchanges.utils.misc import parse_number

from datetime import datetime
from typing import Dict, Any

@define
class Symbol_trade_history():
    symbol: str
    sequence: str
    ms_time: datetime
    price: str
    size: str
    side: str

    @classmethod
    def from_api(cls, history: Dict[str, Any]) -> 'Symbol_trade_history':
        return cls(
            symbol=history['symbol'],
            sequence=history['sequence'],
            ms_time=history['ms_time'],
            price=parse_number(history['price']),
            size=parse_number(history['size']),
            side=history['side'],
        )

