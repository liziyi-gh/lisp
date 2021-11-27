import operator

def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def is_number(x):
    try:
        return int(x)
    except ValueError:
        pass
    try:
        return float(x)
    except ValueError:
        pass
    try:
        return complex(x)
    except:
        pass

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

def get_nth_region(exp, n:int):
    pass



def apply(env, exp):
    func = env[exp[0]]
    if func is standard_env['+']:
        return func(eval(exp[1]), eval(exp[2]))


def eval(exp, env=standard_env):
    tmp = exp[1] if exp[0] == '(' else exp[0]
    if env['number?'](tmp):
        # TODO: float complex support
        return int(tmp)
    if env['symbol?'](tmp):
        if hasattr(env[tmp], '__call__'):
            return apply(env, exp[1:-1])
        else:
            return env(tmp)


def parse_tokens(tokens):
    pass

def parse(exp:str):
    # TODO: exp has to be one line format now
    tokens = []
    tmp = ""
    for i in range(len(exp)):
        if exp[i] == '(':
            tokens.append(exp[i])
            tmp=''
        elif exp[i] == ')':
            if exp[i-1] != ')':
                tokens.append(tmp)
            tmp=''
            tokens.append(')')
        elif exp[i] == ' ':
            tokens.append(tmp)
            tmp = ''
        else:
            tmp += exp[i]
    return tokens

source = "(+ 1 (+ 2 1))"
tokens = parse(source)
blocks = parse_tokens(tokens)
print(tokens)
print(eval(tokens))
