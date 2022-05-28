from loguru import logger
import re
import aiohttp
from exceptions import BotException
import numpy as np
import time
from .market_api import Kucoin_market

from attrs import define, field
from typing import Dict, Any, List
from .data.symbols_ticker.all_tickers import All_tickers

@define
class Symbols_Ticker:
    _market_api: Kucoin_market

    
    @classmethod
    def from_facade(cls, configured: Dict[str, Any], auth) -> Kucoin_market:
        return cls(
            market_api=Kucoin_market.from_config(configured, auth)
        )

    def get_accept_pairs(self):
        """
        get available pairs in exchange
        :return available pairs :list
        """
        market: Kucoin_market = self._market_api

        pairs = market.request_handler.request_api(market.get_all_tickers, async_bool=False)
        available_pairs = [pair['symbolName'] for pair in pairs['ticker']]
        # r = re.compile(reg)
        # TODO: filter not very understand why this syntax work
        # pairs_done = list(filter(r.match, origin_pairs))
        return available_pairs
    
        
    def check_accept_pairs(self, available_pairs) -> None:
        """
        check pairs in config file whether valid in exchange
        :return None
        """
        # start = time.time()
        market: Kucoin_market = self._market_api

        Not_accept = []
        for symbol in market.symbols:
            if symbol not in available_pairs:
                Not_accept.append(symbol)

        if len(Not_accept) > 0:
            raise(BotException(f"{Not_accept} not accept pair in exchange"))

        return None

        # stop = time.time()
        # print('Time: ', stop - start)
    
    
    def get_all_tickers_current_info(self):
        """
        Request market tickers for all the trading pairs in the market (including 24h volume).
        """
        market: Kucoin_market = self._market_api
        
        res = market.request_handler.request_api(market.get_all_tickers, async_bool=False)
        """response
        {
            "time":1602832092060,
            "ticker":[
                {
                    "symbol": "BTC-USDT",   // symbol
                    "symbolName":"BTC-USDT", // Name of trading pairs, it would change after renaming
                    "buy": "11328.9",   // bestAsk
                    "sell": "11329",    // bestBid
                    "changeRate": "-0.0055",    // 24h change rate
                    "changePrice": "-63.6", // 24h change price
                    "high": "11610",    // 24h highest price
                    "low": "11200", // 24h lowest price
                    "vol": "2282.70993217", // 24h volume，the aggregated trading volume in BTC
                    "volValue": "25984946.157790431",   // 24h total, the trading volume in quote currency of last 24 hours
                    "last": "11328.9",  // last price
                    "averagePrice": "11360.66065903",   // 24h average transaction price yesterday
                    "takerFeeRate": "0.001",    // Basic Taker Fee
                    "makerFeeRate": "0.001",    // Basic Maker Fee
                    "takerCoefficient": "1",    // Taker Fee Coefficient
                    "makerCoefficient": "1" // Maker Fee Coefficient
                }
            ]
        }
        """

        data = []

        if res:
            for ticker_info in range(len(res['ticker'])):
                ticker = res['ticker'][ticker_info]
                ticker = {
                    'exchange': market.exchange,
                    'time': res['time'],
                    'symbol': ticker['symbol'],
                    'symbolName': ticker['symbolName'],
                    'buy': ticker['buy'],
                    'sell': ticker['sell'],
                    'changeRate': ticker['changeRate'],
                    'changePrice': ticker['changePrice'],
                    'high': ticker['high'],
                    'low': ticker['low'],
                    'vol': ticker['vol'],
                    'volValue': ticker['volValue'],
                    'last': ticker['last'],
                    'averagePrice': ticker['averagePrice'],
                    'takerFeeRate': ticker['takerFeeRate'],
                    'makerFeeRate': ticker['makerFeeRate'],
                    'takerCoefficient': ticker['takerCoefficient'],
                    'makerCoefficient': ticker['makerCoefficient']
                }
                data.append(All_tickers.from_api(ticker))
        return data
            

        

