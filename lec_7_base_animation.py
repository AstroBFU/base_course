import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # Координаты объекта анимации

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной x
ax.set_ylim(-1,1) # Пределы изменения переменной y
# frame - параметр
def update(frame): # Функция подстановки координат в объект анимации
  xdata.append(frame) # Расчёт координаты x
  ydata.append(np.sin(frame)) # Расчёт координать y
  anim_object.set_data(xdata, ydata) # Передача координат
  return anim_object,
ani = FuncAnimation(fig, # Стандартный вызов пространства для анимации
update, # Вызов функции подстановки координат
frames=np.arange(0, 2*np.pi, 0.1),
interval=100 # Интервал между кадрами,
) # По умолчанию 200 милисекунд
ani.save('lec_7_create_animation.gif')
