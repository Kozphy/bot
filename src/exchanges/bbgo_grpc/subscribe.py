import click
from loguru import logger

from bbgo import MarketService
from bbgo.data import Subscription
from bbgo.enums import ChannelType
from bbgo.enums import DepthType


@click.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=50051)
def main(host, port):
    subscriptions = [
        Subscription('kucoin', ChannelType.KLINE, symbol='BTCUSDT',
         depth=DepthType.FULL, interval='1m'),
    ]

    service = MarketService(host, port)
    service.query_klines()

    response_iter = service.subscribe(subscriptions)
    for response in response_iter:
        logger.info(response)

if __name__ == '__main__':
    main()