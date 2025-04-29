from os import name
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


class Abs(LambdaExpression):
    def __init__(self, param, body):
        self.param = param
        self.body = body

    def __repr__(self):
        return f"(λ{self.param}.{self.body})"

class App(LambdaExpression):
    def __init__(self, func, arg):
        self.func=func
        self.arg=arg

    def __repr__(self):
        return f"({self.func} {self.arg})"

def free_variables(expr):
    pass


def substitute(term, var, repl):
    pass


def alpha_conversion(abs_term, new_param):
    pass


def beta_reduction(term):
    pass


def normalise(term):
    pass


def pretty_print(term):
    return repr(term)


class Parser:
    def __init__(self, file):
        self.file=file
        self.pos=0

    def parse_expr(self):
        pass


def main():
    file=open(sys.argv[1]).read()


if __name__ == "__main__":
    main()
