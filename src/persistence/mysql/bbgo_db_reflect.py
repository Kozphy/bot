from sqlalchemy import (Column, Table, MetaData,
                        Integer, String, DateTime,Boolean, PrimaryKeyConstraint)
from sqlalchemy.types import VARCHAR, NUMERIC, BigInteger
from loguru import logger
from persistence.engine import init_db_engine

# MysqlNumeric(16,8, unsigned=True)


bbgo_db_meta = MetaData()
# TODO: the paramaters must load from yaml file
db_url = init_db_engine('mysql', 'kopher', '0270453', 'localhost', 'bbgo')
bbgo_db_meta.reflect(bind=db_url)

