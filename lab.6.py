from sympy.vector import CoordSys3D
from math import acos, degrees

N=CoordSys3D('N')

a=4*N.i+3*N.j+8*N.k
b=-2*N.i+8*N.j+7*N.k
c=-5*N.i-6*N.j+12*N.k

expr_1 = (a.dot(b))/(a.magnitude()*b.magnitude())
expr_2 = (a.dot(c))/(a.magnitude()*c.magnitude())
expr_3 = (b.dot(c))/(b.magnitude()*c.magnitude())

print(degrees(acos(expr_1.evalf())), degrees(acos(expr_2.evalf())), degrees(acos(expr_3.evalf())), sep='\n')