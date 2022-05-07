import logging
import sys
from logging import Formatter, StreamHandler
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
# from bot.constants import LOG_FILE
import os

logger = logging.getLogger(__name__)

LOGFORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGFORMATED = Formatter(LOGFORMAT)

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

    logging.basicConfig(
        level=logging.DEBUG,
        format=LOGFORMAT,
        handlers=[logging.StreamHandler(sys.stderr)]
    )
    
    
# TODO: confuse this function doing
def get_existing_handlers(handlertype):
    """
    Returns Existing handler or None (if the handler has not yet been added to the root handlers).
    """

    return next((h for h in logging.root.handers if isinstance(h, handlertype)), None)

def setup_logging(config: Dict[str, Any]) -> None:
    """
    Process -v/--verbose, --logfile options
    """
    # print(config) 
    # Log level
    verbosity = config['verbosity']
    # logging.root.anddHandler()
    logfile = config.get('logfile')
    if logfile:
        # handler_rf = get_existing_handlers(RotatingFileHandler)
        # print(logfile)
        handler_rf = RotatingFileHandler(logfile, 
                                        maxBytes=1024*1024*10,
                                        backupCount=5
                                        )

        # print(handler_rf)
        handler_rf.setFormatter(LOGFORMATED)
        logging.root.addHandler(handler_rf)
        # print(logging.root.handle)


    logging.root.setLevel(logging.INFO if verbosity < 1 else logging.DEBUG)
    # print(logging.root.handle)
    logger.info(f'Verbosity set to {verbosity}')

