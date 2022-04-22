"""
Definition of cli arguments used in arguments.py
"""

from bot import __version__
from pathlib import Path
import logging
from bot.constants import (BOT_DIR, CONFIG, LOG_FILE, DEFAULT_USERDATA_DIR,
DEFAULT_DB_DIR, DEFAULT_DB_PORT,DEFAULT_DB_NAME, DEFAULT_DB_USER, DEFAULT_DB_HOST)
from datetime import datetime
import argparse

class Arg:
    # Optional cli arguments
    def __init__(self, *args, **kwargs):
        self.cli = args
        self.kwargs = kwargs

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%M-%D")
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)

## option arguments
ARGS_COMMON = ['verbosity', 'logfile', 'version', 'config', 'user_data_dir']

ARGS_TRADE = ['strategy','strategy_path', 'db_path', 'db_name', 'db_user', 'db_host', 'db_port', 'dry_run',
 'dry_run_wallet']

SYNC_ARGS = ['startAt', 'endAt', 'db_path', 'db_name', 'db_host', 'db_user', 'db_port']

ARGS_COMMON_OPTIMIZE = ['timeframe', 'timerange', 'fee']

## List of avalilable cli options
AVAILABLE_CLI_OPTIONS = {
    # Common options
    'verbosity': Arg(
        '-v', '--verbose', 
        help='Verbose mode (-vv for more, -vvv to get all messages).',
        action='count',
        default=0,
    ),
    'logfile': Arg(
        '--logfile',
        help='Log to the file specified.',
        metavar='FILE',
        nargs='?',
        default=LOG_FILE,
    ),
    'version': Arg(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {__version__}',
    ),
    'config': Arg(
        '-c', '--config',
        help=f'Specify configuration file',
        metavar='PATH',
        nargs='?',
        default=CONFIG
    ),
    'user_data_dir': Arg(
        '-udd', '--user-data-dir',
        help='Path point to userdata directory.',
        metavar='PATH',
        nargs='?',
        default=DEFAULT_USERDATA_DIR,
    ),
    'db_host': Arg(
        '-dbh', '--db-host',
        help='Database host',
        default=DEFAULT_DB_HOST,
    ),
    'db_user': Arg(
        '-dbu', '--db-user',
        help='who want to connect database?',
        metavar='USER',
        nargs='?',
        default=DEFAULT_DB_USER,
    ),
    'db_path': Arg(
        '-dbp', '--db-path',
        help='Where did you want to set the database?',
        metavar='PATH',
        nargs='?',
        default=DEFAULT_DB_DIR,
    ),
    'db_name': Arg(
        '-dbn', '--db-name',
        help='what db name do you want?',
        metavar='NAME',
        nargs='?',
        default=DEFAULT_DB_NAME,
    ),
    'db_port': Arg(
        '-p', '--port',
        help='The port to connect to',
        metavar='PORT',
        nargs='?',
        default=DEFAULT_DB_PORT,
    ),
    # Trade options
    'strategy': Arg(
        '-s', '--strategy',
        help='What strategy do you want to run?',
        metavar='PATH',
        nargs=1
    ),
    'strategy_path': Arg(
        '-sp', '--strategy-path',
        help='Where did you put the strategy?',
        metavar='PATH',
        nargs='?',
        default=f'{BOT_DIR}/user_data/strategy',
    ),
    'dry_run': Arg(
        '-drun', '--dry-run',
        help='active virtual trade mode',
        action='store_true',
    ),
    'dry_run_wallet': Arg(
        '-drw', '--dry-run-wallet',
        help='How much dry run wallet do you want to initialize?',
        metavar='number',
        default='1000',
        nargs=1,
    ),
   # no-config required  (sync, backtest)
   'startAt': Arg(
       '-sAt', '--start-at',
       help='when do you want to start',
       metavar='YYYY-MM-DD',
       nargs='?',
       type=valid_date
    ),
   'endAt': Arg(
       '-eAt', '--end-at',
       help='when do you want to stop',
       metavar='YYYY-MM-DD',
       nargs='?',
       type=valid_date
   )
}


