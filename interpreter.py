from unittest import result
from tool.sentence import Sentence
from tool.parser import parse, parse_tokens
from tool.standard_enviorment import TOP_ENV, to_number, define

def apply(exp:Sentence, env):
    tmp = exp.tokens[0]
    if isinstance(env[tmp], Sentence):
        if env[tmp].child[0] == 'lambda':
            args = env[tmp].child[1].child
            len_args = len(args)

    else:
        func = env[exp.tokens[0]]
        if func in [TOP_ENV['+'], TOP_ENV['-'], TOP_ENV['*'], TOP_ENV['/'],
                    TOP_ENV['cons'], ]:
            return func(eval(exp.tokens[1], env), eval(exp.tokens[2], env))


def eval(exp, env=TOP_ENV):
    tmp = None
    if isinstance(exp, Sentence):
        tmp = exp.tokens[0]
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
        if isinstance(env[tmp], Sentence) and env[tmp].child[0] == 'lambda':
            apply(exp, env)

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
