from sqlalchemy import (Column, Table, MetaData,
                        Boolean)
from sqlalchemy.dialects.mysql import TIME
from sqlalchemy.types import NUMERIC, BigInteger
from sqlalchemy.schema import ForeignKey


kucoin_kline_meta = MetaData()

# klines table
klines_table = Table("base_klines", kucoin_kline_meta,
    Column('kline_id', BigInteger, nullable=False, autoincrement=True, primary_key=True),
    Column('exchange_id', BigInteger, ForeignKey("exchanges.exchange_id"), nullable=False),
    Column('symbol_id', BigInteger, ForeignKey("symbols.symbol_id"), nullable=False),
    Column('timeframes_id',BigInteger, ForeignKey("timeframes.timeframes_id"), nullable=False),
    Column('start_time', TIME(fsp=3), nullable=False),
    Column('end_time', TIME(fsp=3), nullable=False),
    Column('open', NUMERIC(28,13), nullable=False),
    Column('high',NUMERIC(28,13), nullable=False),
    Column('low',NUMERIC(28,13), nullable=False),
    Column('close',  NUMERIC(28,13), nullable=False),
    Column('volume', NUMERIC(28,13), nullable=False, default=0),
    Column('amount', NUMERIC(28,13), nullable=False, default=0),
    Column('closed', Boolean, nullable=False, default=True),
)
