import logging 
from bot.exchanges import Exchange
# from kucoin.client import Market, User, Trade
# from bot.exchanges.kucoin.market.market import Kucoin_market
# from bot.exchanges.kucoin.trade.trade import Kucoin_trade
# from bot.exchanges.kucoin.user.user import Kucoin_user
from datetime import datetime
import time
import math

logger = logging.getLogger(__name__)

class Kucoin(Exchange):
    def __init__(self, configured, yaml):
        super().__init__(configured, yaml)
        from bot.persistence.migrations import migrations_update
        migrations_update(configured)
    
    # def migration():
    #     migrations_downgrade(configured)
    #     show_history(configured)
        





    
    
    