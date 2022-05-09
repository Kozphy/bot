from sqlalchemy import (Column, Table, MetaData,
                        Integer, String, DateTime,Boolean, PrimaryKeyConstraint)
from sqlalchemy.dialects.mysql import NUMERIC as MysqlNumeric
from sqlalchemy.types import VARCHAR, NUMERIC
import logging

logger = logging.getLogger(__name__)

metadata_obj = MetaData()

# klines table
# kline_table = Table("Mysql_kucoin_kline", metadata_obj, autoload=
#     Column('Symbol', String),
#     Column('exchange', VARCHAR(10), nullable=False),
#     Column('timeframe', String),
#     Column('start_time', DateTime, primary_key=True),
#     Column('open', MysqlNumeric(16,8, unsigned=True), nullable=False),
#     Column('close', MysqlNumeric(16,8, unsigned=True), nullable=False),
#     Column('high', MysqlNumeric(16,8, unsigned=True), nullable=False),
#     Column('low', MysqlNumeric(16,8, unsigned=True), nullable=False),
#     Column('volume', NUMERIC(20,8)),
#     Column('amount', NUMERIC(20,8)),
# )

