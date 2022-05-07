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
from bot.configuration import Configuration
import sys


# from bot.configuration.load_config import load_yaml_setting

# check min. python version
if sys.version_info < (3, 9, 12):
    sys.exit('short bot requires Python version >= 3.9.12')


logger = logging.getLogger('short_bot')        

args = None

def main(sysargv: List[str] = None) -> None:
    """
    This function will initiate the bot and start the trading loop
    :return None
    """
    return_code: Any = 1
    # print(sys.path)
        

    try:
        setup_logging_pre()
        arguments = Arguments(sysargv)
        # TODO: unknown global args whether using in future, so temporarily place here
        global args
        args = arguments.get_parsed_arg()
        c = Configuration(args=args)
        configured, yaml = c.get_config()
        print(yaml)

        if 'func' in args:
            return_code = args['func'](configured, yaml)
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