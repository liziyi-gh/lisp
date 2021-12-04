import sys
import unittest
from unittest import result
sys.path.append("..")
from interpreter import eval_source

class TestLambda(unittest.TestCase):

    def test_lambda_1(self):
        # Given
        eval_source("(define a (lambda (x) x))")
        # When
        result = eval_source("(a 3)")
        expect_result = 3
        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_2(self):
        # Given
        eval_source("(define self_+ (lambda (x y) (+ x y)))")
        expect_result = 4
        # When
        result = eval_source("(self_+ 1 3)")
        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_3(self):
        # Given
        eval_source("(define a 3)")
        eval_source("(define b 4)")
        eval_source("(define self_+ (lambda (x y) (+ x y)))")
        expect_result = 7
        # When
        result = eval_source("(self_+ a b)")
        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_1(self):
        # Given
        eval_source("(define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))")
        # When
        expect_result = 1
        result = eval_source("(fact 1)")
        # Then
        self.assertTrue(result == expect_result)

    def test_lambda_fact_2(self):
        # Given
        eval_source("(define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))")
        # When
        expect_result = 5040
        result = eval_source("(fact 7)")
        # Then
        self.assertTrue(result == expect_result)


if __name__=="__main__":
    unittest.main()
