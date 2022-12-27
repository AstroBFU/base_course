import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt. subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(time):
    alpha = angle_vel * (np.pi/180) * time
    x0= R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=1, time=i))
ani = FuncAnimation(fig,
                    animate,
                    frames=180,
                    interval=30
                    )
ani.save('lec_7_standart_animation.gif')


