class LispList():
    def __init__(self, t):
        self.tokens = t

    def __getitem__(self, idx):
        return self.tokens[idx]

    def __str__(self):
        tmp = ''
        for item in self.tokens:
            if item == ')':
                tmp = tmp.strip() + item
                return tmp

            tmp += str(item)
            if tmp != '(':
                tmp += ' '

        return tmp

    def __len__(self):
        return len(self.tokens)

    def add_token(self, exp):
        self.tokens.append(exp)
