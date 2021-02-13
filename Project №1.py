import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

g = 9.81
fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2, color='g')
point, = plt.plot([], [], '*', color='r')


def lin(v0, i, a):
tp = (v0 * np.sin(a)) / g
t = np.linspace(0, 2 * tp, 500)
v0x = v0 * np.cos(a)
v0y = v0 * np.sin(a)
x = v0x * t[i]
y = v0y * t[i] - (g * t[i] ** 2) / 2
ax.set_xlim(0, np.max(x) * 1.1)
ax.set_ylim(0, np.max(y) * 1.1)
return x, y


xdata, ydata = [], []


def update(i):
xdata.append(lin(v0=1, i=i, a=30)[0])
ydata.append(lin(v0=1, i=i, a=30)[1])
anim_object.set_data(xdata, ydata)
point.set_data(lin(v0=1, i=i, a=30)[0], lin(v0=1, i=i, a=30)[1])


ani = FuncAnimation(fig,
update,
frames=400,
interval=30
)
ani.save('move_around1.gif')
