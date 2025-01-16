import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint as rnd

#пространство и подпространство для анимации
fig, ax = plt.subplots()

#обьект анимации
anim_object, = plt.plot([],[],'-',lw =2)
x, y = [],[] #координаты
frames_interval = np.linspace(0,10,10)

#перделы
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

def update(frame):
    alph = rnd(0,360)
    x.append(np.cos(alph))
    y.append(np.sin(alph))

    anim_object.set_data(x,y)

    return anim_object

ani = FuncAnimation(fig, #выз0ов фигуры
                    update, #вызов функции
                    frames=frames_interval,
                    interval = 10)
ani.save('animation_1.gif', writer="pillow")