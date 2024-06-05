from __future__ import annotations

from dataclasses import dataclass, field
from datetime import time, timedelta
from enum import Enum
from logging import Handler
from multiprocessing.context import BaseContext
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Optional, TextIO, Union

if TYPE_CHECKING:
    from loguru import (
        CompressionFunction,
        FilterDict,
        FilterFunction,
        FormatFunction,
        Logger,
        Message,
        RetentionFunction,
        RotationFunction,
        Writable,
    )


class LogLevel(Enum):
    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


@dataclass
class LoguruConf:
    sink: Union[
        TextIO,
        Writable,
        Callable[[Message], None],
        Handler,
        str,
        PathLike[str],
    ]
    level: Union[str, int]
    format: Union[str, FormatFunction]
    filter: Optional[Union[str, FilterFunction, FilterDict]]
    colorize: Optional[bool]
    serialize: bool
    backtrace: bool
    diagnose: bool
    enqueue: bool
    context: Optional[Union[str, BaseContext]]
    catch: bool
    rotation: Optional[Union[str, int, time, timedelta, RotationFunction]]
    retention: Optional[Union[str, int, timedelta, RetentionFunction]]
    compression: Optional[Union[str, CompressionFunction]]
    delay: bool
    watch: bool
    encoding: Optional[str]


@dataclass
class LogConf:
    loguru_settings: LoguruConf

    log_directory: Path
    _logger_builder: Callable[[LogConf, str], Logger] = field(repr=False, compare=False)

    def get_logger(self, module_name: str) -> Logger:
        return self._logger_builder(self, module_name)
