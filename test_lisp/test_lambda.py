import sys
import copy
import unittest

sys.path.append("..")
from interpreter import eval_source, TOP_ENV
from tool import log

env = copy.deepcopy(TOP_ENV)

def setUpModule():
    log.init_logging()


class TestLambda(unittest.TestCase):

    def test_lambda_1(self):
        # Given
        eval_source("(define a (lambda (x) x))", env)

        # When
        result = eval_source("(a 3)", env)
        expect_result = 3

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_2(self):
        # Given
        eval_source("(define self_+ (lambda (x y) (+ x y)))", env)
        expect_result = 4

        # When
        result = eval_source("(self_+ 1 3)", env)

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_3(self):
        # Given
        eval_source("(define a 3)", env)
        eval_source("(define b 4)", env)
        eval_source("(define self_+ (lambda (x y) (+ x y)))", env)
        expect_result = 7

        # When
        result = eval_source("(self_+ a b)", env)

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_4(self):
        # Given
        source = "((lambda (x) x) 123)"

        # When
        result = eval_source(source, env)
        expect_result = 123

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_5(self):
        # Given
        source = "((lambda (x) x+1) 123)"

        # When
        result = eval_source(source, env)
        expect_result = 124

        # Then
        self.assertTrue(result == expect_result)

    def test_recursive_1(self):
        # Given
        eval_source("(define accu (lambda (x) (if (= x 1) 1 (+ x (accu (- x 1))))))", env)
        result = eval_source("(accu 2)", env)

        # When
        expect_result = 3

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_1(self):
        # Given
        eval_source("(define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))", env)

        # When
        expect_result = 1
        result = eval_source("(fact 1)", env)

        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_2(self):
        # Given
        eval_source("(define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))", env)

        # When
        expect_result = 120
        result = eval_source("(fact 5)", env)

        # Then
        self.assertTrue(result == expect_result)

    def test_y_combinator(self):
        # Given
        eval_source("(define y-combinator (lambda (f) (lambda (x) (f (x x)) (lambda (x) (f (x x))))))", env)

        # When
        result = eval_source("((y-combinator (lambda (self) (lambda (n) (if (= n 1) 1 (* n (self (- n 1))))))) 3)", env)
        expect_result = 6

        # Then
        print('result is ', result)
        self.assertTrue(result == expect_result)


if __name__=="__main__":
    unittest.main()
