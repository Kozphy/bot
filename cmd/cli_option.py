"""
Definition of cli arguments used in arguments.py
"""

from bot import __version__
from pathlib import Path
import logging

class Arg:
    # Optional cli arguments
    def __init__(self, *args, **kwargs):
        self.cli = args
        self.kwargs = kwargs

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
        default=f'{Path.cwd()}/user_data/config/config.yaml'
    ),
    'user_data_dir': Arg(
        '--userdir', '--user-data-dir',
        help='Path point to userdata directory.',
        metavar='PATH',
        nargs='?',
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
        default=f'{Path.cwd()}/user_data/strategy',
    ),
    'db_path': Arg(
        '-dbp', '--db-path',
        help='Where did you want to set the database?',
        metavar='PATH',
        nargs='?',
        default=f'{Path.cwd()}/db/test.db',
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
        nargs=1
    ),
   # no-config required 
   'sync': Arg(
       '-sc', '--sync',
       help='download data and let it store in sql',
       action='store_true',
   )
}