from loguru import logger
import aiohttp
from .market_api import Kucoin_market
import asyncio
import numpy as np
import time
import pprint
from persistence.write_kline import kline_to_database
from exchanges.utils.misc import convert_symbols_to_request_format, isodate_to_unixtime
from typing import List, Dict, Any
from attrs import define, field

from .data.kline import KLine
from .data.error import ErrorMessage


@define
class Histories:
    _market_api: Kucoin_market

    @classmethod 
    def from_api(cls, configured: Dict[str, Any]):
        return cls(
            market_api=Kucoin_market.from_config(configured),
        )

    async def get_klines(self, symbols, startAt, endAt, timeframes) -> List[KLine]:
        market: Kucoin_market = self._market_api
        # exit()
        symbols = convert_symbols_to_request_format(symbols, '/', '-')
        data = []
        # TODO: refactor
        for symbol in symbols:
            # data.update({symbol:{}})
            req_args = {
                'symbol': symbol,
                'kline_type': None,
                'startAt': isodate_to_unixtime(startAt),
                'endAt': isodate_to_unixtime(endAt),
            }
            # exit()

            for timeframe in timeframes:
                req_args['kline_type'] = market.timeframe_format[timeframe]

                # print(req_args)
                # exit()
                data = await market.asy_to_thread(market.get_kline, req_args)

                start = time.process_time()
                # print(data)
                # TODO: fix to many request
                if isinstance(data[0], Exception) == True:
                    logger.error(f"{data[0]}")
                    raise Exception(data[0])

                if len(data[0]) > 0:
                    for kline in data[0]:
                        ohlcv = {
                            'exchange': market.exchange,
                            'symbol': symbol,
                            'timeframe': timeframe,
                            'start_time': kline[0],
                            'end_time': kline[0],
                            'open': kline[1],
                            'close': kline[2],
                            'high': kline[3],
                            'low': kline[4],
                            'volume': kline[5],
                            'amount': kline[6],
                            'closed': True
                        }
                        
                        data.append(KLine.from_api(ohlcv))



                # print(data)
                end = time.process_time() 
                logger.debug(f'process {symbol} {timeframe} kline consume time: {end-start}')

        return data

    async def get_trade_histories(self):
        market: Kucoin_market = self._market_api

        for symbol in market.symbols:
            req_args = {
                'symbol': symbol
            }
            res = await market.asy_to_thread(market.get_trade_histories, req_args)
        
        return res

    
