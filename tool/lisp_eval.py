import logging

from tool.sentence import LispList
from tool.misc import to_number, is_number
from tool.lisp_enviroment import LispEnviorment
from tool.lisp_enviroment import Lisp_is_symbol
from tool.lisp_enviroment import Lisp_look_up
from tool.lisp_enviroment import is_primitive



class LispLambdaFunction():

    def __init__(self, exp, env: LispEnviorment) -> None:
        self.exp = exp
        self.env = env


def Lisp_eval_cond(clauses: LispList, env):
    if clauses.tokens == []:
        return LispList([])

    first_clause_result = Lisp_eval(clauses[0][0], env)

    if first_clause_result == "else":
        return Lisp_eval(clauses[0][1], env)

    if first_clause_result == False:
        Lisp_eval_cond(clauses[1:], env)
    else:
        Lisp_eval(clauses[0][1], env)


def Lisp_eval_list(l: LispList, env):
    list_tmp = []
    logging.debug(f"l in Lisp_eval_list is {l}")

    for token in l.tokens:
        token_value = Lisp_eval(token, env)
        list_tmp.append(token_value)

    return LispList(list_tmp)


def Lisp_define(exp:LispList, env:LispEnviorment):
    para_name = exp[1]
    para_value = Lisp_eval(exp[2], env)
    env.env[para_name] = para_value

    return


def create_lisp_lambda_func(exp:LispList, env: LispEnviorment) -> LispLambdaFunction:
    return LispLambdaFunction(exp, env)


def Lisp_eval(exp, env: LispEnviorment):
    if is_number(exp):
        return to_number(exp)

    if Lisp_is_symbol(exp, env):
        return Lisp_look_up(exp, env)

    if exp[0] == "QUOTE":
        return exp[1]

    if exp[0] == "lambda":
        return create_lisp_lambda_func(exp, env)

    if exp[0] == "cond":
        Lisp_eval_cond(exp[1:], env)

    if exp[0] == "define":
        Lisp_define(exp, env)

        return

    return Lisp_apply(Lisp_eval(exp[0], env), Lisp_eval_list(LispList(exp[1:]), env))


def Lisp_bind(formal_parameters:LispList, args, env:LispEnviorment)->LispEnviorment:
    new_env_dict = {}
    for i in range(len(formal_parameters)):
        new_env_dict[formal_parameters[i]] = args[i]

    return LispEnviorment(new_env_dict, env)


# Should I use object to do this?

def is_lisp_lambda_function(func:LispLambdaFunction)->bool:
    return isinstance(func, LispLambdaFunction)


def get_lambda_func_body(func:LispLambdaFunction)->LispList:
    return func.exp[2]


def get_lambda_func_formal_parameters(func:LispLambdaFunction)->LispList:
    return func.exp[1]


def get_lambda_func_env(func:LispLambdaFunction)->LispEnviorment:
    return func.env


def Lisp_apply(func, args):
    logging.debug("applying")
    if is_primitive(func):
        logging.debug("is primitive")
        return func(args)

    if is_lisp_lambda_function(func):
        logging.debug("is lambda function")
        f = get_lambda_func_body(func)
        logging.debug(f"lambda body is {f}")
        formal_parameters = get_lambda_func_formal_parameters(func)
        logging.debug(f"formal_parameters is {formal_parameters}")
        env = get_lambda_func_env(func)
        return Lisp_eval(f, Lisp_bind(formal_parameters, args, env))
