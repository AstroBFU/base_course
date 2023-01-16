import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt. subplots()
ball, = plt.plot([], [], 'o', color='g', label='Ball')

def circle_move(v0, a, t):
    v0x = v0*np.cos(a)
    v0y = v0*np.sin(a)
    x = v0x * t
    y = v0y * t - (10*t**2)/2
   
    return x, y

plt.axis('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def animate(i):
    ball.set_data(circle_move(v0 = 5, a = 30, t = i))
ani = FuncAnimation(fig,
                    animate,
                    frames=360,
                    interval=30
                    )
ani.save('proect.gif')
