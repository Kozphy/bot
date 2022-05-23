from sqlalchemy import (Column, Table, MetaData,
                        Boolean)
from sqlalchemy.dialects.mysql import TIME
from sqlalchemy.types import VARCHAR, NUMERIC, BigInteger, DateTime
from sqlalchemy.schema import ForeignKey
from loguru import logger
from persistence.mysql.exchanges import exchanges_meta
# from persistence.engine import init_db_engine

# db_url = init_db_engine('mysql', 'kopher', '0270453', 'localhost', 'test')
# klines_meta = MetaData()

timeframes_table = Table("timeframes", exchanges_meta,
    Column('timeframes_id', BigInteger, nullable=False, autoincrement=True, primary_key=True),
    Column('timeframes', VARCHAR(3), nullable=False),
)

symbols_table = Table("symbols", exchanges_meta,
    Column('symbol_id', BigInteger, nullable=False, autoincrement=True, primary_key=True),
    Column('base_currency', VARCHAR(10), nullable=False),
    Column('quote_currency', VARCHAR(10), nullable=False),
)

# klines table
klines_table = Table("base_klines", exchanges_meta,
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

# exchanges_meta.create_all(db_url)

# for fkey in klines_table.foreign_keys:
#     print(fkey)