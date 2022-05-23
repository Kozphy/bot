from sqlalchemy import (Column, Table, MetaData,
                        Integer, String, DateTime,Boolean, PrimaryKeyConstraint)
from sqlalchemy.types import VARCHAR, NUMERIC, BigInteger
from loguru import logger


exchanges_meta = MetaData()

# klines table
exchanges_table = Table("exchanges", exchanges_meta,
    Column('exchange_id', BigInteger, nullable=False, autoincrement=True, primary_key=True),
    Column('exchange', VARCHAR(10), nullable=False),
)