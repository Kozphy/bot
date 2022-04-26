import logging
import aiohttp
from .market_api import Kucoin_market
from bot.exchanges.misc import ms_to_seconds
import asyncio
import numpy as np


logger = logging.getLogger(__name__)

class Histories(Kucoin_market):


    async def get_klines(self):
        startAt = ms_to_seconds(self.startAt)
        endAt = ms_to_seconds(self.endAt)
        data = {}
        # TODO: refactor
        for symbol in self.symbols:
            symbol = symbol.split('/')
            symbol = symbol[0] + '-' + symbol[1]
            # print(symbol)
            # print(self.startAt)
            # print(self.endAt)

            req_args = {
                'symbol': symbol,
                'kline_type': '1day',
                'startAt': startAt,
                'endAt': endAt,
            }
            res = await self.asy_to_thread(self.market.get_kline, req_args)
            data.update({symbol: res[0]})

        result = {
            symbol: {
                'timestamp_start':'',
                'open_price':'',
                'close_price': '',
                'highest_price': '',
                'lowest_price':'',
                'Tranc_volume':'',
                'Tracn_amount':'',
            },
        },
        # print(data['BTC-USDT'])
        return data

    async def get_trade_histories(self):
        for symbol in self.symbols:
            req_args = {
                'symbol': symbol
            }
            res = await self.asy_to_thread(self.market.get_trade_histories, req_args)
        
        return res

    
