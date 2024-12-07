import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 50, 0.4)

def decay_func(z, t):
    T_1, T_2 = z

    dT1_dt = dT0_dt + alpha_1*(T_g-T_1) + 4*alpha_2*(T_e-T_1) + alpha_3*(T_2-T_1)
    dT2_dt = 4*alpha_2*(T_e-T_2) + alpha_1*(T_1-T_2)

    return dT1_dt, dT2_dt

T_g = 0
alpha_1 = 0.05
T_e = 20
alpha_2 = 0.02
alpha_3 = 0.01

T_10 = 10
T_20 = 20
dT0_dt = 5

z0 = T_10, T_20

sol = odeint(decay_func, z0, t)
T_1 = sol[:, 0]
T_2 = sol[:, 1]

def animate(i):
    T_1_func.set_data([t[:i]], [T_1[:i]])
    T_2_func.set_data([t[:i]], [T_2[:i]])

fig, ax = plt.subplots()

T_1_func, = plt.plot([], [], '-', color='r')
T_2_func, = plt.plot([], [], '-', color='g')

edge = 40
ax.set_xlim(0, 40)
ax.set_ylim(0, 50)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('extratasks givs/lab_3_extratask5.gif')
