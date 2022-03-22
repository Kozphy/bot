#!/usr/bin/env python3
"""
Main bot script.
Read the documentation to know what cli arguments you need.
"""

import logging
import sys
from typing import Any, List

from bot.cmd.arguments import Arguments
from bot.loggers import setup_logging_pre
from bot.exceptions import OperationalException, BotException

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
        print(args)
        if 'func' in args:
            return_code = args['func'](args)
        else:
            raise OperationalException('Usage of bot requires subcommand to be given in cli interface.')

    except SystemExit as e:
        return_code = e
    except KeyboardInterrupt:
        logger.info('SIGINT received, aborting ...')
    except BotException as e: 
        logger.error(str(e))
        return_code = 2
    except Exception:
        logger.exception('Fatal exception!')
    finally:
        sys.exit(return_code)

if __name__ == '__main__':
    main()