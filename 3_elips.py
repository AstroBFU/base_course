# (x**2)/(a**2)+(y**2)/(b**2) = 1
# y = +- (b**2 * (1 - (x**2)/(a**2)))

import matplotlib.pyplot as plt
import numpy as np

a = 5
b = 2

x = [i for i in np.linspace(-5,5)]
y1 = [(b**2 * (1 - (j**2)/(a**2))) for j in x]
y2 = [-(b**2 * (1 - (l**2)/(a**2))) for l in x]

plt.plot(x,y1) 
plt.plot(x,y2) 

plt.savefig('ellipse') # сохранение графика