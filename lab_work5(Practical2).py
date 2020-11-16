from sympy import simplify,sqrt,symbols
a=symbols('a')

expr=(sqrt(a)-a/(sqrt(a)+1))*((a-1)/sqrt(a))

expr_simplify = simplify(expr) 
print(f"{expr} = {expr_simplify}")




