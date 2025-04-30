from os.path import lexists
import unittest
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'src')
    )
)
from lambdaInterpreter import Var, Abs, App, free_variables, substitute, alpha_conversion, beta_reduction, normalise, pretty_print, lexer, Parser

class TestLambdaInterpreter(unittest.TestCase):
    def test_free_variables(self):
        self.assertEqual(free_variables(Var('x')), {'x'})

    # @unittest.skip("Not implemented yet")
    def test_substitute(self):
        # (x y)[x := (λz.z) y] => ((λz.z) y)
        expr = App(Var('x'), Var('y'))
        repl = Abs('z', Var('z'))
        result = substitute(expr, 'x', repl)
        self.assertIsInstance(result.func, Abs)
        self.assertEqual(result.arg, Var('y'))

    # @unittest.skip("Not implemented yet")
    def test_alpha_conversion(self):
        orig = Abs('x', App(Var('x'), Var('y')))
        renamed = alpha_conversion(orig, 'w')
        self.assertEqual(free_variables(renamed), {'y'})

    # @unittest.skip("Not implemented yet")
    def test_beta_reduction(self):
        # (λx.x) y => y
        expr = App(Abs('x', Var('x')), Var('y'))
        reduced = beta_reduction(expr)
        self.assertEqual(reduced, Var('y'))

    # @unittest.skip("Not implemented yet")
    def test_normalise(self):
        expr = App(Abs('x', Var('x')), Var('y'))
        nf = normalise(expr)
        self.assertEqual(pretty_print(nf), 'y')

    def test_pretty_print(self):
        expr = Abs('x', Var('x'))
        self.assertEqual(pretty_print(expr), '(λx.x)')

    def test_lexer(self):
        tokens = lexer('(λx.(x y))')
        self.assertEqual(tokens, ['(', 'λ', 'x', '.', '(', 'x', 'y', ')', ')'])

    @unittest.skip("Not implemented yet")
    def test_parser(self):
        p = Parser('x')
        self.assertEqual(p.parse_expr(), Var('x'))


if __name__ == '__main__':
    unittest.main()
