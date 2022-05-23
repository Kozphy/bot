from loguru import logger
import aiohttp
from .market_api import Kucoin_market
import asyncio
import numpy as np
import time
import pprint
from persistence.write_kline import kline_to_database

from typing import List, Dict, Any
from attrs import define, field
from .data.kline import KLine
from .data.error import ErrorMessage


@define
class Histories:
    _market_api: Kucoin_market


    @classmethod 
    def from_api(cls, configured: Dict[str, Any], is_sandbox):
        return cls(
            market_api=Kucoin_market.from_config(configured, is_sandbox)
        )

    async def get_klines(self) -> List[KLine]:
        market: Kucoin_market = self._market_api
        # print(market)
        # exit()

        data = []
        # TODO: refactor
        for symbol in market.symbols:
            # data.update({symbol:{}})
            req_args = {
                'symbol': symbol,
                'kline_type': None,
                'startAt': market.startAt,
                'endAt': market.endAt,
            }

            for timeframe in market.timeframes:
                req_args['kline_type'] = market.timeframe_format[timeframe]
                res = await market.asy_to_thread(market.get_kline, req_args)

                start = time.process_time()
                # TODO: fix to many request
                if isinstance(res[0], Exception) == True:
                    logger.error(f"{res[0]}")
                    raise
                if res:
                    # print(res)
                    for kline in res[0]:
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
                        

                        # dt_format = {
                        #     kline[0]: ohlcv
                        # }
                        # pprint.pprint(ohlcv)
                        # data[symbol].update(dt_format)
                        data.append(KLine.from_api(ohlcv))

                        # error = ErrorMessage.from_api(res)
                        # if error.code != 0:
                        #     logger.error(error.message)

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

    
