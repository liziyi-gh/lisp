from tool.sentence import LispList


def find_next_brackets(tokens, begin) -> int:
    stack = 0
    while begin < len(tokens):
        if tokens[begin] == '(':
            stack += 1
        if tokens[begin] == ')':
            stack -= 1
            if stack == 0:
                return begin
        begin += 1
    return -1


def parse_tokens(tokens) -> LispList:
    root = LispList([])
    i = 0
    j = 0
    if len(tokens) == 1:
        return LispList(tokens)

    while (i < len(tokens)):
        if tokens[i] == '(':
            j = find_next_brackets(tokens, i)
            root.add_token(parse_tokens(tokens[i + 1:j]))
            i = j
        else:
            root.add_token(tokens[i])
        i = i + 1

    return root


def tokenize(exp: str) -> list:
    # TODO: exp has to be one line format now
    tokens = []
    tmp = ""
    for i in range(len(exp)):
        if exp[i] == '(':
            tokens.append(exp[i])
            tmp = ''
        elif exp[i] == ')':
            if tmp != '':
                tokens.append(tmp)
            tmp = ''
            tokens.append(')')
        elif exp[i] == ' ':
            if tmp != '':
                tokens.append(tmp)
            tmp = ''
        else:
            tmp += exp[i]
    if tmp != '':
        tokens.append(tmp)
    return tokens
