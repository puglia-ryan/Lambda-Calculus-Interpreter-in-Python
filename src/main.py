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
    pass


class Abs(LambdaExpression):
    pass


class App(LambdaExpression):
    pass


def main():
    file = open(sys.argv[1]).read()


if __name__ == "__main__":
    main()
