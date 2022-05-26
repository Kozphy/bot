from enums import RunMode
import asyncio
from typing import Dict, Any, List

from loguru import logger
from attrs import define, field
from kucoin.client import Market
from exchanges.utils.misc import convert_symbols_to_request_format, isodate_to_unixtime
# from pyrate_limiter import BucketFullException, Duration, RequestRate, Limiter


@define(slots=False)
class Kucoin_market(Market):
    key: str
    secret: str
    passphrase: str
    is_v1api: bool
    # timeframe_format: Dict[str, str] 
    exchange: str
    is_sandbox: bool
    symbols: List[str]
    startAt: int
    endAt: int
    timeframes: List[str]
    # limiter: Limiter

    def __attrs_post_init__(self):
        super().__init__(self.key, self.secret, self.passphrase, self.is_sandbox, self.is_v1api)


    @classmethod
    def from_config(cls, configured: Dict[str, Any]):
        req_params = cls.convert_to_request_format(cls, configured)
        exchange = configured['exchange']
        apikey = exchange['apikey']
        version_api = False if apikey['version'] == 2 else True
        return cls(
            # timeframe_format = cls.get_timeframe_format(),
            key=apikey['public'],
            secret=apikey['secret'],
            is_v1api=version_api,
            passphrase=apikey['password'],
            exchange = exchange['marketplace'],
            is_sandbox = exchange['is_sandbox'],
            symbols = req_params['symbols'],
            startAt = req_params['startAt'],
            endAt = req_params['endAt'],
            timeframes = req_params['timeframes'],
        )
    def convert_to_request_format(self, configured):
        req_para = {}
        timeframe_format = self.get_timeframe_format()
        if configured['common']['runmode'] == RunMode.SYNC:
            sync_format = {
                'symbols': convert_symbols_to_request_format(configured['sync']['sync_symbols'], '/', '-'),
                'startAt': isodate_to_unixtime(configured['sync']['startAt']),
                'endAt': isodate_to_unixtime(configured['sync']['endAt']),
                'timeframes': [],
            }

            for timeframe in configured['sync']['timeframes']:
                sync_format['timeframes'].append(timeframe_format[timeframe])

            req_para.update(sync_format)
        return req_para

    def get_timeframe_format() -> Dict[str, str]:
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
        
        # result = self.process_to_many_request(res, req_args.get('symbol'))
        

        return res
    
    # async def process_to_many_request(self, res):
    #     if isinstance(res[0], Exception) == True:
    #         if res[0].get('code') == 429:
    #             logger.error(f"{res[0]}")


                