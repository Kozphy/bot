from loguru import logger
import sys
from logging import Formatter, StreamHandler
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
# from bot.constants import LOG_FILE
import os
LOGFORMAT = '{time:YYYY-MM-DD HH:mm:ss,SSS} - {name} - {level} - {message}'
# LOGFORMATED = Formatter(LOGFORMAT)

def _set_thirdlib_loggers(verbosity: int = 0, api_verbosity:str = 'info') -> None:
    """
    Set logging level for third party libraries
    :return None
    """
    pass


def setup_logging_pre() -> None:
    """
    Early setup for logging.
    Uses DEBUG loglevel and only the Streamhandler.
    Early messages (before proper logging setup) will therefore only be sent to additional
    logging handlers after the real initialization, because we don't know which
    ones the user desires beforehand.
    """
    # config = {
    #     "handlers" : [
    #         dict(sink=sys.stderr, format=LOGFORMAT, level='DEBUG', serialize=False),
    #     ],
    # }

    # logger.configure(**config)
    logger.remove()
    logger.add(sys.stderr,level='DEBUG')

    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format=LOGFORMAT,
    #     handlers=[logging.StreamHandler(sys.stderr)]
    # )
    
    
# TODO: confuse this function doing
# def get_existing_handlers(handlertype):
#     """
#     Returns Existing handler or None (if the handler has not yet been added to the root handlers).
#     """

#     return next((h for h in logging.root.handers if isinstance(h, handlertype)), None)

def setup_logging(config: Dict[str, Any]) -> None:
    """
    Process -v/--verbose, --logfile options
    """
    # Log level
    verbosity = config['verbosity']
    # print(verbosity)
    logfile = config.get('logfile')
    # print(logfile)
    loglevel = 'INFO' if verbosity < 1 else 'DEBUG'
    logger.remove()
    logger.add(sys.stderr, level=loglevel)
    

    if logfile:
        logger.add(logfile, level=loglevel, format=LOGFORMAT,
         rotation='10MB')
        # handler_rf = get_existing_handlers(RotatingFileHandler)
        # print(logfile)
        # handler_rf = RotatingFileHandler(logfile, 
        #                                 maxBytes=1024*1024*10,
        #                                 backupCount=5
        #                                 )

        # print(handler_rf)
        # handler_rf.setFormatter(LOGFORMATED)
        # logging.root.addHandler(handler_rf)
        # .handle)

    # print(logging.root.handle)
    logger.info(f'Verbosity set to {verbosity}')

