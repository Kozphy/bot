"""
Definition of cli arguments used in arguments.py
"""

from pathlib import Path
from constants import (BOT_DIR, CONFIG, LOG_FILE, DEFAULT_USERDATA_DIR, BOT_NAME,
DEFAULT_DB_DIR, DEFAULT_DB_PORT,DEFAULT_DB_NAME, DEFAULT_DB_USER, DEFAULT_DB_HOST, __version__)
from datetime import datetime
import argparse
import click

class Arg:
    # Optional cli arguments
    def __init__(self, *args, **kwargs):
        self.cli = args
        self.kwargs = kwargs

# Deprecated
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
        help='Verbose mode (-vv for debug message, -vvv to get all messages).',
        count=True,
        default=0,
        show_default=True,
    ),
    'logfile': Arg(
        '--logfile',
        help='Log to the file specified.',
        metavar='FILE',
        default=LOG_FILE,
        show_default=True,
    ),
    'version': Arg(
        '-v', '--version',
        prog_name=BOT_NAME,
        message=f'%(prog)s {__version__}',
    ),
    'config': Arg(
        '-c', '--config',
        help=f'Specify configuration file',
        metavar='PATH',
        default=CONFIG,
        show_default=True,
    ),
    'user_data_dir': Arg(
        '-udd', '--user-data-dir',
        help='Path point to userdata directory.',
        metavar='PATH',
        default=DEFAULT_USERDATA_DIR,
        show_default=True,
    ),
    'db_name': Arg(
        '-dbn', '--db-name',
        help='what db name do you want?',
        metavar='NAME',
        default=DEFAULT_DB_NAME,
        show_default=True,
    ),
    'db_path': Arg(
        '-dbph', '--db-path',
        help='Where did you want to set the database?',
        metavar='PATH',
        default=DEFAULT_DB_DIR,
        show_default=True,
    ),
    'db_host': Arg(
        '-dbh', '--db-host',
        help='Database host',
        default=DEFAULT_DB_HOST,
        show_default=True,
    ),
    'db_user': Arg(
        '-dbu', '--db-user',
        help='who want to connect database?',
        metavar='USER',
        default=DEFAULT_DB_USER,
        show_default=True,
    ),
    'db_port': Arg(
        '-dbpt', '--db-port',
        help='The port to connect to',
        metavar='PORT',
        default=DEFAULT_DB_PORT,
        show_default=True,
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
       type=click.DateTime(formats=['%Y-%m-%d']),
    ),
   'endAt': Arg(
       '-eAt', '--end-at',
       help='when do you want to stop',
       metavar='YYYY-MM-DD',
       type=click.DateTime(formats=['%Y-%m-%d'])
   )
}


