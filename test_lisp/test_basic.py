import sys
import copy
import unittest
sys.path.append("..")
from interpreter import eval_source, TOP_ENV
env = copy.deepcopy(TOP_ENV)


class TestBasic(unittest.TestCase):
    def test_basic_add_1_1(self):
        # Given
        source = "(+ 1 1)"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 2
        assert(result == expect_result)

    def test_basic_add_1_2(self):
        # Given
        source = "(+ 1 11)"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 12
        assert(result == expect_result)

    def test_basic_add_2_2(self):
        # Given
        source = "(+ -22 22)"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 0
        assert(result == expect_result)

    def test_nest_add_1(self):
        # Given
        source = "(+ (+ 1 43) (+ -32 -1))"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 11
        assert(result == expect_result)

    def test_define_add_1(self):
        # Given
        eval_source("(define a 1)", env)
        expect_result = 2

        # When
        result = eval_source("(+ a 1)", env)

        # Then
        assert(result == expect_result)

    def test_define_add_2(self):
        # Given
        eval_source("(define a 1)", env)
        eval_source("(define b 1)", env)
        expect_result = 2

        # When
        result = eval_source("(+ a b)", env)

        # Then
        assert(result == expect_result)


    def test_if_1(self):
        # Given
        source = "(if (= (if (= 1 2) 1 2) 2) 1)"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 1
        assert(result == expect_result)

    def test_if_2(self):
        # Given
        source = "(if (= (if (= 1 2) 1 2) 1) 1 0)"

        # When
        result = eval_source(source, env)

        # Then
        expect_result = 0
        assert(result == expect_result)

    # def test_cond_1(self):
    #     # Given
    #     source = "(cond (= 1 0) 2 (= 1 1) (+ 13 -13))"
    #     # When
    #     result = eval_source(source, env)
    #     # Then
    #     expect_result = 0
    #     assert(result == expect_result)

    # def test_begin_1(self):
    #     # Given
    #     source = "(begin (+ 11 3) (- 22 22))"
    #     # When
    #     result = eval_source(source, env)
    #     # Then
    #     expect_result = 0
    #     assert(result == expect_result)

    # def test_basic_list_1(self):
    #     # Given
    #     source = "(list 1 2 3)"
    #     # When
    #     result = eval_source(source, env)
    #     # Then
    #     assert(result[0] == 1)
    #     assert(result[1] == 2)
    #     assert(result[2] == 3)

    # def test_basic_list_2(self):
    #     # Given
    #     source = "(list 1 2 (+ 1 2))"
    #     # When
    #     result = eval_source(source, env)
    #     # Then
    #     assert(result[0] == 1)
    #     assert(result[1] == 2)
    #     assert(result[2] == 3)

    # def test_basic_comma_1(self):
    #     # Given
    #     source = "(list 'abc 'e)"
    #     # When
    #     result = eval_source(source, env)
    #     # Then
    #     assert(result[0] == "abc")
    #     assert(result[1] == "e")

    # TODO: 嵌套宏
