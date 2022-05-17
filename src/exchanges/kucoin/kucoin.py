from exchanges import Exchange
# from kucoin.client import Market, User, Trade
# from bot.exchanges.kucoin.market.market import Kucoin_market
# from bot.exchanges.kucoin.trade.trade import Kucoin_trade
# from bot.exchanges.kucoin.user.user import Kucoin_user


class Kucoin(Exchange):
    def __init__(self, configured):
        super().__init__(configured)
        # get_para = {
        #     'host': '127.0.0.1',
        #     'port': 50051,
        #     'exchange': 'kucoin',
        #     'symbol' : 'DOTUSDT',
        #     'timeframe': '4h',
        #     'start_time': 1651408281,
        #     'end_time': 1651840281,
        #     'limit':30
        # }
        # grpc_get_kline(**get_para)
        # from bot.persistence.migrations import migrations_update, migrations_downgrade
        # migrations_update(configured)
        # migrations_downgrade(configured)
    
    # def migration():
    #     migrations_downgrade(configured)
    #     show_history(configured)
        





    
    
    