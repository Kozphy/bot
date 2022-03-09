"""
This module contains the argument manager class
"""

import argparse
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging

from bot.cmd.cli_option import AVAILABLE_CLI_OPTIONS

ARGS_COMMON = ['verbosity', 'logfile', ' version', 'config', 'datadir','user_data_dir']

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
        :return: List[str] List of arguments
        """
        if self._parsed_arg is None:
            self._build_subcommands()
            self._parsed_arg = self._parse_args()
        
        return vars(self._parsed_arg)
    
    def _parse_args(self) -> argparse.Namespace:
        """
        Parses given arguments and returns an argparse Namespace instance.
        """
        logging.info('parse args')

        self.parser = argparse.ArgumentParser(description='trading bot')
        parsed_arg = self.parser.parse_args(self.args)
        pass
    
    def _build_args(self, optionlist, parser):
        logging.info('buid args')

        for val in optionlist: 
            opt = AVAILABLE_CLI_OPTIONS[val]
            parser.add_argument(*opt.cli, dest=val, **opt.kwargs)


    def _build_subcommands(self) -> None:
        """
        Builds and attaches all subcommands.
        :return None
        """
        logging.info('build_subcommands')

        # Build shared arguments (as group Common Options)
        _common_parser = argparse.ArgumentParser(add_help=False)
        group = _common_parser.add_argument_group("Common arguments")
        self._build_args(optionlist=ARGS_COMMON, parser=group)

