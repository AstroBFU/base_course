from sympy import symbols, Abs
from sympy.solvers.inequalities import reduce_abs_inequality

x = symbols('x')

expr = Abs(x**2 + 2*x - 3) + 3*(x + 1)

print(reduce_abs_inequality(expr, '<', x))