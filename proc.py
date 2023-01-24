import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.plot([7, 7], [0, 7])
plt.axis('equal')

plt.plot([0, 0], [0.5, 7])
plt.axis('equal')

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def move(a):

    x = 7
    y = a

    return x, y

def move1():

    x = 0
    y = 2*x

    return x, y

def move2():

    x = 7
    y = 3*x

    return x, y

edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(move(a = 3))
 
ani = FuncAnimation(fig,
                    animate,
                    frames=180,
                    interval=30
                    )
 
ani.save('nnn.gif')