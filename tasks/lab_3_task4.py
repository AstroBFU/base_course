import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 200, 0.5)

def move_func(z, t):
    y, v = z

    dy_dt = -v
    dv_dt = g + k*y/m
    return dy_dt, dv_dt

k = 500
m = 0.8
v0 = 5
g = 9.8
y0 = 0

z0 = y0, v0

sol = odeint(move_func, z0, t)
y = sol[:, 0]
print(y)

def animate(i):
    move.set_data([0], [y[i]])
    move_line.set_data(np.full(20, 0), np.linspace(y[i], 0.4, 20))

fig, ax = plt.subplots()

move_line, = plt.plot([], [], '-', color='g')
move, = plt.plot([], [], 'o', color='r')
roof, = plt.plot(np.linspace(-0.4, 0.4, 20), np.full(20, 0.4), '-', color='0')

edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=300, interval=30)
ani.save('lab_3_task4.gif')

