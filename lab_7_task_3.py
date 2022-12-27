import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
baterfly, = plt.plot([], [], '-', color = 'r', label='Batterfly')

def batterfly(time):
   
    t = np.arange(0, 12*np.pi, 0.1)
    x = np.sin(t) * (np.e**np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
    y = np.cos(t) * (np.e**np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12)**5) 
    x0 = x * time
    y0 = y * time
    return x, y

plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    battrefly.set_data(circle_move(time = i))
ani = FuncAnimation(fig,
                    animate,
                    frames=180,
                    interval=30
                    )
ani.save('batterfly')
