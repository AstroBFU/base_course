import matplotlib.pyplot as plt
import numpy as np
def ris(s=3,b=1,k=2):
  '''s=1(логарифмическая спираль),s=2(архимедова спираль),s=3(спираль "жезл"),s=4(роза)'''
  if s==1:
    phi=np.arange(0,8*np.pi,0.01)
    r=np.exp(b*phi)
  elif s==2:
    phi=np.arange(0,8*np.pi,0.01)
    r=k*phi
  elif s==3:
    phi=np.arange(0.01,8*np.pi,0.01)
    r=k/np.sqrt(phi)
  elif s==4:
    phi=np.arange(0,8*np.pi,0.01)
    r=np.sin(k*phi)
  x=r*np.cos(phi)
  y=r*np.sin(phi)
  plt.plot(x,y)
  plt.axis('equal')
  plt.show()
ris()