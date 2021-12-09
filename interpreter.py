import copy
from typing import Dict, Union
from unittest import result
from tool.sentence import Sentence
from tool.parser import tokenize, parse_tokens

def cdr(x:list, y):
    if len(x[0]) == 2:
        return x[0][1]
    else:
        return x[0][1:]

class InternalException(Exception):
    pass


def to_number(x) -> Union[int, float, complex]:
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

def is_number(x) -> bool:
    try:
        _ = to_number(x)
        return True
    except InternalException:
        return False

def op_add(args:list, env) -> Union[int, float, complex]:
    ans = 0
    for ele in args:
        ans += ele

    return ans

def op_sub(args:list, env) -> Union[int, float, complex]:
    ans = args[0] - args[1]

    return ans

def op_mul(args:list, env):
    ans = 1
    for ele in args:
        ans *= ele

    return ans

def op_if(exp:Sentence, env):
    if eval(exp[1], env) == True:
        return eval(exp[2], env)
    else:
        return eval(exp[3], env)

def op_list(args:list, env):
    return Sentence(args)

TOP_ENV = {
    '+': op_add,
    '-': op_sub,
    '*': op_mul,
    '/': lambda x, y: x[0] / x[1],
    'equal?': lambda x, y: x[0] == x[1],
    'eq?': lambda x, y: x[0] is x[1],
    '=': lambda x, y: x[0] == x[1],
    'car': lambda x, y: x[0][0],
    'cdr': cdr,
    'cons': lambda x, y: Sentence([x[0], x[1]]),
    'number?': is_number,
    'symbol?':lambda x, y: x in y.keys(),
    'if': op_if,
    'list': op_list,
}

def define(exp:Sentence, env) -> None:
    name = exp[1]
    value = exp[2]
    if isinstance(value, Sentence):
        if value[0] == 'lambda':
            env[name] = value
        else:
            env[name] = eval(value, env)
        return
    if is_number(value):
        env[name] = to_number(value)
        return


def define_syntax(exp:Sentence, env) -> None:
    name = exp[1]
    systax_rules = exp[2]
    len_rules = len(systax_rules) - 2
    value = {}
    # ownership
    for i in range(len_rules):
        tmp_rule = systax_rules[i+2]
        args_num = len(tmp_rule[0])-1
        tmp_args = tmp_rule[0]
        tmp_args.tokens.pop(0)
        value[args_num] = Sentence(['lambda', tmp_args, tmp_rule[1]])
    env[name] = value


def apply_lambda(exp:Sentence, env):
    if isinstance(exp[0], Sentence) and exp[0][0] == 'lambda':
        lam_exp = exp[0]
        pass
    else:
        lam_exp = env[exp[0]]
    formal_parameters = lam_exp[1]
    lam_body = lam_exp[2]
    env = copy.deepcopy(env)
    for i in range(len(formal_parameters)):
        env[formal_parameters[i]] = eval(exp[i+1], env)
    return eval(lam_body, env)


def apply(exp:Sentence, env):
    func = env[exp[0]]
    len_args = len(exp) -1
    args = []
    for i in range(len_args):
        args.append(eval(exp[i+1], env))
    return func(args, env)


def eval(exp, env=TOP_ENV):
    tmp = None
    if isinstance(exp, Sentence):
        if len(exp) > 0:
            tmp = exp[0]
        else:
            return None
        if isinstance(tmp, Sentence):
            if tmp[0] == 'lambda':
                return apply_lambda(exp, env)
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
        while eval(exp[i], env) != True:
            i += 1
        return eval(exp[i+1], env)

    if tmp == 'let':
        # env = copy.deepcopy(env)
        # return
        pass

    if tmp == 'if':
        return op_if(exp, env)

    if tmp == 'begin':
        result = None
        for i in range(len(exp)-1):
            result = eval(exp[i+1])
        return result

    if tmp[0] == '\'':
        return tmp[1:]

    if env['symbol?'](tmp, env):
        # TODO: if tmp is a function then return itself
        tmp = env[tmp]
        if isinstance(tmp, Sentence) and tmp[0] == 'lambda':
            return apply_lambda(exp, env)

        if isinstance(tmp, Dict):
            args_num = len(tmp)-1
            return apply_lambda(tmp[args_num], env)

        if hasattr(tmp, '__call__'):
            return apply(exp, env)

        return tmp


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
