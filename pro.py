import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
spiral, = plt.plot([], [], 'o', color='r', label='spiral')


def spiral_move(a):
    t = 0.1 * a
    x = t * np.sin(t)
    y = t * np.cos(t)
    return x, y

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate():
    spiral.set_data(spiral_move(a = i))
ani = FuncAnimation(fig,
                    animate,
                    frames=600,
                    interval=30
                    )
ani.save('spiral.gif')