import logging
from functools import wraps


def init_logging():
    logging.basicConfig(level=logging.DEBUG, filename="lisp.log")
    logging.debug("\n\nNew interpreter\n\n")


def log_entry_exit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        logging.info(
            f"[Log Helper] enter function {func_name}, args is {args}, kwargs is {kwargs}"
        )

        result = func(*args, **kwargs)

        logging.info(f"[Log Helper] exit function {func_name}")

        return result

    return wrapper
