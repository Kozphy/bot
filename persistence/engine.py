"""
Contain database metaclass
"""
import logging
from sqlalchemy import create_engine



logger = logging.getLogger(__name__)

support_databases = {
    'MYSQL': "mysql+mysqldb://"
}

support_ssl = ['MYSQL']

def init_db(db, user, password, host, dbname, port, charset="utf8mb4", ssl=False, echo=True, future=True) -> None:
        """Initialize the database engine"""
        db = db.upper()

        if db not in support_databases:
            raise Exception("Database not supported")
        try:
            db_url = f"{support_databases[db]}{user}:{password}@{host}:{port}/{dbname}?charset={charset}"

            if db not in support_ssl or ssl == False:
                engine = create_engine(db_url, echo=echo, future=future)
                return engine

            # TODO: not set now, need to set
            connect_args ={
                "ssl": {
                    "ssl_ca": "/etc/mysql/ca-cert.pem",
                    "ssl_cert": "/etc/mysql/client-cert.pem",
                    "ssl_key": "/etc/mysql/client-key.pem"
                }
            }

            engine = create_engine(db_url, connect_args, echo=echo, future=future)
            return engine
            
        except Exception as e:
            logger.error(e)
            raise Exception("Database connection failed")

