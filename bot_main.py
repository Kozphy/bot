import logging
from typing import Dict, Any
from bot import __version__, constants


logger = logging.getLogger(__name__)

class main_bot():
    """Main class of the bot"""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Init all variables and objects the bot needs to work
        :param config: configuration dict, you can use Configuration.get_config()
        to get the config dict.
        """
        logger.info('Starting bot %s', __version__)
        