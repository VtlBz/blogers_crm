from __future__ import annotations

import sys
from dataclasses import asdict
from typing import TYPE_CHECKING, Set

from loguru import logger

from .filters import error_and_critical, info_and_warning, module_log_filter
from .models import LogConf
from .pathmakers import make_log_path

if TYPE_CHECKING:
    from loguru import Logger


logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": "ERROR", "filter": error_and_critical},
        {"sink": sys.stdout, "level": "INFO", "filter": info_and_warning},
    ],
)

registred_loggers: Set[str] = set()


def make_logger(log_conf: LogConf, module_name: str) -> Logger:
    if module_name not in registred_loggers:
        log_conf.loguru_settings.sink = make_log_path(
            log_conf.log_directory, module_name
        )
        log_conf.loguru_settings.filter = module_log_filter(module_name)
        logger.add(**asdict(log_conf.loguru_settings))
        registred_loggers.add(module_name)

    return logger
