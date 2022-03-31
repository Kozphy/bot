from enum import Enum

class RunMode(Enum):
    """
    Bot running mode (backtesting, ...)
    can be "live", "dry-run"
    """
    LIVE = "live"
    DRY_RUN = "dry_run"
    Other = "Other"