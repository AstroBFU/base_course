import mathlotlib.pyplot as plt 
import numpy as np
def parabola_plotter(a=1,b=1,c=0,title='Parabola plotter'):
   x = np.arange(-10,10,0.01)
   y = a*x**2 + b*x + c
   plt.plot(x, y, color='g', label='luchte', marker='^', ms=5)
   plt.xlabel('coord: x')
   plt.ylabel('coord: y')
   plt.legende()
   plt.title('Base')
   plt.grid()
   plt.show() 