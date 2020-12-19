import matplotlib.pyplot as plt
import numpy as np
f='Окружность(o) или эллипс(e)'

def ris(f,rad=5,xa=-20,xb=20,N=100,a=5,b=4):
  x = np.linspace(xa,xb,N)
  y = np.linspace(xa,xb,N)
  X, Y = np.meshgrid(x,y)
  if f == 'o':
    fxy = X**2 + Y**2 - rad**2
    plt.title('Окружность')
    plt.axis('equal')
  elif f == 'e':
    fxy = X**2 / a**2 + Y**2 / b**2 - 1
    plt.title('Эллипс')
  plt.contour(X,Y,fxy,levels=[0])
  plt.show()

ris(f='e')