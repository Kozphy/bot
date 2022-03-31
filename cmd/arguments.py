"""
This module contains the argument manager class
"""

import argparse
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging
from bot.constants import DEFAULT_CONFIG
from bot.cmd.cli_option import AVAILABLE_CLI_OPTIONS

ARGS_COMMON = ['verbosity', 'logfile', 'version', 'config', 'user_data_dir']

ARGS_TRADE = ['strategy','strategy_path', 'db_path', 'dry_run', 'dry_run_wallet']

NO_CONFIG_REQUIRED = ['sync']

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

        # Workaround issue in argparse with action='append' and default value
        # (see https://bugs.python.org/issue16399)
        # Allow no-config for certain commands (like downloading)
        # if ('config' in parsed_arg and parsed_arg['config'] is None):
        #     no_conf_required = ('command' in parsed_arg and parsed_arg['command'] in NO_CONFIG_REQUIRED)

        #     ## if cli interface have specify user_dir
        #     if 'user_data_dir' in parsed_arg and parsed_arg.user_data_dir is not None:
        #         user_dir = parsed_arg.user_data_dir
        #     else: 
        #         # Default case
        #         user_dir = 'user_data'
        #         # Try loading from 'user_data/config.json'
        #         cfgfile = Path(user_dir) / DEFAULT_CONFIG
        #         if cfgfile.is_file():
        #             parsed_arg['config'] = [str(cfgfile)]
        #         else:
        #             # use 'config.yaml'
        #             cfgfile = Path.cwd() / DEFAULT_CONFIG
        #             if cfgfile.is_file() or not no_conf_required:
        #                 parsed_arg['config'] = [str(cfgfile)]
        # print(parsed_arg)
        return parsed_arg


    
    def _build_args(self, optionlist, parser):

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
        from bot.cmd.trade_command import start_trade
        trade_cmd = subparsers.add_parser('trade', help='activate trade mode',
                                            parents=[_common_parser])
        self._build_args(optionlist=ARGS_TRADE, parser=trade_cmd)
        trade_cmd.set_defaults(func=start_trade)
        # trade.add_argument('bar', help='trade mode')

        