import asyncio
import json
import logging
import sys
import time
from contextlib import contextmanager
from functools import wraps
from typing import Dict

from structlog import configure, get_logger
from structlog.processors import TimeStamper, format_exc_info

from helpers.types.json_types import JSON

EVENT_DICT_TYPE = Dict[str, JSON]

out_handler = logging.StreamHandler(sys.stdout)
out_handler.setLevel("DEBUG")

logging.basicConfig(
    format="%(name)s | [%(levelname)s]: %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("websockets").setLevel(logging.WARNING)
logging.getLogger("google").setLevel(logging.WARNING)
logging.getLogger("googleapiclient").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)


def event_to_message(
    logger: logging.Logger, method_name: str, event_dict: EVENT_DICT_TYPE,
) -> EVENT_DICT_TYPE:
    """Move `event` to `message` field."""
    if "event" in event_dict and "message" not in event_dict:
        event_dict["message"] = event_dict.pop("event")
    return event_dict


def format_args(
    logger: logging.Logger, method_name: str, event_dict: EVENT_DICT_TYPE,
) -> EVENT_DICT_TYPE:
    """Support inline kwargs format for `message` field using event dict."""
    message = event_dict.get("message", None)
    if message:
        event_dict["message"] = message.format(**event_dict)
    return event_dict


severities = {
    # method_name: severity_str
    "debug": logging.getLevelName(logging.DEBUG),
    "info": logging.getLevelName(logging.INFO),
    "warning": logging.getLevelName(logging.WARNING),
    "error": logging.getLevelName(logging.ERROR),
    "exception": logging.getLevelName(logging.ERROR),
    "critical": logging.getLevelName(logging.CRITICAL),
}


def add_severity(
    logger: logging.Logger, method_name: str, event_dict: EVENT_DICT_TYPE,
) -> EVENT_DICT_TYPE:
    """Add severity to log record."""
    event_dict["severity"] = severities[method_name]
    return event_dict


def json_dumps(
    logger: logging.Logger, method_name: str, event_dict: EVENT_DICT_TYPE,
) -> str:
    """Dumps record to json."""
    return json.dumps(event_dict, default=str)


configure(
    processors=[
        format_exc_info,
        event_to_message,
        format_args,
        add_severity,
        TimeStamper("iso"),
        json_dumps,
    ],
    cache_logger_on_first_use=True,
)
logger = get_logger()


def log_time():
    """Logs function execution time."""

    def deco(fn):
        fn_name = f"{fn.__module__}.{fn.__name__}"  # noqa: WPS609 Found direct magic attribute usage
        local_logger = get_logger(function=fn_name)

        @wraps(fn)
        def async_wrapper(*args, **kwargs):
            with _timer(args, kwargs, local_logger):
                return fn(*args, **kwargs)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            with _timer(args, kwargs, local_logger):
                return fn(*args, **kwargs)

        if asyncio.iscoroutinefunction(fn):
            return async_wrapper

        return wrapper

    return deco


@contextmanager
def _timer(fn_args, fn_kwargs, local_logger):
    record = {"args": fn_args, "kwargs": fn_kwargs}
    started_at = time.monotonic()
    try:
        yield
    except Exception as exc:
        record["exc_info"] = exc
        raise
    finally:
        spent = time.monotonic() - started_at
        record["elapsed_in"] = spent
        local_logger.debug(
            "Function {function} elapsed in {elapsed_in} seconds", **record
        )


access_logger = get_logger(name="access_log")


class RequestLogger:
    """Logger for aiohttp requests."""

    def log(self, request, response, time):
        """Emit log to logger."""
        if request.path == "/healthcheck":
            return

        access_logger.info(
            "{http_method} {path_qs} {status} in {timeit} sec",
            http_method=request.method,
            path=request.path,
            path_qs=request.path_qs,
            query=dict(request.query),
            timeit=time,
            status=response.status,
        )
