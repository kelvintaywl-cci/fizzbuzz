import unittest

from cli import validate


class ValidateTestCase(unittest.TestCase):
    def test_passed(self):
        for case in [
            "1",
            "19",
            "300",
        ]:
            self.assertEqual(validate(case), int(case))

    def test_raises(self):
        case = "0"
        with self.assertRaises(AssertionError, msg=f"Number is not positive: {case}"):
            validate(case)

        case = "hello"
        with self.assertRaises(AssertionError, msg=f"Invalid number supplied: {case}"):
            validate(case)
