import re
import math
import operator

"""
There a functional way to do this
"""

def car(x):
    return x[0]

def cdr(x):
    return x[1:]

standard_env = {
    '+': operator.add,
    '-': operator.sub,
    'equal?': operator.eq,
    'eq?': operator.is_,
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
    'cons': lambda x, y: [x, y],
    'number?': lambda x: isinstance(x, (int, float, complex)),
    'symbol?':lambda x: isinstance(x, str),
}

def apply():
    pass

def eval(exp, env=standard_env, stack_depth=0):
    if exp[0] == '(':
        tmp = exp[1]
        if env['number?'](tmp):
            # TODO float complex support
            return int(tmp)
        if env['symbol?'](tmp):
            # TODO handle error
            return env(tmp)

def parse(exp:str):
    # TODO see python3 cook book tokens
    # TODO more pythonic
    # TODO exp should be one line format
    tokens = []
    tmp = ""
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == ')':
            tokens.append(exp[i])
        if exp[i] == ' ':
            tokens.append(tmp)
            tmp = ""
        else:
            tmp += exp[i]
    return tokens


source = "(+ 1 2 (- 2 3) (- 3 3))"
print(parse(source))
