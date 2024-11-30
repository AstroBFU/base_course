import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 1
c = -6
x0 = -5
xk = 5
n = 100
xsd = [x for x in np.linspace(x0,0,n)]
xsp = [x for x in np.linspace(0,xk,n)]
yd = [1/i for i in xsd]
yp = [1/i for i in xsp]
plt.plot(xsd,yd) 
plt.plot(xsp,yp) 
plt.savefig('mygiperbola.png') # сохранение графика