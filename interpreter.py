import copy
from unittest import result
from tool.sentence import Sentence
from tool.parser import parse, parse_tokens
from tool.standard_enviorment import TOP_ENV, is_number, to_number, is_number

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
    lambda_expression = env[exp.tokens[0]]
    len_args = len(exp.tokens) - 1
    for i in range(len_args):
        env[lambda_expression.tokens[1].tokens[i]] = eval(exp.tokens[i+1])
    return eval(lambda_expression.tokens[2], copy.deepcopy(env))


def apply(exp:Sentence, env):
    func = env[exp.tokens[0]]
    if func in [TOP_ENV['+'], TOP_ENV['-'], TOP_ENV['*'], TOP_ENV['/'],
                TOP_ENV['cons'], TOP_ENV['='], TOP_ENV['equal?'],
                TOP_ENV['eq?'], ]:
        return func(eval(exp.tokens[1], env), eval(exp.tokens[2], env))


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

    if env['symbol?'](tmp, env):
        if isinstance(env[tmp], Sentence) and env[tmp].tokens[0] == 'lambda':
            return apply_lambda(exp, env)

        if hasattr(env[tmp], '__call__'):
            return apply(exp, env)
        else:
            return env[tmp]


def eval_source(source, env=TOP_ENV):
    tokens = parse(source)
    sentences = parse_tokens(tokens)
    result = eval(sentences, env)
    return result

if __name__ == '__main__':
    print("Lisp interpreter Version 0.01")
    env = TOP_ENV
    while True:
        print("> ",end="")
        source = input()
        result = eval_source(source, env)
        if result is not None:
            print(result)
