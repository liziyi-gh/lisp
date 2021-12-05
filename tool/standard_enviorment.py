from tool.sentence import Sentence

def cdr(x:list, y):
    if len(x[0].tokens) == 2:
        return x[0].tokens[1]
    else:
        return x[0].tokens[1:]

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

def op_add(args:list, env):
    ans = 0
    for ele in args:
        ans += ele

    return ans

def op_sub(args:list, env):
    ans = args[0] - args[1]

    return ans

def op_mul(args:list, env):
    ans = 1
    for ele in args:
        ans *= ele

    return ans

TOP_ENV = {
    '+': op_add,
    '-': lambda x, y: x[0] - x[1],
    '*': op_mul,
    '/': lambda x, y: x[0] / x[1],
    'equal?': lambda x, y: x[0] == x[1],
    'eq?': lambda x, y: x[0] is x[1],
    '=': lambda x, y: x[0] == x[1],
    'car': lambda x, y: x[0].tokens[0],
    'cdr': cdr,
    'cons': lambda x, y: Sentence([x[0], x[1]]),
    'number?': is_number,
    'symbol?':lambda x, y: x in y.keys(),
}
