import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as plt3d

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 5
tau = np.linspace(0, years*seconds_in_year, frames)

def matrix(z, cols):
	rows = int(len(z) / cols)
	d = np.array(z).reshape((rows, cols))
	d = list(map(list, d))
	return d
  
def collision(get, m, q, rad, mainPIdx):
		mainP = get[mainPIdx]
		
		vx = mainP[1]
		vy = mainP[3]
		vz = mainP[5]
		
    r = np.sqrt((mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2 + (mainP[4] - currentP[4])**2) # Расчет расстояния между центрами частиц
		
    	# Проверка условия на столкновение: расстояние
    	# должно быть меньше 2-х радиусов
    for i in range(len(get))
    	currentP = get[i]
	    if r <= 2 * rad and i != mainPIdx:
	        # Пересчет  скорости первой частицы
	        vx = mainP[1] * (m[mainPIdx] - m[i]) / (m[mainPIdx] + m[i]) + (2) * m[i] * currentP[1] / (m[mainPIdx] + m[i])
	        vy = mainP[3] * (m[mainPIdx] - m[i]) / (m[mainPIdx] + m[i]) + (2) * m[i] * currentP[3] / (m[mainPIdx] + m[i])
	        vz = mainP[5] * (m[mainPIdx] - m[i]) / (m[mainPIdx] + m[i]) + (2) * m[i] * currentP[5] / (m[mainPIdx] + m[i])

    return vx, vy, vz

def betweens(get, m, q, mainPIdx):
   mainP = get[mainPIdx]

   Fx = []
   Fy = []
   Fz = []
   for i in range(len(get)):
      if i != mainPIdx:
         currentP = get[i]
         r = (mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2 + (mainP[4] - currentP[4])**2
            
         Fx.append((k * q[mainPIdx] * q[i] * (mainP[0] - currentP[0])) / (r ** (3/2) *  m[mainPIdx]))
         Fy.append((k * q[mainPIdx] * q[i] * (mainP[2] - currentP[2])) / (r ** (3/2) *  m[mainPIdx]))
         Fz.append((k * q[mainPIdx] * q[i] * (mainP[4] - currentP[4])) / (r ** (3/2) *  m[mainPIdx]))     

         Fx.append((-G * m[i] * (mainP[0] - currentP[0])) / r ** (3/2))
         Fy.append((-G * m[i] * (mainP[2] - currentP[2])) / r ** (3/2))
         Fz.append((-G * m[i] * (mainP[4] - currentP[4])) / r ** (3/2))

   return (sum(Fx)), (sum(Fy)), (sum(Fz))

# Определяем функцию для системы диф. уравнений
def move_func(s, t):

   get = matrix(list(s), 6)
   
   res = []
   for i in range(len(get)):
         
      axe, aye, aze = betweens(get, m, q, i)
      res.append(get[i][1]) #dxdt
      res.append(axe) #dvxdt
      res.append(get[i][3]) #dydt
      res.append(aye) #dvydt
      res.append(get[i][5]) #dzdt
      res.append(aze) #dvzdt

   return tuple(res)

# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений
AE = 149 * 10**9

s0 = (-AE, 0, 0, 0, 0, 0,
      AE, 0, 0, 0, 0, 0)


m = [10**29, 10**29]
q = [0, 0]
rad = 10*7

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

count = 2

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)
coor = []
tau = np.linspace(0, years*seconds_in_year, frames)
for k in range(frames - 1):

    t = [tau[k], tau[k+1]]
    sol = odeint(move_func, s0, t)
		
		x, y, z = [], [], []
		
		for i in range(len(get)):
			s0[6*i] = sol[1, 6*i]
			s0[6*i + 2] = sol[1, 6*i + 2]
			s0[6*i + 4] = sol[1, 6*i + 4]
			
			s0[6*i + 1] = sol[1, 6*i + 1] 
			s0[6*i + 3] = sol[1, 6*i + 3]
			s0[6*i + 5] = sol[1, 6*i + 5]
			
			get = matrix(s0, 6)
			
			x.append(s0[6*i])
			y.append(s0[6*i + 2])
			z.append(s0[6*i + 4])
			
			t = [x, y, z]
			
			s0[6*i + 1], s0[6*i + 3, s0[6*i + 5] = collision(get, m, q, rad, i)
		
		coor.append(t)

# Строим решение в виде графика и анимируем
fig = plt.figure()
ax = plt3d.Axes3D(fig)
fig.add_axes(ax)

balls = []
balls_lines = []

colors = ['r', 'g']

for i in range(count):
    balls.append(plt.plot([], [], 'o', color = colors[i]))
    balls_lines.append(plt.plot([], [], '-', color = colors[i]))

def animate(i):
   print(round(i / (frames / 100), 1), '%')
   for j in range(count):
        balls[j][0].set_data(coor[j][0][i], coor[j][1][i])
        balls[j][0].set_3d_properties(coor[j][2][i])

        balls_lines[j][0].set_data(coor[j][0][:i], coor[j][0][:i])
        balls_lines[j][0].set_3d_properties(coor[j][0][:i])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')

edge = 3 * AE
ax.set_xlim3d([-edge, edge])
ax.set_xlabel('x')
ax.set_ylim3d([-edge, edge])
ax.set_ylabel('y')
ax.set_zlim3d([-edge, edge])
ax.set_zlabel('z')


ani.save('pop.gif')