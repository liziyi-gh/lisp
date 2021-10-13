import math
import operator

"""
There a functional way to do this
"""

standard_env = {
    '+': operator.add,
    '-': operator.sub,
    'equal?': operator.eq,
    'eq?': operator.is_,
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
    'cons': lambda x, y: [x, y],
}

def apply():
    pass

def eval(exp, env=standard_env):
    pass

def parse(exp):
    pass

a = [1, 2, 3]
