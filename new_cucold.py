import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#пространство и подпространство для анимации
fig, ax = plt.subplots()

#обьект анимации
anim_object, = plt.plot([],[],'-',lw =2)
x, y = [],[] #координаты
frames_interval = np.linspace(0,20, 100)

#перделы
ax.set_xlim(0,20)
ax.set_ylim(0,8)

def update(frame):
    x.append(frame)
    y.append(np.sin(frame))

    anim_object.set_data(x,y)

    return anim_object

ani = FuncAnimation(fig, #выз0ов фигуры
                    update, #вызов функции
                    frames=frames_interval,
                    interval = 50)
ani.save('animation_1.gif', writer="pillow")