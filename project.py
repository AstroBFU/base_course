import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='gold', label='The Sun')

def Sun_move(R, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x = np.cos(alpha)*R
  y = np.sin(alpha)*R
  ax.fill_betweenx(y, x, facecolor='gold')
  return x,y

edge=50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
  ball.set_data(Sun_move(R=5, alpha = np.arange(0, 3*np.pi, 0.1)))

ani = FuncAnimation(fig, animate, frames=180, interval=30)



ani.save('project.gif')