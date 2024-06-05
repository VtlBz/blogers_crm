from pathlib import Path
from typing import Union

from .config import loguru_conf
from .core import make_logger
from .models import LogConf, LogLevel
from .pathmakers import make_base_log_directory


def get_log_configuration(path: Union[Path, str]) -> LogConf:
    return LogConf(
        loguru_settings=loguru_conf,
        log_directory=make_base_log_directory(path),
        _logger_builder=make_logger,
    )


__all__ = ["LogLevel", "get_log_configuration"]
