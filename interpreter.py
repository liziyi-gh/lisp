import copy
from unittest import result
from tool.sentence import Sentence
from tool.parser import tokenize, parse_tokens

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

def op_if(exp:Sentence, env):
    if eval(exp.tokens[1], env) == True:
        return eval(exp.tokens[2], env)
    else:
        return eval(exp.tokens[3], env)

TOP_ENV = {
    '+': op_add,
    '-': op_sub,
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
    'if': op_if,
}

def define(exp:Sentence, env):
    name = exp.tokens[1]
    value = exp.tokens[2]
    if isinstance(value, Sentence):
        if value.tokens[0] == 'lambda':
            env[name] = value
        else:
            env[name] = eval(value, env)
        return
    if is_number(value):
        env[name] = to_number(value)
        return


def apply_lambda(exp:Sentence, env):
    lam_exp = env[exp.tokens[0]]
    formal_parameters = lam_exp.tokens[1].tokens
    lam_body = lam_exp.tokens[2]
    env = copy.deepcopy(env)
    for i in range(len(formal_parameters)):
        env[formal_parameters[i]] = eval(exp.tokens[i+1], env)
    return eval(lam_body, env)


def apply(exp:Sentence, env):
    func = env[exp.tokens[0]]
    len_args = len(exp.tokens) -1
    args = []
    for i in range(len_args):
        args.append(eval(exp.tokens[i+1], env))
    return func(args, env)


def eval(exp, env=TOP_ENV):
    tmp = None
    if isinstance(exp, Sentence):
        if len(exp.tokens) > 0:
            tmp = exp.tokens[0]
        else:
            return None
        if isinstance(tmp, Sentence):
            return eval(tmp, env)
    else:
        tmp = exp

    if env['number?'](tmp):
        return to_number(tmp)

    if tmp == 'define':
        define(exp, env)
        return

    if tmp == 'cond':
        i = 1
        while eval(exp.tokens[i], env) != True:
            i += 1
        return eval(exp.tokens[i+1], env)

    if tmp == 'let':
        # env = copy.deepcopy(env)
        # return
        pass

    if tmp == 'if':
        return op_if(exp, env)

    if tmp == 'begin':
        result = None
        for i in range(len(exp.tokens)-1):
            result = eval(exp.tokens[i+1])
        return result

    if env['symbol?'](tmp, env):
        # TODO: if tmp is a function then return itself
        if isinstance(env[tmp], Sentence) and env[tmp].tokens[0] == 'lambda':
            return apply_lambda(exp, env)

        if hasattr(env[tmp], '__call__'):
            return apply(exp, env)
        else:
            return env[tmp]


def eval_source(source, env=TOP_ENV):
    tokens = tokenize(source)
    sentences = parse_tokens(tokens)
    result = eval(sentences, env)
    return result

if __name__ == '__main__':
    print("Lisp interpreter Version 0.02")
    env = TOP_ENV
    while True:
        print("> ",end="")
        source = input()
        result = eval_source(source, env)
        if result is not None:
            print(result)
