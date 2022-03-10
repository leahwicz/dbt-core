# Stubs for logbook.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from logbook._fallback import StackedObject
from typing import Any, Optional

def set_datetime_format(datetime_format: Any) -> None: ...

CRITICAL: int
ERROR: int
WARNING: int
NOTICE: int
INFO: int
DEBUG: int
TRACE: int
NOTSET: int

def level_name_property(): ...
def lookup_level(level: Any): ...
def get_level_name(level: Any): ...

class _ExceptionCatcher:
    logger: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def __init__(self, logger: Any, args: Any, kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any): ...

class ContextObject(StackedObject):
    stack_manager: Any = ...
    def push_greenlet(self) -> None: ...
    def pop_greenlet(self) -> None: ...
    def push_context(self) -> None: ...
    def pop_context(self) -> None: ...
    def push_thread(self) -> None: ...
    def pop_thread(self) -> None: ...
    def push_application(self) -> None: ...
    def pop_application(self) -> None: ...

class NestedSetup(StackedObject):
    objects: Any = ...
    def __init__(self, objects: Optional[Any] = ...) -> None: ...
    def push_application(self) -> None: ...
    def pop_application(self) -> None: ...
    def push_thread(self) -> None: ...
    def pop_thread(self) -> None: ...
    def push_greenlet(self) -> None: ...
    def pop_greenlet(self) -> None: ...
    def push_context(self) -> None: ...
    def pop_context(self) -> None: ...

class Processor(ContextObject):
    stack_manager: Any = ...
    callback: Any = ...
    def __init__(self, callback: Optional[Any] = ...) -> None: ...
    def process(self, record: Any) -> None: ...

class _InheritedType:
    def __reduce__(self): ...

Inherit: Any

class Flags(ContextObject):
    stack_manager: Any = ...
    def __init__(self, **flags: Any) -> None: ...
    @staticmethod
    def get_flag(flag: Any, default: Optional[Any] = ...): ...

class LogRecord:
    keep_open: bool = ...
    time: Any = ...
    heavy_initialized: bool = ...
    late: bool = ...
    information_pulled: bool = ...
    channel: Any = ...
    msg: Any = ...
    args: Any = ...
    kwargs: Any = ...
    level: Any = ...
    exc_info: Any = ...
    extra: Any = ...
    frame: Any = ...
    frame_correction: Any = ...
    process: int = ...
    def __init__(
        self,
        channel: Any,
        level: Any,
        msg: Any,
        args: Optional[Any] = ...,
        kwargs: Optional[Any] = ...,
        exc_info: Optional[Any] = ...,
        extra: Optional[Any] = ...,
        frame: Optional[Any] = ...,
        dispatcher: Optional[Any] = ...,
        frame_correction: int = ...,
    ) -> None: ...
    def heavy_init(self) -> None: ...
    def pull_information(self) -> None: ...
    def close(self) -> None: ...
    def __reduce_ex__(self, protocol: Any): ...
    def to_dict(self, json_safe: bool = ...): ...
    @classmethod
    def from_dict(cls, d: Any): ...
    def update_from_dict(self, d: Any): ...
    def message(self): ...
    level_name: Any = ...
    def calling_frame(self): ...
    def func_name(self): ...
    def module(self): ...
    def filename(self): ...
    def lineno(self): ...
    def greenlet(self): ...
    def thread(self): ...
    @property
    def thread_name(self) -> str: ...
    def process_name(self): ...
    @property
    def formatted_exception(self) -> Optional[str]: ...
    def exception_name(self): ...
    @property
    def exception_shortname(self): ...
    def exception_message(self): ...
    @property
    def dispatcher(self): ...

class LoggerMixin:
    level_name: Any = ...
    def trace(self, *args: Any, **kwargs: Any) -> None: ...
    def debug(self, *args: Any, **kwargs: Any) -> None: ...
    def info(self, *args: Any, **kwargs: Any) -> None: ...
    def warn(self, *args: Any, **kwargs: Any) -> None: ...
    def warning(self, *args: Any, **kwargs: Any): ...
    def notice(self, *args: Any, **kwargs: Any) -> None: ...
    def error(self, *args: Any, **kwargs: Any) -> None: ...
    def exception(self, *args: Any, **kwargs: Any): ...
    def critical(self, *args: Any, **kwargs: Any) -> None: ...
    def log(self, level: Any, *args: Any, **kwargs: Any) -> None: ...
    def catch_exceptions(self, *args: Any, **kwargs: Any): ...
    disabled: bool = ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...

class RecordDispatcher:
    suppress_dispatcher: bool = ...
    name: Any = ...
    handlers: Any = ...
    group: Any = ...
    level: Any = ...
    def __init__(self, name: Optional[Any] = ..., level: Any = ...) -> None: ...
    disabled: Any = ...
    def handle(self, record: Any) -> None: ...
    def make_record_and_handle(
        self,
        level: Any,
        msg: Any,
        args: Any,
        kwargs: Any,
        exc_info: Any,
        extra: Any,
        frame_correction: Any,
    ) -> None: ...
    def call_handlers(self, record: Any) -> None: ...
    def process_record(self, record: Any) -> None: ...

class Logger(RecordDispatcher, LoggerMixin): ...

class LoggerGroup:
    loggers: Any = ...
    level: Any = ...
    disabled: bool = ...
    processor: Any = ...
    def __init__(
        self, loggers: Optional[Any] = ..., level: Any = ..., processor: Optional[Any] = ...
    ) -> None: ...
    def add_logger(self, logger: Any) -> None: ...
    def remove_logger(self, logger: Any) -> None: ...
    def process_record(self, record: Any) -> None: ...
    def enable(self, force: bool = ...) -> None: ...
    def disable(self, force: bool = ...) -> None: ...

def dispatch_record(record: Any) -> None: ...
