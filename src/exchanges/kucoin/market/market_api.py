from enums import RunMode
import asyncio
from typing import Dict, Any

from loguru import logger
from attrs import define, field
from kucoin.client import Market
from pyrate_limiter import BucketFullException, Duration, RequestRate, Limiter


@define(slots=False)
class Kucoin_market(Market):
    key: str
    secret: str
    passphrase: str
    is_v1api: bool
    timeframe_format: Dict[str, str] 
    exchange: str
    is_sandbox: bool

    def __attrs_post_init__(self):
        super().__init__(self.key, self.secret, self.passphrase, self.is_sandbox, self.is_v1api)


    @classmethod
    def from_config(cls, configured: Dict[str, Any]):
        exchange = configured['exchange']
        apikey = exchange['apikey']
        version_api = False if apikey['version'] == 2 else True
        return cls(
            timeframe_format = cls.get_timeframe_format(),
            key=apikey['public'],
            secret=apikey['secret'],
            is_v1api=version_api,
            passphrase=apikey['password'],
            exchange = exchange['marketplace'],
            is_sandbox = exchange['is_sandbox'],
        )
    def get_timeframe_format():
        timeframe_format = {
            '1m': '1min',
            '3m': '3min',
            '5m': '5min',
            '15m': '15min',
            '30m': '30min',
            '1h': '1hour',
            '2h': '2hour',
            '4h': '4hour',
            '6h': '6hour',
            '8h': '8hour',
            '12h': '12hour',
            '1d': '1day',
            '1w': '1week',
        }
        return timeframe_format


    async def asy_to_thread(self, fn, req_args):
        # TODO: need to fix rate limit
        # reference article: https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/
        # In considering use https://github.com/vutran1710/PyrateLimiter, or other method
        res = await asyncio.gather(
            asyncio.to_thread(fn, **req_args),
            return_exceptions=True)
        
        result = self.process_to_many_request(res, req_args.get('symbol'))
        

        return result
    
    async def process_to_many_request(self, res):
        if isinstance(res[0], Exception) == True:
            if res[0].get('code') == 429:
                logger.error(f"{res[0]}")

                