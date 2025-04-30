import sys

# There are 3 lambda expressions which can make up a term: A varaibale,
# a lambda abstraction and an application

# LambdaExpression serves as an abstract


class LambdaExpression:
    """
    Abstract base class for each valid Lambda Expression
    """

    pass


class Var(LambdaExpression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Var) and self.name == other.name


class Abs(LambdaExpression):
    def __init__(self, param, body):
        self.param = param
        self.body = body

    def __repr__(self):
        return f"(λ{self.param}.{self.body})"


class App(LambdaExpression):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def __repr__(self):
        return f"({self.func} {self.arg})"


def free_variables(expr):
    if isinstance(expr, Var):
        return {expr.name}
    if isinstance(expr, Abs):
        fv = free_variables(expr.body)
        fv.discard(expr.param)
        return fv
    if isinstance(expr, App):
        return free_variables(expr.func) | free_variables(expr.arg)
    return set()


def substitute(term, var, repl):
    if isinstance(term, Var):
        if term.name == var:
            return repl
        return term
    if isinstance(term, Abs):
        if term.param == var:
            return term
        return Abs(term.param, substitute(term.body, var, repl))
    if isinstance(term, App):
        return App(substitute(term.func, var, repl), substitute(term.arg, var, repl))
    return term


def alpha_conversion(abs_term, new_param):
    return Abs(new_param, substitute(abs_term.body, abs_term.param, Var(new_param)))


def beta_reduction(term):
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


def normalise(term):
    next_term = beta_reduction(term)
    while next_term is not None:
        term = next_term
        next_term = beta_reduction(term)
    return term


def pretty_print(term):
    return repr(term)


# Lexer function which tokenises the input file's characters
def lexer(src):
    tokens = []
    i = 0
    while i < len(src):
        c = src[i]
        if c.isspace():
            i += 1
        elif c in "().λ\\":
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
    def __init__(self, src):
        self.tokens = lexer(src)
        self.pos = 0

    # This function allows the parser to inspect the next token without consuming it
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None

    # Consumes the next token and ensures it matches the expected value
    def consume(self, expected):
        token = self.tokens[self.pos]
        if expected and token != expected:
            raise SyntaxError(f"Expected {expected}, but got {token}")
        self.pos += 1
        return token

    def parse_expr(self):
        pass


def main():
    file = open(sys.argv[1]).read()


if __name__ == "__main__":
    main()
