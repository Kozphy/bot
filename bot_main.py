import logging
from typing import Dict, Any
from bot import __version__, constants


logger = logging.getLogger(__name__)

class main_bot():
    """Main class of the bot"""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        logger.info('Starting bot %s', __version__)
        