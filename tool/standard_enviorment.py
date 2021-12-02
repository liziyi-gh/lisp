import operator

from tool.sentence import Sentence

def car(x):
    return x[0]

def cdr(x):
    return x[1:]

class InternalException(Exception):
    pass


def to_number(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        try:
            return float(x)
        except (ValueError, TypeError):
            try:
                return complex(x)
            except (ValueError, TypeError):
                raise InternalException

def is_number(x):
    try:
        _ = to_number(x)
        return True
    except InternalException:
        return False

def define(exp:Sentence, env):
    name = exp.child[1]
    env[name] = exp.child[2]

TOP_ENV = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    # 'equal?': operator.eq,
    # 'eq?': operator.is_,
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
    'cons': lambda x, y: [x, y],
    'number?': is_number,
    'symbol?':lambda x, y: x in y.keys(),
}
