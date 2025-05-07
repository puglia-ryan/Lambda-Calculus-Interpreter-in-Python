import sys
from typing import List, Set, Optional, Union


class LambdaExpression:
    """
    Abstract base class for all lambda calculus expressions.
    Used as a parent for Var, Abs, and App.
    """

    pass


class Var(LambdaExpression):
    """A variable expression (e.g., x)"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Var) and self.name == other.name


class Abs(LambdaExpression):
    """A lambda abstraction (e.g., λx.M)"""

    def __init__(self, param: str, body: LambdaExpression) -> None:
        self.param = param
        self.body = body

    def __repr__(self) -> str:
        return f"(λ{self.param}.{self.body})"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Abs)
            and self.param == other.param
            and self.body == other.body
        )


class App(LambdaExpression):
    """An application of one expression to another (e.g., M N)"""

    def __init__(self, func: LambdaExpression, arg: LambdaExpression) -> None:
        self.func = func
        self.arg = arg

    def __repr__(self) -> str:
        return f"({self.func} {self.arg})"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, App) and self.func == other.func and self.arg == other.arg
        )


def free_variables(expr: LambdaExpression) -> Set[str]:
    """Returns the set of free variables in the given lambda expression"""
    if isinstance(expr, Var):
        return {expr.name}
    if isinstance(expr, Abs):
        fv = free_variables(expr.body)
        fv.discard(expr.param)
        return fv
    if isinstance(expr, App):
        return free_variables(expr.func) | free_variables(expr.arg)
    return set()


def substitute(
    term: LambdaExpression, var: str, repl: LambdaExpression
) -> LambdaExpression:
    """Performs capture-avoiding substitution of a variable in a term"""
    if isinstance(term, Var):
        return repl if term.name == var else term
    if isinstance(term, Abs):
        if term.param == var:
            return term
        return Abs(term.param, substitute(term.body, var, repl))
    if isinstance(term, App):
        return App(substitute(term.func, var, repl), substitute(term.arg, var, repl))
    return term


def alpha_conversion(abs_term: Abs, new_param: str) -> Abs:
    """Renames the bound variable in an abstraction to a new variable name"""
    return Abs(new_param, substitute(abs_term.body, abs_term.param, Var(new_param)))


def beta_reduction(term: LambdaExpression) -> Optional[LambdaExpression]:
    """Performs a single beta reduction (normal-order)"""
    if isinstance(term, App):
        if isinstance(term.func, Abs):
            return substitute(term.func.body, term.func.param, term.arg)
        left = beta_reduction(term.func)
        if left is not None:
            return App(left, term.arg)
        right = beta_reduction(term.arg)
        if right is not None:
            return App(term.func, right)
    if isinstance(term, Abs):
        reduced = beta_reduction(term.body)
        if reduced is not None:
            return Abs(term.param, reduced)
    return None


def normalise(term: LambdaExpression) -> LambdaExpression:
    """Reduces a term to its normal form using beta reduction"""
    next_term = beta_reduction(term)
    while next_term is not None:
        term = next_term
        next_term = beta_reduction(term)
    return term


def pretty_print(term: LambdaExpression) -> str:
    """Returns a string representation of the lambda expression"""
    return repr(term)


def lexer(src: str) -> List[str]:
    """Converts a source string into a list of tokens for parsing"""
    tokens = []
    i = 0
    while i < len(src):
        c = src[i]
        if c.isspace():
            i += 1
        elif c in "().λ":
            tokens.append(c)
            i += 1
        elif c.isalnum() or c in "_'":
            start = i
            while i < len(src) and (src[i].isalnum() or src[i] in "_'"):
                i += 1
            tokens.append(src[start:i])
        else:
            raise SyntaxError(f"Unexpected character: {c}")
    return tokens


class Parser:
    """Parses a token list into a lambda expression AST"""

    def __init__(self, src: str) -> None:
        self.tokens = lexer(src)
        self.pos = 0

    def peek(self) -> Optional[str]:
        """Returns the next token without consuming it"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None

    def consume(self, expected: Optional[str] = None) -> str:
        """Consumes the next token, optionally checking it matches the expected value"""
        token = self.tokens[self.pos]
        if expected and token != expected:
            raise SyntaxError(f"Expected {expected}, but got {token}")
        self.pos += 1
        return token

    def parse_atom(self) -> LambdaExpression:
        """Parses a variable or parenthesized expression"""
        token = self.peek()
        if token == "(":
            self.consume("(")
            expr = self.parse_expr()
            self.consume(")")
            return expr
        else:
            return Var(self.consume())

    def parse_expr(self) -> LambdaExpression:
        """Parses a full lambda expression: abstraction, application, or atomic term"""
        if self.peek() == "λ":
            self.consume()
            param = self.consume()
            self.consume(".")
            body = self.parse_expr()
            return Abs(param, body)
        term = self.parse_atom()
        while True:
            next_token = self.peek()
            if next_token is None or next_token == ")":
                break
            arg = self.parse_atom()
            term = App(term, arg)
        return term


def main() -> None:
    """Reads a .lam file and evaluates each line as a separate expression."""
    if len(sys.argv) != 2:
        print("Usage: python3 src/lambdaInterpreter.py lam_files/<file>.lam")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as f:
            lines = [line.strip() for line in f if line.strip()]

        for idx, line in enumerate(lines):
            print(f"\nExpression {idx + 1}: {line}")
            try:
                expr = Parser(line).parse_expr()
                nf = normalise(expr)
                print("Parsed:       ", pretty_print(expr))
                print("Normal form:  ", pretty_print(nf))
            except SyntaxError as e:
                print(f"Syntax error on line {idx + 1}: {e}")

    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
