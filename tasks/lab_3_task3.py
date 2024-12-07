import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 10000, 0.5)

def decay_func(z, t):
    A, X, Y =  z
    if A > 0:
        dX_dt = k1 * A
        dY_dt = k2 * A
        dA_dt = - dX_dt - dY_dt
    return dA_dt, dX_dt, dY_dt

A0 = 500
k1 = 0.02
k2 = 0.05

X0 = 0
Y0 = 0
z0 = A0, X0, Y0

sol = odeint(decay_func, z0, t)
X = sol[:, 1]
Y = sol[:, 2]
A = sol[:, 0]

def animate(i):
    X_el.set_data([t[:i]], [X[:i]])

    Y_el.set_data([t[:i]], [Y[:i]])

    A_el.set_data([t[:i]], [A[:i]])

fig, ax = plt.subplots()

X_el, = plt.plot([], [], '-', color='r')
Y_el, = plt.plot([], [], '-', color='g')
A_el, = plt.plot([], [], '-', color='b')

ax.set_xlim(0, 200)
ax.set_ylim(0, 500)

ani = FuncAnimation(fig, animate, frames=200, interval=30)
ani.save('lab_3_task3.gif')