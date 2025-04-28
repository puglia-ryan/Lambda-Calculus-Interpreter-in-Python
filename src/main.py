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


class Abs(LambdaExpression):
    def __init__(self, param, body):
        self.param = param
        self.body = body


class App(LambdaExpression):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

class Parser:
    def __init__(self, file):
        self.file = file
        self.pos = 0

def main():
    file = open(sys.argv[1]).read()


if __name__ == "__main__":
    main()
