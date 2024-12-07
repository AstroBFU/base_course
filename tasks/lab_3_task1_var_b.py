import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 2, frames)

def move_func(z, t):
    x, vx, y, vy = z
    
    ax = k * vx**2
    ay = k * vy**2

    dx_dt = vx
    dvx_dt = - ax
    dy_dt = vy
    dvy_dt = - g - ay
    
    return dx_dt, dvx_dt, dy_dt, dvy_dt


g = 9.8
v0 = 20
alpha = 60 * np.pi / 180
k = 0.2

x0 = 0
vx0 = v0 * np.cos(alpha)
y0 = 0
vy0 = v0 * np.sin(alpha)

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)
x = sol[:, 0]
y = sol[:, 2]

def animate(i):
    ball.set_data([x[i]], [y[i]])

    ball_line.set_data([x[:i]], [y[:i]])

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

ax.set_xlim(0, 10)
ax.set_ylim(0, 8)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_3_task1_var_b.gif')