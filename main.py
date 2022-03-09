#!/usr/bin/env python3
"""
Main Freqtrade bot script.
Read the documentation to know what cli arguments you need.
"""

import logging
import sys
from typing import Any, List

from bot.cmd import Arguments
from bot.loggers import setup_logging_pre

# check min. python version
if sys.version_info < (3, 8, 10):
    sys.exit('short bot requires Python version >= 3.8.10')


logger = logging.getLogger('short_bot')        

def main(sysargv: List[str] = None) -> None:
    """
    This function will initiate the bot and start the trading loop
    :return None
    """

    return_code: Any = 1

    try:
        setup_logging_pre()
        arguments = Arguments(sysargv)
        args = arguments.get_parsed_arg()
        
    except:
        exit()

if __name__ == '__main__':
    main()