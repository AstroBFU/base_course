import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 10, 0.01)

def decay_func(z, t):
    x, y, v = z

    dx_dt = -v
    dy_dt = -v
    dv_dt = g

    return dx_dt, dy_dt, dv_dt

L = 2.5
l = 0.1
h = 1
g = 10

x0 = L - l
y0 = l
v0 = 0 

z0 = x0, y0, v0

sol = odeint(decay_func, z0, t)
x = sol[:, 0]
y = sol[:, 1]
print(x)
print(y)

def animate(i):
    if x[i] > 0:
        x_func.set_data(np.linspace(0, x[i], 20), [np.full(20, l)])
        y_func.set_data([np.full(20, 0)], np.linspace(y[i], l, 20))
    else:
        x_func.set_data([], [])
        y_func.set_data([np.full(20, 0)], np.linspace(y[i], y[i] + L, 20))

fig, ax = plt.subplots()

x_func, = plt.plot([], [], '-', color='r')
y_func, = plt.plot([], [], '-', color='r')
# table, = plt.plot(np.full(20, np.linspace(0, L, 20)), np.full(20, np.linspace(0, l, 20)), '-', color='0')

edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('extratasks givs/lab_3_extratask4.gif')