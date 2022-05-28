from symtable import Symbol
from .symbols_ticker import Symbols_Ticker
from .histories import Histories

from attrs import define, field
from typing import Dict, Any

@define
class Market_facade:
    histories: Histories
    symbols_ticker: Symbols_Ticker

    #TODO: fix annotation issue
    # @classmethod
    # def from_market(cls, configured: Dict[str, Any], is_sandbox) -> 'Market_facade':
    #     histories = Histories.from_api(configured, is_sandbox)
    #     histories_methods = cls.get_other_class_func(Histories)
    #     for history_method in histories_methods:
    #         setattr(cls, history_method, getattr(histories, history_method))

    #     symbols_ticker = Symbols_Ticker.from_api(configured, is_sandbox) 
    #     symbols_ticker_methods = cls.get_other_class_func(Symbols_Ticker)
    #     for symbols_ticker_method in symbols_ticker_methods:
    #         setattr(cls, symbols_ticker_method, getattr(symbols_ticker, symbols_ticker_method))

    #     return cls()

    @classmethod
    def from_client(cls, configured: Dict[str, Any], auth) -> 'Market_facade':
        return cls(
            histories=Histories.from_facade(configured, auth),
            symbols_ticker=Symbols_Ticker.from_facade(configured, auth),
        )


    # def get_other_class_func(class_name):
    #     return [f for f in dir(class_name) if not f.startswith('_') and f.find('from_api')]

