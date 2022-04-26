import logging
from sqlalchemy import insert
from .models import kline_table

logger = logging.getLogger(__name__)

def kline_to_database(engine, data):
    """
    Insert data to database
    """
    print(data)
    print(engine)
    exit()



    stmt = insert(kline_table).Values()

    # connect and insert
    # with engine.connect() as conn:
        