from bbgo import MarketService

import click


# @click.command()
# @click.option('--host', default='127.0.0.1')
# @click.option('--port', default=50051)
def grpc_get_kline(**kwargs):
    service = MarketService(kwargs['host'], kwargs['port'])

    klines = service.query_klines(
        exchange=kwargs['exchange'],
        symbol=kwargs['symbol'],
        interval=kwargs['timeframe'],
        start_time=kwargs['start_time'],
        end_time=kwargs['end_time'],
        limit=kwargs['limit'],
    )
    # print(klines)
    print(type(klines))
    for kline in klines:
        print(kline)



