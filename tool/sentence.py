class Sentence():
    def __init__(self):
        self.tokens = []

    def add_child(self, exp):
        self.tokens.append(exp)
