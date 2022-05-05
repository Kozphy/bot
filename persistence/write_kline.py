import logging
from sqlalchemy import insert
from .models import kline_table

logger = logging.getLogger(__name__)

def kline_to_database(engine, data):
    """
    Insert data to database
    """
    print(engine)
    print(data)
    # kline = convert_kline_format(data)
    # print(data)
    # print(engine)
    # exit()



    # stmt = insert(kline_table).Values()

    # connect and insert
    # with engine.connect() as conn:
        
def convert_kline_format(data):
    """
    Convert kline format
    """
    # print(data)