import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
star,=plt.plot([],[],'-',color='r',label='Star')
t=np.arange(0,2*np.pi,0.1)
a=3
x0=y0=a**2

plt.axis('equal')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

def animate(i):
  t=0.1*i
  x=x0*np.cos(t)-y0*np.sin(t)
  y=y0*np.cos(t)+x0*np.sin(t)
  star.set_data(x,y)
  return star,
ani=FuncAnimation(fig,
animate,
frames=100,
interval=30
)
ani.save('lab_7_task_4_DOP.gif')
