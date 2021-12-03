import sys
import unittest
sys.path.append("..")
from interpreter import eval_source

class TestAdd(unittest.TestCase):

    def test_basic_add_1_1(self):
        # Given
        source = "(+ 1 1)"
        # When
        result = eval_source(source)
        # Then
        expect_result = 2
        self.assertTrue(result == expect_result)

    def test_basic_add_1_2(self):
        # Given
        source = "(+ 1 11)"
        # When
        result = eval_source(source)
        # Then
        expect_result = 12
        self.assertTrue(result == expect_result)

    def test_basic_add_2_2(self):
        # Given
        source = "(+ -22 22)"
        # When
        result = eval_source(source)
        # Then
        expect_result = 0
        self.assertTrue(result == expect_result)

    def test_nest_add_1(self):
        # Given
        source = "(+ (+ 1 43) (+ -32 -1))"
        # When
        result = eval_source(source)
        # Then
        expect_result = 11
        self.assertTrue(result == expect_result)

    def test_define_add_1(self):
        # Given
        eval_source("(define a 1)")
        expect_result = 2
        # When
        result = eval_source("(+ a 1)")
        # Then
        self.assertTrue(result == expect_result)

    def test_define_add_2(self):
        # Given
        eval_source("(define a 1)")
        eval_source("(define b 1)")
        expect_result = 2
        # When
        result = eval_source("(+ a b)")
        # Then
        self.assertTrue(result == expect_result)

if __name__=="__main__":
    unittest.main()
