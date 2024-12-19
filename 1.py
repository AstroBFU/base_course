# Импортируем библиотеки
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)
		
x, y = [], [] # Координаты объекта анимации	
frames_interval = np.linspace(-5, 5, 100)
		
ax.set_xlim(10,30) # Пределы изменения переменной Х	
ax.set_ylim(-10,10) # Пределы изменения переменной У

	

	
def cucloid_move(r,t):	
    x = r*(t-np.sin(t)**3) # Расчет координаты Х	
    y = r*(1-np.cos(t)**3) # Расчет координаты У	   
	
    return  x, y

ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')
	
frames = 180
	
coords = np.zeros((frames, 2))

	
def animate(i):
    coords[i] = cucloid_move(r=3, t = 5)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
	
    return ball, ball_line

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('cucold.gif', writer="pillow") 