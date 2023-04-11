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
t = np.linspace(0, years*seconds_in_year, frames)

def matrix(z, cols):
	rows = int(len(z) / cols)
	d = np.array(z).reshape((rows, cols))
	d = list(map(list, d))
	return d
  

def betweens(get, m, q, mainPIdx):
   mainP = get[mainPIdx]

   Fx = []
   Fy = []
   Fz = []
   for i in range(len(get)):
      if i != mainPIdx:
         currentP = get[i]
         r = (mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2
            
         Fx.append((k * q[mainPIdx] * q[i] * (mainP[0] - currentP[0])) / (r ** (3/2) *  m[mainPIdx]))
         Fy.append((k * q[mainPIdx] * q[i] * (mainP[2] - currentP[2])) / (r ** (3/2) *  m[mainPIdx]))
     

         Fx.append((-G * m[i] * (mainP[0] - currentP[0])) / r ** (3/2))
         Fy.append((-G * m[i] * (mainP[2] - currentP[2])) / r ** (3/2))

   return (sum(Fx)), (sum(Fy))

# Определяем функцию для системы диф. уравнений
def move_func(s, t):

   get = matrix(s, 4)
   
   res = []
   for i in range(len(get)):
         
      axe, aye = betweens(get, m, q, i)
      res.append(get[i][1]) #dxdt
      res.append(axe) #dvxdt
      res.append(get[i][3]) #dydt
      res.append(aye) #dvydt

   return tuple(res)

# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений
AE = 149 * 10**9

x10 = 0
v_x10 = 10000
y10 = 0
v_y10 = 0
z10 = 0
v_z10 = 0

x20 = 149 * 10**9
v_x20 = 0
y20 = 0
v_y20 = 0
z20 = 0
v_z20 = 10000

s0 = (0, 10000, 0, 0,
      AE, 10000, 0, 30000)

m1 = 2 * 10**30
q1 = 0

m2 = 6 * 10**24
q2 = 0

m = [m1, m2]
q = [q1, q2]

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

balls = []
balls_lines = []

for i in range(2):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))

def animate(i):
   print(round(i / (frames / 100), 1), '%')
   for j in range(2):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])

        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')

edge = 10 * AE
ax.set_xlim([-edge, edge])
ax.set_ylim([-edge, edge])


ani.save('2d.gif')