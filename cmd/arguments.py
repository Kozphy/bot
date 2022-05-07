"""
This module contains the argument manager class
"""
import click
import argparse
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging
# from bot.constants import CONFIG
from bot.cmd.cli_option import (AVAILABLE_CLI_OPTIONS, ARGS_COMMON, ARGS_TRADE,
 SYNC_ARGS, ARGS_COMMON_OPTIMIZE)


# NO_CONFIG_REQUIRED = ['sync']

## position argument
POSITION_ARGS = ['trade', 'backtesting', 'sync']

logger = logging.getLogger(__name__)

class Arguments:
    """
    Arguments Class. Manage the arguments received by the cli
    """
    
    def __init__(self, args: Optional[List[str]]) -> None:
        self.args = args
        self._parsed_arg: Optional[argparse.Namespace] = None
    
    def get_parsed_arg(self) -> Dict[str, Any]:
        """
        Return the list of arguments
        :return: List[str]  List of arguments
        """
        if self._parsed_arg is None:
            self.parser = argparse.ArgumentParser(description='trading bot', prog='short_bot')
            self._build_subcommands()
            self._parsed_arg = self._parse_args()
        
        return vars(self._parsed_arg)
    

    def _parse_args(self) -> argparse.Namespace:
        """
        Parses cli interface given arguments and returns an argparse Namespace instance.
        """
        logging.debug('load cli interface arguments to namespace object')

        parsed_arg = self.parser.parse_args(self.args)

        return parsed_arg

    
    def _build_args(self, optionlist, parser, positionlist = None):

        if positionlist is None: 
            for val in optionlist: 
                if hasattr(parser, 'title'):
                    logging.debug(f'create {val} arguments string to {parser.title} parser')
                elif hasattr(parser, 'prog'):
                    logging.debug(f'create {val} arguments string to {parser.prog} parser')
                opt = AVAILABLE_CLI_OPTIONS[val]
                parser.add_argument(*opt.cli, dest=val, **opt.kwargs)


    def _build_subcommands(self) -> None:
        """
        Builds and attaches all subcommands.
        :return None
        """
        logging.debug('build_subcommands')

        # Build option arguments (as group Common Options)
        _common_parser = argparse.ArgumentParser(add_help=False)
        group = _common_parser.add_argument_group("Common arguments")
        self._build_args(optionlist=ARGS_COMMON, parser=group)
        # _common_parser.print_help()

        # Build command into self.parser
        self._build_args(optionlist=['version'], parser=self.parser)

        ## build subcommand
        subparsers = self.parser.add_subparsers(dest='command')

        from bot.cmd import (start_trade, start_sync)

        # build trade command and options
        trade_cmd = subparsers.add_parser('trade', help='activate trade mode',
                                            parents=[_common_parser])
        self._build_args(optionlist=ARGS_TRADE, parser=trade_cmd)
        trade_cmd.set_defaults(func=start_trade)
        # trade.add_argument('bar', help='trade mode')

        # build sync command and options
        sync_cmd = subparsers.add_parser('sync', help='download data and let it store in sql',
                                        parents=[_common_parser])
        self._build_args(optionlist=SYNC_ARGS, parser=sync_cmd)
        sync_cmd.set_defaults(func=start_sync)