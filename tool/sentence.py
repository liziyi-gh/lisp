class Sentence():
    def __init__(self, t):
        self.tokens = t

    def __str__(self):
        tmp = ''
        for i in range(len(self.tokens)):
            if isinstance(self.tokens[i], Sentence):
                tmp += str(self.tokens[i])
            tmp += str(self.tokens[i])
        return tmp

    def add_token(self, exp):
        self.tokens.append(exp)
