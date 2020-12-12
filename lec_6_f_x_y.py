import mathlotlib.pyplot as plt 
import numpy as np
def cricle_lotter(radius=10):
   x=np.arange(-2*radius, 2*radius, 0.1)
   y = np.arange(-2*radius, 2*radius, 0.1)
   X,Y = np.meshgrid(x,y)
   fxy = X**2 + Y**2
   plt.contour(X,Y,fxy, levels=[radius**2])
   plt.axis('equal')
   plt.show()

cricle_plotter()
