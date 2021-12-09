class Sentence():
    def __init__(self, t):
        self.tokens = t

    def __getitem__(self, idx):
        return self.tokens[idx]

    def __str__(self):
        tmp = '('
        for i in range(len(self.tokens)):
            tmp += str(self.tokens[i])
            if i != len(self.tokens)-1:
                tmp += ' '
        return tmp + ')'

    def __len__(self):
        return len(self.tokens)

    def add_token(self, exp):
        self.tokens.append(exp)
