import matplotlib.pyplot as plt
import numpy as np
f= 'Parabola(p) or Giperbola(g)'
def ris(f,a=1,b=3,c=6,k=1,xa=-100,xb=100,N=10):
  x = np.arange(xa,xb,N)
  if f == 'p':
    y=a*x**2+b*x+c
    plt.title('Parabola')
  elif f == 'g':
    y = k/x
    plt.title('Giperbola')
  plt.plot(x,y)
  plt.show()
ris(f='p')