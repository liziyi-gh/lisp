import copy

from tool.block import Block
from tool.parser import parse, parse_tokens
from tool.standard_enviorment import STD_ENV, to_number, define

def apply(exp, env):
    func = env[exp.child[0]]
    if func in [STD_ENV['+'], STD_ENV['-'], STD_ENV['*'], STD_ENV['/'],
                STD_ENV['cons'], ]:
        return func(eval(exp.child[1]), eval(exp.child[2]))


def eval(exp, env=STD_ENV):
    tmp = ''
    try:
        print(env['a'])
    except:
        pass
    if isinstance(exp, Block):
        for i in range(len(exp.child)):
            tmp = exp.child[i]
            if isinstance(tmp, Block):
                ret = eval(tmp, copy.deepcopy(env))
                if i == len(exp.child)-1:
                    return ret
    else:
        tmp = exp[0]
    # print(tmp)
    if env['number?'](tmp):
        return to_number(tmp)
    if tmp == 'define':
        define(exp, env)
        return
    if env['symbol?'](tmp, env):
        if hasattr(env[tmp], '__call__'):
            return apply(exp, env)
        else:
            return env(tmp)


# source = "((define a (lambda (x) x))(+ 1 (a 1)))"
source = "((+ 1 1) (+1 3))"
tokens = parse(source)
root = parse_tokens(tokens)
result = eval(root)
print(result)
