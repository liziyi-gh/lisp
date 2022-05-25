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

    def __eq__(self, o) -> bool:
        if type(self) != type(o):
            return False

        if len(self.tokens) != len(o.tokens):
            return False

        for i, val in enumerate(self.tokens):
            if val != o.tokens[i]:
                return False

        return True

    def __hash__(self) -> int:
        return hash(repr(self))

    def add_token(self, exp):
        self.tokens.append(exp)
