import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 2000, 0.05)

def move_func(z, t):
    y, v = z

    dy_dt = v
    dv_dt = g - k*y/m - 0.8*v
    return dy_dt, dv_dt

m = 0.5

delta_L = 0.08
F_0 = 1
k = F_0 / delta_L

v0 = 0.5
g = 9.8
y0 = - delta_L

z0 = y0, v0

sol = odeint(move_func, z0, t)
y = sol[:, 0]
print(y)

def animate(i):
    move.set_data([0], [y[i]])
    move_line.set_data(np.full(20, 0), np.linspace(y[i], 1, 20))

fig, ax = plt.subplots()

move_line, = plt.plot([], [], '-', color='g')
move, = plt.plot([], [], 'o', color='r')
roof, = plt.plot(np.linspace(-1, 1, 20), np.full(20, 1), '-', color='0')

edge = 2
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=300, interval=50)
ani.save('extratasks givs/lab_3_extratask2_var_b.gif')
