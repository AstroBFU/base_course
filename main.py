import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
point,=plt.plot([],[],'o',color='r')
def ne_circle_move(R,i):
  t=np.linspace(0,4*np.pi,500)
  x1=R*(t[i]-np.sin(t[i]))
  y1=R*(1-np.cos(t[i]))
  return x1,y1
xdata, ydata = [], [] # Координаты объекта анимации

def changer(vo,x, t,):
  x = vo*x*t
  y = vo*x*t-(10*t**2)/2
  return x,y
# print(changer())
print(changer(5,1,10))

def changer(v0,a):
 tpol = (2*v0*np.sin(a))/10
 lmax = (v0**2*np.sin(2*a))/10
 hmax = (v0**2*(np.sin(a))**2)/2*10
 return tpol, lmax,hmax
print(changer(5,80))

ax.set_xlim(0, 1*np.pi) # Пределы изменения переменной x
ax.set_ylim(0,5) # Пределы изменения переменной y
# frame - параметр
def update(frame): # Функция подстановки координат в объект анимации
  xdata.append(frame) # Расчёт координаты x
  ydata.append(np.sin(frame)) # Расчёт координать y
  anim_object.set_data(xdata, ydata) # Передача координат
  point.set_data(xdata, ydata)
  return anim_object,
ani = FuncAnimation(fig, # Стандартный вызов пространства для анимации
update, # Вызов функции подстановки координат
frames=np.arange(0, 3*np.pi, 0.1),
interval=70 # Интервал между кадрами,
) # По умолчанию 200 милисекунд
ani.save('lec_7_create_animation.gif')
