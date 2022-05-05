from ast import Num
from sqlalchemy import (Column, Table, MetaData,
                        Integer, String, DateTime,Boolean, PrimaryKeyConstraint)
from sqlalchemy.dialects.mysql import NUMERIC as MysqlNumeric
import logging



logger = logging.getLogger(__name__)

metadata_obj = MetaData()

# klines table
kline_table = Table("kline", metadata_obj,
    Column('Symbol', String),
    Column('timeframe', String),
    Column('TimeStamp', DateTime, primary_key=True),
    Column('open', MysqlNumeric(16,8, unsigned=True), nullable=False),
    Column('close', MysqlNumeric(16,8, unsigned=True), nullable=False),
    Column('high',MysqlNumeric(16,8, unsigned=True), nullable=False),
    Column('low',MysqlNumeric(16,8,unsigned=True), nullable=False),
    Column('volume', MysqlNumeric(16,8, unsigned=True)),
    Column('amount', MysqlNumeric(16,8,unsigned=True)),
)

