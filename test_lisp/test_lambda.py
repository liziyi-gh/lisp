import sys
import unittest
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

    # def test_lambda_2(self):
    #     # Given
    #     eval_source("(define fact (lambda (x)  ))")
    #     expect_result = 6
    #     # When
    #     result = eval_source("(fact 3)")
    #     # Then
    #     self.assertTrue(result == expect_result)


if __name__=="__main__":
    unittest.main()
