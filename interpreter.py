import operator

class Block():
    def __init__(self):
        self.exp = ''
        self.child = []

    def add_child(self, exp):
        self.child.append(exp)


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

def find_next_brackets(tokens, begin)->int:
    stack = 0
    while begin<len(tokens):
        if tokens[begin] == '(':
            stack += 1
        if tokens[begin] == ')':
            stack -= 1
            if stack == 0:
                return begin
        begin += 1
    return -1


def parse_tokens(tokens):
    root = Block()
    i = 0
    j = 0
    while(i<len(tokens)):
        if tokens[i] == '(':
            j = find_next_brackets(tokens, i)
            root.exp = tokens[i:j+1]
            root.add_child(parse_tokens(tokens[i+1:j]))
            i = j
        i = i+1
    return root

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
syntax_tree = parse_tokens(tokens)
print(tokens)
# print(eval(tokens))
