import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 1000, 1)

def decay_func(z, t):
    M, h, v = z

    if M > 0:
        dM_dt = - dM0_dt
    else:
        dM_dt = 0

    dh_dt = v
    dv_dt = -u*dM_dt / (M+m) - G * M_earth/(R_earth + h)**2

    return dM_dt, dh_dt, dv_dt

h_0 = 0
v_0 = 0

M_0 = 200
m = 50
u = 3 * 1000
dM0_dt = 1

G = 6.67 * 10**(-11)
M_earth = 5.974 * 10**24
R_earth = 6378.1 * 10**3

z0 = M_0, h_0, v_0

sol = odeint(decay_func, z0, t)
h_t = sol[:, 1] / 10**3
v_t = sol[:, 2]

def animate_h(i):
    h_func.set_data([t[:i]], [h_t[:i]])

def animate_v(i):
    v_func.set_data([t[:i]], [v_t[:i]])

fig_h, ax_h = plt.subplots()

h_func, = plt.plot([], [], '-', color='r')

ax_h.set_xlim(0, 1000)
ax_h.set_ylim(0, 800)

ani_h = FuncAnimation(fig_h, animate_h, frames=1000, interval=30)
ani_h.save('extratasks givs/lab_3_extratask3_h.gif')

fig_v, ax_v = plt.subplots()

v_func, = plt.plot([], [], '-', color='g')

ax_v.set_xlim(0, 1000)
ax_v.set_ylim(0, 3000)

ani_v = FuncAnimation(fig_v, animate_v, frames=1000, interval=30)
ani_v.save('extratasks givs/lab_3_extratask3_v.gif')