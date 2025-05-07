# Lambda-Calculus-Interpreter-in-Python
### The goal of this project is to create a simple lambda-calculus interpreter in Python. The interpreter should have the following:
- A function for computing the set of free variables in a lambda expression;
- A function for substituting, in a lambda expression, all the occurrences of the formal parameter with another lambda expression;
- A function for performing α-conversion;
- A function for performing β-reduction;
- A function for reducing a lambda expression to its normal form;
- A function for pretty-printing a lambda expression.


## Syntax of the .lam files
The Python interpreter should expect  the following syntax/language in the .lam files provided to it:
  - Variables(plain names like x, n, etc..)
  - Abstractions, using the following syntax λx.M
  - Applications, using the following syntax (M N)
  - Parentheses

This info was retrieved about lambda syntax was retrieved from the Wikipedia page about lambda calculus(https://en.wikipedia.org/wiki/Lambda_calculus)
The evaluation of a lambda expression should be done by performing normal-order reduction, i.e., the outermost-leftmost term is selected for reduction at each step of the evaluation.

## How to run the program:
When running the lambdaInterpreter.py file, a valid .lam file must be provided to it as an argument
`python3 src/lambdaInterpreter.py <file>.lam"`

Some example files can be found in the lam_files directory
