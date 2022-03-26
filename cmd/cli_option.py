"""
Definition of cli arguments used in arguments.py
"""

from bot import __version__

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
        metavar='FILE'
    ),
    'version': Arg(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    ),
    'config': Arg(
        '-c', '--config',
        help=f'Specify configuration file',
        action='append',
        metavar='PATH'
    ),
    'datadir': Arg(
        '-d', '--datadir',
        help='Path point to historical backtesting data.',
        metavar='PATH'
    ),
    'user_data_dir': Arg(
        '--userdir', '--user-data-dir',
        help='Path point to userdata directory.',
        metavar='PATH'
    ),
    # Trade options
    'strategy': Arg(
        '-s', '--strategy',
        help='what strategy do you want to run?',
        metavar='PATH'
    )
    

}