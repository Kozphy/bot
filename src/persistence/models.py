from sqlalchemy import (Column, Table, MetaData,
                        Integer, String, DateTime,Boolean, PrimaryKeyConstraint)
from sqlalchemy.types import VARCHAR, NUMERIC
from loguru import logger

# MysqlNumeric(16,8, unsigned=True)


metadata_obj = MetaData()

# metadata_obj.reflect()
# klines table
kline_table = Table("kline", metadata_obj,
    Column('Symbol', VARCHAR(20), nullable=False),
    Column('exchange', VARCHAR(10), nullable=False),
    Column('timeframe', VARCHAR(3), nullable=False),
    Column('start_time', DateTime, primary_key=True),
    Column('open', NUMERIC(20,8), nullable=False),
    Column('close',  NUMERIC(20,8), nullable=False),
    Column('high',NUMERIC(20,8), nullable=False),
    Column('low',NUMERIC(20,8), nullable=False),
    Column('volume', NUMERIC(20,8)),
    Column('amount', NUMERIC(20,8)),
)

