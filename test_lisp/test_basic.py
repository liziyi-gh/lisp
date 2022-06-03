import sys
import unittest

sys.path.append("..")
from interpreter import eval_source
from tool.lisp_enviroment import LispEnviorment, get_top_env
from tool.lisp_list import LispList
from tool import log
from test_lisp.test_helper import SimpleTestCase
from test_lisp.test_helper import run_all_simple_tests

top_env = get_top_env()


class TestBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.init_logging()

    def test_basic_add(self):
        cases = (
            SimpleTestCase("(+ 1 1)", 2, top_env),
            SimpleTestCase("(+ 1 11)", 12, top_env),
            SimpleTestCase("(+ -22 22)", 0, top_env),
            SimpleTestCase("(+ (+ 1 43) (+ -32 -1))", 11, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_minus(self):
        cases = (
            SimpleTestCase("(- 1 1)", 0, top_env),
            SimpleTestCase("(- 1 11)", -10, top_env),
            SimpleTestCase("(- -22 22)", -44, top_env),
            SimpleTestCase("(- (- 1 43) (- -32 -1))", -11, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_multiplication(self):
        cases = (
            SimpleTestCase("(* 1 1)", 1, top_env),
            SimpleTestCase("(* 1 0)", 0, top_env),
            SimpleTestCase("(* 1 11)", 11, top_env),
            SimpleTestCase("(* -22 22)", -484, top_env),
            SimpleTestCase("(* (- 1 43) (- -32 -1))", 1302, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_division(self):
        cases = (
            SimpleTestCase("(/ 1 1)", 1, top_env),
            SimpleTestCase("(/ 1 32)", 1 / 32, top_env),
            SimpleTestCase("(/ 1 11)", 1 / 11, top_env),
            SimpleTestCase("(/ -22 22)", -1, top_env),
            SimpleTestCase("(/ (- 1 43) (- -32 -1))", 42 / 31, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_car(self):
        cases = (
            SimpleTestCase("(car (cons 1 2))", 1, top_env),
            SimpleTestCase("(car (cons 0 (cons 1 2)))", 0, top_env),
            SimpleTestCase("(car (cons -1 (cons 0 (cons 1 2))))", -1, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_cdr(self):
        cases = (
            SimpleTestCase("(cdr (cons 1 2))", 2, top_env),
            SimpleTestCase("(cdr (cons 0 (cons 1 2)))", LispList([1, 2]), top_env),
            SimpleTestCase("(cdr (cdr (cons 0 (cons 1 2))))", 2, top_env),
            SimpleTestCase("(cdr (cdr (cdr (cons 0 (cons 1 (cons 2 3))))))", 3, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_equal(self):
        cases = (
            SimpleTestCase("(= 1 1)", True, top_env),
            SimpleTestCase("(= 1 32)", False, top_env),
            SimpleTestCase("(= 1 11)", False, top_env),
            SimpleTestCase("(= -22 22)", False, top_env),
            SimpleTestCase("(= (- 1 43) (- 1 43))", True, top_env),
        )

        run_all_simple_tests(self, cases)

    def test_basic_define_1(self):
        # Given
        env = LispEnviorment({}, top_env)
        expect_result = 1
        eval_source(f"(define a {expect_result})", env)

        # When
        result = eval_source("a", env)

        # Then
        assert result == expect_result

    def test_basic_define_2(self):
        # Given
        env = LispEnviorment({}, top_env)
        eval_source("(define a 1)", env)
        expect_result = 2

        # When
        result = eval_source("(+ a 1)", env)

        # Then
        assert (result == expect_result)

    def test_basic_define_3(self):
        # Given
        env = LispEnviorment({}, top_env)
        eval_source("(define a 1)", env)
        eval_source("(define b 1)", env)
        expect_result = 2

        # When
        result = eval_source("(+ a b)", env)

        # Then
        assert (result == expect_result)

    def test_cond_1(self):
        # Given
        source = "(cond (= 1 0) 2 (= 1 1) (+ 13 -13))"
        # When
        result = eval_source(source, top_env)
        # Then
        expect_result = 0
        assert (result == expect_result)

    def test_cond_2(self):
        # Given
        source = "(cond (= 1 0) 2 else (+ 13 -13))"
        # When
        result = eval_source(source, top_env)
        # Then
        expect_result = 0
        assert (result == expect_result)

    def test_apply_1(self):
        # Given
        source = "(apply (lambda (x) x) 1)"
        # When
        result = eval_source(source, top_env)
        # Then
        expect_result = 1
        assert (result == expect_result)

    def test_apply_2(self):
        # Given
        source = "(apply (lambda (x) x) 1)"
        # When
        result = eval_source(source, top_env)
        # Then
        expect_result = 1
        assert (result == expect_result)

    # def test_if_1(self):
    #     # Given
    #     source = "(if (= (if (= 1 2) 1 2) 2) 1)"

    #     # When
    #     result = eval_source(source, env)

    #     # Then
    #     expect_result = 1
    #     assert (result == expect_result)

    # def test_if_2(self):
    #     # Given
    #     source = "(if (= (if (= 1 2) 1 2) 1) 1 0)"

    #     # When
    #     result = eval_source(source, env)

    #     # Then
    #     expect_result = 0
    #     assert (result == expect_result)

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
