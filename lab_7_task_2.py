import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
circle, = plt.plot([], [], '-', color='r', label='Circle')

def circle_move(phi,a,t):
  alpha = a * (np.pi/180) * t
  R = alpha * t
  x = R*np.cos(phi)
  y = R*np.sin(phi)
  return x,y

edge=50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  circle.set_data(circle_move(a=1, phi=np.linspace(0, 2*np.pi, 100), t=i))
ani = FuncAnimation(fig,
animate,
frames=100,
interval=30
)
ani.save('lab_7_task_2.gif')
