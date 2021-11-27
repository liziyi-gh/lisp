import operator
from tool.block import Block
from tool.parser import parse, parse_tokens

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


standard_env = {
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

def apply(exp, env):
    print(exp.child)
    func = env[exp.child[0]]
    if func is standard_env['+']:
        return func(eval(exp.child[1]), eval(exp.child[2]))


def eval(exp, env=standard_env):
    print('eval', exp)
    tmp = ''
    if isinstance(exp, Block):
        tmp = exp.child[0]
        if isinstance(tmp, Block):
            return eval(tmp, env)
    else:
        tmp = exp[0]
    if env['number?'](tmp):
        return to_number(tmp)
    if env['symbol?'](tmp):
        if hasattr(env[tmp], '__call__'):
            return apply(exp, env)
        else:
            return env(tmp)


source = "(+ 1 (+ 2 (+ 3 4)))"
tokens = parse(source)
root = parse_tokens(tokens)
result = eval(root)
print(result)
