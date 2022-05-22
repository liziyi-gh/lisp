import logging

from tool.parser import tokenize, parse_tokens
from tool.lisp_eval import Lisp_eval
from tool import log
from tool.lisp_enviroment import get_top_env


Lisp_version = 0.03


def eval_source(source, env):
    tokens = tokenize(source)
    logging.debug(f"tokens is {tokens}")
    sentences = parse_tokens(tokens)[0]
    logging.debug(f"sentences is {sentences}")
    result = Lisp_eval(sentences, env)

    logging.debug(f"result is {result}")

    return result


if __name__ == '__main__':
    log.init_logging()
    logging.debug("Lisp interpreter Version {}".format(Lisp_version))
    env = get_top_env()

    while True:
        logging.debug("> ")
        source = input()
        result = eval_source(source, env)
        print(result)
        if result is not None:
            logging.debug(result)
