import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, plt.plot([], [], '-', color='g')

def circle_move(R):
    a = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(a)
    y = R*np.sin(a)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def animate(i):
    one.set_data(circle_move(R=0.02 * i))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('oone.gif')