from functools import wraps
# TODO: 让 hook 的函数支持参数？看看 emacs 怎么做的，我觉得是不太可能

FUNC_HOOK_DICT = {}

class Hook():

    def __init__(self) -> None:
        self.before_hook = []
        self.after_hook = []

    def add_before_hook(self,func):
        self.before_hook.append(func)

    def add_atfer_hook(self,func):
        self.after_hook.append(func)

    def run_before_hook(self):
        for func in self.before_hook:
            func()

    def run_after_hook(self):
        for func in self.after_hook:
            func()

def find_func_hook(func) -> Hook:
    try:
        hook = FUNC_HOOK_DICT[func]
    except KeyError:
        hook = Hook()
        FUNC_HOOK_DICT[func] = hook

    return hook

def func_with_hook(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        hook = find_func_hook(wrapper)
        hook.run_before_hook()
        result = func(*args, **kwargs)
        hook.run_after_hook()
        return result

    return wrapper

@func_with_hook
def a(b):
    print(b)

def add_before_hook(func_be_hook, func):
    hook = find_func_hook(func_be_hook)
    hook.add_before_hook(func)

def add_after_hook(func_be_hook, func):
    hook = find_func_hook(func_be_hook)
    hook.add_atfer_hook(func)

def t_before():
    print("before")

def t_after():
    print("after")

add_before_hook(a, t_before)
add_after_hook(a, t_after)

a("a")
