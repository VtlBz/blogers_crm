from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from .models import LogLevel

if TYPE_CHECKING:
    from loguru import Record


def info_and_warning(record: Record) -> bool:
    """Filter for sending ``INFO`` and ``WARNING`` log messages to a ``stdout``."""

    is_info = record["level"].name == LogLevel.INFO.name
    is_success = record["level"].name == LogLevel.SUCCESS.name
    is_warning = record["level"].name == LogLevel.WARNING.name
    return is_info or is_warning or is_success


def error_and_critical(record: Record) -> bool:
    """Filter for sending ``ERROR`` and ``CRITICAL`` log messages to a ``stderr``."""

    is_error = record["level"].name == LogLevel.ERROR.name
    is_critical = record["level"].name == LogLevel.CRITICAL.name
    return is_error or is_critical


def module_log_filter(module_name: str) -> Callable[[Record], bool]:
    """
    Filter for sending log messages to a logfile located in the ``module_name`` folder.

    Receives the module name as input and returns a filter
    that processes messages from the appropriating module.

    ### Parameters
    --------------
    module_name : |str|
        Module name for writing logs to his corresponding folder.
    """

    def _module_log_filter(record: Record) -> bool:
        return record["name"] == module_name

    return _module_log_filter
