from enums import RunMode
import asyncio
from typing import Dict, Any, List

from loguru import logger
from attrs import define, field
from kucoin.client import Market
from exchanges.utils.misc import convert_symbols_to_request_format, isodate_to_unixtime
# from pyrate_limiter import BucketFullException, Duration, RequestRate, Limiter
from exchanges.request_handler import Request_handler


@define(slots=False)
class Kucoin_market(Market):
    request_handler: Request_handler
    auth: Dict[str, Any]
    exchange: str
    is_sandbox: bool
    symbols: List[str]
    startAt: int
    endAt: int
    timeframes: List[str]
    # limiter: Limiter

    def __attrs_post_init__(self):
        # print(dir(self.auth))
        super().__init__(self.auth['key'], self.auth['secret'],
         self.auth['passphrase'], self.is_sandbox)


    @classmethod
    def from_config(cls, configured: Dict[str, Any], auth: Dict[str, Any]):
        req_params = cls.convert_to_request_format(cls, configured)
        exchange = configured['exchange']

        return cls(
            request_handler = Request_handler.activate(),
            auth = auth,
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


                


    
        



                