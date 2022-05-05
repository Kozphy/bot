import logging
import aiohttp
from .market_api import Kucoin_market
from bot.exchanges.misc import ms_to_seconds
import asyncio
import numpy as np
import time
from bot.persistence.write_kline import kline_to_database
logger = logging.getLogger(__name__)

class Histories(Kucoin_market):

    async def get_klines(self):
        startAt = ms_to_seconds(self.startAt)
        endAt = ms_to_seconds(self.endAt)
        data = {}
        # with engine.connect() as conn:
        # TODO: refactor
        for symbol in self.symbols:
            symbol = symbol.split('/')
            symbol = symbol[0] + '-' + symbol[1]
            data.update({symbol:{}})

            req_args = {
                'symbol': symbol,
                'kline_type': None,
                'startAt': startAt,
                'endAt': endAt,
            }
            for timeframe in self.timeframe:
                req_args['kline_type'] = self.timeframe_format[timeframe]
                res = await self.asy_to_thread(self.market.get_kline, req_args)

                start = time.process_time()
                if res:
                    # print(res)
                    for kline in res[0]:
                        ohlcv = {
                            'timeframe': timeframe,
                            'open': kline[1],
                            'close': kline[2],
                            'high': kline[3],
                            'low': kline[4],
                            'volumne': kline[5],
                            'amount': kline[6],
                        }

                        dt_format = {
                            kline[0]: ohlcv
                        }

                        # kline_to_database(dt_format)
                        # data[symbol])
                        data[symbol].update(dt_format)
                print(data)
                end = time.process_time() 
                print(f'process {symbol} {timeframe} kline consume time: ', end - start)
        # exit()
        # print(data)
        return

    async def get_trade_histories(self):
        for symbol in self.symbols:
            req_args = {
                'symbol': symbol
            }
            res = await self.asy_to_thread(self.market.get_trade_histories, req_args)
        
        return res

    
