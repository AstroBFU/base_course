import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
star,=plt.plot([],[],'-',color='r',label='Star')
t=np.arange(0,4*np.pi,0.01)
x0=12*np.cos(t)+8*np.cos(1.5*t)
y0=12*np.sin(t)-8*np.sin(1.5*t)

plt.axis('equal')
ax.set_xlim(-25,25)
ax.set_ylim(-25,25)

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
ani.save('lab_7_task_3_DOP.gif')
