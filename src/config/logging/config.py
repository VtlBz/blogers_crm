from __future__ import annotations

import sys

from .models import LogLevel, LoguruConf

default_log_level: str = LogLevel.WARNING.name

default_rotation: str = "1 hour"

default_retention: str = "30 days"

default_log_msg_format: str = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS Z}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


loguru_conf = LoguruConf(
    sink=sys.stdout,
    level=default_log_level,
    format=default_log_msg_format,
    filter=None,
    colorize=None,
    serialize=False,
    backtrace=True,
    diagnose=False,
    enqueue=False,
    context=None,
    catch=True,
    rotation=default_rotation,
    retention=default_retention,
    compression=None,
    delay=True,
    watch=False,
    encoding="utf8",
)
