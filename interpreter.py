from tool.block import Block
from tool.parser import parse, parse_tokens
from tool.standard_enviorment import STD_ENV, to_number

def apply(exp, env):
    func = env[exp.child[0]]
    if func in [STD_ENV['+'], STD_ENV['-'], STD_ENV['*'], STD_ENV['/'],
                STD_ENV['cons'], ]:
        return func(eval(exp.child[1]), eval(exp.child[2]))


def eval(exp, env=STD_ENV):
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


source = " ( + (+ 1 2 )   ( + 3 4) )"
tokens = parse(source)
root = parse_tokens(tokens)
result = eval(root)
print(result)
