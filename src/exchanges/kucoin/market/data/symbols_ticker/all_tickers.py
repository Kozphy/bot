from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Union
from decimal import Decimal
from exchanges.utils.misc import (parse_number)

@dataclass
class All_tickers:
    exchange: str
    time: Union[str, int]
    symbol: str
    symbolName: str
    buy: Decimal
    sell: Decimal
    changeRate: Decimal
    changePrice: Decimal
    high: Decimal
    low: Decimal
    vol: Decimal
    volValue: Decimal
    last: Decimal
    averagePrice: Decimal
    takerFeeRate: Decimal
    makerFeeRate: Decimal
    takerCoefficient: Decimal
    makerCoefficient: Decimal

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> All_tickers:
        return cls(
            exchange=data['exchange'],
            time=data['time'],
            symbol=data['symbol'],
            symbolName=data['symbolName'],
            buy=parse_number(data['buy']),
            sell=parse_number(data['sell']),
            changeRate=parse_number(data['changeRate']),
            changePrice=parse_number(data['changePrice']),
            high=parse_number(data['high']),
            low=parse_number(data['low']),
            vol=parse_number(data['vol']),
            volValue=parse_number(data['volValue']),
            last=parse_number(data['last']),
            averagePrice=parse_number(data['averagePrice']),
            takerFeeRate=parse_number(data['takerFeeRate']),
            makerFeeRate=parse_number(data['makerFeeRate']),
            takerCoefficient=parse_number(data['takerCoefficient']),
            makerCoefficient=parse_number(data['makerCoefficient'])
        )
