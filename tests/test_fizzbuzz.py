import unittest

from fizzbuzz import fizzbuzz


class MyTestCase(unittest.TestCase):
    def test_fizz_cases(self):
        for case in [
            3,
            9,
            123,
            60003,
        ]:
            self.assertEqual(fizzbuzz(case), "FIZZ")

    def test_buzz_cases(self):
        for case in [
            5,
            100,
            100000,
            100000000,
            400000000000,
        ]:
            self.assertEqual(fizzbuzz(case), "BUZZ")

    def test_fizzbuzz_cases(self):
        for case in [15 * (n + 1) for n in range(1001)]:
            self.assertEqual(fizzbuzz(case), "FIZZBUZZ")

    def test_na_cases(self):
        for case in [
            7,
            19,
            181,
            199,
        ]:
            self.assertEqual(fizzbuzz(case), case)
