from datetime import datetime
from decimal import Decimal
from typing import Union
import logging
from loguru import logger



def parse_number(s: Union[str, float]) -> Decimal:
    if s is None:
        return 0

    if s == "":
        return 0

    return Decimal(s)


def from_unix_timestamp_to_localdate(t: Union[str, int]) -> datetime:
    if isinstance(t, str):
        t = int(t)

    return datetime.fromtimestamp(t)
