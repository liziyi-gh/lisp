import sys

class TailRecursiveOptimizeException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def TailRecursiveOptimize(func):
    """
    Suitable for side-effect-free functions
    """
    def wrapper(*args, **kwargs):
        stack = sys._getframe()
        if stack.f_back and stack.f_back.f_back.f_code == stack.f_code:
            print("rasing exception")
            raise TailRecursiveOptimizeException(args, kwargs)
        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailRecursiveOptimizeException as e:
                    args = e.args
                    kwargs = e.kwargs

    return wrapper

@TailRecursiveOptimize
def factorial(n, acc=1):
    print("real factorial")
    if n==0:
        return acc
    return factorial(n-1, n*acc)

print(factorial(3))
