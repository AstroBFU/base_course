import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

fig, ax = plt.subplots()
x = [1, 2, 3]
y = [7, 9, 7]
ax.plot(x, y, '-', lw=2, color = 'k')

t = np.linspace(np.pi/2+np.pi/6, np.pi/2-np.pi/6, 100)
x = 4 + 2 * np.cos(t)
y = 5.25 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color = 'k')

x = [5, 6, 7]
y = [7, 9, 7]
ax.plot(x, y, '-', lw=2, color = 'k')

t =  np.linspace(np.pi * 2, np.pi, 200)
x = 4 + 3 * np.cos(t)
y = 7 + 5 * np.sin(t)
ax.plot(x, y, '-', lw=2, color = 'k')

t = np.linspace(np.pi/2-np.pi/3.5,np.pi/2+np.pi/3.5, 100 )
x = 3 + 1*np.cos(t)
y = 4.75 + 1*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(-np.pi/2+np.pi/3.5,-np.pi/2-np.pi/3.5, 100 )
x = 3 + 1*np.cos(t)
y = 6 + 1*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi/2-np.pi/3.5,np.pi/2+np.pi/3.5, 100 )
x = 5 + 1*np.cos(t)
y = 4.75 + 1*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(-np.pi/2+np.pi/3.5,-np.pi/2-np.pi/3.5, 100 )
x = 5 + 1*np.cos(t)
y = 6 + 1*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(-np.pi/2,3*np.pi/2, 100 )
x = 5 + 0.2*np.cos(t)
y = 5.32 + 0.2*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(-np.pi/2,3*np.pi/2, 100 )
x = 3 + 0.2*np.cos(t)
y = 5.32 + 0.2*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi, 3*np.pi/2, 100 )
x = 4.5 + 0.5*np.cos(t)
y = 3.8 + 0.6*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(3/2*np.pi, 2*np.pi, 100 )
x = 3.5 + 0.5*np.cos(t)
y = 3.8 + 0.6*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(-np.pi/2,3*np.pi/2, 100 )
x = 4 + 0.2*np.cos(t)
y = 4 + 0.1*np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

x = [5, 6]
y = [4, 4.8]
ax.plot(x, y, '-', lw=2, color = 'k')

x = [5, 6]
y = [4, 4.1]
ax.plot(x, y, '-', lw=2, color = 'k')

x = [5, 5.9]
y = [4, 3.5]
ax.plot(x, y, '-', lw=2, color = 'k')

x = [3, 2]
y = [4, 4.8]
ax.plot(x, y, '-', lw=2, color = 'k')

x = [3, 2]
y = [4, 4.1]
ax.plot(x, y, '-', lw=2, color = 'k')

x = [3, 2.1]
y = [4, 3.5]
ax.plot(x, y, '-', lw=2, color = 'k')

plt.axis('equal')
plt.savefig('cat.png')