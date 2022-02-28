import copy
from functools import reduce
from typing import Union, Any
from tool.sentence import Sentence
from tool.parser import tokenize, parse_tokens


Lisp_version = 0.03

class lispLambdaFuntion():
    def __init__(self, code:Sentence) -> None:
        self.code = code
        self.formal_parameters = code[1]
        self.parameter_num = len(self.formal_parameters)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        env = copy.deepcopy(args[1])
        parameters = args[0]
        len_parameters = len(parameters)
        if len_parameters == 0:
            return self

        if len_parameters > self.parameter_num:
            # TODO:
            print("too many args")

        if len_parameters < self.parameter_num:
            closure_env = {}
            i = 0
            new_code = copy.deepcopy(self.code)
            for para in parameters[1:1+len_parameters]:
                closure_env[self.formal_parameters[i]] = eval(para, env)
                new_code[1].pop(0)
                i += 1

            for item in new_code[2]:
                if item in closure_env:
                    item = closure_env[item]

            return lispLambdaFuntion(new_code)

        if len_parameters==self.parameter_num:
            i = 0
            for para in parameters:
                env[self.formal_parameters[i]] = eval(para, env)
                i += 1

            return eval(self.code[2], env)


class lispInternalNumberException(Exception):
    pass


def to_number(x) -> Union[int, float, complex]:
    try:
        return int(x)
    except (ValueError, TypeError):
        try:
            return float(x)
        except (ValueError, TypeError):
            try:
                return complex(x)
            except (ValueError, TypeError):
                raise lispInternalNumberException

def is_number(x) -> bool:
    try:
        _ = to_number(x)
        return True
    except lispInternalNumberException:
        return False


def lisp_op_if(args, env):
    condition = args[0]
    true_caluse = args[1]
    if len(args)>=3:
        false_caluse = args[2]
    else:
        false_caluse = None

    if eval(condition, env):
        return eval(true_caluse, env)
    else:
        return eval(false_caluse, env)


def lisp_op_add(args, env):
    return reduce(lambda x, y:eval(x, env)+eval(y, env), args)


def lisp_op_sub(args, env):
    return reduce(lambda x, y:eval(x, env)-eval(y, env), args)


def lisp_op_mul(args, env):
    return reduce(lambda x, y:eval(x, env)*eval(y, env), args)


def lisp_define(exp:Sentence, env) -> None:
    name = exp[0]
    value = exp[1]
    env[name] = eval(value, env)


def lisp_print(args, env):
    for item in args:
        print(eval(item, env))


TOP_ENV = {
    '+': lisp_op_add,
    '-': lisp_op_sub,
    '*': lisp_op_mul,
    'define': lisp_define,
    'if': lisp_op_if,
    '=': lambda x, env: eval(x[0], env) == eval(x[1], env),
    'print': lisp_print,
    # 'number?': is_number,
    # '/': lambda x, y: x[0] / x[1],
    # 'equal?': lambda x, y: x[0] == x[1],
    # 'eq?': lambda x, y: x[0] is x[1],
    # 'car': lambda x, y: x[0][0],
    # 'cdr': cdr,
    # 'cons': lambda x, y: Sentence([x[0], x[1]]),
    # 'symbol?':lambda x, y: x in y.keys(),
    # 'list': lisp_op_list,
}


def lisp_callable(element, env):
    if isinstance(element, str):
        try:
            value = env[element]
            if isinstance(value, lispLambdaFuntion):
                return True

            if callable(value):
                return True
        except KeyError:
            pass

    if isinstance(element, Sentence):
        if element[0] == 'lambda':
            return True

    return False


def apply(exp:Sentence, env):
    """
    Non-strict eval
    """
    func = eval(exp[0], env)
    args = exp[1:len(exp)]

    return func(args, env)


def eval(exp, env):
    """
    Sentence.tokens format like "+ 1 2 Sentence 5"
    """
    if isinstance(exp, Sentence):
        first_element = exp[0]
    elif isinstance(exp, str):
        first_element = exp
    elif isinstance(exp, lispLambdaFuntion):
        first_element = exp
    else:
        print("wrong type")
        print(type(exp))
        raise RuntimeError("eval first element type error")

    if is_number(first_element):
        return to_number(first_element)

    # this should place before apply function
    if isinstance(exp, str) and exp in env:
        return env[first_element]

    if lisp_callable(first_element, env):
        return apply(exp, env)

    if first_element == 'lambda':
        return lispLambdaFuntion(exp)

    return exp


def eval_source(source, env):
    tokens = tokenize(source)
    sentences = parse_tokens(tokens)[0]
    result = eval(sentences, env)
    return result


if __name__ == '__main__':
    print("Lisp interpreter Version {}".format(Lisp_version))
    env = TOP_ENV

    while True:
        print("> ", end="")
        source = input()
        result = eval_source(source, env)
        if result is not None:
            print(result)
