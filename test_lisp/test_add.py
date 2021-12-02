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
        self.assert_(result == expect_result)

    def test_basic_add_1_2(self):
        # Given
        source = "(+ 1 11)"
        # When
        result = eval_source(source)
        # Then
        expect_result = 12
        self.assert_(result == expect_result)

    def test_basic_add_2_2(self):
        # Given
        source = "(+ -22 22)"
        # When
        result = eval_source(source)
        # Then
        expect_result = 0
        self.assert_(result == expect_result)



if __name__=="__main__":
    unittest.main()
