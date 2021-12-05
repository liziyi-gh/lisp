class Sentence():
    def __init__(self, t):
        self.tokens = t

    def __str__(self):
        tmp = '('
        for i in range(len(self.tokens)):
            tmp += str(self.tokens[i])
            if i != len(self.tokens)-1:
                tmp += ' '
        return tmp + ')'

    def add_token(self, exp):
        self.tokens.append(exp)
