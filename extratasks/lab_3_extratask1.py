import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 10000, 0.5)

def decay_func(z, t):
    A, B, C =  z
    dA_dt = - k1*A
    dB_dt = k1*A - k2*B
    dC_dt = k2*B - k3*C
    return dA_dt, dB_dt, dC_dt

k1 = 0.02
k2 = 0.05
k3 = 0.01

A0 = 500
B0 = 0
C0 = 0
z0 = A0, B0, C0

sol = odeint(decay_func, z0, t)
A = sol[:, 0]
B = sol[:, 1]
C = sol[:, 2]

def animate(i):
    A_sum.set_data([t[:i]], [A[:i]])
    B_sum.set_data([t[:i]], [B[:i]])
    C_sum.set_data([t[:i]], [C[:i]])

fig, ax = plt.subplots()

A_sum, = plt.plot([], [], '-', color='r')
B_sum, = plt.plot([], [], '-', color='g')
C_sum, = plt.plot([], [], '-', color='b')

ax.set_xlim(0, 200)
ax.set_ylim(0, 500)

ani = FuncAnimation(fig, animate, frames=300, interval=30)
ani.save('extratasks givs/lab_3_extratask1.gif')