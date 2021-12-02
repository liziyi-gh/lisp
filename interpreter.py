from tool.block import Sentence
from tool.parser import parse, parse_tokens
from tool.standard_enviorment import TOP_ENV, to_number, define

def apply(exp, env):
    func = env[exp.child[0]]
    if func in [TOP_ENV['+'], TOP_ENV['-'], TOP_ENV['*'], TOP_ENV['/'],
                TOP_ENV['cons'], ]:
        return func(eval(exp.child[1], env), eval(exp.child[2], env))


def eval(exp, env=TOP_ENV):
    tmp = ''
    if isinstance(exp, Sentence):
        tmp = exp.child[0]
        if isinstance(tmp, Sentence):
            return eval(tmp, env)
    else:
        tmp = exp[0]
    if env['number?'](tmp):
        return to_number(tmp)
    if tmp == 'define':
        define(exp, env)
        return
    if env['symbol?'](tmp, env):
        if hasattr(env[tmp], '__call__'):
            print('applying')
            return apply(exp, env)
        else:
            return env(tmp)


while True:
    source = input()
    tokens = parse(source)
    root = parse_tokens(tokens)
    result = eval(root)
    print(result)
