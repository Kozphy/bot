from datetime import datetime

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

def isodate_to_unixtime(timer):
    return ms_to_seconds(isodate_to_datetime_ms(timer))


