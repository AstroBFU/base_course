import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
G = 6/67 * 10**(-11)
M = 1/9891*10**33
R = 150 * 10**9
V = 465.1013
a_earth = 
g_sat = a_earth
V_mars = 24130
R_mars = 228 * 10**9
a_mars = 
a_sat = (a_earth + a_mars)/2
T_sat = ((4*(np.pi)**2)/(G*M) * a_sat**3)**0.5
t_fly = T_sat/2


fig, ax = plt.subplots()
circle1, = plt.plot([], [], '-', color='grey', label='-')
circle2, = plt.plot([], [], '-', color='grey', label='-')
Earth, = plt.plot([], [], '-', color='blue', label='Earth')
circle3, = plt.plot([], [], '-', color='r', label='-')
Sun, = plt.plot([], [], '-', color='gold', label='The Sun')
Mars, = plt.plot([], [], 'o', color='r', label='Mars', ms=10)
Satellite, = plt.plot([], [], 'o', color='black', label='Satellite', ms=6)


def Sun_move(R1, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x1 = np.cos(alpha)*R1
  y1 = np.sin(alpha)*R1
  ax.fill_betweenx(y1, x1, facecolor='gold')
  return x1,y1

def Earth_move(R2, alpha, R3):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x2 = np.cos(alpha)*R2
  y2 = np.sin(alpha)*R2 + R3
  ax.fill_betweenx(y2, x2, facecolor='blue')
  return x2,y2

def circle1_move(R3, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x3 = np.cos(alpha)*R3
  y3 = np.sin(alpha)*R3
  return x3,y3

def circle2_move(R4, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x4 = np.cos(alpha)*R4
  y4 = np.sin(alpha)*R4
  return x4,y4

def Mars_move(R5, W, t):
  alpha = t/np.pi * 180 * W
  x5 = np.cos(alpha)*R5
  y5 = np.sin(alpha)*R5
  #ax.fill_betweenx(y5, x5, facecolor='r')
  return x5,y5

def circle3_move(R3, R4, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x6 = np.cos(alpha)*(0.5*R3+0.5*R4)
  y6 = np.sin(alpha)*(0.5*R3+0.5*R4)-10
  return x6,y6

def Satellite_move(R5, R3, W, t):
  alpha = t/np.pi * 180 * W
  y7 = R5 * (np.sin(alpha)) - R3
  x7 = R5 * (np.cos(alpha))
  #ax.fill_betweenx(y7, x7, facecolor='black')
  return x7, y7

edge=150
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  Sun.set_data(Sun_move(R1=10, alpha = np.arange(0, 3*np.pi, 0.1)))
  Earth.set_data(Earth_move(R2=5, R3=50, alpha = np.arange(0, 3*np.pi, 0.1)))
  circle1.set_data(circle1_move(R3=50, alpha = np.arange(0, 3*np.pi, 0.1)))
  circle2.set_data(circle2_move(R4=70, alpha = np.arange(0, 3*np.pi, 0.1)))
  Mars.set_data(Mars_move(R5=70, W=0.2, t=i))
  circle3.set_data(circle3_move(R3=50, R4=70, alpha = np.arange(0, 3*np.pi, 0.1)))
  Satellite.set_data(Satellite_move(R3=10, R5=60, W = 0.3, t=i))
  

ani = FuncAnimation(fig, animate, frames=np.arange(0, 3*np.pi, 0.01), interval=100)

plt.show()
#ani.save('project.gif')
