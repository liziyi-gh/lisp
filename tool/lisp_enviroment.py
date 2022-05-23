from functools import reduce
import logging
from typing import Dict

from tool.lisp_list import LispList


class LispEnviorment():

    def __init__(self, env: Dict, farther_env=None):
        self.env = env
        self.farther_env = farther_env


def Lisp_is_symbol(exp, env: LispEnviorment):
    logging.debug(f"is symbol {exp}?")
    logging.debug(f"keys is {env.env.keys()}")

    if exp in env.env.keys():
        logging.debug(f"{exp} is symbol")
        return True
    else:
        if env.farther_env is None:
            return False
        else:
            return Lisp_is_symbol(exp, env.farther_env)


def Lisp_look_up(exp, env: LispEnviorment):
    if exp in env.env.keys():
        return env.env[exp]
    else:
        if env.farther_env is None:
            return False
        else:
            return Lisp_look_up(exp, env.farther_env)


def Lisp_add(*args):
    logging.debug(f"args type is {type(args)}")
    logging.debug(f"args is {args}")
    lisp_list = args[0]
    ans = sum(lisp_list.tokens)
    logging.debug(f"sum is {ans}")

    return ans


def Lisp_minus(*args):
    logging.debug(f"args type is {type(args)}")
    logging.debug(f"args is {args}")
    lisp_list = args[0]
    ans = lisp_list[0] - lisp_list[1]
    logging.debug(f"minus result is {ans}")

    return ans


def Lisp_multpy(*args):
    logging.debug(f"args type is {type(args)}")
    logging.debug(f"args is {args}")
    lisp_list = args[0]
    ans = reduce(lambda x, y: x * y, lisp_list.tokens)
    logging.debug(f"multpy result is {ans}")

    return ans


def Lisp_div(*args):
    logging.debug(f"args type is {type(args)}")
    logging.debug(f"args is {args}")
    lisp_list = args[0]
    ans = lisp_list[0] / lisp_list[1]
    logging.debug(f"div result is {ans}")

    return ans


def Lisp_equal(*args):
    lisp_list = args[0]
    ans = lisp_list[0] == lisp_list[1]

    return ans


def Lisp_car(*args):
    lisp_list = args[0][0]
    logging.debug(f"lisp_list.tokens is {lisp_list.tokens}")

    return Lisp_eval(lisp_list[0])


def Lisp_cdr(*args):
    lisp_list = args[0]

    return LispList(lisp_list(lisp_list[1:]))


__primitive_env = {
    '+': Lisp_add,
    '-': Lisp_minus,
    '*': Lisp_multpy,
    '/': Lisp_div,
    '=': Lisp_equal,
    'car': Lisp_car,
    'cdr': Lisp_cdr,
}


def is_primitive(func):
    return func in __primitive_env.values()


__top_env = {**__primitive_env}

TOP_ENV = LispEnviorment(__top_env)


def get_top_env() -> LispEnviorment:
    return TOP_ENV
