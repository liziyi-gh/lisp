from tool.sentence import Sentence

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
    root = Sentence()
    i = 0
    j = 0
    while(i<len(tokens)):
        if tokens[i] == '(':
            j = find_next_brackets(tokens, i)
            # root.exp = tokens[i:j+1]
            root.add_child(parse_tokens(tokens[i+1:j]))
            i = j
        else:
            root.add_child(tokens[i])
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
            if tmp != '':
                tokens.append(tmp)
            tmp=''
            tokens.append(')')
        elif exp[i] == ' ':
            if tmp != '':
                tokens.append(tmp)
            tmp = ''
        else:
            tmp += exp[i]
    return tokens
