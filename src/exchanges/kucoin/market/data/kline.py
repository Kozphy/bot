from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

from exchanges.kucoin.market.data.utils.convert import (parse_float, 
from_unix_timestamp_to_localdate)

@dataclass
class KLine:
    exchange: str
    symbol: str
    open: float
    high: float
    low: float
    close: float
    amount: float
    session: str = None
    start_time: datetime = None
    end_time: datetime = None
    volume: float = None
    closed: bool = None

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> KLine:
        return cls(
            exchange=data['exchange'],
            symbol=data['symbol'],
            open=parse_float(data['open']),
            high=parse_float(data['high']),
            low=parse_float(data['low']),
            close=parse_float(data['close']),
            volume=parse_float(data['volume']),
            amount=parse_float(data['amount']),
            start_time=from_unix_timestamp_to_localdate(data['start_time']),
            end_time=from_unix_timestamp_to_localdate(data['end_time']),
            closed=data['close'],
        )
