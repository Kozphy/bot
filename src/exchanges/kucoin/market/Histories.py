import logging
import aiohttp
from .market_api import Kucoin_market
from exchanges.utils.misc import convert_symbols_to_request_format
import asyncio
import numpy as np
import time
import pprint
from persistence.write_kline import kline_to_database
from typing import List

from .data.kline import KLine
from .data.error import ErrorMessage

logger = logging.getLogger(__name__)

class Histories(Kucoin_market):
    async def get_klines(self) -> List[KLine]:
        data = []
        # TODO: refactor
        try:
            for symbol in self.symbols:
                # data.update({symbol:{}})
                req_args = {
                    'symbol': symbol,
                    'kline_type': None,
                    'startAt': self.startAt,
                    'endAt': self.endAt,
                }

                for timeframe in self.timeframe:
                    req_args['kline_type'] = self.timeframe_format[timeframe]
                    res = await self.asy_to_thread(self.market.get_kline, req_args)

                    start = time.process_time()
                    if res:
                        # print(res)
                        for kline in res[0]:
                            ohlcv = {
                                'exchange': self.exchange,
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
                    print(f'process {symbol} {timeframe} kline consume time: ', end - start)
        except Exception as e: 
            logger.error(e)

        return data

    async def get_trade_histories(self):
        for symbol in self.symbols:
            req_args = {
                'symbol': symbol
            }
            res = await self.asy_to_thread(self.market.get_trade_histories, req_args)
        
        return res

    