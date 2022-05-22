import unittest
from collections import namedtuple
from typing import Tuple

from interpreter import eval_source

SimpleTestCase = namedtuple('SimpleTestCase', ['source', 'expect_result', 'env'])

def run_all_simple_tests(self:unittest.TestCase, cases:Tuple[SimpleTestCase, ...]):
    for case in cases:
        with self.subTest(case=case):
            # Given

            # When
            result = eval_source(case.source, case.env)

            # Then
            assert result == case.expect_result
