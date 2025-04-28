import lambdaInterpreter
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestLambdaInterpreter(unittest.TestCase):
    def test_free_variables(self):
        pass

    def test_substitute(self):
        pass

    def test_alpha_conversion(self):
        pass

    def test_beta_reduction(self):
        pass

    def test_normalise(self):
        pass

    def test_pretty_print(self):
        pass

    def test_parser(self):
        pass


if __name__ = '__main__':
    unittest.main()
