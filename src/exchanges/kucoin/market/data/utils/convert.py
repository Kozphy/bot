from datetime import datetime
from typing import Union
import logging

logger = logging.getLogger(__name__)


def parse_float(s: Union[str, float]) -> float:
    if s is None:
        return 0

    if s == "":
        return 0

    return float(s)


def from_unix_timestamp_to_localdate(t: Union[str, int]) -> datetime:
    if isinstance(t, str):
        t = int(t)

    return datetime.fromtimestamp(t)
