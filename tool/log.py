import logging

def init_logging():
    logging.basicConfig(level=logging.DEBUG, filename="lisp.log")
    logging.debug("\n\nNew interpreter\n\n")
