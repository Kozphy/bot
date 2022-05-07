from datetime import datetime

def split_pairs_to_request_format(pairs):
    """
    Split pairs to request format
    :param pairs:
    :return:
    """
    result = []
    for pair in pairs:
        pair = pair.split('/')
        pair = pair[0] + '-' + pair[1]
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
