import logging
from kucoin.client import Market
import math
from datetime import datetime

logger = logging.getLogger(__name__)

class Kucoin_market():
    def __init__(self, symbols, timeframe, startAt, endAt, is_sandbox=False):
        self.market = Market()
        self.is_sandbox = is_sandbox
        self.symbols =  symbols
        self.timeframe = timeframe
        self.startAt = startAt
        self.endAt = endAt
    



