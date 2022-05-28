from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Union
from decimal import Decimal

from exchanges.utils.misc import (parse_number)

@dataclass
class KLine:
    exchange: str
    symbol: str
    timeframe: str
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    amount: Decimal
    session: str = None
    start_time: Union[str,int] = None
    end_time: Union[str, int] = None
    volume: Decimal = None
    closed: bool = None

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> KLine:
        return cls(
            exchange=data['exchange'],
            symbol=data['symbol'],
            timeframe=data['timeframe'],
            open=parse_number(data['open']),
            high=parse_number(data['high']),
            low=parse_number(data['low']),
            close=parse_number(data['close']),
            volume=parse_number(data['volume']),
            amount=parse_number(data['amount']),
            start_time=data['start_time'],
            end_time=data['end_time'],
            closed=data['close'],
        )
