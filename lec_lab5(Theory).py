from sympy import sqrt, cos, sin, pi

expr = sqrt(5) + sin(3*pi) - cos(pi/3) # Выражение.
print(expr)
print(expr * 2 + 100)



print()
from sympy import symbols

x, y, z = symbols('x y z') # Символы.
expr = sqrt(x) + sin(y) - cos(y/2) # Выражение с символами.
print(expr)

expr_subs = expr.subs(x, 2) # Заменяет нужный символ в выражении. 
print(expr_subs)

expr_subs = expr.subs([(y, pi), (x, 2)]) # Заменяет несколько символов.
print(expr_subs)

expr_evalf = expr_subs.evalf() # Решает выражение.
print(f"{expr_subs} = {expr_evalf}")



print()
from sympy import simplify

expr = sin(x)**2 + cos(x)**2

expr_simplify = simplify(expr) # Упрощает выражение.
print(f"{expr} = {expr_simplify}")

expr = 2*sin(x)*cos(x)

expr_simplify = simplify(expr)
print(f"{expr} = {expr_simplify}")

expr = (x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)

expr_simplify = simplify(expr)
print(f"{expr} = {expr_simplify}")



print()
from sympy import trigsimp

expr = cos(x)**2 - sin(x)**2

expr_trigsimp = trigsimp(expr) # Упрощает тригонометрическое выражение.
print(f"{expr} = {expr_trigsimp}")

expr = sin(x)**2 - 2*sin(x)*cos(x) + cos(x)**2

expr_trigsimp = trigsimp(expr)
print(f"{expr} = {expr_trigsimp}")



print()
from sympy import expand

expr = (x + y)**2

expr_expand = expand(expr) # Раскрывает выражение.
print(f"{expr} = {expr_expand}")

expr = (x + y)*(x - y)

expr_expand = expand(expr)
print(f"{expr} = {expr_expand}")



print()
from sympy import factor

expr = x**2 + x

expr_factor = factor(expr) # Выносит множитель
print(f"{expr} = {expr_factor}")

expr = x**3 - x**2 + x - 1

expr_factor = factor(expr)
print(f"{expr} = {expr_factor}")



print()
from sympy import solve

expr = x**2 - y

expr_solve = solve(expr, x) # Решает выражение относительно нужного символа. 
print(f"{expr}: {expr_solve}")



print()
from sympy import Eq
expr_1=x**2+2
expr_2=x**2+2
print(Eq(expr_1,expr_2))



print()
from sympy import solveset




print()
from sympy import linsolve 


exprs = [x + y + z - 1, x + y + 2*z - 3, x - 2*y + z]

exprs_linsolve = linsolve(exprs, (x, y, z))
print(f"{exprs}: {exprs_linsolve}")



print()
from sympy import nonlinsolve 

exprs = [x**2 + x, x - y]

exprs_nonlinsolve = nonlinsolve(exprs, [x, y])
print(f"{exprs}: {exprs_nonlinsolve}") 

