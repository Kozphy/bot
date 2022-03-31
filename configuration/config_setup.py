import logging
from typing import Any, Dict

from bot.enums import RunMode
from .configuration import Configuration

logger = logging.getLogger(__name__)

def setup_utils_configuration(args: Dict[str, Any], runmode: RunMode) -> Dict[str, Any]:
    """
    Prepare the configuration for utils subcommands
    :param args: Cli args from Arguments.py
    :param method: Bot running mode
    :return: Configuration
    """
    configuration = Configuration(args, runmode)
    config = configuration.get_config()