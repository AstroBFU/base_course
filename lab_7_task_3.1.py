import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
heart, = plt.plot([], [], '-', color = 'r', label='heart')

def heart(time):
    t = np.arange(0, 2*np.pi, 0.1)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos (3 * t) - np.cos(4 * t)
    x0 = x * time
    y0 = y * time
    return x, y

plt.axis('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def animate(i):
    heart.set_data(circle_move(time = i))
ani = FuncAnimation(fig,
                    animate,
                    frames=180,
                    interval=30
                    )
ani.save('heart')
