from datetime import datetime
from typing import Union
from decimal import Decimal

def convert_symbols_to_request_format(pairs, in_delimiter=None, out_delimiter=None):
    """
    convert symbols to request format
    :param pairs:
    :return: list
    """
    result = []
    for pair in pairs:
        pair = pair.split(in_delimiter)
        if out_delimiter is None:
            pair = pair[0] + pair[1]
            result.append(pair)
            continue

        pair = pair[0] + out_delimiter + pair[1]
        result.append(pair)
    return result

# process time
def isodate_to_datetime_ms(timer):
    min_time = datetime.min.time()
    result = datetime.combine(timer, min_time).timestamp()*1000
    return round(result)

def ms_to_seconds(timer):
    result = round(timer/1000)
    return result

def ms_to_localtime(t: Union[str, int]) -> datetime:
    if isinstance(t, str):
        t = int(t)

    return datetime.fromtimestamp(t/1000)

def isodate_to_unixtime(timer):
    return ms_to_seconds(isodate_to_datetime_ms(timer))


def parse_number(s: Union[str, float]) -> Decimal:
    if s is None:
        return 0

    if s == "":
        return 0

    return Decimal(s)

def unix_timestamp_to_localtime(t: Union[str, int]) -> datetime:
    if isinstance(t, str):
        t = int(t)

    return datetime.fromtimestamp(t)

