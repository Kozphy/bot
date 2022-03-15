import logging
import sys
from logging import Formatter, StreamHandler
from typing import Any, Dict

logger = logging.getLogger(__name__)

LOGFORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def _set_thirdlib_loggers(verbosity: int = 0, api_verbosity:str = 'info') -> None:
    """
    Set logging level for third party libraries
    :return None
    """
    pass


def setup_logging_pre() -> None:
    """
    Early setup for logging.
    Uses INFO loglevel and only the Streamhandler.
    Early messages (before proper logging setup) will therefore only be sent to additional
    logging handlers after the real initialization, because we don't know which
    ones the user desires beforehand.
    """
    logging.basicConfig(
        level=logging.INFO,
        format=LOGFORMAT,
        handlers=[logging.StreamHandler(sys.stderr)]
    )

def setup_logging(config: Dict[str, Any]) -> None:
    """
    Process -v/--verbose, --logfile options
    """
    
    # Log level
    verbosity = config['verbosity']
    logging.root.anddHandler()
