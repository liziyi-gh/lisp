import operator

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
        raise InternalException
    try:
        return float(x)
    except (ValueError, TypeError):
        raise InternalException
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


STD_ENV = {
    '+': operator.add,
    '-': operator.sub,
    # 'equal?': operator.eq,
    # 'eq?': operator.is_,
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
    'cons': lambda x, y: [x, y],
    'number?': is_number,
    'symbol?':lambda x: isinstance(x, str),
}
