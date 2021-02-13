import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
frak,=plt.plot([],[],'o',color='r',label='Frak')

ax.set_xlim(-0.2,0.4)
ax.set_ylim(0,0.8)
x,y=[],[]
def first(n=100,x0=0.1,y0=0.1):
  x.append(x0)
  y.append(y0)
  C=0.3
  D=0.33
  for i in range(n):
    x_L=x[-1]
    y_L=y[-1]
    x.append(x_L**2-y_L**2+C)
    y.append(2*x_L*y_L+D)
xdata,ydata=[],[]
def update(i):
  xdata.append(x[i])
  ydata.append(y[i])
  frak.set_data(xdata,ydata)
  return frak,
first()
ani=FuncAnimation(fig,
update,
frames=100,
interval=100
)
ani.save('lab_7_task_4.gif')
