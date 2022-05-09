"""
Definition of cli position arguments
"""
from bot.cmd.cli_option import Arg
# TODO: refactor position arguemnts

AVAILABLE_CLI_POSITIONS = {
    'trade': Arg(
        help='activate trade mode',
    ),
    'sync': Arg(
        help='download data and let it store in sql',
    ),
    'backtesting': Arg(
        help='backtesting strategy with historical data'
    )

}
