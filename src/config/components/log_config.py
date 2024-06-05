import os
from pathlib import Path

from config.logging import get_log_configuration
from config.logging.models import LogConf, LogLevel

LOG_BASE_DIR: Path = Path(os.path.expanduser("~")) / os.getenv(
    "COMPOSE_PROJECT_NAME", "UntitledProject"
)

DEBUG_STATE = globals().get("DEBUG_STATE", False)

log_conf: LogConf = get_log_configuration(LOG_BASE_DIR)
log_conf.loguru_settings.diagnose = DEBUG_STATE

default_log_level: str = LogLevel.DEBUG.name if DEBUG_STATE else LogLevel.WARNING.name


def get_logger(module_name: str, log_level: str = default_log_level):
    log_conf.loguru_settings.level = log_level
    return log_conf.get_logger(module_name)
