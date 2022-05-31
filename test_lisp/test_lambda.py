import sys
import copy
import unittest

sys.path.append("..")
from interpreter import eval_source
from tool.lisp_enviroment import get_top_env
from tool import log
from test_lisp.test_helper import SimpleTestCase
from test_lisp.test_helper import run_all_simple_tests

env = get_top_env()


def setUpModule():
    log.init_logging()


class TestLambda(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.init_logging()

    def test_basic_lambda(self):
        cases = (
            SimpleTestCase("((lambda (x) x) 3)", 3, env),
            SimpleTestCase("((lambda (x y) (+ x y)) 1 3)", 4, env),
            SimpleTestCase("((lambda (x) x) 123)", 123, env),
            SimpleTestCase("((lambda (x) (+ x 1)) 123)", 124, env),
        )

        run_all_simple_tests(self, cases)

    def test_lambda_1(self):
        # Given
        eval_source("(define self_+ (lambda (x y) (+ x y)))", env)
        expect_result = 7

        # When
        result = eval_source("(self_+ 3 4)", env)

        # Then
        assert result == expect_result

    def test_lambda_2(self):
        # Given
        eval_source("(define self_+3 (lambda (x) (+ x 3)))", env)
        expect_result = 7

        # When
        result = eval_source("(self_+3 4)", env)

        # Then
        assert result == expect_result

    def test_recursive_1(self):
        # Given
        eval_source("(define accu (lambda (x) (cond (= x 1) 1 else (+ x (accu (- x 1))))))", env)
        result = eval_source("(accu 2)", env)

        # When
        expect_result = 3

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_1(self):
        # Given
        eval_source("(define fact (lambda (x) (cond (= x 1) 1 else (* x (fact (- x 1))))))", env)

        # When
        expect_result = 1
        result = eval_source("(fact 1)", env)

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_2(self):
        # Given
        eval_source("(define fact (lambda (x) (cond (= x 1) 1 else (* x (fact (- x 1))))))", env)

        # When
        expect_result = 120
        result = eval_source("(fact 5)", env)

        # Then
        self.assertTrue(result == expect_result)

    # def test_y_combinator(self):
    #     # Given
    #     eval_source("(define y-combinator (lambda (f) (lambda (x) (f (x x)) (lambda (x) (f (x x))))))", env)

    #     # When
    #     result = eval_source("((y-combinator (lambda (self) (lambda (n) (if (= n 1) 1 (* n (self (- n 1))))))) 3)", env)
    #     expect_result = 6

    #     # Then
    #     print('result is ', result)
    #     self.assertTrue(result == expect_result)


if __name__ == "__main__":
    unittest.main()
