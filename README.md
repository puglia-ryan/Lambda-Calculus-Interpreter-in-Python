# Lambda-Calculus-Interpreter-in-Python
### The goal of this project is to create a simple lambda-calculus interpreter in Python. The interpreter should have the following:
- A function for computing the set of free variables in a lambda expression;
- A function for substituting, in a lambda expression, all the occurrences of the formal parameter with another lambda expression;
- A function for performing α-conversion;
- A function for performing β-reduction;
- A function for reducing a lambda expression to its normal form;
- A function for pretty-printing a lambda expression.

The evaluation of a lambda expression should be done by performing normal-order reduction, i.e., the outermost-leftmost term is selected for reduction at each step of the evaluation.
## How to run the program:
`python3 src/lambdaInterpreter.py <file>.lam"`

Some example files can be found in the lam_files directory
