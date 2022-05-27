from loguru import logger
import aiohttp
from .market_api import Kucoin_market
import asyncio
import numpy as np
import time
import pprint
from typing import List, Dict, Any
from attrs import define, field

from .data.kline import KLine
from .data.symbol_histories import Symbol_trade_history


@define
class Histories:
    _market_api: Kucoin_market

    @classmethod 
    def from_api(cls, configured: Dict[str, Any]):
        return cls(
            market_api=Kucoin_market.from_config(configured),
        )

    def get_klines(self) -> List[KLine]:
        market: Kucoin_market = self._market_api
        task = []
        data = []

        # TODO: refactor
        for symbol in market.symbols:
            for timeframe in market.timeframes:
                req_args = {
                    'symbol': symbol,
                    'kline_type': timeframe,
                    'startAt': market.startAt,
                    'endAt': market.endAt,
                }
                task.append(req_args)

        start_reqesut_time = time.time()
        res = market.request_api(market.get_kline, task, async_bool=True)
        end_request_time = time.time()
        logger.debug(f'request klines consume time: {end_request_time-start_reqesut_time}')
        # print(task)
        # print(res[0])
        # exit()
        # TODO: fix to many request
        if len(res) > 0:
            for i in range(len(res)):
                start = time.time()
                for kline in res[i]:
                    """
                    volume: Transaction volume
                    amount: Transaction amount

                    Note: 
                    Only have start time of the candle cycle in get klines api
                    """
                    ohlcv = {
                        'exchange': market.exchange,
                        'symbol': task[i]['symbol'],
                        'timeframe': task[i]['kline_type'],
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
                end= time.time()
                logger.debug(f"process {task[i]['symbol']} {task[i]['kline_type']} kline cunsume {end - start}")

        data = np.array(data, dtype=KLine)
        # exit()

        return data

    def get_symbol_histories(self):
        market: Kucoin_market = self._market_api

        data = []

        for symbol in market.symbols:
            req_args = {
                'symbol': symbol
            }
            res = market.request_api(market.get_trade_histories, req_args, async_bool=True)
        
            if isinstance(res[0], Exception) == True:
                logger.error(f"{res[0]}")
                raise Exception(res[0])
            
            if len(res[0]) > 0:
                for symbol_history in res[0]:
                    """
                    sequence: Sequence number
                    time: Transaction time (milliseconds.)
                    price: Filled price
                    size: Filled amount
                    side: Filled side. The filled side is set to the taker by default

                    Note:
                    The trade side indicates the taker order side. 
                    A taker order is the order that was matched with orders opened on the order book.
                    """
                    histories = {
                        'symbol': symbol,
                        'sequence': symbol_history['sequence'],
                        'ms_time': symbol_history['time'],
                        'price': symbol_history['price'],
                        'size': symbol_history['size'],
                        'side': symbol_history['side'],
                    }

                    data.append(Symbol_trade_history.from_api(histories))
        
        data = np.array(data)
                
        return data 

    
