import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
Sun, = plt.plot([], [], '-', color='gold', label='The Sun')
Earth, = plt.plot([], [], '-', color='blue', label='Earth')
circle1, = plt.plot([], [], '-', color='grey', label='-')
circle2, = plt.plot([], [], '-', color='grey', label='-')
Mars, = plt.plot([], [], '-', color='r', label='Mars')
circle3, = plt.plot([], [], '-', color='r', label='-')


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

def Mars_move(R5, alpha, R4):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x5 = np.cos(alpha)*R5
  y5 = np.sin(alpha)*R5 - R4
  ax.fill_betweenx(y5, x5, facecolor='r')
  return x5,y5

def circle3_move(R3, R4, alpha):
  alpha = np.arange(0, 3*np.pi, 0.1)
  x6 = np.cos(alpha)*(0.5*R3+0.5*R4)
  y6 = np.sin(alpha)*(0.5*R3+0.5*R4)-10
  return x6,y6

edge=150
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  Sun.set_data(Sun_move(R1=10, alpha = np.arange(0, 3*np.pi, 0.1)))
  Earth.set_data(Earth_move(R2=5, R3=50, alpha = np.arange(0, 3*np.pi, 0.1)))
  circle1.set_data(circle1_move(R3=50, alpha = np.arange(0, 3*np.pi, 0.1)))
  circle2.set_data(circle2_move(R4=70, alpha = np.arange(0, 3*np.pi, 0.1)))
  Mars.set_data(Mars_move(R5=3, R4=70, alpha = np.arange(0, 3*np.pi, 0.1)))
  circle3.set_data(circle3_move(R3=50, R4=70, alpha = np.arange(0, 3*np.pi, 0.1)))
  

ani = FuncAnimation(fig, animate, frames=180, interval=30)

ani.save('project.gif')
