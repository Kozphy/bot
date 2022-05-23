from .symbols_ticker import Symbols_Ticker
from .Histories import Histories

from attrs import define, field
from typing import Dict, Any

@define()
class Market_facade:

    @classmethod
    def from_market(cls, configured: Dict[str, Any], is_sandbox) -> Histories:
        histories = Histories.from_api(configured, is_sandbox)
        histories_methods = cls.get_other_class_func(Histories)
        for history_method in histories_methods:
            setattr(cls, history_method, getattr(histories, history_method))

        symbols_ticker = Symbols_Ticker.from_api(configured, is_sandbox) 
        symbols_ticker_methods = cls.get_other_class_func(Symbols_Ticker)
        for symbols_ticker_method in symbols_ticker_methods:
            setattr(cls, symbols_ticker_method, getattr(symbols_ticker, symbols_ticker_method))

        return cls()


    def get_other_class_func(class_name):
        return [f for f in dir(class_name) if not f.startswith('_') and f.find('from_api')]

